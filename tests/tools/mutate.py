"""Guarded mutation testing. One mutation at a time, always in the foreground, always restored.

    python -I tests/tools/mutate.py --list             # catalogue
    python -I tests/tools/mutate.py DD-V               # apply one mutant, run its suite, restore, verify
    python -I tests/tools/mutate.py --all              # every mutant, strictly one after another
    python -I tests/tools/mutate.py --recover          # restore after an interrupted run (power loss, kill -9 ...)

Safety protocol (per mutant):
  1. Refuse to start if a recovery journal exists, or if src/ differs from tests/tools/baseline.json.
  2. Copy the pristine file to %TEMP%/annachy-mutation/backup/ and write journal.json there (fsynced) BEFORE mutating.
  3. Apply exactly one textual replacement (the anchor must occur exactly once), marked so leftovers are detectable.
  4. Run the target suite in the foreground (timeout 280 s). The mutant is "caught" when the suite fails.
  5. finally / SIGINT / SIGTERM / atexit: restore from the backup, verify SHA-256 equals the pristine hash,
     then delete the backup and the journal. A failed verification exits 2 and keeps the backup for --recover.
Never run this in the background or in parallel with another test run. Run from the project root.
"""
import atexit, hashlib, json, os, shutil, signal, subprocess, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True; sys.path.insert(0, HERE)
import baseline

