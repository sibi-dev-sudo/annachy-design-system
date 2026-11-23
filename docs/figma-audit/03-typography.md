# 03 — Typography

| Item | Value |
|---|---|
| Source page | › ② Typography ✓ `220:10667` |
| Sections | Typography System `1557:39451` · Typography Documentation (specimen sheet) `1557:44867` · Screen - Layout `1558:51031` |
| Method | Documentation text parsed from `get_metadata` (layer names = visible text); specimen nodes inspected with `get_design_context`; `get_variable_defs` on both sections. All read-only. |
| Status | Two **conflicting** type scales documented. No text-style variables returned *for the Foundations sections* (components are bound — §4.1; clarified 2026-11-19). Decision D-04 open. |

Tags: table values are **[EXTRACTED]** as documentation text (what the designers wrote). Values marked **[APPLIED]** were returned by `get_design_context` from actual rendered specimen nodes.

---

## 1. Typeface

| Property | Value | Source |
|---|---|---|
| Family | **Proxima Nova** | both sections; specimen fonts `Proxima_Nova:Regular/Medium/SemiBold/Bold` [APPLIED] |
| Designer / foundry | Mark Simonson / Mark Simonson Studio | `1557:44867` |
| Licence | **Commercial only** — "not an open-source typeface"; Google Fonts: N/A; Adobe Fonts: included; web use requires "a licensed web embed" | `1557:44867` |
| Letter spacing | 0 ("Keep Letter Spacing at 0") | `1557:39451` |
| Fallback stack | [MISSING] — not specified | — |

⚠ **Implementation blocker:** a web-font licence (or Adobe Fonts kit) for Proxima Nova is required before fonts can be shipped in `src/assets/fonts/`. The font files are not in Figma and cannot be exported from it.

### Weights

| Typography System `1557:39451` (5 weights) | Documentation `1557:44867` (8 weights) |
|---|---|
| Light 300 — Decorative & Supporting | Thin ~100 |
| Regular 400 — Body Text | Light ~300 |
| Medium 500 — Body Emphasis | Regular 400 |
| Semibold 600 — Subheadings & Labels | Medium 500 |
| Bold 700 — Headings & Display | Semibold 600 |
| | Bold 700 |
| | Extrabold 800 |
| | Black 900 |

Weights actually used by the System scale below: Regular, Medium, Semibold, Bold (**Light 300 is listed but used by no style**) [DERIVED].

---

## 2. Scale A — "Typography System" `1557:39451` (responsive)

Header claims **26 styles**, "Mobile + Desktop", "5 weights". Rows extracted: **28**.

### 2.1 Headings (header: "8 styles"; footer: "Heading Styles: 9"; rows: 9)

| Style | Weight | Mobile size / LH | Desktop size / LH | Usage | Row node |
|---|---|---|---|---|---|
| H1 | Bold | 32 / 38 | 48 / 58 | Main page title | `1558:48884` |
| H2 | Bold | 28 / 36 | 40 / 48 | Section heading | `1558:48892` |
| H3 | Bold | 26 / 34 | 36 / 42 | Subsection heading | `1558:48900` |
| H3 *(duplicate)* | Semibold | 26 / 30 | 36 / 42 | Secondary emphasis | `1558:48908` |
| H4 | Semibold | 24 / 26 | 32 / 38 | Component heading | `1558:48916` |
| H5 | Semibold | 20 / 24 | 28 / 34 | Small section heading | `1558:48924` |
| H6 | Semibold | 18 / 20 | 24 / 28 | Compact heading | `1558:48932` |
| H7 | Semibold | 16 / 18 | 20 / 24 | Smallest heading | `1558:48940` |
| H8 | Bold | 14 / 18 | 14 / 18 | Smallest heading | `1558:48948` |

### 2.2 Subheading & Body (header: "10 styles"; footer: "Styles: 11"; rows: 11)

