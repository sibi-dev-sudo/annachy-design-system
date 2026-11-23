# 13 — Global Token Decisions: Evidence Review (D-01 … D-08)

| Item | Value |
|---|---|
| Purpose | Detailed evidence for the eight global decisions that gate R1 (Tokens) and R2 (Base). |
| Basis | Local audit files only. **No Figma access. No tokens or implementation files created or changed. No decisions made.** |
| Evidence classes | **DOC** = documentation evidence (values written or shown on Foundations/doc pages: text layers, specimens, doc frames). **BIND** = actual component bindings (`get_variable_defs` / `get_design_context` on component variants). **DERIVED** = reasoning over DOC/BIND. |
| Recommendation rule | An option is recommended **only** where BIND evidence clearly supports it. All items still require design-owner confirmation (**⚑ OWNER**). |

Source abbreviations: `02` = `02-color.md`, `03` = `03-typography.md`, `04` = `04-spacing-layout.md`, `05` = `05-elevation-effects.md`, `07` = `07-component-inventory.md`, `11` = `11-dependencies-and-sources.md`, `12` = `12-design-decision-review.md`, `C/<name>` = `components/<name>.md`.

---

## D-01 · Canonical colour naming scheme and value conflicts

### 1. Naming conventions observed

| Convention | Pattern | Example | Where | Class |
|---|---|---|---|---|
| **N1 Brand Title Case** | `Brand/<Group>/<Step or Role>` | `Brand/Blue/500`, `Brand/Text/Primary`, `Brand/Button/Primary/Background/Hover` | Colour Usage `1557:31595`; **all components** | DOC + BIND |
| **N2 lowercase kebab** | `<group>/<role>` or `brand/<group>/<step>` | `text/primary`, `brand/blue-grey/300`, `brand/base/gradient-start` | Brand Colours `1557:23523`, Typography `1557:39451`/`1557:44867`, Grid `1558:51715`, Radius `1561:56909` | DOC only |
| **N3 icon semantic (bare)** | `<state>` | `brand`, `disabled`, `error`, `success`, `warning` | Icon pilot `1106:12812`; **Input Error/Success/Filled states** | DOC + BIND |
| **N4 Supporting** | `Supporting/<Status>/<Step>` | `Supporting/Error/500` | `1557:31595` | DOC only (duplicates N1 values) |
| **N5 spaced** | `Brand / Blue-Grey / 600` | — | Shadow docs `1561:57814` | DOC only |
| **N6 foreign** | `surface-bg`, `border-default`, `Colors/alpha/50`, `Text/Neutral/*`, `--sds-*` | — | Checkbox/Radio (BIND); effect docs (DOC) | DOC + BIND |

Note on tool output: `get_design_context` renders every variable as a lower-cased CSS custom property (e.g. `var(--brand/button/primary/background/default)`), while `get_variable_defs` returns the real Figma name (`Brand/Button/Primary/Background/Default`). This is **MCP output normalisation, not a seventh scheme** [DERIVED from identical values on the same nodes, e.g. `887:364`].

### 2. Value conflicts (same role, different value)

| # | N2 (lowercase) | Value | N1 (Brand) | Value | N2 node(s) | N1 node | Source |
|---|---|---|---|---|---|---|---|
| 1 | `text/primary` | `#000204` | `Brand/Text/Primary` | `#0b0c0f` | `1557:23523`, `1557:44867` | `1557:31595` | `02` §2 |
| 2 | `text/secondary` | `#030a14` | `Brand/Text/Secondary` | `#555d6d` | `1557:39451`, `1557:44867` | `1557:31595` | `02` §2.1 |
| 3 | `text/tertiary` | `#181b21` | `Brand/Text/Tertiary` | `#707a8f` | `1557:39451`, `1557:44867` | `1557:31595` | `02` §2.1 |
| 4 | `brand/blue-grey/300` | `#1f242e` | `Brand/Blue-Grey/300` | `#bfc4cf` | `1557:23523` | `1557:31595` | `02` §2 |
| 5 | `brand/base/gradient-start` | `#3a6ff7` | `Brand/Gradient/Color 1` · `Brand/Button/Gradient Start` | `#3a79f7` | `1557:23523` | `1557:31595` | `02` §2 |
| 6 | `brand/base/black` | `#0b0d0f` | `Brand/Base/Black` | `#0b0c0f` | `1557:39451` | `1557:31595` | `02` §2.1 |
| 7 | `background/secondary` | `#f5f9ff` | `Brand/Background/Secondary` | `#f6f7f9` | `1558:51715` | `1557:31595` | `04` L11 |
| 8 | `icon/primary` | `#000204` | `Brand/Icon/Primary` | `#0b0c0f` | `1561:56909`, `1561:57340` | `1557:31595` | `04` L11 |

