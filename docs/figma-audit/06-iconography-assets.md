# 06 — Iconography & Assets

| Item | Value |
|---|---|
| Source pages | › ③ Iconography ◐ `375:10889` · Archive › ① Component Source `556:2` · Research › Brainstorming `0:1` |
| Method | Structure from saved `get_metadata`; `get_variable_defs` on pilot doc `1106:12812`. Read-only. |
| Status | **Foundations part complete** (structure, variants, colours, sources). **Asset download pending (Phase 5)** — needs scope decision (§6). |

---

## 1. Icon locations compared

| Location | Node | Role (assessed) | Icons | Variant model | Components |
|---|---|---|---:|---|---:|
| Iconography — 37 category frames | `478:68250` … `478:95749` | Catalogue / browsing sheet | 1,243 slots (1,226 unique names) | `Style` only (6), 24 × 24 | ≈7,518 |
| Iconography — 52 pilot frames | `556:190` … `564:16445` | **Pilot of the target icon system** | 52 | `Style (6) × Size (9) × Semantic state (5)` = 270 | 14,040 |
| Archive › Component Source | `556:2` (240 frames, `892:2` …) | **Full source of the pilot model** | 240 | same 270-variant matrix | 64,800 |
| Brainstorming › Icons | `5:15097`, `5:12734` | Exploration — comparing icon libraries (Lucide, Tabler, Huge Icons, Phosphor, Solar) | ~1,054 × 2 styles | `Style=Outline/Filled` | 10,547 |
| **External library — "Annachy Icons File"** *(added 2026-11-19)* | library key `lk-826bf23d…382636`; in-file hidden copies e.g. `1777:9468`, `1779:36485` | **Used by production components** (Button, Input/Outline, Dropdown) | unknown total | `Style` Outline/Filled × `Icon Size` XS 16 · S 20 · M 24 · L 32 · XL 40 | not countable |
| **External library — "UI Icons"** *(added 2026-11-19)* | library key `lk-c918…09544` | Candidate; **no observed use** | unknown total | single components, kebab-case names (`chevron-down`, `alert-circle`, `home-03`) | not countable |

[EXTRACTED counts; roles DERIVED from names and structure.]

**External library status (unverified):** both libraries were found via `search_design_system` (Phase 5, `11` §1–3). Neither is reported by `get_libraries`; **file keys are unknown, so neither can be inspected or exported; ownership by Annachy is unverified** (D-13, D-14). Annachy Icons File component sets show `updatedAt` 2026-11-19 (actively edited). *[Corrected 2026-11-19 — this section originally listed only the four in-file locations; the external libraries were recorded only in §8.]*

Source labels used across reports: S1 = category catalogue, S2 = pilots, S3 = Component Source, S4 = Brainstorming, S5 = Annachy Icons File, S6 = UI Icons.

Overlap [DERIVED]: all 52 pilot icons exist in Component Source; 233 of 240 Component Source icons also appear in the Iconography categories; 7 do not (`Cloud Sun 1`, `Cloud Sun 2`, `Record 1`, `Record 2`, `Soundwave 1/2/3`).

---

## 2. Icon system model (pilot `1106:12812` "Wind — icon system pilot")

Documented: *"Style × Size variants · semantic state variables · Light/Dark modes"*, *"Default: Linear · 24px | Duotone opacity preserved from source"*.

| Property | Values |
|---|---|
| `Style` (6) | Linear *(default)*, Bold, Bold Duotone, Broken, Line Duotone, Outline |
| `Size` (9) | 14, 16, 20, **24** *(default)*, 28, 32, 36, 38, 42 |
| `Semantic state` (5) | Brand, Disabled, Error, Success, Warning |

Semantic state colours [EXTRACTED, `get_variable_defs` on `1106:12812`]:

