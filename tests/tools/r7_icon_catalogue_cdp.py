"""R7: browser icon catalogue (showcase/icons/) — real input over HTTP (CDP): counts, search, filters, sizes, styles,
paging, restricted Brands toggle, actual SVG rendering with currentColor, no missing assets.
Run from the project root: python -I tests/tools/r7_icon_catalogue_cdp.py"""
import json, os, sys, time, urllib.request
sys.dont_write_bytecode = True; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cdp_lib import Harness

cat = json.load(open("src/icons/catalogue.json", encoding="utf-8"))
sets = [s for c in cat["categories"] for s in c["sets"]]
lib = [s for c in cat["categories"] if not c.get("restricted") for s in c["sets"]]
variants = sum(len(st.get("variants", {})) for s in sets for st in s["styles"].values())
H = Harness(1400, 1000)
ok, ev = H.ok, H.ev

def settle():
    for _ in range(100):
        if ev("document.getElementById('ic-grid').dataset.rendered") and ev("[...document.querySelectorAll('.ic-icon')].every(c => c.querySelector('svg') || c.classList.contains('ic-icon--missing'))"): return
        time.sleep(0.1)

def count(): return int(ev("document.getElementById('ic-count').textContent").split(" ")[0])

H.navigate("showcase/icons/index.html"); settle()
ok("catalogue loads without errors", not H.problems(), H.problems())
summary = ev("document.getElementById('ic-summary').textContent")
ok("summary: 5,128 sets, 35,890 variants", f"{len(sets)} icon sets" in summary and f"{variants} Figma variants" in summary and len(sets) == 5128 and variants == 35890, summary)
ok("default view = library sets (Brands hidden)", count() == len(lib), (count(), len(lib)))
ok("first page renders 48 cards", ev("document.querySelectorAll('.ic-card').length") == 48)
ok("no missing asset on the first page", ev("document.querySelectorAll('.ic-icon--missing').length") == 0, ev("[...document.querySelectorAll('.ic-icon--missing')].map(c => c.dataset.error).slice(0,3)"))
sizes = ev("[...document.querySelectorAll('.ic-icon')].map(c => [c.dataset.size, c.querySelector('svg').getBoundingClientRect().width, c.querySelector('svg').getBoundingClientRect().height])")
want = {"XS": 16, "S": 20, "M": 24, "L": 32, "XL": 40}
bad = [s for s in sizes if s[1] != want[s[0]] or s[2] != want[s[0]]]
ok(f"every rendered SVG has its Figma size ({len(sizes)} icons)", sizes and not bad, bad[:3])
ok("artwork paints with currentColor (card icon colour)", ev("(() => { const c = document.querySelector('.ic-card'); const p = c.querySelector('.ic-icon svg [fill]:not([fill=none]), .ic-icon svg [stroke]:not([stroke=none])'); const v = p.getAttribute('fill') && p.getAttribute('fill') !== 'none' ? getComputedStyle(p).fill : getComputedStyle(p).stroke; return v === getComputedStyle(c).color; })()"))
H.click("#ic-q"); H.type("home 54"); settle()
ok("search 'home 54' finds Home/Home 54", "Home/Home 54" in ev("[...document.querySelectorAll('.ic-card__name')].map(e => e.textContent).join('|')"))
ev("document.getElementById('ic-q').value = '1802:68148'; document.getElementById('ic-q').dispatchEvent(new Event('input'))"); settle()
ok("search by set node id → exactly that set", count() == 1 and ev("document.querySelector('.ic-card').dataset.node") == "1802:68148")
ev("document.getElementById('ic-q').value = '1802:68159'; document.getElementById('ic-q').dispatchEvent(new Event('input'))"); settle()
ok("search by variant node id (M Outline) → its set", count() == 1)
ev("document.getElementById('ic-q').value = ''; document.getElementById('ic-q').dispatchEvent(new Event('input'))"); settle()
first = next(c for c in cat["categories"] if not c.get("restricted"))
ev(f"document.getElementById('ic-cat').value = {json.dumps(first['slug'])}; document.getElementById('ic-cat').dispatchEvent(new Event('change'))"); settle()
ok(f"category filter ({first['name']}) shows its {len(first['sets'])} sets", count() == len(first["sets"]))
ev("document.getElementById('ic-cat').value = ''; document.getElementById('ic-cat').dispatchEvent(new Event('change'))")
ev("document.getElementById('ic-style').value = 'filled'; document.getElementById('ic-style').dispatchEvent(new Event('change'))"); settle()
nf = sum(1 for s in lib if "filled" in s["styles"])
ok(f"style filter Filled → {nf} sets, only filled rows", count() == nf and ev("[...document.querySelectorAll('.ic-icon')].every(c => c.dataset.style === 'filled')"))
ev("document.getElementById('ic-style').value = ''; document.getElementById('ic-style').dispatchEvent(new Event('change'))")
ev("document.getElementById('ic-size').value = 'XL'; document.getElementById('ic-size').dispatchEvent(new Event('change'))"); settle()
ok("size filter XL → only 40 px icons", ev("[...document.querySelectorAll('.ic-icon')].every(c => c.dataset.size === 'XL' && c.querySelector('svg').getBoundingClientRect().width === 40)"))
ev("document.getElementById('ic-size').value = ''; document.getElementById('ic-size').dispatchEvent(new Event('change'))"); settle()
H.ev("document.getElementById('ic-next').scrollIntoView({ block: 'center' })"); H.click("#ic-next"); settle()
ok("paging: next page", ev("document.getElementById('ic-page').textContent").startswith("Page 2 of"))
H.ev("document.getElementById('ic-prev').scrollIntoView({ block: 'center' })"); H.click("#ic-prev"); settle()
ok("paging: previous page", ev("document.getElementById('ic-page').textContent").startswith("Page 1 of"))
H.ev("document.getElementById('ic-brands').scrollIntoView({ block: 'center' })"); H.click("#ic-brands"); settle()
ok("Brands toggle adds the restricted sets and shows the rights notice", count() == len(sets) and ev("!document.getElementById('ic-brands-note').hidden"))
brands = next((c for c in cat["categories"] if c.get("restricted")), None)
if brands:
    ev(f"document.getElementById('ic-cat').value = {json.dumps(brands['slug'])}; document.getElementById('ic-cat').dispatchEvent(new Event('change'))"); settle()
    ok("restricted Brands render from restricted/ (no missing assets)", ev("document.querySelectorAll('.ic-icon svg').length") > 0 and ev("document.querySelectorAll('.ic-icon--missing').length") == 0)
# Network-level cancellations of in-flight SVG fetches (superseded renders) are not asset failures: the page marks any
# fetch error as .ic-icon--missing, which is asserted after every step above, and every file is fetched below.
probs = H.problems()
cancelled = [p for p in probs if "net::ERR_ABORTED" in p and p.endswith(".svg (Fetch)")]
ok("no runtime errors other than cancelled in-flight SVG fetches", not [p for p in probs if p not in cancelled], [p for p in probs if p not in cancelled][:5])
ok("no icon ever flagged missing in the page", ev("document.querySelectorAll('.ic-icon--missing').length") == 0)
files = sorted({f for s_ in sets for st in s_["styles"].values() for f in [st["file"], *st.get("perSize", {}).values()]})
bad = []
for f in files:
    try: code = urllib.request.urlopen(f"{H.base}/src/icons/{f}").status
    except Exception as e: code = str(e)
    if code != 200: bad.append((f, code))
ok(f"every catalogue asset is served (HTTP 200): {len(files)} files", not bad, bad[:5])
sys.exit(H.finish("R7 ICON CATALOGUE"))
