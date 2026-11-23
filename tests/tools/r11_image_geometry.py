"""R11-0: record the rendered geometry of every R11 image layer (regression lock for the screen fixtures).

Each img.scr-img__art inside a [data-annachy-image] placeholder -> its border box relative to the placeholder's box
(after transforms: crops, offsets, instance scaling, ribbon rotation). Written ONLY after the one-time comparison against
Figma's own renders passed (tests/tools/r11_image_fidelity_once.py); the screen fixtures then require the same boxes.
    python -I tests/tools/r11_image_geometry.py --write     # record tests/fixtures/r11-image-geometry.json
    python -I tests/tools/r11_image_geometry.py             # print the current boxes vs the recorded ones
"""
import json, os, sys
sys.dont_write_bytecode = True; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
from cdp_lib import Harness

OUT = "tests/fixtures/r11-image-geometry.json"
PAGES = ["showcase/screens/pdp/desktop-bg-colours.html", "showcase/screens/pdp/mobile.html", "showcase/screens/pdp/pdp-v1.html",
         "showcase/screens/sample-screen/desktop-pdp-1375-30858.html", "showcase/screens/sample-screen/mobile-pdp-1608-7090.html",
         "showcase/screens/sample-screen/mobile-putaway-1627-11756.html"]
JS = """(() => { const out = {};
  for (const a of document.querySelectorAll('[data-annachy-image]')) { const A = a.getBoundingClientRect();
    out[a.dataset.figmaNode] = [...a.querySelectorAll('img.scr-img__art')].map((i) => { const r = i.getBoundingClientRect();
      return [i.dataset.imgOriginal || i.getAttribute('src').split('/').pop(),+(r.left - A.left).toFixed(2), +(r.top - A.top).toFixed(2), +r.width.toFixed(2), +r.height.toFixed(2)]; }); }
  return JSON.stringify(out); })()"""
H = Harness(1600, 1200)
H.call("Emulation.setDeviceMetricsOverride", width=1600, height=1200, deviceScaleFactor=1, mobile=False)
geo = {}
for p in PAGES:
    H.navigate(p)
    H.ev("new Promise((r) => { const t = () => [...document.images].every((i) => i.complete) ? r(true) : setTimeout(t, 100); t(); })")
    geo[os.path.basename(p)] = json.loads(H.ev(JS))
H.close()
n = sum(len(v) for v in geo.values()); layers = sum(len(x) for v in geo.values() for x in v.values())
print(f"placeholders: {n} · image layers: {layers}")
if "--write" in sys.argv:
    json.dump(geo, open(OUT, "w", encoding="utf-8"), indent=1, ensure_ascii=False); print("written", OUT)
elif os.path.exists(OUT):
    old = json.load(open(OUT, encoding="utf-8"))
    print("identical to the recorded geometry:", old == geo)
