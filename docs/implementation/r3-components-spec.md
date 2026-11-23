# R3 Implementation Plan — Core Controls

| Item | Value |
|---|---|
| Phase | **R3 — Core controls** (roadmap `docs/figma-audit/10-summary-and-roadmap.md` §7) |
| Status | **R3 CLOSED (2026-11-19) — see `r3-closure-report.md`.**  R3 complete: Button, Button (gradient), Input, Checkbox, Radio and Toggle implemented and validated; Selection Controls wrapper documented as an alias.** R3-0 / R3-0b evidence complete (98 read-only calls). R3-0a token addendum done (464 tokens). B-01 approved. |
| Depends on | R1 tokens (457, validated) · R2 base (validated) — both unchanged by R3 |
| Source of truth | Figma file `rM3ixSG6i3DFfKZFWuxzs4`; component evidence in `docs/figma-audit/components/*.md` |
| Date | 2026-11-19 |

---

## 1. Scope

| Component | Figma set | Variants | Spec | In R3 |
|---|---|---:|---|---|
| Button (All Buttons) | `887:2492` | 432 | `button.md` | ✅ |
| Button (gradient) | `1153:3370` | 55 | `button.md` §2 | ✅ |
| Input Field / Outline | `1066:37962` | 150 | `input.md` | ✅ |
| Input Field / Filled | `1066:40663` | 175 | `input.md` | ✅ |
| Checkbox | `1504:53300` | 126 | `checkbox.md` | ✅ |
| Radio Button | `1504:52363` | 108 | `radio.md` | ✅ |
| Toggle | `1504:54471` | 180 | `toggle.md` | ✅ |
| Selection Controls (wrapper) | `1504:57173` | 3 | `selection-controls.md` | ✅ (as documentation alias — §4.6) |
| Dropdown, Tooltip, Select | — | — | — | ❌ R4 |
| Navigation | — | — | — | ❌ R6 |

Total Figma variants covered: **1,229**.

---

## 2. Architecture

### 2.1 Files (per component)

```
src/components/<name>/
├── <name>.css      layer annachy.components — consumes R1 tokens only (+ evidenced component-local values)
├── <name>.html     canonical markup reference (all variants as markup patterns)
├── <name>.js       only where native HTML cannot express a Figma state (see §2.5)
└── README.md       API: classes ↔ Figma properties, states, a11y notes, flags
```

Entry `src/annachy.css` gains, after the base imports:
`@import url("components/<name>/<name>.css") layer(annachy.components);` for button, input, checkbox, radio, toggle.

### 2.2 Figma property → markup mapping (traceability rule)

Every Figma variant property maps 1:1 to a modifier class; Figma property **values** keep their Figma spelling (kebab-cased).

| Figma property | Markup | Example |
|---|---|---|
| `Type` | `.annachy-button--<type>` | `Type=Secondary Grey` → `.annachy-button--secondary-grey` |
| `Size` (numeric) | `.annachy-<c>--size-<n>` | `Size=40` → `.annachy-button--size-40` |
| `Size` (named) | `.annachy-<c>--<size>` | `Size=Medium` → `.annachy-checkbox--medium` |
| `Radius` (Input) | `.annachy-input--radius-<n>` | `Radius=6` → `.annachy-input--radius-6` |
| `Position` / `Alignment` | `.annachy-<c>--control-<pos>` / `--align-<a>` | `Position=Right` → `--control-right` |
| Booleans (`showLabel`, `showLeftIcon`, …) | presence/absence of the child element | no class |
| Text props (`label`, `subText`, …) | element content | — |
| `State` | **native states** (`:hover`, `:active`, `:focus-visible`, `:disabled`, `:checked`, `[aria-invalid]`, `[aria-busy]`) **plus** forced-state classes `.is-hover`, `.is-focus`, `.is-pressed` for static showcase/parity testing only | Figma `State=Pressed` ↔ `:active` / `.is-pressed` |

### 2.3 Values rule

