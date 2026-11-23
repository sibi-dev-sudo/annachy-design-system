# 01 — File & Page Inventory

| Item | Value |
|---|---|
| File | Annachy CF — Design System |
| File key | `rM3ixSG6i3DFfKZFWuxzs4` |
| Inspected | 2026-11-19 |
| Method | `get_metadata` (page list + every page), `get_libraries` — **read-only** |
| Not used | `create_session` (read-only nature could not be proven from its definition — skipped per policy); `download_assets` (not needed in this phase) |
| Pages found | **39** (matches expected count) [EXTRACTED] |
| Pages accessible | **39 / 39** — no access errors |
| Linked libraries | `get_libraries` reported none subscribed, **but Phase 5 found instances of the external library "Annachy Icons File" in use** (Button, Input, Dropdown), and org libraries "Design System" and "UI Icons" are discoverable via search. See `11-dependencies-and-sources.md` §1.3. [CORRECTED] |
| Phase status | Phase 3 **complete** — page inventory + foundations (`02`–`06`). Next: Phase 4 components. |

Evidence files:
- `raw/metadata/<page-id>.xml` — full raw `get_metadata` XML for the 15 large pages (≈16 MB total).
- `raw/phase3-working-notes.md` — observations for pages that returned inline (raw XML not separately saved for these).
- `raw/variant-matrices.md` — variant properties/values derived from component layer names.

Evidence tags: **[EXTRACTED]** returned by Figma · **[DERIVED]** computed from extracted data · **[VISUAL]** screenshot-only · **[MISSING]** not in Figma · **[INACCESSIBLE]** could not be read.

---

## 1. Page status markers

Page names carry suffix markers. Their meaning is **not documented in the file**; the interpretation below is an assumption.

| Marker | Assumed meaning | Pages |
|---|---|---|
| ✓ | Complete / approved | most Research, Foundations, Components and Archive pages |
| ◐ | In progress | Iconography |
| ○ | Not started | Navigation · Mobile, Navigation · Desktop |
| (none) | Unmarked | Cover, Brainstorming, Sample Screen, PDP, Component Source, EMPTY PAGE |

---

## 2. Complete page list (file order)

Counts are [DERIVED] from saved XML. "Comps" = Figma component nodes (`symbol`); "Inst" = instances. "—" = page returned inline; total node count not measured (component counts for inline pages are exact, counted from variant names).

