"""R7: pixel fidelity of the normalised icon assets against the ORIGINAL Figma exports — memory-safe, resumable.

Method (one Chrome instance; one original file per batch; a fresh page per batch so memory is released):
  1. the original category export is parsed once into the page (inline SVG at 1:1) and every drawing element's box is
     measured once (getBoundingClientRect);
  2. for each variant, the ORIGINAL elements lying inside the variant's Figma box are selected purely by geometry
     (independent of the export pipeline's name pairing), cloned with their accumulated transforms into a small tile
     whose viewBox is the box, rendered at 2× the icon's true px size;
  3. the normalised library asset is rendered in a matching tile; 50 variant pairs per screenshot;
  4. ink masks (pixels clearly not white) are compared here.
  Pass: ≤ 2 % of pixels disagree and the ink area differs by ≤ 3 % (antialiasing at edges). Each batch also runs a
  negative control (a variant against a different icon's asset) that must be detected as a mismatch.

Sample: every normalised asset file once at its reference size (M, or the size of a per-size file) + one variant for every
original × style × size. Results are checkpointed per original in %TEMP%/annachy-fidelity/ — a rerun skips completed
originals (delete that folder to start over). Run from the project root:
    python -I tests/tools/r7_icon_fidelity_cdp.py [substring-of-original-path]
"""
import base64, collections, json, os, struct, sys, time, zlib
sys.dont_write_bytecode = True; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cdp_lib import Harness

