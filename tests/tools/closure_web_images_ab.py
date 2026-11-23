"""Closure: A/B check of the web copies against the originals at the real screen display sizes, then (with --apply)
switch the screen <img> references to the copies that passed. Originals stay in assets/images/ and stay declared in
data-annachy-image; a switched <img> records its source file in data-img-original.

Per image placeholder and per device-pixel-ratio (1 and 2): screenshot the placeholder's visible box with the originals,
swap every layer to its web copy, screenshot again, compare. PASS = tier 1 (raw: mean |Δ| <= 3 of 0-255 and <= 1 % of pixels
off by > 32) OR tier 2 (after a 3x3 box blur of both renders: mean |Δ| <= 2, and still <= 1 % raw pixels off by > 32).
An ASSET is switched only when every placeholder using it passes at both ratios (no page downloads both versions).
The screen frame's own clipping is lifted for the measurement, so carousel items that lie beyond the phone frame (never
visible on the screen, but still downloaded) are compared at their real rendered size too; card / tile clipping stays.
    python -I tests/tools/closure_web_images_ab.py [--apply]
"""
import base64, json, os, re, struct, sys, zlib
sys.dont_write_bytecode = True; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
from cdp_lib import Harness

WEB = json.load(open("showcase/screens/assets/images-web/manifest.json", encoding="utf-8"))
PAGES = ["showcase/screens/pdp/desktop-bg-colours.html", "showcase/screens/pdp/mobile.html", "showcase/screens/pdp/pdp-v1.html",
         "showcase/screens/sample-screen/desktop-pdp-1375-30858.html", "showcase/screens/sample-screen/mobile-pdp-1608-7090.html",
         "showcase/screens/sample-screen/mobile-putaway-1627-11756.html"]
OUT = "docs/replication/closure-image-ab-results.json"


def png(data):
    pos, idat = 8, b""
    while pos < len(data):
        n, typ = struct.unpack(">I4s", data[pos:pos + 8]); body = data[pos + 8:pos + 8 + n]; pos += 12 + n
        if typ == b"IHDR": w, h, depth, ctype = struct.unpack(">IIBB", body[:10])
        elif typ == b"IDAT": idat += body
    bpp = 4 if ctype == 6 else 3; raw, stride, prev, rows = zlib.decompress(idat), w * bpp, bytearray(w * bpp), []
    for y in range(h):
        f = raw[y * (stride + 1)]; line = bytearray(raw[y * (stride + 1) + 1:(y + 1) * (stride + 1)])
        for i in range(stride):
            a = line[i - bpp] if i >= bpp else 0; b = prev[i]; c = prev[i - bpp] if i >= bpp else 0
            if f == 1: line[i] = (line[i] + a) & 255
            elif f == 2: line[i] = (line[i] + b) & 255
            elif f == 3: line[i] = (line[i] + ((a + b) >> 1)) & 255
            elif f == 4:
                p = a + b - c; pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                line[i] = (line[i] + (a if pa <= pb and pa <= pc else b if pb <= pc else c)) & 255
        rows.append(line); prev = line
    return w, h, rows, bpp


