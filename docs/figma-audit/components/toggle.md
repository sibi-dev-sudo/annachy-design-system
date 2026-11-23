# Component Spec — Toggle (Switch)

| Item | Value |
|---|---|
| Page | › ④ Checkbox /Radio/Toggle ✓ `375:10893` |
| Component set | **.Selection Controls / Toggle** `1504:54471` (180 variants) |
| Duplicate | Archive › Toggle `1438:5542` (180, property `Toggle Position`) + doc `1504:48004` |
| Method | `get_design_context` ×2 (On `1504:54622`, Off `1504:54637`); `get_variable_defs` ×6 (Hover On `54652`, Hover Off `54667`, Focus On `54682`, Pressed On `54712`, Disabled On `54742`, Disabled Off `54757`) — Size=Medium, Position=Left, Alignment=Center. Read-only. |

## 1. Properties

| Property | Values |
|---|---|
| `State` | On, Off, Hover On, Hover Off, Focus On, Focus Off, Pressed On, Pressed Off, Disabled On, Disabled Off |
| `Size` | Small, Medium, Large |
| `Position` | Left, Right |
| `Alignment` | Center, Top, Bottom (order differs from Checkbox/Radio) |
| `label`, `subtext`, `showLabel`, `showSubtext` | as Checkbox |

10 × 3 × 2 × 3 = 180, complete.

## 2. Dimensions & anatomy [APPLIED, Medium]

| Element | Value |
|---|---|
| Root | 234 × 41 [META] |
| Toggle Container | 38 × 20 (Off: `justify-content: flex-end` — container alignment flips between On/Off) |
| Track + thumb | **single flattened vector image** 38 × 20 (Off image extends 5 % below for shadow) |
| Label | padding-left 12, **max-width 240**, Label Medium — Medium 16/21 `Text/Primary` |
| Subtext | padding-left 12, width 184, Body S Regular 14/20 `Text/Tertiary` |

Small/Large track sizes: not inspected [GAP].

## 3. States (Medium) [BOUND]

| State | Track colour | Thumb colour | Effect style | Label |
|---|---|---|---|---|
| On | `Button/Primary/Background/Default` `#004feb` (confirmed via wrapper `1504:57178`) | `Content/Loading` `#fafcff` | `Toggle/On` | `Text/Primary` |
| Off | [vector — not readable] | — | `Toggle/Off` | `Text/Primary` |
| Hover On | `Button/Primary/Background/Hover` `#003fbc` | `Button/Primary/Content/Loading` `#fafcff` | `Toggle/On` | `Text/Primary` |
| Hover Off | `Blue-Grey/200` `#dcdfe5` (likely) / `Blue-Grey/50` `#f6f7f9` | `Content/Loading` `#fafcff` | `Toggle/Off` | `Text/Primary` |
| Focus On | `Button/Primary/Background/Focus` `#004feb` + border `Button/Primary/Border/Focus` `#003fbc` | `#fafcff` | `Toggle/On` | `Text/Primary` |
| Focus Off | not inspected | | | |
| Pressed On | `Button/Primary/Background/Pressed-Active` `#3372ef` | `#fafcff` | `Toggle/On` + **`Toggle/Press`** | `Text/Primary` |
| Pressed Off | not inspected | | | |
| Disabled On | `Blue-Grey/100` `#edeff2` | `#fafcff` | `Toggle/On` | `Blue-Grey/200` `#dcdfe5` |
| Disabled Off | `Blue-Grey/50` `#f6f7f9` | `#fafcff` | `Toggle/Off` | `Blue-Grey/200` |

### Effect styles [EXTRACTED]

| Style | Layers (colour · x,y · blur) |
|---|---|
| `Toggle/On` | `#00000017` 0,0 ·1 · `#0000000D` -1,1 ·1 · `#00000003` -2,1 ·1 · `#00000000` -2,2 ·1 |
| `Toggle/Off` | `#3C343417` 0,0 ·1 · `#3C34340D` 1,1 ·1 · `#3C343403` 2,2 ·1 · `#3C343400` 3,2 ·1 |
| `Toggle/Press` | `#004FEB4A` 0,0 ·1 · `#004FEB42` 0,1 ·2 · `#004FEB26` -1,2 ·2 · `#004FEB0A` -2,4 ·2 · `#004FEB03` -3,7 ·3 |

(Thumb shadow direction mirrors between On (left) and Off (right).)

## 4. Findings

| # | Finding | Severity |
|---|---|---|
| T1 | **Track/thumb flattened to a vector** in On/Off; colours partly readable only in other states. | High |
| T2 | Thumb bound to **`Button/Primary/Content/Loading`** — semantic misuse of a button-loading token. | Medium |
| T3 | Disabled On (`#edeff2`) and Disabled Off (`#f6f7f9`) are near-identical — on/off barely distinguishable when disabled. | High (a11y) |
| T4 | Toggle has Hover states; Checkbox/Radio don't — inconsistent interaction model across Selection Controls. | Medium |
| T5 | Toggle effect styles (`Toggle/*`) and Button effect styles (`Button/*`) are not on the Shadow foundation page. | Medium |
| T6 | Alignment option order differs (Center first). | Low |
| T7 | Not inspected: On/Off base track colours (vector), Small/Large dimensions, Focus Off, Pressed Off. | Gap |


## R3-0 update (2026-11-19)

Read-only inspection; full evidence with node IDs in `../r3-0-evidence.md`. Original findings above are preserved.

- **T7 resolved:** tracks 32×16 / 38×20 / 44×24; thumbs 12/16/20, inset 2, Off x 2 → On x 18/20/22; Off track `Blue-Grey/50`; thumb `#fafcff` + `Blue-Grey/100` + `Toggle/On`/`Toggle/Off` effect (§13).
- Focus Off adds `Button/Primary/Border/Focus` `#003fbc` + `Blue-Grey/200`; Pressed Off adds `Blue-Grey/300`. Focus On thumb x 18.5. Hidden "Focus Ring" layer (−4 inset, unbound) stays hidden in all variants.
- **New:** label style per size — Label Small 14/20 / Label Medium 16/21 / Label Large 18/22.
- **Still unresolved:** track radius, thumb stroke width, Focus/Pressed Off stroke element and width (D-27).

## R3-6 update (2026-11-19)

Implemented in `src/components/toggle/` (all 180 variants; evidence `../r3-0-evidence.md` §26).
- Per-element bindings (Track − Thumb) were resolved for all 10 states.
- Thumb offsets: Focus On is 1.5px inward and Focus Off is at x 3, at every size.
- **TG-1:** the Off, Disabled On and Disabled Off track fills are derived; they are the only bound candidate, shared with the thumb.
- **New A39:** the Off track `#f6f7f9` has 1.04:1 contrast against the page and against the thumb, failing WCAG 1.4.11. Reproduced unchanged.
- **D-27 unchanged:** the track radius (the track renders square), thumb stroke width and focus border width are not drawn.