1. Colours, typography, radius, heights, effects → **R1 tokens only**.
2. Padding, gap, border widths, control/track geometry → **component-local private custom properties** (e.g. `--_button-padding-x`) whose literal values are evidenced Figma values with the node ID in a comment. These are not a spacing scale (D-08) and are not exported tokens.
3. Raw Figma values that are not variables (e.g. Input/Outline focus `#3a6ff7`, gradient-button raw shadow, Tooltip raw radius) → component-local, commented with node ID and flag.
4. **No value is used unless it appears in the audit evidence.** Missing values are listed in §5 and must be completed (R3-0) before the affected part is coded.

### 2.4 Faithful-replication rule for known design defects

Where Figma itself has a defect, R3 reproduces Figma and flags it (it does **not** silently fix it):

| Defect | Component | Flag |
|---|---|---|
| Link Hover identical to Default | Button | D-20 / B1 |
| Primary Pressed `#3372ef` lighter than Hover; label 4.26:1 | Button | D-22 / D-26 |
| Gradient label 3.89:1 at light end | Button (gradient) | D-22 |
| Secondary Grey Pressed bound to `Border/Disabled` | Button | SUS-03 / D-26 |
| Placeholder `#dcdfe5` (Filled 1.25:1) | Input | D-22 |
| Outline has no Hover; Error icon visible in all states | Input | D-20 / IN5 |
| No Hover / Error in Checkbox & Radio | Checkbox, Radio | D-20 |
| Foreign `surface-bg` / `border-default` / `shadow/sm` | Checkbox, Radio | D-19 (compat tokens) |
| Toggle thumb bound to `Button/Primary/Content/Loading` | Toggle | T2 (token used as bound) |

Each flagged rule carries a CSS comment and is listed in the component README.

### 2.5 Semantics & JavaScript (B-01 — **approved 2026-11-19**)

| Component | Element | JS |
|---|---|---|
| Button | native `<button type="button">` (Link type: `<button>` styled as link; `<a>` when navigating) | none; Loading = `aria-busy="true"` + `disabled` |
| Input | native `<input>` + `<label for>`; description/sub-text via `aria-describedby`; Error = `aria-invalid="true"` | none |
| Checkbox | native `<input type="checkbox">` + label | `checkbox.js`: sets `.indeterminate` from `data-indeterminate` (Figma `Multi-select`) — only JS in R3 |
| Radio | native `<input type="radio">` in a `fieldset` group | none (native arrow-key behaviour) |
| Toggle | native `<input type="checkbox" role="switch">` | none |

Native elements provide keyboard operation and roles without custom scripting. Figma contains no behaviour; **B-01 approved by the owner**: native HTML semantics are the behaviour baseline, including accessible names (visible `<label>`, or `aria-label` for icon-only buttons) and ARIA state where native state is insufficient (`aria-busy`, `aria-invalid`, `aria-describedby`; `role="switch"` for Toggle).

### 2.6 Focus

Per R2 decision: no global focus style. Each component applies **its own Figma Focus variant** to `:focus-visible` (and `.is-focus`):

| Component | Figma focus treatment (evidence) |
|---|---|
| Button Primary | 2px border `Button/Primary/Border/Focus` `#003fbc` (`887:484`) |
| Button Secondary | 2px border `Button/Secondary/Border/Default` (`887:784`) |
| Button Secondary Grey / Tertiary / Tertiary Grey / Link | **2px** border `…/Border/Focus` `#004feb` (`887:1084`, `1384`, `1684`, `1984` — R3-0 §3) |
| Button (gradient) | **2px** `Blue/500` border + gradient `Blue/600`→`Blue/400`, no shadow (`1153:3641` — R3-0 §5) |
| Input Outline | 1px border `#3a6ff7` raw (`1066:38544`) |
| Input Filled | 1px border `Blue/600`, bg `Blue-Grey/50` (`1066:41213`) |
| Checkbox / Radio | 2px `#004feb` border on `Blue-White/300` + `Button/Focus` + `shadow/sm` — Figma shows the **unchecked** appearance only. **D-20 RECOMMENDATION (not a confirmed Figma specification):** when focused *and* checked/selected, preserve the checked appearance (fill, glyph/dot) and apply the focus treatment (border + `Button/Focus` effect) on top. Flagged in CSS and README. |
| Toggle | Focus On: `Background/Focus` + `Border/Focus` (`1504:54682`, thumb x 18.5); Focus Off adds `Button/Primary/Border/Focus` `#003fbc` + `Blue-Grey/200` (`1504:54697`) — **target element and stroke width not returned** (see §7). Hidden "Focus Ring" layer (−4 inset, no bindings) stays hidden in Focus variants → **not rendered**. |

