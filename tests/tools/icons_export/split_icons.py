"""R7-1 split: pair, analyse and normalise every icon variant of the Figma Icons page exports.
    python -I tests/tools/icons_export/split_icons.py
Reads the byte-preserved originals (never modifies them) and the saved page metadata. Writes:
  src/icons/svg/<style>/<slug>[--<size>].svg, restricted/brands/svg/<style>/<slug>[--<size>].svg   normalised assets
  src/icons/catalogue.json, src/icons/manifest.json, restricted/brands/manifest.json
  tests/tools/icons_export/variant-boxes.json, tests/tools/icons_export/results/*.json (report data)
Deletes nothing: if a previously generated asset is no longer produced, the run fails and lists it.
"""
import collections, json, math, os, re, sys, copy
import xml.etree.ElementTree as ET
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE))
import common as C
import pairing as P
import svggeom as G
import icons_lib as L

SVGNS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVGNS)
TOL = 1e-3                     # canonical tolerance (fraction of the icon size)
REF_ORDER = ["M", "L", "S", "XL", "XS"]
fmt = lambda v: ("%.10g" % v)


# ------------------------------------------------------------------ export transform
def exact_transform(ex, meta_frame, fit_s, fit_ox, fit_oy, clamped):
    off = 6.0 if abs(fit_ox / fit_s - 6) < abs(fit_ox / fit_s) else 0.0
    W, H = float(meta_frame.get("width")), float(meta_frame.get("height"))
    if not clamped:
        s, how = 1.0, "unscaled export"
    else:
        bg = next(e for e in ex.root if G.local(e.tag) == "rect")
        rw, rh = float(bg.get("width")), float(bg.get("height"))
        # exact when the clamped side is the frame side (+ outside stroke); otherwise (content overflowing the frame,
        # e.g. Alerts) derived from the background rect width, which is printed with 6 significant digits
        exact = {"4096/(H+2*off)": 4096 / (H + 2 * off), "4096/(W+2*off)": 4096 / (W + 2 * off)}
        how, s = min(exact.items(), key=lambda kv: abs(kv[1] * (W + 2 * off) - rw))
        if abs(s * (W + 2 * off) - rw) > 1e-3:
            how, s = "bgRectW/(W+2*off)", rw / (W + 2 * off)
    assert abs(s - fit_s) / s < 1e-4 and abs(s * off - fit_ox) < 0.6 * s and abs(s * off - fit_oy) < 0.6 * s, \
        (s, fit_s, off, fit_ox, fit_oy)
    return s, off, how


# ------------------------------------------------------------------ canonical geometry
def canonical(ex, el, x0, y0, size):
    st, nums, q = ex.geometry(el)
    out = []
    for kind, v in nums:
        if kind == "P": out += [(v[0] - x0) / size, (v[1] - y0) / size]
        elif kind == "L": out.append(v / size)
        else: out.append(v)
    return tuple(st), out, q / size        # q/size: worst export rounding as a fraction of the icon size


def equivalent(a, b, tol=TOL):
    """a, b = (structure, numbers, qrel). Scale-equivalent when structure is identical and every number agrees within
    tol plus the export rounding of both variants. Returns (equal, max |difference|)."""
    if a[0] != b[0] or len(a[1]) != len(b[1]): return False, None
    lim = tol + a[2] + b[2]
    d = max((abs(x - y) for x, y in zip(a[1], b[1])), default=0.0)
    return d <= lim, d


def rounded_key(c, step=1e-3):
    return (c[0], tuple(round(v / step) for v in c[1]))


