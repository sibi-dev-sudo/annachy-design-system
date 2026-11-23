# Component Spec — Input Field

| Item | Value |
|---|---|
| Page | › ② Input ✓ `375:10892` |
| Component sets | **Input Field / Outline** `1066:37962` (150) · **Input Field / Filled** `1066:40663` (175) |
| Location | Section `1567:1642` "Input Feild Component Source" › `1567:2351` "Inputs" |
| Method | `get_design_context` ×5 (`1066:38089`, `38539`, `39889`, `40783`, `41208`); `get_variable_defs` ×11 (all states at Size 48 / Radius 8). Read-only. |
| Tags | **[APPLIED]** design context · **[BOUND]** variable defs (element not always identifiable) · **[META]** metadata |

---

## 1. Properties

| Property | Outline | Filled |
|---|---|---|
| `State` | Default, Focused, Filled, Error, Disabled, Success (6) | Default, **Hover**, Focused, Filled, Error, Disabled, Success (7) |
| `Size` (field height) | 46, 48, 50, 54, 56 | same |
| `Radius` | 4, 6, 8, 10, 12 | same |
| `label`, `description`, `placeholder`, `subText` | Text | Text |
| `showLabel`, `showDescription`, `showSubText` | Boolean | Boolean |
| `showLeftIcon`, `showRightIcon1`, `showRightIcon2`, `showSubTextIcon` | **absent** | Boolean |
| `leftIcon`, `rightIcon1`, `rightIcon2`, `subTextIcon` | **absent** (icons fixed) | Instance swap |

Defaults: label "Label", description "Description", placeholder "Placeholder Active", subText "Sub-text".

## 2. Anatomy & layout [APPLIED, Size 48 / Radius 8]

```
Root (column, gap 2, width 337, overflow clip)
├─ Top Section (column, gap 4, height 90)
│  ├─ Label Container (column)
│  │  ├─ Label        — Heading/H7 Semibold 16/18
│  │  └─ Description  — Body S Regular 14/20
│  └─ Input Field (row, gap 6, height = Size, padding-x 14, radius = Radius var, border 1px)
│     ├─ Left icon (24)
│     ├─ Value/placeholder — Body M Medium 16/24, flex 1
│     └─ Right Icons (row, gap 8): 2 × 24 icons
└─ Sub-text Group (row, gap 4 [Outline] / 2 [Filled])
   ├─ Sub-text — Body S Regular 14/20
   └─ Sub-text icon (Outline: Error circle 16, always present; Filled: 14, toggleable)
```

Root heights [META]: Size 46→110, 48→112, 50→114, 54→118, 56→120 (field height + 64). Width 336/337 alternating.

Icons:
- **Outline** — fixed instances from icon source **S5 (Annachy Icons File)** *[Naming standardised to S5 on 2026-11-19; see `06` §1 for S1–S6 labels.]*: `User/User Curved` (M 24) left; `Arrow/Chevron Up` + `Arrow/Chevron Down` (M 24, Filled) right; `Alerts/Error circle` (XS 16). Chevron Up is built from a source layer named "Down" and vice-versa, both vertically flipped [APPLIED + Figma description].
- **Filled** — swappable slots defaulting to `Cloud` (Solar pilot set, `Style=Linear, Size=24/14, Semantic state=Brand`, nodes `561:36135`, `561:36137`), at **opacity 30 %** in Default.

## 3. State styling

### 3.1 Outline (Size 48, Radius 8)

| State | Field border | Field bg | Label/desc | Value text | Sub-text | Evidence |
|---|---|---|---|---|---|---|
| Default | 1px `Brand/Blue-Grey/300` `#bfc4cf` | none | label `Blue-Grey/800` `#272b35`, desc `Blue-Grey/700` `#3d4451` | placeholder `Blue-Grey/200` **`#dcdfe5`** | `Blue-Grey/500` `#707a8f` | [APPLIED] |
| Focused | 1px **`#3a6ff7` (raw, unbound)** | none | `Blue-Black/500` `#121417` | `Base/Grey` `#1f242e` | `Blue-Grey/900` `#15181e` | [APPLIED] |
| Filled | [not inspected] | — | `Blue-Black/500` | `Base/Black` `#0b0c0f` (likely value) | `Blue-Grey/900` | [BOUND] |
| Error | 1px `error` `#e72b23` | none | `Blue-Black/500` | `Base/Grey` | `error` `#e72b23` | [APPLIED] |
| Disabled | [element unconfirmed] | — | uses `Blue-Grey/200` `#dcdfe5`, `Blue-Grey/100` `#edeff2` | — | — | [BOUND] |
| Success | likely `success` `#276732` | — | `Blue-Black/500` | `Base/Grey` | — | [BOUND] |

### 3.2 Filled (Size 48, Radius 8)