Browser default focus remains for any element without a Figma focus variant.

---

## 3. Shared conventions

| Item | Rule |
|---|---|
| Class prefix | `.annachy-<component>` |
| State classes for testing | `.is-hover`, `.is-focus`, `.is-pressed` — equivalent to native states; used by showcase and parity fixtures |
| Width | Hug content (Figma auto-layout) unless Figma shows fixed width (Input 337 is a documentation frame width → `inline-size: 100%` of container with **no** invented max) |
| Icons | **Slots** (`.annachy-<c>__icon`) sized per Figma (Button 20, Input 24/16, Filled sub-text 14). No icon assets shipped in R3 (D-12/D-13 → R5). Showcase shows empty slots. |
| Dark theme | Components reference semantic/component tokens only, so a future dark theme applies without component edits. |

---

## 4. Component plans

### 4.1 Button (All Buttons)

| Aspect | Confirmed (evidence) | Gap |
|---|---|---|
| Structure | `[icon][label][icon]`, row, centred, clip; icon instance 20×20 at all sizes | — |
| Height / radius | `Height/N`; radius 4 (24–28), 8 (32–40), 12 (42–56) | — |
| Typography per size | 24–26 Body XS-Semibold 12/18; 28–32 Body S-Semi 14/18; 36–42 H7 16/18; 46–48 H6 18/20; 52–56 H5 20/24 | — |
| Padding (x / y) / gap | 24: 10/4, 4 · 26: 10/4, 4 · 28: 10/8, 4 · 32: 10/12, 4 · 36: 12/10, 6 · 38: 14/10, 6 · 40: 16/12, 6 · 42: 16/12, 6 · 46: 16/16, 8 · 48: 16/18, 8 · 52: 18/18, 8 · 56: 20/20, 8 | ✅ complete (R3-0 §1) |
| State colours (6 types × 5 states) | All bound variables (R1 `--annachy-color-button-*`) | — |
| Focus | **2px border, all six types** (R3-0 §3) | ✅ |
| Secondary default border | **1px** `Secondary/Border/Default` (R3-0 §2) | ✅ |
| Loading | 3 ellipses 6×6 at x 0/11/22 in 28×6; dot colour = per-type `Content/Loading`; Secondary / Secondary Grey bg = `Background/Loading` `#fafcff` (R3-0 §4) | ⚠ **7 Loading variables missing from R1 → token addendum R3-0a** (§6) |
| Widths | Focus variants +4px (border outside content) | — |

### 4.2 Button (gradient)

| Aspect | Confirmed | Gap |
|---|---|---|
| Size 24 Default | gradient `--annachy-gradient-brand`, 1.5px `Blue/300` border, raw radius 4, px 8, gap 4, raw 4-layer shadow, Body XS-Semi, `Base/White` | — |
| States @40 | Default / Hover (raw rgba gradient) / Focus (2px `Blue/500`, `Blue/600`→`Blue/400`) / Pressed (`Blue/500`→`Color 2`, blue shadow) / Disabled (19 % alpha) — R3-0 §5 | ✅ |
| Sizes 32 / 40 / 48 / 56 | px 12/12/16/16, gap 8/8/12/12, raw radius 8/8/12/12, type H7 / H7 / **Subheading L-Semibold 18/25** / H5 — R3-0 §6 | ✅ |
| Gradient angle | **size-dependent**: 22.57° @24, 23.41° @32, 28.43° @40, 28.99° @48, 31.87° @56 → component-local per-size angle; `--annachy-gradient-brand` exact only at 24 | ✅ (rule) |
| Sizes 26 / 28 / 36 / 42 / 46 / 52 | exist in Figma | ❌ **not inspected** (padding, gap, radius, type, angle) — do not ship these sizes until inspected |

