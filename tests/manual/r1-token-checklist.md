# R1 Tokens & R2 Base — Verification Checklist

| Item | Value |
|---|---|
| Scope | R1 design tokens only (no base styles, no components) |
| Expected source | `docs/implementation/r1-token-mapping.md` (Figma file `rM3ixSG6i3DFfKZFWuxzs4`) |
| Implementation | `src/tokens/*.css`, `src/tokens/themes/light.css`, `src/tokens/tokens.json`, `src/annachy.css` |
| Automated browser check | `tests/fixtures/r1-token-check.html` (serve the project root over HTTP, e.g. `python -m http.server`, then open the page) |

Mark each item ✅ / ❌ and record the reviewer and date.

## 1. Automated check

- [ ] `tests/fixtures/r1-token-check.html` shows **STATUS: PASS**
- [ ] tokens.json count = **464** (457 R1 + 7 R3-0a Loading colours); computed present = 464; missing = 0; mismatched = 0
- [ ] Layer statement = `annachy.tokens, annachy.base, annachy.components`
- [ ] 6 imports listed as `loaded [layer annachy.tokens]` in this order: primitives, typography, effects, component-tokens, compat, themes/light

## 2. Counts (expected per mapping §9)

| Group | Expected | File | ✅/❌ |
|---|---:|---|---|
| Colour primitives | 82 | `primitives.css` | |
| Semantic colours (Light) | 27 | `themes/light.css` | |
| Button component colours | 50 (43 + 7 R3-0a) | `component-tokens.css` | |
| Icon-state colours | 5 | `component-tokens.css` | |
| Compatibility values | 5 (+ `shadow/sm`) | `compat.css` | |
| Typography primitives | 7 | `primitives.css` | |
| Type styles × 7 properties | 28 × 7 = 196 | `typography.css` | |
| Heights | 12 | `primitives.css` | |
| Radius | 11 | `primitives.css` | |
| Border widths | 3 | `primitives.css` | |
| Grid reference values | 13 | `primitives.css` | |
| Documented shadows (incl. swatch) | 33 | `effects.css` | |
| Component effect styles | 6 | `effects.css` | |
| Blur / Glass / glass fills | 12 | `effects.css` | |
| Gradient | 1 | `effects.css` | |
| **Total** | **464** | | |

## 3. Value spot-checks against Figma evidence

| Token | Expected | Evidence | ✅/❌ |
|---|---|---|---|
| `--annachy-color-blue-500` | `#004feb` | `02` §1.2 | |
| `--annachy-color-error-700` | `#9d4520` (D-02 — preserved) | `02` §1.2 | |
| `--annachy-color-text-primary` | `#0b0c0f` | `02` §1.3 | |
| `--annachy-color-background-secondary` | `#f6f7f9` | `02` §1.3 | |
| `--annachy-color-button-primary-background-pressed-active` | `#3372ef` | `button.md` §1.4 | |
| `--annachy-color-button-tertiary-grey-background-hover` | `#f3f4f7` | `button.md` §1.4 | |
| `--annachy-color-icon-state-error` | `#e72b23` | `06` §2 | |
| `--annachy-compat-color-border-default` | `#e1e1e2` | `checkbox.md` §4 | |
| `--annachy-font-family-sans` | `"Proxima Nova"` (no fallback — D-06) | `03` §1 | |
| `--annachy-type-h7-font-size` / `-line-height` | `16px` / `18px` (Mobile, active) | `03` §2.1 | |
| `--annachy-type-h7-font-size-desktop` | `20px` (reference, not active) | `03` §2.1 | |
| `--annachy-type-body-s-semibold-font-size` / `-line-height` | `14px` / `18px` | `03` §4.1 | |
| `--annachy-type-label-medium-line-height` | `21px` | `03` §2.3 | |
| `--annachy-size-height-40` | `40px` | `button.md` §1.3 | |
| `--annachy-radius-12` | `12px` | `04` §3.1 | |
| `--annachy-border-width-m` | `1.5px` | `05` §3 | |
| `--annachy-grid-desktop-margin` | `120px` | `04` §1.1 | |
| `--annachy-shadow-scale-sm-01` | `1.9500000476837158px 1.9500000476837158px 2.5999999046325684px 0px #00000026` (unrounded) | `05` §1 | |
| `--annachy-effect-button-focus` | 5 layers `#0141c0…` | `05` §3.1 | |
| `--annachy-blur-sm-01` | `0px` (D-11 — preserved) | `05` §2 | |
| `--annachy-gradient-brand` | `linear-gradient(22.572274294652743deg, … 13.397%, … 86.603%)` | `button.md` §2 | |

## 4. Architecture rules

- [ ] No spacing tokens exist (D-08)
- [ ] No `@media` rules in `src/tokens/` (D-07)
- [ ] Every active `--annachy-type-*-font-size` / `-line-height` equals its `-mobile` value; `-desktop` values are not referenced by any active token (D-05)
- [ ] Semantic colours declared on `:root, [data-annachy-theme="light"]`
- [ ] `src/tokens/themes/dark.css` does **not** exist (V1 Light only, D-03)
- [ ] Lowercase Figma colour scheme and `Supporting/*` are **absent** (D-01)
- [ ] Scale B (specimen sheet) styles are **absent** (D-04)
- [ ] Flagged tokens carry an inline comment: D-02 (`error-700`), D-04 (both H3 rows), D-06 (font family), D-11 (blur 0), D-19 (compat), SUS-03 (`button-secondary-grey-border-disabled`)
- [ ] `src/annachy.js` has no R1 JavaScript. *Since R3-4 it re-exports `initCheckboxes` from `components/checkbox/checkbox.js`, the only R3 script.*

## 5. Showcase visual review (`showcase/`)