| Style | Weight | Mobile size / LH | Desktop size / LH | Usage | Row node |
|---|---|---|---|---|---|
| Subheading L | Semibold | 18 / 25 | 20 / 28 | Supporting heading | `1558:48989` |
| Body L | Regular | 18 / 27 | 18 / 27 | Large body text | `1558:48997` |
| Body M | Regular | 16 / 24 | 16 / 24 | Default body text | `1558:49005` |
| Body M — Medium | Medium | 16 / 24 | 16 / 24 | Emphasized body text | `1558:49013` |
| Body S | Regular | 14 / 20 | 14 / 21 | Small body text | `1558:49021` |
| Body S — Medium | Medium | 14 / 20 | 14 / 21 | Emphasized small text | `1558:49029` |
| Body S *(second "Body S" row — Semibold; naming collision, see T3 / §4.1)* | Semibold | 14 / 18 | 14 / 18 | Small body text | `1558:49069` |
| Body XS | Medium | 12 / 18 | 12 / 18 | Compact UI text | `1558:49037` |
| Body XS — Semibold | Semibold | 12 / 18 | 12 / 18 | Emphasized compact text | `1558:49045` |
| Body XXS | Medium | 10 / 15 | 10 / 15 | Very small text | `1558:49053` |
| Body Micro | Semibold | 8 / 12 | 8 / 12 | Micro UI text | `1558:49061` |

### 2.3 Labels & Captions (header: "8 styles"; rows: 8)

| Style | Weight | Mobile size / LH | Desktop size / LH | Usage | Row node |
|---|---|---|---|---|---|
| Label Large | Medium | 18 / 22 | 18 / 25 | Large UI label | `1558:49114` |
| Label Medium | Medium | 16 / 21 | 16 / 22 | Default UI label | `1558:49122` |
| Label Small | Medium | 14 / 20 | 14 / 20 | Small UI label | `1558:49130` |
| Label XSmall | Regular | 12 / 17 | 12 / 18 | Compact UI label | `1558:49138` |
| Label XSmall — SB | Semibold | 12 / 17 | 12 / 18 | Emphasized label | `1558:49146` |
| Caption Small | Semibold | 11 / 15 | 11 / 15 | Supporting metadata | `1558:49154` |
| Caption XSmall | Regular | 10 / 14 | 10 / 14 | Secondary metadata | `1558:49162` |
| Caption Micro | Medium | 8 / 10 | 8 / 12 | Compact metadata | `1558:49170` |

Documented responsive progression (text in file): Mobile `32 → 28 → 26 → 24 → 20 → 18 → 16 → 14 → 12 → 11 → 10 → 8`; Desktop `48 → 40 → 36 → 32 → 28 → 24 → 20 → 18 → 16 → 14 → 12 → 11 → 10 → 8`.

Breakpoint at which Mobile switches to Desktop: **[MISSING]** (see `04-spacing-layout.md`).

---

## 3. Scale B — "Typography Documentation" specimen sheet `1557:44867` (single size)

| Style | Size | Line height |
|---|---|---|
| Display XL | 72 | 80 |
| Display L | 56 | 64 |
| Heading 1 | 48 | 56 |
| Heading 2 | 40 | 48 |
| Heading 3 | 32 | 40 |
| Subtitle | 24 | 32 |
| Body Large | 20 | 28 |
| Body | 16 | 24 |
| Body Small | 14 | 20 |
| Caption | 12 | 16 |
| Label | 11 | 14 |

Weights per style: [MISSING]. This sheet is a generic Proxima Nova specimen ("VERSION 2.0 • 14 SECTIONS", footer "© 2025") and also recommends sizes outside both scales (13 px dashboards, 15 px reports, 22 px+ marketing).

---

## 4. Applied values on specimen nodes [APPLIED]

