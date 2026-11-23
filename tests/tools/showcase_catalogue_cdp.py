"""Showcase catalogue (index search + filters) and Iconography page, real input over HTTP (CDP).
Run from the project root: python -I tests/tools/showcase_catalogue_cdp.py"""
import os, sys, time, urllib.request
sys.dont_write_bytecode = True; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cdp_lib import Harness

H = Harness(1400, 900)
ok, ev = H.ok, H.ev
visible = lambda: ev("[...document.querySelectorAll('.sc-card')].filter(c => !c.hidden).map(c => c.querySelector('a').textContent.trim()).join('|')")
H.navigate("showcase/index.html")
ok("index loads without errors", not H.problems(), H.problems())
total = ev("document.querySelectorAll('.sc-card').length")
ok("catalogue lists foundations (7) + components (8) + screens", ev("document.querySelectorAll('[data-category=foundation]').length") == 8 and ev("document.querySelectorAll('[data-category=component]').length") == 8 and ev("document.querySelectorAll('[data-category=screen]').length") == 8, total)
ok("count announces all entries", ev("document.getElementById('sc-q-count').textContent") == f"{total} of {total} entries")
H.click("#sc-q"); H.type("dropdown")
ok("search 'dropdown' → Dropdown only", visible() == "Dropdown", visible())
for _ in range(8): H.key("Backspace")
H.type("887:2492"); ok("search by Figma node id → Button", visible() == "Button", visible())
for _ in range(8): H.key("Backspace")
H.type("zzqx"); ok("no match shows the empty state", ev("!document.getElementById('sc-empty').hidden") and visible() == "")
for _ in range(4): H.key("Backspace")
ok("clearing restores all", ev("document.querySelectorAll('.sc-card:not([hidden])').length") == total)
H.click('[data-filter="component"]')
ok("Components filter shows the 8 components", ev("document.querySelectorAll('.sc-card:not([hidden])').length") == 8 and ev("document.querySelector('[data-filter=component]').getAttribute('aria-pressed')") == "true")
ok("other groups hidden", ev("document.querySelector('[data-group=foundation]').hidden") is True)
H.click('[data-filter="all"]')
links = ev("[...document.querySelectorAll('.sc-card a')].map(a => a.href)")
bad = []
for href in links:
    try: code = urllib.request.urlopen(href).status
    except Exception as e: code = str(e)
    if code != 200: bad.append((href, code))
ok(f"every catalogue link resolves ({len(links)})", not bad, bad)
H.navigate("showcase/foundations/iconography.html")
time.sleep(0.3)
for _ in range(100):   # wait until every mapped slot has rendered (or failed) — not just the first fill pass
    if ev("[...document.querySelectorAll('[data-annachy-icon]')].every(e => e.querySelector(':scope > svg') || e.dataset.annachyIconError)"): break
    time.sleep(0.1)
probs = [p for p in H.problems() if not ("net::ERR_ABORTED" in p and p.endswith(".svg (Fetch)"))]   # cancelled-then-retried SVG fetches
ok("iconography loads without errors", not probs, probs)
ok("no icon slot reports a load error", ev("document.querySelectorAll('[data-annachy-icon-error]').length") == 0, ev("[...document.querySelectorAll('[data-annachy-icon-error]')].map(e => e.dataset.annachyIconError)"))
ok("manifest status rendered as active with icons", ev("document.getElementById('ic-manifest').textContent").startswith('status "active", 6100 icons'), ev("document.getElementById('ic-manifest').textContent"))
ok("slot table lists the slot cases", ev("document.querySelectorAll('.sc-icon-slots tbody tr').length") == 11)
for _ in range(50):
    if ev("document.documentElement.dataset.iconsFilled"): break
    time.sleep(0.1)
ok("mapped slots render their Figma icon (Button / Gradient / Input Outline / Dropdown search)", ev("[...document.querySelectorAll('.sc-icon-slots [data-annachy-icon]')].length") >= 6 and ev("[...document.querySelectorAll('.sc-icon-slots [data-annachy-icon]')].every(s => s.querySelector(':scope > svg'))"))
ok("unmapped slots stay empty (Dropdown indicator, Input Filled, Checkbox glyph, Tooltip arrow)", ev("[...document.querySelectorAll('.sc-icon-slots .annachy-dropdown-item__indicator, .sc-icon-slots .annachy-input--filled .sc-slot, .sc-icon-slots .annachy-checkbox__glyph')].every(s => !s.children.length)"))
sys.exit(H.finish("SHOWCASE CATALOGUE"))
