"""R3 closure audit — static checks. Run from project root."""
import glob, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
fails, n = [], [0]
def ok(name, cond, detail=""):
    n[0] += 1
    if not cond: fails.append(f"{name} {detail}")
    return cond
COMPONENTS = {  # dir, Figma set, variants, fixture, showcase, evidence sections, component spec
 "button": ("887:2492", 432, "r3-button-check.html", "button.html", ["§1", "§2", "§3", "§4", "§21"], "button.md"),
 "button-gradient": ("1153:3370", 55, "r3-button-gradient-check.html", "button-gradient.html", ["§5", "§6", "§17", "§18", "§22"], "button.md"),
 "input": ("1066:37962", 325, "r3-input-check.html", "input.html", ["§7", "§8", "§9", "§23"], "input.md"),
 "checkbox": ("1504:53300", 126, "r3-checkbox-check.html", "checkbox.html", ["§10", "§11", "§19", "§24"], "checkbox.md"),
 "radio": ("1504:52363", 108, "r3-radio-check.html", "radio.html", ["§11", "§12", "§19", "§25"], "radio.md"),
 "toggle": ("1504:54471", 180, "r3-toggle-check.html", "toggle.html", ["§11", "§13", "§19", "§26"], "toggle.md"),
}
evidence = open("docs/figma-audit/r3-0-evidence.md", encoding="utf-8").read()
entry = open("src/annachy.css", encoding="utf-8").read()
imports = re.findall(r'@import url\("([^"]+)"\) layer\(([\w.]+)\);', entry)
# 1. integration
comp_imports = [(h, l) for h, l in imports if h.startswith("components/")]
ok("R3 component import order (R4+ may follow)", [h for h, _ in comp_imports][:6] == [f"components/{c}/{c}.css" for c in COMPONENTS], comp_imports)
ok("component layer", all(l == "annachy.components" for _, l in comp_imports))
ok("layer statement", "@layer annachy.tokens, annachy.base, annachy.components;" in entry)
ok("tokens + base imports first", [h for h, _ in imports if h != "tokens/themes/dark.css"][:10] == ["tokens/primitives.css", "tokens/typography.css", "tokens/effects.css", "tokens/component-tokens.css", "tokens/compat.css", "tokens/themes/light.css", "base/reset.css", "base/document.css", "base/typography.css", "base/utilities.css"])
js = open("src/annachy.js", encoding="utf-8").read()
ok("annachy.js exports initCheckboxes first (R4 exports follow)", re.findall(r"export\s*\{([^}]*)\}", js)[:1] == [" initCheckboxes "], js)
ok("R3 has one script (checkbox.js); R4 adds dropdown.js", sorted(p.replace("\\", "/") for p in glob.glob("src/components/*/*.js"))[:1] == ["src/components/checkbox/checkbox.js"])
ok("no framework / build deps", not glob.glob("package.json") and not glob.glob("node_modules"))
total = 0
for c, (node, variants, fx, sc, sections, spec) in COMPONENTS.items():
    d = f"src/components/{c}"
    for f in (f"{c}.css", f"{c}.html", "README.md"): ok(f"{c}: {f} exists", os.path.exists(f"{d}/{f}"))
    ok(f"{c}: fixture exists", os.path.exists(f"tests/fixtures/{fx}"))
    ok(f"{c}: showcase exists", os.path.exists(f"showcase/components/{sc}"))
    fxs = open(f"tests/fixtures/{fx}", encoding="utf-8").read()
    m = re.search(r"variants rendered: \$\{[^}]+\} \(expected (\d+)", fxs)
    ok(f"{c}: fixture expects {variants}", m and int(m.group(1)) == variants, m and m.group(1))
    total += variants
    readme = open(f"{d}/README.md", encoding="utf-8").read(); css = open(f"{d}/{c}.css", encoding="utf-8").read()
    ok(f"{c}: README cites Figma set {node}", node in readme or (c == "input" and "1066:40663" in readme))
    ok(f"{c}: CSS cites Figma set", node in css)
    for sec in sections:
        ok(f"{c}: evidence {sec} exists", re.search(rf"^## {sec[1:]}\. ", evidence, re.M) is not None)
        ok(f"{c}: README references {sec}", sec in readme or sec.replace("§", "§") in readme)
    # every node ID cited in the CSS is present in the evidence or the component spec
    spec_txt = open(f"docs/figma-audit/components/{spec}", encoding="utf-8").read()
    ids = set(re.findall(r"\b(\d{3,4}:\d{3,5})\b", css))
    missing = sorted(i for i in ids if i not in evidence and i not in spec_txt and i.split(":")[1] not in evidence)
    ok(f"{c}: CSS node IDs traceable ({len(ids)})", not missing, missing)
