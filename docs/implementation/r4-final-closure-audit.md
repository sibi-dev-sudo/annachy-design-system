# R4 Final Closure Audit

| Item | Value |
|---|---|
| Date | 2026-11-20 |
| Type | Audit only. **No component source was modified.** One documentation addition (evidence node index, AUD-2). |
| Overall status | **Update 2026-11-20: AUD-1 fixed and AUD-3 done (approved); see §10.** **R4 CLOSED — PASS.** All 108 approved variants are validated; the R1–R4 regression is clean. One non-blocking observation (AUD-1) is reported for decision; no source correction was made. |
| Figma | **Not accessed during the audit.** Whole-session operations, verified from the session transcript: `get_design_context` 147, `get_variable_defs` 128, `get_metadata` 98, `search_design_system` 3, `get_libraries` 1. These are all read-only tools. `download_assets`, `create_session`, `get_screenshot` and every write tool were never invoked. |

---

## 1. Component-by-component results

| Component | Approved variants | Files (css / js / html / README) | Visual | Real input | Showcase (HTTP) | Status |
|---|---:|---|---|---|---|---|
| Dropdown / Item (Light) | 20 | ✅ all four | 469 checks / 0 failures (with Menu) | 82 / 0 | 15 / 0 | ✅ PASS |
| Dropdown / Menu (Light, Footer=None) | 8 | (same) | menu heights = Figma META 188 / 261 / 220 / 293 | (same) | (same) | ✅ PASS |
| Tooltip | 80 (10 arrows × 2 devices × 2 modes × 2 formats) | ✅ all four | 1,441 / 0, each variant against its own Figma arrow geometry | 39 / 0 | 13 / 0 | ✅ PASS |

Behaviour verified with **real** keyboard, mouse and touch input through the Chrome DevTools Protocol:
- **Selection:** single selection commits and closes; multiple selection toggles and stays open.
- **Search:** filtering, the result announcement, and Escape clearing the text and then closing.
- **Keyboard:** typeahead (500 ms buffer, repeated-letter cycling); arrow keys, Home/End, Ctrl+Home/End; disabled options can become active but are not selectable.
- **Closing and focus:** Escape; outside click; Tab closing; focus restored to the trigger; the disabled trigger; flip above at the bottom edge.
- **Touch:** tap open and tap select.
- **Tooltip:** hover 500 ms / leave 150 ms / keyboard immediate; hoverable; warm-up; one at a time; Escape (and re-hover); blur; `aria-disabled` triggers; touch tap and tap outside; collision flips at the right and bottom edges.

Integration:
- `src/annachy.css` imports `dropdown.css` and `tooltip.css` last, in `annachy.components`.
- `src/annachy.js` exports exactly `initCheckboxes`, `initDropdowns` and `initTooltips`.
- Each showcase page loads over HTTP with no console or network errors.

## 2. Test summary (sequential final run, 2026-11-20)

| Suite | Checks | Failures |
|---|---:|---:|
| R1 static (mapping ↔ CSS ↔ tokens.json) | 464 tokens | 0 |
| R2 static | — | 0 |
| Component static (8 components: token refs, private props, raw-colour allow-list, state pairing, layer) | — | 0 |
| R3 closure static | 136 | 0 |
| **R4 closure static** (completeness, architecture, duplicate selectors, namespaces, init guards, evidence traceability, documentation agreement, tokens, assets, Figma tool log, leftover mutations) | **108** | 0 |
| R1 browser | 464 computed | 0 |
| R2 browser | — | 0 |
| R3 browser: Button 9,964 · Gradient 1,863 · Input 11,952 · Checkbox 3,108 · Radio 2,423 · Toggle 4,904 | 34,214 | 0 |
| R4 browser: Dropdown 469 · Tooltip 1,441 | 1,910 | 0 |
| R3 real-input + R3 showcase audit | 232 | 0 |
| R4 Dropdown real-input | 82 | 0 |
| R4 Tooltip real-input | 39 | 0 |
| **R4 init-safety** (repeated init: same controllers, one toggle per click, one change event, one show per hover) | **10** | 0 |
| R4 showcase HTTP (Dropdown 15 · Tooltip 13) | 28 | 0 |
| Showcase link check | 18 references | 0 broken |

**Mutation sensitivity (audit re-check):** both mutants were caught and restored byte-for-byte through the guarded runner:
- DD-V, Dropdown Selected fill: 4 failures.
- M7, Tooltip Escape disabled: 1 failure.