| Specimen | Node | Labelled as | Applied font | Applied size | Line height | Matches Scale A? |
|---|---|---|---|---|---|---|
| "Discover your style" | `1558:48865` | H1 | Proxima Nova Bold | **36 px** | normal (auto) | **No** — H1 is 32 (mobile) / 48 (desktop); 36 = H3 desktop |
| "Start your journey today" | `1558:48970` | Subheading L | Proxima Nova SemiBold | 20 px | normal | Size/weight ✓ desktop; LH ✗ (28 expected) |
| "Add to cart" | `1558:49092` | Label Large | Proxima Nova Medium | 18 px | normal | Size/weight ✓; LH ✗ (22/25 expected) |

Specimen colours use `brand/base/black` `#0b0d0f` and labels `text/secondary` `#030a14` — the lowercase variable scheme (see `02-color.md` C1).

`get_design_context` returned no text-style or typography-variable references for these nodes [EXTRACTED]. This indicates specimens are **not bound to Figma text styles**, despite the rule "Use the predefined Typography Text Styles" (`1557:39451`). [DERIVED — absence of evidence; confirm with design owner]

> *[Corrected 2026-11-19 — evidence: `13-global-token-decisions.md` §D-04. Scope clarification: the statement above applies to **documentation specimens only**. Phase 4 found that **components are bound** to Figma text styles and typography variables (see §4.1).]*

### 4.1 Component text-style bindings [added 2026-11-19]

Confirmed evidence from `get_variable_defs` / `get_design_context` on component variants (`07` §4, `components/*.md`):

| Figma text style (as named) | Variable path | Bound size / LH | Scale A row | Scale A Mobile vs Desktop | Value resolved | Used by |
|---|---|---|---|---|---|---|
| Body XS — Semibold | `Subheading & Body/Body/XXS-Semibold/*` | 12 / 18 | Body XS — Semibold | equal | — | Button 24–26 (`887:333`) |
| Body S - Semi | `Subheading & Body/Body/XS-Semibold/*` | 14 / 18 | Body S (Semibold) `1558:49069` | equal | — | Button 28–32, Tooltip (`1429:2`) |
| Body S — Regular | `Subheading & Body/Body/S/*` | 14 / 20 | Body S (Regular) `1558:49021` | 14/20 vs 14/21 | **Mobile** | Input, Checkbox, Radio, Toggle |
| Body M — Medium | `Subheading & Body/Body/M-Medium/*` | 16 / 24 | Body M — Medium | equal | — | Input value |
| Body M — Regular | `Subheading & Body/Body/M/*` | 16 / 24 | Body M | equal | — | Dropdown search |
| Heading/H7 — Semibold | `Heading/H7/Semibold/*` | 16 / 18 | H7 | 16/18 vs 20/24 | **Mobile** | Button 36–42, Input label |
| Heading/H6 — Semibold | `Heading/H6/Semibold/*` (`Line Height 2`) | 18 / 20 | H6 | 18/20 vs 24/28 | **Mobile** | Button 46–48 |
| Heading/H5 — Semibold | `Heading/H5/Semibold/*` | 20 / 24 | H5 | 20/24 vs 28/34 | **Mobile** | Button 52–56 |
| Label Small — Medium | `Labels & Captions/Label/Small/*` | 14 / 20 | Label Small | equal | — | Dropdown Item, Selection Controls wrapper |
| Label Medium — Medium | `Labels & Captions/Label/Medium/*` | 16 / 21 | Label Medium | 16/21 vs 16/22 | **Mobile** | Checkbox, Radio, Toggle |
| Label XSmall — Regular | `Labels & Captions/Label/XSmall/*` | 12 / 17 | Label XSmall | 12/17 vs 12/18 | **Mobile** | Tooltip description |

- **Confirmed:** all 11 component text styles match Scale A; none match Scale B. In every case where Scale A Mobile differs from Desktop (6 styles), components resolve the **Mobile** value; no Desktop value was observed on any component.
- **Interpretation:** typography variables probably have Mobile/Desktop modes with Mobile active where components were inspected (mode names are not retrievable). Grid variables on the Desktop layout frame resolved to Desktop values (`04` §1.1), suggesting modes are set per frame.
- **Unresolved:** the Mobile→Desktop switch width and whether Mobile is the intended default (D-05).

