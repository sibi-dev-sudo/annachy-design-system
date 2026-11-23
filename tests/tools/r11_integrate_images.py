"""R11-0: integrate the approved product imagery into its 108 screen placeholders (internal reproduction only).

Reads docs/figma-audit/r11-0-product-imagery-manifest.json and the staging export (%TEMP%/annachy-image-staging: assets/,
dc/ = Figma design-context code with asset URLs removed). Copies each ORIGINAL asset byte-for-byte to
showcase/screens/assets/images/<assetId>.<ext> (refuses to overwrite different content) and fills each placeholder with
Figma's own image wrappers (crop boxes, offsets, clipping, stacked layers) converted from the design context.
Idempotent: a placeholder already carrying data-annachy-image / data-annachy-css is left untouched.
    python -I tests/tools/r11_integrate_images.py [--dry-run]
"""
import hashlib, json, os, re, shutil, sys
sys.stdout.reconfigure(encoding="utf-8")
sys.dont_write_bytecode = True; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import r11_jsx as J

ST = os.path.join(os.environ["TEMP"], "annachy-image-staging")
DRY = "--dry-run" in sys.argv
M = json.load(open("docs/figma-audit/r11-0-product-imagery-manifest.json", encoding="utf-8"))
DEST = "showcase/screens/assets/images"
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
# assets drawn by other (non-R11) placeholders or out of scope: never placed by R11
NOT_R11 = {"c6cc8", "7d14a", "394d3", "7d88c", "45da3", "2963b", "2e905"}
RIGHTS = {"AI-generated (Gemini file name)": "ai-generated-unverified", "product photo (SKU-style file name)": "sku-photo-unverified",
          "web download (generic file name)": "web-download-unverified", "screenshot": "screenshot-unverified",
          "emoji raster": "emoji-third-party", "unattributed": "source-unknown"}
ROOT_KEEP = re.compile(r"^(background|overflow|border-radius|opacity)")

_cache = {}

def staged(aid):
    """The staged original for an asset id (Figma's asset link extension is not always the real format)."""
    aid = aid.split(".")[0]
    hits = [f for f in os.listdir(os.path.join(ST, "assets")) if f.split(".")[0] == aid]
    if len(hits) != 1: sys.exit(f"staged asset for {aid}: {hits}")
    return os.path.join(ST, "assets", hits[0])

def fname(aid):
    """Delivered file name: asset id + extension of the ACTUAL format (magic bytes), e.g. JPEG originals -> .jpg."""
    aid = aid.split(".")[0]; b = open(staged(aid), "rb").read(16)
    ext = ("png" if b.startswith(b"\x89PNG") else "jpg" if b.startswith(b"\xff\xd8\xff") else "webp" if b[8:12] == b"WEBP"
           else "gif" if b[:3] == b"GIF" else "svg" if b.lstrip().startswith(b"<") else None)
    if not ext: sys.exit("unknown image format: " + aid)
    return f"{aid}.{ext}"

def tree(dcname):
    if dcname not in _cache: _cache[dcname] = J.load(os.path.join(ST, "dc", dcname + ".tsx"))
    return _cache[dcname]

def find(root, pred):
    return next((n for n in root.walk() if pred(n)), None)

def dcfile(node):
    return node.replace(":", "-").replace(";", "_")

def locate(e):
    """-> (root Node K whose box is the placeholder box, apply_root_styles)"""
    fid, pid = e["figmaNode"], e["placeholderNode"]
    if e["classification"] == "composite" and fid != "1608:7370":          # card: the 'Similar Products - Images' box
        t = tree(dcfile(fid))
        k = find(t, lambda n: n.attrs.get("data-name") == "Similar Products - Images" or n.attrs.get("_component") == "SimilarProductsImages")
        return k, True
    own = "I" * fid.startswith("I") + dcfile(fid.lstrip("I"))
    if fid.startswith("I") and os.path.exists(os.path.join(ST, "dc", own + ".tsx")):   # node-specific verbatim read
        return tree(own).children[0], "(slot fill)" not in pid
    top = fid.lstrip("I").split(";")[0]
    t = tree(dcfile(top))
    k = find(t, lambda n: n.id == fid)
    if k is None and fid.startswith("I"):                                   # component instance rendered from its master
        parent = find(t, lambda n: n.id == fid.rsplit(";", 1)[0])
        k = parent.children[0] if parent is not None else None
    if k is None and top == fid:                                            # dc root rendered from a component (1608:7433…)
        k = t.children[0]
    return k, "(slot fill)" not in pid

