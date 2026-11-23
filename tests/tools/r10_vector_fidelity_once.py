"""R10-0 one-time fidelity check (needs the export staging folder; run before staging cleanup).

1. Integrity: every delivered file in showcase/screens/assets/vectors/ is byte-identical to its staged Figma export.
2. Pixel fidelity: for the 22 direct exports, the delivered artwork (download_assets) is rasterised at 4x next to Figma's
   independent design-context rendering of the same node, and their ink masks are compared (one Chrome instance).
   The 6 asset-URL artworks ARE the design-context renderings (no second reference exists).
Run from the project root: python -I tests/tools/r10_vector_fidelity_once.py
"""
import base64, hashlib, json, os, sys
sys.dont_write_bytecode = True; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cdp_lib import Harness
import struct, zlib


def png_rgb(data):
    """Minimal PNG decoder (8-bit RGB/RGBA, non-interlaced — what Chrome emits). Returns (w, h, list of row bytearrays, bpp)."""
    assert data[:8] == b"\x89PNG\r\n\x1a\n"
    pos, idat = 8, b""
    while pos < len(data):
        n, typ = struct.unpack(">I4s", data[pos:pos + 8]); body = data[pos + 8:pos + 8 + n]; pos += 12 + n
        if typ == b"IHDR": w, h, depth, ctype, _, _, inter = struct.unpack(">IIBBBBB", body); assert depth == 8 and ctype in (2, 6) and inter == 0
        elif typ == b"IDAT": idat += body
        elif typ == b"IEND": break
    bpp = 4 if ctype == 6 else 3
    raw, stride, rows, prev = zlib.decompress(idat), w * bpp, [], bytearray(w * bpp)
    for y in range(h):
        f, line = raw[y * (stride + 1)], bytearray(raw[y * (stride + 1) + 1:(y + 1) * (stride + 1)])
        if f == 1:
            for i in range(bpp, stride): line[i] = (line[i] + line[i - bpp]) & 255
        elif f == 2:
            for i in range(stride): line[i] = (line[i] + prev[i]) & 255
        elif f == 3:
            for i in range(stride): line[i] = (line[i] + (((line[i - bpp] if i >= bpp else 0) + prev[i]) >> 1)) & 255
        elif f == 4:
            for i in range(stride):
                a = line[i - bpp] if i >= bpp else 0; b = prev[i]; c = prev[i - bpp] if i >= bpp else 0
                p = a + b - c; pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                line[i] = (line[i] + (a if pa <= pb and pa <= pc else b if pb <= pc else c)) & 255
        rows.append(line); prev = line
    return w, h, rows, bpp


ST = os.path.join(os.environ["TEMP"], "annachy-vector-staging")
M = json.load(open("docs/figma-audit/r10-0-structural-vector-manifest.json", encoding="utf-8"))
R = {a["artworkId"]: a for a in json.load(open(os.path.join(ST, "export-report.json"), encoding="utf-8"))["artworks"]}
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
H = Harness(1200, 900)
H.call("Emulation.setDeviceMetricsOverride", width=1200, height=900, deviceScaleFactor=1, mobile=False)
results = []
for a in M["artworks"]:
    aid = a["artworkId"]
    H.ok(f"{aid} delivered file byte-identical to its Figma export", sha(a["destination"]) == sha(os.path.join(ST, f"{aid}-asset-1.svg")))
H.navigate("tests/fixtures/r7-icon-fidelity-stage.html")
for a in M["artworks"]:
    aid = a["artworkId"]; dc = os.path.join(ST, f"{aid}-dc.svg")
    if not os.path.exists(dc):
        results.append({"artwork": aid, "result": "no independent reference (the delivered file is Figma's design-context rendering)"}); continue
    w, h = float(R[aid]["svg"]["width"]), float(R[aid]["svg"]["height"])
    k = max(1, min(4, 1100 / max(w, 1)))           # 4x, capped to fit the 1200px viewport
    W, Hh = max(1, round(w * k)), max(1, round(h * k))
    t1 = open(a["destination"], encoding="utf-8").read(); t2 = open(dc, encoding="utf-8").read()
    H.ev("document.body.innerHTML = ''")
    H.ev(f"""(async () => {{
      const mk = (txt, top) => new Promise(r => {{ const i = new Image(); i.onload = r; i.onerror = r; i.style.cssText = `position:absolute;left:0;top:${{top}}px;width:{W}px;height:{Hh}px;background:#fff`;
        i.src = URL.createObjectURL(new Blob([txt], {{ type: 'image/svg+xml' }})); document.body.appendChild(i); }});
      document.body.style.background = '#fff';
      await mk({json.dumps(t1)}, 0); await mk({json.dumps(t2)}, {Hh + 20});
      await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))); return true; }})()""")
    shot = H.call("Page.captureScreenshot", format="png", clip={"x": 0, "y": 0, "width": W, "height": 2 * Hh + 20, "scale": 1})
    _, _, rows, bpp = png_rgb(base64.b64decode(shot["data"]))
    # exact colour comparison: a pixel differs when any channel differs by > 8/255 (detects even near-white strokes);
    # "ink" = pixels that are not pure background (any channel < 252)
    pix = lambda y0: [tuple(r[x * bpp:x * bpp + 3]) for r in rows[y0:y0 + Hh] for x in range(W)]
    A, B = pix(0), pix(Hh + 20)
    diff = sum(1 for p, q in zip(A, B) if max(abs(p[0] - q[0]), abs(p[1] - q[1]), abs(p[2] - q[2])) > 8)
    ia, ib = sum(1 for p in A if min(p) < 252), sum(1 for p in B if min(p) < 252)
    px = W * Hh
    same = diff <= max(2, px * 0.01)
    results.append({"artwork": aid, "renderPx": [W, Hh], "inkDelivered": ia, "inkFigmaReference": ib, "diffPx": diff, "match": same})
    H.ok(f"{aid} matches Figma's independent rendering (≤1% px)", same and (ia > 0 or ib == 0), f"{diff}/{px} px differ, ink {ia} vs {ib}")
json.dump(results, open(os.path.join(ST, "fidelity-results.json"), "w"), indent=1)
for r in results: print(" ", r)
sys.exit(H.finish("R10 VECTOR FIDELITY"))
