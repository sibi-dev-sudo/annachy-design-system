"""AUD-1 regression: Dropdown listener lifecycle and memory release (real Chrome, CDP).
Counts real event listeners with DOMDebugger.getEventListeners and checks garbage collection with WeakRef +
HeapProfiler.collectGarbage. Read-only with respect to the repository. Run from the project root:
    python -I tests/tools/r4_dropdown_lifecycle_cdp.py
"""
import os, sys, time
sys.dont_write_bytecode = True; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cdp_lib import Harness

H = Harness(1400, 900)
ok, ev = H.ok, H.ev
M = "import('/src/annachy.js')"


def listeners(expr, type_=None):
    """Number of listeners on the object returned by `expr` (optionally of one event type)."""
    obj = H.call("Runtime.evaluate", expression=expr)["result"]["objectId"]
    ls = H.call("DOMDebugger.getEventListeners", objectId=obj)["listeners"]
    H.call("Runtime.releaseObject", objectId=obj)
    return sum(1 for l in ls if type_ is None or l["type"] == type_)


def gc():
    H.call("HeapProfiler.enable"); H.call("HeapProfiler.collectGarbage"); time.sleep(0.1); H.call("HeapProfiler.collectGarbage")


doc_pd = lambda: listeners("document", "pointerdown")
H.navigate("tests/fixtures/r4-dropdown-interaction.html")
ok("module exports the lifecycle API", ev(f"{M}.then(m => [typeof m.initDropdowns, typeof m.destroyDropdowns, typeof m.getDropdown].join())") == "function,function,function")
base = doc_pd()   # document pointerdown listeners that do not belong to Dropdown (e.g. Tooltip's single module listener)

# 1. no document listener while closed; exactly one while open; none after close
ok("closed dropdowns add no document listener", ev(f"{M}.then(m => m.initDropdowns().length)") == 5 and doc_pd() == base, (doc_pd(), base))
H.click("#single-trigger"); ok("one document listener while open", doc_pd() == base + 1, doc_pd() - base)
H.key("Escape"); ok("listener removed on Escape close", doc_pd() == base, doc_pd() - base)
H.click("#single-trigger"); H.click("#s-2"); ok("listener removed on selection close", doc_pd() == base)
H.click("#single-trigger"); H.click("#before"); ok("listener removed on outside-click close", doc_pd() == base)
H.click("#single-trigger"); H.key("Tab"); ok("listener removed on Tab close", doc_pd() == base)
H.click("#search-trigger"); ok("searchable: one document listener while open", doc_pd() == base + 1)
H.key("Escape"); ok("searchable: removed on close", doc_pd() == base)

# 2. no accumulation over many cycles and repeated init
for _ in range(25):
    H.click("#multi-trigger"); H.key("Escape")
ok("25 open/close cycles leave no document listener", doc_pd() == base, doc_pd() - base)
ev(f"{M}.then(m => {{ for (let i = 0; i < 10; i++) m.initDropdowns(); }})")
ok("10× re-init: one click listener on trigger", listeners("document.getElementById('single-trigger')", "click") == 1)
ok("10× re-init: one keydown listener on trigger", listeners("document.getElementById('single-trigger')", "keydown") == 1)
ok("10× re-init: one click + one mousedown on listbox", listeners("document.getElementById('single-list')", "click") == 1 and listeners("document.getElementById('single-list')", "mousedown") == 1)
ok("10× re-init: search input has one keydown + one input listener", listeners("document.getElementById('search-input')", "keydown") == 1 and listeners("document.getElementById('search-input')", "input") == 1)
ev("window.__changes = []")
H.click("#single-trigger"); H.click("#s-3")
ok("behaviour unchanged after cycles: one change event", ev("window.__changes.length") == 1 and ev("window.__changes[0][0]") == "dd-single" and ev("window.__changes[0][1]") == ev("document.getElementById('s-3').dataset.value || document.querySelector('#s-3 .annachy-dropdown-item__label').textContent.trim()"), ev("window.__changes"))

# 3. destroy while open: closes without moving focus, removes every listener
H.click("#multi-trigger")
ok("open before destroy", ev("!document.getElementById('multi-menu').hidden") and doc_pd() == base + 1)
ev("document.getElementById('before').focus()")
n = ev(f"{M}.then(m => m.destroyDropdowns(document.getElementById('dd-multi')))")
ok("destroyDropdowns(wrapper) destroys one controller", n == 1, n)
ok("destroy closes the popup and resets aria-expanded", ev("document.getElementById('multi-menu').hidden") and ev("document.getElementById('multi-trigger').getAttribute('aria-expanded')") == "false")
ok("destroy removes the document listener", doc_pd() == base, doc_pd() - base)
ok("destroy does not move focus", H.active() == "before", H.active())
ok("destroy removes trigger listeners", listeners("document.getElementById('multi-trigger')") == 0)
ok("destroy removes listbox listeners", listeners("document.getElementById('multi-list')") == 0)
ok("destroy clears the active option", ev("document.querySelectorAll('#multi-list .is-active').length") == 0 and ev("document.getElementById('multi-trigger').hasAttribute('aria-activedescendant')") is False)
ok("getDropdown() is undefined after destroy", ev(f"{M}.then(m => m.getDropdown(document.getElementById('dd-multi')) === undefined)") is True)
H.click("#multi-trigger"); ok("destroyed dropdown no longer opens on click", ev("document.getElementById('multi-menu').hidden"))
ok("second destroy is a no-op (returns 0, no error)", ev(f"{M}.then(m => m.destroyDropdowns(document.getElementById('dd-multi')))") == 0)

