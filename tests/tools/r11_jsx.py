"""R11-0: minimal reader for Figma design-context JSX (local component functions, simple variant conditionals) and a
Tailwind -> inline-CSS converter limited to the classes Figma emits for image wrappers. Unknown classes raise."""
import re

TAG = re.compile(r"<(/?)([A-Za-z][\w.]*)((?:\s+[\w-]+(?:=(?:\"[^\"]*\"|\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}))?)*)\s*(/?)>", re.S)
ATTR = re.compile(r"([\w-]+)(?:=(\"[^\"]*\"|\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}))?")


class Node:
    def __init__(self, tag, attrs, parent):
        self.tag, self.attrs, self.parent, self.children = tag, attrs, parent, []

    @property
    def id(self): return self.attrs.get("data-node-id")

    @property
    def classes(self): return self.attrs.get("className", "").split()

    def walk(self):
        yield self
        for c in self.children: yield from c.walk()


def parse(code):
    consts = dict(re.findall(r"const (\w+) = `\$\{assetPathPrefix\}/([\w.]+)`;", code))
    body = code[code.index("return ("):]
    root = Node("#root", {}, None); cur = root
    for m in TAG.finditer(body):
        close, tag, attrs, selfclose = m.group(1), m.group(2), m.group(3), m.group(4)
        if close:
            cur = cur.parent; continue
        a = {}
        for k, v in ATTR.findall(attrs):
            if v.startswith('"'): a[k] = v[1:-1]
            elif v.startswith("{"):
                inner = v[1:-1].strip()
                a[k] = ("ASSET", consts[inner]) if inner in consts else ("EXPR", inner)
            else: a[k] = True
        n = Node(tag, a, cur); cur.children.append(n)
        if not selfclose: cur = n
    return root, consts


def length(v):
    v = v.replace("_", " ")
    if v.startswith("calc("):   # Tailwind spaces binary + / - inside calc(); Figma's class text omits them (invalid CSS otherwise)
        return re.sub(r"(?<=[\d%a-z)])([+-])(?=[\d.(])", r" \1 ", v)
    if re.fullmatch(r"-?[\d.]+(px|%)", v): return v
    raise ValueError("length " + v)


FRAC = {"1/2": "50%", "0": "0", "px": "1px", "full": "100%"}


def tw(classes):
    css, tx = [], []
    for c in classes:
        neg = c.startswith("-"); k = c[1:] if neg else c
        m = re.fullmatch(r"(left|top|right|bottom|h|w|size|inset|max-w|rounded|border|bg)-(?:\[(.+)\]|(1/2|0|px|full|none|white|solid))", k)
        if k in ("absolute", "relative"): css.append(f"position:{k}")
        elif k == "block": css.append("display:block")
        elif k == "contents": css.append("display:contents")
        elif k in ("overflow-hidden",): css.append("overflow:hidden")
        elif k == "overflow-clip": css.append("overflow:clip")
        elif k == "object-cover": css.append("object-fit:cover")
        elif k == "pointer-events-none": css.append("pointer-events:none")
        elif k == "max-w-none": css.append("max-width:none")
        elif k == "size-full": css += ["width:100%", "height:100%"]
        elif k == "inset-0": css.append("inset:0")
        elif k == "bg-white": css.append("background:#fff")
        elif k == "border-solid": css.append("border-style:solid")
        elif k == "border": css.append("border-width:1px")
        elif k in ("translate-x-1/2", "translate-y-1/2") and neg: tx.append(("x" if "x" in k else "y"))
        elif k in ("shrink-0", "content-stretch", "flex", "flex-col", "items-start", "items-center", "items-end",
                   "justify-center", "justify-end", "justify-start"): css.append({"flex": "display:flex", "flex-col": "flex-direction:column", "items-start": "align-items:flex-start",
                   "items-center": "align-items:center", "items-end": "align-items:flex-end", "justify-center": "justify-content:center",
                   "justify-end": "justify-content:flex-end", "justify-start": "justify-content:flex-start", "shrink-0": "flex-shrink:0"}.get(k, "") or "")
        elif m:
            p, val = m.group(1), m.group(2) or m.group(3)
            if p in ("left", "top", "right", "bottom", "h", "w", "size"):
                L = FRAC.get(val) if val in FRAC else length(val)
                if neg: L = f"calc(-1 * {L})" if not L.startswith("-") else L[1:]
                if p == "h": css.append(f"height:{L}")
                elif p == "w": css.append(f"width:{L}")
                elif p == "size": css += [f"width:{L}", f"height:{L}"]
                else: css.append(f"{p}:{L}")
            elif p == "inset": css.append("inset:" + " ".join(length(x) for x in val.split("_")))
            elif p == "rounded": css.append(f"border-radius:{length(val)}")
            elif p == "border" and val.startswith("#"): css.append(f"border-color:{val}")
            elif p == "border" and val.endswith("px"): css.append(f"border-width:{val}")
            elif p == "bg" and val.startswith("#"): css.append(f"background:{val}")
            else: raise ValueError("class " + c)
        elif re.fullmatch(r"rotate-\[[-\d.]+deg\]|-?rotate-\d+", k) or k.startswith("rotate-"):
            ang = re.search(r"[-\d.]+", k).group(0); ang = ("-" if neg else "") + ang
            tx.append(("r", ang))
        elif k.startswith("opacity-"):
            css.append(f"opacity:{int(k.split('-')[1]) / 100:g}")
        else: raise ValueError("unknown class " + c)
    css = [x for x in css if x]
    t = []
    if "x" in tx and "y" in tx: t.append("translate(-50%,-50%)")
    elif "x" in tx: t.append("translateX(-50%)")
    elif "y" in tx: t.append("translateY(-50%)")
    for r in [x for x in tx if isinstance(x, tuple)]: t.append(f"rotate({r[1]}deg)")
    if t: css.append("transform:" + " ".join(t))
    return ";".join(css)