Together with R4 (16 / 16) that is **18 / 18 caught**.

## 3. Architecture results

| Check | Result |
|---|---|
| Vanilla HTML / CSS / ES modules only | ✅ no `require` / `module.exports`; no framework or build-tool references in `src/`; no `package.json`, lockfiles or `node_modules` |
| Cascade layers and import order | ✅ tokens (6) → base (4) → R3 (6) → R4 (2), each in its own layer; the layer statement is present |
| Duplicate or conflicting selectors | ✅ no duplicate selector blocks in any component file; every component's selectors stay in its own namespace |
| State precedence | ✅ `:where()`-equalised state selectors (Input, selection controls, Dropdown item) |
| JavaScript initialisation | ✅ `initDropdowns` / `initTooltips` / `initCheckboxes` are idempotent (WeakMap guards). Repeated calls return the same controllers, and real input shows no duplicate handling. Tooltip global listeners are registered once at module scope |
| R1–R3 unchanged | ✅ R3 sources byte-identical to their validated versions; every R1–R3 suite passes |

## 4. Design fidelity

| Area | Result |
|---|---|
| Dropdown Item (20) | Size 320 × 40 / 352 × 48; padding 12 / 10 and 12; gap 12; `Radius/8`; indicator 20 × 20 at x 12, centred; label at x 44; typography Label Small 14/20 (Desktop) / Body M 16/24 (Mobile); 5 state fills and labels; Multiple indicator colours; inset focus stroke + `Button/Focus` (stroke outside layout, §6) |
| Dropdown Menu (8) | Padding 8, gap 8, options gap 4, `Radius/12`, inset 1px `Border/Primary`, no shadow; exact heights; search field 48 / padding 14 / gap 6 / `Radius/8`; divider; placeholder colour and typography (D6) |
| Tooltip (80) | Padding 10, raw radius 4, max 300, colours per mode, typography per device/format, fixed heading sizes and text positions; **all 10 arrow positions** with every variant's own offset (−13 / 9 / 12, the 50% ± sub-pixel offsets) and transform matrix |
| Derived values (flagged, not silent) | DD-1 search focus border `#3a6ff7` (from the Input instance); TT-POS 12px trigger gap (from the arrow geometry) |
| Figma defects reproduced (not corrected) | D2 no menu shadow; D6 placeholder; TT1 invisible light tooltip; TT5 fixed heading size; TT3 raw radius; per-variant sub-pixel arrow offsets |

## 5. Accessibility results

| Area | Result |
|---|---|
| Roles | combobox (select-only and search), listbox (+ multiselectable), option, non-modal dialog, status (polite), tooltip; decorative slots `aria-hidden` |
| Names / descriptions | Trigger names via `aria-labelledby`; the search combobox is named "Search" (not the placeholder); tooltip as description via `aria-describedby`; icon-only triggers named by `aria-label` |
| States | expanded, `aria-activedescendant`, selected (explicit false), disabled options and triggers, busy (R3) |
| Focus | Keyboard focus stays on the trigger or search field; the active option shows the Figma Focus visual (8.04:1); focus is restored on close; a mouse click doesn't trigger the focus treatment |
| Live announcements | "N selected" / "N results" (debounced 500 ms), re-announced when identical, no animation-frame dependency |
| A40 | Light tooltip vs light page **1.00:1**: documented in `09-accessibility.md`, unchanged, reproduced |
| A41 | Dropdown Menu boundary **1.70:1** (border), 1.04:1 (fill): documented, unchanged, reproduced |

## 6. Integrity and documentation

| Check | Result |
|---|---|
| Tokens | 464; the 457 originals byte-identical (value and metadata); token CSS files byte-identical to the pre-R3 backup except the 7 approved `R3-0a` lines; no Radius 6/10 token |
| Figma | Read-only tools only (whole session); no writes |
| Assets | No image or font files in `src/`; no Figma asset URLs in `src/` or `showcase/` |
| Leftover mutations | All mutated files are byte-identical to their validated pre-mutation backups (Dropdown, Tooltip, Input, Checkbox, Radio, Toggle, Gradient); no mutation markers present |
| Evidence references | Every node ID cited in the R4 CSS resolves in the evidence documents (after AUD-2); README section references resolve |
| Documentation agreement | The counts 108 / 469 / 1,441 / 82 / 39 agree across the completion report, component READMEs, progress log and R4 spec; CHANGELOG `[0.5.0-r4]` and README status updated; A40 and A41 present |

