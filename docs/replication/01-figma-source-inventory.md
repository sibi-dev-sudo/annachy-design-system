# 01 — Figma Source Inventory (complete, classified)

| Item | Value |
|---|---|
| File | `rM3ixSG6i3DFfKZFWuxzs4` "Annachy CF — Design System" (immutable single source of truth) |
| Date | 2026-11-20 |
| Method | Read-only. Page structure from saved `get_metadata` (`docs/figma-audit/raw/metadata/`, 15 page dumps). Details in `docs/figma-audit/01-file-inventory.md` (39 pages, node counts) and `07-component-inventory.md` |
| Classes | **A** active design-system content · **B** patterns & sample screens · **C** archived / deprecated / duplicate · **D** empty or unfinished · **E** research / exploration (not design-system output) · **X** unresolved / inaccessible |

## 1. Every page

| # | Page | Node | Class | Content | Replication |
|---|---|---|---|---|---|
| 1 | ⓪ START | `375:10885` | D | Section divider (empty) | n/a |
| 2 | › ① Cover | `375:10886` | E | File thumbnail image | n/a (cover image, not design-system content) |
| 3 | ----- | `375:10888` | D | Divider | n/a |
| 4 | ① RESEARCH | `367:12000` | D | Divider | n/a |
| 5 | › ① Brainstorming | `0:1` | E | Typography exploration; icon-library comparison (~10,524 components: Lucide, Tabler, Huge, Phosphor, Solar); prompts; survey | Not replicated: exploration, not the system. Its icon sections are candidate sources (S4) only |
| 6–10 | › ②–⑥ Research boards (reviews, survey, insights, analytics, personas) | `373:12671`, `373:12818`, `373:12745`, `373:12852`, `254:13410` | E | Research findings, third-party brand logos (Amazon, Flipkart) | Not replicated (research, not UI) |
| 11 | --- | `1556:23522` | D | Divider | n/a |
| 12 | ② FOUNDATIONS | `1556:5` | D | Divider | n/a |
| 13 | › ① Colour | `273:10649` | **A** | Brand colours, supporting colours, usage, prompt | ✅ tokens + `showcase/foundations/colors.html` |
| 14 | › ② Typography | `220:10667` | **A** | Typography system, screen layout, documentation | ✅ 28 styles + `typography.html` |
| 15 | › ③ Iconography | `375:10889` | **A** (◐) | 41 category frames (S1), 52 pilot frames (S2), "Wind" pilot | ◐ model + slots in `iconography.html`; **artwork blocked** (doc 05) |
| 16 | › ④ Grid & Layout | `317:12589` | **A** | Grid system, layout frames | ✅ 13 grid reference values + `grid.html` |
| 17 | › ⑤ Radius | `365:11441` | **A** | 11 radius tokens | ✅ `dimensions.html` |
| 18 | › ⑥ Shadow | `1351:18308` | **A** | Shadow scale, effects | ✅ `effects.html` |
| 19 | › ⑦ Blur | `1351:18312` | **A** | Blur & glass | ✅ `effects.html` |
| 20–21 | dividers | `1556:74`, `375:10890` | D | — | n/a |
| 22 | › ① Button | `375:10891` | **A** | Button 432 + Gradient 55 | ✅ |
| 23 | › ② Input | `375:10892` | **A** | Outline 150 + Filled 175 | ✅ |
| 23a | › ② Icons ✓ *(added by the owner 2026-11-20)* | `1801:5142` | **A** | 5,128 icon component sets (35,890 variants), Outline/Filled × XS–XL, Iconly-derived | Identity map ✅ (`src/icons/figma-icon-map.json`); **artwork pending export authorisation** |
| 24 | › ③ Input Dropdown | `1351:18309` | **A** | Menu 48 + Item 40 | ✅ (R4 + R6) |
| 25 | › ④ Checkbox / Radio / Toggle | `375:10893` | **A** | 126 + 108 + 180 + wrapper 3 | ✅ |
| 26 | › ⑤ Tooltip | `1351:18311` | **A** | 80 | ✅ |
| 27 | › ⑥ Navigation · Mobile | `1351:18314` | **D** | **Empty page** (0 nodes) | n/a: nothing to reproduce |
| 28 | › ⑦ Navigation · Desktop | `1556:7200` | **D** | **Empty page** (0 nodes) | n/a |
| 29–30 | dividers | `1556:77`, `1499:21976` | D | — | n/a |
| 31 | › ① Sample Screen | `1375:30857` | **B** | Desktop 1440 × 3533 / 1073, Mobile 360 × 4683 / 800, "Job - Listing page" | `showcase/screens/sample-screen/` (doc 03) |
| 32 | › ② PDP | `581:11523` | **B** | Desktop 1440 × 1024, Mobile 360 × 1536, PDP V1 × 3 (393 wide) | `showcase/screens/pdp/` (doc 03) |
| 33–34 | dividers | `1556:76`, `375:10898` | D | — | n/a |
| 35 | › ① Component Source | `556:2` | **C** | 240 icon frames × 270 components (source of the pilot icon model, S3) | Not replicated as UI; candidate icon source (S3) |
| 36 | › ② Checkbox (archive) | `1351:18310` | **C** | Duplicate Checkbox set, legacy "check box", duplicate Dropdown/Item, mock-ups | Superseded by the active sets (`docs/figma-audit/raw/archive-diff.md`) |
| 37 | › ③ Radio (archive) | `1489:5449` | **C** | Radio set + docs (duplicate of active) | Superseded |
| 38 | › ④ Toggle (archive) | `1351:18313` | **C** | Toggle set + docs (duplicate of active) | Superseded |
| 39 | EMPTY PAGE | `479:4` | **C** | Not empty: a duplicate "Core Button Components" frame | Superseded duplicate of the Button set |
| — | External "Annachy Icons File" (S5) | library `lk-826bf23d…` | **X** | Icons used by Button, Input/Outline, Dropdown (built from Iconly artwork, `r6-0-evidence.md` §4) | **Inaccessible** (file key not exposed, D-13); icon matching needs Iconly access |
| — | External "Design System" / "UI Icons" libraries | `lk-483b…`, `lk-c918…` | **X** | `Select`, `Pagination`, shadows; kebab-case icons | Not linked to the file; ownership unknown (D-14) |

## 2. Totals

| Class | Pages | Notes |
|---|---:|---|
| A active | 12 | 7 foundations + 5 component pages (11 sets, 1,397 variants) |
| B patterns & screens | 2 | 10 top-level frames |
| C archived / duplicate | 5 | Every component duplicate maps to an active set |
| D empty / dividers | 13 | Includes the two empty Navigation pages |
| E research / exploration | 7 | Cover + Brainstorming + 5 research boards |
| X inaccessible (external) | 3 libraries | S5 icons, "Design System", "UI Icons" |
| **Total** | **39** | |

**Update 2026-11-20:** the file now has **40 pages**. The new page is `1801:5142` "② Icons" (class A), so class A = 13.