# 4. re-init after destroy creates a fresh, working controller
fresh = ev(f"{M}.then(m => {{ const before = m.getDropdown(document.getElementById('dd-multi')); const c = m.initDropdowns(document.getElementById('dd-multi').parentElement).find(x => x.root.id === 'dd-multi'); return before === undefined && !!c && c.destroyed === false; }})")
ok("re-init after destroy creates a fresh controller", fresh is True, fresh)
ev("window.__changes = []")
H.click("#multi-trigger"); H.click("#m-1")
ok("re-initialised dropdown works (one change event)", ev("window.__changes.length") == 1, ev("window.__changes"))
H.key("Escape"); ok("re-initialised dropdown closes cleanly", doc_pd() == base)
ok("re-init: exactly one click listener on trigger", listeners("document.getElementById('multi-trigger')", "click") == 1)

# 5. pending announcement timer is cleared on destroy
H.click("#search-trigger"); H.type("Ap")
ev("document.querySelector('#search-menu .annachy-dropdown-menu__status').textContent = 'sentinel'")
ev(f"{M}.then(m => m.destroyDropdowns(document.getElementById('dd-search')))")
time.sleep(0.8)
ok("destroy cancels the debounced announcement", ev("document.querySelector('#search-menu .annachy-dropdown-menu__status').textContent") == "sentinel")
ok("destroy of searchable clears the search field and filter", ev("document.getElementById('search-input').value") == "" and ev("[...document.querySelectorAll('#search-list [role=option]')].every(o => !o.hidden)"))
ok("search input listeners removed", listeners("document.getElementById('search-input')") == 0)

# 6. memory: destroyed + removed dropdowns are garbage-collectable; nothing accumulates on document
ev(f"""{M}.then(m => {{
  window.__refs = [];
  const host = document.createElement('div'); host.id = 'dyn'; document.body.append(host);
  for (let i = 0; i < 100; i++) {{
    host.insertAdjacentHTML('beforeend', `<div class="annachy-dropdown" data-annachy-dropdown id="w${{i}}">
      <button type="button" role="combobox" aria-haspopup="listbox" aria-controls="m${{i}}">T</button>
      <div class="annachy-dropdown-menu annachy-dropdown-menu--desktop" id="m${{i}}"><ul role="listbox" aria-label="L">
      <li role="option" id="o${{i}}" aria-selected="false" class="annachy-dropdown-item annachy-dropdown-item--desktop"><span class="annachy-dropdown-item__label">A</span></li></ul></div></div>`);
  }}
  const cs = m.initDropdowns(host);
  cs.forEach(c => {{ c.open(); window.__refs.push(new WeakRef(c)); }});
  return cs.length;
}})""")
ok("100 dynamic dropdowns open → 100 document listeners", doc_pd() == base + 100, doc_pd() - base)
ok("destroyDropdowns(host) destroys 100", ev(f"{M}.then(m => m.destroyDropdowns(document.getElementById('dyn')))") == 100)
ok("all 100 document listeners removed", doc_pd() == base, doc_pd() - base)
ev("document.getElementById('dyn').remove()")
gc()
alive = ev("window.__refs.filter(r => r.deref() !== undefined).length")
ok("destroyed + removed controllers are garbage-collected", alive == 0, f"{alive} of 100 still alive")
# closed dropdowns removed WITHOUT destroy are also collectable (no document listener holds them)
ev(f"""{M}.then(m => {{
  window.__refs2 = [];
  const host = document.createElement('div'); host.id = 'dyn2'; document.body.append(host);
  for (let i = 0; i < 50; i++) host.insertAdjacentHTML('beforeend', `<div data-annachy-dropdown><button role="combobox" aria-haspopup="listbox" aria-controls="n${{i}}">T</button><div class="annachy-dropdown-menu" id="n${{i}}"><ul role="listbox"><li role="option" id="p${{i}}">A</li></ul></div></div>`);
  m.initDropdowns(host).forEach(c => {{ c.open(); c.close(false); window.__refs2.push(new WeakRef(c)); }});
  host.remove();
}})""")
gc()
alive2 = ev("window.__refs2.filter(r => r.deref() !== undefined).length")
ok("closed dropdowns removed without destroy() are garbage-collected", alive2 == 0, f"{alive2} of 50 still alive")
ok("no document listener accumulated overall", doc_pd() == base, doc_pd() - base)
ok("no runtime errors", not H.problems(), H.problems())
sys.exit(H.finish("R4 DROPDOWN LIFECYCLE"))
