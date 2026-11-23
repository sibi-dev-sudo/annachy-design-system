# Component Spec — Button

| Item | Value |
|---|---|
| Page | › ① Button ✓ `375:10891` |
| Component sets | **All Buttons** `887:2492` (432 variants) · **Button** (gradient) `1153:3370` (55 variants) |
| Location | Section "Core Button Components" `1563:60424` › "Main -Components Set" `1564:61398` |
| Duplicate | EMPTY PAGE `479:4` › `1590:19040` — same 432 variant names, **360 differ in size** (e.g. Primary/24 72 px vs 104 px wide) — divergent copy (`raw/archive-diff.md`) |
| Method | `get_design_context` on 10 variants; `get_variable_defs` on 32 variants; layer sizes from `get_metadata`. Read-only. |
| Evidence | **[APPLIED]** = returned by `get_design_context`; **[BOUND]** = variable returned by `get_variable_defs`; **[META]** = `get_metadata` dimensions |

---

## 1. All Buttons `887:2492`

### 1.1 Properties

| Property | Type | Values / default |
|---|---|---|
| `Type` | Variant | Primary, Secondary, Secondary Grey, Tertiary, Tertiary Grey, Link |
| `State` | Variant | Default, Hover, Focus, Pressed, Disabled, Loading |
| `Size` | Variant | 24, 26, 28, 32, 36, 38, 40, 42, 46, 48, 52, 56 |
| `label` | Text | "Button" |
| `showLabel` | Boolean | true |
| `showLeftIcon` | Boolean | true |
| `showRightIcon` | Boolean | true |

6 × 6 × 12 = 432 variants, complete. Loading variants have no label/icon properties (dots only).

### 1.2 Anatomy [APPLIED]

`[left icon] [label] [right icon]` — horizontal auto-layout, `justify-content: center`, `align-items: center`, `overflow: hidden` (clip). Icon instance: **Home/Home 54** (`1777:9468`), `Icon Size=S, Style=Outline`, **20 × 20 at every button size**.

Loading: label/icons replaced by "Loading Dots" frame **28 × 6** (`887:2163`) containing 3 ellipses 6 × 6 at x = 0 / 11 / 22 (`887:2164–2166`), same padding/background as Default.

### 1.3 Size scale

| Size | Height var [BOUND] | Radius var [BOUND] | Padding (x / y) | Gap | Text style [BOUND] | Font size / LH | Default width (Primary) [META] |
|---|---|---|---|---|---|---|---|
| 24 | `Height/24` = 24 | `Radius/4` = 4 | 10 / 4 [APPLIED] | 4 [APPLIED] | Body XS — Semibold (vars `Body/XXS-Semibold`) | 12 / 18 | 104 |
| 26 | `Height/26` = 26 | `Radius/4` | [not inspected] | — | Body XS — Semibold | 12 / 18 | 104 |
| 28 | `Height/28` = 28 | `Radius/4` | [not inspected] | — | Body S - Semi (vars `Body/XS-Semibold`) | 14 / 18 | 110 |
| 32 | `Height/32` = 32 | `Radius/8` = 8 | 10 / 12 [APPLIED] | 4 [APPLIED] | Body S - Semi | 14 / 18 | 110 |
| 36 | `Height/36` | `Radius/8` | [not inspected] | — | Heading/H7 — Semibold | 16 / 18 | 124 |
| 38 | `Height/38` | `Radius/8` | [not inspected] | — | H7 — Semibold | 16 / 18 | 128 |
| 40 | `Height/40` | `Radius/8` | 16 / 12 [APPLIED] | 6 [APPLIED] | H7 — Semibold | 16 / 18 | 132 |
| 42 | `Height/42` | `Radius/12` = 12 | [not inspected] | — | H7 — Semibold | 16 / 18 | 132 |
| 46 | `Height/46` | `Radius/12` | [not inspected] | — | Heading/H6 — Semibold (LH var `Line Height 2`) | 18 / 20 | 142 |
| 48 | `Height/48` | `Radius/12` | 16 / 18 [APPLIED] | 8 [APPLIED] | H6 — Semibold | 18 / 20 | 142 |
| 52 | `Height/52` | `Radius/12` | [not inspected] | — | Heading/H5 — Semibold | 20 / 24 | 152 |
| 56 | `Height/56` | `Radius/12` | 20 / 20 [APPLIED] | 8 [APPLIED] | H5 — Semibold | 20 / 24 | 156 |

Height is fixed by `Height/N` variables; vertical padding + line-height exceeds height at several sizes (e.g. 40: 12+18+12 = 42 > 40; 56: 20+24+20 = 64 > 56) — content is centred and clipped, so **vertical padding is nominal** and height governs. [DERIVED]

