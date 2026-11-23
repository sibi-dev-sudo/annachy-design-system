# 11 — Dependencies & Source Investigation (Phase 5)

| Item | Value |
|---|---|
| Date | 2026-11-19 |
| Operations | `get_metadata` ×13 (page list; `375:10889` re-read; `1777:9468`; `370:50569`; `1504:53703`; `1451:24796`; `887:2163`; `1214:12125`; `1311:7795`; `1633:30319`; `1471:36870`; `1242:19336`; `1311:7548`), `search_design_system` ×2. Plus offline analysis of saved metadata. **All read-only. No downloads/exports.** |
| Skipped | `download_assets` (not authorised this phase); `create_session` (read-only nature unproven). Nothing else was uncertain. |
| Canonical selection | **Not made** — candidates only, per instruction. |

Tags: **[EXTRACTED]** tool output · **[DERIVED]** reasoning from extracted data · **[INACCESSIBLE]** could not be read.

---

## 1. Icon source S5 — Annachy Icons File (`17xx` nodes) — located

*[Naming standardised to S5 on 2026-11-19; see `06` §1 for S1–S6 labels.]* Earlier phases called this the "5th icon source".

### 1.1 Evidence chain

| Step | Operation | Result | Tag |
|---|---|---|---|
| 1 | Search all saved page XML for `1777:9468`, `1779:36485`, `1779:38813`, `1779:39438`, `1780:40127`, `1777:12415` | Not present on any page | [EXTRACTED] |
| 2 | Re-read page list | Unchanged — 39 pages | [EXTRACTED] |
| 3 | Re-read Iconography `375:10889` | Byte-identical size to Phase 3 (2,906,662 chars) → page unchanged, no `17xx` nodes | [EXTRACTED] |
| 4 | `get_metadata` on `1777:9468` | Error: *"invalid node selection… select a node from a visible page"* → node exists in the document but **not on any visible page** | [EXTRACTED] |
| 5 | `get_metadata` on `370:50569` (source layer named in its description) | Error: *"node ID was not found in the file"* | [EXTRACTED] |
| 6 | `search_design_system` "Home 54", "User Curved", "Error circle", "Chevron Down" | All found in published library **"Annachy Icons File"** | [EXTRACTED] |

### 1.2 Conclusion

The `17xx` icon components are **instances of a separate, published Figma library — "Annachy Icons File"** (`libraryKey lk-826bf23d…382636`). The `17xx` IDs are this file's hidden internal copies of those remote components (Figma stores imported library masters off-canvas) [DERIVED from steps 4–6]. Their descriptions reference source layers (e.g. `370:50569`, `379:123577`, `414:87684`, `32:2085`) that exist **in the Annachy Icons File, not here** [DERIVED].

| Property | Value |
|---|---|
| Library | Annachy Icons File |
| Library key | `lk-826bf23d92b87402715c3221e0b1b8e067f2e85dc89aa41f637251790c0a6d8dc21deb0d184e945cc26e4858907a829c0b9ea8f2b03f0acc2d06f00b4f382636` |
| File key | **[INACCESSIBLE]** — not exposed by search results; library cannot be inspected without it |
| Model | Component sets; `Style` Outline/Filled (some single-style); `Icon Size` XS 16 · S 20 · M 24 · L 32 · XL 40 |
| Naming | `Category/Name` (e.g. `Home/Home 54`, `User/User Curved`, `Arrow/Chevron Down`, `Alerts/Error circle`, `Banking/Bank Carrd star`, `Transport/Car Select`) |
| Activity | `updatedAt` 2026-11-19 09:56–11:07 UTC on all returned sets — **actively being built today** |
| Curation notes in descriptions | "Manually verified Outline + Filled pair", "match: primary-visual", "match: auto-confirmed-single", "Original sources untouched" |

### 1.3 Contradiction with Phase 3

`get_libraries` (Phase 3) returned `libraries_added_to_file: []` and listed only community kits as available. Yet this file contains instances of the Annachy Icons File, and search also surfaces two more organisation libraries (below). → `get_libraries` does not reflect libraries whose components are already in use or organisation libraries [DERIVED]. **`01-file-inventory.md` "Linked libraries: None" corrected.**

---

## 2. All icon / glyph sources used by components

