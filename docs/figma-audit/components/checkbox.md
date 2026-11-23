# Component Spec — Checkbox

| Item | Value |
|---|---|
| Page | › ④ Checkbox /Radio/Toggle ✓ `375:10893` |
| Component set | **.Selection Controls / Checkbox** `1504:53300` (126 variants) |
| Location | Section `1568:28311` "Core (Radio/ Checkbox/ Toggle)" |
| Duplicates | Archive › Checkbox `1500:25474` (126, property `Checkbox Position`); legacy "check box" `1464:10379` (8 variants: Platform × Mode=Light × State) |
| Method | `get_design_context` ×2 (`1504:53701` Checked, `1504:53976` Focus); `get_variable_defs` ×5 (Multi-select, Unchecked, Disabled, Disabled On, Pressed) — all Size=Medium, Position=Left, Alignment=Center. Read-only. |

Leading "." in the set name marks it as a hidden/private set in Figma (not published) [DERIVED from Figma naming convention]. The public wrapper is **Selection Controls** `1504:57173` (see `selection-controls.md`).

---

## 1. Properties

| Property | Values |
|---|---|
| `State` | Checked, Multi-select, Unchecked, Disabled, Disabled On, Focus, Pressed |
| `Size` | Small, Medium, Large |
| `Position` | Left, Right (control relative to label) |
| `Alignment` | Top, Center, Bottom (control vertical alignment vs multi-line text) |
| `label` | Text — "Title text goes here" |
| `subtext` | Text — "Secondary text line goes here " (trailing space) |
| `showLabel`, `showSubtext` | Boolean |

7 × 3 × 2 × 3 = 126, complete.

## 2. Dimensions

| Size | Root width × height [META] | Control box |
|---|---|---|
| Small | 216 × 41 | 20 × 20 [DERIVED: −4 px vs Medium; matches Radio doc "Small 20 × 20"] |
| Medium | 220 × 41 | **24 × 24** [APPLIED] |
| Large | 224 × 41 | 28 × 28 [DERIVED] |

## 3. Anatomy [APPLIED, Medium]

```
Root (row, align center)
├─ Checkbox Container 24×24, radius Radius/4 (4)
│   └─ functional/check icon 20×20   (Checked)
└─ Content (column)
    ├─ Label Container (padding-left 12) → Label: Label Medium — Medium 16/21, Text/Primary #0b0c0f
    ├─ Subtext Container (padding-left 12) → Body S — Regular 14/20, Text/Tertiary #707a8f, width 184
    └─ Layout Anchor (0×0)
```

Label-to-control gap is implemented as `padding-left: 12px` on text containers (no auto-layout gap).

## 4. States (Medium)

| State | Box fill | Box border | Effect | Icon | Evidence |
|---|---|---|---|---|---|
| Checked | `Button/Primary/Background/Default` `#004feb` | 1px `Blue/300` `#99b9f7` | `Button/Default` | check 20 | [APPLIED] |
| Multi-select (indeterminate) | `#004feb` | 1px `Blue/300` | `Button/Default` | [indeterminate glyph not inspected] | [BOUND] |
| Unchecked | **`surface-bg` `#ffffff`** | **`border-default` `#e1e1e2`** | — | — | [BOUND] |
| Focus | `Blue-White/300` `#ebf2ff` | **2px** `Button/Primary/Background/Focus` `#004feb` | `Button/Focus` + `shadow/sm` | none (unchecked) | [APPLIED] |
| Pressed | `Button/Primary/Background/Pressed-Active` `#3372ef` | 1px `Blue/300` | **`Button/Hover`** | check (assumed) | [BOUND] |
| Disabled (unchecked) | `Blue-Grey/100` `#edeff2` (likely) | `Blue-Grey/200` `#dcdfe5` (likely) | — | — | [BOUND] |
| Disabled On | `Button/Primary/Background/Disabled` `#bfc4cf` | — | — | `Button/Primary/Content/Disabled` `#fafcff` | [BOUND] |

Label in Disabled states binds `Blue-Grey/200` `#dcdfe5` (no `Text/Primary`) [BOUND, element likely label].

### Effect styles used [EXTRACTED]

| Style | Layers (colour · x,y · blur) |
|---|---|
| `Button/Default` | `#17191C21` 0,1 ·1 · `#17191C14` -1,2 ·1 · `#17191C05` -1,3 ·1 · `#17191C00` -2,4 ·2 |
| `Button/Hover` | `#325CB34F` 0,0 ·1 · `#325CB345` 0,0 ·2 · `#325CB329` 0,0 ·3 · `#325CB30D` 0,0 ·3 · `#325CB303` 0,0 ·3 |
| `Button/Focus` | see `dropdown.md` §4 |
| `shadow/sm` | `#1A1A1A14` 0,1 · blur `Blur/blur-2` (3) · `Colors/alpha/50` (rgba(26,26,26,.08)) 0,0.5 · blur `Blur/blur-0` (0) |

## 5. Findings

| # | Finding | Severity |
|---|---|---|
| CB1 | **Unchecked uses foreign variables** `surface-bg` `#ffffff` / `border-default` `#e1e1e2` — not in the Annachy palette (the palette white is `#fafcff`). | High |
| CB2 | **Focus exists only as a single (unchecked-looking) state** — no Focus+Checked; State mixes check-state and interaction-state in one property. | High |
| CB3 | **No Hover state.** | Medium |
| CB4 | **No Error/invalid state** (e.g. required checkbox). | Medium |
| CB5 | Pressed uses the `Button/Hover` effect style; Checked uses `Button/Default` — Button effect styles reused, but these styles are absent from the Shadow foundation page. | Medium |
| CB6 | `shadow/sm`, `Blur/blur-*`, `Colors/alpha/*` — a third foreign token set (alongside Simple Design System). | Medium |
| CB7 | State naming: `Disabled` / `Disabled On` here vs `Disabled Unselected` / `Disabled Selected` (Radio) vs `Disabled Off` / `Disabled On` (Toggle). | Low |
| CB8 | Subtext has fixed width 184 px (doesn't fill). Default subtext string has a trailing space. | Low |
| CB9 | Not inspected: Small/Large exact control size, indeterminate glyph, Right/Top/Bottom layouts. | Gap |


## R3-0 update (2026-11-19)

Read-only inspection; full evidence with node IDs in `../r3-0-evidence.md`. Original findings above are preserved.

- **CB9 mostly resolved:** box 20/24/28 (Small/Medium/Large), `Radius/4`, glyph 16/20/20; label style unchanged across sizes; Unchecked & Disabled border **2px**; Checked border 1px `Blue/300` (§10).
- Right layout: content → control, text padding-right 12; Top: `align-items: flex-start` (§11). Alignment=Bottom not inspected.
- **Still unresolved:** check & `functional/remove` glyph geometry/colour — rendered as images, frames have no child shapes (D-27).
- Focus + Checked: **D-20 recommendation (not a confirmed Figma specification)** — preserve checked appearance and apply focus treatment.

## R3-4 update (2026-11-19)

Implemented in `src/components/checkbox/` (all 126 variants; evidence `../r3-0-evidence.md` §24).
- All 7 state element mappings are confirmed: Pressed keeps the check and uses `Button/Hover`; Disabled On has no border or shadow; in the disabled states, label and subtext are `Blue-Grey/200`.
- The Multi-select glyph slot is 16 (Small) and 20 (Large), centred.
- **D-27 unchanged:** the check and remove glyph geometry is still unreadable. The glyph slot ships empty, with its evidenced size, position and colour.
- D-20 is implemented as the documented recommendation.
