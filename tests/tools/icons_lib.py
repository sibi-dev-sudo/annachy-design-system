"""R5 icon infrastructure: manifest schema validation, SVG validation, naming, duplicate and integrity checks.
Python standard library only. Pure functions; never writes files. Rule codes are documented in
docs/implementation/r5-implementation-spec.md §6.

Rule codes
  S    manifest does not match manifest.schema.json
  P01  status 'blocked' but sources / icons / sizeScale / styles are not empty
  P02  status 'active' but a decision gate is still 'open'
  P03  icon licence does not allow redistribution          P04  attribution required but empty
  P05  icon source not in sources[] or source not approved P06  style not in approved styles
  P07  size not in approved sizeScale                       P08  multi-tone SVG (opacity / several fills) not flagged multicolor
  P09  category not in categories
  N01  normalized path is not src/icons/svg/<style>/<name>.svg, or original not under src/icons/originals/<source>/
  D01  duplicate (name, style)                              D02  two icons with identical normalized artwork
  I01  file hash differs from the manifest                  I02  listed file missing
  I03  SVG under src/icons/ not listed in the manifest (orphan)
  V01  not well-formed XML     V02 root is not <svg> (SVG namespace)   V03 viewBox missing / invalid
  V04  width/height on root    V05 active or external content (script, on*, foreignObject, image, external href, javascript:)
  V06  colour other than currentColor / none                           V07 <text> (glyphs must be outlined)
  V08  id attributes (collide when inlined)                            V09 <style> element
  V10  DOCTYPE / entities      V11 larger than 16 KB
Originals (byte-preserved exports) are only checked for V01, V02, V05, V10 — they are never modified.
R7-1 extensions (manifest.schema.json description E1–E7): P03 accepts 'internal-only'; gates may be notApplicable;
status 'restricted' requires a root under restricted/ (N01); N01 / I03 use the manifest 'root' (default src/icons);
perSize files are hash-, SVG- and path-checked like 'normalized'; top-level 'originals' (E8) are hash-checked and count as listed; codes in an icon's knownProblems are recorded, not failed;
each file is read and hashed once (originals are category files shared by many icons).
"""
import hashlib, json, os, re
import xml.etree.ElementTree as ET

SVG_NS = "http://www.w3.org/2000/svg"
XLINK = "{http://www.w3.org/1999/xlink}href"
MAX_BYTES = 16 * 1024
SLUG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
COLOUR_ATTRS = ("fill", "stroke", "color", "stop-color", "flood-color", "lighting-color")
ALLOWED_COLOUR = {"currentcolor", "none", "inherit", "transparent"}
sha_bytes = lambda b: hashlib.sha256(b).hexdigest()


# ------------------------------------------------------------------ minimal JSON Schema (draft 2020-12 subset)
def schema_errors(inst, schema, root=None, path="$"):
    root = root or schema
    if "$ref" in schema:
        node = root
        for part in schema["$ref"].lstrip("#/").split("/"): node = node[part]
        return schema_errors(inst, node, root, path)
    errs = []
    if "oneOf" in schema:
        hits = sum(1 for s in schema["oneOf"] if not schema_errors(inst, s, root, path))
        if hits != 1: errs.append(f"{path}: matches {hits} of oneOf")
        return errs
    if "const" in schema and inst != schema["const"]: errs.append(f"{path}: expected {schema['const']!r}")
    if "enum" in schema and inst not in schema["enum"]: errs.append(f"{path}: {inst!r} not in {schema['enum']}")
    t = schema.get("type")
    types = {"object": dict, "array": list, "string": str, "boolean": bool}
    if t == "integer" and not (isinstance(inst, int) and not isinstance(inst, bool)): return errs + [f"{path}: not an integer"]
    if t in types and not isinstance(inst, types[t]): return errs + [f"{path}: not a {t}"]
    if isinstance(inst, str):
        if "pattern" in schema and not re.search(schema["pattern"], inst): errs.append(f"{path}: {inst!r} !~ {schema['pattern']}")
        if len(inst) < schema.get("minLength", 0): errs.append(f"{path}: too short")
        if "maxLength" in schema and len(inst) > schema["maxLength"]: errs.append(f"{path}: too long")
    if isinstance(inst, int) and not isinstance(inst, bool):
        if "minimum" in schema and inst < schema["minimum"]: errs.append(f"{path}: < {schema['minimum']}")
        if "maximum" in schema and inst > schema["maximum"]: errs.append(f"{path}: > {schema['maximum']}")
    if isinstance(inst, list):
        if len(inst) < schema.get("minItems", 0): errs.append(f"{path}: fewer than {schema['minItems']} items")
        if schema.get("uniqueItems") and len({json.dumps(x, sort_keys=True) for x in inst}) != len(inst): errs.append(f"{path}: items not unique")
        if "items" in schema:
            for i, x in enumerate(inst): errs += schema_errors(x, schema["items"], root, f"{path}[{i}]")
    if isinstance(inst, dict):
        for k in schema.get("required", []):
            if k not in inst: errs.append(f"{path}: missing {k}")
        props = schema.get("properties", {})
        for k, v in inst.items():
            if k in props: errs += schema_errors(v, props[k], root, f"{path}.{k}")
            elif schema.get("additionalProperties") is False: errs.append(f"{path}: unexpected property {k}")
    return errs