def keep(n, assets):
    return any(x.tag == "img" and isinstance(x.attrs.get("src"), tuple) and x.attrs["src"][1].split(".")[0] in assets for x in n.walk())

def scaled(n, inner):
    """Resized component instance: lay the children out at the master size, then scale (Figma scale constraints)."""
    sc = n.attrs.get("_scale")
    if not sc or not inner: return inner
    sx, sy, dw, dh = sc
    return (f'<span class="scr-img__box" style="position:absolute;left:0;top:0;width:{dw:g}px;height:{dh:g}px;'
            f'transform:scale({sx:.6f},{sy:.6f});transform-origin:0 0">{inner}</span>')

def html(n, assets, rel):
    if n.tag == "img":
        aid = n.attrs["src"][1]
        return f'<img class="scr-img__art" src="{rel}{fname(aid)}" alt="" style="{J.tw(n.classes)}">'
    if n.tag != "div": raise ValueError("unexpected tag " + n.tag)
    inner = scaled(n, "".join(html(c, assets, rel) for c in n.children if keep(c, assets)))
    return f'<span class="scr-img__box" style="{J.tw(n.classes)}">{inner}</span>'

def ribbon(assets, rel):
    # Figma (group 1375:31232 design context): box 72.556 x 38.596 centred in the node box, rotate(89.92deg); vector inset wrapper
    t = tree("1375-31233"); w = find(t, lambda n: n.tag == "div" and any(c.startswith("inset-[") for c in n.classes))
    img = w.children[0]
    return ('<span class="scr-img__box" style="position:absolute;left:50%;top:50%;width:72.556px;height:38.596px;transform:translate(-50%,-50%) rotate(89.92deg)">'
            f'<span class="scr-img__box" style="{J.tw(w.classes)}"><img class="scr-img__art" src="{rel}598fb.svg" alt="" style="{J.tw(img.classes)}"></span></span>')

AIR = {  # design context 1608:7168 / 7171 / 7174 (read-only values; no asset): two bars, linear gradient, rotate-180, opacity 15 %
    "I068": (2, [("100%", 3, 3), ("19px", 2, 3)]), "I069": (0.954, [("100%", 1.431, 1.431), ("9.061px", 0.954, 1.431)]),
    "I070": (2, [("100%", 3, 3), ("19px", 2, 3)])}
CSS_ONLY = {"I106": ("bottom-edge", "background:#0b0d0f"),   # Figma var background/inverse (no matching R1 token)
            "I107": ("home-indicator", "background:#fafcff; overflow:clip; border-radius:100px")}   # Figma var background/primary

def air(eid):
    gap, bars = AIR[eid]
    out = []
    for w, h, r in bars:
        row = "display:flex;align-items:center;justify-content:center;position:relative;flex-shrink:0" + (";width:100%" if w == "100%" else "")
        inner = "flex:none;transform:rotate(180deg)" + (";width:100%" if w == "100%" else "")
        bar = (f"position:relative;height:{h:g}px;width:{w};border-radius:{r:g}px 0 0 {r:g}px;"
               "background-image:linear-gradient(to right,#fff 3.448%,#005aaa 82.759%)")
        out.append(f'<span class="scr-img__box" style="{row}"><span class="scr-img__box" style="{inner}"><span class="scr-img__box" style="{bar}"></span></span></span>')
    return f"display:flex;flex-direction:column;gap:{gap:g}px;align-items:flex-start;opacity:0.15", "".join(out)

REFILL = "--refill" in sys.argv   # rebuild placeholders this tool already filled (e.g. after a converter fix)

def unfill(s, pid, extra_style):
    """Return s with the R11 fill of placeholder `pid` removed (inner content, R11 attributes, appended root style)."""
    m = re.search(r'<(span|div)(\b[^>]*data-figma-node="' + re.escape(pid) + r'"[^>]*)>', s)
    if not m or "data-annachy-image" not in m.group(2) and "data-annachy-css" not in m.group(2): return s
    tag, depth, i = m.group(1), 1, m.end()
    for t in re.finditer(r"<(/?)" + tag + r"\b[^>]*>", s[m.end():]):
        depth += -1 if t.group(1) else 1
        if depth == 0: end_inner, end_tag = m.end() + t.start(), m.end() + t.end(); break
    else: sys.exit("unbalanced placeholder " + pid)
    head = re.sub(r' data-(annachy-image|img-layers|img-rights|annachy-css)="[^"]*"', "", m.group(2))
    if extra_style:
        if f"; {extra_style}" in head: head = head.replace(f"; {extra_style}", "", 1)
        elif f' style="{extra_style}"' in head: head = head.replace(f' style="{extra_style}"', "", 1)
        else: sys.exit("cannot remove appended style of " + pid)
    return s[:m.start()] + f"<{tag}{head}></{tag}>" + s[end_tag:]

