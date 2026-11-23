"""R5 icon infrastructure — static checks (read-only). Run from the project root:
    python -I tests/tools/r5_icons_static.py
1. The real manifest (src/icons/manifest.json) validates against the schema and policy. Since R7-1 (export approved
   2026-11-20) it is 'active'; the full R7-1 asset checks are in tests/tools/r7_icons_static.py.
2. Icon artwork exists only under src/icons/originals/ and src/icons/svg/ (no asset URLs in src/).
3. Validator self-test: every synthetic valid probe passes; every invalid probe fails with exactly its expected rule code;
   every manifest case yields exactly its expected rule codes. (Fixtures: tests/fixtures/r5-icons/ — geometric probes, not icons.)
"""
import glob, json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
sys.dont_write_bytecode = True; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import icons_lib as L

fails, n = [], [0]
def ok(name, cond, detail=""):
    n[0] += 1
    if not cond: fails.append(f"{name} {detail}")

schema = json.load(open("src/icons/manifest.schema.json", encoding="utf-8"))
ok("schema declares draft 2020-12", schema.get("$schema", "").endswith("2020-12/schema"))
man = json.load(open("src/icons/manifest.json", encoding="utf-8"))
probs = L.manifest_problems(man, schema, ".", recorded=[])
ok("src/icons/manifest.json valid (schema + policy)", not probs, probs)
ok("manifest status is 'active' (R7-1)", man["status"] == "active")
ok("D-12 / D-13 resolved (in-file Icons page 1801:5142)", all(isinstance(man["decisions"][k], dict) for k in ("D-12", "D-13")))
ok("export approval recorded (R7-1), no gate open", isinstance(man["decisions"]["exportApproval"], dict) and "open" not in man["decisions"].values())
# identity map: component slot -> Figma icon set (no artwork)
fmap = json.load(open("src/icons/figma-icon-map.json", encoding="utf-8"))
inv = json.load(open("docs/figma-audit/r7-0-iconography-inventory.json", encoding="utf-8"))
inv_sets = {i["setNodeId"]: i for i in inv["icons"] if i.get("setNodeId")}
css = "".join(open(f, encoding="utf-8").read() for f in glob.glob("src/components/*/*.css"))
for sl in fmap["slots"]:
    ok(f"map {sl['id']}: set {sl['setNodeId']} exists in the Icons-page inventory", sl["setNodeId"] in inv_sets)
    ok(f"map {sl['id']}: size {sl['iconSize']} = {sl['px']}px is a size of the set", f"{sl['iconSize']} {sl['px']}" in (inv_sets.get(sl["setNodeId"], {}).get("sizes") or []))
    ok(f"map {sl['id']}: style {sl['style']} exists in the set", sl["style"] in (inv_sets.get(sl["setNodeId"], {}).get("styles") or []))
    ok(f"map {sl['id']}: slot class exists in component CSS", sl["slotClass"].split()[0] in css)
ok("map lists 8 mapped slots and 5 documented exceptions", len(fmap["slots"]) == 8 and len(fmap["unmapped"]) == 5)
ok("manifest lists the Iconly source, icons, sizes 16–40 and outline/filled", man["sources"] and man["icons"] and man["sizeScale"] == [16, 20, 24, 32, 40] and man["styles"] == ["outline", "filled"])
svgs = [f.replace("\\", "/") for f in glob.glob("src/**/*.svg", recursive=True)]
ok("SVG artwork only under src/icons/originals/ and src/icons/svg/", all(f.startswith(("src/icons/originals/", "src/icons/svg/")) for f in svgs), [f for f in svgs if not f.startswith(("src/icons/originals/", "src/icons/svg/"))][:5])
ok("no Figma asset URLs in src/", not any(b"figma.com/api/mcp/asset" in open(f, "rb").read() for f in glob.glob("src/**/*.*", recursive=True)))
ok("src/icons holds README, catalogue, map, icons.js helper, manifest, schema, originals/ and svg/", sorted(x for x in os.listdir("src/icons") if x != ".gitkeep") == ["README.md", "catalogue.json", "figma-icon-map.json", "icons.js", "manifest.json", "manifest.schema.json", "originals", "svg"], os.listdir("src/icons"))

FX = "tests/fixtures/r5-icons"
for f in sorted(glob.glob(f"{FX}/svg/valid/*.svg")):
    p = L.svg_problems(open(f, "rb").read())
    ok(f"valid probe {os.path.basename(f)} passes", not p, p)
for f in sorted(glob.glob(f"{FX}/svg/invalid/*.svg")):
    want = os.path.basename(f)[:3].upper()
    codes = {c for c, _ in L.svg_problems(open(f, "rb").read())}
    ok(f"invalid probe {os.path.basename(f)} rejected with {want} only", codes == {want}, codes)
orig = open(f"{FX}/manifests/ok-active/src/icons/originals/test-source/probe-square.svg", "rb").read()
ok("original (fixed size, hex colour) accepted under the reduced original rules", not L.svg_problems(orig, normalized=False))
ok("…but would be rejected as a normalized file (V04, V06)", {c for c, _ in L.svg_problems(orig)} == {"V04", "V06"})
ok("duotone probe detected as multi-tone", L.is_multitone(open(f"{FX}/svg/valid/duotone-opacity.svg", "rb").read()))
ok("canonical artwork hash ignores whitespace", L.canonical_artwork(b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><rect width="4"  height="4"/></svg>')
   == L.canonical_artwork(b'<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">\n <rect height="4" width="4"/>\n</svg>'))
cases = sorted(glob.glob(f"{FX}/manifests/*/manifest.json"))
for f in cases:
    m = json.load(open(f, encoding="utf-8")); want = sorted(set(m.pop("$expect")))
    got = sorted({c for c, _ in L.manifest_problems(m, schema, os.path.dirname(f))})
    ok(f"manifest case {os.path.basename(os.path.dirname(f))} → {want or 'valid'}", got == want, got)
ok("manifest self-test covers every policy / duplicate / integrity / naming rule",
   {c for f in cases for c in json.load(open(f, encoding="utf-8"))["$expect"]} >= {"S", "P01", "P02", "P03", "P04", "P05", "P06", "P07", "P08", "D01", "D02", "I01", "I02", "I03", "N01", "V06"})
ok("SVG self-test covers V01–V11", {os.path.basename(f)[:3].upper() for f in glob.glob(f"{FX}/svg/invalid/*.svg")} == {f"V{i:02d}" for i in range(1, 12)})

print(f"R5 ICONS STATIC: {n[0]} checks · failures: {len(fails)}")
for f in fails: print("  FAIL", f)
print("R5 ICONS STATIC RESULT:", "PASS" if not fails else "FAIL")
sys.exit(1 if fails else 0)
