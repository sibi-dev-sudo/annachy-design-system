"""R7-1 icon export pipeline — shared helpers (Python standard library only).

Pipeline (run from the project root with `python -I`):
  1. Exports were made read-only with the Figma MCP tool `download_assets` (format svg) on the 33 category frames of
     page 1801:5142 and downloaded with curl into %TEMP%/annachy-icon-staging/<nodeId with ':'→'-'>.svg (outside the repo).
  2. ingest_exports.py  — copies each staging export byte-for-byte to its original path and writes exports.json.
  3. split_icons.py     — pairs SVG groups with metadata variants, fits the export transform, analyses scale
                          equivalence and duplicates, writes the normalised assets, catalogue, manifests, variant boxes.
  4. write_report.py    — writes docs/figma-audit/r7-1-icon-export-report.md from the JSON results.
Inputs: the saved page metadata (get_metadata of 1801:5142, path in METADATA or env ANNACHY_ICON_METADATA) and
docs/figma-audit/r7-0-iconography-inventory.json.
"""
import hashlib, json, os, re, unicodedata
import xml.etree.ElementTree as ET

ROOT = os.getcwd()
HERE = os.path.dirname(os.path.abspath(__file__))
FILE_KEY = "rM3ixSG6i3DFfKZFWuxzs4"
PAGE = "1801:5142"
EXPORTED_ON = "2026-11-20"
STAGING = os.path.join(os.environ.get("TEMP", "/tmp"), "annachy-icon-staging")
METADATA = os.environ.get("ANNACHY_ICON_METADATA", os.path.join(
    os.environ.get("TEMP", "/tmp"), "claude", "6aacffd1445ba30d", "11b77c01-2212-4a89-9a6c-46510b235852",
    "scratchpad", "iconography", "icons-page.xml"))
INVENTORY = "docs/figma-audit/r7-0-iconography-inventory.json"
SIZES = {"XS": 16, "S": 20, "M": 24, "L": 32, "XL": 40}
SIZE_ORDER = ["XS", "S", "M", "L", "XL"]
SOURCE_ID = "iconly-annachy"
ORIG_DIR = "src/icons/originals/" + SOURCE_ID
BRANDS_ROOT = "restricted/brands"
LICENCE_TEXT = "Iconly (purchased by the project owner; licence text not on file) — internal use only, not for redistribution"
OUT_JSON = os.path.join(HERE, "results")          # machine-readable results (no URLs)

sha = lambda b: hashlib.sha256(b).hexdigest()


def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii").lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "icon"


def strip_suffix(i):
    """Figma de-duplicates SVG ids with _2, _3 … and writes non-ASCII names as Latin-1 character references of their
    UTF-8 bytes (e.g. 'س' → '&#216;&#179;'); undo both before comparing with the Figma layer name."""
    i = re.sub(r"_\d+$", "", i)
    try: return i.encode("latin-1").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError): return i


def categories():
    """The 33 category frames (inventory order), with unique slugs; the second 'Calender & date' is a duplicate."""
    inv = json.load(open(INVENTORY, encoding="utf-8"))
    cats, seen = [], {}
    for c in inv["categories"]:
        if not (c.get("nodeId") or "").startswith("1802:"): continue
        base = slugify(c["name"])
        e = {"name": c["name"], "nodeId": c["nodeId"], "slug": base, "inventoryVariants": c["variants"], "inventorySets": c["iconCount"]}
        if base in seen:
            e["slug"] = f"{base}-{sum(1 for x in cats if x['slug'].startswith(base)) + 1}"
            e["duplicateOf"] = seen[base]
        else:
            seen[base] = c["nodeId"]
        e["restricted"] = c["name"] == "Brands"
        e["original"] = f"{BRANDS_ROOT}/originals/brands.svg" if e["restricted"] else f"{ORIG_DIR}/{e['slug']}.svg"
        e["staging"] = os.path.join(STAGING, c["nodeId"].replace(":", "-") + ".svg")
        cats.append(e)
    assert len(cats) == 33, len(cats)
    return cats, inv


def load_metadata():
    root = ET.parse(METADATA).getroot()
    parent = {c: p for p in root.iter() for c in p}
    return root, parent


def parse_variant_name(name):
    """'Icon Size=XS, Style=Outline' → ('XS', 'Outline' | None)."""
    props = dict(p.split("=", 1) for p in [x.strip() for x in name.split(",")] if "=" in p)
    props = {k.strip(): v.strip() for k, v in props.items()}
    return props.get("Icon Size"), props.get("Style"), props


def dump(name, obj, compact=False):
    os.makedirs(OUT_JSON, exist_ok=True)
    with open(os.path.join(OUT_JSON, name), "w", encoding="utf-8", newline="\n") as f:
        json.dump(obj, f, ensure_ascii=False, indent=None if compact else 1, separators=(",", ":") if compact else None)
        f.write("\n")