copied, placed, skipped, problems = [], [], [], []
need = {}
for e in M["elements"]:
    for i in e["images"]:
        if i["assetId"] not in NOT_R11: need[fname(i["assetId"])] = 1
for f in sorted(need):
    src, dst = staged(f), f"{DEST}/{f}"
    if not os.path.exists(src): problems.append("missing staged " + f); continue
    if os.path.exists(dst):
        if sha(dst) != sha(src): sys.exit(f"REFUSING: {dst} exists with different content")
        continue
    if not DRY: os.makedirs(DEST, exist_ok=True); shutil.copyfile(src, dst)
    copied.append(f)

for e in M["elements"]:
    path = e["screenFile"]; s = open(path, encoding="utf-8").read()
    pid = e["placeholderNode"]
    rel = "../assets/images/"
    assets = {i["assetId"] for i in e["images"]} - NOT_R11
    extra_style, attrs = "", ""
    if e["id"] in AIR:
        extra_style, inner = air(e["id"]); attrs = ' data-annachy-css="air-streaks"'
    elif e["id"] in CSS_ONLY:
        name, extra_style = CSS_ONLY[e["id"]]; inner = ""; attrs = f' data-annachy-css="{name}"'
    elif assets == {"598fb"}:
        inner = ribbon(assets, rel)
    else:
        k, root_styles = locate(e)
        if k is None: problems.append(f"{e['id']}: Figma node not found in design context"); continue
        found = {x.attrs["src"][1].split(".")[0] for x in k.walk() if x.tag == "img" and isinstance(x.attrs.get("src"), tuple)}
        if not assets <= found: problems.append(f"{e['id']}: assets {sorted(assets - found)} not under the located node"); continue
        if k.tag == "img": inner = html(k, assets, rel)
        else: inner = scaled(k, "".join(html(c, assets, rel) for c in k.children if keep(c, assets)))
        if root_styles and k.tag == "div":
            extra_style = ";".join(d for d in J.tw(k.classes).split(";") if ROOT_KEEP.match(d))
    if assets:
        files = sorted({fname(i["assetId"]) for i in e["images"] if i["assetId"] in assets})
        layers = len(re.findall(r'<img class="scr-img__art"', inner))
        rc = RIGHTS.get(e["rightsClass"], "source-unknown") if not all(f.endswith(".svg") for f in files) else "design-vector-unverified"
        attrs = f' data-annachy-image="{" ".join(files)}" data-img-layers="{layers}" data-img-rights="{rc}"'
    if REFILL: s = unfill(s, pid, extra_style)
    pat = re.compile(r'<(span|div)(\b[^>]*data-figma-node="' + re.escape(pid) + r'"[^>]*)>(\s*)</\1>')
    m = pat.search(s)
    if m and "data-annachy-" in m.group(2): m = None            # already filled (empty colour fills match the empty pattern)
    if not m:
        if re.search(r'data-figma-node="' + re.escape(pid) + r'"[^>]*data-annachy-(image|css)', s): skipped.append(e["id"]); continue
        problems.append(f"{e['id']}: placeholder not found / not empty"); continue
    head = m.group(2)
    if extra_style:
        if 'style="' in head: head = re.sub(r'style="([^"]*)"', lambda mm: f'style="{mm.group(1).rstrip("; ")}; {extra_style}"', head, count=1)
        else: head += f' style="{extra_style}"'
    new = s[:m.start()] + f"<{m.group(1)}{head}{attrs}>{inner}</{m.group(1)}>" + s[m.end():]
    if not DRY: open(path, "w", encoding="utf-8").write(new)
    placed.append((e["id"], path.split("/")[-1], attrs.strip()[:70]))

print(f"assets copied: {len(copied)} · placeholders filled: {len(placed)} · already filled: {len(skipped)} · problems: {len(problems)}" + (" [DRY RUN]" if DRY else ""))
for p in problems: print("  PROBLEM", p)
if "-v" in sys.argv:
    for p in placed: print("  ", *p)