| Component | Element | Source | Node / key | Location type |
|---|---|---|---|---|
| Button (All Buttons) | left/right icon | **Annachy Icons File** — `Home/Home 54` (Outline, S 20) | instance `1777:12415`, set `1777:9468` | External library |
| Button (All Buttons) | Loading | Local vector "Loading Dots": 3 ellipses 6 × 6, gaps 5 (frame 28 × 6) | `887:2163`–`887:2166` | Local, inside component |
| Button (gradient) | icons | Annachy Icons File — `Home/Home 54` | `1777:12415` | External library |
| Input / Outline | left icon | Annachy Icons File — `User/User Curved` (Outline, M 24) | `1779:37533` | External library |
| Input / Outline | right icons | Annachy Icons File — `Arrow/Chevron Up`, `Arrow/Chevron Down` (Filled, M 24) | `1779:38814`, `1779:39439` | External library |
| Input / Outline | sub-text icon | Annachy Icons File — `Alerts/Error circle` (Outline, XS 16) | `1780:40128` | External library |
| Input / Filled | left/right/sub-text icon slots | **Iconography pilot (Solar model)** — `Cloud` `Style=Linear, Size=24/14, Semantic state=Brand` | `561:36135`, `561:36137` (set `561:36765`, Iconography page) | Local, Foundations page |
| Dropdown / Item | Selected indicator | **Lucide** `lucide:badge-check` | instance `1451:24796` → master `5:15330` (Brainstorming › Icons › Lucide.dev `5:15098`) | Local, **Research/exploration page** |
| Dropdown / Menu | search icon | Annachy Icons File — `User/User Curved` (via nested Input) | `1779:37533` | External library |
| Dropdown / Menu | footer icon | Annachy Icons File — `Home/Home 54` (via nested Button) | `1777:12415` | External library |
| Checkbox | check | Local frame `functional/check` (20 × 20) — not an instance | `1504:53703` | Local, inside component |
| Radio | ring/dot | Flattened vector image | `1504:52686` | Local, inside component |
| Toggle | track/thumb | Flattened vector image | `1504:54624` | Local, inside component |
| Tooltip | arrow | Polygon vector | `1429:16126` | Local, inside component |

**Icon sources actually used by production components: 3** — Annachy Icons File (external), Iconography Solar pilot (local), Lucide exploration (local, Research page). Plus 4 local in-component vectors.

---

## 3. Complete icon-source candidate register (no selection made)

| # | Source | Where | Size | Model | Used by components? | Notes |
|---|---|---|---|---|---|---|
| S1 | Iconography catalogue | `375:10889` category frames | 1,243 slots | Style ×6 (Solar), 24 px | No | Page marked ◐ |
| S2 | Iconography pilots | `375:10889` pilot frames | 52 icons | Style ×6 × Size ×9 × State ×5 | **Yes** — Input/Filled (`Cloud`) | |
| S3 | Archive › Component Source | `556:2` | 240 icons | same as S2 | No | Archive page |
| S4 | Brainstorming › Icons | `0:1` › `5:15097`, `5:12734` | ~1,054 × 2 | Lucide, Tabler, Huge Icons, Phosphor, Solar sections | **Yes** — Dropdown Selected (`lucide:badge-check`) | Research page |
| S5 | **Annachy Icons File** (external library) | separate file | unknown total | Outline/Filled × XS–XL | **Yes** — Button, Input/Outline, Dropdown | Updated today; curated |
| S6 | "UI Icons" (external org library) | `lk-c918…09544` | unknown | single components, kebab-case (`chevron-down`, `alert-circle`, `home-03`) | No evidence of use | Updated 2026-04-16 |
| — | Iconly Pro | Sample Screen frames `1651:893`, `1662:896`… | few | — | No (screens only) | Commercial set |

Size-scale conflict between candidates [EXTRACTED]: S2/S3 sizes 14/16/20/24/28/32/36/38/42; S5 sizes 16/20/24/32/40.

---

## 4. Other dependencies traced

### 4.1 Nested component instances