ok("wrapper documented", os.path.exists("src/components/selection-controls/README.md") and "1504:57173" in open("src/components/selection-controls/README.md", encoding="utf-8").read())
ok("total variants 1,226", total == 1226, total)
# 2. API: every Figma property value has a class (spot inventory from CSS)
api = {
 "button": [f"annachy-button--{t}" for t in ("primary", "secondary", "secondary-grey", "tertiary", "tertiary-grey", "link")] + [f"annachy-button--size-{s}" for s in (24, 26, 28, 32, 36, 38, 40, 42, 46, 48, 52, 56)],
 "button-gradient": [f"annachy-button-gradient--size-{s}" for s in (24, 26, 28, 32, 36, 40, 42, 46, 48, 52, 56)],
 "input": ["annachy-input--outline", "annachy-input--filled", "annachy-input--success"] + [f"annachy-input--size-{s}" for s in (46, 48, 50, 54, 56)] + [f"annachy-input--radius-{r}" for r in (4, 6, 8, 10, 12)],
 "checkbox": [f"annachy-checkbox--{x}" for x in ("small", "medium", "large", "control-right", "align-top", "align-bottom")],
 "radio": [f"annachy-radio--{x}" for x in ("small", "medium", "large", "control-right", "align-top", "align-bottom")],
 "toggle": [f"annachy-toggle--{x}" for x in ("small", "medium", "large", "control-right", "align-top", "align-bottom")],
}
for c, classes in api.items():
    css = open(f"src/components/{c}/{c}.css", encoding="utf-8").read()
    miss = [k for k in classes if f".{k}" not in css]
    ok(f"{c}: API classes defined ({len(classes)})", not miss, miss)
# 3. tokens + token CSS: committed integrity baseline (tests/tools/baseline.json)
sys.dont_write_bytecode = True; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import baseline
bl = json.load(open(baseline.BASELINE, encoding="utf-8"))
new = {t["css"]: t for t in json.load(open("src/tokens/tokens.json", encoding="utf-8"))["tokens"]}
changed = [k for k, h in bl["tokens_original"].items() if k not in new or baseline.canon(new[k]) != h]
ok("457 original tokens unchanged (value + metadata)", len(bl["tokens_original"]) == 457 and not changed, changed)
added = sorted(set(new) - set(bl["tokens_original"]))
ok("only the 7 approved Loading tokens added", added == sorted(bl["tokens_added"]) and len(added) == 7 and all(a.endswith("-loading") for a in added), added)
ok("no radius-6 / radius-10 token", "--annachy-radius-6" not in new and "--annachy-radius-10" not in new)
for f, h in bl["token_css"].items():
    ok(f"{f} byte-identical to pre-R3 baseline", baseline.sha(f) == h)
# 4. no hard-coded colours outside documented raw Figma values
RAW = {"button": {"#dcdfe5"}, "input": {"#3a6ff7"}}
for c in COMPONENTS:
    src = re.sub(r"/\*.*?\*/", "", open(f"src/components/{c}/{c}.css", encoding="utf-8").read(), flags=re.S)
    hexes = set(h.lower() for h in re.findall(r"#[0-9a-fA-F]{3,8}\b", src))
    ok(f"{c}: only documented raw hex", hexes <= RAW.get(c, set()), hexes)
# Figma operations: verified from a Claude Code session transcript when one is supplied
# (env ANNACHY_FIGMA_LOG = path to the .jsonl); otherwise reported as SKIPPED (not counted).
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
    print("Figma tool invocations (transcript):", used)
else:
    print("SKIPPED Figma transcript check (set ANNACHY_FIGMA_LOG to a session .jsonl to enable)")
print(f"STATIC CHECKS: {n[0]} · failures: {len(fails)}")
for f in fails: print("  FAIL", f)
print("R3 CLOSURE STATIC RESULT:", "PASS" if not fails else "FAIL")
sys.exit(1 if fails else 0)