Font: `Font Family/Sans Serif` = Proxima Nova, `Weight/Semibold` = 600, letter-spacing 0 [BOUND].

Widths of Focus variants are 4 px wider than Default (e.g. 136 vs 132 at size 40) [META] — focus border is added outside content.

### 1.4 State colours (Size 40) [BOUND unless noted]

| Type | Default | Hover | Focus | Pressed | Disabled |
|---|---|---|---|---|---|
| **Primary** bg | `Primary/Background/Default` `#004feb` | `…/Background/Hover` `#003fbc` | `…/Background/Focus` `#004feb` + **2 px border** `…/Border/Focus` `#003fbc` [APPLIED] | `…/Background/Pressed-Active` **`#3372ef`** | `…/Background/Disabled` `#bfc4cf` |
| Primary text/icon | `…/Content/Default` `#fafcff` | same | same | same | `…/Content/Disabled` `#fafcff` |
| **Secondary** bg | none (transparent) | `…/Background/Hover` `#f3f7ff` | none | `…/Background/Pressed-Active` **`#e8f0ff`** | none |
| Secondary border | `…/Border/Default` `#004feb` | `#004feb` | **2 px** `…/Border/Default` `#004feb` [APPLIED] | `#004feb` | `…/Border/Disabled` `#bfc4cf` |
| Secondary text | `…/Content/Default` `#004feb` | same | same | same | `…/Content/Disabled` `#bfc4cf` |
| **Secondary Grey** bg | none | `…/Background/Hover` `#f6f7f9` | none | `…/Background/Pressed-Active` `#dcdfe5` | none |
| Secondary Grey border | `…/Border/Default` `#bfc4cf` | **none bound** | `…/Border/Focus` `#004feb` | **`…/Border/Disabled` `#dcdfe5`** | `…/Border/Disabled` `#dcdfe5` |
| Secondary Grey text | `…/Content/Default` `#1f242e` | same | same | same | `…/Content/Disabled` `#bfc4cf` |
| **Tertiary** bg | none | `…/Background/Hover` `#f3f7ff` | none | `…/Background/Pressed-Active` `#e8f0ff` | none |
| Tertiary border | none | none | `…/Border/Focus` `#004feb` | none | none |
| Tertiary text | `…/Content/Default` `#004feb` | same | same | `…/Content/Pressed-Active` `#003fbc` | `…/Content/Disabled` `#bfc4cf` |
| **Tertiary Grey** bg | none | `…/Background/Hover` **`#f3f4f7`** | none | `…/Background/Pressed-Active` **`#e4e7ec`** | none |
| Tertiary Grey border | none | none | `…/Border/Focus` `#004feb` | none | none |
| Tertiary Grey text | `…/Content/Default` `#1f242e` | same | same | same | `…/Content/Disabled` `#bfc4cf` |
| **Link** bg | none | none | none | none | none |
| Link border | none | none | `…/Border/Focus` `#004feb` | none | none |
| Link text | `…/Content/Default` `#004feb` | **same — no change** [APPLIED: no underline, no bg] | same | `…/Content/Pressed-Active` `#003fbc` | `…/Content/Disabled` `#bfc4cf` |

Variable paths are `Brand/Button/<Type>/…`; note the Type segment spelling varies: `Secondary-Grey` (hyphen) vs `Tertiary Grey` (space).

Colours **not in any palette scale** (`02-color.md`): `#e8f0ff`, `#f3f4f7`, `#e4e7ec`. Primary Pressed `#3372ef` (= Blue/400) is *lighter* than Hover `#003fbc` (= Blue/600).

Focus border width for Tertiary/Tertiary Grey/Link not confirmed (only variable bound; width not inspected) — Primary and Secondary confirmed 2 px.

### 1.5 Effects

No shadows on All Buttons variants [APPLIED: none present on inspected variants].

---

## 2. Button (gradient) `1153:3370`

Figma description [EXTRACTED]: *"55 auto-layout button variants: 11 sizes × Default, Hover, Focus, Pressed, Disabled. Fill, stroke and shadow are native on each button component… Label and both icon visibility/swap properties remain."*

| Property | Values |
|---|---|
| `Size` | 24, 26, 28, 32, 36, 40, 42, 46, 48, 52, 56 (**no 38**) |
| `State` | Default, Hover, Focus, Pressed, Disabled (**no Loading**) |
| `label` / `labelText` / `leftIcon` / `rightIcon` | Text / Boolean ×3 (names differ from All Buttons: `showLabel`, `showLeftIcon`, `showRightIcon`) |

Size 24 Default `1153:3371` [APPLIED]:

