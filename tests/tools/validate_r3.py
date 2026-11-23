"""Static validation for R3 component CSS. Run from project root: python -I validate_r3.py <component> [...]
Checks: token references resolve; only private --_ props defined; literal colours limited to the documented
raw-Figma allow-list; no @media/@font-face/@import/url(); every forced state class has its native counterpart;
entry imports the component in annachy.components."""
import json, re, sys
sys.stdout.reconfigure(encoding="utf-8")
tokens = {t["css"] for t in json.load(open("src/tokens/tokens.json", encoding="utf-8"))["tokens"]}
RENDER = "--annachy-base-font-family-render"
# raw Figma values that are not variables (documented flags) — per component
RAW_COLOURS = {
    "button": {"#dcdfe5"},          # BTN-2 Secondary Grey Hover border (887:1024)
    "input": {"#3a6ff7"},           # IN2 Outline Focused border raw (1066:38544)
    "dropdown": {"#3a6ff7"},        # DD-1 search field focus, derived from Input Outline Focused (IN2 raw)
}
# raw rgba() literals (Figma raw paints/shadows, not variables) — per component, documented flags
RAW_RGBA = {
    "button-gradient": {  # B9 raw shadows (1153:3621/3631/3651), GB-4 raw Hover fill (1153:3631)
        "rgba(0, 79, 235, 0.12)", "rgba(0, 79, 235, 0.4)", "rgba(23, 25, 28, 0)", "rgba(23, 25, 28, 0.02)", "rgba(23, 25, 28, 0.08)",
        "rgba(23, 25, 28, 0.13)", "rgba(23, 70, 162, 0.85)", "rgba(50, 92, 179, 0.01)", "rgba(50, 92, 179, 0.05)", "rgba(50, 92, 179, 0.16)",
        "rgba(50, 92, 179, 0.27)", "rgba(50, 92, 179, 0.31)", "rgba(58, 111, 247, 0.92)"},
}
NATIVE = {"is-hover": ":hover", "is-focus": ":focus-visible", "is-pressed": ":active"}
fail = []
entry = open("src/annachy.css", encoding="utf-8").read()
for comp in sys.argv[1:]:
    path = f"src/components/{comp}/{comp}.css"
    raw = open(path, encoding="utf-8").read()
    src = re.sub(r"/\*.*?\*/", "", raw, flags=re.S)
    refs = set(re.findall(r"var\((--[\w-]+)", src))
    unknown = sorted(r for r in refs if not r.startswith("--_") and r not in tokens and r != RENDER)
    defined = set(re.findall(r"(?<![\w-])(--[\w-]+)\s*:", src))
    public = sorted(d for d in defined if not d.startswith(f"--_{comp}") and not d.startswith("--_"))
    undefined_private = sorted(r for r in refs if r.startswith("--_") and r not in defined)
    colours = set(m.lower() for m in re.findall(r"#[0-9a-fA-F]{3,8}\b", src))
    bad_colours = sorted(colours - RAW_COLOURS.get(comp, set()))
    rgba_lits = set(re.findall(r"rgba?\([^)]*\)", src))
    bad_colours += sorted(rgba_lits - RAW_RGBA.get(comp, set()))
    forbidden = [k for k, p in [("@media", r"@media"), ("@font-face", r"@font-face"), ("@import", r"@import"), ("url(", r"url\(")] if re.search(p, src)]
    # forced-state pairing: every selector list containing .is-X must also contain the native pseudo-class
    unpaired = []
    for sel in re.findall(r"([^{}]+)\{", src):
        for cls, pseudo in NATIVE.items():
            # aria-activedescendant widgets (dropdown options) mark the active option with .is-active instead of :focus-visible
            if f".{cls}" in sel and pseudo not in sel and not (cls == "is-focus" and ".is-active" in sel):
                unpaired.append(sel.strip()[:90])
    imported = f'@import url("components/{comp}/{comp}.css") layer(annachy.components);' in entry
    print(f"[{comp}] var refs {len(refs)} · unknown {unknown} · private defined {len(defined)} · public props {public}")
    print(f"[{comp}] literal colours {sorted(colours)} · not allow-listed {bad_colours} · forbidden {forbidden}")
    print(f"[{comp}] undefined private refs {undefined_private} · unpaired forced states {len(unpaired)} · imported {imported}")
    for cond, msg in [(unknown, "unknown token refs"), (public, "public custom properties defined"), (bad_colours, "unlisted literal colours"),
                      (forbidden, "forbidden constructs"), (undefined_private, "undefined private props"), (unpaired, "forced state without native"),
                      (not imported, "not imported in annachy.components")]:
        if cond: fail.append(f"{comp}: {msg}: {cond if cond is not True else ''}")
print("\nR3 STATIC RESULT:", "PASS" if not fail else "FAIL")
for f in fail: print(" -", f)
sys.exit(1 if fail else 0)
