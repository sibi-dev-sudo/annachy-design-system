# tests/tools — validation tooling (AUD-3)

Python 3 standard library only, plus a local Google Chrome. No packages, no build step, no network beyond `127.0.0.1`.
**Run every command from the project root.** Use `python -I` (isolated mode). The tools set `sys.dont_write_bytecode`, so no `__pycache__` is left behind.

| Setting | Default | Override |
|---|---|---|
| Chrome | `C:\Program Files\Google\Chrome\Application\chrome.exe` | env `ANNACHY_CHROME` |
| Figma read-only transcript check | skipped | env `ANNACHY_FIGMA_LOG` = path to a Claude Code session `.jsonl` |

## Full regression (sequential)

```sh
python -I tests/tools/run_all.py            # all suites, one at a time, then a leftovers check
python -I tests/tools/run_all.py static     # only the static suites
```

The runner exits 1 if any suite fails, or if anything is left behind: temporary Chrome profiles, mutation state, or a bytecode cache.

## Suites

| Command | What it checks |
|---|---|
| `baseline.py` | 464 tokens (457 originals hash-identical + the 7 approved R3-0a tokens), token CSS byte-identical, every `src/` file equal to the validated baseline (catches leftover mutations and unreviewed edits) |
| `validate_r1.py` · `validate_r2.py` | R1 token mapping ↔ CSS ↔ `tokens.json`; R2 base layer |
| `validate_r3.py <component…>` | component CSS: token references resolve, private props, raw-colour allow-list, forced/native state pairing, layer import |
| `r3_closure_static.py` · `r4_closure_static.py` | closure audits: completeness, architecture, import order, duplicate selectors, namespaces, init guards, AUD-1 lifecycle, evidence traceability, documentation agreement, assets, leftover mutations |
| `r5_icons_static.py` | icon manifest (schema + policy, still blocked/empty), no artwork in `src/`, validator self-test (`tests/fixtures/r5-icons/`) |
| `browser_check.py [fixture…]` | loads `tests/fixtures/<fixture>` in headless Chrome and reads its `#result`; with no arguments, runs R1 + R2 and checks the showcase links |
| `r3_closure_cdp.py` | real keyboard, mouse and accessibility tree for R3, plus every showcase page |
| `r4_dropdown_cdp.py` · `r4_tooltip_cdp.py` | real keyboard, mouse and touch for Dropdown and Tooltip |
| `r4_dropdown_lifecycle_cdp.py` | AUD-1: listener counts across open/close/destroy, re-init, and garbage collection |
| `r4_init_safety_cdp.py` | repeated initialisation adds no duplicate handling |
| `r4_showcase_dropdown_cdp.py` · `r4_showcase_tooltip_cdp.py` | showcase pages over HTTP |

## Mutation testing (guarded)

```sh
python -I tests/tools/mutate.py --list      # catalogue (19 mutants)
python -I tests/tools/mutate.py DD-V        # one mutant: apply → run its suite → restore → verify
python -I tests/tools/mutate.py --all       # every mutant, strictly one after another
python -I tests/tools/mutate.py --recover   # restore after an interrupted run
```

How a run stays safe:
- **Before mutating.** The runner refuses to start if `src/` differs from `baseline.json` or a journal already exists. It copies the pristine file and writes a journal to `%TEMP%/annachy-mutation/`, a fixed path outside the repository and outside synced folders, flushed to disk before the source is touched.
- **The mutation itself.** One mutation is applied at a time. Each is marked `/*MUTANT*/`, and the static audit fails if a marker is ever found.
- **After every run.** The file is restored in `finally`, on SIGINT/SIGTERM and at exit. Its SHA-256 must equal the pristine hash, and then the journal and backup are deleted.
- **After a crash.** A hard kill (such as a power loss or `kill -9`) leaves the journal in place. The next run refuses to start until `--recover` restores the file; this was verified by killing a live run.

Rules:
- **Never run mutations in the background or in parallel with another test run.** A batch run once triggered a low-memory stop.

## Baseline maintenance

`baseline.json` is the validated state. After an approved source change, update it only once the full regression passes:

```sh
python -I tests/tools/run_all.py && python -I tests/tools/baseline.py --write-sources
```

`--write-sources` never rewrites the token sections, so the 457 original tokens stay pinned to the pre-R3 values.

## Fixture generation

`gen_r5_fixtures.py` rewrites `tests/fixtures/r5-icons/` only. Those files are synthetic geometric probes, not icon artwork.

## R11 product imagery

| Tool | Purpose |
|---|---|
| `r11_jsx.py` | Reads Figma design-context JSX: local components, simple variant conditionals and resized-instance scaling. Converts Figma's Tailwind classes to inline CSS, including `calc()` spacing; unknown classes raise |
| `r11_integrate_images.py` | Copies the staged originals (named by actual format) to `showcase/screens/assets/images/`, refusing to overwrite, and fills the 108 placeholders. It is idempotent; `--refill` rebuilds after a converter fix, and `--dry-run` is available. It needs `%TEMP%/annachy-image-staging` |
| `r11_image_fidelity_once.py` | One-time check (needs staging): byte identity against staging, identity of every raster with an original upload, and a visual comparison with Figma's own node renders. Pixels under overlays are masked, and reviewed exceptions are listed in the tool |
| `r11_image_geometry.py` | Records (`--write`) or compares the rendered image-layer boxes in `tests/fixtures/r11-image-geometry.json`. Write it only after a passing fidelity check |

## Closure tools

| Tool | Purpose |
|---|---|
| `closure_optimize_images.py` | WebP web copies of the R11 rasters (2×–4× display size, aspect kept, never enlarged). Never overwrites |
| `closure_web_images_ab.py` | A/B check of the copies against the originals at real display sizes (1× and 2×); `--apply` switches only the images whose every placeholder passes |
| `closure_image_weight.py` | Image bytes per screen before and after, plus a measured load |
| `closure_icon_match.py` | One-time: library exact-match search for the staged icon artwork (needs staging) |
| `closure_integrate_icons.py` | One-time: places the closure icons and logotype (needs staging; idempotent; refuses to overwrite) |
| `closure_a11y_cdp.py` | Regression suite: console and network errors, accessible names, alt, focus visibility, ids, language and title on every showcase page |
