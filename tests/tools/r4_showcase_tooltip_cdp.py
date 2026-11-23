import sys, os, time, urllib.request
sys.dont_write_bytecode = True; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cdp_lib import Harness
H = Harness()
H.navigate("showcase/components/tooltip.html")
H.ok("tooltip showcase loads without errors", not H.problems(), H.problems())
H.ok("80 static variants visible", H.ev("[...document.querySelectorAll('.sc-tt-cell .annachy-tooltip')].filter(t => !t.hidden).length") == 80)
H.ok("6 interactive tooltips initialised hidden", H.ev("[...document.querySelectorAll('.sc-tt-inter .annachy-tooltip')].filter(t => t.hidden).length") == 6)
H.hover(".sc-tt-inter button"); time.sleep(0.65)
H.ok("interactive hover shows tooltip", H.ev("!document.getElementById('sc-tt0').hidden"))
for href in H.ev("[...document.querySelectorAll('a[href]')].map(a => a.href)"):
    try: code = urllib.request.urlopen(href).status
    except Exception as e: code = str(e)
    H.ok(f"link {href}", code == 200, code)
sys.exit(H.finish("TOOLTIP SHOWCASE"))
