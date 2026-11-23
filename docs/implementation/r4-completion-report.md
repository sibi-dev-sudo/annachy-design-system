# R4 Completion Report — Dropdown and Tooltip

| Item | Value |
|---|---|
| Date | 2026-11-20 |
| Scope | The 108 variants approved as ready: Dropdown Item 20 + Menu 8 (Light, Footer=None) and Tooltip 80 |
| Verdict | **R4 (approved scope) COMPLETE — all suites PASS.** Blocked parts were not started. |
| Figma | Read-only only. R4-0 evidence: 15 calls (`get_design_context` ×5, `get_metadata` ×5, `get_variable_defs` ×5). No writes, screenshots, exports or downloads. |
| Tokens | 464, unchanged: 457 original values byte-identical plus the 7 R3-0a tokens. No token added in R4. |

## 1. Components

| Component | Figma | Variants implemented | Files |
|---|---|---:|---|
| Dropdown / Item | `1451:25092` | **20** of 40 (Light) | `src/components/dropdown/` (`dropdown.css`, `dropdown.js`, `dropdown.html`, `README.md`) |
| Dropdown / Menu | `1451:25521` | **8** of 48 (Light, Footer=None) | same |
| Tooltip | `1448:16825` | **80** of 80 | `src/components/tooltip/` (`tooltip.css`, `tooltip.js`, `tooltip.html`, `README.md`) |
| **Total** | | **108** | |

Integration:
- `src/annachy.css` imports `dropdown.css` and `tooltip.css` in `annachy.components`, after R3.
- `src/annachy.js` exports `initCheckboxes`, `initDropdowns` and `initTooltips`; each auto-initialises its markup.
- No dependencies or build tools.

## 2. Test results (final, sequential run 2026-11-20)

| Suite | Checks | Failures |
|---|---:|---:|
| R1 static | 464 tokens | 0 |
| R2 static | — | 0 |
| R3 component static (now 8 components incl. dropdown, tooltip) | — | 0 |
| R3 closure static | 136 | 0 |
| R1 browser (`r1-token-check`) | 464 computed | 0 |
| R2 browser (`r2-base-check`) | — | 0 |
| R3 browser (Button 9,964 · Gradient 1,863 · Input 11,952 · Checkbox 3,108 · Radio 2,423 · Toggle 4,904) | 34,214 | 0 |
| **R4 Dropdown visual** (`r4-dropdown-check`) | **469** | 0 |
| **R4 Tooltip visual** (`r4-tooltip-check`) | **1,441** | 0 |
| R3 closure real-input audit (keyboard / mouse / accessibility tree / R3 showcase) | 232 | 0 |
| **R4 Dropdown real-input audit** (`r4-dropdown-interaction`) | **82** | 0 |
| **R4 Tooltip real-input audit** (`r4-tooltip-interaction`) | **39** | 0 |
| R4 showcase pages over HTTP (Dropdown 15 · Tooltip 13) | 28 | 0 |
| Showcase link check | 18 references | 0 broken |

### 2.1 Mutation tests (each caught, then restored byte-identical)

| Component | Mutation | Failures detected |
|---|---|---:|
| Dropdown | Mobile padding 12 → 10 | 10 |
| Dropdown | Selected fill | 4 |
| Dropdown | Focus stroke 2 → 1 | 4 |
| Dropdown | Menu radius 12 → 8 | 8 |
| Dropdown | Typeahead 500 → 2,000 ms | 9 |
| Dropdown | Disabled-option guard removed | 7 |
| Dropdown | Wrap at the list end | 1 |
| Dropdown | No focus restore on search Escape | 1 |
| Tooltip | Desktop light centring −0.5 → 0px | 2 |
| Tooltip | Right-arrow mirror removed | 8 |
| Tooltip | Mobile heading height 62 → 60 | 20 |
| Tooltip | Desktop text weight 500 → 600 | 20 |
| Tooltip | Show delay 500 → 100 ms | 1 |
| Tooltip | Hide delay 150 → 0 ms | 1 |
| Tooltip | Escape disabled | 1 |
| Tooltip | Arrow gap 12 → 0 | 2 |

