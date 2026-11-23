# Component Spec — Tooltip

| Item | Value |
|---|---|
| Page | › ⑤ Tooltip ✓ `1351:18311` |
| Component set | **tooltip** `1448:16825` (80 variants) |
| Location | Section `1568:38568` "CoreTooltip Components" › `1568:40001` "Tooltip" |
| Method | `get_design_context` ×2 (`1429:16132` Mobile/dark/left/Text only; `1448:128` Desktop/light/left/Heading and description); `get_variable_defs` ×1 (`1429:16131` Mobile/light/left/Text only). Read-only. |

## 1. Properties

| Property | Values |
|---|---|
| `Device` | Mobile, Desktop |
| `Mode` | dark, light (lower-case) |
| `Arrow` | left, left center, right, right center, top, top left, top right, bottom, bottom left, bottom right |
| `Format` | Text only, Heading and description |
| `content` | Text — "This is the tool tip content" |
| `heading` | Text — "Tooltip heading" (Heading format only) |

2 × 2 × 10 × 2 = 80, complete.

## 2. Dimensions [META]

| Format | Mobile | Desktop |
|---|---|---|
| Text only | 182 × 38 | 157 × 38 |
| Heading and description | 260 × 62 | 240 × 59 (fixed w 240 / h 59 [APPLIED]) |

Max width 300 [APPLIED]. Why Mobile is wider than Desktop for the same text is not explained (padding/typography not inspected for Desktop Text-only) [GAP].

## 3. Anatomy & styling [APPLIED]

| Attribute | Value |
|---|---|
| Container | column, padding 10, radius **4 (raw)**, max-width 300; Heading format: gap 4 |
| Arrow | polygon vector in a 20 × 20 box, rotated (−90° for `left`), positioned outside the body (`left: -13px; top: 9px` for `left`) |
| Dark bg / text | `Brand/Base/Black` `#0b0c0f` / `Brand/Base/White` `#fafcff` |
| Light bg / text | `Brand/Base/White` `#fafcff` / `Brand/Base/Black` `#0b0c0f` |
| Text-only content | **Body S - Semi** (vars `Body/XS-Semibold`) 14 / 18, weight 600 |
| Heading | Body S - Semi 14 / 18, 600 |
| Description | **Label XSmall — Regular** 12 / 17, 400 |
| Shadow / border | **none** on either mode |

## 4. Findings

| # | Finding | Severity |
|---|---|---|
| TT1 | **Light tooltip has no shadow or border** — `#fafcff` on `#fafcff`/white page backgrounds is effectively invisible. | High |
| TT2 | Theme via `Mode=dark/light` variant + raw Base Black/White — doesn't use the variable Dark mode or semantic tokens (vs Dropdown `Theme=Light/Dark`). | Medium |
| TT3 | Radius 4 is raw (not `Radius/4`). | Low |
| TT4 | Arrow set lacks "top center"/"bottom center" naming symmetry with "left center"/"right center". | Low |
| TT5 | Desktop Heading variant has fixed height 59 — long text will clip. | Medium |
| TT6 | No delay/trigger/dismiss behaviour documented; no max-lines rule. | Gap |
| TT7 | Mobile vs Desktop size differences unexplained. | Gap |

## R4-0 update (2026-11-20)

Read-only evidence in `../r4-0-evidence.md` §4. Original findings are preserved.
- **TT7 resolved:** Desktop Text-only uses Body XS Medium 12/18 (Mobile uses Body S-Semi 14/18).
- **TT5 extended:** every Heading variant is fixed-size: Desktop 240 × 59 and Mobile 260 × 62 (Mobile heading H7 Semibold 16/18, description Body S Regular 14/20).
- All 10 arrow positions are recorded (offsets and transforms). The arrow is a `regular-polygon` filled with the body colour; its shape (point count, rounding) is not readable.

## R4-2 implementation (2026-11-20)

Implemented in `src/components/tooltip/`: **all 80 variants**, with each variant's arrow offset and transform matched to its Figma output (`../r4-0-evidence.md` §4).
- **G12:** the arrow glyph is an empty positioned slot.
- **TT-POS (derived):** a 12px trigger-to-tooltip gap, so the arrow tip touches the trigger.
- **A40:** the light tooltip is 1.00:1 against a light page (TT1). Reproduced.
