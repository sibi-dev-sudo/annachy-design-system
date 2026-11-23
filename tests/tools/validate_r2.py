"""Static validation for R2 base styles. Run from project root. Exit 1 on failure."""
import json, re, glob, sys
sys.stdout.reconfigure(encoding="utf-8")
fail = []
tokens = {t["css"] for t in json.load(open("src/tokens/tokens.json", encoding="utf-8"))["tokens"]}
RENDER = "--annachy-base-font-family-render"
files = sorted(glob.glob("src/base/*.css"))
print("base files:", [f.replace("\\", "/") for f in files])
if [f.replace("\\", "/").split("/")[-1] for f in files] != ["document.css", "reset.css", "typography.css", "utilities.css"]:
    fail.append("unexpected base file set")
defined, refs, text_classes, util_classes = [], set(), set(), set()
for f in files:
    raw = open(f, encoding="utf-8").read()
    src = re.sub(r"/\*.*?\*/", "", raw, flags=re.S)
    defined += re.findall(r"(--annachy-[\w-]+)\s*:", src)
    refs |= set(re.findall(r"var\((--annachy-[\w-]+)\)", src))
    for bad, pat in [("@media", r"@media"), ("@font-face", r"@font-face"), (":focus", r":focus"), ("outline", r"\boutline\s*:"),
                     ("url(", r"url\("), ("@import", r"@import")]:
        if bad in ("@font-face", "url(") and f.replace("\\", "/").endswith("base/document.css"): continue  # self-hosted Inter (design team)
        if re.search(pat, src): fail.append(f"{bad} found in {f}")
    for m in re.finditer(r"\b(margin|padding)(?:-[a-z]+)?\s*:\s*([^;]+);", src):
        if not re.fullmatch(r"0(\s*!important)?", m.group(2).strip()):
            fail.append(f"non-zero {m.group(1)} in {f}: {m.group(2)}")
    for m in re.finditer(r"#[0-9a-fA-F]{3,8}\b|\b\d+(?:\.\d+)?px\b", src):
        # only the technical visually-hidden 1px is allowed
        if not (f.endswith("utilities.css") and m.group(0) == "1px"):
            fail.append(f"literal design value {m.group(0)} in {f}")
    text_classes |= set(re.findall(r"\.(annachy-text-[\w-]+)\s*\{", src))
    util_classes |= set(re.findall(r"\.(annachy-(?:color-text|bg|radius|shadow|effect|visually)[\w-]*)\s*\{", src))
new_props = sorted(set(defined))
print("custom properties defined in base:", new_props)
if new_props != [RENDER]: fail.append(f"unexpected custom properties: {new_props}")
unknown = sorted(r for r in refs if r not in tokens and r != RENDER)
print("var() references:", len(refs), "| unknown:", unknown)
if unknown: fail.append(f"unknown token refs: {unknown}")
print("text classes:", len(text_classes), "| utility classes:", len(util_classes))
if len(text_classes) != 28: fail.append("text class count != 28")
if len(util_classes) != 62: fail.append("utility class count != 62")
doc = open("src/base/document.css", encoding="utf-8").read()
if f'{RENDER}: "Inter", system-ui, sans-serif;' not in doc: fail.append("render stack differs from spec (Inter confirmed by design team)")
if "InterVariable.woff2" not in doc: fail.append("Inter @font-face missing")
if '--annachy-font-family-sans' in doc.split(":root {")[-1].split("}")[0]: fail.append("render stack must not reference the Proxima token")
typo = open("src/base/typography.css", encoding="utf-8").read()
if "-desktop)" in typo: fail.append("desktop typography activated")
entry = open("src/annachy.css", encoding="utf-8").read()
imports = [i for i in re.findall(r'@import url\("([^"]+)"\) layer\(([\w.]+)\);', entry) if i != ("tokens/themes/dark.css", "annachy.tokens")]   # R6 optional Dark mode
exp = [("tokens/primitives.css", "annachy.tokens"), ("tokens/typography.css", "annachy.tokens"), ("tokens/effects.css", "annachy.tokens"),
       ("tokens/component-tokens.css", "annachy.tokens"), ("tokens/compat.css", "annachy.tokens"), ("tokens/themes/light.css", "annachy.tokens"),
       ("base/reset.css", "annachy.base"), ("base/document.css", "annachy.base"), ("base/typography.css", "annachy.base"), ("base/utilities.css", "annachy.base")]
extra_ok = all(h.startswith("components/") and l == "annachy.components" for h, l in imports[10:])  # R3+ component imports
print("imports:", len(imports), "first 10 in expected order/layers:", imports[:10] == exp, "| later imports are components:", extra_ok)
if imports[:10] != exp or not extra_ok: fail.append("import order/layers")
print("\nR2 STATIC RESULT:", "PASS" if not fail else "FAIL")
for f in fail: print(" -", f)
sys.exit(1 if fail else 0)
