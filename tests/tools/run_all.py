"""Full regression, strictly sequential (one suite at a time, foreground). Run from the project root:
    python -I tests/tools/run_all.py            # everything
    python -I tests/tools/run_all.py static     # only suites whose name contains "static"
    python -I tests/tools/run_all.py --skip fidelity   # everything except suites whose name contains "fidelity" (memory-heavy)
Exits 1 if any suite fails. Verifies afterwards that nothing was left behind (temporary Chrome profiles,
mutation state, bytecode caches) and that src/ still matches the validated baseline.
"""
import glob, os, subprocess, sys, tempfile, time
sys.stdout.reconfigure(encoding="utf-8")
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
PY = [sys.executable, "-I"]
t = lambda *a: PY + [os.path.join(HERE, a[0])] + list(a[1:])
R3 = ["button", "button-gradient", "input", "checkbox", "radio", "toggle", "dropdown", "tooltip"]
SUITES = [
    ("integrity baseline (static)", t("baseline.py")),
    ("R1 tokens (static)", t("validate_r1.py")),
    ("R2 base (static)", t("validate_r2.py")),
    ("component CSS, 8 components (static)", t("validate_r3.py", *R3)),
    ("R3 closure (static)", t("r3_closure_static.py")),
    ("R4 closure (static)", t("r4_closure_static.py")),
    ("R5 icon infrastructure (static)", t("r5_icons_static.py")),
    ("R7 icon assets (static)", t("r7_icons_static.py")),
    ("R1 + R2 browser + showcase links", t("browser_check.py")),
    *[(f"R3 browser {f}", t("browser_check.py", f"r3-{f}-check.html")) for f in ("button", "button-gradient", "input", "checkbox", "radio", "toggle")],
    ("R4 browser dropdown", t("browser_check.py", "r4-dropdown-check.html")),
    ("R4 browser tooltip", t("browser_check.py", "r4-tooltip-check.html")),
    ("R5 browser icon slots", t("browser_check.py", "r5-icon-slot-check.html")),
    ("R6 browser dropdown dark + footer", t("browser_check.py", "r6-dropdown-check.html")),
    ("Screens: Sample Screen (5 frames)", t("browser_check.py", "screens-sample-check.html")),
    ("Screens: PDP (3 frames)", t("browser_check.py", "screens-pdp-check.html")),
    ("R3 real input + showcase", t("r3_closure_cdp.py")),
    ("R4 dropdown real input", t("r4_dropdown_cdp.py")),
    ("R4 dropdown lifecycle (AUD-1)", t("r4_dropdown_lifecycle_cdp.py")),
    ("R4 init safety", t("r4_init_safety_cdp.py")),
    ("R4 tooltip real input", t("r4_tooltip_cdp.py")),
    ("R4 dropdown showcase", t("r4_showcase_dropdown_cdp.py")),
    ("R4 tooltip showcase", t("r4_showcase_tooltip_cdp.py")),
    ("R6 dropdown footer real input", t("r6_dropdown_footer_cdp.py")),
    ("showcase catalogue + iconography", t("showcase_catalogue_cdp.py")),
    ("R7 icon catalogue real input", t("r7_icon_catalogue_cdp.py")),
    ("Showcase crawl: every page, links, icons, Dark", t("showcase_crawl_cdp.py")),
    ("R7 icon fidelity vs Figma originals", t("r7_icon_fidelity_cdp.py")),
    ("Closure accessibility: every page (errors, names, alt, focus)", t("closure_a11y_cdp.py")),
    ("Checkout prototype (brief): rules, edge cases, both directions", t("checkout_proto_cdp.py")),
]


def profiles():
    tmp = tempfile.gettempdir()
    return set(glob.glob(os.path.join(tmp, "annachy-cdp-*")) + glob.glob(os.path.join(tmp, "annachy-chrome-*")))


def summary(out):
    keep = [l.strip() for l in out.splitlines() if ("checks" in l and "failures" in l) or "RESULT" in l or l.startswith("== ") or "STATUS" in l]
    return " | ".join(keep[-3:]) if keep else (out.strip().splitlines() or ["(no output)"])[-1]


if __name__ == "__main__":
    args = sys.argv[1:]
    skip = args[args.index("--skip") + 1] if "--skip" in args else None
    if skip: args = [a for a in args if a not in ("--skip", skip)]
    flt = args[0] if args else ""
    before = profiles()
    failed = []
    t0 = time.time()
    for name, cmd in SUITES:
        if flt and flt not in name: continue
        if skip and skip in name: print(f"SKIP  {name}  (--skip {skip})"); continue
        s = time.time()
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", timeout=600)
            out, code = r.stdout + r.stderr, r.returncode
        except subprocess.TimeoutExpired:
            out, code = "TIMEOUT", 1
        print(f"{'PASS' if code == 0 else 'FAIL'}  {name:<40} {time.time() - s:5.1f}s  {summary(out)}")
        if code != 0:
            failed.append(name)
            print("      " + "\n      ".join([l for l in out.splitlines() if "FAIL" in l][:8]))
    left = profiles() - before
    pyc = glob.glob(os.path.join(HERE, "__pycache__"))
    mut = os.path.exists(os.path.join(tempfile.gettempdir(), "annachy-mutation"))
    print(f"leftovers: {len(left)} Chrome profiles · bytecode cache {'present' if pyc else 'none'} · mutation state {'PRESENT' if mut else 'none'}")
    if left or pyc or mut: failed.append("leftovers")
    print(f"REGRESSION: {len(failed)} failing of {sum(1 for n, _ in SUITES if (not flt or flt in n) and not (skip and skip in n))} suites in {time.time() - t0:.0f}s"
          + (f" — {failed}" if failed else "") + "\nREGRESSION RESULT: " + ("PASS" if not failed else "FAIL"))
    sys.exit(1 if failed else 0)