| Page | Check | ✅/❌ |
|---|---|---|
| `foundations/colors.html` | 171 swatches render (82 + 27 + 50 + 5 + 3 compat + 4 glass fills); colours match Figma Colour page | |
| `foundations/typography.html` | 28 styles; banner states font files not loaded; Mobile active / Desktop reference shown | |
| `foundations/effects.html` | Shadow Scale 17, Shadow Effects 15, swatch 1, component effects 6, compat 1, blur 5, glass 3, gradient 1 | |
| `foundations/grid.html` | 13 grid tokens; 3 illustrations (4 / 12 / 12 columns); "reference only" banner | |
| `foundations/dimensions.html` | 12 heights, 11 radius, 3 border widths; "no spacing tokens" banner | |

Known, expected differences from Figma (not defects):
- Text renders in the browser default font — Proxima Nova files are not included (R2, D-06).
- Glass specimens use `backdrop-filter` as an approximation — Figma GLASS parameters other than radius are not retrievable.

## 6. R2 — Base styles (added 2026-11-19)

Automated: `tests/fixtures/r2-base-check.html` (serve project root over HTTP).

- [ ] `r2-base-check.html` shows **STATUS: PASS**, failures 0
- [ ] `r1-token-check.html` still PASS — R1 token values unchanged (464 after the R3-0a addendum)
- [ ] First 10 imports load in order (later imports are R3 components in `annachy.components`): 6 × `annachy.tokens`, then `base/reset.css`, `base/document.css`, `base/typography.css`, `base/utilities.css` in `annachy.base`
- [ ] 0 author `:focus` / `outline` rules · 0 `@font-face` · 0 `@media`
- [ ] Body computed style: 16px / 24px, weight 400 (Body M), colour = `Text/Primary`, background = `Background/Primary`, margin 0
- [ ] Body font-family begins `"Proxima Nova"` followed by `system-ui, sans-serif` (temporary render fallback, D-06)
- [ ] `--annachy-font-family-sans` is still exactly `"Proxima Nova"`
- [ ] Only one new custom property in base: `--annachy-base-font-family-render`
- [ ] 28 `.annachy-text-*` classes compute to active (Mobile) token values; none uses a `-desktop` token
- [ ] 62 utilities: text colour 7, background 3, radius 11, shadow/effect 39, gradient 1, `.annachy-visually-hidden` 1
- [ ] No spacing, layout, breakpoint, grid or focus utilities exist
- [ ] Reset does not remove browser focus indicators (Tab through `showcase/foundations/base.html`: link and button show the browser default)

| Page | Check | ✅/❌ |
|---|---|---|
| `foundations/base.html` | Font-fallback and focus banners visible; document defaults; 28 text classes; 62 utilities | |
| `foundations/typography.html` | Samples use `.annachy-text-*` classes; banner states the system fallback is temporary | |
| All foundations pages | Nav includes "Base & utilities" | |

Known, expected differences (not defects): system font metrics differ from Proxima Nova; no custom focus styling until R3 applies Figma component focus specs.

Reviewer: ______________  Date: ______________

## 7. R3-1 — Button (added 2026-11-19)

Automated: `tests/fixtures/r3-button-check.html` (serve the project root over HTTP).

- [ ] **STATUS: PASS**, 432 variants rendered, failures 0
- [ ] r1 and r2 fixtures still PASS
- [ ] `showcase/components/button.html`: 6 tables (one per Type), each 12 sizes × 6 states; Loading shows 3 dots (4px at 24–28, 6px at 32–56)
- [ ] Interactive row: hover changes the fill (except Link, B1); Tab shows the 2px Figma focus border and no browser outline; press shows the Pressed colours
- [ ] Icon-only button is announced as "Home"; a Loading button is announced by its label and as busy (screen reader spot check)
- [ ] Flags B1, B4/D-22, SUS-03, BTN-1, BTN-2 and D-21 are visible in the CSS comments and README

Known, expected differences: label widths (system fallback font); icon slots are empty.

## 8. R3-2 — Button (gradient) (added 2026-11-19)

- [ ] `tests/fixtures/r3-button-gradient-check.html` **STATUS: PASS**, 55 variants, failures 0
- [ ] `showcase/components/button-gradient.html`: 11 sizes × 5 states; Focus has a 2px stroke and darker fill; Disabled is faded
- [ ] Tab to a size-24 gradient button: the label line height switches to 12/17 (GB-3)
- [ ] r1, r2 and r3-button fixtures still PASS

## 9. R3-3 — Input (added 2026-11-19)

- [ ] `tests/fixtures/r3-input-check.html` **STATUS: PASS**, 325 variants, failures 0
- [ ] `showcase/components/input.html`: Outline (6 states) and Filled (7 states) for every size × radius
- [ ] Interactive: Filled border turns `Blue/500` on hover; focusing shows the Focused colours with no browser outline; typing a value then leaving shows Filled
- [ ] A screen reader announces the label, description and sub-text; the Error example announces "invalid"

## 10. R3-4 / R3-5 / R3-6 — Checkbox, Radio, Toggle (added 2026-11-19)

- [ ] `r3-checkbox-check.html` (126), `r3-radio-check.html` (108) and `r3-toggle-check.html` (180) all show **STATUS: PASS**
- [ ] Serve over HTTP: on the Checkbox showcase, Multi-select shows the checked fill (set by `checkbox.js`)
- [ ] The check glyph, radio ring and toggle track radius are deliberately absent (D-27). Confirm with the design owner before release.
- [ ] Keyboard: Space toggles the checkbox and switch; arrow keys move within the radio group; focus shows the Figma focus treatment
- [ ] A screen reader announces "switch" for Toggle, "checkbox, mixed" for Multi-select, and the subtext as the description
