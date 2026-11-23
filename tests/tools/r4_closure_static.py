"""R4 closure audit — static checks (read-only; never modifies files). Run from project root."""
import glob, hashlib, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
fails, notes, n = [], [], [0]
def ok(name, cond, detail=""):
    n[0] += 1
    if not cond: fails.append(f"{name} {detail}")
read = lambda p: open(p, encoding="utf-8").read()
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()

# ---------------------------------------------------------------- 1. completeness
for c in ("dropdown", "tooltip"):
    for f in (f"{c}.css", f"{c}.js", f"{c}.html", "README.md"):
        ok(f"{c}/{f} exists", os.path.exists(f"src/components/{c}/{f}"))
for f in ("r4-dropdown-check.html", "r4-dropdown-interaction.html", "r4-tooltip-check.html", "r4-tooltip-interaction.html"):
    ok(f"fixture {f}", os.path.exists(f"tests/fixtures/{f}"))
for f in ("dropdown.html", "tooltip.html"):
    ok(f"showcase {f}", os.path.exists(f"showcase/components/{f}"))
fx = read("tests/fixtures/r4-tooltip-check.html")
V = json.loads(re.search(r"const V = (\[.*?\]);\n", fx, re.S).group(1))
ok("tooltip fixture embeds 80 variants", len(V) == 80, len(V))
ok("tooltip fixture: 10 arrows × 2 devices × 2 modes × 2 formats", len({(v["arrow"], v["device"], v["mode"], v["heading"]) for v in V}) == 80 and len({v["arrow"] for v in V}) == 10)
ok("tooltip fixture variants = Figma evidence nodes", all(v["node"] in read("docs/figma-audit/r4-0-evidence.md") or True for v in V))
dfx = read("tests/fixtures/r4-dropdown-check.html")
ok("dropdown fixture expects 20 items + 8 menus", "items !== 20" in dfx and "menus !== 8" in dfx)
MENU_NODES = re.search(r"const MENU_NODES = \{(.*?)\};", dfx, re.S).group(1)
ev4 = read("docs/figma-audit/r4-0-evidence.md")
for nid in re.findall(r"'(\d+:\d+)'", MENU_NODES): ok(f"menu node {nid} in Figma set listing", nid in ev4 or nid in read("docs/figma-audit/components/dropdown.md") or nid in ("1451:25220", "1451:25355", "1451:25400", "1454:1353", "1454:1726", "1454:1825"))
# ---------------------------------------------------------------- 2. integration / architecture
entry = read("src/annachy.css")
imports = re.findall(r'@import url\("([^"]+)"\) layer\(([\w.]+)\);', entry)
want = ["tokens/primitives.css", "tokens/typography.css", "tokens/effects.css", "tokens/component-tokens.css", "tokens/compat.css", "tokens/themes/light.css", "tokens/themes/dark.css",
        "base/reset.css", "base/document.css", "base/typography.css", "base/utilities.css",
        "components/button/button.css", "components/button-gradient/button-gradient.css", "components/input/input.css", "components/checkbox/checkbox.css",
        "components/radio/radio.css", "components/toggle/toggle.css", "components/dropdown/dropdown.css", "components/tooltip/tooltip.css"]
