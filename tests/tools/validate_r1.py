"""Independent static validation of R1: mapping (expected) vs CSS declarations (actual) vs tokens.json.
Run from project root. Exit code 1 on any failure."""
import json, re, sys, glob
sys.stdout.reconfigure(encoding="utf-8")
md = open("docs/implementation/r1-token-mapping.md", encoding="utf-8").read()
fail = []

# ---------- expected from mapping ----------
exp = {}
def cells(line): return [c.strip() for c in line.strip().strip("|").split(" | ")]
def bt(s): return s.strip().strip("`")
current = None
WEIGHT = {"Regular": "400", "Medium": "500", "Semibold": "600", "Bold": "700"}
for line in md.splitlines():
    if line.startswith("#"):
        current = line
        continue
    if not line.startswith("| ") or line.startswith("|---"):
        continue
    c = cells(line)
    if "6.2" in current and c[1].startswith("`") and not c[0].startswith("Style"):
        k = bt(c[1]); ms, ml = [x.strip() for x in c[3].split("/")]; ds, dl = [x.strip() for x in c[4].split("/")]
        b = f"--annachy-type-{k}"
        exp.update({f"{b}-font-size": ms+"px", f"{b}-line-height": ml+"px", f"{b}-font-weight": WEIGHT[c[2]],
                    f"{b}-font-size-mobile": ms+"px", f"{b}-line-height-mobile": ml+"px",
                    f"{b}-font-size-desktop": ds+"px", f"{b}-line-height-desktop": dl+"px"})
        continue
    if "7.4" in current and c[0].startswith("`grid/"):
        prop = {"`grid/width` · frame width": "frame-width", "`grid/columns`": "columns", "`grid/margin`": "margin",
                "`grid/gutter`": "gutter", "`grid/height`": "frame-height"}[c[0]]
        for cls, v in zip(("mobile", "desktop", "large"), c[1:4]):
            if v != "—": exp[f"--annachy-grid-{cls}-{prop}"] = v
        continue
    idx = [i for i, x in enumerate(c) if x.startswith("`--annachy-")]
    if not idx: continue
    i = idx[0]; name = bt(c[i])
    if name == "--annachy-": continue  # header row "Prefix", not a token
    if "8.1" in current or "8.2" in current or "8.4" in current: val = c[i+1]
    elif "8.3" in current: val = c[i+1]
    else: val = c[1]
    val = bt(val)
    if name == "--annachy-font-family-sans": val = '"Proxima Nova"'
    if name == "--annachy-compat-shadow-sm": val = "0px 1px 3px 0px #1a1a1a14, 0px 0.5px 0px 0px #1a1a1a14"
    if name in exp: fail.append(f"duplicate in mapping: {name}")
    exp[name] = val

# ---------- actual from CSS ----------
act, where = {}, {}
for f in glob.glob("src/tokens/*.css") + [x for x in glob.glob("src/tokens/themes/*.css") if not x.replace("\\", "/").endswith("dark.css")]:   # dark.css re-maps (checked below)
    src = re.sub(r"/\*.*?\*/", "", open(f, encoding="utf-8").read(), flags=re.S)
    for m in re.finditer(r"(--annachy-[\w-]+)\s*:\s*([^;]+);", src):
        n, v = m.group(1), " ".join(m.group(2).split())
        if n in act: fail.append(f"declared twice: {n} ({where[n]}, {f})")
        act[n], where[n] = v, f.replace("\\", "/")

# ---------- tokens.json ----------
J = json.load(open("src/tokens/tokens.json", encoding="utf-8"))
jt = {t["css"]: " ".join(t["value"].split()) for t in J["tokens"]}
if J["count"] != len(J["tokens"]): fail.append("tokens.json count field mismatch")

# ---------- compare ----------
missing = sorted(set(exp) - set(act)); extra = sorted(set(act) - set(exp))
mism = [(n, exp[n], act[n]) for n in sorted(set(exp) & set(act)) if " ".join(exp[n].split()) != act[n]]
jmism = [n for n in act if jt.get(n) != act[n]] + [n for n in jt if n not in act]
fail += [f"missing in CSS: {n}" for n in missing] + [f"not in mapping: {n}" for n in extra]
fail += [f"value mismatch {n}: mapping '{e}' vs css '{a}'" for n, e, a in mism]
fail += [f"tokens.json vs css: {n}" for n in jmism]

