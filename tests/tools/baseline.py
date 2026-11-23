"""Integrity baseline for the validated library (read-only check by default).

    python -I tests/tools/baseline.py                 # verify (exit 1 on any difference)
    python -I tests/tools/baseline.py --write-sources # record current src/ hashes (ONLY after a full green regression)

baseline.json holds:
  tokens_original  SHA-256 of each of the 457 original tokens (canonical JSON), recorded from the pre-R3 backup
  tokens_added     the 7 approved R3-0a token names
  token_css        SHA-256 of the token CSS files that must stay byte-identical
  sources          SHA-256 of every validated file under src/ (detects leftover mutations / unreviewed edits)
The token sections are never rewritten by --write-sources. Run from the project root.
"""
import glob, hashlib, json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
BASELINE = os.path.join(HERE, "baseline.json")
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
canon = lambda t: hashlib.sha256(json.dumps(t, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()
UNCHANGED_TOKEN_CSS = ["src/tokens/primitives.css", "src/tokens/typography.css", "src/tokens/effects.css", "src/tokens/compat.css", "src/tokens/themes/light.css"]


def source_files():
    return sorted(f.replace("\\", "/") for f in glob.glob("src/**/*", recursive=True) if os.path.isfile(f))


def check(verbose=True):
    """Return a list of failure strings (empty = intact)."""
    b = json.load(open(BASELINE, encoding="utf-8"))
    fails = []
    tokens = {t["css"]: t for t in json.load(open("src/tokens/tokens.json", encoding="utf-8"))["tokens"]}
    if len(tokens) != 464: fails.append(f"token count {len(tokens)} != 464")
    changed = [k for k, h in b["tokens_original"].items() if k not in tokens or canon(tokens[k]) != h]
    if changed: fails.append(f"original tokens changed: {changed[:5]}")
    extra = sorted(set(tokens) - set(b["tokens_original"]))
    if extra != sorted(b["tokens_added"]): fails.append(f"added tokens differ from the 7 approved: {extra}")
    for f, h in b["token_css"].items():
        if sha(f) != h: fails.append(f"{f} not byte-identical")
    now = source_files()
    for f, h in b["sources"].items():
        if not os.path.exists(f): fails.append(f"missing {f}")
        elif sha(f) != h: fails.append(f"{f} differs from the validated baseline")
    for f in now:
        if f not in b["sources"]: fails.append(f"unbaselined file {f}")
    if verbose:
        print(f"BASELINE: {len(b['tokens_original'])} original tokens · {len(b['token_css'])} token CSS · {len(b['sources'])} source files · failures: {len(fails)}")
        for x in fails: print("  FAIL", x)
    return fails


def write_sources():
    b = json.load(open(BASELINE, encoding="utf-8")) if os.path.exists(BASELINE) else {}
    if "tokens_original" not in b:                     # one-time bootstrap from the pre-R3 token backup
        bk = os.path.join(os.environ["TEMP"], "tokens_backup_r3_0a")
        old = {t["css"]: t for t in json.load(open(os.path.join(bk, "tokens.json"), encoding="utf-8"))["tokens"]}
        new = {t["css"]: t for t in json.load(open("src/tokens/tokens.json", encoding="utf-8"))["tokens"]}
        assert len(old) == 457 and all(old[k] == new[k] for k in old), "current tokens do not match the 457 originals"
        b["tokens_original"] = {k: canon(v) for k, v in sorted(old.items())}
        b["tokens_added"] = sorted(set(new) - set(old))
        assert len(b["tokens_added"]) == 7
        b["token_css"] = {}
        for f in UNCHANGED_TOKEN_CSS:
            assert sha(f) == sha(os.path.join(bk, f[len("src/tokens/"):])), f
            b["token_css"][f] = sha(f)
    b["sources"] = {f: sha(f) for f in source_files()}
    with open(BASELINE, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(b, fh, indent=1, sort_keys=True); fh.write("\n")
    print(f"baseline written: {len(b['sources'])} source files")


if __name__ == "__main__":
    if "--write-sources" in sys.argv: write_sources()
    else: sys.exit(1 if check() else 0)
