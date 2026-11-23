# 06 — Final Regression Report

Date 2026-11-20. Command: `python -I tests/tools/run_all.py` (strictly sequential), with the Figma transcript check enabled.
**Result: 29 / 29 suites PASS in 110 s; 0 leftovers** (Chrome profiles, bytecode caches, mutation state).

| Suite | Checks | Failures |
|---|---:|---:|
| Integrity baseline: 457 original tokens hash-identical, 5 token CSS files, 45 `src/` files | — | 0 |
| R1 tokens static (464) · R2 base static · component CSS static (8 components) | PASS | 0 |
| R3 closure static | 136 | 0 |
| R4 closure static (architecture, AUD-1 lifecycle, traceability incl. R6 evidence, Figma read-only) | 107 | 0 |
| R5 icon infrastructure static | 53 | 0 |
| R1 + R2 browser (464 tokens computed, 0 mismatched) + showcase links | PASS | 0 |
| R3 browser: Button 9,964 · Gradient 1,863 · Input 11,952 · Checkbox 3,108 · Radio 2,423 · Toggle 4,904 | 34,214 | 0 |
| R4 browser: Dropdown Light 469 · Tooltip 1,441 | 1,910 | 0 |
| **R6 browser: Dropdown Dark + Footer** (60 variants; menu sizes = Figma META) | **757** | 0 |
| R5 icon-slot contract | 73 | 0 |
| **Screens: Sample Screen (5 frames)** | **1,363** | 0 |
| **Screens: PDP (3 frames)** | **303** | 0 |
| R3 real input + every component showcase page | 232 | 0 |
| R4 Dropdown real input · lifecycle · init safety | 82 · 40 · 10 | 0 |
| R4 Tooltip real input | 39 | 0 |
| **R6 Dropdown footer real input** (staged commit, keyboard / mouse / touch, Dark, lifecycle) | **38** | 0 |
| Showcase: Dropdown (all 48 menus vs META, live staged commit) · Tooltip · **catalogue + Iconography** | 20 · 13 · **14** | 0 |
| **Mutation** (`mutate.py --all`, one at a time, each restored byte-identical) | **24 / 24 caught** | — |

Figma usage across the whole session, from the transcript: read-only tools only. `create_session`, `get_screenshot`, `download_assets` and all write tools: **0**. Subagent calls are reported separately (screens: 57 read-only calls, doc 03).

## Changes to existing tests in this phase (all justified by approved changes, none weakened)

| Test | Change | Reason |
|---|---|---|
| `validate_r1.py` | "dark.css must not exist (V1)" replaced by a strict rule: one `[data-annachy-theme="dark"]` block that only re-maps names existing in `light.css` to hex values | Dark mode where Figma defines it (mission §4) |
| `validate_r2.py`, `r3_closure_static.py`, `r1-token-check.html`, `r2-base-check.html` | Accept `dark.css` only directly after `light.css` in `annachy.tokens` | Same |
| `r4_closure_static.py` | 7 token imports; 8 dropdown element listeners (+2 footer); R6 evidence in the traceability corpus | Footer |
| `r4_showcase_dropdown_cdp.py` | 11 interactive / 40 items / 48 menus (was 8 / 20 / 8); new staged-commit check | Dark + Footer added to the showcase |

## R7-1 icons — regression after the approved icon export (2026-11-20)

Command: `python -I tests/tools/run_all.py --skip fidelity` (sequential). **28 of 31 suites passed in the run. The other 3 (static) failed on rules that pre-dated the approved export; they were updated and re-run individually: PASS.** 0 leftovers from that run.

| New or changed suite | Result |
|---|---|
| `r7_icons_static.py`: catalogue ↔ files ↔ manifest, 35,890 variants accounted, slug uniqueness, `svg_problems` on 6,890 assets, originals SHA-256, no asset URLs, Brands only under `restricted/` | **7,292 / 0** |
| `r7_icon_catalogue_cdp.py`: counts, search (name / set / variant node), category / style / size filters, paging, Brands toggle, rendered sizes, `currentColor`, **all 6,890 files served** | **20 / 0** |
| Screens with icons: Sample Screen · PDP (exact icons must fill their Figma box; all other placeholders empty) | 1,363 / 0 · 303 / 0 |
| Showcase catalogue + Iconography (mapped slots render, unmapped stay empty, manifest active) | 15 / 0 |
| R3 / R4 closure static: `download_assets` allowed **only** on page `1801:5142` nodes; no write / session / screenshot tool | PASS |
| R5 icon infrastructure static | 87 / 0 |
| Integrity baseline (now 6,183 `src/` files) | 0 failures |
| All R1–R6 suites | unchanged, PASS |

**Not completed: pixel fidelity.**
- `r7_icon_fidelity_cdp.py` compares vector crops of the original exports with the library assets, over 1,751 sampled variants.
- The run was **stopped by the system for low memory**. Per the project rule it was not retried, so fidelity is **unverified**.
- An earlier raster-based attempt matched within tolerance on 1,722 of 1,751 variants. The 29 deviations were small (≤ 1.5 % of pixels) and concentrated in frames Figma scaled down at export. One variant (`1802:215892`) showed an empty crop. That method was then found to blur the scaled originals, so it was replaced with the vector comparison.
- Re-run on request, when memory allows: `python -I tests/tools/r7_icon_fidelity_cdp.py`.

**Mutation tests** were not re-run: the changed source is icon data and `src/icons/icons.js`, and the 24 mutants target Dropdown / Tooltip, which are unchanged.

## Final clean run (2026-11-20, R8)

**33 / 33 suites PASS** (`run_all.py`, sequential, 543 s, 0 leftovers) · **24 / 24 mutants caught** (`mutate.py --all`). The new suites are:
- the showcase crawl (25 pages, 110 checks);
- icon fidelity (7,105 variants: 7,100 match; 5 Figma defects FIG-ICON-1 reported).

An earlier attempt overlapped two regression runs by mistake. Its failures (a leftover-profile flag and one crawl timing) were caused by the overlap. It was discarded, and this run was made alone. Details are in doc 08.