import tempfile
# Kept outside the repository (which may sit in a synced folder that locks new directories) at a FIXED path so an
# interrupted run can always be found and recovered.
STATE_DIR = os.path.join(tempfile.gettempdir(), "annachy-mutation")
JOURNAL = os.path.join(STATE_DIR, "journal.json")
BACKUP_DIR = os.path.join(STATE_DIR, "backup")
PY = [sys.executable, "-I"]
T = lambda *a: PY + [os.path.join(HERE, a[0])] + list(a[1:])
DD_VIS, DD_CDP, DD_LIFE = T("browser_check.py", "r4-dropdown-check.html"), T("r4_dropdown_cdp.py"), T("r4_dropdown_lifecycle_cdp.py")
R6_VIS, R6_CDP = T("browser_check.py", "r6-dropdown-check.html"), T("r6_dropdown_footer_cdp.py")
TT_VIS, TT_CDP = T("browser_check.py", "r4-tooltip-check.html"), T("r4_tooltip_cdp.py")
SCR_PDP, SCR_SAMPLE = T("browser_check.py", "screens-pdp-check.html"), T("browser_check.py", "screens-sample-check.html")
DCSS, DJS = "src/components/dropdown/dropdown.css", "src/components/dropdown/dropdown.js"
TCSS, TJS = "src/components/tooltip/tooltip.css", "src/components/tooltip/tooltip.js"
# id: (file, anchor, replacement, suite, description)
MUTANTS = {
    "DD-PAD":    (DCSS, "--_dd-min-h: 48px; --_dd-py: 12px;", "--_dd-min-h: 48px; --_dd-py: 10px;", DD_VIS, "Dropdown Mobile item padding 12 → 10"),
    "DD-V":      (DCSS, "--_dd-fill: var(--annachy-color-blue-50);", "--_dd-fill: var(--annachy-color-background-tertiary);", DD_VIS, "Dropdown Selected fill"),
    "DD-FOCUS":  (DCSS, "--_dd-focus: inset 0 0 0 2px", "--_dd-focus: inset 0 0 0 1px", DD_VIS, "Dropdown focus stroke 2 → 1"),
    "DD-RADIUS": (DCSS, "border-radius: var(--annachy-radius-12);", "border-radius: var(--annachy-radius-8);", DD_VIS, "Dropdown Menu radius 12 → 8"),
    "DD-TYPE":   (DJS, "const TYPEAHEAD_MS = 500;", "const TYPEAHEAD_MS = 2000;", DD_CDP, "typeahead buffer 500 → 2,000 ms"),
    "DD-DIS":    (DJS, "if (!opt || isDisabled(opt)) return;", "if (!opt) return;", DD_CDP, "disabled-option guard removed"),
    "DD-WRAP":   (DJS, ": Math.min(opts.length - 1, Math.max(0, i + delta));", ": (i + delta + opts.length) % opts.length;", DD_CDP, "wrap at the list end"),
    "DD-SESC":   (DJS, "if (this.search.value) { this.search.value = ''; this.filter(true); }", "if (this.search.value) { this.search.value = ''; this.filter(true); this.close(false); }", DD_CDP, "search Escape closes instead of clearing"),
    "DD-LEAK":   (DJS, "    this.openScope?.abort();\n", "", DD_LIFE, "AUD-1: document listener not removed on close"),
    "DD-DESTROY": (DJS, "    this.lifetime.abort();\n", "", DD_LIFE, "AUD-1: destroy() keeps element listeners"),
    "DD-TIMER":  (DJS, "    clearTimeout(this.announceTimer);\n    this.typed = '';", "    this.typed = '';", DD_LIFE, "AUD-1: destroy() keeps the announcement timer"),
    "R6-DSEL":   (DCSS, "--_dd-fill: var(--annachy-color-blue-500); --_dd-label: var(--annachy-color-base-white);", "--_dd-fill: var(--annachy-color-blue-500); --_dd-label: var(--annachy-color-blue-50);", R6_VIS, "Dark Selected label Base/White -> Blue/50"),
    "R6-DARK":   ("src/tokens/themes/dark.css", "--annachy-color-background-tertiary: #1f242e;", "--annachy-color-background-tertiary: #edeff2;", R6_VIS, "Dark Hover fill reverts to Light"),
    "R6-FTYPE":  (DCSS, "--_button-font-size: var(--annachy-type-label-small-font-size);", "--_button-font-size: var(--annachy-type-h7-font-size);", R6_VIS, "Desktop footer label 14 -> 16 (D4 override lost)"),
    "R6-STAGE":  (DJS, "      if (!this.footer) this.emit();", "      this.emit();", R6_CDP, "footer: change fired on every toggle (not staged)"),
    "R6-REVERT": (DJS, "    if (this.footer && this.committed) this.restore(this.committed);", "", R6_CDP, "footer: Escape keeps staged changes"),
    "TT-CX":     (TCSS, ".annachy-tooltip--desktop.annachy-tooltip--light { --_tt-cx: -0.5px; }", ".annachy-tooltip--desktop.annachy-tooltip--light { --_tt-cx: 0px; }", TT_VIS, "Desktop light centring −0.5 → 0"),
    "TT-MIRROR": (TCSS, "inset-block-start: 9px; transform: rotate(-90deg) scaleY(-1); }", "inset-block-start: 9px; transform: rotate(-90deg); }", TT_VIS, "Right-arrow mirror removed"),
    "TT-H":      (TCSS, "inline-size: 260px; block-size: 62px; }", "inline-size: 260px; block-size: 60px; }", TT_VIS, "Mobile heading height 62 → 60"),
    "M4":        (TCSS, "  font-weight: var(--annachy-type-body-xs-font-weight);", "  font-weight: var(--annachy-type-body-xs-semibold-font-weight);", TT_VIS, "Desktop text weight 500 → 600"),
    "M5":        (TJS, "const SHOW_DELAY = 500;", "const SHOW_DELAY = 100;", TT_CDP, "show delay 500 → 100 ms"),
    "M6":        (TJS, "const HIDE_DELAY = 150;", "const HIDE_DELAY = 0;", TT_CDP, "hide delay 150 → 0 ms"),
    "M7":        (TJS, "if (e.key === 'Escape' && current)", "if (e.key === 'EscapeX' && current)", TT_CDP, "Escape dismissal disabled"),
    "M8":        (TJS, "const ARROW_TIP_GAP = 12;", "const ARROW_TIP_GAP = 0;", TT_CDP, "arrow tip gap 12 → 0"),
    # R11 product imagery (screen files; suites = screen fixtures)
    "R11-SRC":   ("showcase/screens/pdp/desktop-bg-colours.html", 'src="../assets/images-web/f8cdd.webp"', 'src="../assets/images-web/26d80.webp"', SCR_PDP, "R11: placeholder shows another image (web copy of a different original) than declared"),
    "R11-CROP":  ("showcase/screens/pdp/pdp-v1.html", 'left:calc(50% + 0.5px);top:calc(50% + 0.5px);width:394px', 'left:calc(50% + 0.5px);top:calc(50% + 4.5px);width:394px', SCR_PDP, "R11: hero crop offset +4 px"),
    "R11-SCALE": ("showcase/screens/pdp/pdp-v1.html", 'transform:scale(0.573570,0.573567);transform-origin:0 0"><span class="scr-img__box" style="position:absolute;inset:0;overflow:clip"><span class="scr-img__box" style="position:absolute;height:181.333px;left:50%;top:calc(50% + 0.16px);width:136.159px;transform:translate(-50%,-50%)"><span class="scr-img__box" style="position:absolute;inset:0;pointer-events:none"><span class="scr-img__box" style="position:absolute;inset:0;overflow:hidden"><img class="scr-img__art" src="../assets/images-web/9b5e5.webp" data-img-original="9b5e5.png" alt="" style="position:absolute;height:99.99%;left:-0.07%;max-width:none;top:0.01%;width:100.15%"></span><img class="scr-img__art" src="../assets/images-web/8b1ad.webp"', 'transform:scale(1,1);transform-origin:0 0"><span class="scr-img__box" style="position:absolute;inset:0;overflow:clip"><span class="scr-img__box" style="position:absolute;height:181.333px;left:50%;top:calc(50% + 0.16px);width:136.159px;transform:translate(-50%,-50%)"><span class="scr-img__box" style="position:absolute;inset:0;pointer-events:none"><span class="scr-img__box" style="position:absolute;inset:0;overflow:hidden"><img class="scr-img__art" src="../assets/images-web/9b5e5.webp" data-img-original="9b5e5.png" alt="" style="position:absolute;height:99.99%;left:-0.07%;max-width:none;top:0.01%;width:100.15%"></span><img class="scr-img__art" src="../assets/images-web/8b1ad.webp"', SCR_PDP, "R11: Green thumbnail loses Figma's instance scaling"),
    "R11-OVL":   ("showcase/screens/sample-screen/mobile-pdp-1608-7090.html", '<div class="scr-abs" style="width:178px; height:237px; left:-2px; top:-49px; pointer-events:none;">', '<div class="scr-abs" style="width:178px; height:237px; left:-2px; top:0; pointer-events:none;">', SCR_SAMPLE, "R11: review overlay back at the media box (pre-R11 error)"),
    # closure (screen icons, focus fix)
    "CL-ICON":   ("showcase/screens/sample-screen/desktop-pdp-1375-30858.html", 'src="../assets/vectors/icon-23ffe.svg"', 'src="../assets/vectors/icon-fecd1.svg"', SCR_SAMPLE, "closure: location icon shows another artwork than declared"),
    "CL-FOCUS":  ("showcase/screens/pdp/pdp.css", ".scr-p-delivery .annachy-input:not(:has(.annachy-input__control:focus-visible)) .annachy-input__field { border-color", ".scr-p-delivery .annachy-input .annachy-input__field { border-color", T("closure_a11y_cdp.py"), "closure: delivery field focus border overridden again"),
}
MARK = "/*MUTANT*/"
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
_active = {}


