"""R10-0: integrate the 28 approved structural-vector artworks into their 50 screen placeholders.

Reads docs/figma-audit/r10-0-structural-vector-manifest.json + the staging export report, copies each ORIGINAL artwork
file byte-for-byte to showcase/screens/assets/vectors/ (refuses to overwrite), and fills each placeholder with Figma's own
placement (inset wrapper / rotation taken from the node's design context). Idempotent: a placeholder that already carries
data-annachy-vector is left untouched. Run from the project root:
    python -I tests/tools/r10_integrate_vectors.py [--dry-run]
"""
import hashlib, json, os, re, shutil, sys
sys.stdout.reconfigure(encoding="utf-8")
STAGING = os.path.join(os.environ["TEMP"], "annachy-vector-staging")
DRY = "--dry-run" in sys.argv
M = json.load(open("docs/figma-audit/r10-0-structural-vector-manifest.json", encoding="utf-8"))
R = {a["artworkId"]: a for a in json.load(open(os.path.join(STAGING, "export-report.json"), encoding="utf-8"))["artworks"]}
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()

def inset_of(wrapper):
    m = re.search(r"inset-\[([^\]]+)\]", wrapper)
    return m.group(1).replace("_", " ") if m else "0"

VERTICAL = {"R02", "R03", "R17"}
copied, placed, skipped = [], [], []
art = {a["artworkId"]: a for a in M["artworks"]}
for aid, a in art.items():
    src = os.path.join(STAGING, f"{aid}-asset-1.svg")
    assert os.path.exists(src), src
    dst = a["destination"]
    if os.path.exists(dst):
        if sha(dst) != sha(src): sys.exit(f"REFUSING: {dst} exists with different content")
        continue
    if not DRY:
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(src, dst)
    copied.append((aid, dst, sha(src)))

for e in M["elements"]:
    a = art[e["artworkId"]]; rep = R[e["artworkId"]]
    svg_w, svg_h = float(rep["svg"]["width"]), float(rep["svg"]["height"])
    rel = "../assets/vectors/" + os.path.basename(a["destination"])
    path = e["screenFile"]; html = open(path, encoding="utf-8").read()
    pat = re.compile(r'(<span\b[^>]*data-figma-node="' + re.escape(e["placeholderNode"]) + r'"[^>]*)>(\s*)</span>')
    if not pat.search(html):
        if re.search(r'data-figma-node="' + re.escape(e["placeholderNode"]) + r'"[^>]*data-annachy-vector', html): skipped.append(e["id"]); continue
        sys.exit(f"placeholder not found or not empty: {e['id']} {e['placeholderNode']} in {path}")
    img = f'<img class="scr-vec__art" src="{rel}" alt="" width="{svg_w:g}" height="{svg_h:g}">'
    wrapper = rep["wrapperClasses"]["wrapper"]
    if e["artworkId"] in VERTICAL:
        L = float(e["h"])   # node box is ~0 × L; Figma draws an L × 0 line rotated by an ancestor (direction not observable)
        inner = (f'<span class="scr-vec scr-vec--rotated" style="width:{L:g}px;height:0;transform:translate(-50%,-50%) rotate(90deg)">'
                 f'<span class="scr-vec__inset" style="inset:{inset_of(wrapper)}">{img}</span></span>')
        kind = "vertical"
    elif e["artworkId"] == "R12" and "rotate(" not in pat.search(html).group(1):
        # placeholder is the 57 × 54 node box (V36): Figma = centred 78.518 × 0 line box, rotate(43.45deg), inset -1.5px top;
        # a placeholder that is already the rotated line box (V23) only needs the inset (falls through to 'inset')
        inner = (f'<span class="scr-vec scr-vec--rotated" style="width:78.518px;height:0;transform:translate(-50%,-50%) rotate(43.45deg)">'
                 f'<span class="scr-vec__inset" style="inset:{inset_of(wrapper)}">{img}</span></span>')
        kind = "diagonal-in-box"
    else:
        inner = f'<span class="scr-vec__inset" style="inset:{inset_of(wrapper)}">{img}</span>'
        kind = "inset"
    lw, lh = svg_w, svg_h
    if wrapper.startswith("(no wrapper"):   # Figma draws the img at the node box (absolute inset-0 size-full)
        lw, lh = float(e["w"]), float(e["h"])
    attrs = f' data-annachy-vector="{os.path.basename(a["destination"])}" data-vec-artwork="{e["artworkId"]}" data-vec-w="{lw:g}" data-vec-h="{lh:g}"'
    new, n = pat.subn(lambda m_: m_.group(1) + attrs + ">" + inner + "</span>", html)
    if not DRY: open(path, "w", encoding="utf-8").write(new)
    placed.append((e["id"], e["artworkId"], kind, path.split("/")[-1], n))

print(f"artworks copied: {len(copied)} · placeholders filled: {len(placed)} (elements; occurrences {sum(p[4] for p in placed)}) · already filled: {len(skipped)}" + (" [DRY RUN]" if DRY else ""))
for p in placed: print("  ", *p)
