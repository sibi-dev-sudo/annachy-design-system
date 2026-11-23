# Final Test Report

Date: 2026-11-20 · Machine: Windows 11, headless Chrome, project served over a local HTTP server (127.0.0.1) by the test harness.
All runs were sequential and in the foreground; no overlapping runs and no background test jobs.

## 1. Full regression (`python -I tests/tools/run_all.py`)

**Final clean run: 34 / 34 suites PASS (241 s); leftovers: 0 Chrome profiles, no bytecode cache, no mutation state.**

The run immediately before it was **not clean**: 33 / 34. The *R6 dropdown footer real input* suite failed 4 checks after
`net::ERR_NETWORK_CHANGED` interrupted the load of `src/components/input/input.css`; the operating system's network changed
during the run. The three Dark-style failures were consequences of the missing stylesheet. The suite then passed 3 / 3 times
on its own, and the full regression was repeated with the result below. No code or test was changed between the two runs.

| Suite | Result | Time | Detail |
|---|---|---|---|
| integrity baseline (static) | PASS | 3.2s | BASELINE: 457 original tokens · 5 token CSS · 6183 source files · failures: 0 |
| R1 tokens (static) | PASS | 0.1s | RESULT: PASS |
| R2 base (static) | PASS | 0.1s | R2 STATIC RESULT: PASS |
| component CSS, 8 components (static) | PASS | 0.2s | R3 STATIC RESULT: PASS |
| R3 closure (static) | PASS | 0.2s | R3 CLOSURE STATIC RESULT: PASS |
| R4 closure (static) | PASS | 6.5s | R4 CLOSURE STATIC: 106 checks · failures: 0 | R4 CLOSURE STATIC RESULT: PASS |
| R5 icon infrastructure (static) | PASS | 11.0s | R5 ICONS STATIC: 87 checks · failures: 0 | R5 ICONS STATIC RESULT: PASS |
| R7 icon assets (static) | PASS | 17.1s | R7 ICONS STATIC: 7292 checks · failures: 0 | R7 ICONS STATIC RESULT: PASS |
| R1 + R2 browser + showcase links | PASS | 5.0s | == r2-base-check.html: pass | STATUS: PASS | BROWSER RESULT: PASS |
| R3 browser button | PASS | 3.6s | STATUS: PASS | checks: 9964 · failures: 0 | BROWSER RESULT: PASS |
| R3 browser button-gradient | PASS | 3.5s | STATUS: PASS | checks: 1863 · failures: 0 | BROWSER RESULT: PASS |
| R3 browser input | PASS | 3.8s | STATUS: PASS | checks: 11952 · failures: 0 | BROWSER RESULT: PASS |
| R3 browser checkbox | PASS | 3.8s | STATUS: PASS | checks: 3108 · failures: 0 | BROWSER RESULT: PASS |
| R3 browser radio | PASS | 3.8s | STATUS: PASS | checks: 2423 · failures: 0 | BROWSER RESULT: PASS |
| R3 browser toggle | PASS | 3.7s | STATUS: PASS | checks: 4904 · failures: 0 | BROWSER RESULT: PASS |
| R4 browser dropdown | PASS | 3.7s | STATUS: PASS | checks: 469 · failures: 0 | BROWSER RESULT: PASS |
| R4 browser tooltip | PASS | 3.6s | STATUS: PASS | checks: 1441 · failures: 0 | BROWSER RESULT: PASS |
| R5 browser icon slots | PASS | 3.5s | == r5-icon-slot-check.html: pass | checks: 73 · failures: 0 | BROWSER RESULT: PASS |
| R6 browser dropdown dark + footer | PASS | 3.8s | STATUS: PASS | checks: 757 · failures: 0 | BROWSER RESULT: PASS |
| Screens: Sample Screen (5 frames) | PASS | 4.1s | STATUS: PASS | checks: 1441 · failures: 0 | BROWSER RESULT: PASS |
| Screens: PDP (3 frames) | PASS | 4.0s | STATUS: PASS | checks: 306 · failures: 0 | BROWSER RESULT: PASS |
| R3 real input + showcase | PASS | 9.4s | R3 CLOSURE CDP RESULT: PASS |
| R4 dropdown real input | PASS | 10.5s | R4-1 DROPDOWN CDP: 82 checks · failures: 0 | R4-1 DROPDOWN CDP RESULT: PASS |
| R4 dropdown lifecycle (AUD-1) | PASS | 4.3s | R4 DROPDOWN LIFECYCLE: 40 checks · failures: 0 | R4 DROPDOWN LIFECYCLE RESULT: PASS |
| R4 init safety | PASS | 3.7s | R4 INIT-SAFETY: 10 checks · failures: 0 | R4 INIT-SAFETY RESULT: PASS |
| R4 tooltip real input | PASS | 16.9s | R4-2 TOOLTIP CDP: 39 checks · failures: 0 | R4-2 TOOLTIP CDP RESULT: PASS |
| R4 dropdown showcase | PASS | 2.9s | DROPDOWN SHOWCASE: 20 checks · failures: 0 | DROPDOWN SHOWCASE RESULT: PASS |
| R4 tooltip showcase | PASS | 3.4s | TOOLTIP SHOWCASE: 13 checks · failures: 0 | TOOLTIP SHOWCASE RESULT: PASS |
| R6 dropdown footer real input | PASS | 3.3s | R6 DROPDOWN FOOTER: 38 checks · failures: 0 | R6 DROPDOWN FOOTER RESULT: PASS |
| showcase catalogue + iconography | PASS | 3.5s | SHOWCASE CATALOGUE: 16 checks · failures: 0 | SHOWCASE CATALOGUE RESULT: PASS |
| R7 icon catalogue real input | PASS | 23.9s | R7 ICON CATALOGUE: 20 checks · failures: 0 | R7 ICON CATALOGUE RESULT: PASS |
| Showcase crawl: every page, links, icons, Dark | PASS | 19.9s | SHOWCASE CRAWL: 110 checks · failures: 0 | SHOWCASE CRAWL RESULT: PASS |
| R7 icon fidelity vs Figma originals | PASS | 26.0s | R7 ICON FIDELITY RESULT: PASS | R7 ICON FIDELITY RESULT: PASS |
| Closure accessibility: every page (errors, names, alt, focus) | PASS | 25.3s | CLOSURE A11Y: 147 checks · failures: 0 | CLOSURE A11Y RESULT: PASS |

