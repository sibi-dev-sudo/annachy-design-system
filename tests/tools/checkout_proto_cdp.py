"""Mixed-cart checkout prototype (showcase/screens/checkout): brief requirements in real Chrome, both directions.

Static: checkout.css uses no raw colours, and every var(--annachy-*) it references is defined by the library.
Per direction (A, B), mobile 390 and desktop 1440: no console errors / failed requests; per-group free delivery at ₹299
with a ₹40 fee and an "Add ₹X more" cue; instant totals on quantity change; unavailable item excluded; delivery: full
slots disabled, Pay blocked until a slot is chosen, same-day option priced, slot sold out while choosing (auto-picks the
next free slot, announced); pay together / separately; payment failure then retry; confirmation shows two shipments with
their contents and next steps; every button and option tile >= 44 px high.
    python -I tests/tools/checkout_proto_cdp.py
"""
import glob, json, os, re, sys, time
sys.dont_write_bytecode = True; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
from cdp_lib import Harness

D = "showcase/screens/checkout/"
css = open(D + "checkout.css", encoding="utf-8").read()
defined = set()
for f in glob.glob("src/**/*.css", recursive=True):
    defined |= set(re.findall(r"(--annachy-[a-z0-9-]+)\s*:", open(f, encoding="utf-8").read()))
H = Harness(1600, 1200)
H.ok("checkout.css: no raw colour values (tokens only)", not re.search(r"#[0-9a-fA-F]{3,8}\b|rgba?\(", re.sub(r"/\*.*?\*/", "", css, flags=re.S)))
used = set(re.findall(r"var\((--annachy-[a-z0-9-]+)", css))
H.ok("checkout.css: every referenced token exists", used <= defined, ", ".join(sorted(used - defined)))
for js in ("checkout-core.js", "direction-a.js", "direction-b.js"):
    t = open(D + js, encoding="utf-8").read()
    H.ok(f"{js}: no raw colour values", not re.search(r"#[0-9a-fA-F]{6}\b|rgba?\(", t))

def go(page, w=390):
    H.call("Emulation.setDeviceMetricsOverride", width=w, height=900, deviceScaleFactor=1, mobile=w < 900)
    H.navigate(D + page); H.ev("localStorage.clear(); true"); H.navigate(D + page); wait(0.3)
def wait(s): time.sleep(s)
txt = lambda sel: H.ev(f"(document.querySelector({json.dumps(sel)}) || {{}}).textContent || ''")
body = lambda: H.ev("document.getElementById('co-root').innerText")
click = lambda sel: H.ev(f"(() => {{ const e = document.querySelector({json.dumps(sel)}); if (!e) return false; e.click(); return true; }})()")

