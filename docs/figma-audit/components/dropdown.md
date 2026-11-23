# Component Spec — Dropdown (Menu & Item)

| Item | Value |
|---|---|
| Page | › ③ Input Dropdown ✓ `1351:18309` |
| Component sets | **Dropdown / Menu** `1451:25521` (48) · **Dropdown / Item** `1451:25092` (40) |
| Location | Section `1567:22786` "Dropdown / Core Components"; docs `1567:13261` |
| Duplicate | Dropdown / Item also on Archive › Checkbox `1464:2972` (40 variants) |
| Method | `get_design_context` ×3 (`1451:25175`, `1451:25074`, `1451:25250`); `get_variable_defs` ×3 (`1451:25073`, `1454:1199`, `1451:25265`); dimensions from metadata. Read-only. |

Figma descriptions [EXTRACTED]:
- Menu: *"48 dropdown variants … Checkboxes and selection indicators sit left of option labels. Edit each option by selecting its individual row… Search field and Footer button properties remain exposed. Responsive width and content-driven height."*
- Item: *"40 option-row variants. Left-aligned selection indicators and checkboxes, with fill-width editable labels… Multiple rows may independently use State=Selected. Linked typography and semantic themes."*

---

## 1. Properties

| Set | Property | Values |
|---|---|---|
| Menu | `Selection` | Single, Multiple |
| Menu | `Platform` | Desktop, Mobile |
| Menu | `Theme` | Light, Dark |
| Menu | `Search` | Off, On |
| Menu | `Footer` | None, Label, Icon + label |
| Item | `Selection`, `Platform`, `Theme` | as above |
| Item | `State` | Default, Hover, Focus, Selected, Disabled |
| Item | `label` | Text (default "Product design") |

## 2. Dimensions [META]

| Variant group | Desktop | Mobile |
|---|---|---|
| Item | 320 × 40 (min-height 40) | 352 × 48 |
| Menu, Search Off, Footer None | 320 × 188 | 352 × 220 |
| Menu, Search Off, Footer Label / Icon+label | 320 × 253 | 352 × 293 |
| Menu, Search On, Footer None | 320 × 261 | 352 × 293 |
| Menu, Search On, Footer Label / Icon+label | 320 × 326 | 352 × 366 |

## 3. Anatomy & layout [APPLIED, Desktop Light]

**Menu** `1451:25250`: column, padding 8, gap 8, radius `Radius/12` (12), border 1px `Brand/Border/Primary` `#bfc4cf`, bg `Brand/Background/Secondary` `#f6f7f9`, clip. **No shadow.**
- *Search region* (Search=On): nested **Input Field / Outline** instance (48 px, px 14, `Radius/8`, border `Brand/Border/Primary`, icon `User/User Curved` 24), placeholder "Search teams" Body M Regular 16/24 `Brand/Text/Secondary` `#555d6d`; then 1px divider `Brand/Border/Secondary` `#dcdfe5`; region padding-bottom 8.
- *Options*: column, gap 4, 4 sample rows (Selected, Default ×2, Disabled).
- *Footer* (Footer≠None): padding-top 4, gap 12, 1px divider `Brand/Border/Secondary`, then **All Buttons Primary 40** instance (full width, 40 h, px 16, `Radius/8`, icon Home/Home 54) labelled "Apply selection" — text overridden to **Label Small Medium 14/20** (Button default is H7 Semibold 16/18).

**Item**: row, gap 12, padding 12 / 10, min-height 40, radius `Radius/8`, full width.
- Selection indicator 20 × 20 (Single: check icon when Selected — instance of **`lucide:badge-check`** `5:15330` from Brainstorming › Lucide.dev [Phase 5]; Multiple: checkbox — not inspected).
- Label: **Label Small — Medium** 14/20, weight 500, flex 1.

## 4. Item states (Desktop, Light, Single)

| State | Background | Label colour | Border / effect | Evidence |
|---|---|---|---|---|
| Default | `Background/Secondary` `#f6f7f9` | `Text/Primary` `#0b0c0f` | — | [APPLIED] |
| Hover | `Background/Tertiary` `#edeff2` | `Text/Primary` | — | [BOUND] |
| Focus | `Background/Secondary` | `Text/Primary` | **2px `Button/Primary/Border/Focus` `#003fbc`** + effect style **`Button/Focus`** (below) | [APPLIED] |
| Selected | `Blue/50` `#f3f7ff` | `Blue/500` `#004feb` + check icon 20 | — | [APPLIED] |
| Disabled | `Background/Secondary` | `Text/Tertiary` `#707a8f` | — | [APPLIED] |