### 4.3 Input (Outline & Filled)

| Aspect | Confirmed | Gap |
|---|---|---|
| Anatomy | label (H7 16/18), description (Body S 14/20), field (row, gap 6, px 14, height = Size, 1px border), value (Body M-Medium 16/24), right icons gap 8, sub-text (Body S) | — |
| Sizes | field height 46/48/50/54/56; **padding-x 14, gap 6 at every size** (R3-0 §7) | ✅ |
| Radius | 4/6/8/10/12 (property values) | 6/10 off-scale (D-09) — implemented as component-local values, flagged |
| Outline Default/Focused/Error | full colours (`input.md` §3.1) | — |
| Outline Filled/Disabled/Success | element mapping (R3-0 §8) | ✅ |
| Filled Default/Focused | full colours | — |
| Filled Hover/Filled/Error/Disabled/Success | element mapping (R3-0 §9); Filled Disabled has **no fill** | ✅ |
| Icon opacity | 30 % in Filled Default/Hover/Disabled; 100 % otherwise | ✅ |

### 4.4 Checkbox

| Aspect | Confirmed | Gap |
|---|---|---|
| Medium | box 24×24, `Radius/4`, label pl 12 (Label Medium 16/21), subtext 14/20 w184 | — |
| Checked / Pressed / Disabled On / Focus / Unchecked | colours & effects bound; Checked border 1px `Blue/300`; **Unchecked & Disabled border 2px** (R3-0 §10) | ✅ |
| Small / Large | box **20 / 28**, `Radius/4`; glyph 16 / 20; label style unchanged (Label Medium 16/21) | ✅ |
| Multi-select (indeterminate) | colours as Checked; glyph `functional/remove` 20×20 | glyph **geometry/colour** ❌ (image-only, D-27) |
| Check glyph | frame `functional/check` 20×20 (16 at Small); no child shapes | glyph **geometry/colour** ❌ (image-only, D-27) |
| Position Right / Alignment Top | Right: content → control, text padding-right 12; Top: `align-items: flex-start` (R3-0 §11) | ✅ |
| Alignment Bottom | variant exists | ❌ not inspected (presumed `flex-end`, unverified) |
| Focus + Checked | not in Figma | **D-20 recommendation** (§2.6) |

### 4.5 Radio

| Aspect | Confirmed | Gap |
|---|---|---|
| Medium layout | as Checkbox; control 24×24 | — |
| Sizes | 20 / 24 / 28 (`1504:52373`, `52686`, `52997`) | ✅ |
| Selected | fill `Button/Primary/Background/Default`, stroke colour `Blue/300`, effect `Button/Default`; dot `Background/Primary` `#fafcff` **8 / 10 / 12** at inset 6 / 7 / 8 (R3-0 §12) | ring **stroke width** ❌ (image-only) |
| Unselected | 2px `border-default`, `surface-bg`, radius 12 (full circle) | ✅ |
| Layouts | Right / Top as Checkbox | ✅ (Bottom ❌) |

### 4.6 Toggle & Selection Controls wrapper

