"""Serve the project root locally, load the R1 fixture in headless Chrome, and check showcase links.
Run from project root. Local only (127.0.0.1)."""
import http.server, threading, subprocess, functools, re, sys, urllib.request, html.parser, os, tempfile
sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.getcwd()
Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT)
class Quiet(Handler.func):  # type: ignore
    def log_message(self, *a): pass
srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=ROOT))
port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
base = f"http://127.0.0.1:{port}"
sys.dont_write_bytecode = True; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cdp_lib import CHROME
import shutil
ok = True

def dump(url):
    prof = tempfile.mkdtemp(prefix="annachy-chrome-")
    try:
        r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-first-run", f"--user-data-dir={prof}",
                            "--virtual-time-budget=8000", "--dump-dom", url], capture_output=True, text=True, encoding="utf-8", timeout=120)
        return r.stdout
    finally:
        for _ in range(20):                      # always delete the temporary profile
            if not os.path.exists(prof): break
            shutil.rmtree(prof, ignore_errors=True)

# 1. fixtures
for fx in sys.argv[1:] or ("r1-token-check.html", "r2-base-check.html"):
    dom = dump(f"{base}/tests/fixtures/{fx}")
    m = re.search(r'<pre id="result" data-status="(\w+)">(.*?)</pre>', dom, re.S)
    if not m:
        print(fx, ": result element not found"); ok = False
    else:
        print(f"== {fx}: {m.group(1)}")
        print(html.unescape(m.group(2)))
        ok &= m.group(1) == "pass"

# 2. showcase pages + every referenced local asset
class Refs(html.parser.HTMLParser):
    def __init__(self): super().__init__(); self.refs = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        for k in ("href", "src"):
            if k in a and not a[k].startswith(("http", "#", "mailto")): self.refs.append(a[k])
pages = ["showcase/index.html"] + [f"showcase/foundations/{p}" for p in ("colors.html", "typography.html", "iconography.html", "effects.html", "grid.html", "dimensions.html", "base.html")]
checked = set(); broken = []
for p in pages:
    url = f"{base}/{p}"
    body = urllib.request.urlopen(url).read().decode("utf-8")
    parser = Refs(); parser.feed(body)
    for r in parser.refs:
        target = urllib.parse.urljoin(url, r)
        if target in checked: continue
        checked.add(target)
        try:
            code = urllib.request.urlopen(target).status
        except Exception as e:
            code = str(e)
        if code != 200: broken.append((target, code))
    print(f"page {p}: 200, {len(parser.refs)} refs")
print(f"unique local references checked: {len(checked)}; broken: {len(broken)}")
for b in broken: print("  BROKEN", b)
ok &= not broken

# 3. rendered showcase: computed token present on colours page
dom = dump(f"{base}/showcase/foundations/colors.html")
print("colors page rendered swatches:", dom.count('class="sc-swatch"'))

srv.shutdown()
print("BROWSER RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
