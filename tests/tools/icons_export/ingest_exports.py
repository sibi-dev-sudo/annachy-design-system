"""Copy each staged Figma export byte-for-byte to its original path and record size + SHA-256 (exports.json).
    python -I tests/tools/icons_export/ingest_exports.py
Never edits an export. Refuses to overwrite an existing original with different bytes.
"""
import os, re, shutil, sys
sys.dont_write_bytecode = True; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C

cats, _ = C.categories()
out = []
for c in cats:
    data = open(c["staging"], "rb").read()
    head = data[:400].decode("utf-8", "replace")
    w, h = (float(x) for x in re.search(r'<svg width="([\d.]+)" height="([\d.]+)"', head).groups())
    dst = os.path.join(C.ROOT, c["original"])
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if os.path.exists(dst) and open(dst, "rb").read() != data: sys.exit(f"refusing to overwrite different original {c['original']}")
    if not os.path.exists(dst): shutil.copyfile(c["staging"], dst)
    assert open(dst, "rb").read() == data
    out.append({"category": c["name"], "slug": c["slug"], "nodeId": c["nodeId"], "tool": "download_assets", "format": "svg",
                "exportedOn": C.EXPORTED_ON, "original": c["original"], "bytes": len(data), "sha256": C.sha(data),
                "svgWidth": w, "svgHeight": h, "clampedTo4096": max(w, h) == 4096, "restricted": c["restricted"],
                **({"duplicateOf": c["duplicateOf"]} if "duplicateOf" in c else {})})
    print(f"{c['slug']:<22} {len(data):>10} B  {w:>6g}x{h:<6g} {C.sha(data)[:16]}")
C.dump("exports.json", out)
print(f"{len(out)} exports, {sum(e['bytes'] for e in out):,} bytes")