# One placeholder's visible box. Carousel items scrolled out of view are first scrolled into view inside their own
# scroll containers (deterministic, so both phases measure the same state).
JS_BOX = """((k) => { const a = document.querySelectorAll('[data-annachy-image]')[k];
    for (let p = a.parentElement; p; p = p.parentElement) { const o = getComputedStyle(p).overflowX;
      if ((o === 'auto' || o === 'scroll') && p.scrollWidth > p.clientWidth) { const r = a.getBoundingClientRect(), q = p.getBoundingClientRect();
        if (r.left < q.left || r.right > q.right) p.scrollLeft += r.left - q.left; } }
    let r = a.getBoundingClientRect(), x0 = r.left, y0 = r.top, x1 = r.right, y1 = r.bottom;
    for (const i of a.querySelectorAll('img')) { const q = i.getBoundingClientRect(); x0 = Math.min(x0, q.left); y0 = Math.min(y0, q.top); x1 = Math.max(x1, q.right); y1 = Math.max(y1, q.bottom); }
    for (let p = a.parentElement; p; p = p.parentElement) { if (getComputedStyle(p).overflow !== 'visible') { const q = p.getBoundingClientRect();
      x0 = Math.max(x0, q.left); y0 = Math.max(y0, q.top); x1 = Math.min(x1, q.right); y1 = Math.min(y1, q.bottom); } }
    return JSON.stringify([a.dataset.figmaNode, x0 + scrollX, y0 + scrollY, x1 - x0, y1 - y0, [...a.querySelectorAll('img')].map((i) => i.getAttribute('src'))]); })"""
SWAP = """(async (to) => { const imgs = [...document.querySelectorAll('[data-annachy-image] img.scr-img__art')];
  for (const i of imgs) { const f = i.getAttribute('src').split('/').pop(); const id = f.split('.')[0];
    if (to === 'web' && WEB[id]) i.src = '../assets/images-web/' + id + '.webp';
    if (to === 'orig') i.src = '../assets/images/' + (i.dataset.imgOriginal || f); }
  await Promise.all(imgs.map((i) => i.decode().catch(() => {}))); return true; })"""

results, passed = [], {}
H = Harness(1600, 1200)
for dpr in (1, 2):
    H.call("Emulation.setDeviceMetricsOverride", width=1600, height=1200, deviceScaleFactor=dpr, mobile=False)
    for page in PAGES:
        H.navigate(page)
        H.ev("new Promise((r) => { const t = () => [...document.images].every((i) => i.complete) ? r(true) : setTimeout(t, 100); t(); })")
        H.ev("(() => { const s = document.createElement('style'); s.textContent = 'html { scrollbar-width: none !important; } .scr-frame { overflow: visible !important; }'; document.head.appendChild(s); return 1; })()")
        web_ids = {k: True for k, v in WEB.items() if v.get("kept")}
        H.ev(f"window.WEB = {json.dumps(web_ids)}; 1")
        H.ev(f"({SWAP})('orig')")
        count = H.ev("document.querySelectorAll('[data-annachy-image]').length")
        shots = {}
        for phase in ("orig", "web"):
            if phase == "web": H.ev(f"({SWAP})('web')")
            for k in range(count):
                node, x, y, w, h, srcs = json.loads(H.ev(f"({JS_BOX})({k})"))
                if not any(s.split("/").pop().split(".")[0] in web_ids for s in srcs): continue
                if w < 1 or h < 1: results.append({"page": os.path.basename(page), "node": node, "dpr": dpr, "error": "not visible"}); continue
                s = H.call("Page.captureScreenshot", format="png", captureBeyondViewport=True,
                           clip={"x": round(x), "y": round(y), "width": max(1, round(w)), "height": max(1, round(h)), "scale": 1})
                shots.setdefault(node, []).append(png(base64.b64decode(s["data"])))
        for node, pair in shots.items():
            (w1, h1, A, bpp), (w2, h2, B, _) = pair
            W_, H_ = min(w1, w2), min(h1, h2)
            n = tot = big = 0
            for y in range(H_):
                ra, rb = A[y], B[y]
                for x in range(W_):
                    i = x * bpp; d = max(abs(ra[i] - rb[i]), abs(ra[i + 1] - rb[i + 1]), abs(ra[i + 2] - rb[i + 2]))
                    tot += d; big += d > 32; n += 1
            # tier 2: 3x3 box blur of both renders (removes sub-pixel resampling / texture noise, keeps any visible change in
            # tone, crop or position), per channel; mean |delta| of the blurred images
            def blur(rows, c):   # separable 3x3 box (edges: available neighbours only)
                h1 = []
                for y in range(H_):
                    r = rows[y]; v = [r[x * bpp + c] for x in range(W_)]
                    h1.append([(v[x - 1] if x else 0) + v[x] + (v[x + 1] if x + 1 < W_ else 0) for x in range(W_)])
                cw = [(2 if x in (0, W_ - 1) else 3) if W_ > 1 else 1 for x in range(W_)]
                out = []
                for y in range(H_):
                    up, mid, dn = h1[y - 1] if y else None, h1[y], h1[y + 1] if y + 1 < H_ else None
                    ch = 1 + (up is not None) + (dn is not None)
                    out.append([(mid[x] + (up[x] if up else 0) + (dn[x] if dn else 0)) / (cw[x] * ch) for x in range(W_)])
                return out
            bt = 0
            for c in range(3):
                BA, BB = blur(A, c), blur(B, c)
                bt += sum(abs(BA[y][x] - BB[y][x]) for y in range(H_) for x in range(W_))
            bmad = bt / max(3 * n, 1)
            mad, share = tot / max(n, 1), big / max(n, 1)
            tier1 = mad <= 3 and share <= 0.01
            tier2 = bmad <= 2.0 and share <= 0.01
            results.append({"page": os.path.basename(page), "node": node, "dpr": dpr, "px": n, "meanAbsDiff": round(mad, 3),
                            "blurredMeanAbsDiff": round(bmad, 3), "pxOver32": round(share, 5), "tier1": tier1, "tier2": tier2, "pass": tier1 or tier2})
            passed.setdefault((os.path.basename(page), node), []).append(tier1 or tier2)
