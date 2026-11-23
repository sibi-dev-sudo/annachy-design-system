# R3 Closure Report — Core Controls

| Item | Value |
|---|---|
| Date | 2026-11-19 |
| Scope | Button, Button (gradient), Input (Outline + Filled), Checkbox, Radio, Toggle, Selection Controls wrapper |
| Verdict | **R3 CLOSED — PASS.** All suites pass. The known limitations below are documented and intentional (they are not invented values). |
| Figma | No write operation in the whole session. Invocations: `get_design_context` 142, `get_variable_defs` 123, `get_metadata` 93, `search_design_system` 3, `get_libraries` 1. These are all read-only tools, verified from the session transcript. No exports, downloads, screenshots or `create_session`. |
| Tokens | 464 = the 457 original values (byte-identical; metadata unchanged) + the 7 approved Loading tokens. No Radius 6/10 token added. |

---

## 1. Final component status

| Component | Figma set | Variants | Files | Status |
|---|---|---:|---|---|
| Button | `887:2492` | 432 | `src/components/button/` (css, html, README) | ✅ Complete |
| Button (gradient) | `1153:3370` | 55 | `src/components/button-gradient/` | ✅ Complete (every variant inspected) |
| Input / Outline + Filled | `1066:37962` / `1066:40663` | 150 + 175 | `src/components/input/` | ✅ Complete (State/Size/Radius model verified) |
| Checkbox | `1504:53300` | 126 | `src/components/checkbox/` (+ `checkbox.js`) | ✅ Complete; glyph slot empty (D-27) |
| Radio Button | `1504:52363` | 108 | `src/components/radio/` | ✅ Complete; ring not drawn (D-27) |
| Toggle | `1504:54471` | 180 | `src/components/toggle/` | ✅ Complete; radius and strokes not drawn (D-27); TG-1 |
| Selection Controls wrapper | `1504:57173` | 3 (aliases) | `src/components/selection-controls/README.md` | ✅ Documented alias of the Small variants; no CSS by design |
| **Total** | | **1,226** (+ 3 aliases) | | |

Integration:
- `src/annachy.css` declares `@layer annachy.tokens, annachy.base, annachy.components`.
- It imports 6 token files, then 4 base files, then 6 component files in the `annachy.components` layer, in that order.
- `src/annachy.js` exports only `initCheckboxes`, the single R3 script. It initialises indeterminate checkboxes on load.
- There are no frameworks, `package.json` or build tools.

## 2. Test results (2026-11-19, final run)

| Suite | Type | Checks | Failures | Result |
|---|---|---:|---:|---|
| R1 token validator | static | 464 tokens; 0 missing, extra or mismatched | 0 | PASS |
| R2 base validator | static | imports, focus rules, utilities | 0 | PASS |
| R3 component validator | static, 6 components | token refs, private props, raw-colour allow-list, forced/native state pairing, layer | 0 | PASS |
| R3 closure static audit | static | **136** | 0 | PASS |
| `r1-token-check.html` | browser | 464 computed | 0 | PASS |
| `r2-base-check.html` | browser | base computed styles | 0 | PASS |
| `r3-button-check.html` | browser | **9,964** (432 variants) | 0 | PASS |
| `r3-button-gradient-check.html` | browser | **1,863** (55) | 0 | PASS |
| `r3-input-check.html` | browser | **11,952** (325) | 0 | PASS |
| `r3-checkbox-check.html` | browser | **3,108** (126) | 0 | PASS |
| `r3-radio-check.html` | browser | **2,423** (108) | 0 | PASS |
| `r3-toggle-check.html` | browser | **4,904** (180) | 0 | PASS |
| R3 closure real-input audit (`r3-interaction.html` + 13 showcase pages, Chrome DevTools Protocol) | browser, real keyboard / mouse / accessibility tree | **218** | 0 | PASS |
| Showcase link check | HTTP | 16 local references | 0 broken | PASS |
| **R3 component browser checks total** | | **34,214** | **0** | |

Mutation tests (deliberate CSS defects, each caught, then the file was restored byte-identical):

| Component | Mutations caught |
|---|---|
| Button (gradient) | 1 (3 failures) |
| Input | 5 (90, 975, 325, 26, 1 failures) |
| Checkbox | 4 (48, 18, 189, 18) |
| Radio | 3 (36, 18, 18) |
| Toggle | 4 (19, 18, 60, 18) |

The real-input audit covers:
- **Tab order:** disabled controls are skipped; a radio group is a single stop; the Loading button stays reachable.
- **Keyboard focus visuals for every component:**
  - Button 2px border, with the outline suppressed;
  - gradient 2px stroke;
  - Input Outline `#3a6ff7` and Filled `Blue/600`;
  - the Checkbox Focus box;
  - D-20 Focus + Checked;
  - Toggle Focus thumb offsets (x 3 / 18.5).
- **Keyboard actions:**
  - Enter and Space activate buttons;
  - typing goes into the input and the Filled state applies after blur;
  - Error wins over Focused;
  - Space toggles the checkbox, the mixed checkbox and the switch;
  - ArrowDown moves the radio selection and skips the disabled radio.
- **Real mouse:**
  - `:hover` and `:active` (Primary `#003fbc` / `#3372ef`);
  - Filled field hover;
  - switch hover;
  - a mouse click does not show the focus border;
  - disabled checkbox, input and radio cannot be activated;
  - clicking the circle selects a radio.