## 7. Defects and observations

| ID | Finding | Severity | Action |
|---|---|---|---|
| **AUD-1** | `dropdown.js` adds one capturing `document` `pointerdown` listener per dropdown (outside-click) and has no teardown. A dropdown removed from the DOM keeps its listener and controller reachable. No functional failure: idempotency and real-input tests pass | Low (lifecycle / memory in long-lived SPAs) | **Not changed (audit-only).** Proposed fix for approval: a single shared delegated listener, or a `destroy()` API. Requires a new validation cycle |
| **AUD-2** | 11 element node IDs cited in `dropdown.css` / `tooltip.css` were not indexed in the evidence documents (all present in the recorded read-only outputs) | Documentation | **Fixed in documentation:** `r4-0-evidence.md` §7 node index. No source change |
| AUD-3 | Real-input drivers, the mutation runner and the validators are scratchpad authoring aids, not shipped (as in R1–R3). Fixtures are in the repo, but reproducing the real-input runs needs those drivers | Process | Proposal: add the drivers under `tests/tools/` if approved |

## 8. Known limitations and unresolved design-owner decisions

| ID | Item |
|---|---|
| G12 | Tooltip arrow glyph (polygon shape) not specified: an empty positioned slot |
| G8 / G9 | Dropdown check and Multiple indicator icons (research page): empty slots |
| B4-1 / G13 | Select trigger missing (D-17 / D-14) |
| B4-2 | Dark theme scope (D-23) |
| R4-Q3 | Footer Apply commit model, so the Footer Dropdown is blocked |
| G1–G4 | Empty, loading, scroll and group-header states |
| G5 / A40, G6 / A41, G7 | Light tooltip visibility, menu elevation, fixed heading clipping |
| D-27 | R3 image-only geometry (checkbox glyphs, radio ring, toggle radius and strokes) |
| D-22 | Contrast decisions A04, A14, A16, A38, A39, A40, A41 |
| D-09 | Radius 6/10 tokens |
| D-06, D-12, D-13, D-15 | Font licence; icon source, access and licences (R5) |

## 9. Files changed during the audit

| File | Change |
|---|---|
| `docs/figma-audit/r4-0-evidence.md` | §7 element node index added (AUD-2) |
| `docs/implementation/r4-final-closure-audit.md` | **new**: this report |
| `docs/implementation/r5-planning-proposal.md` | **new**: R5 proposal (planning only) |
| `docs/figma-audit/audit-progress-log.md`, `CHANGELOG.md` | audit entries |

**No file under `src/`, `showcase/` or `tests/` was modified by the audit.**

---

## 10. Post-audit resolution (approved 2026-11-20)

### 10.1 AUD-1: Dropdown listener lifecycle (FIXED)

| Change | Detail |
|---|---|
| `src/components/dropdown/dropdown.js` | Every element listener is bound to a per-controller `AbortController`. The outside-click `pointerdown` (capture) listener is added on `open()` and aborted on every close path, so it exists **only while open**. New `destroy()` closes without moving focus, aborts all listeners, clears the announcement timer and active option, and releases the controller. It is idempotent. New exports: `destroyDropdowns(root)` and `getDropdown(el)` |
| `src/annachy.js` | Re-exports `destroyDropdowns` and `getDropdown`. `initDropdowns` signature and behaviour are unchanged, so the public API stays backward compatible |
| `src/components/dropdown/README.md` | "JavaScript lifecycle" section |
| Test | `tests/tools/r4_dropdown_lifecycle_cdp.py`: **40 checks / 0 failures**. It counts real listeners with `DOMDebugger.getEventListeners` across every close path, 25 cycles, 10× re-init and destroy (also while open). It also checks the timer is cancelled and that 100 destroyed and 50 closed-then-removed dropdowns are garbage-collected (`WeakRef` + forced GC) |
| Mutants | DD-LEAK (15 failures), DD-DESTROY (9), DD-TIMER (1): all caught |
| Behaviour preserved | Dropdown visual 469 / 0, real input 82 / 0, init safety 10 / 0, showcase 15 / 0, unchanged from before the fix |

### 10.2 AUD-3: test tooling preserved (DONE)