# ---------- group counts vs mapping §9 ----------
s9 = md.split("## 9. Token counts")[1]
declared = {cells(l)[0]: int(cells(l)[1]) for l in s9.splitlines() if l.startswith("| ") and not l.startswith("| Group") and not l.startswith("|---")}
def cnt(p): return sum(1 for n in act if p(n))
groups = {
 "Colour primitives": (lambda n: where[n].endswith("primitives.css") and n.startswith("--annachy-color-")),
 "Semantic colours (light)": (lambda n: where[n].endswith("themes/light.css")),
 "Button component colours": (lambda n: n.startswith("--annachy-color-button-")),
 "Icon-state colours": (lambda n: n.startswith("--annachy-color-icon-state-")),
 "Compat (foreign) values": (lambda n: n.startswith("--annachy-compat-") and n != "--annachy-compat-shadow-sm"),
 "Typography primitives": (lambda n: n.startswith("--annachy-font-")),
 "Type styles (× 7 properties each)": (lambda n: n.startswith("--annachy-type-") and n.endswith("-font-weight")),
 "Heights": (lambda n: n.startswith("--annachy-size-height-")),
 "Radius": (lambda n: n.startswith("--annachy-radius-")),
 "Border widths": (lambda n: n.startswith("--annachy-border-width-")),
 "Grid reference values": (lambda n: n.startswith("--annachy-grid-")),
 "Documented shadows (incl. swatch)": (lambda n: n.startswith(("--annachy-shadow-scale-", "--annachy-shadow-effects-")) or n == "--annachy-shadow-swatch"),
 "Component effect styles (incl. compat)": (lambda n: n.startswith("--annachy-effect-") or n == "--annachy-compat-shadow-sm"),
 "Blur / Glass / glass fills": (lambda n: n.startswith(("--annachy-blur-", "--annachy-glass-", "--annachy-color-glass-"))),
 "Gradients": (lambda n: n.startswith("--annachy-gradient-")),
}
print(f"{'Group':42} {'expected':>8} {'actual':>7}")
total_exp = 0
for g, p in groups.items():
    e, a = declared[g], cnt(p); total_exp += e * (7 if g.startswith("Type styles") else 1)
    print(f"{g:42} {e:>8} {a:>7} {'OK' if e == a else 'FAIL'}")
    if e != a: fail.append(f"count {g}: expected {e}, actual {a}")
typestyle_props = cnt(lambda n: n.startswith("--annachy-type-"))
print(f"{'Type style properties (28 × 7)':42} {28*7:>8} {typestyle_props:>7} {'OK' if typestyle_props == 196 else 'FAIL'}")
print(f"{'TOTAL tokens':42} {total_exp:>8} {len(act):>7} {'OK' if total_exp == len(act) else 'FAIL'}")
print(f"mapping rows parsed: {len(exp)} | css declarations: {len(act)} | tokens.json: {len(jt)}")
print(f"missing: {len(missing)} | extra: {len(extra)} | value mismatches: {len(mism)} | tokens.json mismatches: {len(jmism)}")
if total_exp != len(act): fail.append("total count mismatch")

# ---------- rule checks ----------
desk_active = [n for n in act if n.startswith("--annachy-type-") and re.search(r"-(font-size|line-height)$", n)
               and act[n] != act[n + "-mobile"]]
print("active typography != mobile:", len(desk_active))
if desk_active: fail.append(f"active typography not Mobile: {desk_active}")
entry = open("src/annachy.css", encoding="utf-8").read()
imports = re.findall(r'@import url\("([^"]+)"\) layer\(([\w.]+)\);', entry)
want = ["tokens/primitives.css", "tokens/typography.css", "tokens/effects.css", "tokens/component-tokens.css", "tokens/compat.css", "tokens/themes/light.css"]
print("imports:", [i for i, _ in imports])
if [i for i, _ in imports][:6] != want or any(l != "annachy.tokens" for _, l in imports[:6]): fail.append("token import order/layers wrong")  # R2+ may append base/component imports after the 6 token imports
if "@layer annachy.tokens, annachy.base, annachy.components;" not in entry: fail.append("layer statement missing")
light = open("src/tokens/themes/light.css", encoding="utf-8").read()
if ':root,\n[data-annachy-theme="light"] {' not in light: fail.append("light theme selector missing")
# R6 (supersedes the V1 Light-only rule, D-03): dark.css may only RE-MAP existing light-theme names to hex values,
# inside a single [data-annachy-theme="dark"] block. It never adds token names.
if glob.glob("src/tokens/themes/dark.css"):
    dk = re.sub(r"/\*.*?\*/", "", open("src/tokens/themes/dark.css", encoding="utf-8").read(), flags=re.S)
    blocks = re.findall(r"([^{}]+)\{([^{}]*)\}", dk)
    if [b[0].strip() for b in blocks] != ['[data-annachy-theme="dark"]']: fail.append("dark.css must contain exactly one [data-annachy-theme=\"dark\"] block")
    light_names = set(re.findall(r"(--annachy-[\w-]+)\s*:", re.sub(r"/\*.*?\*/", "", light, flags=re.S)))
    for n, v in re.findall(r"(--annachy-[\w-]+)\s*:\s*([^;]+);", "".join(b[1] for b in blocks)):
        if n not in light_names: fail.append(f"dark.css re-maps a name not in light.css: {n}")
        if not re.fullmatch(r"#[0-9a-f]{6}", v.strip()): fail.append(f"dark.css value not a lower-case hex: {n} {v}")
if any(n.startswith(("--annachy-space", "--annachy-spacing")) for n in act): fail.append("spacing token found")
if re.search(r"@media", "".join(open(f, encoding="utf-8").read() for f in glob.glob("src/tokens/**/*.css", recursive=True))): fail.append("media query found in tokens")

print("\nRESULT:", "PASS" if not fail else "FAIL")
for f in fail[:50]: print(" -", f)
sys.exit(1 if fail else 0)