| State | Field border | Field bg | Other bound colours | Evidence |
|---|---|---|---|---|
| Default | 1px `Blue-Grey/100` `#edeff2` | `Background/Secondary` `#f6f7f9` | icons opacity 30 % | [APPLIED] |
| Hover | [element unconfirmed] | `Background/Secondary` | `Blue-Grey/800`, `/700`, `/400`, `/500`, `Blue/500`, `brand` | [BOUND] |
| Focused | 1px `Blue/600` `#003fbc` | `Blue-Grey/50` `#f6f7f9` | icons full opacity | [APPLIED] |
| Filled | — | `Background/Secondary` | `Blue-Black/50` `#202d47`, `Blue-Grey/300` | [BOUND] |
| Error | likely `error` `#e72b23` | `Background/Secondary` | — | [BOUND] |
| Disabled | — | — | `Blue-Grey/200`, `Blue-Grey/100` | [BOUND] |
| Success | likely `success` `#276732` | `Background/Secondary` | — | [BOUND] |

No focus ring / shadow on any inspected state — focus = 1px border colour change only [APPLIED].

## 4. Typography [BOUND]

| Element | Style | Size / LH | Weight |
|---|---|---|---|
| Label | Heading/H7 Semibold | 16 / 18 | 600 |
| Description, Sub-text | Body S | 14 / 20 | 400 |
| Value / placeholder | Body M-Medium | 16 / 24 | 500 |

## 5. Findings

| # | Finding | Severity |
|---|---|---|
| IN1 | **Placeholder colour `#dcdfe5`** has insufficient contrast where a background is defined: **Input / Filled** placeholder on field fill `#f6f7f9` = **1.25:1** (`09` A16) — far below WCAG 4.5:1. **Input / Outline** field has **no fill (transparent)**, so its placeholder contrast **depends on the page background** and no ratio is assigned until a background colour is confirmed (`09` §1.2). *[Corrected 2026-11-19 — originally: "Placeholder colour `#dcdfe5` on white — far below WCAG 4.5:1"; no white background is defined in the Outline component.]* | High (a11y) |
| IN2 | **Focus colour inconsistent and unbound**: Outline uses raw `#3a6ff7` (= lowercase `brand/base/gradient-start`); Filled uses `Blue/600` `#003fbc`. 1px change only — weak focus indicator. | High |
| IN3 | Outline has **no Hover state**; Filled has one. | Medium |
| IN4 | Error/Success use the **icon semantic variables** `error`/`success` (600 shades), not `Brand/Feedback/*` (500 shades). | Medium |
| IN5 | Outline always shows the Error-circle icon (no boolean), even in Default/Focused/Success. | Medium |
| IN6 | Outline and Filled use **different icon sources** (S5 Annachy Icons File vs S2 Iconography pilot) *[Naming standardised to S5 on 2026-11-19; see `06` §1 for S1–S6 labels.]* and different property models (fixed vs slots). | Medium |
| IN7 | Radius 6 and 10 not in the radius scale; Radius is a variant property (×5 variants) rather than a token choice. | Medium |
| IN8 | Chevron Up/Down icons built from swapped source layers + flips. | Low |
| IN9 | Doc column headers mislabel states (`1567:2352`: "Active"; `1567:2359`: Success/Disable swapped). | Low |
| IN10 | No character counter, prefix/suffix text, textarea, or read-only state defined. | Gap |
| IN11 | Not inspected: Size 46/50/54/56 padding (assumed same 14 px); Disabled/Success/Hover element-level mapping. | Gap |


## R3-0 update (2026-11-19)

Read-only inspection; full evidence with node IDs in `../r3-0-evidence.md`. Original findings above are preserved.

- **IN11 resolved:** padding-x **14** and gap 6 at all sizes 46–56 (§7).
- Outline Filled/Disabled/Success and Filled Hover/Filled/Error/Disabled/Success element mappings recorded (§8–§9). Filled Disabled has no fill; icons 30 % in Default/Hover/Disabled.

## R3-3 update (2026-11-19)

Implemented in `src/components/input/`. Evidence: `../r3-0-evidence.md` §23 (radius, sizes and cross-combinations verified; State/Size/Radius model).
- **IN-12 (new):** the Top Section has a fixed height (Size + 42) even when the label or description is hidden. Reproduced.
- **IN-13 (new, confirmed accessibility issue, A38):** the Filled Hover placeholder `Blue-Grey/400` `#98a0ae` on `Background/Secondary` `#f6f7f9` is **2.46:1**, which fails WCAG 1.4.3 (and the 3:1 large-text threshold). Reproduced unchanged; changing it needs design-owner approval (D-22).
- **D-09:** Radius 6 and 10 are bound to Figma variables `Radius/6` and `Radius/10`, which have no R1 tokens. They are implemented as exact component-local values (6px / 10px).
