"""Regenerates tests/fixtures/r5-icons/ (synthetic geometric probes for the R5 validator self-test; NOT icon artwork).
Run from the project root: python -I tests/tools/gen_r5_fixtures.py — deletes and rewrites only that fixture folder."""
import hashlib, json, os, shutil
ROOT = "tests/fixtures/r5-icons"
if os.path.exists(ROOT): shutil.rmtree(ROOT)
NS = 'xmlns="http://www.w3.org/2000/svg"'
SQUARE = f'<svg {NS} viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" fill="currentColor"/></svg>\n'
CIRCLE = f'<svg {NS} viewBox="0 0 24 24"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="2"/></svg>\n'
DUO = f'<svg {NS} viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="20" fill="currentColor" opacity="0.4"/><rect x="8" y="8" width="8" height="8" fill="currentColor"/></svg>\n'
ORIG = f'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" {NS}>\n<rect x="4" y="4" width="16" height="16" fill="#1C274C"/>\n</svg>\n'
SVG = {
    "valid/square.svg": SQUARE, "valid/circle-stroke.svg": CIRCLE, "valid/duotone-opacity.svg": DUO,
    "invalid/v01-not-xml.svg": f'<svg {NS} viewBox="0 0 24 24"><rect></svg>',
    "invalid/v02-root-not-svg.svg": f'<g {NS} viewBox="0 0 24 24"><rect width="1" height="1"/></g>',
    "invalid/v03-no-viewbox.svg": f'<svg {NS}><rect width="4" height="4" fill="currentColor"/></svg>',
    "invalid/v03-bad-viewbox.svg": f'<svg {NS} viewBox="0 0 0 24"><rect width="4" height="4" fill="currentColor"/></svg>',
    "invalid/v04-fixed-size.svg": f'<svg {NS} width="24" height="24" viewBox="0 0 24 24"><rect width="4" height="4" fill="currentColor"/></svg>',
    "invalid/v05-script.svg": f'<svg {NS} viewBox="0 0 24 24"><script>alert(1)</script></svg>',
    "invalid/v05-event-handler.svg": f'<svg {NS} viewBox="0 0 24 24" onload="x()"><rect width="4" height="4" fill="currentColor"/></svg>',
    "invalid/v05-foreign-object.svg": f'<svg {NS} viewBox="0 0 24 24"><foreignObject width="4" height="4"/></svg>',
    "invalid/v05-external-href.svg": f'<svg {NS} xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 24 24"><use xlink:href="https://example.com/a.svg#x"/></svg>',
    "invalid/v05-raster-image.svg": f'<svg {NS} viewBox="0 0 24 24"><image href="data:image/png;base64,AAAA" width="4" height="4"/></svg>',
    "invalid/v06-hard-colour.svg": f'<svg {NS} viewBox="0 0 24 24"><rect width="4" height="4" fill="#1C274C"/></svg>',
    "invalid/v06-style-colour.svg": f'<svg {NS} viewBox="0 0 24 24"><rect width="4" height="4" style="fill:red"/></svg>',
    "invalid/v07-text.svg": f'<svg {NS} viewBox="0 0 24 24"><text x="0" y="12">A</text></svg>',
    "invalid/v08-id-attribute.svg": f'<svg {NS} viewBox="0 0 24 24"><rect id="a" width="4" height="4" fill="currentColor"/></svg>',
    "invalid/v09-style-element.svg": f'<svg {NS} viewBox="0 0 24 24"><style>rect{{fill:currentColor}}</style><rect width="4" height="4"/></svg>',
    "invalid/v10-doctype-entity.svg": f'<!DOCTYPE svg [<!ENTITY x "y">]><svg {NS} viewBox="0 0 24 24"><rect width="4" height="4" fill="currentColor"/></svg>',
    "invalid/v11-too-large.svg": f'<svg {NS} viewBox="0 0 24 24"><path fill="currentColor" d="M0 0{" L1 1" * 4000}"/></svg>',
}
for p, c in SVG.items():
    os.makedirs(os.path.dirname(f"{ROOT}/svg/{p}"), exist_ok=True)
    open(f"{ROOT}/svg/{p}", "w", encoding="utf-8", newline="\n").write(c)
sha = lambda s: hashlib.sha256(s.encode("utf-8")).hexdigest()
GATE = {"approvedBy": "TEST FIXTURE", "date": "2026-11-20", "reference": "synthetic self-test, not an approval"}
LIC = {"name": "TEST-ONLY", "redistribution": "allowed", "attributionRequired": False}
def base_active():
    return {"schemaVersion": "1.0.0", "status": "active", "decisions": {k: GATE for k in ("D-12", "D-13", "D-14", "D-15", "exportApproval")},
            "sizeScale": [16, 20, 24], "styles": ["linear"], "categories": ["test"],
            "sources": [{"id": "test-source", "name": "Synthetic probes", "kind": "owner-supplied", "owner": "test", "licence": LIC, "approved": GATE}],
            "icons": [icon("probe-square", SQUARE), icon("probe-circle", CIRCLE)]}