| # | Page name (as in Figma) | Node ID | Group | Nodes | Comps | Inst | Content summary | Evidence |
|---|---|---|---|---:|---:|---:|---|---|
| 1 | ⓪ START | `375:10885` | Divider/Header | 0 | 0 | 0 | Empty section header | inline |
| 2 | › ① Cover | `375:10886` | Start | 2 | 0 | 0 | Frame `1556:2` "thumbnail" 1611×976 with image `1556:3` | inline |
| 3 | ----- | `375:10888` | Divider | 0 | 0 | 0 | Empty | inline |
| 4 | ① RESEARCH | `367:12000` | Divider/Header | 0 | 0 | 0 | Empty section header | inline |
| 5 | › ① Brainstorming | `0:1` | A. Research | 28,081 | 10,547 | 2,365 | Typography exploration, **icon sections (10,524 components)**, typography usability test, prompts, survey summary | `0-1.xml` |
| 6 | › ② Qualitative · Play Store Reviews ✓ | `373:12671` | A. Research | — | 0 | 0 | Research board `373:12672`: review analysis (2,512 reviews, Jan–Aug 2026) | inline |
| 7 | › ③ Quantitative · Survey Overview ✓ | `373:12818` | A. Research | — | 0 | 0 | Survey screenshots + verbatim responses, frame `373:12819` | inline |
| 8 | › ④ Quantitative · Survey Insights ✓ | `373:12745` | A. Research | — | 0 | 0 | Insights board `373:12746` | inline |
| 9 | › ⑤ Quantitative · Product Analytics ✓ | `373:12852` | A. Research | 859 | 0 | 0 | Section `373:12853` "Annachy Analytics Overview" | `373-12852.xml` |
| 10 | › ⑥ User Personas ✓ | `254:13410` | A. Research | — | 0 | 0 | Persona `254:13412`; contains third-party brand logos (Amazon, Flipkart) | inline |
| 11 | --- | `1556:23522` | Divider | 0 | 0 | 0 | Empty | inline |
| 12 | ② FOUNDATIONS | `1556:5` | Divider/Header | 0 | 0 | 0 | Empty section header | inline |
| 13 | › ① Colour ✓ | `273:10649` | B. Foundations | 7,803 | 0 | 0 | Sections: Brand Colours `1557:23523`, Supporting Colours `1557:25193`, Colour Usage `1557:31595`, COLOUR SYSTEM PROMPT `1557:37808` | `273-10649.xml` |
| 14 | › ② Typography ✓ | `220:10667` | B. Foundations | 1,231 | 0 | 0 | Sections: Typography System `1557:39451`, Screen - Layout `1558:51031`, Typography Documentation `1557:44867` | `220-10667.xml` |
| 15 | › ③ Iconography ◐ | `375:10889` | B. Foundations | 23,241 | 21,558 | 21 | 41 category frames + 52 per-icon "pilot" frames (270 comps each) + "Wind — Icon System Pilot" | `375-10889.xml` |
| 16 | › ④ Grid & Layout ✓ | `317:12589` | B. Foundations | 610 | 0 | 0 | Sections: Grid System (All Sizes) `1558:51715` & `1558:55670`, Layout Frames `1558:56469`; loose screenshot `317:12649` | `317-12589.xml` |
| 17 | › ⑤ Radius ✓ | `365:11441` | B. Foundations | — | 0 | 0 | Section `1561:56908` "Radius-Document": 11 radius tokens + usage tables | inline + notes |
| 18 | › ⑥ Shadow ✓ | `1351:18308` | B. Foundations | — | 0 | 0 | Section `1561:57735`: Shadow Scale `1561:57736` + Shadow Effects `1561:57961` | inline + notes |
| 19 | › ⑦ Blur ✓ | `1351:18312` | B. Foundations | — | 0 | 0 | Section `1563:58295`: Blur & Glass Effects `1563:58296` | inline + notes |
| 20 | --- | `1556:74` | Divider | 0 | 0 | 0 | Empty | inline |
| 21 | ③ COMPONENTS | `375:10890` | Divider/Header | 0 | 0 | 0 | Empty section header | inline |
| 22 | › ① Button ✓ | `375:10891` | C. Components | 1,995 | 487 | 40 | Core Button Components `1563:60424`, docs `1563:58784`, library `1564:67987`, colour usage `1564:64276` | `375-10891.xml` |
| 23 | › ② Input ✓ | `375:10892` | C. Components | — | 325 | 3 | Section `1567:1642` "Input Feild Component Source" | inline + notes |
| 24 | › ③ Input Dropdown ✓ | `1351:18309` | C. Components | 744 | 88 | 95 | Docs `1567:13261`, Core Components `1567:22786` | `1351-18309.xml` |
| 25 | › ④ Checkbox /Radio/Toggle ✓ | `375:10893` | C. Components | 1,091 | 417 | 96 | Core `1568:28311`, Docs `1568:30663`, Master `1568:36951` | `375-10893.xml` |
| 26 | › ⑤ Tooltip ✓ | `1351:18311` | C. Components | — | 80 | 0 | Section `1568:38568` → `1568:40001` → frame `1448:16825` | inline + notes |
| 27 | › ⑥ Navigation · Mobile ○ | `1351:18314` | C. Components | **0** | 0 | 0 | **Empty page** | inline |
| 28 | › ⑦ Navigation · Desktop ○ | `1556:7200` | C. Components | **0** | 0 | 0 | **Empty page** | inline |
| 29 | --- | `1556:77` | Divider | 0 | 0 | 0 | Empty | inline |
| 30 | ④ PATTERNS & SCREENS | `1499:21976` | Divider/Header | 0 | 0 | 0 | Empty section header | inline |
| 31 | › ① Sample Screen | `1375:30857` | D. Patterns & Screens | 1,027 | 0 | 56 | Section `1608:11615`; mobile frames `1627:11756`, `1629:11987` "Job - Listing page"; Iconly Pro icons; screenshots | `1375-30857.xml` |
| 32 | › ② PDP | `581:11523` | D. Patterns & Screens | 2,086 | 0 | 178 | PDP V1 mobile frames `1214:11887`, `1218:13662`, `1280:10398`; Desktop `605:17532`; reference screenshots | `581-11523.xml` |
| 33 | --- | `1556:76` | Divider | 0 | 0 | 0 | Empty | inline |
| 34 | ⑨ ARCHIVE | `375:10898` | Divider/Header | 0 | 0 | 0 | Empty section header | inline |
| 35 | › ① Component Source | `556:2` | E. Archive | 65,043 | **64,800** | 3 | 240 icon frames × 270 components (icon source) | `556-2.xml` |
| 36 | › ② Checkbox ✓ | `1351:18310` | E. Archive | 812 | 174 | 55 | Checkbox (126), legacy "check box" (8), duplicate Dropdown / Item (40), product-page mockups | `1351-18310.xml` |
| 37 | › ③ Radio ✓ | `1489:5449` | E. Archive | — | 108 | — | Radio Button set `1493:3` + docs `1500:22374` | inline + notes |
| 38 | › ④ Toggle ✓ | `1351:18313` | E. Archive | 395 | 180 | 38 | Toggle set `1438:5542` + docs `1504:48004` | `1351-18313.xml` |
| 39 | EMPTY PAGE | `479:4` | **Unclassified** | 713 | 432 | 0 | **Not empty** — frame `1590:18891` "Core Button Components" (duplicate of the button set) | `479-4.xml` |

