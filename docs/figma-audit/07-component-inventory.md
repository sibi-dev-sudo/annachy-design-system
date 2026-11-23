# 07 — Component Inventory

| Item | Value |
|---|---|
| Phase | 4 — complete (component-level). Detailed specs in `components/*.md`. |
| Method | Per-variant `get_design_context` (29 calls, incl. 1 sparse whole-set response) and `get_variable_defs` (64 calls), plus saved `get_metadata`. All read-only. No downloads. See `audit-progress-log.md`. |
| Coverage | Representative variants per state at one size (and a size sweep for Button). Not every one of the 1,397 variants was inspected individually; gaps are listed per spec. |

---

## 1. Inventory

| # | Component | Set node | Variants | Properties | States present | Spec |
|---|---|---|---:|---|---|---|
| 1 | Button | `887:2492` | 432 | Type ×6, State ×6, Size ×12; label, 3 booleans | Default, Hover, Focus, Pressed, Disabled, Loading | `button.md` |
| 2 | Button (gradient) | `1153:3370` | 55 | Size ×11, State ×5; label, 3 booleans | Default, Hover, Focus, Pressed, Disabled | `button.md` §2 |
| 3 | Input Field / Outline | `1066:37962` | 150 | State ×6, Size ×5, Radius ×5; 4 text, 3 booleans | Default, Focused, Filled, Error, Disabled, Success (**no Hover**) | `input.md` |
| 4 | Input Field / Filled | `1066:40663` | 175 | State ×7, Size ×5, Radius ×5; 4 text, 7 booleans, 4 instance-swaps | + Hover | `input.md` |
| 5 | Dropdown / Menu | `1451:25521` | 48 | Selection, Platform, Theme, Search, Footer | (container) | `dropdown.md` |
| 6 | Dropdown / Item | `1451:25092` | 40 | Selection, Platform, Theme, State ×5; label | Default, Hover, Focus, Selected, Disabled | `dropdown.md` |
| 7 | Checkbox | `1504:53300` | 126 | State ×7, Size ×3, Position, Alignment; 2 text, 2 booleans | Checked, Multi-select, Unchecked, Focus, Pressed, Disabled, Disabled On (**no Hover/Error**) | `checkbox.md` |
| 8 | Radio | `1504:52363` | 108 | State ×6, Size ×3, Position, Alignment | Selected, Unselected, Focus, Pressed, Disabled ×2 (**no Hover/Error**) | `radio.md` |
| 9 | Toggle | `1504:54471` | 180 | State ×10, Size ×3, Position, Alignment | On/Off × {rest, Hover, Focus, Pressed, Disabled} | `toggle.md` |
| 10 | Selection Controls | `1504:57173` | 3 | Control Type | wrapper | `selection-controls.md` |
| 11 | Tooltip | `1448:16825` | 80 | Device, Mode, Arrow ×10, Format; content, heading | (static) | `tooltip.md` |
| 12 | Navigation | — | 0 | — | **[MISSING] — pages empty** | `navigation.md` |

Total current component variants: **1,397** (+ 40 duplicate Dropdown/Item in Archive excluded).

## 2. Sub-components & dependencies

| Dependency | Node | Used by |
|---|---|---|
| Icon source **S5 — Annachy Icons File** (Outline + Filled; sizes XS 16 / S 20 / M 24 / L 32 / XL 40) — e.g. `Home/Home 54` `1777:9468`, `User/User Curved` `1779:36485`, `Arrow/Chevron Up/Down` `1779:38813`/`1779:39438`, `Alerts/Error circle` `1780:40127` | various `17xx:` | Button, Input/Outline, Dropdown |
| Solar pilot icons (`Cloud`, `561:36135`) | `561:*` | Input/Filled |
| `functional/check` | `1504:53703` | Checkbox |
| Loading Dots vector | `887:2163` | Button Loading |
| Input Field / Outline (nested) | `1066:38094` | Dropdown search region |
| All Buttons Primary 40 (nested) | `887:363` | Dropdown footer |
| Dropdown / Item (nested) | `1451:25072…` | Dropdown / Menu |