| Aspect | Confirmed | Gap |
|---|---|---|
| Sizes | track **32×16 / 38×20 / 44×24**; thumb **12 / 16 / 20**; inset 2; thumb x Off 2 → On 18 / 20 / 22; roots 228×40 / 234×41 / 240×42 (R3-0 §13) | ✅ |
| Label per size | **Label Small 14/20 / Label Medium 16/21 / Label Large 18/22** (new finding) | ✅ |
| Colours | On track `Button/Primary/Background/Default`; **Off track `Blue-Grey/50`**; thumb `#fafcff` + `Blue-Grey/100` + effect `Toggle/On`/`Toggle/Off`; Focus Off `+#003fbc`, `Blue-Grey/200`; Pressed Off `+Blue-Grey/300` | ✅ colours |
| Track radius | pill visually | ❌ value not returned |
| Thumb stroke width; Focus Off / Pressed Off element & width | — | ❌ not returned |
| Focus On thumb | x 18.5 (vs 20) | ✅ reproduce as-is (flag) |
| Wrapper `1504:57173` | each variant = one instance of the Small control (R3-0 §14) | ✅ **documentation alias of Small — no separate CSS** |

---

## 5. R3-0 — Evidence completion (read-only Figma inspection, before coding)

Read-only operations only (`get_design_context` with screenshot excluded, `get_variable_defs`, `get_metadata`). No downloads, no writes. Results appended to the component specs with dated notes.

| # | Component | Nodes | Operation | Resolves |
|---|---|---|---|---|
| 1 | Button sizes | `887:339`, `344`, `354`, `359`, `369`, `374`, `384` | design_context ×7 | padding/gap 26–52 |
| 2 | Button Secondary Default | `887:664` | design_context | default border width |
| 3 | Button focus widths | `887:1084`, `887:1384`, `887:1684`, `887:1984` | design_context ×4 | focus border width |
| 4 | Button Loading dots | `887:2163` | design_context | dot colour |
| 5 | Gradient states @40 | `1153:3621`, `3631`, `3641`, `3651`, `3661` | design_context ×5 | state paints/borders/shadows |
| 6 | Gradient sizes | `1153:3521`, `1153:3771`, `1153:3871` | design_context ×3 | padding/gap/radius/type per size |
| 7 | Input sizes (Outline, R8) | `1066:37999`, `38179`, `38269`, `38359` | design_context ×4 | padding per size |
| 8 | Input Outline states | `1066:38989`, `39439`, `40339` | design_context ×3 | element mapping |
| 9 | Input Filled states | `1066:43333`, `41633`, `42483`, `42058`, `42908` | design_context ×5 | element mapping |
| 10 | Checkbox sizes | `1504:53311`, `1504:54091` | design_context ×2 | Small/Large geometry |
| 11 | Checkbox states/glyphs | `1504:53761`, `1504:53819`, `1504:53867`, `1504:53703` | design_context ×3 + metadata ×1 | indeterminate, borders, check glyph |
| 12 | Checkbox layouts | `1504:53731`, `1504:53691` | design_context ×2 | Right / Top layouts |
| 13 | Radio | `1504:52373`, `1504:52997`, `1504:52738`, `1504:52686`, `1504:52712`, `1504:52676` | design_context ×5 + metadata ×1 | sizes, borders, selected geometry, layouts |
| 14 | Toggle | `1504:54472`, `1504:54772`, `1504:54487`, `1504:54787`, `1504:54637`, `1504:54697`, `1504:54727`, `1504:54624`, `1504:55717`, `1504:55672` | design_context ×9 + metadata ×1 | sizes, Off colours, Focus/Pressed Off, geometry, layouts |
| 15 | Wrapper | `1504:57174`, `57176`, `57178` | design_context ×3 | distinct styling? |

Budget: **60 read-only calls** (design_context 57, metadata 3; variable_defs only if a binding is ambiguous). Flattened vectors (Radio dot, Toggle thumb, check glyph) may remain opaque to these tools; if so, the remaining options are (a) design-owner geometry spec or (b) explicitly approved read-only SVG export via `download_assets` (D-27).

**Outcome (2026-11-19):** all 15 groups inspected — **79 read-only calls** (`get_design_context` 41, `get_variable_defs` 18, `get_metadata` 20; counts verified from the session transcript). Overrun vs 60: per-element `get_variable_defs` where `get_design_context` returned images (Loading dots, Radio, Toggle). No writes, downloads, screenshots or `create_session`. Results: `docs/figma-audit/r3-0-evidence.md` §16.