Consistent pairs (same value, two names): `text/inverse` = `background/primary` = `background/light` = `Brand/Base/White` `#fafcff`; `brand/blue-primary/100` = `Brand/Blue/100` `#e6edfd`; `brand/base/gradient-end` = `Brand/Gradient/Color 2` `#1746a2`.

N2-only roles with no N1 equivalent: `border/strong #030a14`, `border/subtle #ebf2ff`, `background/inverse #0b0d0f`.

Raw (unbound) use of an N2 value in a component: Input/Outline Focused border **`#3a6ff7`** (= N2 `brand/base/gradient-start`) at `1066:38544` — the only N2 value found in a component, and it is not bound to a variable [BIND via `get_design_context`].

### 3. Component bindings (BIND)

| Component | Schemes bound | Evidence |
|---|---|---|
| Button (All Buttons, gradient) | N1 only (`Brand/Button/*`, `Brand/Gradient/*`, `Brand/Blue/300`, `Brand/Base/White`) | `C/button` §1.4, §2 |
| Input / Outline | N1 (`Brand/Blue-Grey/*`, `Brand/Base/*`, `Brand/Blue-Black/500`) + **N3** (`error`, `success`) + raw `#3a6ff7` | `C/input` §3.1 |
| Input / Filled | N1 + **N3** (`brand`, `error`, `success`) | `C/input` §3.2 |
| Dropdown Menu/Item | N1 only (incl. Dark mode values) | `C/dropdown` §3–5 |
| Checkbox / Radio | N1 + **N6** (`surface-bg`, `border-default`, `Colors/alpha/50`) | `C/checkbox` §4, `C/radio` §4 |
| Toggle | N1 only | `C/toggle` §3 |
| Tooltip | N1 only (`Brand/Base/Black/White`) | `C/tooltip` §3 |

**N2 is never bound by any inspected component.** N1 is bound by every component and is the only scheme with an observed Dark mode (`C/dropdown` §5).

### 4. Contradictions between earlier reports

| Report | Statement | Correction |
|---|---|---|
| `02` C1, `12` D-01 headline | "six value conflicts" | **Eight** conflicts (rows 7–8 recorded in `04` L11 but not counted in `02`). **Applied 2026-11-19** (`02` C1, §2.2; `08` INC-04; `10`; `12`). |
| `02` §3 C7 | No primitive/semantic separation | Still accurate; N1 mixes primitives (`Brand/Blue/500`), semantics (`Brand/Text/*`) and component tokens (`Brand/Button/*`) under one root. |

### 5. Recommendation

**Evidence supports N1 (`Brand/*`) as the canonical scheme** — sole scheme bound by all components and the only one with Dark-mode values. ⚑ OWNER must confirm, and additionally decide:
- (a) whether N2 is deprecated; (b) whether N3 icon-state names are kept as a separate scheme (bound by Input); (c) the replacement for raw `#3a6ff7` in Input focus; (d) N6 removal (→ D-19).

---

## D-02 · `Brand/Error/700 = #9d4520`

### Evidence

| Step | Brand/Error (DOC, `1557:31595`) | Brand/Warning (DOC) |
|---|---|---|
| 100 | `#fff7f6` | `#fff8f1` |
| 200 | `#ffe6e2` | `#ffddb3` |
| 300 | `#ffc1b6` | `#ffbd6b` |
| 400 | `#ff9c8c` | `#f88f33` |
| 500 | `#ff614e` | `#f26e2d` |
| 600 | `#e72b23` | `#b9512e` |
| **700** | **`#9d4520`** | **`#9d4520`** |
| 800 | `#7a2515` | `#6c2e18` |
| 900 | `#521e11` | `#4c2213` |