Totals [DERIVED]: 135,731 nodes across the 15 saved pages (inline pages not counted). Component nodes across all pages: **99,196**, of which **96,905 (≈97.7%) are icons** (Brainstorming 10,547 + Iconography 21,558 + Component Source 64,800).

---

## 3. Classification summary

| Group | Pages | Notes |
|---|---|---|
| Start / divider / header | 12 | 11 empty pages (`375:10885`, `375:10888`, `367:12000`, `1556:23522`, `1556:5`, `1556:74`, `375:10890`, `1556:77`, `1499:21976`, `1556:76`, `375:10898`) + Cover `375:10886` (thumbnail only). |
| A. Research | 6 | Brainstorming, Play Store Reviews, Survey Overview, Survey Insights, Product Analytics, User Personas. Research content only — **except Brainstorming, which holds 10,547 components** (icons). |
| B. Foundations | 7 | Colour, Typography, Iconography, Grid & Layout, Radius, Shadow, Blur. |
| C. Components | 7 | Button, Input, Input Dropdown, Checkbox/Radio/Toggle, Tooltip, Navigation · Mobile (empty), Navigation · Desktop (empty). |
| D. Patterns & Screens | 2 | Sample Screen, PDP. No component definitions; instances only. |
| E. Archive | 4 | Component Source, Checkbox, Radio, Toggle. |
| Unclassified | 1 | EMPTY PAGE `479:4` — sits after Archive, outside any section. |

12 + 6 + 7 + 7 + 2 + 4 + 1 = **39** ✓

---

## 4. Component sets discovered (current Components section)

[DERIVED] from layer names `Property=Value, …`. Full value lists in `raw/variant-matrices.md`. Whether each frame is a true Figma *component set* (variant group) vs. loose components in a frame will be confirmed in Phase 4.

| Component | Node ID | Page | Properties (value count) | Variants | Matrix |
|---|---|---|---|---:|---|
| All Buttons | `887:2492` | Button | Type (6) × State (6) × Size (12) | 432 | complete |
| Button | `1153:3370` | Button | Size (11) × State (5) | 55 | complete — purpose TBD (no Type prop) |
| Input Field / Outline | `1066:37962` | Input | State (6) × Size (5) × Radius (5) | 150 | complete — no Hover |
| Input Field / Filled | `1066:40663` | Input | State (7) × Size (5) × Radius (5) | 175 | complete |
| Dropdown / Menu | `1451:25521` | Input Dropdown | Selection (2) × Platform (2) × Theme (2) × Search (2) × Footer (3) | 48 | complete |
| Dropdown / Item | `1451:25092` | Input Dropdown | Selection (2) × Platform (2) × Theme (2) × State (5) | 40 | complete |
| .Selection Controls / Radio Button | `1504:52363` | Checkbox/Radio/Toggle | State (6) × Size (3) × Position (2) × Alignment (3) | 108 | complete |
| .Selection Controls / Checkbox | `1504:53300` | Checkbox/Radio/Toggle | State (7) × Size (3) × Position (2) × Alignment (3) | 126 | complete |
| .Selection Controls / Toggle | `1504:54471` | Checkbox/Radio/Toggle | State (10) × Size (3) × Position (2) × Alignment (3) | 180 | complete |
| Selection Controls | `1504:57173` | Checkbox/Radio/Toggle | Control Type (3) | 3 | complete — wrapper |
| tooltip | `1448:16825` | Tooltip | Device (2) × Mode (2) × Arrow (10) × Format (2) | 80 | complete |
| Navigation | — | Navigation pages | — | 0 | **[MISSING]** |