---

## 6. Build order & acceptance

| Step | Work | Acceptance |
|---|---|---|
| R3-0 | Evidence completion (§5) | ✅ Done — every gap resolved or escalated (§7) |
| **R3-0a** | **R1 token addendum**: add the 7 Loading colour variables (`Secondary/Content/Loading` `#004feb`, `Secondary/Background/Loading` `#fafcff`, `Secondary-Grey/Content/Loading` `#1f242e`, `Secondary-Grey/Background/Loading` `#fafcff`, `Tertiary/Content/Loading` `#004feb`, `Tertiary Grey/Content/Loading` `#1f242e`, `Link/Content/Loading` `#004feb`) to `tokens.json` + `component-tokens.css` + mapping | 457 → **464** tokens; R1/R2 fixtures updated and PASS; no existing value changed |
| R3-1 | Button (All Buttons) | Fixture: computed height, radius, padding, gap, typography, colours for 6 types × 6 states × 12 sizes = token/evidence values; focus widths |
| R3-2 | Button (gradient) | Sizes 24/32/40/48/56 × states; per-size gradient angles. Sizes 26/28/36/42/46/52 deferred until inspected |
| R3-3 | Input Outline & Filled | 325 variants: sizes, radii, state colours, typography |
| R3-4 | Checkbox, Radio | Sizes, states, layouts; native keyboard |
| R3-5 | Toggle | Sizes, states, geometry |
| R3-6 | Showcase `showcase/components/*.html` + `tests/fixtures/r3-*-check.html` + checklist §7 | All fixtures PASS; R1 (457) and R2 fixtures still PASS |

Visual-parity references: optional `get_screenshot` per component set (read-only render, saved to `docs/figma-audit/screenshots/`) — requires explicit approval because it saves rendered images locally.

---

## 7. Readiness

| Part | Status |
|---|---|
| Architecture, mapping rules, file structure, semantics (B-01 approved) | **Ready** |
| Button (All Buttons) — 12 sizes, 6 types, all states incl. Loading | **Ready after R3-0a** (7-token addendum) |
| Button (gradient) sizes 24 / 32 / 40 / 48 / 56, all states | **Ready** |
| Button (gradient) sizes 26 / 28 / 36 / 42 / 46 / 52 | **Not ready** — uninspected (read-only inspection, ~6 calls; no owner decision needed) |
| Input Outline & Filled — all sizes, radii, states | **Ready** |
| Checkbox — sizes, borders, states, Right/Top layouts | **Ready**, except check / remove **glyph** (D-27) |
| Radio — sizes, dot geometry, colours, Unselected, layouts | **Ready**, except selected **ring stroke width** |
| Toggle — sizes, thumb geometry & travel, colours, labels | **Ready**, except **track radius**, **thumb stroke width**, **Focus Off / Pressed Off stroke element & width** |
| Alignment=Bottom (Checkbox / Radio / Toggle) | **Not ready** — uninspected (read-only, ~3 calls) |
| Selection Controls wrapper | **Ready** — documentation alias of Small, no CSS |

### Remaining items

| ID | Item | Type | Affects |
|---|---|---|---|
| D-27 (narrowed) | Check & indeterminate glyph geometry/colour; Radio ring stroke width; Toggle thumb stroke width, track radius, Focus/Pressed Off stroke width — **not readable** by `get_design_context` / `get_metadata` / `get_variable_defs` (rendered as images) | **Owner decision**: supply values, or approve read-only SVG export (`download_assets`) of these nodes | Checkbox, Radio, Toggle |
| D-20 | Focus + Checked/Selected | **Recommendation applied, not a confirmed Figma specification**: preserve checked appearance + apply focus treatment (§2.6). Owner may override. | Checkbox, Radio |
| R3-0b | Gradient sizes 26/28/36/42/46/52; Alignment=Bottom | Further read-only inspection (≈9 calls) — needs go-ahead | Button (gradient), selection controls |
| R3-0a | 7 Loading tokens | R1 addendum (evidence complete) | Button |
| ~~B-01~~ | Native semantics | ✅ **Approved 2026-11-19** | — |