- `Supporting/Error/*` exposes only 100/500/800 — 700 not duplicated there (DOC).
- BIND: **No component binds `Brand/Error/700`.** Components bind Error-family colours only via N3 `error` = `#e72b23` (= Error/600) in Input (`1066:39889`, `1066:42483`).
- DERIVED: 700 breaks the red hue progression (600 red → 700 orange-brown → 800 red) and equals Warning/700 exactly.

### Contradictions
None between reports; `08` classes it as suspected (SUS-01), not confirmed — consistent.

### Recommendation
**No value can be recommended** — the correct 700 cannot be derived from the file. Evidence suggests a copy error. ⚑ OWNER: confirm intent and supply value if incorrect.

---

## D-03 · Dark theme scope for v1

### Documentation evidence (DOC)

| Evidence | Node | Source |
|---|---|---|
| Icon pilot doc text: "Style × Size variants · semantic state variables · **Light/Dark modes**" | `1106:12812` | `06` §2 |
| Dropdown property `Theme = Light / Dark` (24 Menu + 20 Item Dark variants) | `1451:25521`, `1451:25092` | `C/dropdown` §1 |
| Tooltip property `Mode = dark / light` (40 dark variants) | `1448:16825` | `C/tooltip` §1 |
| Legacy "check box" set has `Mode=Light` only | `1464:10379` | `raw/variant-matrices.md` |

### Component bindings (BIND) — Dark values observed

| Variable | Light | Dark | Node |
|---|---|---|---|
| `Brand/Background/Secondary` | `#f6f7f9` | `#181b21` | `1451:25265` |
| `Brand/Text/Primary` | `#0b0c0f` | `#fafcff` | `1451:25265` |
| `Brand/Border/Primary` | `#bfc4cf` | `#171e2a` | `1451:25265` |
| `Brand/Text/Tertiary` | `#707a8f` | `#707a8f` | `1451:25265` |
| `Brand/Blue/500` | `#004feb` | `#004feb` | `1451:25265` |
| `Brand/Base/White` | `#fafcff` | `#fafcff` | `1451:25265` |

Tooltip dark does **not** use variable modes — it binds raw `Brand/Base/Black` bg + `Brand/Base/White` text (`1429:16132`).

Not observed: Dark values for Button, Input, Checkbox, Radio, Toggle (no Dark variants exist for these components) [DOC: variant matrices]; full Dark value set for the collection [INACCESSIBLE — collection modes not returned by tools].

### Contradictions between reports

| Report | Statement | Status |
|---|---|---|
| `02` original C9 (Phase 3) | "No dark-mode colour set was returned" | **Superseded** in Phase 4 — `02` C9 corrected. |
| `02` §6 Limitations | "does not return collection names, mode names" | Still accurate (values per mode only visible via Dark variants). |

### Recommendation
**None — product-scope decision.** Evidence shows Dark mode is *partially* designed (Dropdown, Tooltip only). ⚑ OWNER: (a) Dark in v1 or later; (b) if v1, supply the full Dark value set or authorise read-only collection from Dark variants; (c) whether Button/Input/Selection controls need Dark designs.

---

## D-04 · Canonical type scale; H3 and Body S

### Documentation evidence (DOC)

| Scale | Node | Styles | Model | Notes |
|---|---|---|---|---|
| **Scale A** "Typography System" | `1557:39451` | 28 rows (header says 26) | Mobile + Desktop size/LH; 5 weights | Product examples ("Add to cart", "Discover your style"); usage rules |
| **Scale B** "Typography Documentation" | `1557:44867` | 11 styles | Single size/LH; 8 weights | Generic Proxima Nova specimen ("VERSION 2.0", "© 2025"); Display XL 72/80 … Label 11/14 |

Comparison A vs B (size / line-height):