`tests/tools/` contains 22 files (see its README):
- validators, harness and real-input drivers (moved from the scratchpad and made portable);
- the integrity baseline `baseline.py` / `baseline.json`, which replaces session-only backups and pins the 457 original tokens by hash;
- the sequential runner `run_all.py`;
- the guarded mutation runner `mutate.py` (19 mutants);
- R5 validators and the fixture generator.

Safety fixes made while porting:

| Issue | Fix |
|---|---|
| Temporary Chrome profiles were never deleted (250 had accumulated in `%TEMP%` from earlier runs) | The harness deletes its profile on finish and at exit. The leftovers were removed (one locked directory remains). `run_all.py` fails if any new profile is left behind |
| Mutation backups lived in the session scratchpad; an interrupted run could not be recovered by anyone else | Journal and backup are kept at a fixed `%TEMP%/annachy-mutation/`, flushed to disk before mutating. Restore happens in `finally`, on SIGINT/SIGTERM and at exit; a start is refused while a journal exists; `--recover` is available. **Verified by hard-killing a live mutation run**: journal detected, start refused, restored byte-identical |
| The backup folder inside the repository was locked by OneDrive sync | Moved outside the repository |
| `python -I` still wrote `__pycache__` | Tools set `sys.dont_write_bytecode` |
| Mutation anchors failed on CRLF files | The runner matches the file's line endings |
| The Figma read-only check depended on this session's transcript path | Optional via `ANNACHY_FIGMA_LOG`; otherwise reported as SKIPPED |
| The R3 real-input suite asserted the old export list | Updated to the exact new list, still strict |

### 10.3 Final regression after AUD-1 and the tooling migration

`python -I tests/tools/run_all.py`, run sequentially: **24 / 24 suites PASS** in 104 s, with 0 leftovers (Chrome profiles, bytecode, mutation state).

| Suite | Checks / result |
|---|---|
| Baseline: 457 original tokens, 5 token CSS files, 44 `src/` files | 0 failures |
| R1 static · R2 static · component CSS (8) | PASS |
| R3 closure static | 136 / 0 |
| R4 closure static (now with AUD-1 lifecycle assertions) | 107 / 0 |
| R5 icon infrastructure static | 53 / 0 |
| R1 + R2 browser, showcase links | PASS (18 references, 0 broken) |
| R3 browser: Button 9,964 · Gradient 1,863 · Input 11,952 · Checkbox 3,108 · Radio 2,423 · Toggle 4,904 | 34,214 / 0 |
| R4 browser: Dropdown 469 · Tooltip 1,441 | 1,910 / 0 |
| R5 icon-slot contract | 73 / 0 |
| R3 real input + showcase | 232 / 0 |
| R4 Dropdown real input · lifecycle · init safety | 82 / 0 · 40 / 0 · 10 / 0 |
| R4 Tooltip real input | 39 / 0 |
| R4 showcases: Dropdown · Tooltip | 15 / 0 · 13 / 0 |
| Mutation (`mutate.py --all`, sequential) | **19 / 19 caught**, all restored byte-identical; no state or markers left |
| Figma transcript check | Read-only tools only. Counts unchanged: `get_design_context` 147, `get_variable_defs` 128, `get_metadata` 98, `search_design_system` 3, `get_libraries` 1 |

**Intermittent observation (not a product defect).** One earlier full run had a single `ERR_CONNECTION_REFUSED` page-load error in the lifecycle suite; all 40 functional checks passed in that run. It did not reproduce in 5 isolated runs, 3 sequential Dropdown runs or the final full run. The harness now reports the failing URL and resource type, so a recurrence can be diagnosed. Recorded as an open test-environment observation (**TOOL-1**).

### 10.4 Files changed after the audit

| File | Change |
|---|---|
| `src/components/dropdown/dropdown.js`, `src/annachy.js`, `src/components/dropdown/README.md` | AUD-1 |
| `src/icons/manifest.schema.json`, `manifest.json`, `README.md` | R5 infrastructure (no artwork) |
| `tests/tools/` (22 files), `tests/fixtures/r5-icon-slot-check.html`, `tests/fixtures/r5-icons/` | AUD-3 and R5 tests |
| Docs | this report, `r5-planning-proposal.md`, `r5-implementation-spec.md`, `r5-readiness-report.md`, `README.md`, `CHANGELOG.md`, `audit-progress-log.md` |

No change to tokens, base styles, R3 components, Tooltip, or any CSS.