## 2. Mutation tests (`python -I tests/tools/mutate.py <id>`, one at a time, foreground)

**30 / 30 caught; every file restored byte-identical (SHA-256); no recovery journal left.**

| Mutant | Result | Restore |
|---|---|---|
| DD-PAD | CAUGHT | byte-identical |
| DD-V | CAUGHT | byte-identical |
| DD-FOCUS | CAUGHT | byte-identical |
| DD-RADIUS | CAUGHT | byte-identical |
| DD-TYPE | CAUGHT | byte-identical |
| DD-DIS | CAUGHT | byte-identical |
| DD-WRAP | CAUGHT | byte-identical |
| DD-SESC | CAUGHT | byte-identical |
| DD-LEAK | CAUGHT | byte-identical |
| DD-DESTROY | CAUGHT | byte-identical |
| DD-TIMER | CAUGHT | byte-identical |
| R6-DSEL | CAUGHT | byte-identical |
| R6-DARK | CAUGHT | byte-identical |
| R6-FTYPE | CAUGHT | byte-identical |
| R6-STAGE | CAUGHT | byte-identical |
| R6-REVERT | CAUGHT | byte-identical |
| TT-CX | CAUGHT | byte-identical |
| TT-MIRROR | CAUGHT | byte-identical |
| TT-H | CAUGHT | byte-identical |
| M4 | CAUGHT | byte-identical |
| M5 | CAUGHT | byte-identical |
| M6 | CAUGHT | byte-identical |
| M7 | CAUGHT | byte-identical |
| M8 | CAUGHT | byte-identical |
| R11-SRC | CAUGHT | byte-identical |
| R11-CROP | CAUGHT | byte-identical |
| R11-SCALE | CAUGHT | byte-identical |
| R11-OVL | CAUGHT | byte-identical |
| CL-ICON | CAUGHT | byte-identical |
| CL-FOCUS | CAUGHT | byte-identical |

## 3. Closure-specific checks

| Check | Result |
|---|---|
| Original images (`assets/images/`, 52 files) | Byte-identical to the R11 delivery (SHA-256 checked before and after the optimisation) |
| Web copies, A/B at real display sizes (1× and 2×; frame clipping lifted so off-frame carousel items are measured too) | 190 comparisons: 186 pass (123 raw tier, 63 blurred tier). The failures all involve `62f2c`, which therefore keeps its original. Worst raw mean 6.66/255, worst blurred 1.97/255 |
| R11 geometry lock with web copies | Identical (112 layers, 0.1 px) |
| Image requests per screen | All screens: 0 failed image requests (`closure-image-weight.json`); every page: 0 failed requests or console errors (accessibility suite and showcase crawl) |
| Icon artwork | 37 SVGs byte-identical to the Figma export (checked before staging was deleted); fixtures verify the declared file, that it loads, and its size |
| Library match search | 6,098 library icons; 1 exact match reused; the other candidates rejected with recorded reasons (`closure-icon-match.json`) |
| Accessibility (every one of the 25 pages) | 147 / 0: language and title, unique ids, alt on every image, accessible name on every control, visible focus on the first 12 Tab stops |
| Tokens, components, icons intact | Baseline: 457 original tokens (+7 approved = 464), 5 token CSS files, 6,183 `src/` files, 0 differences. No `src/` file changed in the closure |
| Staging / temporary exports | None left (`annachy-*-staging`, `annachy-mutation`: absent) |
| Figma | Read-only tools only; no `create_session`, no writes |

## 4. Test-suite corrections made in the closure (no coverage weakened)

- **Screen fixtures.** A web copy is accepted only at `assets/images-web/<id>.webp` and only when it is linked to its declared original through `data-img-original`. The geometry is still compared per original.
- **Accessibility focus check.** The first version tested a detached clone of the element, which cannot show the field wrapper's `:has(:focus-visible)` state or the D-21 border-width focus. It now compares the real focused and blurred states of the element and its 3 nearest ancestors. It still found, and the closure fixed, one genuine defect (the PDP V1 field).
- **R11-SRC and R11-SCALE mutants.** Their anchors were re-targeted to the web-copy references. The runner had refused to start R11-SCALE when its old anchor disappeared (0 matches), so no file was changed.
- **The R10 and R11 one-time fidelity tools are not part of the regression.** They need their export staging; results are recorded in their manifests.