| Parent | Nested | Override |
|---|---|---|
| Dropdown / Menu (Search=On) | Input Field / Outline (`I1451:23740;1066:*`) | placeholder text "Search teams", `Text/Secondary` colour, Body M Regular |
| Dropdown / Menu (Footer≠None) | All Buttons Primary 40 (`1451:23803`) | label "Apply selection"; text style → Label Small Medium 14/20 |
| Dropdown / Menu | Dropdown / Item ×4 (`1451:25072…`) | labels, states |
| Selection Controls (wrapper) | `.Selection Controls / *` | label style Label Small 14/20 |

### 4.2 Variable collections observed in bindings (names as returned)

| Group | Examples | Origin |
|---|---|---|
| `Brand/*` (Title Case) | `Brand/Blue/500`, `Brand/Button/Primary/Background/Hover`, `Brand/Text/Primary` | Annachy — has Light & Dark mode |
| lowercase scheme | `text/primary`, `brand/base/black`, `border/strong` | Annachy docs pages (conflicting values) |
| Icon semantic | `brand`, `disabled`, `error`, `success`, `warning` | Icon pilot; reused by Input |
| Typography | `Font Family/Sans Serif`, `Weight/*`, `Heading/H7/Semibold/*`, `Subheading & Body/Body/*`, `Labels & Captions/Label/*` | Annachy |
| Dimension | `Height/{24…56}`, `Radius/{4,8,12}`, `grid/*`, `Border/{XS,S,M}`, `S` | Annachy |
| **Foreign** | `surface-bg`, `border-default` (Checkbox/Radio); `shadow/sm`, `Blur/blur-0/2`, `Colors/alpha/50`; `--sds-*`, `Text/Neutral/*`, `Background/Neutral/*` | Third-party kits (Simple Design System + one unidentified kit) |

### 4.3 Effect styles (complete list found)

| Style | Defined on Shadow page? | Used by |
|---|---|---|
| `Shadow Scale/*` (17), `Shadow Effects/*` (15) | Yes | docs specimens only (no component use found) |
| `Blur/*` (5), `Glass/*` (3) | Yes (Blur page) | docs only |
| `Shadow` (5-layer) | No | Colour swatches |
| `Button/Default`, `Button/Hover`, `Button/Focus` | **No** | Checkbox, Radio, Dropdown Item |
| `Toggle/On`, `Toggle/Off`, `Toggle/Press` | **No** | Toggle |
| `shadow/sm` | **No** (foreign) | Checkbox/Radio Focus |
| `Shadow/xs…3xl`, `Shadow/* focused 4px *` | No — in external "Design System" library | none observed |

→ **No component uses the documented Shadow Scale / Shadow Effects styles** [DERIVED from all Phase 4 inspections].

---

## 5. Duplicate / legacy / candidate register (no canonical selected)

| Asset | Candidates | Evidence | Status |
|---|---|---|---|
| Button | `887:2492` (Components) · `1590:19040` (EMPTY PAGE) | same names, 360/432 sizes differ | Candidate current vs divergent copy |
| Checkbox | `1504:53300` (Components) · `1500:25474` (Archive) · `1464:10379` "check box" (Archive, 8 variants) | structural copies; legacy 8-variant set | — |
| Radio | `1504:52363` · `1493:3` (Archive) | structural copies | — |
| Toggle | `1504:54471` · `1438:5542` (Archive) | structural copies | — |
| Dropdown / Item | `1451:25092` · `1464:2972` (Archive) | structural copies | — |
| Icons | S1–S6 (§3) | — | — |
| Shadows | Scale · Effects · Button/Toggle styles · external Design System styles | — | — |
| Type scale | Scale A (Typography System) · Scale B (specimen) | components bind Scale A values | — |
| Colour naming | `Brand/*` · lowercase | components bind `Brand/*` | — |

---

## 6. Missing components

### 6.1 Navigation