PX = {"XS": 16, "S": 20, "M": 24, "L": 32, "XL": 40}
SCALE = float(os.environ.get("ANNACHY_FIDELITY_SCALE", "2"))        # render scale vs the icon's true px size
ONLY = [v for v in os.environ.get("ANNACHY_FIDELITY_ONLY", "").split(",") if v]   # re-examine specific variants (no checkpoint)
CELL = int(40 * SCALE) + 4
COLS, ROWS = max(1, 420 // CELL), max(1, 860 // CELL)     # default (2×): 84 px cells, 5 × 10 = 50 pairs per screenshot
CK = os.path.join(os.environ.get("TEMP", "."), "annachy-fidelity")
os.makedirs(CK, exist_ok=True)


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


def mask(rows, bpp, x0, y0, size):
    return [1 if max(255 - r[(x0 + x) * bpp], 255 - r[(x0 + x) * bpp + 1], 255 - r[(x0 + x) * bpp + 2]) > 64 else 0
            for r in rows[y0:y0 + size] for x in range(size)]


boxes = json.load(open("tests/tools/icons_export/variant-boxes.json", encoding="utf-8"))
flt = sys.argv[1] if len(sys.argv) > 1 else ""
pick = {}
for vid in sorted(boxes):
    b = boxes[vid]
    ref = b["normalized"].rsplit("--", 1)[1][:-4].upper() if "--" in b["normalized"] else "M"
    if b["size"] == ref: pick.setdefault(("file", b["normalized"]), vid)
for vid in sorted(boxes):
    b = boxes[vid]; pick.setdefault(("combo", b["original"], b["style"], b["size"]), vid)
by_original = collections.defaultdict(list)
for vid in (ONLY or sorted(set(pick.values()))):
    if flt in boxes[vid]["original"]: by_original[boxes[vid]["original"]].append(vid)

PAGE_JS = """window.__load = async (orig) => {
  const t = await fetch('/' + orig).then(r => r.text());
  const doc = new DOMParser().parseFromString(t, 'image/svg+xml');
  const root = document.importNode(doc.documentElement, true);
  root.removeAttribute('viewBox'); root.style.position = 'absolute'; root.style.left = '0'; root.style.top = '2000px';
  document.getElementById('src').replaceChildren(root);
  const r0 = root.getBoundingClientRect();
  window.__root = root; window.__leaves = [];
  for (const el of root.querySelectorAll('path, rect, circle, ellipse, line, polyline, polygon')) {
    if (el.closest('defs, clipPath, mask')) continue;
    const r = el.getBoundingClientRect();
    window.__leaves.push({ el, x: r.left - r0.left, y: r.top - r0.top, w: r.width, h: r.height });
  }
  return window.__leaves.length;
};
window.__tile = (i, b, size, assetText) => {
  const NS = 'http://www.w3.org/2000/svg', cell = window.__cell, col = i % window.__cols, row = Math.floor(i / window.__cols);
  const tol = Math.max(b.w, b.h) * 0.02;
  const s = document.createElementNS(NS, 'svg');
  s.setAttribute('viewBox', `${b.x} ${b.y} ${b.w} ${b.h}`); s.setAttribute('width', size); s.setAttribute('height', size);
  s.setAttribute('preserveAspectRatio', 'none');
  const rootInv = window.__root.getScreenCTM().inverse();
  const used = new Set(); let n = 0;
  for (const L of window.__leaves) {
    if (L.w === 0 && L.h === 0) continue;
    if (L.x < b.x - tol || L.y < b.y - tol || L.x + L.w > b.x + b.w + tol || L.y + L.h > b.y + b.h + tol) continue;
    const m = rootInv.multiply(L.el.getScreenCTM());
    const g = document.createElementNS(NS, 'g'); g.setAttribute('transform', `matrix(${m.a} ${m.b} ${m.c} ${m.d} ${m.e} ${m.f})`);
    const c = L.el.cloneNode(true);
    // carry inherited presentation (fill/stroke) from ancestors the clone leaves behind
    const cs = getComputedStyle(L.el);
    for (const p of ['fill', 'stroke', 'stroke-width', 'fill-rule', 'clip-rule', 'opacity', 'fill-opacity', 'stroke-opacity', 'stroke-linecap', 'stroke-linejoin'])
      if (!c.getAttribute(p)) c.setAttribute(p, cs.getPropertyValue(p));
    for (const a of ['clip-path', 'mask']) { const v = L.el.closest(`[${a}]`)?.getAttribute(a); const id = v && v.match(/#([^)]+)/)?.[1]; if (id) used.add(id); }
    g.appendChild(c); s.appendChild(g); n++;
  }
  if (used.size) { const d = document.createElementNS(NS, 'defs'); for (const id of used) { const e = window.__root.querySelector(`[id="${id}"]`); if (e) d.appendChild(e.cloneNode(true)); } s.prepend(d); }
  const o = document.getElementById('o'), a = document.getElementById('a');
  const ho = document.createElement('div'); ho.className = 'cell'; ho.style.width = ho.style.height = `${cell}px`; ho.style.left = `${col * cell}px`; ho.style.top = `${row * cell}px`; ho.appendChild(s); o.appendChild(ho);
  const ha = document.createElement('div'); ha.className = 'cell'; ha.style.width = ha.style.height = `${cell}px`; ha.style.left = `${col * cell}px`; ha.style.top = `${row * cell}px`; ha.innerHTML = assetText;
  ha.firstElementChild.setAttribute('width', size); ha.firstElementChild.setAttribute('height', size); a.appendChild(ha);
  return n;
};"""

H = Harness(1000, 900)
H.call("Emulation.setDeviceMetricsOverride", width=1000, height=900, deviceScaleFactor=1, mobile=False)
fails_all, compared, t0 = [], 0, time.time()
order = sorted(by_original.items(), key=lambda kv: len(kv[1]))
for n, (orig, vids) in enumerate(order):
    ckf = os.path.join(CK, orig.replace("/", "_") + ".json")
    if os.path.exists(ckf) and not ONLY:
        done = json.load(open(ckf, encoding="utf-8"))
        if done.get("vids") == vids:
            compared += done["compared"]; fails_all += done["fails"]
            for f in done["fails"]: H.ok(f"{f['variant']} {f['file']} {f['size']}", False, f"{f['diff']}/{f['px']} (checkpoint)")
            H.checks += done["compared"] - len(done["fails"])
            print(f"[{n + 1}/{len(order)}] {orig}: checkpoint reused ({done['compared']} variants, {len(done['fails'])} mismatches)", flush=True)
            continue
    H.navigate("tests/fixtures/r7-icon-fidelity-stage.html")
    H.ev(PAGE_JS); H.ev(f"window.__cell = {CELL}; window.__cols = {COLS}; document.querySelectorAll('#o,#a').forEach(e => e.style.width = '{COLS * CELL}px'); document.getElementById('a').style.left = '460px'")
    leaves = H.ev(f"window.__load({json.dumps(orig)})")
    H.ok(f"original loaded and measured: {orig}", isinstance(leaves, int) and leaves > 0, leaves)
    other = next((x for x in vids if boxes[x]["normalized"] != boxes[vids[0]]["normalized"]), None)
    plan = [(v, boxes[v]["normalized"], False) for v in vids] + ([(vids[0], boxes[other]["normalized"], True)] if other else [])
    fails, cnt = [], 0
    for start in range(0, len(plan), COLS * ROWS):
        chunk = plan[start:start + COLS * ROWS]
        H.ev("document.getElementById('o').textContent = ''; document.getElementById('a').textContent = ''")
        texts = H.ev("Promise.all(%s.map(f => fetch('/src/icons/' + f).then(r => r.text())))" % json.dumps([c[1] for c in chunk]))
        counts = [H.ev(f"window.__tile({i}, {json.dumps(boxes[v])}, {int(PX[boxes[v]['size']] * SCALE)}, {json.dumps(texts[i])})") for i, (v, _, _) in enumerate(chunk)]
        H.ev("new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)))")
        shot = H.call("Page.captureScreenshot", format="png", clip={"x": 0, "y": 0, "width": 900, "height": 860, "scale": 1})
        _, _, rows, bpp = png_rgb(base64.b64decode(shot["data"]))
        for i, (v, asset, control) in enumerate(chunk):
            b = boxes[v]; size = int(PX[b["size"]] * SCALE); col, row = i % COLS, i // COLS
            A = mask(rows, bpp, col * CELL, row * CELL, size); B = mask(rows, bpp, 460 + col * CELL, row * CELL, size)
            diff = sum(1 for p, q in zip(A, B) if p != q); ia, ib = sum(A), sum(B); px = size * size
            good = diff <= px * 0.02 and abs(ia - ib) <= max(2, ia * 0.03) and ia > 0 and counts[i] > 0
            if control:
                H.ok(f"negative control detects wrong artwork ({orig})", not good, f"{diff}/{px}"); continue
            H.ok(f"{v} {asset} {b['size']}", good, f"{diff}/{px} px differ, ink {ia} vs {ib}, {counts[i]} original elements")
            if not good: fails.append({"variant": v, "file": asset, "size": b["size"], "diff": diff, "px": px, "inkOriginal": ia, "inkAsset": ib, "originalElements": counts[i]})
            cnt += 1
    if not ONLY: json.dump({"vids": vids, "compared": cnt, "fails": fails}, open(ckf, "w", encoding="utf-8"))
    compared += cnt; fails_all += fails
    print(f"[{n + 1}/{len(order)}] {orig}: {cnt} variants, {len(fails)} mismatches ({time.time() - t0:.0f}s)", flush=True)
print(f"compared {compared} variants · stage-1 (2x) mismatches {len(fails_all)} · checkpoints: {CK}")
H.chrome_done = H.close()
# Figma defects: the Figma variant box itself is empty (no original element inside it) and so is the asset.
defects = [f for f in fails_all if f["originalElements"] == 0 and f["inkOriginal"] == 0 and f["inkAsset"] == 0]
rest = [f for f in fails_all if f not in defects]
for f in defects: print("  FIGMA DEFECT (artwork outside its variant frame in Figma):", f["variant"], f["file"])
code = 0 if not rest else 1
if rest and not ONLY and SCALE < 8:
    # Stage 2: re-examine stage-1 mismatches at 8x, where antialiasing of thin strokes no longer dominates.
    import subprocess
    env = dict(os.environ, ANNACHY_FIDELITY_SCALE="8", ANNACHY_FIDELITY_ONLY=",".join(f["variant"] for f in rest))
    r = subprocess.run([sys.executable, "-I", os.path.abspath(__file__)], env=env, capture_output=True, text=True, encoding="utf-8")
    print("STAGE 2 (8x) re-examination of", len(rest), "variants:")
    for l in r.stdout.splitlines():
        if "MISMATCH" in l or "compared" in l or "RESULT" in l: print("  " + l)
    code = r.returncode
print(f"VERDICT: {compared} variants compared · {len(defects)} Figma defects (reported) · {len(rest)} stage-1 mismatches → stage 2 {'PASS' if code == 0 else 'FAIL'}")
print("R7 ICON FIDELITY RESULT:", "PASS" if code == 0 else "FAIL")
sys.exit(code)