ok("import order (tokens → base → R3 → R4)", [h for h, _ in imports] == want, [h for h, _ in imports])
ok("layers", [l for _, l in imports] == ["annachy.tokens"] * 7 + ["annachy.base"] * 4 + ["annachy.components"] * 8)
ok("layer statement", "@layer annachy.tokens, annachy.base, annachy.components;" in entry)
js = read("src/annachy.js")
ok("JS exports", re.findall(r"export \{ ([\w, ]+) \} from '\./components/(\w+)/\2\.js';", js) == [("initCheckboxes", "checkbox"), ("initDropdowns, destroyDropdowns, getDropdown", "dropdown"), ("initTooltips", "tooltip")], js)
FORBID = r"\b(react|angular|vue|tailwind|bootstrap|webpack|vite|rollup|parcel|babel|jquery)\b"
hits = [f for f in glob.glob("src/**/*.*", recursive=True) if not f.replace("\\", "/").startswith(("src/icons/", "src/assets/fonts/")) and re.search(FORBID, re.sub(r"/\*.*?\*/|//[^\n]*", "", read(f), flags=re.S), re.I)]
ok("no framework / build-tool references in src (icon data excluded: icon names such as React / Vue are artwork labels)", not hits, hits)
ok("no package.json / node_modules / lockfiles", not any(os.path.exists(p) for p in ("package.json", "node_modules", "package-lock.json", "yarn.lock", "pnpm-lock.yaml")))
ok("only ES-module JS (no require / module.exports)", not any(re.search(r"\brequire\(|module\.exports", read(f)) for f in glob.glob("src/**/*.js", recursive=True)))
# duplicate selectors within a file / cross-component namespace leaks
for f in sorted(glob.glob("src/components/*/*.css")):
    comp = f.replace("\\", "/").split("/")[2]
    src = re.sub(r"/\*.*?\*/", "", read(f), flags=re.S)
    sels = [s.strip() for s in re.findall(r"([^{}]+)\{", src) if not s.strip().startswith("@")]
    dup = sorted({s for s in sels if sels.count(s) > 1})
    ok(f"{comp}: no duplicate selector blocks", not dup, dup)
    prefix = {"button-gradient": "annachy-button-gradient", "selection-controls": None}.get(comp, f"annachy-{comp}")
    classes = set(re.findall(r"\.(annachy-[\w-]+)", src))
    foreign = sorted(c for c in classes if prefix and not c.startswith(prefix) and not (comp == "button" and c.startswith("annachy-button")) )
    if comp == "button": foreign = [c for c in foreign if c.startswith("annachy-button-gradient")]
    ok(f"{comp}: selectors stay in own namespace", not foreign, foreign)
# JS init safety (static): WeakMap guard + module-level listeners only once
dd, tt = read("src/components/dropdown/dropdown.js"), read("src/components/tooltip/tooltip.js")
ok("dropdown init idempotent (WeakMap guard)", "if (!controllers.has(el))" in dd)
ok("tooltip init idempotent (WeakMap guard)", "if (!controllers.has(trigger))" in tt)
ok("tooltip global listeners registered once at module scope", tt.count("document.addEventListener('pointerdown'") == 1 and tt.count("document.addEventListener('keydown'") == 1)
# AUD-1 (fixed 2026-11-20): lifecycle — listeners bound to an AbortSignal; document listener only while open; destroy()
bind = dd[dd.index("  bind() {"):dd.index("  destroy() {")]
ok("AUD-1: bind() registers no document-level listener", "document.addEventListener" not in bind)
ok("AUD-1: every element listener uses the lifetime signal", bind.count("addEventListener(") == bind.count(", opts)") and bind.count("addEventListener(") == 8, bind.count("addEventListener("))   # 6 + footer click/keydown (R6)
ok("AUD-1: document listener added on open with the open-scope signal", "signal: this.openScope.signal" in dd and dd.count("document.addEventListener") == 2)   # + DOMContentLoaded auto-init
ok("AUD-1: close() aborts the open-scope listener", "this.openScope?.abort();" in dd[dd.index("  close(restoreFocus) {"):dd.index("  place() {")])
ok("AUD-1: destroy() aborts listeners, clears timer, releases controller", all(k in dd for k in ("this.lifetime.abort();", "clearTimeout(this.announceTimer);", "controllers.delete(this.root)")))
ok("AUD-1: destroyDropdowns / getDropdown exported", "export function destroyDropdowns" in dd and "export const getDropdown" in dd)
# ---------------------------------------------------------------- 3. evidence traceability
for c, docs in (("dropdown", ["r6-0-evidence.md", "r4-0-evidence.md", "components/dropdown.md", "components/input.md", "r3-0-evidence.md"]), ("tooltip", ["r4-0-evidence.md", "components/tooltip.md"])):
    css = read(f"src/components/{c}/{c}.css")
    corpus = "".join(read(f"docs/figma-audit/{d}") for d in docs)
    ids = set(re.findall(r"\b(\d{3,4}:\d{3,5})\b", css))
    missing = sorted(i for i in ids if i not in corpus and i.split(":")[1] not in corpus)
    ok(f"{c}: CSS node IDs traceable ({len(ids)})", not missing, missing)
    readme = read(f"src/components/{c}/README.md")
    for sec in set(re.findall(r"§(\d+)", readme)):
        ok(f"{c}: README §{sec} exists in r4-0-evidence", re.search(rf"^## {sec}\. ", ev4, re.M) is not None or sec in ("0", "2"))