**16 / 16 caught.** One additional Dropdown mutant (no focus restore on a plain dropdown's Escape) was *equivalent*: focus never leaves the select-only trigger, so it can't be observed. It was replaced by the search-Escape mutant above.

**Process note:** the first Tooltip batch was stopped by the system for low memory and left one mutation (M4) applied. It was detected and restored before any other step (byte-identical to the validated original). M4–M8 were then run one at a time in the foreground, with a pristine-backup check, a `finally` restore and SHA-256 verification.

## 3. Accessibility results

| Area | Result |
|---|---|
| Dropdown semantics | Select-only combobox + listbox (plain), dialog + search combobox (searchable). The accessibility tree shows the combobox role, name and expanded state, the listbox name, options with selected / disabled state, `multiselectable`, the dialog name, a named search combobox (not the placeholder) and the status role |
| Dropdown keyboard | Arrow keys (no wrap), Home / End, Ctrl+Home / End (search), PageUp / Down, Enter / Space, typeahead (500 ms, repeated-letter cycling), Escape (search: clear, then close), Tab closes; **disabled options can become active but are never selectable** (R4-Q2) |
| Dropdown pointer / touch | Click and tap select; hover styling does not move the active option; outside pointer closes; disabled trigger cannot open; flips above at the bottom edge |
| Announcements | Polite "N selected" / "N results" (R4-Q6); identical consecutive messages are still re-announced; no animation-frame dependency |
| Tooltip | `role="tooltip"` with `aria-describedby`; icon-only triggers named by `aria-label`; shown on keyboard focus immediately and on hover after 500 ms; hides 150 ms after leave; hoverable; Escape without moving focus; touch tap; one at a time; content non-interactive; `aria-disabled` triggers supported (T13) |
| Contrast (text) | Pass: 5.89:1 (selected) to 19.03:1 (tooltip) |
| Contrast (non-text) | **A40** light tooltip on a light page 1.00:1; **A41** Menu boundary 1.70:1 (no shadow). Both reproduced as designed (D-22-style owner decision) |

## 4. Known limitations (documented, not invented)

| ID | Limitation |
|---|---|
| **G12** | The tooltip arrow glyph is not drawn: an empty 20 × 20 slot, positioned and transformed exactly per variant |
| **G8 / G9** | The Dropdown Single check and Multiple "checkbox" icons are research-page assets, so the slots are empty; size and state colour are implemented |
| **G13 / B4-1** | No Select trigger design; the consumer supplies the trigger (R3 Button in the examples) |
| G1–G4 | No empty, loading, scroll/max-height or group-header states, so there is no "No results" message |
| G5 / TT1 · A40 | Light tooltip invisible on light surfaces |
| G6 / D2 · A41 | Menu has no shadow |
| G7 / TT5 | Heading tooltips are fixed-size; long text overflows the body |
| D6 | Search placeholder `Text/Secondary` / Body M Regular |
| **DD-1 (derived)** | Search focus border = Input Field / Outline Focused `#3a6ff7` |
| **TT-POS (derived)** | Trigger-to-tooltip gap 12px (arrow tip touches the trigger) |
| Mobile / Desktop | Visual variants only; no breakpoints (D-07) |
| Font | Temporary system fallback (D-06): label widths and wrap points differ from Proxima Nova |

## 5. Defects found and fixed during R4

| # | Defect | Fix |
|---|---|---|
| R4-D1 | Menu 2px taller than Figma (the border counted in the layout) | Inset stroke (Figma stroke is outside the layout) |
| R4-D2 | Live-region text set inside `requestAnimationFrame`, which doesn't run on hidden pages | Direct write; repeated messages alternate a trailing no-break space |
| R4-D3 | A public `--annachy-dropdown-offset` hook introduced an undesigned dimension | Removed (no spacing added) |
| R4-D4 | After Escape, a fresh hover didn't re-show the tooltip (T5) | Pointer entry re-arms it; regression check added |

## 6. Not started (blocked, per instruction)

| Item | Blocker |
|---|---|
| Dropdown Footer (16 Menu variants) | R4-Q3: Apply commit model |
| Dropdown Dark (20 Item + 24 Menu variants) | B4-2: Dark scope |
| Select | B4-1: no component in Figma |
| Tooltip arrow glyph | G12: polygon shape unknown (owner geometry or export approval) |
| Dropdown icons | G8 / G9: icon-source decision |

## 7. Files

| Added | Changed |
|---|---|
| `src/components/dropdown/` (4 files), `src/components/tooltip/` (4 files) | `src/annachy.css`, `src/annachy.js` |
| `showcase/components/dropdown.html`, `showcase/components/tooltip.html` | `showcase/index.html`, `showcase/showcase.css`, all component pages (navigation) |
| `tests/fixtures/r4-dropdown-check.html`, `r4-dropdown-interaction.html`, `r4-tooltip-check.html`, `r4-tooltip-interaction.html` | `docs/figma-audit/r4-0-evidence.md` (§6), `09-accessibility.md` (A40, A41), `components/dropdown.md`, `components/tooltip.md` |
| `docs/implementation/r4-completion-report.md` | `r4-behaviour-spec.md`, `r4-components-spec.md`, `audit-progress-log.md`, `CHANGELOG.md`, `README.md` |

The real-input test drivers (`cdp_lib.py`, `r4_dropdown_cdp.py`, `r4_tooltip_cdp.py`) and the mutation runner are authoring aids in the session scratchpad and are not shipped, matching the earlier validators.