# ------------------------------------------------------------------ normalised SVG
def normalised_svg(ex, el, X, Y, s, px, idprefix):
    """<svg viewBox="0 0 px px"> wrapping the variant's elements, geometry untouched, colours → currentColor, ids removed."""
    k = 1.0 / s
    tr = f"translate({fmt(-X)} {fmt(-Y)})" if s == 1.0 else f"scale({fmt(k)}) translate({fmt(-X)} {fmt(-Y)})"
    inherited = {}
    for a in ex.ancestors(el):                                  # inherited presentation attributes (e.g. root fill="none")
        for key, v in a.attrib.items():
            if key in G.STRUCT_ATTRS and key not in ("clip-path", "mask", "filter"): inherited[key] = v
        if a.get("transform"): raise AssertionError("ancestor transform not expected")
    refs = ex.refs(el)
    idmap = {d.get("id"): f"{idprefix}-{G.local(d.tag).lower()}{i}" for i, d in enumerate(refs)}
    def clean(e):
        e = copy.deepcopy(e)
        for x in e.iter():
            x.attrib.pop("id", None)
            for key in ("fill", "stroke", "stop-color", "color", "flood-color", "lighting-color"):
                v = x.get(key)
                if v is not None and v.strip().lower() not in ("none", "currentcolor", "inherit", "transparent") and not v.startswith("url("):
                    x.set(key, "currentColor")
            for key, v in list(x.attrib.items()):
                if "url(#" in v: x.set(key, re.sub(r"url\(#([^)]+)\)", lambda m: f"url(#{idmap.get(m.group(1), m.group(1))})", v))
        return e
    def unwrap(e):
        """Drop attribute-less <g> wrappers (no geometry or styling change)."""
        out = []
        for ch in e:
            if G.local(ch.tag) == "g" and not ch.attrib: out += unwrap(ch)
            else:
                ch[:] = unwrap(ch) if G.local(ch.tag) == "g" else list(ch); out.append(ch)
        return out
    body = clean(el)
    kids = unwrap(body) if not body.attrib else [body]
    if body.attrib: body[:] = unwrap(body)
    svg = ET.Element(f"{{{SVGNS}}}svg", {"viewBox": f"0 0 {px} {px}"})
    if refs:
        defs = ET.SubElement(svg, f"{{{SVGNS}}}defs")
        for d in refs:
            dd = clean(d); dd.set("id", idmap[d.get("id")]); defs.append(dd)
    g = ET.SubElement(svg, f"{{{SVGNS}}}g", {**{k2: ("currentColor" if k2 in ("fill", "stroke") and v not in ("none",) else v) for k2, v in inherited.items()}, "transform": tr})
    g.extend(kids)
    txt = ET.tostring(svg, encoding="unicode", short_empty_elements=True)
    txt = re.sub(r"\s*\n\s*", "", txt)
    return (txt + "\n").encode("utf-8"), bool(refs)