Not blocking R3 CSS: D-12/D-13 (icons → slots), D-19 (compat tokens used as bound), D-22/D-26 (reproduced and flagged), D-09 (radius 6/10 reproduced and flagged).


---

## 8. Progress (2026-11-19)

| Step | Status | Validation |
|---|---|---|
| R3-0a token addendum | ✅ Done: 457 → 464; no existing value changed | R1 static PASS 464/464; browser `r1-token-check` PASS 464; regression diff: 0 changed or removed |
| R3-0b inspections | ✅ Gradient sizes 26/28/36/42/46/52; gradient angle rule (§18.1); Alignment=Bottom = `flex-end`; Button borders, Loading geometry, Secondary Grey Hover raw border (evidence §17–§21) | 19 additional read-only calls |
| R3-1 Button | ✅ `src/components/button/` (css, html, README); showcase `showcase/components/button.html` | `r3-button-check.html` PASS: 432 variants, 9,964 checks, 0 failures; R3 static PASS; R1/R2 PASS |
| R3-0c gradient inspections | ✅ 34 read-only `get_design_context` calls (32 planned, plus 24 Disabled and 56 Pressed, which had never been inspected); all 55 variants now inspected (evidence §22) | GB-3 resolved: only size 24 Focus differs (Label XSmall Semibold 12/17) |
| R3-2 Button (gradient) | ✅ `src/components/button-gradient/` (css, html, README); showcase `showcase/components/button-gradient.html` | `r3-button-gradient-check.html` PASS: 55 variants, 1,863 checks, 0 failures; mutation test caught 3/3; R3 static PASS; R1/R2/R3-1 PASS |

Validator changes: the R2 fixture and validator now apply the "no focus rules" and "exactly 10 imports" invariants to tokens and base only. Later imports must be `components/*` in `annachy.components`.
| R3-0d Input verification | ✅ 18 read-only calls (2 server errors retried): all radii in both sets, Filled sizes 46/54/56, 7 cross-combinations (evidence §23) | Model verified: State → colours; Size → height; Radius → corner. Radius/6 and Radius/10 are Figma variables without R1 tokens (component-local) |
| R3-3 Input (Outline & Filled) | ✅ `src/components/input/` (css, html, README); showcase `showcase/components/input.html` | `r3-input-check.html` PASS: 325 variants, **11,952 checks**, 0 failures (Disabled behaviour, precedence and radius checks added; two precedence bugs fixed with `:where()`); 5 mutation tests caught; IN-13 / A38 recorded as a confirmed a11y issue |
| R3-4 Checkbox | ✅ `src/components/checkbox/` (css, js, html, README); showcase `checkbox.html` | `r3-checkbox-check.html` PASS: 126 variants, 3,108 checks, 0 failures; 4 mutation tests caught; glyph slot empty (D-27) |
| R3-5 Radio | ✅ `src/components/radio/` (css, html, README); showcase `radio.html` | `r3-radio-check.html` PASS: 108 variants, 2,423 checks, 0 failures; 3 mutation tests caught; ring not drawn (D-27) |
| R3-6 Toggle | ✅ `src/components/toggle/` (css, html, README); showcase `toggle.html` | `r3-toggle-check.html` PASS: 180 variants, 4,904 checks, 0 failures; 4 mutation tests caught; track radius and strokes not drawn (D-27); TG-1 derived track fills; A39 1.04:1 |
| Selection Controls wrapper | ✅ documented as an alias of the Small variants (`src/components/selection-controls/README.md`), no CSS | — |
| R3-0e/f/g evidence | Checkbox ×5, Radio ×10, Toggle ×28 read-only calls (§24–§26) | Running total 193 read-only calls; no writes, exports or downloads |