Key property values:
- **Button** Type: Primary, Secondary, Secondary Grey, Tertiary, Tertiary Grey, Link · State: Default, Hover, Focus, Pressed, Disabled, Loading · Size: 24, 26, 28, 32, 36, 38, 40, 42, 46, 48, 52, 56.
- **Input** State (Filled set): Default, Hover, Focused, Filled, Error, Disabled, Success · Size: 46, 48, 50, 54, 56 · Radius: 4, 6, 8, 10, 12.
- **Toggle** State: On/Off × {rest, Hover, Focus, Pressed, Disabled}.
- **Checkbox** State: Checked, Multi-select, Unchecked, Disabled, Disabled On, Focus, Pressed.
- **Radio** State: Selected, Unselected, Disabled Unselected, Disabled Selected, Focus, Pressed.

---

## 5. Inventory-level findings (feed into `08-inconsistencies.md`)

| # | Finding | Evidence | Tag |
|---|---|---|---|
| F1 | **Navigation (Mobile & Desktop) pages are empty.** No navigation spec exists. | `1351:18314`, `1556:7200` | [EXTRACTED] / [MISSING] |
| F2 | **"EMPTY PAGE" is not empty** — it holds a 432-variant button set with the same variant names as the current set but **different dimensions in 360 variants** (divergent copy; see `raw/archive-diff.md`). | `479:4` → `1590:19040` vs `887:2492` | [EXTRACTED] |
| F3 | **Six icon source candidates**: **in this file (4)** — S1 Iconography category catalogue and S2 Iconography pilots (together 21,558 comps, `375:10889`), S3 Archive › Component Source (64,800, `556:2`), S4 Research › Brainstorming (10,524 in `5:15097`); **external libraries (2)** — S5 "Annachy Icons File" (`lk-826bf23d…`, used by components) and S6 "UI Icons" (`lk-c918…`, no observed use). Canonical source must be decided (D-12). *[Corrected 2026-11-19 — originally "Icons are stored in three places" (Iconography, Component Source, Brainstorming); Iconography is now split into S1/S2 and the two external libraries found in Phase 5 are added — see `06` §1, `11` §3.]* | `375:10889`, `556:2`, `0:1` → `5:15097`; S5/S6 library keys | [EXTRACTED] |
| F4 | Checkbox, Radio and Toggle exist both in Components and in Archive. Archive versions use different property names (`Radio Position`, `Checkbox Position`, `Toggle Position` vs `Position`). | `375:10893` vs `1489:5449`, `1351:18310`, `1351:18313` | [EXTRACTED] |
| F5 | Dropdown / Item (40 variants) is duplicated on Archive › Checkbox page. | `1451:25092` vs `1464:2972` | [EXTRACTED] |
| F6 | Light/dark is modelled as a **variant property** with inconsistent casing: `Theme=Light/Dark` (Dropdown) vs `Mode=dark/light` (Tooltip). | `1451:25521`, `1448:16825` | [EXTRACTED] |
| F7 | Input uses radius values **6 and 10**, which are not in the documented radius scale (4, 8, 12, 14, 16, 18, 24, 26, 28, 32, 34). | `1066:37962`; Radius `1561:57646` | [EXTRACTED] |
| F8 | Radius usage conflicts: Button/Input mapped to Radius/8 in one table, Radius/12 = "Buttons" in another. | `1561:57590` vs `1561:57673` | [EXTRACTED] |
| F9 | Copy-paste header labels: Radius page header says "COLOUR SYSTEM"; Blur page header says "Shadow Scale". | `1561:57266`, `1563:58298` | [EXTRACTED] |
| F10 | Shadow Scale claims "18 variants"; 17 specimens are present. Blur claims "2 variants"; 8 specimens present; "Large" specimens labelled "XS". | `1561:57818`, `1563:58680`, `1563:58729` | [EXTRACTED] |
| F11 | Input column headings don't match the variant columns ("Active" vs Filled; Success/Disabled swapped). | `1567:2352`, `1567:2359` | [EXTRACTED] |
| F12 | Missing interaction states: Input / Outline has no Hover; Checkbox and Radio have no Hover; no Error state for Checkbox/Radio. | variant matrices | [DERIVED] |
| F13 | Naming typos: "Input Feild", "Typrography", "Clound Cross", "Essentional, UI", "CoreTooltip". | `1567:1642`, `5:10905`, `561:20856`, `478:86765`, `1568:38568` | [EXTRACTED] |
| F14 | Third-party trademarks in file (Amazon, Flipkart logos; "Iconly Pro" icons in Sample Screen). Licensing of Iconly Pro must be confirmed before any reuse. | `254:13503`, `254:13504`, `1651:893` | [EXTRACTED] |
| F15 | Sub-pixel inconsistency in Input widths (alternating 336/337 px). | `1066:37962` children | [EXTRACTED] |