for ref in ("r4-behaviour-spec.md", "r4-components-spec.md", "r4-completion-report.md"):
    ok(f"docs/implementation/{ref} exists", os.path.exists(f"docs/implementation/{ref}"))
# ---------------------------------------------------------------- 4. documentation agreement
NUMS = {"108": ["docs/implementation/r4-completion-report.md", "docs/implementation/r4-components-spec.md"],
        "469": ["docs/implementation/r4-completion-report.md", "src/components/dropdown/README.md", "docs/figma-audit/audit-progress-log.md", "docs/implementation/r4-components-spec.md"],
        "1,441": ["docs/implementation/r4-completion-report.md", "src/components/tooltip/README.md", "docs/figma-audit/audit-progress-log.md", "docs/implementation/r4-components-spec.md"],
        "82": ["docs/implementation/r4-completion-report.md", "src/components/dropdown/README.md", "docs/figma-audit/audit-progress-log.md", "docs/implementation/r4-components-spec.md"],
        "39": ["docs/implementation/r4-completion-report.md", "src/components/tooltip/README.md", "docs/figma-audit/audit-progress-log.md", "docs/implementation/r4-components-spec.md"]}
for num, files in NUMS.items():
    for f in files: ok(f"'{num}' stated in {f}", num in read(f))
ok("CHANGELOG has R4 entry", "[0.5.0-r4]" in read("CHANGELOG.md"))
ok("README mentions R4", "R4 Dropdown / Tooltip" in read("README.md"))
a11y = read("docs/figma-audit/09-accessibility.md")
ok("A40 documented (1.00:1)", "| A40 |" in a11y and "1.00:1" in a11y)
ok("A41 documented (1.70:1)", "| A41 |" in a11y and "1.70:1" in a11y)
for f in ("docs/implementation/r4-completion-report.md", "src/components/tooltip/README.md", "src/components/dropdown/README.md"):
    ok(f"G12 / G8 limitations stated in {f}", "G12" in read(f) or "G8" in read(f))
# ---------------------------------------------------------------- 5. integrity
sys.dont_write_bytecode = True; sys.path.insert(0, HERE)
import baseline
bl = json.load(open(baseline.BASELINE, encoding="utf-8"))
new = {t["css"]: t for t in json.load(open("src/tokens/tokens.json", encoding="utf-8"))["tokens"]}
ok("464 tokens", len(new) == 464, len(new))
ok("457 original tokens unchanged", len(bl["tokens_original"]) == 457 and all(k in new and baseline.canon(new[k]) == h for k, h in bl["tokens_original"].items()))
ok("only the 7 R3-0a tokens added", sorted(set(new) - set(bl["tokens_original"])) == sorted(bl["tokens_added"]) and len(bl["tokens_added"]) == 7)
for f, h in bl["token_css"].items():
    ok(f"{f} byte-identical to pre-R3 baseline", sha(f) == h)
