"""Closure: practical accessibility / developer-usability audit of every showcase page (real Chrome, local HTTP).

Per page: no console errors / exceptions / failed or 4xx requests (same rules as the showcase crawl); <html lang> and a
<title>; no duplicate ids; every <img> has an alt attribute (decorative = alt=""); every interactive control (a[href],
button, input, select, textarea, [role=button|link|checkbox|radio|switch|tab|option|menuitem], [tabindex>=0]) has an
accessible name (Chrome's accessibility tree); keyboard: the first 12 Tab stops each receive focus and show a visible
focus indicator (outline, box-shadow, border or background of the element or one of its 3 nearest ancestors differs
between the focused and the blurred state: covers D-21 2px-border focus and the input field's :has(:focus-visible) state).
    python -I tests/tools/closure_a11y_cdp.py
"""
import glob, json, os, sys
sys.dont_write_bytecode = True; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
from cdp_lib import Harness

PAGES = sorted(p.replace(os.sep, "/") for p in glob.glob("showcase/**/*.html", recursive=True))
H = Harness(1600, 1200)
STATIC = """(() => { const r = {};
  r.lang = !!document.documentElement.getAttribute('lang'); r.title = !!document.title.trim();
  const ids = [...document.querySelectorAll('[id]')].map((e) => e.id); r.dupIds = [...new Set(ids.filter((x, i) => ids.indexOf(x) !== i))];
  r.imgNoAlt = [...document.querySelectorAll('img')].filter((i) => !i.hasAttribute('alt')).map((i) => i.getAttribute('src')).slice(0, 5);
  return JSON.stringify(r); })()"""
for page in PAGES:
    H.navigate(page)
    H.ev("new Promise((r) => { let n = 0; const t = () => (++n > 60 || [...document.images].every((i) => i.complete)) ? r(true) : setTimeout(t, 100); t(); })")
    H.ev("new Promise((r) => setTimeout(() => r(true), 300))")
    probs = [p for p in H.problems() if not ("net::ERR_ABORTED" in p and p.endswith(".svg (Fetch)"))]
    H.ok(f"{page}: no console errors or failed requests", not probs, "; ".join(probs[:3]))
    st = json.loads(H.ev(STATIC))
    H.ok(f"{page}: <html lang> and <title>", st["lang"] and st["title"])
    H.ok(f"{page}: no duplicate ids", not st["dupIds"], ",".join(st["dupIds"][:5]))
    H.ok(f"{page}: every <img> has an alt attribute", not st["imgNoAlt"], ",".join(st["imgNoAlt"]))
    # accessible names from Chrome's accessibility tree
    tree = H.call("Accessibility.getFullAXTree")["nodes"]
    ROLES = {"button", "link", "checkbox", "radio", "switch", "tab", "option", "menuitem", "textbox", "combobox", "searchbox", "listbox", "slider", "spinbutton"}
    unnamed = []
    for n in tree:
        role = (n.get("role") or {}).get("value"); name = ((n.get("name") or {}).get("value") or "").strip()
        if n.get("ignored") or role not in ROLES: continue
        if not name: unnamed.append(f"{role}#{n.get('backendDOMNodeId')}")
    if unnamed:
        desc = []
        for u in unnamed[:4]:
            bid = int(u.split("#")[1])
            o = H.call("DOM.resolveNode", backendNodeId=bid)["object"]["objectId"]
            desc.append(H.call("Runtime.callFunctionOn", objectId=o, functionDeclaration="function(){return this.outerHTML.slice(0,140)}", returnByValue=True)["result"]["value"])
        H.ok(f"{page}: every interactive control has an accessible name", False, f"{len(unnamed)} unnamed: " + " | ".join(desc))
    else:
        H.ok(f"{page}: every interactive control has an accessible name", True)
    # keyboard focus visibility
    H.ev("document.activeElement && document.activeElement.blur(); window.scrollTo(0, 0); true")
    seen, invisible = 0, []
    for _ in range(12):
        H.key("Tab")
        # real state change: signature of the element and its 3 nearest ancestors while focused vs after blur (the design's
        # focus treatment may be a border-width change, or drawn on the field wrapper via :has(:focus-visible))
        r = json.loads(H.ev("""(() => { const e = document.activeElement; if (!e || e === document.body) return 'null';
          const sig = () => { const out = []; let n = e; for (let k = 0; n && k < 4; k++, n = n.parentElement) { const f = getComputedStyle(n);
            out.push([f.outlineStyle, f.outlineWidth, f.outlineColor, f.boxShadow, f.borderTopWidth, f.borderTopColor, f.backgroundColor].join('|')); } return out.join('#'); };
          const on = sig(); e.blur(); const off = sig(); e.focus();
          const visible = on !== off;
          return JSON.stringify([e.tagName + (e.id ? '#' + e.id : '') + '.' + String(e.className).slice(0, 40), visible]); })()"""))
        if r is None: break
        seen += 1
        if not r[1]: invisible.append(r[0])
    if seen: H.ok(f"{page}: visible focus on the first {seen} Tab stops", not invisible, ", ".join(invisible[:4]))
sys.exit(H.finish("CLOSURE A11Y"))