def recover(quiet=False):
    """Restore every file recorded in the journal; verify; remove the journal and backups."""
    if not os.path.exists(JOURNAL):
        if not quiet: print("recover: no journal - nothing to restore")
        return True
    j = json.load(open(JOURNAL, encoding="utf-8"))
    shutil.copyfile(j["backup"], j["path"])
    good = sha(j["path"]) == j["sha"]
    if not quiet or not good: print(f"recover: {j['path']} restored for {j['id']} — {'byte-identical' if good else 'HASH MISMATCH'}")
    if good:
        os.remove(JOURNAL); shutil.rmtree(STATE_DIR, ignore_errors=True)
    return good


def _restore_active(*_):
    if _active and os.path.exists(JOURNAL):
        ok = recover(quiet=True)
        _active.clear()
        if not ok: sys.exit(2)


def run_one(mid):
    path, old, new, suite, desc = MUTANTS[mid]
    if os.path.exists(JOURNAL): sys.exit("ABORT: a mutation journal exists - run --recover first")
    drift = baseline.check(verbose=False)
    if drift: sys.exit(f"ABORT: src/ is not pristine (differs from baseline): {drift[:3]}")
    src = open(path, "rb").read().decode("utf-8")
    nl = "\r\n" if "\r\n" in src else "\n"              # anchors are written with \n; match the file's line endings
    old, new = old.replace("\n", nl), new.replace("\n", nl)
    if src.count(old) != 1: sys.exit(f"ABORT: anchor for {mid} found {src.count(old)} times")
    os.makedirs(BACKUP_DIR, exist_ok=True)
    bak = os.path.join(BACKUP_DIR, os.path.basename(path))
    shutil.copyfile(path, bak)
    with open(JOURNAL, "w", encoding="utf-8") as fh:
        json.dump({"id": mid, "path": path, "backup": bak, "sha": sha(path)}, fh); fh.flush(); os.fsync(fh.fileno())
    _active[mid] = True
    caught, line = False, "no result line"
    try:
        # every mutant carries a /*MUTANT*/ marker so a leftover is detectable by the static audit
        mutated = src.replace(old, (new + MARK) if new else (MARK + nl), 1)
        with open(path, "wb") as fh: fh.write(mutated.encode("utf-8"))
        r = subprocess.run(suite, capture_output=True, text=True, encoding="utf-8", timeout=280)
        out = r.stdout + r.stderr
        line = next((l.strip() for l in out.splitlines() if "failures" in l and "checks" in l), out.strip().splitlines()[-1] if out.strip() else "no output")
        caught = r.returncode != 0
    except subprocess.TimeoutExpired:
        line, caught = "suite timed out (counted as caught)", True
    finally:
        restored = recover(quiet=True)
        _active.clear()
    print(f"{mid:<11} {'CAUGHT ' if caught else 'SURVIVED'} {desc} — {line}")
    print(f"{'':<11} restore: {'byte-identical' if restored else 'FAILED'}")
    if not restored: sys.exit(2)
    return caught


atexit.register(_restore_active)
for sig in (signal.SIGINT, signal.SIGTERM):
    signal.signal(sig, lambda *a: (_restore_active(), sys.exit(130)))

if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "--list"
    if arg == "--list":
        for k, v in MUTANTS.items(): print(f"{k:<11} {v[0]:<40} {v[4]}")
    elif arg == "--recover":
        sys.exit(0 if recover() else 2)
    elif arg == "--all":
        results = {m: run_one(m) for m in MUTANTS}
        survived = [m for m, c in results.items() if not c]
        print(f"MUTATION: {len(results) - len(survived)} / {len(results)} caught" + (f" · survived: {survived}" if survived else ""))
        sys.exit(1 if survived else 0)
    elif arg in MUTANTS:
        sys.exit(0 if run_one(arg) else 1)
    else:
        sys.exit(f"unknown mutant {arg}; use --list")
