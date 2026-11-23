# 04 — Spacing, Grid, Layout & Radius

| Item | Value |
|---|---|
| Source pages | › ④ Grid & Layout ✓ `317:12589` · › ⑤ Radius ✓ `365:11441` |
| Method | `get_variable_defs` on `1558:51715`, `1561:56902`, `1561:56909`, `1561:57340`; `get_design_context` on `1561:57341`; documentation text from `get_metadata`. Read-only. |
| Status | Grid extracted (variables exist). Radius values documented but **not bound to variables**. Spacing scale **[MISSING]**. |

---

## 1. Grid

### 1.1 Grid variables [EXTRACTED]

Bound on Grid System `1558:51715` and Layout frame `1561:56902` (resolved value shown — mode not visible):

| Variable | Resolved value |
|---|---|
| `grid/width` | 1440 |
| `grid/height` | 1024 |
| `grid/columns` | 12 |
| `grid/margin` | 120 |
| `grid/gutter` | 32 |

The documentation lists three grid sizes, so these variables probably have per-breakpoint modes; only the Desktop values were returned. [DERIVED]

### 1.2 Documented grid specs [EXTRACTED as documentation text, `1558:55670` / `1558:51715`]

| Grid class | Frame width | Columns | Margin (L/R) | Gutter | Column width | Type |
|---|---|---|---|---|---|---|
| Mobile | 360 px | 4 | 16 px | 16 px | Auto | Stretch |
| Desktop | 1440 px | 12 | 120 px | 32 px | Auto | Stretch |
| Large Desktop | 1920 px | 12 | 140 px | 32 px | Auto | Stretch |

Grid overlay colour: `#004FEB` (= `Brand/Blue/500`); an additional field "24" accompanies the colour — meaning not labelled (likely overlay opacity %). [EXTRACTED value / meaning unconfirmed]

Derived column widths [DERIVED]: Desktop (1440 − 2×120 − 11×32) / 12 = **70.67 px**; Large (1920 − 2×140 − 11×32) / 12 = **107.33 px**; Mobile (360 − 2×16 − 3×16) / 4 = **70 px**.

Documented behaviour: "Responsive Column Grid", "Fixed Margins & Gutters", breakpoints "Mobile, Desktop, Large Desktop". Usage rules 01–08 (align to grid, respect margins, use column spans for hierarchy…) in `1558:55994`.

### 1.3 Layout frames `1558:56469`

| Frame | Node | Size |
|---|---|---|
| Mobile | `1561:56879` | 360 × 800 |
| Desktop | `1561:56902` | 1440 × 1024 |
| Desktop | `1561:56904` | 1920 × 1080 |

### 1.3.1 Mobile reference width inconsistency [added 2026-11-19]

| Source | Mobile width | Node(s) | Evidence |
|---|---|---|---|
| Foundations — grid spec & layout frame | **360** | `1558:55670`, `1561:56879` | [EXTRACTED] |
| Patterns › Sample Screen — mobile frames | **360** × 800 | `1627:11756`, `1629:11987` | [EXTRACTED] |
| Patterns › PDP — PDP V1 mobile screens | **393** | `1214:11887`, `1218:13662`, `1280:10398`; TOP NAV `1214:12126` (393 × 97); Bottom Nav Bar `1242:19336` (393 × 120) | [EXTRACTED] |
| Patterns › PDP — other mobile frames | 360 | `1171:9676` (Mobile 360 × 1536), `1201:9774` (Top Nav Bar 360 × 58) | [EXTRACTED] |
| Dropdown `Platform=Mobile` | 352-wide component | `1451:25521` | [META] — component width, not viewport |

Interpretation: the 4-column Mobile grid is specified at 360 (2 × 16 margins); PDP V1 screens are drawn at 393. Which width is the reference is **unresolved** (D-07). *Source: `13` §D-07.*

### 1.4 Breakpoints

Only **design frame widths** are defined (360 / 1440 / 1920). **Responsive breakpoint ranges are [MISSING]**: no tablet size, no min/max widths, no rule for widths between 361–1439 px, no max content width. These are required for CSS media queries and for the Mobile→Desktop typography switch (`03-typography.md`).

---

## 2. Spacing

**No spacing scale is defined** in the file [MISSING]:
- No Spacing foundation page.
- No spacing variables returned by `get_variable_defs` on any foundation section (only `grid/*`).
- Components use auto-layout gaps/padding (e.g. 2, 4, 16 px seen in specimens) as raw values.

Phase 4 will collect every padding/gap value used by components to propose an evidence-based spacing scale for approval. No values will be invented.

---

## 3. Radius

### 3.1 Documented scale [EXTRACTED as documentation text, table `1561:57646`]