# ------------------------------------------------------------------ SVG
def svg_problems(data: bytes, normalized=True):
    """Return a list of (code, message). `normalized=False` applies the reduced rule set for byte-preserved originals."""
    out = []
    text = data.decode("utf-8", errors="replace")
    if re.search(r"<!DOCTYPE|<!ENTITY", text, re.I): return [("V10", "DOCTYPE / entity declarations are not allowed")]
    try: root = ET.fromstring(data)
    except ET.ParseError as e: return [("V01", f"not well-formed: {e}")]
    if root.tag != f"{{{SVG_NS}}}svg": out.append(("V02", f"root is {root.tag}"))
    for el in root.iter():
        tag = el.tag.split("}")[-1]
        if tag in ("script", "foreignObject", "image", "iframe", "audio", "video", "animate", "set"): out.append(("V05", f"<{tag}> not allowed"))
        for k, v in el.attrib.items():
            name = k.split("}")[-1]
            if name.lower().startswith("on"): out.append(("V05", f"event handler {name}"))
            if (name == "href" or k == XLINK) and not v.startswith("#"): out.append(("V05", f"external reference {v[:40]}"))
            if "javascript:" in v.lower(): out.append(("V05", "javascript: URL"))
    if not normalized: return out
    vb = root.get("viewBox", "")
    nums = re.split(r"[\s,]+", vb.strip()) if vb else []
    try: ok_vb = len(nums) == 4 and float(nums[2]) > 0 and float(nums[3]) > 0
    except ValueError: ok_vb = False
    if not ok_vb: out.append(("V03", f"viewBox {vb!r}"))
    if root.get("width") is not None or root.get("height") is not None: out.append(("V04", "width/height on <svg> (size comes from the slot)"))
    for el in root.iter():
        tag = el.tag.split("}")[-1]
        if tag == "text" or tag == "tspan": out.append(("V07", "<text> present"))
        if tag == "style": out.append(("V09", "<style> element"))
        if el.get("id") is not None: out.append(("V08", f"id={el.get('id')}"))
        for a in COLOUR_ATTRS:
            v = el.get(a)
            if v is not None and v.strip().lower() not in ALLOWED_COLOUR and not v.startswith("url(#"): out.append(("V06", f"{a}={v}"))
        st = el.get("style")
        if st:
            for prop, val in re.findall(r"([\w-]+)\s*:\s*([^;]+)", st):
                if prop in COLOUR_ATTRS and val.strip().lower() not in ALLOWED_COLOUR: out.append(("V06", f"style {prop}:{val.strip()}"))
    if len(data) > MAX_BYTES: out.append(("V11", f"{len(data)} bytes"))
    return out


def is_multitone(data: bytes):
    """True when the artwork relies on more than one tone (opacity layers) — must be inlined, not used as a CSS mask."""
    root = ET.fromstring(data)
    return any(el.get("opacity") not in (None, "1") or el.get("fill-opacity") not in (None, "1") or el.get("stroke-opacity") not in (None, "1") for el in root.iter())


def canonical_artwork(data: bytes):
    """Hash of the geometry, independent of whitespace and attribute order (duplicate detection, D02)."""
    root = ET.fromstring(data)
    parts = []
    for el in root.iter():
        parts.append(el.tag + "|" + "|".join(f"{k}={' '.join(v.split())}" for k, v in sorted(el.attrib.items())))
    return hashlib.sha256("\n".join(parts).encode("utf-8")).hexdigest()


# ------------------------------------------------------------------ manifest
REDISTRIBUTABLE = ("allowed", "internal-only")      # R7-1 E1: 'internal-only' = local internal use, never redistributed


