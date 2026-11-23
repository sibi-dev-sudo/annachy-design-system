import sys, os
sys.dont_write_bytecode = True; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cdp_lib import Harness
H = Harness()
H.navigate("showcase/components/dropdown.html")
H.ok("dropdown showcase loads without errors", not H.problems(), H.problems())
H.ok("11 interactive dropdowns initialised + closed (8 R4 + 3 R6)", H.ev("[...document.querySelectorAll('[data-annachy-dropdown] .annachy-dropdown-menu')].filter(m => m.hidden).length") == 11)
H.ok("40 item variants (20 Light + 20 Dark)", H.ev("document.querySelectorAll('.sc-variant-table .annachy-dropdown-item').length") == 40)
H.ok("48 static menus visible (all Figma Menu variants)", H.ev("[...document.querySelectorAll('.sc-dd-figure .annachy-dropdown-menu')].filter(m => !m.hidden).length") == 48)
H.ok("R4 static menu heights = Figma (188/261/220/293)", H.ev("[...document.querySelectorAll('.sc-dd-figure:not(.sc-dd-r6-figure) .annachy-dropdown-menu')].map(m => m.getBoundingClientRect().height).join()") == "188,261,220,293,188,261,220,293")
META_H = {"desktop/off/none": 188, "desktop/on/none": 261, "mobile/off/none": 220, "mobile/on/none": 293, "desktop/off/label": 253, "desktop/off/icon": 253, "desktop/on/label": 326, "desktop/on/icon": 326, "mobile/off/label": 293, "mobile/off/icon": 293, "mobile/on/label": 366, "mobile/on/icon": 366}
got = H.ev("[...document.querySelectorAll('.sc-dd-r6-figure')].map(f => [f.dataset.variant, f.querySelector('.annachy-dropdown-menu').getBoundingClientRect().height])")
bad = [(v, h) for v, h in got if META_H["/".join(v.split("/")[i] for i in (1, 3, 4))] != h]
H.ok("40 R6 static menu heights = Figma META", len(got) == 40 and not bad, bad)
H.ok("Dark item table renders Dark fills", H.ev("getComputedStyle(document.querySelector('#sc-dd-dark-items .annachy-dropdown-item')).backgroundColor") == "rgb(24, 27, 33)")
H.ev("document.getElementById('sc-r6c-b').scrollIntoView({ block: 'start' })")
H.click("#sc-r6c-b"); H.click("#sc-r6c-o3")
H.ok("R6 demo: staged toggle does not commit yet", H.ev("document.querySelector('#sc-r6c').closest('.sc-dd-demo').querySelector('.sc-dd-value span').textContent") == "Product design")
H.click("#sc-r6c .annachy-dropdown-menu__footer-button")
H.ok("R6 demo: staged choice committed by Apply, value shown", H.ev("document.querySelector('#sc-r6c').closest('.sc-dd-demo').querySelector('.sc-dd-value span').textContent") == "Product design, Customer success", H.ev("document.querySelector('#sc-r6c').closest('.sc-dd-demo').querySelector('.sc-dd-value span').textContent"))
H.ev("window.scrollTo(0, 0)")
H.ok("markup reference rendered", "annachy-dropdown-menu__footer-button" in H.ev("document.getElementById('sc-dd-r6-code').textContent"))
H.click(".sc-dd-demo:nth-child(5) button")
H.ok("mobile interactive opens (352 wide)", H.ev("[...document.querySelectorAll('[data-annachy-dropdown] .annachy-dropdown-menu')].filter(m => !m.hidden).map(m => m.getBoundingClientRect().width).join()") == "352")
for href in H.ev("[...document.querySelectorAll('a[href]')].map(a => a.href)"):
    import urllib.request
    try: code = urllib.request.urlopen(href).status
    except Exception as e: code = str(e)
    H.ok(f"link {href}", code == 200, code)
sys.exit(H.finish("DROPDOWN SHOWCASE"))
