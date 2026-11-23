"""Whole-showcase verification (one Chrome instance, pages visited sequentially): every HTML page under showcase/ loads
over HTTP without runtime errors or failed requests, every local link / stylesheet / script / image reference resolves,
every page renders content, library CSS is applied, mapped icon slots render SVGs, and Dark-theme regions resolve the Dark
token values. Run from the project root: python -I tests/tools/showcase_crawl_cdp.py"""
import glob, os, sys, time, urllib.parse, urllib.request
sys.dont_write_bytecode = True; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cdp_lib import Harness

pages = sorted(p.replace("\\", "/") for p in glob.glob("showcase/**/*.html", recursive=True))
H = Harness(1440, 1000)
ok, ev = H.ok, H.ev
checked = {}
for page in pages:
    H.navigate(page)
    for _ in range(150):  # let module scripts settle: every icon slot rendered or reporting an error (≤ 15 s)
        if ev("document.readyState") == "complete" and ev("[...document.querySelectorAll('[data-annachy-icon]')].every(e => e.querySelector(':scope > svg') || e.dataset.annachyIconError)"): break
        time.sleep(0.1)
    time.sleep(0.2)
    probs = [p for p in H.problems() if not ("net::ERR_ABORTED" in p and p.endswith(".svg (Fetch)"))]
    ok(f"{page}: no runtime errors / failed requests", not probs, probs[:3])
    ok(f"{page}: renders content", ev("document.body.innerText.trim().length > 0 && document.body.getBoundingClientRect().height > 100"))
    ok(f"{page}: library stylesheet applied", ev("[...document.styleSheets].some(s => s.href && s.href.endsWith('/src/annachy.css'))"))
    refs = ev("[...document.querySelectorAll('a[href], link[href], script[src], img[src]')].map(e => e.href || e.src).filter(u => u.startsWith(location.origin))")
    for u in refs:
        u = u.split("#")[0]
        if u in checked: continue
        try: checked[u] = urllib.request.urlopen(u).status
        except Exception as e: checked[u] = str(e)
    broken = [u for u in refs if checked.get(u.split("#")[0]) != 200]
    ok(f"{page}: local references resolve ({len(refs)})", not broken, broken[:3])
    slots = ev("[...document.querySelectorAll('[data-annachy-icon]')].map(e => !!e.querySelector(':scope > svg'))")
    if slots: ok(f"{page}: all {len(slots)} mapped icon slots render an SVG", all(slots), ev("[...document.querySelectorAll('[data-annachy-icon]')].filter(e => !e.querySelector(':scope > svg')).map(e => e.dataset.annachyIcon + ' ' + (e.dataset.annachyIconError || 'not filled'))"))
    dark = ev("[...document.querySelectorAll('[data-annachy-theme=dark]')].slice(0, 3).map(e => getComputedStyle(e).getPropertyValue('--annachy-color-background-secondary').trim())")
    if dark: ok(f"{page}: Dark theme regions resolve Dark tokens", all(v == "#181b21" for v in dark), dark)
print(f"pages: {len(pages)} · unique local references: {len(checked)}")
sys.exit(H.finish("SHOWCASE CRAWL"))
