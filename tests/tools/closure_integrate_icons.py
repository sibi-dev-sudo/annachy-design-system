"""Closure: fill the remaining in-scope screen icon placeholders and the Annachy logotype.

Evidence: verbatim design context per node in %TEMP%/annachy-closure-staging/dc (asset links removed) and the staged
original SVGs (assets/). Each artwork is copied byte-for-byte to showcase/screens/assets/vectors/ (refuses to overwrite
different content) and placed with Figma's own wrapper (inset) under the R10 vector contract (data-annachy-vector,
data-vec-w/h = the drawn size). Parent transforms that the node's own design context does not show were read from the
parent's design context (1375:30951, 1375:31080, 1375:31225). One artwork is an exact library icon and reuses it.
Idempotent. Run from the project root:  python -I tests/tools/closure_integrate_icons.py [--dry-run]
"""
import hashlib, os, re, shutil, sys
sys.stdout.reconfigure(encoding="utf-8")
ST = os.path.join(os.environ["TEMP"], "annachy-closure-staging")
DEST = "showcase/screens/assets/vectors"
DRY = "--dry-run" in sys.argv
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
P = "showcase/screens/"
# placeholder node -> screen file
NODES = {
    "pdp/mobile.html": ["1201:9829"],
    "pdp/pdp-v1.html": ["1280:10436", "I1280:10449;1546:27825", "1280:10453", "1280:10467", "1280:10486", "1280:10674"],
    "sample-screen/desktop-pdp-1375-30858.html": ["1375:31338", "1375:31344", "1375:31350", "1375:31355", "1375:31358", "1375:31369",
        "I1375:31375;17:1154", "I1375:31376;17:1154", "I1375:31377;17:1154", "I1375:31378;17:1154", "1375:31381", "1375:31388",
        "1375:30900", "1375:30902", "1375:30912", "1375:30914", "1375:30916", "1375:30918", "1375:30920", "1375:30940", "1375:30952",
        "1375:30955", "1375:31010", "1375:31020", "1375:31051", "1375:31059", "1375:31069", "1375:31082", "1375:31088", "1375:31116",
        "1375:31159", "1375:31227", "1375:31283", "1375:31286", "1375:31293"],
    "sample-screen/job-listing-page-1629-11987.html": ["1629:11992", "1629:12002", "1629:12009"],
    "sample-screen/mobile-pdp-1608-7090.html": ["1608:7143", "1608:7186", "1608:7200", "1608:7219"],
    "sample-screen/mobile-putaway-1627-11756.html": ["1627:11761", "1627:11771"],
}
# transforms from the parents' design context (flex-centred, same box): Tailwind -scale-y-100 rotate-180 / -scale-y-100 / -rotate-90
XFORM = {"1375:30955": "rotate(180deg) scaleY(-1)", "1375:31088": "scaleY(-1)", "1375:31227": "rotate(-90deg)"}
# exact library icon (closure_icon_match.py: IoU 1.000; same geometry at the 24 px slot: bars x 3.25-20.75, 1.5 px) and colour
LIBRARY = {"1375:31369": ("editor-hamburger-menu", "outline", "#3D4451")}


def dcname(n): return n.replace(":", "-").replace(";", "_")


def wrapper(node):
    code = open(os.path.join(ST, "dc", dcname(node) + ".tsx"), encoding="utf-8").read()
    asset = re.search(r"`\$\{assetPathPrefix\}/([\w.]+)`", code).group(1)
    body = code[code.index("export default"):]
    m = re.search(r'<div className="absolute inset-\[([^\]]+)\]">\s*<img', body)
    inset = m.group(1).replace("_", " ") if m else "0"
    if not m: assert re.search(r'<img alt="" className="absolute block inset-0 max-w-none size-full"', body), node
    return asset, inset


def pct(v, size):
    v = v.strip()
    return size * float(v[:-1]) / 100 if v.endswith("%") else float(v.replace("px", "") or 0)


copied, placed, skipped, problems = [], [], [], []
for rel, nodes in NODES.items():
    path = P + rel; s = open(path, encoding="utf-8").read()
    for node in nodes:
        pat = re.compile(r'(<span\b[^>]*data-figma-node="' + re.escape(node) + r'"[^>]*)>(\s*)</span>')
        m = pat.search(s)
        if m and "data-annachy-" in m.group(1): m = None   # library slots stay empty in HTML (filled at runtime)
        if not m:
            if re.search(r'data-figma-node="' + re.escape(node) + r'"[^>]*data-annachy-(vector|icon)', s): skipped.append(node); continue
            problems.append(f"{node}: placeholder not found / not empty in {rel}"); continue
        head = m.group(1)
        if node in LIBRARY:
            name, style, colour = LIBRARY[node]
            head = re.sub(r'style="([^"]*)"', lambda mm: f'style="{mm.group(1).rstrip("; ")}; color:{colour};"', head, count=1)
            s = s[:m.start()] + head + f' data-annachy-icon="{name}" data-annachy-icon-style="{style}"></span>' + s[m.end():]
            placed.append((node, "library " + name)); continue
        asset, inset = wrapper(node)
        aid = asset.split(".")[0]
        fname = ("logo-annachy-" if node == "1375:31293" else "icon-") + asset
        src, dst = os.path.join(ST, "assets", asset), os.path.join(DEST, fname)
        if os.path.exists(dst):
            if sha(dst) != sha(src): sys.exit(f"REFUSING: {dst} exists with different content")
        elif not DRY:
            shutil.copyfile(src, dst); copied.append(fname)
        meta = open(os.path.join(ST, "meta", dcname(node) + ".xml"), encoding="utf-8").read()   # Figma's own node size
        w = float(re.search(r'width="([\d.]+)"', meta).group(1)); h = float(re.search(r'height="([\d.]+)"', meta).group(1))
        t, r_, b, l = (inset.split() + inset.split() * 3)[:4] if len(inset.split()) == 1 else inset.split()
        vw, vh = w - pct(l, w) - pct(r_, w), h - pct(t, h) - pct(b, h)
        img = f'<img class="scr-vec__art" src="../assets/vectors/{fname}" alt="">'
        inner = f'<span class="scr-vec__inset" style="inset:{inset}">{img}</span>'
        if node in XFORM:
            inner = f'<span class="scr-vec scr-vec--xform" style="position:absolute;inset:0;transform:{XFORM[node]}">{inner}</span>'
        attrs = f' data-annachy-vector="{fname}" data-vec-artwork="{aid}" data-vec-w="{vw:g}" data-vec-h="{vh:g}"'
        s = s[:m.start()] + head + attrs + ">" + inner + "</span>" + s[m.end():]
        placed.append((node, fname))
    if not DRY: open(path, "w", encoding="utf-8").write(s)
print(f"artworks copied: {len(copied)} · placeholders filled: {len(placed)} · already filled: {len(skipped)} · problems: {len(problems)}" + (" [DRY RUN]" if DRY else ""))
for p in problems: print("  PROBLEM", p)
if "-v" in sys.argv:
    for p in placed: print("  ", *p)
