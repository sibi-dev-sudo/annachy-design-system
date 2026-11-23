"""Minimal stdlib Chrome DevTools Protocol harness. Serves the project root (current directory) over 127.0.0.1 only.
Chrome path: env ANNACHY_CHROME, else the default Windows install. The temporary browser profile is always deleted."""
import atexit, base64, functools, shutil, http.server, json, os, socket, struct, subprocess, sys, tempfile, threading, time, urllib.request
sys.stdout.reconfigure(encoding="utf-8")

class _Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
    def handle(self):
        try: super().handle()
        except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError): pass

CHROME = os.environ.get("ANNACHY_CHROME", r"C:\Program Files\Google\Chrome\Application\chrome.exe")

def stop_chrome(proc, profile):
    """Terminate Chrome and delete its temporary profile (best effort, retried while files unlock)."""
    if proc and proc.poll() is None:
        proc.terminate()
        try: proc.wait(10)
        except subprocess.TimeoutExpired: proc.kill(); proc.wait(10)
    for _ in range(20):
        if not profile or not os.path.exists(profile): return
        shutil.rmtree(profile, ignore_errors=True); time.sleep(0.2)

class Harness:
    def __init__(self, width=1600, height=1200):
        self.srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(_Quiet, directory=os.getcwd()))
        threading.Thread(target=self.srv.serve_forever, daemon=True).start()
        self.base = f"http://127.0.0.1:{self.srv.server_address[1]}"
        s = socket.socket(); s.bind(("127.0.0.1", 0)); port = s.getsockname()[1]; s.close()
        self.profile = tempfile.mkdtemp(prefix="annachy-cdp-")
        self.chrome = subprocess.Popen([CHROME, "--headless=new", "--disable-gpu", "--no-first-run",
                                        f"--user-data-dir={self.profile}", f"--remote-debugging-port={port}",
                                        f"--window-size={width},{height}", "about:blank"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        atexit.register(self.close)
        for _ in range(100):
            try: targets = json.load(urllib.request.urlopen(f"http://127.0.0.1:{port}/json/list")); break
            except Exception: time.sleep(0.1)
        url = next(t for t in targets if t["type"] == "page")["webSocketDebuggerUrl"]
        host, path = url[len("ws://"):].split("/", 1); h, p = host.split(":")
        self.s = socket.create_connection((h, int(p))); key = base64.b64encode(os.urandom(16)).decode()
        self.s.sendall(f"GET /{path} HTTP/1.1\r\nHost: {host}\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n".encode())
        buf = b""
        while b"\r\n\r\n" not in buf: buf += self.s.recv(1)
        self.id = 0; self.events = []; self.fails = []; self.checks = 0
        for d in ("Page", "Runtime", "Network", "Log", "Accessibility", "DOM"): self.call(f"{d}.enable")
        self.call("Emulation.setFocusEmulationEnabled", enabled=True)   # keep the page focused / visible during long runs

    def _exact(self, n):
        b = b""
        while len(b) < n: b += self.s.recv(n - len(b))
        return b
    def _recv(self):
        data = b""
        while True:
            hdr = self._exact(2); fin = hdr[0] & 0x80; ln = hdr[1] & 0x7F
            if ln == 126: ln = struct.unpack(">H", self._exact(2))[0]
            elif ln == 127: ln = struct.unpack(">Q", self._exact(8))[0]
            data += self._exact(ln)
            if fin: return json.loads(data)
    def call(self, method, **params):
        self.id += 1; msg = json.dumps({"id": self.id, "method": method, "params": params}).encode()
        mask = os.urandom(4); n = len(msg)
        hdr = bytes([0x81]) + (bytes([0x80 | n]) if n < 126 else (bytes([0x80 | 126]) + struct.pack(">H", n) if n < 65536 else bytes([0x80 | 127]) + struct.pack(">Q", n)))
        self.s.sendall(hdr + mask + bytes(b ^ mask[i % 4] for i, b in enumerate(msg)))
        while True:
            m = self._recv()
            if m.get("id") == self.id:
                if "error" in m: raise RuntimeError(f"{method}: {m['error']}")
                return m.get("result", {})
            self.events.append(m)

    # ------------------------------------------------------------ helpers
    def ok(self, name, cond, detail=""):
        self.checks += 1
        if not cond: self.fails.append(f"{name} {detail}")
    def ev(self, expr):
        r = self.call("Runtime.evaluate", expression=expr, returnByValue=True, awaitPromise=True)
        if "exceptionDetails" in r: raise RuntimeError(f"eval: {expr[:100]} -> {r['exceptionDetails'].get('exception', {}).get('description', r['exceptionDetails'].get('text'))}")
        return r["result"].get("value")
    def navigate(self, path):
        self.events.clear(); self.call("Page.navigate", url=f"{self.base}/{path}")
        for _ in range(200):
            if self.ev("document.readyState") == "complete": break
            time.sleep(0.05)
        self.ev("document.fonts.ready.then(() => true)"); time.sleep(0.3)
    def problems(self):
        errs = []
        for e in self.events:
            m = e.get("method")
            if m == "Runtime.exceptionThrown": errs.append("exception: " + str(e["params"]["exceptionDetails"].get("exception", {}).get("description", "")))
            if m == "Log.entryAdded" and e["params"]["entry"]["level"] == "error": errs.append("log: " + e["params"]["entry"]["text"])
            if m == "Runtime.consoleAPICalled" and e["params"]["type"] == "error": errs.append("console.error")
            if m == "Network.loadingFailed":
                url = next((x["params"]["request"]["url"] for x in self.events if x.get("method") == "Network.requestWillBeSent" and x["params"]["requestId"] == e["params"]["requestId"]), "?")
                errs.append(f"load failed: {e['params'].get('errorText', '')} {url} ({e['params'].get('type', '')})")
            if m == "Network.responseReceived" and e["params"]["response"]["status"] >= 400: errs.append(f"HTTP {e['params']['response']['status']} {e['params']['response']['url']}")
        fav = any("favicon.ico" in e for e in errs)
        errs = [e for e in errs if "favicon.ico" not in e]
        line = "log: Failed to load resource: the server responded with a status of 404 (File not found)"
        if fav and line in errs: errs.remove(line)
        return errs
    KEYS = {"Tab": (9, None), "Enter": (13, "\r"), " ": (32, " "), "Escape": (27, None), "ArrowDown": (40, None), "ArrowUp": (38, None),
            "Home": (36, None), "End": (35, None), "Backspace": (8, None)}
    def key(self, k, ctrl=False, shift=False, alt=False):
        vk, text = self.KEYS.get(k, (ord(k.upper()) if len(k) == 1 else 0, k if len(k) == 1 else None))
        code = {"Enter": "Enter", " ": "Space", "Escape": "Escape", "Tab": "Tab"}.get(k, k if len(k) > 1 else f"Key{k.upper()}")
        mods = (2 if ctrl else 0) | (8 if shift else 0) | (1 if alt else 0)
        p = dict(key=k, code=code, windowsVirtualKeyCode=vk, nativeVirtualKeyCode=vk, modifiers=mods)
        if text and not ctrl: self.call("Input.dispatchKeyEvent", type="keyDown", text=text, **p)
        else: self.call("Input.dispatchKeyEvent", type="rawKeyDown", **p)
        self.call("Input.dispatchKeyEvent", type="keyUp", **p)
    def type(self, s):
        for ch in s: self.key(ch)
    def center(self, sel):
        return self.ev(f"(() => {{ const r = document.querySelector({json.dumps(sel)}).getBoundingClientRect(); return [r.left + r.width / 2, r.top + r.height / 2]; }})()")
    def mouse(self, t, x, y, button="none", clicks=0): self.call("Input.dispatchMouseEvent", type=t, x=x, y=y, button=button, clickCount=clicks)
    def click(self, sel):
        x, y = self.center(sel); self.mouse("mouseMoved", x, y); self.mouse("mousePressed", x, y, "left", 1); self.mouse("mouseReleased", x, y, "left", 1)
    def hover(self, sel): x, y = self.center(sel); self.mouse("mouseMoved", x, y)
    def tap(self, sel):
        x, y = self.center(sel)
        self.call("Input.dispatchTouchEvent", type="touchStart", touchPoints=[{"x": x, "y": y}])
        self.call("Input.dispatchTouchEvent", type="touchEnd", touchPoints=[])
    def active(self): return self.ev("document.activeElement && document.activeElement.id")
    def ax(self):
        nodes = self.call("Accessibility.getFullAXTree")["nodes"]; doc = self.call("DOM.getDocument", depth=-1)
        by = {n["backendDOMNodeId"]: n for n in nodes if "backendDOMNodeId" in n}
        def get(sel):
            nid = self.call("DOM.querySelector", nodeId=doc["root"]["nodeId"], selector=sel)["nodeId"]
            if not nid: return None
            b = self.call("DOM.describeNode", nodeId=nid)["node"]["backendNodeId"]; n = by.get(b, {})
            return {"role": n.get("role", {}).get("value"), "name": n.get("name", {}).get("value"), "description": n.get("description", {}).get("value"),
                    **{p["name"]: p["value"].get("value") for p in n.get("properties", [])}}
        return get
    def close(self):
        if getattr(self, "_closed", False): return
        self._closed = True
        try: self.s.close()
        except Exception: pass
        stop_chrome(self.chrome, self.profile); self.srv.shutdown()
    def finish(self, title):
        self.close()
        print(f"{title}: {self.checks} checks · failures: {len(self.fails)}")
        for f in self.fails: print("  FAIL", f)
        print(f"{title} RESULT:", "PASS" if not self.fails else "FAIL")
        return 1 if self.fails else 0