**New finding:** a further icon source — **S5** (Annachy Icons File; originally reported here as the "fifth icon source") *[Naming standardised to S5 on 2026-11-19; see `06` §1 for S1–S6 labels.]* — exists (`17xx:` nodes) with its own model (Style Outline/Filled × Icon Size XS–XL) and Figma descriptions such as *"Manually verified Outline + Filled pair … user-confirmed during catalogue review"*. **Phase 5:** located — these are instances of the external published library **"Annachy Icons File"**; the `17xx` IDs are hidden internal copies (see `11-dependencies-and-sources.md` §1).

## 3. Effect styles discovered in components (not on the Shadow page)

| Style | Used by | Layers |
|---|---|---|
| `Button/Default` | Checkbox Checked, Radio Selected | 4 × `#17191C` |
| `Button/Hover` | Checkbox/Radio Pressed | 5 × `#325CB3` |
| `Button/Focus` | Dropdown Item Focus, Checkbox/Radio Focus | 5 × `#0141C0` |
| `Toggle/On`, `Toggle/Off`, `Toggle/Press` | Toggle | 4–5 layers |
| `shadow/sm` (uses `Blur/blur-*`, `Colors/alpha/50`) | Checkbox/Radio Focus | 2 layers |

## 4. Typography styles used by components [BOUND]

| Style | Size / LH | Weight | Used by |
|---|---|---|---|
| Body XS — Semibold (vars `XXS-Semibold`) | 12/18 | 600 | Button 24–26 |
| Body S - Semi (vars `XS-Semibold`) | 14/18 | 600 | Button 28–32, Tooltip |
| Heading/H7 — Semibold | 16/18 | 600 | Button 36–42, Input label |
| Heading/H6 — Semibold | 18/20 | 600 | Button 46–48 |
| Heading/H5 — Semibold | 20/24 | 600 | Button 52–56 |
| Body S — Regular | 14/20 | 400 | Input description/sub-text, selection-control subtext |
| Body M — Medium | 16/24 | 500 | Input value |
| Body M — Regular | 16/24 | 400 | Dropdown search |
| Label Small — Medium | 14/20 | 500 | Dropdown item, Selection Controls wrapper |
| Label Medium — Medium | 16/21 | 500 | Checkbox/Radio/Toggle label |
| Label XSmall — Regular | 12/17 | 400 | Tooltip description |

All match **Scale A (Typography System)** values — evidence that Scale A is the operative scale (`03-typography.md`). Where Scale A Mobile and Desktop values differ (H7, H6, H5, Body S Regular, Label Medium, Label XSmall), components resolve the **Mobile** values (`03` §4.1, T12). *[Clarified 2026-11-19 — `13` §D-04/D-05.]* Scale A remains a candidate; **D-04 is open**.

## 5. Cross-component findings (summary — detail in specs and `08-inconsistencies.md`)

| # | Finding | Components |
|---|---|---|
| X1 | **Focus treatment inconsistent**: 2px border (Button Primary/Secondary), 1px colour change (Input), 2px border + `Button/Focus` glow (Dropdown, Checkbox), none visible (Link Hover). | All |
| X2 | **Hover missing** on Input/Outline, Checkbox, Radio; **Link Hover identical to Default**. | Input, Checkbox, Radio, Button |
| X3 | **Error state missing** on Checkbox, Radio, Toggle, Dropdown. | Selection controls, Dropdown |
| X4 | **Foreign tokens** in components: `surface-bg`, `border-default`, `shadow/sm`, `Blur/*`, `Colors/alpha/*`; raw `#3a6ff7`. | Checkbox, Radio, Input |
| X5 | **Theme modelled three ways**: variable Dark mode, `Theme=Light/Dark` (Dropdown), `Mode=dark/light` (Tooltip). | Dropdown, Tooltip |
| X6 | **Flattened vectors** for Radio dot and Toggle track — not tokenised. | Radio, Toggle |
| X7 | Status colours: components use icon semantic vars (`error #e72b23`, `success #276732`, 600 shades) instead of `Brand/Feedback/*` (500 shades). | Input |
| X8 | Off-palette state colours: `#e8f0ff`, `#f3f4f7`, `#e4e7ec`, `#3a6ff7`, `#e1e1e2`, `#ffffff`. | Button, Input, Checkbox, Radio |
| X9 | Missing components: Navigation (Mobile/Desktop), Select trigger. | — |