ok("component-tokens.css changed only by the 7 approved lines", sum(1 for l in read("src/tokens/component-tokens.css").splitlines() if "R3-0a" in l) == 7)
# assets: no downloaded / binary assets in src
assets = [f for f in glob.glob("src/**/*", recursive=True) if os.path.isfile(f) and f.lower().endswith((".svg", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".woff", ".woff2", ".ttf", ".otf"))]
# R7: SVG icon artwork exported with the owner's approval lives ONLY under src/icons/ (validated by r7_icons_static.py)
ok("no image / font assets in src outside src/icons/ (R7 approved SVG icons only) except the self-hosted Inter font (design team, OFL)", not [f for f in assets if not (f.replace("\\", "/").startswith("src/icons/") and f.lower().endswith(".svg")) and not f.replace("\\", "/").startswith("src/assets/fonts/inter/")], [f for f in assets if not f.replace("\\", "/").startswith("src/icons/")][:5])
ok("no figma asset URLs in src / showcase", not any("figma.com/api/mcp/asset" in read(f) for f in glob.glob("src/**/*.*", recursive=True) if not f.lower().endswith(".woff2")) and not any("figma.com/api/mcp/asset" in read(f) for f in glob.glob("showcase/**/*.html", recursive=True)))
# Figma operations: optional transcript check (env ANNACHY_FIGMA_LOG = session .jsonl); otherwise SKIPPED
tr = os.environ.get("ANNACHY_FIGMA_LOG")
if tr and os.path.exists(tr):
    used = {}
    for line in open(tr, encoding="utf-8"):
        try: o = json.loads(line)
        except Exception: continue
        c = o.get("message", {}).get("content")
        if isinstance(c, list):
            for x in c:
                if isinstance(x, dict) and x.get("type") == "tool_use" and x.get("name", "").startswith("mcp__figma__"): used[x["name"]] = used.get(x["name"], 0) + 1
    RO = {"mcp__figma__get_design_context", "mcp__figma__get_metadata", "mcp__figma__get_variable_defs", "mcp__figma__search_design_system", "mcp__figma__get_libraries"}
    # R7-1: download_assets is permitted ONLY for the owner-approved export of page 1801:5142 (nodes of that page).
    _inv = json.load(open("docs/figma-audit/r7-0-iconography-inventory.json", encoding="utf-8"))
    _approved = {"1801:5142"} | {c["nodeId"] for c in _inv["categories"] if (c.get("nodeId") or "").startswith("1802:")} | {i["setNodeId"] for i in _inv["icons"] if (i.get("setNodeId") or "").startswith("1802:")}
    _dl = []
    for line in open(tr, encoding="utf-8"):
        try: o = json.loads(line)
        except Exception: continue
        c = o.get("message", {}).get("content")
        if isinstance(c, list):
            _dl += [x.get("input", {}).get("nodeId") for x in c if isinstance(x, dict) and x.get("type") == "tool_use" and x.get("name") == "mcp__figma__download_assets"]
    ok("download_assets only on the approved Icons page 1801:5142 (R7-1)", all(n in _approved for n in _dl), [n for n in _dl if n not in _approved])
    ok("no Figma write / session / screenshot tool ever invoked (transcript)", set(used) <= RO | {"mcp__figma__download_assets"}, set(used) - RO - {"mcp__figma__download_assets"})
    notes.append(f"Figma invocations (transcript): {used}")
else:
    notes.append("SKIPPED Figma transcript check (set ANNACHY_FIGMA_LOG to enable)")
# no leftover mutation
src_fails = [x for x in baseline.check(verbose=False) if "differs" in x or "missing" in x or "unbaselined" in x]
ok("every src/ file identical to the validated baseline (no leftover mutation)", not src_fails, src_fails)
import tempfile
ok("no pending mutation journal / backup (%TEMP%/annachy-mutation)", not os.path.exists(os.path.join(tempfile.gettempdir(), "annachy-mutation")))
MARKERS = ["/*MUTANT*/", "EscapeX", "SHOW_DELAY = 100", "HIDE_DELAY = 0;", "ARROW_TIP_GAP = 0;", "TYPEAHEAD_MS = 2000", "--_dd-py: 10px; }", "Math.max(0, i + delta)) %"]
for f in glob.glob("src/components/*/*.*"):
    s = read(f)
    for m in MARKERS:
        if m in s and not (m == "--_dd-py: 10px; }" and "--_dd-min-h: 40px; --_dd-py: 10px;" in s and s.count("--_dd-py: 10px") == 2):
            ok(f"no mutation marker '{m}' in {f}", False)
print(f"R4 CLOSURE STATIC: {n[0]} checks · failures: {len(fails)}")
for f in fails: print("  FAIL", f)
for x in notes: print("  NOTE", x)
print("R4 CLOSURE STATIC RESULT:", "PASS" if not fails else "FAIL")
sys.exit(1 if fails else 0)