- **Accessibility tree, for 15 controls:**
  - role, name, description, busy, disabled and invalid;
  - mixed checkbox state, switch checked state and the radio group name;
  - decorative parts are hidden.
- **Every showcase page over HTTP:**
  - no console or network errors;
  - tokens applied;
  - instance counts (432 + 9, 55 + 4, 325 + 2, 126 + 1, 108 + 2, 180 + 1);
  - all links return 200;
  - the **18 Checkbox Multi-select examples are indeterminate with the checked fill**.

## 3. Known visual limitations

| Item | Effect |
|---|---|
| Font | Temporary system fallback (D-06). Proxima Nova metrics differ, so label widths differ from Figma. The gradient angle is exact only at the documented Figma width (GB-2). |
| Icons | Icon slots are empty everywhere (D-12/D-13). Consumers supply SVG. |
| Checkbox glyph | The checked and indeterminate states show no check or remove mark (D-27, §5). |
| Radio ring | The Selected/Pressed ring is not drawn (D-27). |
| Toggle | The track is square-cornered (radius D-27). Thumb strokes and the focus border are not drawn. Focus shows only as a track colour and thumb offset (D-21). |
| Input | The Top Section keeps a fixed height when the label or description is hidden (IN-12, reproduced). |

## 4. Accessibility findings (reproduced, not fixed; design-owner decision D-22)

| ID | Component | Pair | Ratio | WCAG |
|---|---|---|---|---|
| **A04** | Button Primary Pressed | label `#fafcff` on `#3372ef` | **4.26:1** | Fails 1.4.3 normal text (passes large text only) |
| A14 | Button (gradient) | label on light gradient end `#3a79f7` | 3.89:1 | Fails 1.4.3 |
| A16 | Input Filled | placeholder `#dcdfe5` on `#f6f7f9` | 1.25:1 | Fails 1.4.3 |
| **A38** | Input Filled Hover | placeholder `#98a0ae` on `#f6f7f9` | **2.46:1** | Fails 1.4.3 (confirmed in R3-3) |
| **A39** | Toggle Off | track `#f6f7f9` vs page `#fafcff` / thumb | **1.04:1** | Fails 1.4.11 non-text (3:1); the track fill is derived (TG-1) |
| D-21 | Primary focus border | `#003fbc` on `#004feb` | 1.36:1 | Weak focus indicator; Toggle focus has no border (D-27) |
| T3 | Toggle Disabled On / Off | `#edeff2` vs `#f6f7f9` | 1.07:1 | On and off are indistinguishable when disabled |

## 5. D-27: unresolved image-only geometry (no export approved)

| Component | Unresolved | What is implemented |
|---|---|---|
| Checkbox | `functional/check` and `functional/remove` glyph geometry | Empty glyph slot with the evidenced size (16/20/20), centring and colour `#fafcff` |
| Radio | Selected/Pressed ring stroke width (`Blue/300` bound) | Fill, dot (8/10/12) and shadow; no ring |
| Toggle | Track corner radius; thumb stroke width; track Focus border width (`Border/Focus` bound) | Square track, thumb with no stroke, no focus border |

To resolve: the design owner supplies the values, or approves a read-only SVG export.

## 6. TG-1: Toggle colour limitation

In **Off**, **Disabled On** and **Disabled Off**, the track has no variable binding of its own (`get_variable_defs` Track − Thumb = ∅). The implemented fills (`Blue-Grey/50`, `/100`, `/50`) are the **only bound candidates**: the track shares them with the thumb's secondary paint. That matches the original audit reading, but it is derived rather than confirmed, and it makes A39 possible. It needs confirmation from the design owner.

## 7. Additional defects found by the closure audit

| # | Finding | Action |
|---|---|---|
| CL-1 | The Button and Input READMEs cited evidence as ranges ("§1–§4", "§7–§9"), so some sections weren't explicitly traceable | **Fixed:** sections are listed explicitly |
| CL-2 | Six element node IDs cited in `input.css` (`1066:38544`, `39889`, `40789`, `40798`, `41213`, `1780:40128`) were absent from the evidence documents | **Fixed:** `r3-0-evidence.md` §23.5 node index added |
| CL-3 / BTN-3 | A Loading button (`aria-disabled`) still fires `click` on Enter; this is native ARIA semantics | **Documented** in the Button README: consumers must guard clicks while busy (design unchanged) |
| CL-4 | Loading button focus has no Figma treatment, so it keeps the browser outline (no Loading+Focus variant exists) | Documented; intentional |
| (R3-3) | Input state precedence bugs (Success vs Error; forced Focus vs Filled) | Fixed earlier with `:where()`; covered by tests |

No defect was found in tokens, layers, imports, JavaScript initialisation, native keyboard behaviour, accessible names or descriptions, or showcase loading.

## 8. Open decisions carried to R4 and beyond

| ID | Decision |
|---|---|
| D-27 | Glyph, ring, radius and stroke geometry: owner values or read-only export approval |
| TG-1 / A39 | Toggle Off track colour |
| D-22 | Contrast fixes for A04, A14, A16, A38 and A39 |
| D-09 | Radius 6/10 tokens. The evidence shows Figma variables `Radius/6` and `Radius/10` exist and are bound by the Input. Adding them as tokens is justified by that binding but needs owner approval; until then they stay as component-local exact values. |
| BTN-1 | `Button/Primary/Background/Loading` variable (identical value) |
| D-06 / D-12 / D-13 | Font licence; icon source |
