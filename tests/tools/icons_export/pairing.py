"""Pair the SVG groups of every category export with the metadata variants (document order, names asserted) and fit
the export transform svg = s · frame + o (Figma clamps exports to 4096 px, so large frames are scaled)."""
import math, os, re, sys
import xml.etree.ElementTree as ET
sys.dont_write_bytecode = True; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C
import svggeom as G

SVGNS = "{http://www.w3.org/2000/svg}"


def is_hidden(n, parent, stop):
    while n is not None and n is not stop:
        if n.get("hidden") == "true": return True
        n = parent.get(n)
    return stop is not None and stop.get("hidden") == "true"


def meta_sets(frame, parent, cat_ids):
    """Sets (elements with symbol children) under an exported frame, document order, with absolute boxes."""
    out = []
    def walk(n, ox, oy, owner):
        for ch in n:
            x, y = ox + float(ch.get("x")), oy + float(ch.get("y"))
            own = ch.get("id") if ch.get("id") in cat_ids else owner
            syms = [s for s in ch if s.tag == "symbol"]
            if syms:
                out.append({"node": ch, "name": ch.get("name"), "nodeId": ch.get("id"), "owner": own,
                            "hidden": is_hidden(ch, parent, frame), "x": x, "y": y,
                            "variants": [{"nodeId": s.get("id"), "name": s.get("name"), "hidden": is_hidden(s, parent, frame),
                                          "x": x + float(s.get("x")), "y": y + float(s.get("y")),
                                          "w": float(s.get("width")), "h": float(s.get("height"))} for s in syms]})
            walk(ch, x, y, own)
    walk(frame, 0.0, 0.0, frame.get("id"))
    return out


class Export:
    def __init__(self, path):
        self.data = open(path, "rb").read()
        self.root = ET.fromstring(self.data)
        self.parent = {c: p for p in self.root.iter() for c in p}
        self.ids = {}
        for e in self.root.iter():
            if e.get("id") is not None: self.ids.setdefault(e.get("id"), e)
        self.groups = [e for e in self.root.iter() if e.get("id") is not None]
        self.pos = {id(e): i for i, e in enumerate(self.groups)}

    def ancestors(self, el):
        a, p = [], self.parent.get(el)
        while p is not None: a.append(p); p = self.parent.get(p)
        return a[::-1]                                   # root … parent

    def ctm_of_parent(self, el):
        m = G.IDENT
        for a in self.ancestors(el): m = G.mul(m, G.parse_transform(a.get("transform")))
        return m

    def refs(self, el):
        """Def elements referenced via url(#…) from el's subtree (recursively)."""
        seen, todo, out = set(), [el], []
        while todo:
            e = todo.pop()
            for x in e.iter():
                for v in x.attrib.values():
                    for r in re.findall(r"url\(#([^)]+)\)", v):
                        if r not in seen and r in self.ids:
                            seen.add(r); out.append(self.ids[r]); todo.append(self.ids[r])
        return out

    def geometry(self, el):
        """Structure + numbers (root coordinates) for the subtree of el and its referenced defs."""
        st, nums, q = [], [], 0.0
        def walk(e, m):
            nonlocal q
            m = G.mul(m, G.parse_transform(e.get("transform")))
            tag = G.local(e.tag)
            if tag in G.SHAPES:
                s, n, qq = G.element_geometry(e, m); st.extend(s); nums.extend(n); q = max(q, qq)
            else:
                st.append(tag + "".join(f"|{a}={e.get(a)}" if not (e.get(a) or "").startswith("url(") else f"|{a}=url"
                                        for a in G.STRUCT_ATTRS if e.get(a) is not None))
            for ch in e: walk(ch, m)
            st.append("/")
        base = self.ctm_of_parent(el)
        walk(el, base)
        for d in self.refs(el):
            st.append("def:" + G.local(d.tag)); walk(d, self.ctm_of_parent(el) if G.local(d.tag) in ("clipPath", "mask") else G.IDENT)
        return st, nums, q


def pair_export(cat, ex, frame, parent, cat_ids):
    """Returns (paired list, missing list, sets list)."""
    sets = meta_sets(frame, parent, cat_ids)
    ptr, paired, missing = 0, [], []
    groups = ex.groups
    for s in sets:
        if s["hidden"]:
            for v in s["variants"]: missing.append({**v, "set": s["nodeId"], "reason": "set hidden in Figma (not exported)"})
            continue
        j = ptr
        while j < len(groups) and not (C.strip_suffix(groups[j].get("id")) == s["name"] and G.local(groups[j].tag) == "g"):
            j += 1
        if j == len(groups):
            for v in s["variants"]: missing.append({**v, "set": s["nodeId"], "reason": "set group not found in export"})
            s["svg"] = None
            continue
        g = groups[j]; s["svg"] = g; ptr = j + 1
        kids = [k for k in g if k.get("id") is not None]
        vis = [v for v in s["variants"] if not v["hidden"]]
        for v in s["variants"]:
            if v["hidden"]: missing.append({**v, "set": s["nodeId"], "reason": "variant hidden in Figma (not exported)"})
        k = 0
        for v in vis:
            while k < len(kids) and C.strip_suffix(kids[k].get("id")) != v["name"]: k += 1
            if k == len(kids):
                missing.append({**v, "set": s["nodeId"], "reason": "variant group not found in export (empty or not rendered)"}); continue
            paired.append({"set": s, "meta": v, "el": kids[k]}); k += 1
        ptr = max(ptr, ex.pos[id(kids[-1])] + 1) if kids else ptr
    return paired, missing, sets


def fit(paired, ex, s_fixed=None):
    """Least-squares fit of geometry-bbox centres against metadata box centres → (s, ox, oy, rms, n)."""
    pts = []
    for p in paired:
        _, nums, _ = ex.geometry(p["el"])
        bb = G.bbox(nums)
        if bb is None: continue
        m = p["meta"]
        pts.append(((m["x"] + m["w"] / 2, m["y"] + m["h"] / 2), ((bb[0] + bb[2]) / 2, (bb[1] + bb[3]) / 2), m["w"]))
    def solve(P):
        n = len(P)
        if s_fixed is not None:
            s = s_fixed
        else:
            mx = sum(a[0][0] for a in P) / n; my = sum(a[0][1] for a in P) / n
            bx = sum(a[1][0] for a in P) / n; by = sum(a[1][1] for a in P) / n
            num = sum((a[0][0] - mx) * (a[1][0] - bx) + (a[0][1] - my) * (a[1][1] - by) for a in P)
            den = sum((a[0][0] - mx) ** 2 + (a[0][1] - my) ** 2 for a in P)
            s = num / den
        ox = sum(a[1][0] - s * a[0][0] for a in P) / n; oy = sum(a[1][1] - s * a[0][1] for a in P) / n
        res = [math.hypot(a[1][0] - (s * a[0][0] + ox), a[1][1] - (s * a[0][1] + oy)) / s for a in P]
        return s, ox, oy, res
    s, ox, oy, res = solve(pts)
    for _ in range(3):
        rms = math.sqrt(sum(r * r for r in res) / len(res))
        keep = [p for p, r in zip(pts, res) if r <= max(3 * rms, 0.5)]
        s, ox, oy, res = solve(keep)
    rms = math.sqrt(sum(r * r for r in res) / len(res))
    return s, ox, oy, rms, len(res), len(pts)