---

## 5. Findings

| # | Finding | Severity | Tag |
|---|---|---|---|
| T1 | **Two incompatible type scales** (Scale A responsive H1–H8/Body/Label; Scale B Display/Heading/Body/Caption/Label). H1 = 32/48 in A vs 48 in B; Label = 12–18 in A vs 11 in B. | High | [EXTRACTED] |
| T2 | Scale A style counts disagree with its own headers (26 claimed, 28 rows; "8 heading styles" vs "9"; "10 body styles" vs "11"). | Medium | [EXTRACTED] |
| T3 | **H3** has two rows with different values (Bold 26/34 `1558:48900` vs Semibold 26/30 `1558:48908`) — a true duplicate; no component binds either. **Body S** has two rows (Regular 14/20 `1558:49021`, Semibold 14/18 `1558:49069`) — **both are used by components** (Regular: Input, selection controls; Semibold as "Body S - Semi": Button, Tooltip), so this is a **naming collision, not a value conflict**. *[Corrected 2026-11-19 — evidence: `13-global-token-decisions.md` §D-04. Originally: "Duplicate style names with different values: H3 …, Body S (Regular 14/20 vs Semibold 14/18)."]* | High (H3) · Low (Body S naming) | [EXTRACTED] |
| T4 | H1 specimen rendered at 36 px, contradicting the H1 row. | Medium | [APPLIED] |
| T5 | Specimens use auto line height rather than the documented LH values. | Medium | [APPLIED] |
| T6 | No text styles / typography variables detected on **documentation specimens**. Components **are** bound to text styles and typography variables (§4.1; `components/button.md` B11). *[Corrected 2026-11-19 — evidence: `13-global-token-decisions.md` §D-04 — scope clarified; original wording retained above.]* | Medium (docs only) | [DERIVED] |
| T7 | Body S desktop LH 21 px (14 × 1.5) vs mobile 20 px — sub-pixel-ish drift; Label Large LH 22 vs 25; Caption Micro 10 vs 12. Intentional? | Low | [EXTRACTED] |
| T8 | 8 px styles (Body Micro, Caption Micro) are below the file's own accessibility rule "Min 12px UI / 14px Body" and "UI labels ≥ 11px" (`1557:44867` §17). | Medium | [EXTRACTED] |
| T9 | Light 300 weight listed but unused; Scale B lists Thin–Black (8 weights) vs Scale A 5. | Low | [EXTRACTED] |
| T10 | Proxima Nova is commercially licensed; no web fallback stack defined. | High (delivery) | [EXTRACTED] / [MISSING] |
| T11 | Section name typo "Typrography" on Brainstorming page `5:10905` (exploration; not a spec). | Low | [EXTRACTED] |
| T12 | Components resolve **Mobile** Scale A values wherever Mobile differs from Desktop (6 of 11 bound styles); no Desktop value observed on components. Values confirmed; mode interpretation in §4.1. *[Added 2026-11-19 — `13` §D-05.]* | Medium | [BOUND] + [DERIVED] |

---

## 6. Recommendation (for approval)

> **Status:** D-04 is **open** — this section is a candidate recommendation, not an approved decision.

Treat **Scale A (Typography System)** as the candidate source of truth: it is the more recent, product-specific, responsive definition and carries usage rules; Scale B reads as a generic font specimen. Before tokens are generated, the design owner should confirm:

1. Scale A is canonical and Scale B is reference-only.
2. Correct values for the duplicated H3 rows; naming for the two Body S styles (both in use). *[Wording corrected 2026-11-19; originally "Correct values for duplicated H3 and Body S."]*
3. The Mobile → Desktop breakpoint, and whether Mobile values (currently resolved by components, T12) are the default.
4. Font licensing path (Adobe Fonts kit vs self-hosted licensed files) and fallback stack.