def manifest_problems(manifest: dict, schema: dict, base_dir: str, recorded=None):
    """Validate a manifest against the schema and the R5 policy. Paths in the manifest are relative to base_dir.
    R7-1 extensions (see the schema description E1–E7): 'internal-only' licences, notApplicable gates, status
    'restricted' (root under restricted/), manifest 'root', '--' names, perSize files, knownProblems. Problems whose
    code is listed in an icon's knownProblems are appended to `recorded` (if a list is given) instead of being errors."""
    errs = [("S", e) for e in schema_errors(manifest, schema)]
    if errs: return errs
    gates_open = [k for k, v in manifest["decisions"].items() if v == "open"]
    icons, sources = manifest["icons"], {s["id"]: s for s in manifest["sources"]}
    root = manifest.get("root", "src/icons")
    if manifest["status"] == "blocked":
        if icons or manifest["sources"] or manifest["sizeScale"] or manifest["styles"]:
            errs.append(("P01", "blocked manifest must not list sources, icons, sizes or styles"))
    elif gates_open:
        errs.append(("P02", f"{manifest['status']} manifest with open gates {gates_open}"))
    if (manifest["status"] == "restricted") != root.startswith("restricted/"):
        errs.append(("N01", f"status {manifest['status']!r} does not match root {root!r} (restricted files live under restricted/ only)"))
    seen, art, cache = {}, {}, {}
    def read(path, normalized):
        key = (path, normalized)
        if key not in cache:
            f = os.path.join(base_dir, path)
            if not os.path.exists(f): cache[key] = None
            else:
                data = open(f, "rb").read()
                probs = svg_problems(data, normalized=normalized)
                cache[key] = (data, sha_bytes(data), probs,
                              canonical_artwork(data) if normalized and not any(c == "V01" for c, _ in probs) else None)
        return cache[key]
    for i in icons:
        tag = f"{i['name']}/{i['style']}"
        known = {k["code"] for k in i.get("knownProblems", [])}
        src = sources.get(i["source"])
        if not src or src["approved"] == "open": errs.append(("P05", f"{tag}: source {i['source']!r} missing or unapproved"))
        lic = src["licence"] if src and i["licence"] == "inherit" else i["licence"] if i["licence"] != "inherit" else None
        if lic and lic["redistribution"] not in REDISTRIBUTABLE: errs.append(("P03", f"{tag}: redistribution {lic['redistribution']}"))
        if lic and lic["attributionRequired"] and not i["attribution"].strip(): errs.append(("P04", f"{tag}: attribution required"))
        if i["style"] not in manifest["styles"]: errs.append(("P06", f"{tag}: style not approved"))
        bad = [s for s in i["sizes"] if s not in manifest["sizeScale"]]
        if bad: errs.append(("P07", f"{tag}: sizes {bad} not in scale"))
        if i["category"] not in manifest["categories"]: errs.append(("P09", f"{tag}: category not listed"))
        orig_dir = f"{root}/originals/" + (f"{i['source']}/" if root == "src/icons" else "")
        per = i.get("perSize", {})
        if i["normalized"]["path"] != f"{root}/svg/{i['style']}/{i['name']}.svg" or not i["original"]["path"].startswith(orig_dir) \
                or any(f["path"] != f"{root}/svg/{i['style']}/{i['name']}--{z.lower()}.svg" for z, f in per.items()):
            errs.append(("N01", f"{tag}: path convention"))
        if tag in seen: errs.append(("D01", f"{tag}: duplicate name/style"))
        seen[tag] = True
        files = [("original", i["original"])] + [("normalized", i["normalized"])] + [(f"normalized {z}", f) for z, f in per.items()]
        for kind, ref in files:
            normalized = kind != "original"
            got = read(ref["path"], normalized)
            if got is None: errs.append(("I02", f"{tag}: {kind} file missing")); continue
            data, digest, probs, h = got
            if digest != ref["sha256"]: errs.append(("I01", f"{tag}: {kind} hash mismatch"))
            for code, msg in probs:
                if normalized and code in known:
                    if recorded is not None: recorded.append((code, f"{tag} ({kind}): {msg}"))
                else: errs.append((code, f"{tag} ({kind}): {msg}"))
            if h is not None:
                if h in art: errs.append(("D02", f"{tag}: same artwork as {art[h]}"))
                art[h] = tag
                if is_multitone(data) and not i.get("multicolor"): errs.append(("P08", f"{tag}: multi-tone artwork not flagged multicolor"))
    for o in manifest.get("originals", []):                              # R7-1 E8
        got = read(o["path"], False)
        if got is None: errs.append(("I02", f"original {o['path']} missing")); continue
        if got[1] != o["sha256"]: errs.append(("I01", f"original {o['path']} hash mismatch"))
        for code, msg in got[2]: errs.append((code, f"original {o['path']}: {msg}"))
    listed = {os.path.normpath(f["path"]) for i in icons for f in [i["original"], i["normalized"], *i.get("perSize", {}).values()]}
    listed |= {os.path.normpath(o["path"]) for o in manifest.get("originals", [])}
    icon_dir = os.path.join(base_dir, *root.split("/"))
    for dp, _, fs in os.walk(icon_dir):
        for fn in fs:
            if fn.lower().endswith(".svg"):
                rel = os.path.normpath(os.path.relpath(os.path.join(dp, fn), base_dir))
                if rel not in listed: errs.append(("I03", f"orphan {rel.replace(os.sep, '/')}"))
    return errs
