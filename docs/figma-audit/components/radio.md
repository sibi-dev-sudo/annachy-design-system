# Component Spec — Radio Button

| Item | Value |
|---|---|
| Page | › ④ Checkbox /Radio/Toggle ✓ `375:10893` |
| Component set | **.Selection Controls / Radio Button** `1504:52363` (108 variants) |
| Duplicate | Archive › Radio `1493:3` (108, property `Radio Position`) + doc `1500:22374` |
| Method | `get_design_context` ×1 (`1504:52685` Selected); `get_variable_defs` ×5 (Unselected `1504:52738`, Disabled Unselected `52786`, Disabled Selected `52835`, Focus `52889`, Pressed `52943`) — Size=Medium, Position=Left, Alignment=Center. Read-only. |

## 1. Properties

| Property | Values |
|---|---|
| `State` | Selected, Unselected, Disabled Unselected, Disabled Selected, Focus, Pressed |
| `Size` | Small, Medium, Large |
| `Position` | Left, Right |
| `Alignment` | Top, Center, Bottom |
| `label`, `subtext` | Text (same defaults as Checkbox) |
| `showLabel`, `showSubtext` | Boolean |

6 × 3 × 2 × 3 = 108, complete.

## 2. Dimensions

| Size | Root [META] | Control | Source |
|---|---|---|---|
| Small | 216 × 41 | 20 × 20 | Archive doc `1500:22384` "Small 20 × 20" [EXTRACTED] |
| Medium | 220 × 41 | 24 × 24 | [APPLIED] + doc `1500:22386` |
| Large | 224 × 41 | 28 × 28 | doc `1500:22388` |

## 3. Anatomy [APPLIED]

Identical to Checkbox (`checkbox.md` §3): control 24 × 24 + Content column with 12 px left padding; Label = Label Medium — Medium 16/21 `Text/Primary`; Subtext = Body S Regular 14/20 `Text/Tertiary`, width 184.

**Radio Container is a flattened vector image** (`1504:52686`) — the ring/dot are not separate shapes; the image extends beyond 24 px (insets −8.33 % / −4.17 % / −16.67 %) to include its drop shadow. Effect `Button/Default` [APPLIED].

## 4. States (Medium)

| State | Bound colours / effects | Evidence |
|---|---|---|
| Selected | vector image; effect `Button/Default` (fill colours baked into vector — not readable as variables) | [APPLIED] |
| Unselected | `surface-bg` `#ffffff`, `border-default` `#e1e1e2` (foreign tokens) | [BOUND] |
| Disabled Unselected | `Blue-Grey/100` `#edeff2`, `Blue-Grey/200` `#dcdfe5` | [BOUND] |
| Disabled Selected | `Button/Primary/Background/Disabled` `#bfc4cf`, `Button/Primary/Content/Disabled` `#fafcff`, `Blue-Grey/200` | [BOUND] |
| Focus | `Blue-White/300` `#ebf2ff`, `Button/Primary/Background/Focus` `#004feb`, effects `Button/Focus` + `shadow/sm` (`Blur/blur-0/2`, `Colors/alpha/50`) | [BOUND] |
| Pressed | `Background/Primary` `#fafcff`, `Button/Primary/Background/Pressed-Active` `#3372ef`, `Blue/300` `#99b9f7`, effect `Button/Hover` | [BOUND] |

Pattern matches Checkbox exactly (same tokens per state) [DERIVED].

## 5. Findings

| # | Finding | Severity |
|---|---|---|
| R1 | **Selected radio is a flattened vector** — colours not tokenised; the dot/ring must be rebuilt in CSS from visual reference. | High |
| R2 | Same issues as Checkbox: foreign Unselected tokens (CB1), single Focus state without selected/unselected split (CB2), **no Hover**, **no Error** state. | High |
| R3 | Archive doc labels inconsistent punctuation ("Small 20 × 20" vs "Medium · 24 × 24"). | Low |
| R4 | Not inspected: Selected dot diameter, Small/Large shadow/spacing. Needs `get_screenshot` or SVG export in Phase 5. | Gap |


## R3-0 update (2026-11-19)

Read-only inspection; full evidence with node IDs in `../r3-0-evidence.md`. Original findings above are preserved.

- **R4 resolved (geometry):** control 20/24/28; Selected = fill `Button/Primary/Background/Default`, ring colour `Blue/300`, effect `Button/Default`; dot `Background/Primary` `#fafcff` **8/10/12** at inset 6/7/8 (§12).
- Unselected: 2px `border-default`, `surface-bg`, radius 12. Right/Top layouts as Checkbox (§11).
- **Still unresolved:** selected ring stroke width (D-27).
- Focus + Selected: **D-20 recommendation (not a confirmed Figma specification)** — preserve selected appearance and apply focus treatment.

## R3-5 update (2026-11-19)

Implemented in `src/components/radio/` (all 108 variants; evidence `../r3-0-evidence.md` §25).
- Disabled Selected: `Button/Primary/Background/Disabled` fill, `Content/Disabled` dot, no stroke bound.
- Pressed: `Pressed-Active` fill, `Background/Primary` dot, `Button/Hover`.
- The radius is a raw half-size value: 10 / 12 / 14.
- **D-27 unchanged:** the Selected and Pressed ring width is unreadable, so no ring is drawn.