def icon(name, normalized, original=ORIG):
    return {"name": name, "category": "test", "style": "linear", "sizes": [20, 24], "source": "test-source", "sourceName": name, "figmaNodeId": "n/a",
            "original": {"path": f"src/icons/originals/test-source/{name}.svg", "sha256": sha(original)},
            "normalized": {"path": f"src/icons/svg/linear/{name}.svg", "sha256": sha(normalized)},
            "licence": "inherit", "attribution": "", "multicolor": False, "usedBy": []}
def case(name, m, files, expect):
    d = f"{ROOT}/manifests/{name}"; os.makedirs(d, exist_ok=True)
    for p, c in files.items():
        os.makedirs(os.path.dirname(f"{d}/{p}"), exist_ok=True)
        open(f"{d}/{p}", "w", encoding="utf-8", newline="\n").write(c)
    m["$expect"] = expect   # stripped by the self-test before validation
    json.dump(m, open(f"{d}/manifest.json", "w", encoding="utf-8", newline="\n"), indent=1)
def files_for(m, override=None):
    out = {}
    for i in m["icons"]:
        out[i["original"]["path"]] = ORIG
        out[i["normalized"]["path"]] = {"probe-square": SQUARE, "probe-circle": CIRCLE, "probe-duo": DUO}.get(i["name"], SQUARE)
    out.update(override or {})
    return out
m = base_active(); case("ok-active", m, files_for(m), [])
m = {"schemaVersion": "1.0.0", "status": "blocked", "decisions": {k: "open" for k in ("D-12", "D-13", "D-14", "D-15", "exportApproval")},
     "sizeScale": [], "styles": [], "categories": [], "sources": [], "icons": []}; case("ok-blocked-empty", m, {}, [])
m = base_active(); m["status"] = "blocked"; case("blocked-with-icons", m, files_for(m), ["P01"])
m = base_active(); m["decisions"]["D-15"] = "open"; case("active-with-open-gate", m, files_for(m), ["P02"])
m = base_active(); m["sources"][0]["licence"] = dict(LIC, redistribution="unknown"); case("licence-not-redistributable", m, files_for(m), ["P03"])
m = base_active(); m["sources"][0]["licence"] = dict(LIC, attributionRequired=True); case("attribution-missing", m, files_for(m), ["P04"])
m = base_active(); m["icons"][1]["source"] = "nope"; case("unknown-source", m, files_for(m), ["P05", "N01"])
m = base_active(); m["icons"][1]["style"] = "bold"; case("style-not-approved", m, files_for(m), ["P06", "N01"])
m = base_active(); m["icons"][1]["sizes"] = [24, 28]; case("size-not-in-scale", m, files_for(m), ["P07"])
m = base_active(); m["icons"][1] = icon("probe-square", SQUARE); case("duplicate-name", m, files_for(m), ["D01", "D02"])
m = base_active(); m["icons"][1] = dict(icon("probe-circle", SQUARE)); case("duplicate-content", m, files_for(m, {"src/icons/svg/linear/probe-circle.svg": SQUARE}), ["D02"])
m = base_active(); f = files_for(m); f["src/icons/svg/linear/probe-circle.svg"] = CIRCLE.replace("r=\"8\"", "r=\"9\""); case("sha-mismatch", m, f, ["I01"])
m = base_active(); f = files_for(m); del f["src/icons/originals/test-source/probe-circle.svg"]; case("original-missing", m, f, ["I02"])
m = base_active(); f = files_for(m); f["src/icons/svg/linear/orphan.svg"] = SQUARE; case("orphan-file", m, f, ["I03"])
m = base_active(); m["icons"][1]["normalized"]["path"] = "src/icons/svg/linear/wrong-name.svg"; f = files_for(m); case("path-convention", m, f, ["N01"])
bad = SVG["invalid/v06-hard-colour.svg"]
m = base_active(); m["icons"][1] = icon("probe-circle", bad); case("normalized-svg-invalid", m, files_for(m, {"src/icons/svg/linear/probe-circle.svg": bad}), ["V06"])
m = base_active(); m["icons"][0]["name"] = "Probe_Square"; case("schema-bad-name", m, files_for(m), ["S"])
m = base_active(); m["extra"] = 1; case("schema-extra-property", m, files_for(m), ["S"])
m = base_active(); m["icons"][1] = icon("probe-duo", DUO); m["icons"][1]["multicolor"] = False; case("duotone-not-flagged", m, files_for(m), ["P08"])
print("fixtures written:", sum(len(fs) for _, _, fs in os.walk(ROOT)))