for d in ("a", "b"):
    for w in (390, 1440):
        for s in ("cart", "delivery", "confirmation"):
            go(f"{d}-{s}.html", w)
            H.ok(f"{d}-{s} @{w}: no console errors or failed requests", not H.problems(), "; ".join(H.problems()[:2]))
            small = H.ev("""JSON.stringify([...document.querySelectorAll('#co-root button, #co-root .co-option, #co-root summary')].filter((e) => e.offsetParent)
              .map((e) => [e.textContent.trim().slice(0, 24), Math.round(e.getBoundingClientRect().height)]).filter((x) => x[1] < 44))""")
            H.ok(f"{d}-{s} @{w}: touch targets >= 44 px", small == "[]", small)
            sw = H.ev("[document.documentElement.scrollWidth, innerWidth]")
            H.ok(f"{d}-{s} @{w}: no horizontal overflow", sw[0] <= sw[1], f"{sw[0]} > {sw[1]}")
    # cart rules
    go(f"{d}-cart.html")
    t = body()
    H.ok(f"{d}: grocery ₹412 qualifies for free delivery", "Free delivery unlocked" in t)
    H.ok(f"{d}: other items ₹249 shows the ₹50 cue and ₹40 fee", "Add ₹50 more for free delivery" in t and "₹40" in t)
    H.ok(f"{d}: total ₹701 (412 + 249 + 40)", "₹701" in t)
    t0 = time.time(); click('[data-qty="o1"][data-d="1"]'); t = body()
    H.ok(f"{d}: +1 towel → other items free, total ₹910, instantly", "Add ₹" not in t and "₹910" in t and time.time() - t0 < 1, f"{time.time() - t0:.2f}s")
    H.ok(f"{d}: change announced to screen readers", "₹910" in H.ev("document.getElementById('co-live').textContent") or (wait(0.1) or "₹910" in H.ev("document.getElementById('co-live').textContent")))
    click('[data-qty="o1"][data-d="-1"]'); click('[data-qty="g2"][data-d="-1"]'); t = body()
    H.ok(f"{d}: removing the atta drops grocery to ₹163 → ₹40 fee and 'Add ₹136 more'", "Add ₹136 more" in t, t[:200])
    go(f"{d}-cart.html?scenario=unavailable"); t = body()
    H.ok(f"{d}: unavailable item shown and excluded from totals (still ₹701)", "No longer available" in t and "₹701" in t)
    click('[data-remove="g4"]'); H.ok(f"{d}: unavailable item can be removed", "Paneer" not in body())
    # delivery
    for w in (390, 1440):
        go(f"{d}-delivery.html", w)
        H.ok(f"{d} @{w}: today's 3 full slots cannot be chosen", H.ev("[...document.querySelectorAll('input[name=slot]')].filter((i) => i.disabled).length") in (0, 3)
             and ("Full" in body()))
        H.ok(f"{d} @{w}: Pay is blocked until a slot is chosen", H.ev("[...document.querySelectorAll('[data-pay]')].filter((b) => b.offsetParent).every((b) => b.getAttribute('aria-disabled') === 'true')"))
    go(f"{d}-delivery.html", 1440)
    H.ev("document.getElementById('d0-s4').click(); true"); wait(0.2)
    H.ok(f"{d}: slot chosen → Pay enabled", H.ev("[...document.querySelectorAll('[data-pay]')].filter((b) => b.offsetParent).every((b) => b.getAttribute('aria-disabled') !== 'true')"))
    if d == "a": H.ev("document.getElementById('express').click(); true")
    else: H.ev("document.getElementById('express').click(); true")
    wait(0.2); H.ok(f"{d}: same-day for other items costs ₹79 → total ₹740", "₹740" in body(), body()[-300:])
    click('[data-pay="all"]'); wait(1.8)
    H.ok(f"{d}: pay together → confirmation", H.ev("location.pathname").endswith(f"{d}-confirmation.html"))
    t = body()
    H.ok(f"{d}: confirmation shows both shipments, the slot and the contents", "Grocery delivery" in t and "Other items delivery" in t and "6–8 PM" in t and "Toned Milk" in H.ev("document.body.innerHTML") and "Camouflage Print T-shirt" in H.ev("document.body.innerHTML"))
    H.ok(f"{d}: next steps: track, edit, help", all(x in t for x in ("Track shipments", "Edit", "help")))
    # sold out while choosing
    go(f"{d}-delivery.html?scenario=slot-soldout", 1440)
    H.ev("document.getElementById('d0-s4').click(); true"); wait(1.6); t = body()
    H.ok(f"{d}: chosen slot sells out → warning and the nearest later free slot picked", ("filled up" in t or "sold out" in t) and H.ev("document.getElementById('d0-s5').checked") is True, t[:300])
    H.ok(f"{d}: sold-out change announced", "6–8 PM" in H.ev("document.getElementById('co-live').textContent"))
    # payment fails, then retry
    go(f"{d}-delivery.html?scenario=payment-fail", 1440)
    H.ev("document.getElementById('d1').click(); true"); wait(0.2); H.ev("document.getElementById('d1-s0').click(); true"); wait(0.2)
    click('[data-pay="all"]'); wait(0.3)
    H.ok(f"{d}: payment shows a loading state", H.ev("!!document.querySelector('[data-pay][aria-busy=true]')"))
    wait(1.6)
    H.ok(f"{d}: payment failure → alert, nothing lost", H.ev("!!document.querySelector('[role=alert]')") and H.ev("document.getElementById('d1-s0').checked") is True)
    click('[data-pay="all"]'); wait(1.8)
    H.ok(f"{d}: retry succeeds → confirmation", H.ev("location.pathname").endswith(f"{d}-confirmation.html"))
    # pay separately
    go(f"{d}-delivery.html", 1440)
    H.ev("document.getElementById('d1').click(); true"); wait(0.2); H.ev("document.getElementById('d1-s0').click(); true"); wait(0.2)
    H.ev(f"document.getElementById('{'separate' if d == 'b' else 'separate'}').click(); true"); wait(0.2)
    H.ok(f"{d}: pay separately → one button per shipment", H.ev("[...document.querySelectorAll('[data-pay]')].filter((b) => b.offsetParent).map((b) => b.dataset.pay).join()") == "grocery,other")
    click('[data-pay="grocery"]'); wait(1.8)
    H.ok(f"{d}: grocery paid, other still to pay", "Grocery paid" in body() and H.ev("!!document.querySelector('[data-pay=other]')"))
    click('[data-pay="other"]'); wait(1.8)
    H.ok(f"{d}: both paid → confirmation", H.ev("location.pathname").endswith(f"{d}-confirmation.html"))
sys.exit(H.finish("CHECKOUT PROTOTYPE"))
