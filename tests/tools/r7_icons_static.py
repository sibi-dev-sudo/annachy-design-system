"""R7-1 icon asset set — static checks (read-only). Run from the project root:
    python -I tests/tools/r7_icons_static.py
1. src/icons/manifest.json (active) and restricted/brands/manifest.json (restricted) validate (schema + policy,
   rule exceptions only where recorded in knownProblems).
2. src/icons/catalogue.json: 33 categories, 5,128 sets, 35,890 variants accounted for, every file exists, unique slugs,
   Brands only under restricted/, duplicate 'Calender & date' frame flagged.
3. Every normalised SVG passes icons_lib.svg_problems (recorded exceptions excepted); file count = unique assets needed.
4. Originals byte-identical to the recorded exports (SHA-256); no Figma asset URL anywhere in the repository.
"""
import glob, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
sys.dont_write_bytecode = True; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import icons_lib as L

fails, n = [], [0]
def ok(name, cond, detail=""):
    n[0] += 1
    if not cond: fails.append(f"{name} {str(detail)[:300]}")

SIZES = {"XS": 16, "S": 20, "M": 24, "L": 32, "XL": 40}
schema = json.load(open("src/icons/manifest.schema.json", encoding="utf-8"))
man = json.load(open("src/icons/manifest.json", encoding="utf-8"))
bman = json.load(open("restricted/brands/manifest.json", encoding="utf-8"))
exports = json.load(open("tests/tools/icons_export/results/exports.json", encoding="utf-8"))
res = json.load(open("tests/tools/icons_export/results/split-results.json", encoding="utf-8"))
cat = json.load(open("src/icons/catalogue.json", encoding="utf-8"))
boxes = json.load(open("tests/tools/icons_export/variant-boxes.json", encoding="utf-8"))

# 1 — manifests
for label, m, status in (("src/icons/manifest.json", man, "active"), ("restricted/brands/manifest.json", bman, "restricted")):
    rec = []
    probs = L.manifest_problems(m, schema, ".", recorded=rec)
    ok(f"{label} valid (schema + policy)", not probs, probs[:5])
    ok(f"{label} status {status}", m["status"] == status)
    ok(f"{label}: export approval recorded", m["decisions"]["exportApproval"] == {"approvedBy": "Project owner", "date": "2026-11-20", "reference": "Export approval for page 1801:5142, local internal use only"})
    ok(f"{label}: D-15 records Iconly purchased / internal-only / licence text not on file",
       isinstance(m["decisions"]["D-15"], dict) and all(w in m["decisions"]["D-15"]["reference"] for w in ("Iconly", "internal use only", "not on file")))
    ok(f"{label}: licence internal-only, attribution kept", all(s["licence"]["redistribution"] == "internal-only" and "Iconly" in s["licence"]["attributionText"] for s in m["sources"]))
    ok(f"{label}: recorded exceptions are only V08 (clip-path defs)", {c for c, _ in rec} <= {"V08"}, rec[:3])
ok("brands manifest root is restricted/brands", bman.get("root") == "restricted/brands")
ok("src manifest lists no Brands icon", not any(i["category"] == "brands" for i in man["icons"]))
ok("brands manifest lists only Brands icons", {i["category"] for i in bman["icons"]} == {"brands"})
fmap = json.load(open("src/icons/figma-icon-map.json", encoding="utf-8"))

# 2 — catalogue
ok("catalogue source block", cat["source"]["fileKey"] == "rM3ixSG6i3DFfKZFWuxzs4" and cat["source"]["page"] == "1801:5142" and "internal use only" in cat["source"]["licence"])
ok("catalogue sizes", cat["sizes"] == SIZES)
cats = cat["categories"]
ok("33 categories", len(cats) == 33, len(cats))
sets = [s for c in cats for s in c["sets"]]
ok("5,128 sets", len(sets) == 5128, len(sets))
variants = [v for s in sets for st in s["styles"].values() for v in st["variants"].values()]
missing = res["missing"]
ok("35,890 variants accounted for (paired + missing with reason)", len(variants) + len(missing) == 35890 and len(set(variants)) == len(variants), (len(variants), len(missing)))
ok("every missing variant has a reason", all(m.get("reason") for m in missing))
slugs = [s["slug"] for s in sets]
ok("no duplicate set slugs", len(slugs) == len(set(slugs)))
ok("slugs are kebab-case (with optional -- qualifiers)", all(re.fullmatch(r"[a-z0-9]+(-{1,2}[a-z0-9]+)*", s) for s in slugs))
dups = [c for c in cats if c.get("duplicateOf")]
ok("duplicated 'Calender & date' frame flagged", [(c["name"], c["nodeId"], c["duplicateOf"]) for c in dups] == [("Calender & date", "1802:138448", "1802:121134")])
files = set()
for c in cats:
    for s in c["sets"]:
        for style, st in s["styles"].items():
            for p in [st["file"], *st.get("perSize", {}).values()]:
                files.add(os.path.normpath(os.path.join("src/icons", p)))
                if c["restricted"]: ok(f"brands file under restricted/: {p}", p.startswith("../../restricted/brands/svg/"))
                else: ok(f"file under svg/: {p}", p.startswith(f"svg/{style}/"))