H.close()
bad = [r for r in results if not r.get("pass")]
cmp_ = [r for r in results if "meanAbsDiff" in r]
print(f"A/B comparisons: {len(cmp_)} (+{len(results) - len(cmp_)} not visible) · tier 1 (raw) pass {sum(r['tier1'] for r in cmp_)} · tier 2 only {sum(r['tier2'] and not r['tier1'] for r in cmp_)} · failing {len(bad)} · worst raw {max(r['meanAbsDiff'] for r in cmp_):.3f} · worst blurred {max(r['blurredMeanAbsDiff'] for r in cmp_):.3f}")
for r in bad: print("  FAIL", r)
json.dump(results, open(OUT, "w", encoding="utf-8"), indent=1)
# switch per ASSET: only when every placeholder that uses it passed at both ratios (no page loads both versions)
uses = {}
for page in PAGES:
    s_ = open(page, encoding="utf-8").read()
    for m in re.finditer(r'data-figma-node="([^"]*)"[^>]*data-annachy-image="([^"]*)"', s_):
        for f in m.group(2).split(): uses.setdefault(f.split(".")[0], []).append((os.path.basename(page), m.group(1)))
switch = sorted(aid for aid, e in WEB.items() if e.get("kept") and all(len(passed.get(u, [])) == 2 and all(passed[u]) for u in uses.get(aid, [])))
json.dump({"switched": switch, "keptOriginal": sorted(a for a, e in WEB.items() if e.get("kept") and a not in switch)},
          open("docs/replication/closure-image-switch.json", "w", encoding="utf-8"), indent=1)
print("assets switchable:", len(switch), "of", sum(1 for e in WEB.values() if e.get("kept")))
if "--apply" in sys.argv:
    n_img = 0
    for page in PAGES:
        s_ = open(page, encoding="utf-8").read()
        def sw(mm):
            global n_img
            f = mm.group(1); aid = f.split(".")[0]
            if aid not in switch: return mm.group(0)
            n_img += 1
            return f'<img class="scr-img__art" src="../assets/images-web/{aid}.webp" data-img-original="{f}"'
        s2 = re.sub(r'<img class="scr-img__art" src="\.\./assets/images/([\w.]+)"', sw, s_)
        if s2 != s_: open(page, "w", encoding="utf-8").write(s2)
    print("img elements switched to web copies:", n_img)