def main():
    cats, inv = C.categories()
    inv_sets = {i["setNodeId"]: i for i in inv["icons"] if i.get("setNodeId")}
    mroot, mparent = C.load_metadata()
    idx = {e.get("id"): e for e in mroot.iter()}
    cat_ids = {c["nodeId"] for c in cats}
    exports = {e["nodeId"]: e for e in json.load(open(os.path.join(C.OUT_JSON, "exports.json"), encoding="utf-8"))}

    sets, missing, fits = [], [], []          # every set (owned by its category) with paired variants + canonical data
    keep_ex = {}
    for c in cats:
        ex = P.Export(os.path.join(C.ROOT, c["original"]))
        assert C.sha(ex.data) == exports[c["nodeId"]]["sha256"]
        frame = idx[c["nodeId"]]
        paired, miss, msets = P.pair_export(c, ex, frame, mparent, cat_ids)
        own = [p for p in paired if p["set"]["owner"] == c["nodeId"]]
        fs, fox, foy, frms, fn, fnp = P.fit(own, ex)
        s, off, how = exact_transform(ex, frame, fs, fox, foy, exports[c["nodeId"]]["clampedTo4096"])
        # residual of the exact transform (geometry-bbox centre vs. metadata box centre), in Figma px
        res = []
        for p in own:
            m = p["meta"]; bb = G.bbox(ex.geometry(p["el"])[1])
            if bb: res.append(math.hypot((bb[0] + bb[2]) / 2 - s * (m["x"] + off + m["w"] / 2), (bb[1] + bb[3]) / 2 - s * (m["y"] + off + m["h"] / 2)) / s)
        res.sort()
        fits.append({"category": c["slug"], "nodeId": c["nodeId"], "scale": s, "frameOffset": off, "scaleFrom": how,
                     "fitScale": fs, "fitOffset": [fox, foy], "medianCentreResidualPx": res[len(res) // 2], "p95CentreResidualPx": res[int(len(res) * .95)],
                     "pairedInExport": len(paired), "owned": len(own), "alsoInOtherCategory": len(paired) - len(own)})
        missing += [{**m, "category": c["slug"]} for m in miss if m.get("set") and any(ms["nodeId"] == m["set"] and ms["owner"] == c["nodeId"] for ms in msets)]
        by_set = collections.OrderedDict()
        for p in own:
            by_set.setdefault(p["set"]["nodeId"], []).append(p)
        sec_of = lambda n: mparent[n].get("name")
        for ms in msets:
            if ms["owner"] != c["nodeId"]: continue
            vs = []
            for p in by_set.get(ms["nodeId"], []):
                m = p["meta"]; size, style, props = C.parse_variant_name(m["name"])
                assert size in C.SIZES and m["w"] == C.SIZES[size] == m["h"], (m, size)
                implicit = style is None
                if implicit: style = "Filled" if sec_of(ms["node"]) == "Filled Only" else "Outline"
                X, Y, Wd = s * (m["x"] + off), s * (m["y"] + off), s * m["w"]
                can = canonical(ex, p["el"], X, Y, Wd)
                worst = max((abs(float(t)) for e in p["el"].iter() for t in G.TOK.findall(e.get("d", "")) if not t.isalpha()), default=0)
                vs.append({"nodeId": m["nodeId"], "name": m["name"], "size": size, "style": style.lower(), "implicit": implicit,
                           "box": [X, Y, Wd, Wd], "el": p["el"], "can": can, "qpx": can[2] * m["w"]})
            sets.append({"cat": c, "name": ms["name"], "nodeId": ms["nodeId"], "variants": vs,
                         "metaVariants": len(ms["variants"]), "section": sec_of(ms["node"]), "ex": c["nodeId"], "s": s})
        keep_ex[c["nodeId"]] = ex
        print(f"{c['slug']:<20} sets {sum(1 for x in msets if x['owner'] == c['nodeId']):>4} variants {len(own):>5}  s={s:.6f} off={off:g} ({how})", flush=True)

    total_meta = sum(s_["metaVariants"] for s_ in sets)
    total_paired = sum(len(s_["variants"]) for s_ in sets)
    assert len(sets) == 5128 and total_meta == 35890, (len(sets), total_meta)
    assert total_paired + len(missing) == total_meta

    # ---------------------------------------------------------------- slugs (global namespace; first occurrence keeps the plain slug)
    used, slug_rule = set(), collections.Counter()
    for st in sets:
        base = C.slugify(st["name"])
        cand = base; rule = "plain"
        if cand in used: cand, rule = f"{base}--{st['cat']['slug']}", "category"
        if cand in used: cand, rule = f"{base}--{st['nodeId'].replace(':', '-')}", "nodeId"
        assert cand not in used
        used.add(cand); st["slug"] = cand; slug_rule[rule] += 1

    # ---------------------------------------------------------------- duplicate category frame
    dup_of = {}
    cat_by_id = {c["nodeId"]: c for c in cats}
    for c in cats:
        if "duplicateOf" not in c: continue
        a = [s_ for s_ in sets if s_["cat"]["nodeId"] == c["duplicateOf"]]
        b = [s_ for s_ in sets if s_["cat"]["nodeId"] == c["nodeId"]]
        assert len(a) == len(b)
        for x, y in zip(a, b):
            same = x["name"] == y["name"] and len(x["variants"]) == len(y["variants"]) and all(
                vx["size"] == vy["size"] and vx["style"] == vy["style"] and equivalent(vx["can"], vy["can"], 0.0)[0]
                for vx, vy in zip(x["variants"], y["variants"]))
            if same: dup_of[y["nodeId"]] = x
            exact = same and all(vx["can"][:2] == vy["can"][:2] for vx, vy in zip(x["variants"], y["variants"]))
            c["byteExactSets"] = c.get("byteExactSets", 0) + exact
        c["verifiedDuplicateSets"] = sum(1 for y in b if y["nodeId"] in dup_of)

    # ---------------------------------------------------------------- scale equivalence per set × style
    assets, eq_stats = [], collections.Counter()
    strict_stats = collections.Counter()
    max_diff_hist = collections.Counter()
    for st in sets:
        st["styles"] = collections.OrderedDict()
        for v in st["variants"]:
            st["styles"].setdefault(v["style"], {})[v["size"]] = v
        for style, bysize in st["styles"].items():
            ref = next(z for z in REF_ORDER if z in bysize)
            info = {"set": st, "style": style, "ref": ref, "sizes": bysize, "differs": [], "diff": {}}
            for z, v in bysize.items():
                if z == ref: continue
                ok, d = equivalent(bysize[ref]["can"], v["can"])
                strict = rounded_key(bysize[ref]["can"]) == rounded_key(v["can"])
                strict_stats["rounded-equal" if strict else "rounded-different"] += 1
                info["diff"][z] = d
                if d is not None: max_diff_hist["<=1e-3" if d <= 1e-3 else "<=2e-3" if d <= 2e-3 else "<=1e-2" if d <= 1e-2 else ">1e-2"] += 1
                else: max_diff_hist["structure differs"] += 1
                if not ok: info["differs"].append(z)
            info["equivalent"] = not info["differs"]
            eq_stats["equivalent" if info["equivalent"] else "not-equivalent"] += 1
            info["implicit"] = any(v["implicit"] for v in bysize.values())
            assets.append(info)

    # ---------------------------------------------------------------- write normalised files
    planned, problems, file_of = {}, [], {}
    multitone, with_defs = [], []
    for a in assets:
        st = a["set"]; c = st["cat"]; ex = keep_ex[st["ex"]]
        base = f"{C.BRANDS_ROOT}/svg/{a['style']}" if c["restricted"] else f"src/icons/svg/{a['style']}"
        if st["nodeId"] in dup_of:
            orig = dup_of[st["nodeId"]]
            src = next(x for x in assets if x["set"] is orig and x["style"] == a["style"])
            a["file"] = src["file"]; a["perSize"] = src["perSize"]; a["duplicateOfSet"] = orig["nodeId"]; a["written"] = False
            continue
        a["written"] = True
        a["file"] = f"{base}/{st['slug']}.svg"; a["perSize"] = {}
        jobs = [(a["ref"], a["file"])] + [(z, f"{base}/{st['slug']}--{z.lower()}.svg") for z in a["differs"]]
        for z, path in jobs:
            v = a["sizes"][z]; X, Y, Wd, _ = v["box"]
            data, has_defs = normalised_svg(ex, v["el"], X, Y, st["s"], C.SIZES[z], f"{st['slug']}-{a['style']}-{z.lower()}")
            assert path not in planned, path
            planned[path] = data
            if z != a["ref"]: a["perSize"][z] = path
            probs = L.svg_problems(data)
            if probs: problems.append({"file": path, "problems": probs, "set": st["name"], "style": a["style"], "size": z})
            if L.is_multitone(data): multitone.append(path)
            if has_defs: with_defs.append(path)
    # write (deterministic, only when different), refuse stale files
    for path, data in planned.items():
        full = os.path.join(C.ROOT, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        if not os.path.exists(full) or open(full, "rb").read() != data:
            with open(full, "wb") as f: f.write(data)
    stale = []
    for d in ("src/icons/svg", f"{C.BRANDS_ROOT}/svg"):
        for dp, _, fs in os.walk(os.path.join(C.ROOT, d)):
            for fn in fs:
                rel = os.path.relpath(os.path.join(dp, fn), C.ROOT).replace(os.sep, "/")
                if rel not in planned: stale.append(rel)
    if stale:
        C.dump("stale-files.json", stale)
        sys.exit(f"{len(stale)} stale generated files listed in results/stale-files.json (review, delete, re-run)")

    # ---------------------------------------------------------------- cross-set duplicates (reference-size canonical geometry)
    buckets = collections.defaultdict(list)
    for a in assets:
        if not a["written"]: continue
        v = a["sizes"][a["ref"]]
        buckets[(v["can"][0], len(v["can"][1]))].append(a)          # same structure → pairwise tolerance check
    dup_groups = []
    for grp in buckets.values():
        if len(grp) < 2: continue
        clusters = []
        for a in grp:
            for cl in clusters:
                if equivalent(cl[0]["sizes"][cl[0]["ref"]]["can"], a["sizes"][a["ref"]]["can"])[0]: cl.append(a); break
            else: clusters.append([a])
        dup_groups += [cl for cl in clusters if len({x["set"]["nodeId"] for x in cl}) > 1]
    dup_assets = sum(len(g) - 1 for g in dup_groups)
    dup_cross_cat = sum(1 for g in dup_groups if len({x["set"]["cat"]["slug"] for x in g}) > 1)
    dup_cross_style = sum(1 for g in dup_groups if len({x["style"] for x in g}) > 1)

    # ---------------------------------------------------------------- catalogue
    rel_src = lambda p: p[len("src/icons/"):] if p.startswith("src/icons/") else "../../" + p
    catalogue = {"source": {"fileKey": C.FILE_KEY, "page": C.PAGE, "exportedOn": C.EXPORTED_ON, "licence": C.LICENCE_TEXT,
                            "note": "Brands are third-party marks: internal use only, rights not verified, files under restricted/ (outside src/)."},
                 "sizes": C.SIZES, "categories": []}
    by_cat = collections.OrderedDict((c["nodeId"], []) for c in cats)
    for a in assets: by_cat[a["set"]["cat"]["nodeId"]].append(a)
    for c in cats:
        ce = {"name": c["name"], "slug": c["slug"], "nodeId": c["nodeId"]}
        if "duplicateOf" in c: ce["duplicateOf"] = c["duplicateOf"]
        ce["restricted"] = c["restricted"]
        ce["original"] = rel_src(c["original"])
        ce["sets"] = []
        seen = collections.OrderedDict()
        for a in by_cat[c["nodeId"]]:
            st = a["set"]
            e = seen.get(st["nodeId"])
            if e is None:
                e = {"name": st["name"], "slug": st["slug"], "nodeId": st["nodeId"]}
                d = inv_sets.get(st["nodeId"], {}).get("description")
                if d: e["description"] = d
                if st["nodeId"] in dup_of: e["duplicateOf"] = dup_of[st["nodeId"]]["nodeId"]
                e["styles"] = {}
                seen[st["nodeId"]] = e; ce["sets"].append(e)
            se = {"file": rel_src(a["file"])}
            if a["implicit"]: se["implicit"] = True
            if a["perSize"]: se["perSize"] = {z: rel_src(p) for z, p in a["perSize"].items()}
            se["variants"] = {z: a["sizes"][z]["nodeId"] for z in C.SIZE_ORDER if z in a["sizes"]}
            e["styles"][a["style"]] = se
        catalogue["categories"].append(ce)
    with open(os.path.join(C.ROOT, "src/icons/catalogue.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(catalogue, f, ensure_ascii=False, separators=(",", ":")); f.write("\n")

    # ---------------------------------------------------------------- variant boxes (for the pixel test)
    boxes = {}
    for a in assets:
        st = a["set"]
        for z, v in a["sizes"].items():
            X, Y, Wd, _ = v["box"]
            boxes[v["nodeId"]] = {"original": st["cat"]["original"], "x": round(X, 6), "y": round(Y, 6), "w": round(Wd, 6), "h": round(Wd, 6),
                                  "normalized": rel_src(a["perSize"].get(z, a["file"])), "size": z, "style": a["style"]}
    with open(os.path.join(HERE, "variant-boxes.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(boxes, f, separators=(",", ":")); f.write("\n")

    # ---------------------------------------------------------------- manifests
    write_manifests(cats, assets, planned, multitone, problems)

    # ---------------------------------------------------------------- results for the report
    prec = collections.defaultdict(lambda: collections.Counter())
    for st in sets:
        for v in st["variants"]:
            q = v["qpx"]
            prec[st["cat"]["slug"]]["≤0.0005px" if q <= 0.0005 else "≤0.005px" if q <= 0.005 else "≤0.05px" if q <= 0.05 else ">0.05px"] += 1
            prec[st["cat"]["slug"]]["max"] = max(prec[st["cat"]["slug"]]["max"], q)
    results = {
        "sets": len(sets), "metaVariants": total_meta, "paired": total_paired, "missing": [{k: m[k] for k in ("nodeId", "name", "set", "category", "reason")} for m in missing],
        "fits": fits, "slugRules": slug_rule,
        "perCategory": {c["slug"]: {"sets": sum(1 for x in sets if x["cat"] is c), "variants": sum(len(x["variants"]) for x in sets if x["cat"] is c)} for c in cats},
        "duplicateFrame": {c["slug"]: {"of": c["duplicateOf"], "verifiedDuplicateSets": c.get("verifiedDuplicateSets"), "numericallyIdenticalSets": c.get("byteExactSets")} for c in cats if "duplicateOf" in c},
        "assetsSetStyle": len(assets), "assetsWritten": sum(1 for a in assets if a["written"]),
        "equivalence": dict(eq_stats), "equivalenceWritten": dict(collections.Counter("equivalent" if a["equivalent"] else "not-equivalent" for a in assets if a["written"])),
        "pairComparisons": dict(strict_stats), "maxDiffHistogram": dict(max_diff_hist),
        "notEquivalent": [{"set": a["set"]["name"], "nodeId": a["set"]["nodeId"], "category": a["set"]["cat"]["slug"], "style": a["style"], "ref": a["ref"],
                           "differs": a["differs"], "maxDiff": {z: a["diff"][z] for z in a["differs"]}} for a in assets if a["written"] and a["differs"]],
        "files": len(planned), "perSizeFiles": dict(collections.Counter(z for a in assets if a["written"] for z in a["perSize"])),
        "filesSrc": sum(1 for p in planned if p.startswith("src/")), "filesRestricted": sum(1 for p in planned if p.startswith("restricted/")),
        "uniqueAssetsNeeded": sum(1 + len(a["differs"]) for a in assets if a["written"]),
        "duplicates": {"groups": len(dup_groups), "redundantAssets": dup_assets, "groupsAcrossCategories": dup_cross_cat, "groupsAcrossStyles": dup_cross_style,
                       "largest": sorted(([x["set"]["name"] + " [" + x["style"] + "]" for x in g] for g in dup_groups), key=len, reverse=True)[:15]},
        "styles": dict(collections.Counter(a["style"] for a in assets)), "implicitAssets": dict(collections.Counter(a["style"] for a in assets if a["implicit"])),
        "validator": {"filesChecked": len(planned), "withProblems": problems, "multitone": multitone, "withDefs": with_defs},
        "precision": {k: dict(v) for k, v in prec.items()},
        "bytes": {"normalisedSrc": sum(len(d) for p, d in planned.items() if p.startswith("src/")),
                  "normalisedRestricted": sum(len(d) for p, d in planned.items() if p.startswith("restricted/")),
                  "largestNormalised": max(len(d) for d in planned.values())},
    }
    C.dump("split-results.json", results)
    print(json.dumps({k: results[k] for k in ("sets", "metaVariants", "paired", "assetsSetStyle", "assetsWritten", "equivalence", "uniqueAssetsNeeded", "files")}, ensure_ascii=False))
    print("duplicates", results["duplicates"]["groups"], results["duplicates"]["redundantAssets"], "problems", len(problems), "multitone", len(multitone), "defs", len(with_defs))


def write_manifests(cats, assets, planned, multitone, problems):
    exports = {e["nodeId"]: e for e in json.load(open(os.path.join(C.OUT_JSON, "exports.json"), encoding="utf-8"))}
    probs_by_file = {p["file"]: p["problems"] for p in problems}
    approval = {"approvedBy": "Project owner", "date": "2026-11-20", "reference": "Export approval for page 1801:5142, local internal use only"}
    base_decisions = json.load(open(os.path.join(C.ROOT, "src/icons/manifest.json"), encoding="utf-8"))["decisions"]
    decisions = {
        "D-12": base_decisions["D-12"], "D-13": base_decisions["D-13"],
        "D-14": {"notApplicable": True, "date": "2026-11-20",
                 "reference": "D-14 concerns only the external 'Design System' / 'UI Icons' libraries; the icon source is the in-file page 1801:5142 (D-12), see docs/implementation/r5-implementation-spec.md (D-14: 'no longer needed for the icons'). D-14 stays open for those libraries."},
        "D-15": {"approvedBy": "Project owner", "date": "2026-11-20",
                 "reference": "Iconly licence purchased by the project owner; internal use only, no redistribution; licence text not on file (to be filed)"},
        "exportApproval": approval}
    iconly = {"name": "Iconly (purchased licence, text not on file)", "url": "https://iconly.io", "redistribution": "internal-only",
              "attributionRequired": True, "attributionText": "Icons: Iconly (iconly.io), licensed to the project owner — internal use only",
              "evidence": "Project owner statement 2026-11-20; licence text not on file"}
    def entry(a, src_id):
        st = a["set"]
        f = lambda p: {"path": p, "sha256": C.sha(planned[p])}
        e = {"name": st["slug"], "category": st["cat"]["slug"], "style": a["style"],
             "sizes": [C.SIZES[z] for z in C.SIZE_ORDER if z in a["sizes"]], "source": src_id, "sourceName": st["name"],
             "figmaNodeId": st["nodeId"], "original": {"path": st["cat"]["original"], "sha256": exports[st["cat"]["nodeId"]]["sha256"]},
             "normalized": f(a["file"]), "licence": "inherit", "attribution": iconly["attributionText"],
             "variants": {z: a["sizes"][z]["nodeId"] for z in C.SIZE_ORDER if z in a["sizes"]}}
        if a["perSize"]: e["perSize"] = {z: f(p) for z, p in a["perSize"].items()}
        files = [a["file"]] + list(a["perSize"].values())
        if any(p in multitone for p in files): e["multicolor"] = True
        kp = sorted({c for p in files for c, _ in probs_by_file.get(p, [])})
        if kp: e["knownProblems"] = [{"code": c, "reason": "Figma artwork uses a clip-path (needs a <clipPath> def with an id); kept unaltered" if c == "V08" else "recorded, artwork not altered"} for c in kp]
        return e
    for restricted in (False, True):
        sel = [a for a in assets if a["written"] and a["set"]["cat"]["restricted"] == restricted]
        cats_sel = sorted({a["set"]["cat"]["slug"] for a in sel}, key=[c["slug"] for c in cats].index)
        src_id = "iconly-annachy-brands" if restricted else C.SOURCE_ID
        m = {"schemaVersion": "1.0.0", "status": "restricted" if restricted else "active",
             **({"root": C.BRANDS_ROOT} if restricted else {}),
             "decisions": decisions, "sizeScale": sorted(C.SIZES.values()), "styles": ["outline", "filled"], "categories": cats_sel,
             "sources": [{"id": src_id, "name": ("Annachy Icons page 1801:5142 — Brands category (third-party brand marks)" if restricted else "Annachy Icons page 1801:5142 (Iconly-derived)"),
                          "kind": "figma-file", "figmaFileKey": C.FILE_KEY, "owner": "Project owner",
                          "licence": ({**iconly, "name": "Iconly artwork of third-party brand marks (rights not verified)",
                                       "evidence": iconly["evidence"] + "; trademark rights of each brand NOT verified — do not publish or redistribute"} if restricted else iconly),
                          "approved": approval}],
             "originals": [{"path": e["original"], "sha256": e["sha256"], "figmaNodeId": e["nodeId"], "category": e["slug"],
                            **({"note": f"duplicate of frame {e['duplicateOf']}; its sets reuse that frame's normalised files"} if e.get("duplicateOf") else {})}
                           for e in exports.values() if e["restricted"] == restricted],
             "icons": [entry(a, src_id) for a in sel]}
        path = os.path.join(C.ROOT, C.BRANDS_ROOT if restricted else "src/icons", "manifest.json")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            json.dump(m, f, ensure_ascii=False, separators=(",", ":")); f.write("\n")


if __name__ == "__main__":
    main()