ok("Brands is the only restricted category", [c["name"] for c in cats if c["restricted"]] == ["Brands"])
ok("every catalogue file exists", all(os.path.isfile(f) for f in files), [f for f in files if not os.path.isfile(f)][:5])
for sl in fmap["slots"]:
    s = next((x for x in sets if x["nodeId"] == sl["setNodeId"]), None)
    ok(f"map slot {sl['id']}: set {sl['setNodeId']} in catalogue with {sl['style']} {sl['iconSize']}", s and sl["iconSize"] in s["styles"].get(sl["style"].lower(), {}).get("variants", {}))

# 3 — normalised files
disk = sorted(f.replace("\\", "/") for d in ("src/icons/svg", "restricted/brands/svg") for f in glob.glob(f"{d}/**/*.svg", recursive=True))
ok("normalised files on disk = files referenced by the catalogue", {os.path.normpath(f) for f in disk} == files, len(disk))
ok("file count = unique artwork assets needed", len(disk) == res["uniqueAssetsNeeded"] == res["files"], (len(disk), res["uniqueAssetsNeeded"]))
known = {f["path"]: {k["code"] for k in i.get("knownProblems", [])} for m in (man, bman) for i in m["icons"] for f in [i["normalized"], *i.get("perSize", {}).values()]}
ok("every normalised file is listed in a manifest", set(known) == set(disk))
bad = []
for f in disk:
    p = [c for c, _ in L.svg_problems(open(f, "rb").read()) if c not in known.get(f, set())]
    if p: bad.append((f, p))
ok(f"all {len(disk)} normalised SVGs pass svg_problems (recorded exceptions excepted)", not bad, bad[:5])
ok("no Brands artwork under src/", not glob.glob("src/**/brands*.svg", recursive=True) and not any(s["slug"].startswith("brands-") and not c["restricted"] for c in cats for s in c["sets"]))
ok("variant boxes: one per paired variant, files exist", len(boxes) == len(variants) and all(os.path.isfile(b["original"]) and os.path.isfile(os.path.normpath(os.path.join("src/icons", b["normalized"]))) for b in boxes.values()))

# 4 — originals and URLs
for e in exports:
    ok(f"original {e['original']} sha256", os.path.isfile(e["original"]) and L.sha_bytes(open(e["original"], "rb").read()) == e["sha256"])
    ok(f"original {e['original']} location", e["original"].startswith("restricted/brands/originals/" if e["restricted"] else "src/icons/originals/iconly-annachy/"))
ok("33 originals recorded", len(exports) == 33)
orig_hash = {e["original"]: e["sha256"] for e in exports}
ok("manifest original hashes = recorded exports", all(orig_hash.get(i["original"]["path"]) == i["original"]["sha256"] for m in (man, bman) for i in m["icons"]))
ok("restricted/brands/README.md states the rights restriction", "not verified" in open("restricted/brands/README.md", encoding="utf-8").read())
url = re.compile(rb"figma\.com/api/mcp/asset/[0-9a-f]{8}-")     # an actual asset URL (with id), not a mention
hits = []
for dp, dn, fn in os.walk("."):
    dn[:] = [d for d in dn if d not in (".git", "node_modules")]
    for f in fn:
        p = os.path.join(dp, f)
        try:
            if url.search(open(p, "rb").read()): hits.append(p)
        except OSError: pass
ok("no Figma asset URL anywhere in the repository", not hits, hits)

print(f"R7 ICONS STATIC: {n[0]} checks · failures: {len(fails)}")
for f in fails[:40]: print("  FAIL", f)
print("R7 ICONS STATIC RESULT:", "PASS" if not fails else "FAIL")
sys.exit(1 if fails else 0)