| Attribute | Value |
|---|---|
| Background | `linear-gradient(22.57deg, Brand/Gradient/Color 1 #3a79f7 13.4%, Brand/Gradient/Color 2 #1746a2 86.6%)` |
| Border | 1.5 px `Brand/Blue/300` `#99b9f7` |
| Radius | **4 px raw** (not a variable) |
| Padding / gap | 8 px horizontal / 4 px gap; height `Height/24` |
| Shadow | `-2px 4px 2px rgba(23,25,28,0)`, `-1px 3px 1px rgba(23,25,28,.02)`, `-1px 2px 1px rgba(23,25,28,.08)`, `0 1px 1px rgba(23,25,28,.13)` (raw, not a style) |
| Text | Body XS — Semibold 12/18, `Brand/Base/White` `#fafcff` |
| Width | 100 px (vs 104 for All Buttons Primary 24) [META] |

Other sizes/states not inspected individually; states assumed to differ in paint only per description [unverified].

---

## 3. Dependencies

| Depends on | Node |
|---|---|
| Icon Home/Home 54 (Outline, size S 20 px) — part of icon source **S5 — Annachy Icons File** (`Icon Size XS/S/M/L/XL`, Outline + Filled) *[Naming standardised to S5 on 2026-11-19; see `06` §1 for S1–S6 labels.]* | `1777:9468`, instance `1777:12415` |
| Loading Dots vector | `887:2163` |
| Text styles: Body XS — Semibold, Body S - Semi, Heading/H7 — Semibold, H6 — Semibold, H5 — Semibold | bound |
| Variables: `Height/{24…56}`, `Radius/{4,8,12}`, `Brand/Button/*`, `Brand/Gradient/*`, `Brand/Blue/300` | bound |

Used by: Selection Controls docs (`All Buttons` instances `1767:22896`, `1778:27631`, `1464:10381`), PDP screens (`Button` instances `1218:18601`, `1218:18627`).

---

## 4. Findings

| # | Finding | Severity |
|---|---|---|
| B1 | **Link Hover is visually identical to Link Default** (no colour, underline or background change). | High (a11y/UX) |
| B2 | **Secondary Focus differs from Default only by border width (1→2 px?, same colour).** Default border width not confirmed. Weak focus indication. | High (a11y) |
| B3 | Secondary Grey **Pressed** binds `Border/Disabled`; **Hover** has no border bound. Likely mis-binding. | Medium |
| B4 | Primary Pressed `#3372ef` is lighter than Hover `#003fbc` — inverted pressed feedback vs Tertiary/Link (pressed darker). | Medium |
| B5 | Off-palette state colours `#e8f0ff`, `#f3f4f7`, `#e4e7ec`. | Medium |
| B6 | Icon fixed at 20 px for all sizes (20 px icon inside 24 px button). | Medium |
| B7 | Text-style names don't match their variables: "Body XS — Semibold" → `XXS-Semibold` vars; "Body S - Semi" → `XS-Semibold` vars; H6 uses `Line Height 2`. | Low |
| B8 | 12 sizes (incl. odd 26, 38, 42, 46, 52) — large scale; gradient set has 11 (no 38). | Low |
| B9 | Gradient button uses raw radius 4 and raw shadow; boolean property names differ from All Buttons. | Low |
| B10 | Radius is bound to `Radius/4/8/12` variables here — contrary to the Radius page, which says Button = 8 (one table) or 12 (other). Actual: size-dependent 4 / 8 / 12. | Info (resolves L5 in practice) |
| B11 | Button text styles **are** bound to Figma text styles and typography variables — corrects `03-typography.md` T6 (specimens unbound, components bound). | Info |
| B12 | Not inspected: padding/gap for sizes 26, 28, 36, 38, 42, 46, 52; focus-border width for Tertiary/Grey/Link; gradient button states. | Gap |


## R3-0 update (2026-11-19)

Read-only inspection; full evidence with node IDs in `../r3-0-evidence.md`. Original findings above are preserved.

- **B12 resolved:** padding/gap for all sizes (§1): 26 10/4·4, 28 10/8·4, 36 12/10·6, 38 14/10·6, 42 16/12·6, 46 16/16·8, 52 18/18·8.
- Secondary Default border **1px**; Focus border **2px** for all six types (§2–§3).
- Loading dots use per-type `Content/Loading`; Secondary / Secondary Grey use `Background/Loading` `#fafcff`. **7 Loading variables are not in R1** → token addendum R3-0a (§4).
- Gradient: states @40 and sizes 32/48/56 recorded (§5–§6); CSS gradient angle is size-dependent; size 48 binds Subheading L-Semibold 18/25. Gradient sizes 26/28/36/42/46/52 **still uninspected**.