def match_paren(s, i):
    """s[i] == '(' -> index of matching ')'"""
    d = 0
    for j in range(i, len(s)):
        if s[j] == "(": d += 1
        elif s[j] == ")":
            d -= 1
            if d == 0: return j
    raise ValueError("unbalanced")


def evaluate(expr, env):
    expr = expr.strip()
    # ternary chain:  a ? b : c   (right-assoc, no nested parens in practice)
    m = re.match(r"^([\w.]+)\s*\?\s*(\"[^\"]*\"|[\w]+)\s*:\s*(.+)$", expr, re.S)
    if m:
        return evaluate(m.group(2), env) if evaluate(m.group(1), env) else evaluate(m.group(3), env)
    m = re.match(r"^([\w.]+)\s*\|\|\s*(.+)$", expr, re.S)
    if m:
        return evaluate(m.group(1), env) or evaluate(m.group(2), env)
    if expr.startswith('"'): return expr[1:-1]
    if expr.startswith("`"):
        return re.sub(r"\$\{([^}]*)\}", lambda mm: str(evaluate(mm.group(1), env) or ""), expr[1:-1])
    if expr in ("undefined", "null"): return None
    if expr == "true": return True
    if expr in env: return env[expr]
    raise ValueError("cannot evaluate " + expr)


def functions(code):
    out = {}
    for m in re.finditer(r"^(?:export default )?function (\w+)\(([^)]*)\)[^{]*\{", code, re.M):
        name, params = m.group(1), m.group(2)
        start = m.end(); r = code.index("return", start)
        pre = code[start:r]
        if code[r + 6:].lstrip().startswith("("):
            p0 = code.index("(", r); p1 = match_paren(code, p0); body = code[p0 + 1:p1]
        else:
            body = code[r + 6:code.index(";", r)]
        defaults = dict(re.findall(r"(\w+)\s*=\s*\"([^\"]*)\"", params))
        out[name] = (defaults, pre, body)
    return out


def instantiate(fn, props, F, consts):
    defaults, pre, body = F[fn]
    env = dict(consts); env.update({k: v for k, v in defaults.items()}); env["className"] = None
    env.update(props)
    for v, val in re.findall(r"const (\w+) = property1 === \"([^\"]+)\";", pre): env[v] = env.get("property1") == val
    for v, lst in re.findall(r"const (\w+) = \[([^\]]*)\]\.includes\(property1\);", pre):
        env[v] = env.get("property1") in re.findall(r"\"([^\"]+)\"", lst)
    # {cond && ( ... )}
    while True:
        m = re.search(r"\{(\w+) && \(", body)
        if not m: break
        p0 = body.index("(", m.start()); p1 = match_paren(body, p0)
        close = body.index("}", p1)
        body = body[:m.start()] + (body[p0 + 1:p1] if env[m.group(1)] else "") + body[close + 1:]
    root = parse_body(body, env, F, consts)
    # Resized instance: Figma's code keeps the master's px geometry for the children, but Figma lays them out with
    # scale constraints. Record master size and scale on the root so the converter can lay out at master size and scale.
    md = re.search(r'className=\{className \|\| "([^"]*)"\}', body)
    if md and props.get("className") and root.children:
        size = lambda c: (re.search(r"(?:^| )w-\[([\d.]+)px\]", c), re.search(r"(?:^| )h-\[([\d.]+)px\]", c))
        (dw, dh), (iw, ih) = size(md.group(1)), size(props["className"])
        if dw and dh and iw and ih:
            dw, dh, iw, ih = (float(x.group(1)) for x in (dw, dh, iw, ih))
            if abs(dw - iw) > 0.01 or abs(dh - ih) > 0.01:
                root.children[0].attrs["_scale"] = (iw / dw, ih / dh, dw, dh)
    return root


TAG = TAG; ATTR = ATTR


def parse_body(body, env, F, consts):
    root = Node("#frag", {}, None); cur = root
    for m in TAG.finditer(body):
        close, tag, attrs, selfclose = m.group(1), m.group(2), m.group(3), m.group(4)
        if close:
            cur = cur.parent; continue
        a = {}
        for k, v in ATTR.findall(attrs):
            if v.startswith('"'): a[k] = v[1:-1]
            elif v.startswith("{"):
                inner = v[1:-1].strip()
                if inner.startswith("{"): a[k] = ("STYLE", inner); continue
                try: a[k] = evaluate(inner, env)
                except ValueError: a[k] = ("EXPR", inner)
            else: a[k] = True
        if tag[0].isupper() and tag in F:
            props = {k: v for k, v in a.items() if isinstance(v, str)}
            sub = instantiate(tag, props, F, consts)
            for ch in sub.children:
                ch.parent = cur; cur.children.append(ch); ch.attrs.setdefault("_component", tag)
            if not selfclose: raise ValueError("component with children")
            continue
        n = Node(tag, a, cur); cur.children.append(n)
        if not selfclose: cur = n
    return root


def load(path):
    code = open(path, encoding="utf-8").read()
    consts = {k: ("ASSET", v) for k, v in re.findall(r"const (\w+) = `\$\{assetPathPrefix\}/([\w.]+)`;", code)}
    F = functions(code)
    main = [n for n in F if re.search(r"export default function " + n + r"\b", code)][0]
    return instantiate(main, {}, F, consts)
