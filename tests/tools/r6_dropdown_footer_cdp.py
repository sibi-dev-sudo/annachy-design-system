"""R6: Dropdown Footer (staged commit, R4-Q3 decision) and Dark theme, driven by real keyboard / mouse / touch (CDP).
Run from the project root: python -I tests/tools/r6_dropdown_footer_cdp.py"""
import os, sys, time
sys.dont_write_bytecode = True; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cdp_lib import Harness

H = Harness(1400, 900)
ok, ev, key = H.ok, H.ev, H.key
isopen = lambda m: ev(f"!document.getElementById('{m}').hidden")
sel = lambda l: ev(f"[...document.querySelectorAll('#{l} [aria-selected=\"true\"]')].map(o => o.id).join()")
changes = lambda: ev("window.__changes.map(c => c.join(':')).join('|')")
H.navigate("tests/fixtures/r6-dropdown-interaction.html")

# --- Multiple + footer: staged until Apply
H.click("#fm-trigger"); ok("click opens footer dropdown", isopen("fm-menu"))
H.click("#fm-2"); H.click("#fm-3")
ok("toggles shown immediately (staged)", sel("fm-list") == "fm-1,fm-2,fm-3", sel("fm-list"))
ok("staged changes fire no annachy-change", changes() == "", changes())
ok("popup stays open while staging", isopen("fm-menu"))
key("Escape")
ok("Escape closes", not isopen("fm-menu"))
ok("Escape discards staged changes", sel("fm-list") == "fm-1", sel("fm-list"))
ok("Escape returns focus to trigger", H.active() == "fm-trigger")
ok("no change event after cancel", changes() == "")
H.click("#fm-trigger"); H.click("#fm-2"); H.click("#before")
ok("outside click closes and discards", not isopen("fm-menu") and sel("fm-list") == "fm-1", sel("fm-list"))
H.click("#fm-trigger"); H.click("#fm-1"); H.click("#fm-3"); H.click("#fm-apply")
ok("Apply commits", sel("fm-list") == "fm-3", sel("fm-list"))
ok("Apply closes and returns focus to trigger", not isopen("fm-menu") and H.active() == "fm-trigger")
ok("Apply fires exactly one annachy-change with committed values", changes() == "dd-fm:cs", changes())
H.click("#fm-trigger"); ok("re-open shows committed selection", sel("fm-list") == "fm-3")
key("Escape")

# --- Keyboard path: arrows + Space stage, Tab to Apply, Enter commits
ev("window.__changes = []")
H.click("#before"); key("Tab"); ok("Tab reaches trigger", H.active() == "fm-trigger")
key("ArrowDown"); ok("ArrowDown opens", isopen("fm-menu"))
key(" ")
ok("ArrowDown opens on the selected option; Space toggles it off (staged)", sel("fm-list") == "", sel("fm-list"))
staged = sel("fm-list")
key("Tab"); ok("Tab from trigger moves to the footer button", H.active() == "fm-apply")
ok("popup still open on footer focus", isopen("fm-menu"))
key("Tab", shift=True); ok("Shift+Tab returns to the trigger", H.active() == "fm-trigger" and isopen("fm-menu"))
key("Tab"); key("Enter")
ok("Enter on Apply commits staged selection", sel("fm-list") == staged and not isopen("fm-menu"), sel("fm-list"))
ok("keyboard Apply fires one change", ev("window.__changes.length") == 1)
H.click("#fm-trigger"); key("Tab"); key("Escape")
ok("Escape on the footer button cancels, closes, focuses trigger", not isopen("fm-menu") and H.active() == "fm-trigger")
H.click("#fm-trigger"); H.click("#fm-1"); key("Tab"); key("Tab")
ok("Tab past the footer button closes and discards", not isopen("fm-menu") and sel("fm-list") == staged, sel("fm-list"))

# --- Single + footer (Dark): option click stages without closing; disabled not selectable
ev("window.__changes = []")
H.click("#fs-trigger"); H.click("#fs-2")
ok("single footer: click stages, popup stays open", isopen("fs-menu") and sel("fs-list") == "fs-2")
H.click("#fs-3"); ok("disabled option never selected", sel("fs-list") == "fs-2")
ok("Dark selected row: Blue/500 fill + Base/White label", ev("[getComputedStyle(document.getElementById('fs-2')).backgroundColor, getComputedStyle(document.querySelector('#fs-2 .annachy-dropdown-item__label')).color].join('|')") == "rgb(0, 79, 235)|rgb(250, 252, 255)")
ok("Dark menu fill #181b21", ev("getComputedStyle(document.getElementById('fs-menu')).backgroundColor") == "rgb(24, 27, 33)")
ok("Dark previous selection cleared to Dark default fill", ev("getComputedStyle(document.getElementById('fs-1')).backgroundColor") == "rgb(24, 27, 33)")
H.tap("#fs-apply")
ok("tap Apply commits single", sel("fs-list") == "fs-2" and not isopen("fs-menu") and changes() == "dd-fs:Bala", changes())
H.click("#fs-trigger")
rest = ev("getComputedStyle(document.getElementById('fs-apply')).backgroundColor")
H.hover("#fs-apply"); time.sleep(0.1)
hov = ev("getComputedStyle(document.getElementById('fs-apply')).backgroundColor")
ok("footer button takes the R3 Primary hover state", rest == "rgb(0, 79, 235)" and hov != rest, f"{rest} -> {hov}")
key("Escape")

# --- Search + footer (Mobile): Tab from the search field reaches Apply
ev("window.__changes = []")
H.click("#fq-trigger"); ok("search focused on open", H.active() == "fq-input")
H.type("Ban"); key("ArrowDown"); key("Enter")
ok("search: Enter stages the active match", sel("fq-list") == "fq-2", sel("fq-list"))
key("Tab"); ok("Tab from search moves to Apply", H.active() == "fq-apply")
key("Enter")
ok("search + footer Apply commits and closes", sel("fq-list") == "fq-2" and not isopen("fq-menu") and changes() == "dd-fq:Bananas", changes())
H.click("#fq-trigger")
ok("mobile footer button 48 tall", ev("document.getElementById('fq-apply').getBoundingClientRect().height") == 48)
key("Escape")

# --- Lifecycle: destroy while staged reverts and removes footer listeners
H.click("#fm-trigger"); H.click("#fm-2")
n = ev("import('/src/annachy.js').then(m => m.destroyDropdowns(document.getElementById('dd-fm')))")
ok("destroy while staged: closes and reverts", n == 1 and not isopen("fm-menu") and sel("fm-list") == staged, sel("fm-list"))
obj = H.call("Runtime.evaluate", expression="document.getElementById('fm-apply')")["result"]["objectId"]
ok("destroy removes footer button listeners", len(H.call("DOMDebugger.getEventListeners", objectId=obj)["listeners"]) == 0)
ok("no runtime errors", not H.problems(), H.problems())
sys.exit(H.finish("R6 DROPDOWN FOOTER"))