---

## 6. Scope for remaining phases

| Phase | Will cover | Primary nodes |
|---|---|---|
| 3 (cont.) | Extract variable collections, modes and actual values for Colour, Typography, Grid, Radius, Shadow, Blur | `1557:23523`, `1557:25193`, `1557:31595`, `1557:39451`, `1557:44867`, `1558:51715`, `1561:57646`, `1561:57736`, `1561:57961`, `1563:58296` |
| 4 | Per-component specs (dimensions, spacing, colours, type, radius, effects, bindings) | Section 4 table |
| 5 | Asset inventory (icon canonical source, logos, images, fonts); SVG staging; inconsistency report | `375:10889`, `556:2`, `0:1`, logotype `1561:57274` |
| 6 | Reports 02–10 + roadmap | — |

Research (A) and Patterns (D) pages are inventoried only; they will be referenced for component usage evidence, not as specifications.

---

## 7. Figma operations log (read-only verification)

Every Figma MCP operation performed during Phase 3, with its safety basis. **No operation modified, created, moved, deleted, published, commented on, branched or uploaded anything in Figma.**

| Operation | Calls | Inputs | Safety basis | Result |
|---|---:|---|---|---|
| `get_metadata` (no nodeId) | 1 | fileKey | Tool definition: returns page list (guid + name); no write parameters | 39 pages listed |
| `get_metadata` (per page) | 39 | fileKey, nodeId | Tool definition: returns XML of IDs, types, names, positions, sizes; no write parameters | All 39 pages read, 0 errors |
| `get_libraries` | 1 | fileKey | Tool definition: lists subscribed/available libraries; does not add or remove any | 0 libraries added to file |

Operations reviewed and **not used**:

| Operation | Reason |
|---|---|
| `create_session` | Definition says it "records the user's current work"; cannot verify it performs no server-side write → skipped. Not required by read tools. |
| `download_assets` | Not needed in Phase 3. Schema shows download-only inputs (fileKey, nodeId, optional format/scale) returning temporary URLs; will be used only after explicit confirmation in Phase 5, without format/scale overrides, saving to `docs/figma-audit/raw/assets/`. |
| All write-capable tools (`use_figma`, `generate_figma_design`, `send_code_to_figma`, `upload_assets`, `create_branch`, `create_new_file`, Code Connect writes, generators, `weave_*`) | Prohibited — never called. |

Local-only outputs: all files written under `annachy-design-system/docs/figma-audit/`. No other project (including `emart-erp`) was accessed. No frontend implementation started.

### 7.1 Phase 3 (Foundations) operations

| Operation | Calls | Nodes | Safety basis |
|---|---:|---|---|
| `get_variable_defs` | 13 | `1557:23523`, `1557:25193`, `1557:31595`, `1557:39451`, `1557:44867`, `1558:51715`, `1561:56909`, `1561:56902`, `1561:57340`, `1561:57814`, `1561:58161`, `1563:58676`, `1106:12812` | Returns bound variable values only; no write inputs |
| `get_design_context` | 4 | `1558:48863`, `1558:48968`, `1558:49090`, `1561:57341` | Returns reference code/metadata for a node; no write inputs. Screenshot excluded. Required skill resource read first. |
| `search_design_system` | 1 | queries: variable ×2, style ×1 | Search only; does not add libraries |
| `ReadMcpResourceTool` | 1 | `skill://figma/figma-design-to-code/SKILL.md` | Reads server guidance text |

No asset downloads performed yet.

## 8. Phase 3 deliverables

| Report | Status |
|---|---|
| `02-color.md` | Complete — 130 + 16 variables; 10 findings |
| `03-typography.md` | Complete — 2 conflicting scales (28 + 11 styles); 12 findings (T12 added 2026-11-19) |
| `04-spacing-layout.md` | Complete — grid, radius; spacing & breakpoints MISSING |
| `05-elevation-effects.md` | Complete — 32 shadows, 5 blur, 3 glass; raw `raw/effects.json` |
| `06-iconography-assets.md` | Foundations complete; downloads pending decision |