| Finding | Evidence | Tag |
|---|---|---|
| Navigation · Mobile and · Desktop pages are empty. | `1351:18314`, `1556:7200` | [EXTRACTED] |
| Screen-level navigation exists only as **frames** (not components): PDP Top Nav Bar ×4 (`1201:9774` 360 × 58), TOP NAV ×3 (`1214:12126` 393 × 97), Breadcrumb (`breadcrumb-item` ×4), Desktop **"Main navigation"** `1311:7548` 1440 × 88 (logo 170 × 51, delivery-location selector, search 704 × 44 with mic, profile menu, cart), "Category navigation", "Store navigation", "Category menu". | `581:11523` | [EXTRACTED] |
| "Bottom Nav Bar/Default" `1242:19336` (393 × 120) is a **bottom action bar** (two buttons 144 + 203 wide, 48 h, plus home indicator 140 × 5) — **not** tab navigation. | `1242:19336` | [EXTRACTED] |
| PDP instance "Bottom Nav Bar" `1214:12125` → nested "Bottom Nav Bar/Default" whose master child `1633:30319` is **not found in this file**; no published library match → master deleted or in an unpublished file. | `1214:12125` | [INACCESSIBLE] |
| Brainstorming has tab-bar explorations: `Selected=Home/Category/Cart/Profile` symbols (`5:12734`), sections "Bottom Navigation (Tabler Icons)", instances `navigation-01/02`, 66 "Header" frames. | `0:1` | [EXTRACTED] |
| No breakpoint behaviour, active/hover states, or mobile↔desktop mapping defined. | — | [MISSING] |

### 6.2 Closed Select trigger

| Finding | Evidence | Tag |
|---|---|---|
| No select-trigger component in this file. Dropdown sets cover only the open menu and rows. | `1451:25521`, `1451:25092` | [EXTRACTED] |
| Input Field / Outline includes a right chevron pair (Up+Down) — reads as a numeric stepper, not a select. | `1066:38098` | [DERIVED] |
| Closest in-file patterns: Desktop header "Delivery location" (`1311:7550`: label + value + 16 px chevron-down) and "Profile" (`1311:7564`) — screen frames, not components. | `1311:7548` | [EXTRACTED] |
| A component set named **"Select"** exists in external org library **"Design System"** (`lk-483b…12dd12`, updated 2026-05-04), alongside "Pagination". Whether this library belongs to Annachy is unconfirmed; it is not linked to this file and its file key is unknown. | `search_design_system` | [EXTRACTED] / ownership unknown |

### 6.3 Undocumented components used on screens

Instances on Sample Screen / PDP whose masters are **not in this file's Components section** (masters not found locally; origin unknown): Lab Card, Similar Products- Card, Similar Products - Images, Product card (`1311:7795` → master child `1471:36870` **not found**), Watchlist/Small Button, Watchlist/ Big Button, Watchlist/ Width Big Button, Top Lablel, Product Details Sections, Colour Change Tabs, Normal Size, YL, Review, Category, Colour preview, Size option, Component 30, Action Button, Status Bar/iOS, "Outline / Map & Location / Map Point", Cart icon. [EXTRACTED names; origin INACCESSIBLE]

---

## 7. Corrections applied to local documentation

| File | Correction |
|---|---|
| `01-file-inventory.md` | "Linked libraries: None" → instances from external library *Annachy Icons File* are in use; org libraries *Design System* and *UI Icons* discoverable. |
| `06-iconography-assets.md` | Added sources S5 (Annachy Icons File), S6 (UI Icons); S4 is used in production (Lucide `badge-check`). |
| `07-component-inventory.md` | §2 "parent page not located" → external library. |
| `components/dropdown.md` | Selected indicator source = `lucide:badge-check`; D1 updated with external "Select" candidate. |
| `components/navigation.md` | Added screen-frame navigation evidence and inaccessible Bottom Nav Bar master. |
| `components/button.md` | Loading Dots geometry. |

---

## 8. Unresolved decisions (for design owner)

1. **Canonical icon source** among S1–S6 (and whether Annachy Icons File is the intended production library).
2. Provide the **Annachy Icons File** (and, if relevant, "Design System") file key/URL for read-only audit — needed before any icon export.
3. Icon size scale: 14–42 (9 steps) vs 16–40 (XS–XL).
4. Ownership and status of the external **"Design System"** library (Select, Pagination, focus shadows) and **"UI Icons"** library.
5. Navigation: design in Figma, or approve PDP/Brainstorming frames as interim reference?
6. Select trigger: design in this file, or adopt "Design System › Select"?
7. Where are the masters of Bottom Nav Bar, Product card and other screen components (deleted / other file)?
8. Remove foreign tokens (`surface-bg`, `border-default`, `shadow/sm`, `--sds-*`)?
9. Which shadow system components should use (documented scales are unused).
10. Status of EMPTY PAGE button set and Archive duplicates.
11. Lucide `badge-check` used in production from a Research page — licence/ownership.