| Token | Mobile | Desktop | Usage | Remarks |
|---|---|---|---|---|
| Radius/4 | 4 | 4 | Small UI elements | Use for compact components |
| Radius/8 | 8 | 8 | Inputs, small cards | General small radius |
| Radius/12 | 12 | 12 | Buttons, cards | General-purpose radius |
| Radius/14 | 14 | 14 | Medium components | Use where 12px feels too tight |
| Radius/16 | 16 | 16 | Cards, containers | Common large component radius |
| Radius/18 | 18 | 18 | Larger cards | Use selectively |
| Radius/24 | 24 | 24 | Large surfaces | Large containers / sheets |
| Radius/26 | 26 | 26 | Large visual components | Use selectively |
| Radius/28 | 28 | 28 | Large cards / promotional UI | Use selectively |
| Radius/32 | 32 | 32 | Large containers | Strongly rounded surfaces |
| Radius/34 | 34 | 34 | Special large components | Use only where required |

Second mapping table `1561:57576` (labelled "VARIABLE NAME … MAPPING CLASS") names them `variables.collection2ColourUsage.Radius/N` with classes: 4 Subtle/Badge/Tag · **8 Small/Button/Input** · 12 Standard/Component/Form · 14 Standard Accent · 16 Large/Medium Cards · 18 Large Accent · 24 Large/Desktop Grid Layout · 26 Extra Large/Drawer · 28 Extra Large Accent · 32 Extra Large/Bottom Sheet · 34 Extra Large/Splash Surface.

Groups (`1561:57412`): Small, Standard, Large, Extra Large. Summary table `1561:57523`: Standard Elements 12 px · Large Elements 16 px · Extra Large Surfaces 24 px.

Guidelines (`1561:57549`): DO use scale variables; nested radius smaller than parent. DON'T use raw pixel values; don't apply extra-large radii to small badges.

### 3.2 Applied values [APPLIED]

`get_design_context` on specimen `1561:57341`: shape `1561:57343` uses `rounded-[4px]` — a **raw value, not a variable**. `get_variable_defs` on the whole radius frame `1561:56909` and specimen grid `1561:57340` returned **no radius variables** (only `icon/primary`). → Radius "variables" exist as documentation text only; none are bound. [DERIVED]

### 3.3 Radius values used outside the scale

| Where | Values | Evidence |
|---|---|---|
| Input Field (Outline/Filled) `Radius` variant property | 4, **6**, 8, **10**, 12 | `1066:37962`, `1066:40663` |
| Radius page container `1561:57342` | 8 | [APPLIED] |

---

## 4. Findings

| # | Finding | Severity | Tag |
|---|---|---|---|
| L1 | **No spacing scale** anywhere in the file. | High | [MISSING] |
| L2 | **No responsive breakpoint ranges**; only 3 frame widths. No tablet. | High | [MISSING] |
| L3 | Grid variables exist but only Desktop values are visible; mode names for Mobile/Large not retrievable with read tools. | Medium | [INACCESSIBLE] |
| L4 | Radius tokens documented as variables but **not bound** on the radius page itself; specimens use raw px — contradicting the page's own DO/DON'T rules. | Medium | [DERIVED] |
| L5 | Radius usage conflict: Button/Input → Radius/8 (`1561:57590`) vs Buttons → Radius/12 and Inputs → Radius/8 (`1561:57673`) vs "Standard Elements 12 px" (`1561:57530`). | High | [EXTRACTED] |
| L6 | Input uses radius 6 and 10, not in the scale. | Medium | [EXTRACTED] |
| L7 | Radius scale has irregular steps (14, 18, 26, 34) with "use selectively" remarks — candidates for consolidation. | Low | [DERIVED] |
| L8 | Collection name `collection2ColourUsage` (as written in docs) holds radius — misleading name. | Low | [EXTRACTED] |
| L9 | Documentation chrome uses **Montserrat** and hard-coded `#6b7280` / `#030a14` (radius specimen labels) — not the product typeface or palette. Affects docs only, but `#6b7280` is not in any colour scale. | Low | [APPLIED] |
| L10 | Copy-paste headers: Radius page `_Status` = "COLOUR SYSTEM" (`1561:57266`); Grid doc footer "COLOUR SYSTEM" (`1558:55670`); Mobile grid spec labelled "Desktop" (`1558:51715`). | Low | [EXTRACTED] |
| L11 | Lowercase colour variables also appear here: `background/secondary` `#f5f9ff` (≠ `Brand/Background/Secondary` `#f6f7f9`), `background/light` `#fafcff`, `icon/primary` `#000204` (≠ `Brand/Icon/Primary` `#0b0c0f`). *[2026-11-19: now counted in `02-color.md` §2.2 as conflicts 7–8.]* | Medium | [EXTRACTED] |
| L12 | **Mobile reference width inconsistent**: Foundations and Sample Screen use 360; PDP V1 screens use 393 (§1.3.1). *[Added 2026-11-19 — `13` §D-07.]* | Medium | [EXTRACTED] |

---

## 5. Open questions

0. Reference mobile width: 360 or 393? *(added 2026-11-19)*
1. Breakpoint ranges (e.g. mobile < X ≤ desktop < Y ≤ large)? Is tablet in scope?
2. Max content width for Large Desktop?
3. Is a spacing scale intended (e.g. 4-pt)? If so, which values?
4. Final radius for Button and Input (8 or 12)? Are 6 and 10 allowed?
