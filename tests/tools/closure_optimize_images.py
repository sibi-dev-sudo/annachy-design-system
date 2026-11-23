"""Closure: web-delivery copies of the R11 raster originals (originals are never modified).

For each PNG/JPEG in showcase/screens/assets/images/ the largest rendered size on any screen is read from the R11 geometry lock
(tests/fixtures/r11-image-geometry.json, CSS px, after crops / instance scaling). The copy is resized to cover that size at
device-pixel-ratio 2 (never enlarged beyond the original) and encoded as WebP by Chrome's own encoder (alpha preserved).
Output: showcase/screens/assets/images-web/<assetId>.webp + manifest.json. Existing copies are never overwritten
(delete a copy deliberately to regenerate it). A copy that is not smaller than its original is not kept.
    python -I tests/tools/closure_optimize_images.py [--quality 0.86]
"""
import base64, hashlib, json, math, os, struct, sys
sys.dont_write_bytecode = True; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
from cdp_lib import Harness

SRC, OUT = "showcase/screens/assets/images", "showcase/screens/assets/images-web"
DPR = float(sys.argv[sys.argv.index("--dpr") + 1]) if "--dpr" in sys.argv else 2
Q = float(sys.argv[sys.argv.index("--quality") + 1]) if "--quality" in sys.argv else 0.86
GEO = json.load(open("tests/fixtures/r11-image-geometry.json", encoding="utf-8"))


def natural(path):
    b = open(path, "rb").read()
    if b.startswith(b"\x89PNG"): return struct.unpack(">II", b[16:24])
    i = 2
    while i < len(b):
        m, L = b[i + 1], int.from_bytes(b[i + 2:i + 4], "big")
        if 0xC0 <= m <= 0xCF and m not in (0xC4, 0xC8, 0xCC):
            h, w = struct.unpack(">HH", b[i + 5:i + 9]); return w, h
        i += 2 + L
    raise ValueError(path)


need = {}                                         # file -> largest scale factor needed (relative to natural size)
for page in GEO.values():
    for layers in page.values():
        for f, x, y, w, h in layers:
            if f.endswith(".svg"): continue
            nw, nh = natural(os.path.join(SRC, f))
            need[f] = max(need.get(f, 0), DPR * w / nw, DPR * h / nh)
os.makedirs(OUT, exist_ok=True)
manifest_path = os.path.join(OUT, "manifest.json")
manifest = json.load(open(manifest_path, encoding="utf-8")) if os.path.exists(manifest_path) else {}
H = Harness(1200, 900)
H.navigate("tests/fixtures/r7-icon-fidelity-stage.html")
sha = lambda b: hashlib.sha256(b).hexdigest()
for f in sorted(need):
    aid = f.split(".")[0]; dst = os.path.join(OUT, aid + ".webp")
    src_b = open(os.path.join(SRC, f), "rb").read(); nw, nh = natural(os.path.join(SRC, f))
    s = min(1.0, need[f])
    if s >= 1.0: tw, th = nw, nh
    else:   # keep the original aspect ratio as exactly as possible (object-fit: cover crops depend on it): search a few px up
        base = max(1, math.ceil(nw * s))
        tw = min(range(base, min(nw, base + 24) + 1), key=lambda w: abs(w * nh / nw - round(w * nh / nw)))
        th = max(1, round(tw * nh / nw))
    if os.path.exists(dst):
        print("exists, kept:", dst); continue
    data = H.ev(f"""(async () => {{
      const img = new Image(); img.src = '/{SRC}/{f}'; await img.decode();
      const bmp = await createImageBitmap(img, {{ resizeWidth: {tw}, resizeHeight: {th}, resizeQuality: 'high' }});
      const c = document.createElement('canvas'); c.width = {tw}; c.height = {th};
      c.getContext('2d', {{ colorSpace: 'srgb' }}).drawImage(bmp, 0, 0);
      const blob = await new Promise((r) => c.toBlob(r, 'image/webp', {Q}));
      const buf = new Uint8Array(await blob.arrayBuffer()); let s = ''; for (let i = 0; i < buf.length; i += 32768) s += String.fromCharCode(...buf.subarray(i, i + 32768));
      return blob.type + ':' + btoa(s); }})()""")
    typ, b64 = data.split(":", 1); out_b = base64.b64decode(b64)
    assert typ == "image/webp" and out_b[8:12] == b"WEBP", (f, typ)
    entry = {"original": f"{SRC}/{f}", "originalBytes": len(src_b), "originalPx": [nw, nh], "originalSha256": sha(src_b),
             "webPx": [tw, th], "scale": round(s, 4), "quality": Q, "dpr": DPR}
    if len(out_b) >= len(src_b):
        entry.update({"kept": False, "reason": f"WebP ({len(out_b)} B) not smaller than the original"}); manifest[aid] = entry
        print(f"{f}: not smaller, original stays"); continue
    open(dst, "wb").write(out_b)
    entry.update({"kept": True, "web": dst.replace(os.sep, "/"), "webBytes": len(out_b), "webSha256": sha(out_b)}); manifest[aid] = entry
    print(f"{f}: {nw}x{nh} {len(src_b):,} B -> {tw}x{th} {len(out_b):,} B")
H.close()
json.dump(manifest, open(manifest_path, "w", encoding="utf-8"), indent=1)
k = [m for m in manifest.values() if m.get("kept")]
print(f"copies: {len(k)} · originals {sum(m['originalBytes'] for m in manifest.values()):,} B · web {sum(m['webBytes'] for m in k) + sum(m['originalBytes'] for m in manifest.values() if not m.get('kept')):,} B")