| Variable | Value | Matches |
|---|---|---|
| `brand` | `#004feb` | Brand/Blue/500 |
| `disabled` | `#bfc4cf` | Brand/Blue-Grey/300 |
| `error` | `#e72b23` | Brand/Error/**600** |
| `success` | `#276732` | Brand/Success/**600** |
| `warning` | `#b9512e` | Brand/Warning/**600** |

No "Default/Neutral" state exists — a default (e.g. `currentColor` / text colour) icon colour is [MISSING]. Light/Dark mode values: only one set returned (mode not visible) [INACCESSIBLE].

Icon size 38 matches Button size 38 (an odd step) — possibly paired with button sizes [DERIVED].

---

## 3. Icon library origin

Style names (Linear, Bold, Bold Duotone, Broken, Line Duotone, Outline) and category names (including the misspelling "Essentional, UI") match the publicly available **Solar** icon set; Brainstorming has a section explicitly named "Solar Icons". [DERIVED — likely, not confirmed in file]

⚠ Licence of the icon source must be confirmed (and attribution recorded) before icons are redistributed in this library. Other assets with third-party origin: "Iconly Pro" icons on Sample Screen (`1651:893`, `1662:896` …) — a commercial set.

---

## 4. Icon categories (Iconography page)

37 categories with icons [EXTRACTED]: Weather, Video/Audio/Sound, Users, Transport/Parts/Service, Time, Text Formatting, Sports, Shopping/Ecommerce, Settings/Fine Tuning, Security, Search, School, Notifications, Notes, Network/IT/Programming, Nature/Travel, Money, Messages/conversation, Medicine, Map & Location, List, Like, Home/Furniture, Hands, Food/Kitchen, Folders, Files, Faces/Emotions/Stickers, **Essentional, UI** (148), Electronic/Devices, Design/Tools, Call, Business/Statistic, Building/Infrastructure, Astronomy, Arrows Action, Arrow.

Empty/odd frames: `Planet 6` `504:9` (empty), `Info Banner` `478:96941` (empty), `Attention` `478:96923` (no components), duplicate empty `Wind` `890:1905`.

---

## 5. Other assets

| Asset | Node(s) | Type | Notes |
|---|---|---|---|
| Annachy logotype | `1561:57274` (and identical copies in every doc header: `1567:2153`, `1568:38579`, `1563:58306` …) | Vector group | Primary brand logo candidate for `src/assets/` |
| Logo badge/frame | `1561:57269` "Frame 2121455714" 156×156 | Frame | Contents to inspect in Phase 5 |
| Cover thumbnail | `1556:3` | Image | Documentation only |
| Unsplash photos | `254:13413`, `1563:58695`, `1563:58714`, `1563:58732`, `1563:58747` … | Raster | Documentation backgrounds — not library assets |
| Third-party brand logos | Amazon `254:13503`, Flipkart `254:13504` | Raster/vector | Research only — **must not ship** |
| Fonts | Proxima Nova | — | Not exportable from Figma; licence required (see `03-typography.md`) |

---

## 6. Download plan (Phase 5 — awaiting decision)

`download_assets` verified as export-only (inputs: fileKey, nodeId, optional format/scale; returns temporary URLs; no write inputs). Files will be saved locally to `docs/figma-audit/raw/assets/` (staging), original SVG preserved, no format/scale overrides.

Scale consideration: the full pilot model is **64,800 components** (240 icons × 270). Exporting every variant is unnecessary because Size and Semantic state are achievable in CSS (`width/height`, `color: currentColor`). Proposed minimal export:

| Option | Scope | Approx. files |
|---|---|---:|
| A (recommended) | 240 Component Source icons × 6 Styles at 24 px, one state | 1,440 SVG |
| B | Only `Linear` style (documented default) for 240 icons | 240 SVG |
| C | Full Iconography catalogue (1,243 icons × 6 styles) | ~7,500 SVG |

Each `download_assets` call returns at most 20 SVGs per node, so the export is batched per icon frame. Decision needed: **which option, and is Component Source (Archive) or the Iconography catalogue the canonical source?**

---

## 7. Findings

| # | Finding | Severity | Tag |
|---|---|---|---|
| I1 | Icons stored in **4 in-file locations** (~96,900 components) **plus 2 external libraries** — six candidates; canonical source undefined. *[Corrected 2026-11-19 — originally "Icons stored in 3 locations".]* | High | [EXTRACTED] |
| I2 | The production-grade icon model (270 variants) lives on an **Archive** page; the Iconography page (◐ in progress) holds only 52 pilots. | High | [EXTRACTED] |
| I3 | Icon semantic colours use 600 shades while UI Feedback tokens use 500 shades (`Brand/Feedback/Error #ff614e` vs icon `error #e72b23`). | Medium | [EXTRACTED] |
| I4 | No default/neutral icon colour state. | Medium | [MISSING] |
| I5 | 17 duplicate icon names within the catalogue (1,243 slots, 1,226 names). | Low | [DERIVED] |
| I6 | Typos: "Essentional, UI", "Clound Cross"; empty frames `Planet 6`, `Info Banner`. | Low | [EXTRACTED] |
| I7 | Third-party icon sets (Solar — likely; Iconly Pro — commercial) — licensing to confirm. | High (legal) | [DERIVED] |
| I8 | Brainstorming `5:12734` contains a bottom tab-bar exploration (`Selected=Home/Category/Cart/Profile`, 393 px wide) — the only navigation-like material in the file, while both Navigation pages are empty. | Info | [EXTRACTED] |

---

## 8. Phase 5 update — additional sources (see `11-dependencies-and-sources.md`)

| # | Source | Used by components? |
|---|---|---|
| S5 | **Annachy Icons File** — external published library (`lk-826bf23d…`), Outline/Filled × XS 16–XL 40, updated 2026-11-19 | **Yes** — Button, Input/Outline, Dropdown |
| S6 | **UI Icons** — external org library (`lk-c918…`), kebab-case single components | No evidence |
| S4 | Brainstorming › Lucide — `lucide:badge-check` (`5:15330`) | **Yes** — Dropdown Item Selected |
| S2 | Iconography pilot `Cloud` (`561:36765`) | **Yes** — Input/Filled |

Correction to §1: four locations in this file plus **two external libraries** — six candidates in total. No canonical source selected.
