"""R3 closure audit — real-browser checks via the Chrome DevTools Protocol (stdlib-only websocket client).
Serves the project root on 127.0.0.1, drives headless Chrome with real keyboard/mouse input, reads the
accessibility tree, and loads every showcase page. Run from project root. Exit 1 on failure."""
import atexit, base64, functools, http.server, json, os, socket, struct, subprocess, sys, tempfile, threading, time, urllib.request
sys.stdout.reconfigure(encoding="utf-8")
sys.dont_write_bytecode = True; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cdp_lib import CHROME, stop_chrome
ROOT = os.getcwd()
class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
    def handle(self):
        try: super().handle()
        except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError): pass   # Chrome closes keep-alive sockets on shutdown
srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=ROOT))
threading.Thread(target=srv.serve_forever, daemon=True).start()
BASE = f"http://127.0.0.1:{srv.server_address[1]}"
s = socket.socket(); s.bind(("127.0.0.1", 0)); DBG = s.getsockname()[1]; s.close()
PROFILE = tempfile.mkdtemp(prefix="annachy-cdp-")
chrome = subprocess.Popen([CHROME, "--headless=new", "--disable-gpu", "--no-first-run",
                           f"--user-data-dir={PROFILE}", f"--remote-debugging-port={DBG}",
                           "--window-size=1600,1200", "about:blank"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
atexit.register(lambda: stop_chrome(chrome, PROFILE))
for _ in range(100):
    try: targets = json.load(urllib.request.urlopen(f"http://127.0.0.1:{DBG}/json/list")); break
    except Exception: time.sleep(0.1)
ws_url = next(t for t in targets if t["type"] == "page")["webSocketDebuggerUrl"]

class WS:
    def __init__(self, url):
        host, path = url[len("ws://"):].split("/", 1); h, p = host.split(":")
        self.s = socket.create_connection((h, int(p))); key = base64.b64encode(os.urandom(16)).decode()
        self.s.sendall(f"GET /{path} HTTP/1.1\r\nHost: {host}\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n".encode())
        buf = b""
        while b"\r\n\r\n" not in buf: buf += self.s.recv(1)
        self.id = 0; self.events = []
    def _recv_exact(self, n):
        b = b""
        while len(b) < n: b += self.s.recv(n - len(b))
        return b
    def _recv(self):
        data = b""
        while True:
            h = self._recv_exact(2); fin = h[0] & 0x80; ln = h[1] & 0x7F
            if ln == 126: ln = struct.unpack(">H", self._recv_exact(2))[0]
            elif ln == 127: ln = struct.unpack(">Q", self._recv_exact(8))[0]
            data += self._recv_exact(ln)
            if fin: return json.loads(data)
    def call(self, method, **params):
        self.id += 1; msg = json.dumps({"id": self.id, "method": method, "params": params}).encode()
        mask = os.urandom(4); hdr = bytes([0x81])
        n = len(msg)
        hdr += bytes([0x80 | n]) if n < 126 else (bytes([0x80 | 126]) + struct.pack(">H", n) if n < 65536 else bytes([0x80 | 127]) + struct.pack(">Q", n))
        self.s.sendall(hdr + mask + bytes(b ^ mask[i % 4] for i, b in enumerate(msg)))
        while True:
            m = self._recv()
            if m.get("id") == self.id:
                if "error" in m: raise RuntimeError(f"{method}: {m['error']}")
                return m.get("result", {})
            self.events.append(m)

ws = WS(ws_url)
for d in ("Page", "Runtime", "Network", "Log", "Accessibility", "DOM"): ws.call(f"{d}.enable")
fails, checks = [], [0]
def ok(name, cond, detail=""):
    checks[0] += 1
    if not cond: fails.append(f"{name} {detail}")
def ev(expr):
    r = ws.call("Runtime.evaluate", expression=expr, returnByValue=True, awaitPromise=True)
    if "exceptionDetails" in r: raise RuntimeError(f"eval error: {expr[:80]} -> {r['exceptionDetails'].get('text')}")
    return r["result"].get("value")
def navigate(url):
    ws.events.clear(); ws.call("Page.navigate", url=url)
    for _ in range(200):
        if ev("document.readyState") == "complete": break
        time.sleep(0.05)
    ev("document.fonts.ready.then(() => true)"); time.sleep(0.3)
def problems():
    errs = []
    for e in ws.events:
        m = e.get("method")
        if m == "Runtime.exceptionThrown": errs.append("exception: " + e["params"]["exceptionDetails"].get("text", ""))
        if m == "Log.entryAdded" and e["params"]["entry"]["level"] == "error": errs.append("log: " + e["params"]["entry"]["text"])
        if m == "Runtime.consoleAPICalled" and e["params"]["type"] == "error": errs.append("console.error")
        if m == "Network.loadingFailed": errs.append("load failed: " + e["params"].get("errorText", ""))
        if m == "Network.responseReceived" and e["params"]["response"]["status"] >= 400: errs.append(f"HTTP {e['params']['response']['status']} {e['params']['response']['url']}")
    # the browser's automatic /favicon.ico request is not a page resource (no favicon is referenced) — ignored
    fav = any("favicon.ico" in e for e in errs)
    errs = [e for e in errs if "favicon.ico" not in e]
    if fav:   # remove exactly one paired console line for the favicon 404
        line = "log: Failed to load resource: the server responded with a status of 404 (File not found)"
        if line in errs: errs.remove(line)
    return errs
def key(k, code=None, text=None, vk=None):
    p = dict(key=k, code=code or k, windowsVirtualKeyCode=vk or 0, nativeVirtualKeyCode=vk or 0)
    ws.call("Input.dispatchKeyEvent", type="rawKeyDown" if not text else "keyDown", **p, **({"text": text} if text else {}))
    ws.call("Input.dispatchKeyEvent", type="keyUp", **p)
TAB = dict(k="Tab", code="Tab", vk=9); SPACE = dict(k=" ", code="Space", text=" ", vk=32); ENTER = dict(k="Enter", code="Enter", text="\r", vk=13)
DOWN = dict(k="ArrowDown", code="ArrowDown", vk=40)
def center(sel): return ev(f"(() => {{ const r = document.querySelector('{sel}').getBoundingClientRect(); return [r.left + r.width / 2, r.top + r.height / 2]; }})()")
def mouse(t, x, y, button="none", clicks=0): ws.call("Input.dispatchMouseEvent", type=t, x=x, y=y, button=button, clickCount=clicks)
cs = lambda sel, prop, pseudo="": ev(f"getComputedStyle(document.querySelector('{sel}'){', ' + repr(pseudo) if pseudo else ''})['{prop}']")
active = lambda: ev("document.activeElement && document.activeElement.id")

# ============ 1. Interaction fixture ============
navigate(f"{BASE}/tests/fixtures/r3-interaction.html")
ok("fixture loads without errors", not problems(), problems())
ok("annachy.js exports exactly initCheckboxes, R4 initDropdowns/initTooltips and the AUD-1 lifecycle API", ev("window.__annachy && window.__annachy.exports.sort().join()") == "destroyDropdowns,getDropdown,initCheckboxes,initDropdowns,initTooltips", ev("window.__annachy && window.__annachy.exports.sort().join()"))
ok("checkbox.js initialises on load (indeterminate)", ev("document.getElementById('cb-mixed').indeterminate") is True)
ok("Multi-select paint (checked fill)", cs("#cb-mixed ~ .annachy-checkbox__box", "backgroundColor") == "rgb(0, 79, 235)")
# 1a. Tab order: disabled controls skipped, radio group is one stop, loading (aria-disabled) stays focusable
ev("document.activeElement.blur(); window.focus()")
order = []
for _ in range(10):
    key(**TAB); order.append(active())
want = ["btn-primary", "btn-icon", "btn-loading", "grad", "in-outline", "in-filled", "in-error", "cb", "cb-mixed", "rb-a"]
ok("Tab order (disabled skipped, radio group single stop)", order == want, f"{order}")
key(**TAB); ok("Tab reaches switch", active() == "tg", active())
# 1b. focus visuals from real keyboard focus (tab_to presses Tab until the target is focused)
def tab_to(id_):
    for _ in range(25):
        if active() == id_: return True
        key(**TAB)
    return active() == id_
ok("tab_to btn-primary", tab_to("btn-primary"))
ok("Button :focus-visible 2px #003fbc", (cs("#btn-primary", "borderTopWidth"), cs("#btn-primary", "borderTopColor")) == ("2px", "rgb(0, 63, 188)"), (cs("#btn-primary", "borderTopWidth"), cs("#btn-primary", "borderTopColor")))
ok("Button focus outline suppressed (Figma border is the indicator)", cs("#btn-primary", "outlineStyle") == "none")
key(**ENTER); key(**SPACE)
ok("Enter and Space activate button", ev("window.__clicks['btn-primary']") == 2, ev("JSON.stringify(window.__clicks)"))
tab_to("btn-loading")
ok("Loading button keeps browser outline (no Figma Loading+Focus)", cs("#btn-loading", "outlineStyle") != "none", cs("#btn-loading", "outlineStyle"))
key(**ENTER); ok("aria-disabled loading button still fires click (consumer must guard)", ev("window.__clicks['btn-loading'] || 0") == 1)
tab_to("grad"); ok("Gradient focus stroke 2px Blue/500", "2px inset" in cs("#grad", "boxShadow") and "rgb(0, 79, 235)" in cs("#grad", "boxShadow"), cs("#grad", "boxShadow"))
ok("Gradient size-40 focus fill Blue/600→Blue/400", "rgb(0, 63, 188)" in cs("#grad", "backgroundImage"))
tab_to("in-outline")
ok("Outline input focus border raw #3a6ff7", cs("#in-outline", "outlineStyle") == "none" and ev("getComputedStyle(document.getElementById('in-outline').closest('.annachy-input__field')).borderTopColor") == "rgb(58, 111, 247)")
for ch in "ab": key(k=ch, code=f"Key{ch.upper()}", text=ch, vk=ord(ch.upper()))
ok("typing enters value", ev("document.getElementById('in-outline').value") == "ab")
tab_to("in-filled")
ok("Outline Filled after blur (Base/Black border)", ev("getComputedStyle(document.getElementById('in-outline').closest('.annachy-input__field')).borderTopColor") == "rgb(11, 12, 15)")
ok("Filled input focus (Blue/600, Blue-Grey/50)", ev("(() => { const f = getComputedStyle(document.getElementById('in-filled-field')); return f.borderTopColor + '|' + f.backgroundColor; })()") == "rgb(0, 63, 188)|rgb(246, 247, 249)")
tab_to("in-error")
ok("Error wins over Focused (aria-invalid)", ev("getComputedStyle(document.getElementById('in-error').closest('.annachy-input__field')).borderTopColor") == "rgb(231, 43, 35)")
tab_to("cb")
ok("Checkbox keyboard focus → Focus box", cs("#cb ~ .annachy-checkbox__box", "backgroundColor") == "rgb(235, 242, 255)")
key(**SPACE); ok("Space checks checkbox", ev("document.getElementById('cb').checked") is True)
ok("D-20 focus+checked keeps checked fill", cs("#cb ~ .annachy-checkbox__box", "backgroundColor") == "rgb(0, 79, 235)" and cs("#cb ~ .annachy-checkbox__box", "borderTopWidth") == "2px")
tab_to("cb-mixed"); key(**SPACE)
ok("Space on mixed checkbox clears indeterminate and checks", ev("[document.getElementById('cb-mixed').indeterminate, document.getElementById('cb-mixed').checked].join()") == "false,true")
key(**TAB); ok("radio group focus lands on checked radio", active() == "rb-a", active())
key(**DOWN); ok("ArrowDown selects next radio", ev("document.getElementById('rb-b').checked") is True and active() == "rb-b")
key(**DOWN); ok("ArrowDown skips disabled radio (wraps to first)", active() == "rb-a", active())
key(**TAB); ok("Tab to switch", active() == "tg", active())
thumbx = "document.querySelector('#tg ~ .annachy-toggle__track .annachy-toggle__thumb').getBoundingClientRect().left - document.querySelector('#tg ~ .annachy-toggle__track').getBoundingClientRect().left"
x0 = ev(thumbx); ok("Focus Off thumb x 3", x0 == 3, x0)
key(**SPACE); ok("Space toggles switch", ev("document.getElementById('tg').checked") is True)
x1 = ev(thumbx); ok("Focus On thumb x 18.5", x1 == 18.5, x1)
# 1c. real mouse hover / press
ev("document.activeElement.blur()")
x, y = center("#btn-disabled"); mouse("mouseMoved", x, y)
ok("hover on disabled button keeps Disabled", cs("#btn-disabled", "color") == "rgb(191, 196, 207)")
x, y = center("#btn-primary"); mouse("mouseMoved", x, y)
ok("real :hover → Primary Hover #003fbc", cs("#btn-primary", "backgroundColor") == "rgb(0, 63, 188)")
mouse("mousePressed", x, y, "left", 1)
ok("real :active → Primary Pressed #3372ef", cs("#btn-primary", "backgroundColor") == "rgb(51, 114, 239)")
mouse("mouseReleased", x, y, "left", 1)
ok("mouse focus does not show focus border (:focus-visible heuristics)", cs("#btn-primary", "borderTopWidth") == "0px")
x, y = center("#in-filled-field"); mouse("mouseMoved", x, y)
ok("real hover on Filled field → Blue/500 border", ev("getComputedStyle(document.getElementById('in-filled-field')).borderTopColor") == "rgb(0, 79, 235)")
x, y = center("#tg ~ .annachy-toggle__track"); mouse("mouseMoved", x, y)
ok("real hover on switch (On) → #003fbc", cs("#tg ~ .annachy-toggle__track", "backgroundColor") == "rgb(0, 63, 188)")
x, y = center('label[for="cb-disabled"]'); mouse("mousePressed", x, y, "left", 1); mouse("mouseReleased", x, y, "left", 1)
ok("click on disabled checkbox label does nothing", ev("document.getElementById('cb-disabled').checked") is False)
x, y = center("#in-disabled"); mouse("mousePressed", x, y, "left", 1); mouse("mouseReleased", x, y, "left", 1)
ok("disabled input cannot be focused by click", active() != "in-disabled")
x, y = center("#rb-b ~ .annachy-radio__circle"); mouse("mousePressed", x, y, "left", 1); mouse("mouseReleased", x, y, "left", 1)
ok("click on radio circle selects (input covers circle)", ev("document.getElementById('rb-b').checked") is True)

# 1d. accessibility tree (names, roles, descriptions, states)
ax = ws.call("Accessibility.getFullAXTree")["nodes"]
node_by_dom = {}
for n in ax:
    if "backendDOMNodeId" in n: node_by_dom[n["backendDOMNodeId"]] = n
doc = ws.call("DOM.getDocument", depth=-1)
def ax_for(id_):
    nid = ws.call("DOM.querySelector", nodeId=doc["root"]["nodeId"], selector=f"#{id_}")["nodeId"]
    bid = ws.call("DOM.describeNode", nodeId=nid)["node"]["backendNodeId"]
    n = node_by_dom.get(bid, {})
    props = {p["name"]: p["value"].get("value") for p in n.get("properties", [])}
    return n.get("role", {}).get("value"), n.get("name", {}).get("value"), n.get("description", {}).get("value"), props
EXPECT = [
 ("btn-primary", "button", "Button", None, {}), ("btn-icon", "button", "Home", None, {}),
 ("btn-loading", "button", "Saving", None, {"busy": True, "disabled": True}), ("btn-disabled", "button", "Disabled", None, {"disabled": True}),
 ("grad", "button", "Gradient", None, {}),
 ("in-outline", "textbox", "Email", "Work address We never share it", {}), ("in-filled", "textbox", "Name", "Full name As on your ID", {}),
 ("in-error", "textbox", "Code", "Code is too short", {"invalid": "true"}), ("in-disabled", "textbox", "Locked", None, {"disabled": True}),
 ("cb", "checkbox", "Accept terms", "Required", {}), ("cb-disabled", "checkbox", "Unavailable", None, {"disabled": True}),
 ("rb-a", "radio", "Standard", "3–5 days", {}), ("rb-c", "radio", "Drone", None, {"disabled": True}),
 ("tg", "switch", "Notifications", "Email me updates", {}), ("tg-disabled", "switch", "Locked switch", None, {"disabled": True}),
]
for id_, role, name, desc, props in EXPECT:
    r, nm, d, p = ax_for(id_)
    ok(f"AX {id_} role", r == role, f"{r}"); ok(f"AX {id_} name", nm == name, f"{nm!r}")
    if desc: ok(f"AX {id_} description", d == desc, f"{d!r}")
    for k, v in props.items(): ok(f"AX {id_} {k}", p.get(k) == v, f"{p.get(k)!r}")
ok("AX mixed checkbox state", ax_for("cb-mixed")[3].get("checked") in ("mixed", "true"), ax_for("cb-mixed")[3].get("checked"))
ok("AX switch checked", ax_for("tg")[3].get("checked") == "true")
ok("AX radio group has name", any(n.get("role", {}).get("value") in ("group", "radiogroup") and n.get("name", {}).get("value") == "Delivery" for n in ax))
ok("AX decorative parts hidden (box/track/dots aria-hidden)", ev("[...document.querySelectorAll('.annachy-checkbox__box,.annachy-radio__circle,.annachy-toggle__track,.annachy-button__loading,.annachy-button__icon')].every(e => e.getAttribute('aria-hidden') === 'true')") is True)

# ============ 2. Every showcase page over HTTP ============
PAGES = {"showcase/index.html": None, "showcase/foundations/colors.html": None, "showcase/foundations/typography.html": None,
         "showcase/foundations/effects.html": None, "showcase/foundations/grid.html": None, "showcase/foundations/dimensions.html": None,
         "showcase/foundations/base.html": None,
         "showcase/components/button.html": (".annachy-button", 432 + 9), "showcase/components/button-gradient.html": (".annachy-button-gradient", 55 + 4),
         "showcase/components/input.html": (".annachy-input", 325 + 2), "showcase/components/checkbox.html": (".annachy-checkbox", 126 + 1),
         "showcase/components/radio.html": (".annachy-radio", 108 + 2), "showcase/components/toggle.html": (".annachy-toggle", 180 + 1)}
for page, expect in PAGES.items():
    navigate(f"{BASE}/{page}")
    ok(f"{page} loads without console/network errors", not problems(), problems())
    ok(f"{page} stylesheet applied", ev("getComputedStyle(document.documentElement).getPropertyValue('--annachy-color-blue-500').trim()") == "#004feb")
    if expect:
        cnt = ev(f"document.querySelectorAll('{expect[0]}').length")
        ok(f"{page} instance count", cnt == expect[1], f"{cnt} != {expect[1]}")
    links = ev("[...document.querySelectorAll('a[href]')].map(a => a.href).filter(h => h.startsWith(location.origin))")
    for href in links:
        try: code = urllib.request.urlopen(href.split("#")[0]).status
        except Exception as e: code = str(e)
        ok(f"{page} link {href[len(BASE):]}", code == 200, code)
navigate(f"{BASE}/showcase/components/checkbox.html")
ms = ev("[...document.querySelectorAll('.annachy-checkbox__input[data-indeterminate=\"true\"]')].map(i => i.indeterminate && getComputedStyle(i.nextElementSibling).backgroundColor)")
ok("showcase Multi-select examples indeterminate + checked fill (HTTP)", len(ms) == 18 and all(c == "rgb(0, 79, 235)" for c in ms), f"{len(ms)} {set(ms)}")

stop_chrome(chrome, PROFILE); srv.shutdown()
print(f"CDP CHECKS: {checks[0]} · failures: {len(fails)}")
for f in fails: print("  FAIL", f)
print("R3 CLOSURE CDP RESULT:", "PASS" if not fails else "FAIL")
sys.exit(1 if fails else 0)