| Style | Scale A Mobile | Scale A Desktop | Scale B | Relationship |
|---|---|---|---|---|
| H1 / Heading 1 | 32 / 38 | 48 / 58 | 48 / 56 | Size = A Desktop; LH differs |
| H2 / Heading 2 | 28 / 36 | 40 / 48 | 40 / 48 | **= A Desktop** |
| H3 / Heading 3 | 26 / 34 (Bold) · 26 / 30 (Semibold) | 36 / 42 | 32 / 40 | Conflict |
| Body L / Body Large | 18 / 27 | 18 / 27 | 20 / 28 | Conflict |
| Body M / Body | 16 / 24 | 16 / 24 | 16 / 24 | Equal |
| Body S / Body Small | 14 / 20 | 14 / 21 | 14 / 20 | = A Mobile |
| Labels | 12–18 | 12–18 | Label 11 / 14 | Conflict |
| Captions | 8–11 | 8–11 | Caption 12 / 16 | Conflict |
| Display XL / L, Subtitle | — | — | 72/80 · 56/64 · 24/32 | B only |

Specimen node `1558:48865` labelled H1 renders **36 px Bold** (matches neither) [BIND via `get_design_context`, but it is a doc specimen, not a component].

### Component bindings (BIND) — text styles and variables

| Component text style (Figma name) | Variable path | Bound value | Scale A row | Mobile / Desktop match | Used by |
|---|---|---|---|---|---|
| Typography/Subheading & Body/**Body XS — Semibold** | `Subheading & Body/Body/XXS-Semibold/*` | 12 / 18, 600 | Body XS — Semibold 12/18 | equal | Button 24–26, gradient Button |
| Typography/Subheading & Body/**Body S - Semi** | `Subheading & Body/Body/XS-Semibold/*` | 14 / 18, 600 | Body S (Semibold) 14/18 `1558:49069` | equal | Button 28–32, Tooltip |
| Typography/Subheading & Body/**Body S — Regular** | `Subheading & Body/Body/S/*` | 14 / 20, 400 | Body S (Regular) 14/20 `1558:49021` | **Mobile** (Desktop LH 21) | Input, Checkbox, Radio, Toggle |
| Body M — Medium | `Body/M-Medium/*` | 16 / 24, 500 | Body M — Medium | equal | Input value |
| Body M — Regular | `Body/M/*` | 16 / 24, 400 | Body M | equal | Dropdown search |
| Heading/**H7 — Semibold** | `Heading/H7/Semibold/*` | 16 / 18 | H7 | **Mobile** (Desktop 20/24) | Button 36–42, Input label |
| Heading/**H6 — Semibold** | `Heading/H6/Semibold/*` (LH var `Line Height 2`) | 18 / 20 | H6 | **Mobile** (Desktop 24/28) | Button 46–48 |
| Heading/**H5 — Semibold** | `Heading/H5/Semibold/*` | 20 / 24 | H5 | **Mobile** (Desktop 28/34) | Button 52–56 |
| Labels & Captions/**Label Small — Medium** | `Label/Small/*` | 14 / 20 | Label Small | equal | Dropdown Item, wrapper |
| Labels & Captions/**Label Medium — Medium** | `Label/Medium/*` | 16 / 21 | Label Medium | **Mobile** (Desktop 16/22) | Checkbox, Radio, Toggle |
| Labels & Captions/**Label XSmall — Regular** | `Label/XSmall/*` | 12 / 17 | Label XSmall | **Mobile** (Desktop 12/18) | Tooltip |

Shared variables: `Font Family/Sans Serif = "Proxima Nova"`, `Weight/Regular|Medium|Semibold` [BIND]. No component binds any Scale B value (Display, Subtitle, Caption 12/16, Label 11/14).

### Findings from the bindings

- **All 11 component text styles match Scale A; none match Scale B** [DERIVED].
- **Body S "duplicate" is not a value conflict:** both rows are in production use — Regular 14/20 (Input, selection controls) and Semibold 14/18 (Button, Tooltip). The issue is **naming** (same name "Body S", style names "Body S — Regular" vs "Body S - Semi", variables `Body/S` vs `Body/XS-Semibold`).
- **H3 duplicate** (Bold 26/34 `1558:48900` vs Semibold 26/30 `1558:48908`): **no component binds either** — no evidence to choose.
- Naming mismatches (style ↔ variable): "Body XS — Semibold" → `XXS-Semibold` vars (the Scale A *XXS* row is 10/15 Medium); "Body S - Semi" → `XS-Semibold` vars; H6 LH variable "Line Height 2".

### Contradictions between earlier reports

| Report | Statement | Status |
|---|---|---|
| `03` T6 | "No text styles / typography variables detected on specimens" → "specimens not bound to text styles" | Accurate for doc specimens; **components are bound** (`C/button` B11, `07` §4). `03` T6 should be read with that correction. **Applied 2026-11-19** (`03` T6, §4.1). |
| `03` T3, `08` INC-14 | "Duplicate style names with different values: … Body S (Regular 14/20 vs Semibold 14/18)" | **Refined:** Body S rows are two distinct, both-used weights — a naming collision, not a value conflict. H3 remains an unresolved duplicate. **Applied 2026-11-19** (`03` T3, `08` INC-14 + INC-57). |
| `03` §6 | Recommends Scale A as candidate | Consistent with bindings. |

### Recommendation

**Evidence supports Scale A (Typography System) as canonical** — every component binding matches it; none matches Scale B. ⚑ OWNER must confirm and decide:
- (a) Scale B status (reference-only?); (b) H3 — which of the two rows (no evidence); (c) whether to rename Body S variants and align style/variable names (`XXS`/`XS` mismatch); (d) the 8 px / 10 px styles against the file's own "Min 12px UI" rule (`09` §4).

---

## D-05 · Mobile → Desktop typography switch point

### Documentation evidence (DOC)

| Evidence | Node | Source |
|---|---|---|
| Scale A provides separate Mobile and Desktop size/LH per style | `1557:39451` | `03` §2 |
| Responsive progression text: Mobile `32 → … → 8`, Desktop `48 → … → 8` | `1557:39451` | `03` §2.3 |
| Rule: "Use the responsive Mobile/Desktop values defined by the system" | `1557:39451` | `03` |
| Design frames: 360 (Mobile), 1440 (Desktop), 1920 (Large) | `1561:56879`, `1561:56902`, `1561:56904` | `04` §1.3 |
| **No switch width documented anywhere** | — | `03`, `04` |

### Component bindings (BIND)

- Wherever Scale A Mobile ≠ Desktop, components resolve to the **Mobile** values in all 6 cases (H7, H6, H5, Body S Regular, Label Medium, Label XSmall) — see D-04 table.
- Components also carry viewport properties with no widths: Dropdown `Platform = Desktop | Mobile` (320 vs 352 wide), Tooltip `Device = Mobile | Desktop`. These change component dimensions, not type size (Dropdown Item text is Label Small 14/20 on both — Mobile/Desktop equal).

### Derived observations

- Typography variables very likely have **Mobile / Desktop modes**, with **Mobile** active where components were inspected. Grid variables on the Desktop layout frame resolved to **Desktop** values (`grid/width 1440`, `1561:56902`). Together these suggest modes are set per frame [DERIVED — mode names not retrievable].
- The switch width is therefore an implementation-time value not present in Figma.

### Contradictions between reports
None. `04` §1.4 and `12` D-05 both record the switch point as missing.

### Recommendation
**None — no width exists in the file.** ⚑ OWNER: supply the switch width (likely tied to D-07) and confirm that Mobile values are the default state.

---

## D-06 · Proxima Nova licence and fallback stack

### Documentation evidence (DOC, `1557:44867` specimen sheet unless noted)

| Evidence | Value |
|---|---|
| Designer / foundry | Mark Simonson / Mark Simonson Studio |
| Licence statement | "Proxima Nova is not an open-source typeface; it is a commercial family…"; "LICENSING: Commercial only (via Mark Simonson Studio and authorized resellers)" |
| Platforms | "Adobe Fonts — INCLUDED"; "MyFonts / Monotype / Fontspring — LICENSED"; "Google Fonts — N/A"; Figma: "Requires a local font install or a licensed web embed" |
| Weights listed | Scale A: Light 300, Regular 400, Medium 500, Semibold 600, Bold 700 (`1557:39451`). Scale B: Thin ~100 … Black 900 (8 weights) |
| Fallback stack | **Not specified** [MISSING] |
| Documentation chrome font | **Montserrat** on Radius page labels (`1561:57345`) — not the product font |

### Component bindings (BIND)

| Variable | Value | Used by |
|---|---|---|
| `Font Family/Sans Serif` | `Proxima Nova` | All components |
| `Weight/Regular`, `Weight/Medium`, `Weight/Semibold` | Regular / Medium / Semibold | All components |
| Bold (700) | via text styles H1–H3/H8 only | **No inspected component** |
| Light (300), Thin, Extrabold, Black | — | **Not used** |

Weights required by inspected components: **400, 500, 600** (700 only if Scale A headings are implemented) [DERIVED].

### Contradictions between reports
`03` lists Scale A as "5 weights"; components use 3 (+ Bold for headings). Not a contradiction — documented scope vs used scope.

### Recommendation
**None — licensing and fallback are owner/procurement decisions.** ⚑ OWNER (legal/procurement): licence route (Adobe Fonts kit vs licensed self-hosted files); ⚑ OWNER (design): fallback stack and whether Light 300 / Bold 700 are needed in v1.

---

## D-07 · Breakpoint ranges, tablet, max content width

### Documentation evidence (DOC)

| Evidence | Values | Node | Source |
|---|---|---|---|
| Grid spec table | Mobile 360 · 4 col · margin 16 · gutter 16; Desktop 1440 · 12 · 120 · 32; Large Desktop 1920 · 12 · 140 · 32 | `1558:55670` | `04` §1.2 |
| Grid overview | "BREAKPOINTS: Mobile, Desktop, Large Desktop"; "LAYOUT BEHAVIOUR: Fixed Margins & Gutters"; "GRID TYPE: Responsive Column Grid" | `1558:55670` | `04` §1.2 |
| Grid spec frames | Overlay colour `#004FEB`, field "24" (unlabelled), Stretch, column width Auto | `1558:51715` | `04` §1.2 |
| Layout frames | 360 × 800, 1440 × 1024, 1920 × 1080 | `1561:56879`, `1561:56902`, `1561:56904` | `04` §1.3 |
| Label error | Mobile grid spec labelled "Desktop" | `1558:51715` | `04` L10 |
| Ranges, tablet, max-width | **Not defined** | — | `04` L2 |

Derived column widths: Mobile 70 px; Desktop 70.67 px; Large 107.33 px (`04` §1.2).

### Variable bindings (BIND)

| Variable | Resolved value | Node |
|---|---|---|
| `grid/width` | 1440 | `1558:51715`, `1561:56902` |
| `grid/height` | 1024 | same |
| `grid/columns` | 12 | same |
| `grid/margin` | 120 | same |
| `grid/gutter` | 32 | same |

Only Desktop values returned; Mobile/Large values exist only as DOC text [INACCESSIBLE: modes].

Component viewport properties without widths: Dropdown `Platform` (Desktop 320 / Mobile 352 wide), Tooltip `Device` (Mobile 182 / Desktop 157 for Text-only), Typography Mobile/Desktop. Patterns use 360, 393 (PDP mobile `1214:11887`), 1440 (PDP desktop `1311:7548`) [DOC].

### Contradictions between reports
- `04` treats mobile as 360; Patterns pages use **393-wide** mobile frames (`01` §2, PDP). Not previously flagged. → mobile design width itself is inconsistent across Foundations (360) and Patterns (393).

### Recommendation
**None — no range values exist.** ⚑ OWNER: define (a) range boundaries between Mobile / Desktop / Large; (b) tablet in or out; (c) max content width; (d) whether 360 or 393 is the reference mobile width.

---

## D-08 · Spacing scale

### Documentation evidence (DOC)
- No Spacing foundation page; no spacing table; no spacing variables returned on any Foundations section (`04` §2).
- Variables `S = 8` and `Radius/S = 8` exist on effect doc pages (`1563:58676`) — names suggest a size scale, but no other steps observed (`05` §3).
- Grid margins/gutters: 16, 32, 120, 140 (DOC grid spec).

### Component bindings (BIND — padding/gap values, all raw px, none bound to variables)

| Component | Node | Padding | Gap |
|---|---|---|---|
| Button 24 | `887:334` | x 10 · y 4 | 4 |
| Button 32 | `887:349` | x 10 · y 12 | 4 |
| Button 40 | `887:364` | x 16 · y 12 | 6 |
| Button 48 | `887:379` | x 16 · y 18 | 8 |
| Button 56 | `887:389` | 20 | 8 |
| Button (gradient) 24 | `1153:3371` | x 8 | 4 |
| Input root / top section | `1066:38089` | — | 2 / 4 |
| Input field | `1066:38094` | x 14 | 6 |
| Input right icons | `1066:38098` | — | 8 |
| Input sub-text group | `1066:38103` / `1251:22951` | — | 4 (Outline) / 2 (Filled) |
| Dropdown Menu | `1451:25250` | 8 | 8 |
| Dropdown Options | `1451:23786` | — | 4 |
| Dropdown Search region | `1451:23739` | bottom 8 | 8 |
| Dropdown Footer | `1451:23801` | top 4 | 12 |
| Dropdown Item | `1451:25074` | x 12 · y 10 | 12 |
| Checkbox / Radio / Toggle label | `1504:53706` | left 12 | — |
| Tooltip | `1429:16132`, `1448:128` | 10 | 4 |

Distinct values observed: **2, 4, 6, 8, 10, 12, 14, 16, 18, 20** [DERIVED].

### Derived observations
- All observed values are even; most are multiples of 2, a subset (4, 8, 12, 16, 20) multiples of 4. Values 6, 10, 14, 18 are not multiples of 4.
- Button vertical padding is nominal (fixed `Height/N` governs — `C/button` §1.3), so 12/18/20 vertical values may not represent intended spacing.
- Not inspected: padding for Button sizes 26/28/36/38/42/46/52, Mobile Dropdown, Small/Large selection controls (`C/*` gap rows).

### Contradictions between reports
None. `04` L1 and `12` D-08 consistent.

### Recommendation
**None — choosing a scale is a design decision; observed values are input only.** ⚑ OWNER: (a) whether a spacing scale is intended; (b) its steps (e.g. which of 6/10/14/18 are kept); (c) whether `S = 8` is the seed of an intended size scale.

---

## Summary

| Decision | Evidence-supported option | Confidence basis | ⚑ OWNER items |
|---|---|---|---|
| D-01 | **Brand/* (N1)** | Bound by all components; only scheme with Dark values | Deprecate N2; N3 icon names; raw `#3a6ff7`; foreign N6 |
| D-02 | None | Value not derivable | Intent + correct value |
| D-03 | None | Dark only partially designed (Dropdown, Tooltip) | Scope; full Dark values |
| D-04 | **Scale A** | All 11 component styles match A, none match B | Scale B status; H3; naming; 8/10 px styles |
| D-05 | None | No width in file; components resolve Mobile values | Switch width; Mobile-as-default |
| D-06 | None | Licensing | Licence route; fallback; weights for v1 |
| D-07 | None | Frame widths only; 360 vs 393 inconsistency | Ranges; tablet; max width; reference mobile width |
| D-08 | None | No scale; 10 raw values observed | Whether a scale exists; its steps |

### Contradictions / refinements to earlier reports — **applied 2026-11-19**

| # | Report(s) | Refinement |
|---|---|---|
| 1 | `02` C1, `12` D-01 | Colour conflicts = **8**, not 6. |
| 2 | `03` T3, `08` INC-14 | Body S rows are two used weights (naming collision), not a value conflict; H3 remains a duplicate. |
| 3 | `03` T6 | Components *are* bound to text styles (already noted in `C/button` B11, `07` §4). Applied to `03`. |
| 4 | `04` | Reference mobile width inconsistent: Foundations 360 vs Patterns 393 (new). |
| 5 | `03`/`05` | Components resolve **Mobile** typography values; layout frame resolves **Desktop** grid values (mode evidence, new). |

All five refinements were applied on 2026-11-19 to `02`, `03`, `04`, `07`, `08`, `10`, `12` with dated correction notes; original wording is preserved in each note.