Multiple / Selected binds `Blue/500` + `Blue/50` (same as Single) [BOUND].

Effect style **`Button/Focus`** [EXTRACTED] — not documented on the Shadow page:

| Layer | Colour | Offset | Blur |
|---|---|---|---|
| 1 | `#0141C07D` | 0, 0 | 2 |
| 2 | `#0141C06E` | 0, 1 | 3 |
| 3 | `#0141C040` | -1, 2 | 4 |
| 4 | `#0141C012` | -2, 3 | 4 |
| 5 | `#0141C003` | -3, 4 | 5 |

CSS [DERIVED]: `box-shadow: 0 0 2px rgb(1 65 192 / 49%), 0 1px 3px rgb(1 65 192 / 43%), -1px 2px 4px rgb(1 65 192 / 25%), -2px 3px 4px rgb(1 65 192 / 7%), -3px 4px 5px rgb(1 65 192 / 1%)`.

## 5. Dark theme [BOUND on `1451:25265`]

Dark variants bind the **same variable names** resolving to **different values** — i.e. the Brand collection has a Dark mode:

| Variable | Light | Dark |
|---|---|---|
| `Brand/Background/Secondary` | `#f6f7f9` | **`#181b21`** |
| `Brand/Text/Primary` | `#0b0c0f` | **`#fafcff`** |
| `Brand/Border/Primary` | `#bfc4cf` | **`#171e2a`** |
| `Brand/Text/Tertiary` | `#707a8f` | `#707a8f` (unchanged) |
| `Brand/Blue/500` | `#004feb` | `#004feb` (unchanged) |

## 6. Findings

| # | Finding | Severity |
|---|---|---|
| D1 | **No closed "select" trigger component** (field + chevron that opens the menu). The page is "Input Dropdown" but only the open menu and rows exist. Phase 5: an external org library "Design System" has a `Select` set (ownership unconfirmed); in-file closest patterns are header frames `1311:7550`/`1311:7564`. | High (gap) |
| D2 | Menu has **no elevation/shadow** — relies on border only. | Medium |
| D3 | `Button/Focus` effect style exists but is absent from the Shadow foundation page; blue `#0141C0` is not a palette colour. | Medium |
| D4 | Footer button overrides Button typography (14/20 Medium vs 16/18 Semibold). | Low |
| D5 | Theme is a variant property (`Theme=Light/Dark`) *and* variables have a Dark mode — redundant mechanisms; Tooltip uses `Mode=dark/light` (different name & casing). | Medium |
| D6 | Search region reuses Input Field / Outline (dependency), but its placeholder uses `Text/Secondary` `#555d6d`, unlike the Input's own `#dcdfe5` placeholder. | Low |
| D7 | No empty state, loading state, group headers, or max-height/scroll behaviour defined. | Gap |
| D8 | Not inspected: Multiple-selection checkbox indicator, Mobile paddings, Dark Hover/Focus/Selected values. | Gap |

## R4-0 update (2026-11-20)

Read-only evidence in `../r4-0-evidence.md`. Original findings are preserved.
- **D8 resolved:** the Multiple indicator is an icon instance "checkbox" (research-page master, not the R3 Checkbox) with colours `Icon/Secondary` / `Blue/500` / `Border/Primary`. Mobile Item: padding 12, min-height 48, Body M Regular 16/24. Dark Selected is `Blue/500` with a white label.
- The Mobile footer button is 48 tall with a Label Medium 16/21 override.
- The Multiple Menu with no search and no footer has no gap (`1454:1254`).

## R4-1 implementation (2026-11-20)

Implemented in `src/components/dropdown/`: Light, Footer=None, **20 Item + 8 Menu variants**. Evidence is in `../r4-0-evidence.md` §1–§3 and §6.
- **New (§6):** the Item Focus stroke and the Menu 1px stroke are **outside the layout** (Focus 320 × 40; Menu 188 = 8 + content + 8), so both are drawn inset.
- **DD-1 (derived):** the search field's focus border = Input Field / Outline Focused (`#3a6ff7`, IN2).
- **A41:** the Menu boundary is 1.70:1 against the page (D2, no shadow).
- **Not implemented:** Dark (B4-2), Footer (R4-Q3), Select (B4-1).
