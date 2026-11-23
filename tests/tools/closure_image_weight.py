"""Closure: image weight per screen, before (R11 originals) and after (web copies where A/B-verified), plus a real load.

Static: unique image files each screen references (R11 originals vs current references; vectors included).
Measured: each screen loaded in Chrome (local HTTP, cache disabled): image requests, encoded bytes, failed image requests,
load-event time, for the CURRENT references and with every web copy swapped back to its original (before).
Writes docs/replication/closure-image-weight.json.   python -I tests/tools/closure_image_weight.py
"""
import json, os, re, sys, time
sys.dont_write_bytecode = True; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
from cdp_lib import Harness

PAGES = ["showcase/screens/pdp/desktop-bg-colours.html", "showcase/screens/pdp/mobile.html", "showcase/screens/pdp/pdp-v1.html",
         "showcase/screens/sample-screen/desktop-pdp-1375-30858.html", "showcase/screens/sample-screen/mobile-pdp-1608-7090.html",
         "showcase/screens/sample-screen/mobile-putaway-1627-11756.html", "showcase/screens/sample-screen/job-listing-page-1629-11987.html",
         "showcase/screens/sample-screen/desktop-1608-9891.html"]
size = lambda p: os.path.getsize(p) if os.path.exists(p) else 0
out = {"pages": {}}
for p in PAGES:
    s = open(p, encoding="utf-8").read(); d = os.path.dirname(p)
    now = set(re.findall(r'<img[^>]*\bsrc="([^"]+)"', s))
    before = set()
    for src in now:
        m = re.search(r'data-img-original="([^"]+)"', s[s.find(src) - 10:s.find(src) + 300])
        before.add("../assets/images/" + m.group(1) if "images-web/" in src and m else src)
    nb = sum(size(os.path.normpath(os.path.join(d, x))) for x in now); bb = sum(size(os.path.normpath(os.path.join(d, x))) for x in before)
    out["pages"][os.path.basename(p)] = {"staticFiles": len(now), "bytesBefore": bb, "bytesAfter": nb}

H = Harness(1600, 1200)
H.call("Network.setCacheDisabled", cacheDisabled=True)
def load(page, swap_back):
    H.events.clear(); t0 = time.time()
    H.navigate(page)
    if swap_back:
        H.events.clear()
        H.ev("""(async () => { const im = [...document.querySelectorAll('img[data-img-original]')]; for (const i of im) i.src = '../assets/images/' + i.dataset.imgOriginal;
          await Promise.all(im.map((i) => i.decode().catch(() => {}))); return true; })()""")
    else:
        H.ev("new Promise((r) => { const t = () => [...document.images].every((i) => i.complete) ? r(true) : setTimeout(t, 50); t(); })")
    ms = (time.time() - t0) * 1000
    reqs = {e["params"]["requestId"]: e["params"]["request"]["url"] for e in H.events if e.get("method") == "Network.requestWillBeSent"}
    img = {rid for rid, u in reqs.items() if re.search(r"\.(png|jpe?g|webp|svg)(\?|$)", u)}
    fin = {e["params"]["requestId"]: e["params"]["encodedDataLength"] for e in H.events if e.get("method") == "Network.loadingFinished"}
    failed = [reqs[e["params"]["requestId"]] for e in H.events if e.get("method") == "Network.loadingFailed" and e["params"]["requestId"] in img]
    return {"imageRequests": len(img), "imageBytes": sum(fin.get(r, 0) for r in img), "failedImageRequests": failed, "wallMs": round(ms)}
for p in PAGES[:6]:
    a = load(p, False); b = load(p, True)
    out["pages"][os.path.basename(p)].update({"measuredAfter": a, "measuredBeforeSwapBytes": b["imageBytes"]})
H.close()
tb = sum(v["bytesBefore"] for v in out["pages"].values()); ta = sum(v["bytesAfter"] for v in out["pages"].values())
out["totals"] = {"screenImageBytesBefore": tb, "screenImageBytesAfter": ta}
for f in ("showcase/screens/assets/images", "showcase/screens/assets/images-web", "showcase/screens/assets/vectors"):
    out["totals"][f] = sum(os.path.getsize(os.path.join(f, x)) for x in os.listdir(f) if not x.endswith((".md", ".json")))
json.dump(out, open("docs/replication/closure-image-weight.json", "w", encoding="utf-8"), indent=1)
for k, v in out["pages"].items(): print(k, v)
print(out["totals"])
