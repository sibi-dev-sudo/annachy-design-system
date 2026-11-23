"""Minimal SVG geometry for the icon pipeline: transforms, path tokenising, canonical geometry, bounding boxes.
Read-only analysis — nothing here rewrites artwork."""
import math, re

NUM = r"[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?"
TOK = re.compile(r"[MmLlHhVvCcSsQqTtAaZz]|" + NUM)
ARGS = {"M": 2, "L": 2, "H": 1, "V": 1, "C": 6, "S": 4, "Q": 4, "T": 2, "A": 7, "Z": 0}
IDENT = (1.0, 0.0, 0.0, 1.0, 0.0, 0.0)
SHAPES = ("path", "rect", "circle", "ellipse", "line", "polygon", "polyline")
STRUCT_ATTRS = ("fill", "stroke", "fill-rule", "clip-rule", "stroke-linecap", "stroke-linejoin", "stroke-miterlimit",
                "opacity", "fill-opacity", "stroke-opacity", "stroke-dasharray", "mask", "clip-path", "filter", "style")


def local(tag): return tag.rsplit("}", 1)[-1]


def mul(m, n):
    a, b, c, d, e, f = m; A, B, C, D, E, F = n
    return (a * A + c * B, b * A + d * B, a * C + c * D, b * C + d * D, a * E + c * F + e, b * E + d * F + f)


def parse_transform(s):
    m = IDENT
    if not s: return m
    for name, args in re.findall(r"(\w+)\s*\(([^)]*)\)", s):
        v = [float(x) for x in re.findall(NUM, args)]
        if name == "matrix": t = tuple(v)
        elif name == "translate": t = (1, 0, 0, 1, v[0], v[1] if len(v) > 1 else 0)
        elif name == "scale": t = (v[0], 0, 0, v[1] if len(v) > 1 else v[0], 0, 0)
        elif name == "rotate":
            a = math.radians(v[0]); co, si = math.cos(a), math.sin(a)
            t = (co, si, -si, co, 0, 0)
            if len(v) == 3: t = mul(mul((1, 0, 0, 1, v[1], v[2]), t), (1, 0, 0, 1, -v[1], -v[2]))
        elif name == "skewX": t = (1, 0, math.tan(math.radians(v[0])), 1, 0, 0)
        elif name == "skewY": t = (1, math.tan(math.radians(v[0])), 0, 1, 0, 0)
        else: raise ValueError(name)
        m = mul(m, t)
    return m


def apply(m, x, y):
    a, b, c, d, e, f = m
    return a * x + c * y + e, b * x + d * y + f


def decimals(tok):
    """Printed precision of a number token (half-ulp)."""
    t = tok.lower().split("e")[0]
    return 0.5 * 10 ** -(len(t.split(".")[1]) if "." in t else 0)


def path_items(d):
    """Yield (CMD, kind-list, raw numbers, raw tokens) with absolute coordinates; kinds: P=point (x,y), L=length, R=raw."""
    toks = TOK.findall(d or "")
    i, cmd, cx, cy, sx, sy = 0, None, 0.0, 0.0, 0.0, 0.0
    out = []
    while i < len(toks):
        t = toks[i]
        if t.isalpha():
            cmd = t; i += 1
            if cmd in "Zz":
                out.append(("Z", [], [], [])); cx, cy = sx, sy
                continue
        n = ARGS[cmd.upper()]
        raw = toks[i:i + n]; i += n
        if len(raw) < n: break
        v = [float(x) for x in raw]
        rel = cmd.islower(); U = cmd.upper()
        pts = []
        if U == "H":
            x = v[0] + (cx if rel else 0); pts = [("P", (x, cy))]; cx = x
        elif U == "V":
            y = v[0] + (cy if rel else 0); pts = [("P", (cx, y))]; cy = y
        elif U == "A":
            x, y = v[5] + (cx if rel else 0), v[6] + (cy if rel else 0)
            pts = [("L", v[0]), ("L", v[1]), ("R", v[2]), ("R", v[3]), ("R", v[4]), ("P", (x, y))]; cx, cy = x, y
        else:
            for k in range(0, n, 2):
                pts.append(("P", (v[k] + (cx if rel else 0), v[k + 1] + (cy if rel else 0))))
            cx, cy = pts[-1][1]
        if U == "M":
            sx, sy = cx, cy
            cmd = "l" if rel else "L"          # implicit lineto after moveto
        out.append((U, pts, v, raw))
    return out


def element_geometry(el, ctm):
    """Return (structure-token list, numbers list as (kind, value)) in root coordinates, and max half-ulp of printed numbers."""
    tag = local(el.tag); g = lambda k, d=0.0: float(el.get(k, d) or d)
    st, nums, q = [tag], [], 0.0
    scale = math.sqrt(abs(ctm[0] * ctm[3] - ctm[1] * ctm[2]))
    for k in ("x", "y", "width", "height", "cx", "cy", "r", "rx", "ry", "x1", "y1", "x2", "y2", "d", "points", "stroke-width"):
        v = el.get(k)
        if v is not None:
            for t in TOK.findall(v):
                if not t.isalpha(): q = max(q, decimals(t))
    def P(x, y): nums.append(("P", apply(ctm, x, y)))
    def L(v): nums.append(("L", v * scale))
    if tag == "path":
        for U, pts, _, _ in path_items(el.get("d")):
            st.append(U)
            for kind, v in pts:
                if kind == "P": P(*v)
                elif kind == "L": L(v)
                else: nums.append(("R", v))
    elif tag == "rect":
        x, y, w, h = g("x"), g("y"), g("width"), g("height")
        P(x, y); P(x + w, y + h)
        if el.get("rx") is not None or el.get("ry") is not None: L(g("rx", el.get("ry") or 0)); L(g("ry", el.get("rx") or 0))
        if ctm[1] or ctm[2]: P(x + w, y); P(x, y + h)
    elif tag == "circle": P(g("cx"), g("cy")); L(g("r"))
    elif tag == "ellipse": P(g("cx"), g("cy")); L(g("rx")); L(g("ry"))
    elif tag == "line": P(g("x1"), g("y1")); P(g("x2"), g("y2"))
    elif tag in ("polygon", "polyline"):
        v = [float(t) for t in re.findall(NUM, el.get("points", ""))]
        for k in range(0, len(v) - 1, 2): P(v[k], v[k + 1])
    if el.get("stroke-width") is not None: L(float(el.get("stroke-width")))
    for a in STRUCT_ATTRS:
        if el.get(a) is not None: st.append(f"{a}={el.get(a).strip().lower()}" if not el.get(a).startswith("url(") else f"{a}=url")
    return st, nums, q * scale


def bbox(numbers):
    xs = [v[0] for k, v in numbers if k == "P"]; ys = [v[1] for k, v in numbers if k == "P"]
    return (min(xs), min(ys), max(xs), max(ys)) if xs else None
