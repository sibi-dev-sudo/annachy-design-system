# 02 — Figma → Web Traceability Matrix, Foundations and Component Coverage

Status values: **Complete** · **Partial** (reason given) · **Missing** · **Blocked** (external) · **Archived** · **N/A** (reason given).
Validation counts come from the final sequential regression (`06-final-regression-report.md`).

## 1. Foundations (`src/tokens/`, 464 tokens + a partial Dark re-map)

| Figma | Variables / styles | Local implementation | Showcase | Validation | Status |
|---|---|---|---|---|---|
| Colour `273:10649` | 82 primitives · 27 semantic (Light) · 50 Button · 5 icon-state · 5 compat | `primitives.css`, `themes/light.css`, `component-tokens.css`, `compat.css` | `colors.html` | R1 static 464/0 · R1 browser 464/0 | Complete |
| Colour, **Dark mode** of `Brand/*` | 7 values observed (`r6-0-evidence.md` §1) | `themes/dark.css` (`[data-annachy-theme="dark"]`) | Dropdown Dark | R6 visual 757/0 | **Partial**: only the variables the Dark variants bind are known. Other components have no Dark variants in Figma |
| Typography `220:10667` | 7 primitives · 28 styles × 7 properties | `typography.css`, `base/typography.css` | `typography.html` | R1, R2 | Complete (font: system fallback until the Proxima Nova licence, D-06) |
| Iconography `375:10889` | Style 6 × Size 9 × state 5 (pilot); S5 Outline/Filled × XS–XL | slot contract, `src/icons/manifest*.json` | `iconography.html` | R5 static 53/0 · slots 73/0 | **Complete for page `1801:5142`**: 5,128 sets / 35,890 variants in `showcase/icons/`; 6,890 assets; 8 component slots render their icons. Solar icons on `375:10889` used by the screens: **not required** (Design Team, 2026-11-20), Dropdown indicators / Checkbox glyph / Tooltip arrow (E-2, E-3) |
| Grid & Layout `317:12589` | 13 reference values | `primitives.css` (`--annachy-grid-*`) | `grid.html` | R1 | Complete (Figma defines no breakpoints) |
| Radius `365:11441` | 11 | `primitives.css` | `dimensions.html` | R1 | Complete |
| Heights / border widths | 12 / 3 | `primitives.css` | `dimensions.html` | R1 | Complete |
| Shadow `1351:18308` | 33 documented + 7 component effect styles | `effects.css` | `effects.html` | R1 | Complete |
| Blur `1351:18312` | 12 blur / glass + 1 gradient | `effects.css` | `effects.html` | R1 | Complete |
| Base | document, reset, text classes, utilities | `src/base/` | `base.html` | R2 | Complete |

## 2. Components (1,397 of 1,397 Figma variants implemented)

| Figma set | Variant properties | Variants | Local implementation | Icons / assets | Validation | Status |
|---|---|---:|---|---|---|---|
| Button `887:2492` | Type 6 × State 6 × Size 12 | 432 | `src/components/button/` | 20 px icon slots (empty) | 9,964 visual · real input | Complete (icons rendered from `1801:5142`, R7) |
| Button Gradient `1153:3370` | Size 11 × State 5 | 55 | `button-gradient/` | 20 px slots | 1,863 | Complete (icons rendered from `1801:5142`, R7) |
| Input / Outline `1066:37962` | State 6 × Size 5 × Radius 5 | 150 | `input/` | 24 / 16 slots | 11,952 (with Filled) | Complete (icons rendered from `1801:5142`, R7) |
| Input / Filled `1066:40663` | State 7 × Size 5 × Radius 5 | 175 | `input/` | 24 / 14 slots | (above) | Complete; Filled icon slots unmapped (E-1: Figma variant changed, Cloud is a Solar pilot icon) |
| Checkbox `1504:53300` | State 7 × Size 3 × Position × Alignment | 126 | `checkbox/` (+ `checkbox.js`) | glyph slot | 3,108 | Complete; glyph geometry D-27 |
| Radio `1504:52363` | State 6 × Size 3 × Position × Alignment | 108 | `radio/` | — | 2,423 | Complete; ring geometry D-27 |
| Toggle `1504:54471` | State 10 × Size 3 × Position × Alignment | 180 | `toggle/` | — | 4,904 | Complete; strokes D-27 / TG-1 |
| Selection Controls `1504:57173` | Control Type | 3 | alias of the Small variants (`selection-controls/README.md`) | — | R3 closure | Complete |
| Dropdown / Item `1451:25092` | Selection × Platform × Theme × State 5 | 40 | `dropdown/` | 20 px indicator (empty) | R4 469 (Light) · **R6 757 (Dark + Footer)** | **Complete** (Light R4, Dark R6) |
| Dropdown / Menu `1451:25521` | Selection × Platform × Theme × Search × Footer 3 | 48 | `dropdown/` (+ `dropdown.js`) | 24 search slot, 20 footer icon slot | R4 469 + 82 real input · R6 757 + **38 footer real input** · lifecycle 40 | **Complete** (Footer R6, staged commit) |
| Tooltip `1448:16825` | Device × Mode × Arrow 10 × Format | 80 | `tooltip/` (+ `tooltip.js`) | 20 px arrow slot | 1,441 · 39 real input | Complete (arrow polygon G12) |
| Navigation (Mobile / Desktop) | — | 0 | — | — | — | **N/A**: both Figma pages are empty |
| Select trigger | — | 0 | — | — | — | **N/A**: no component in this file (external "Design System" library, D-14) |
| **Total** | | **1,397** | | | | |

## 3. Patterns & screens

| Figma frame | Size | Local | Validation | Status |
|---|---|---|---|---|
| Sample Screen `1375:30858` Desktop PDP | 1440 × 3533 | `showcase/screens/sample-screen/` | 1,441 checks (5 frames) | Complete; R11 product images filled (internal use, rights unverified: R11-U1) |
| Sample Screen `1608:9891` Desktop | 1440 × 1073 | (same) | (same) | Partial: no readable children |
| Sample Screen `1608:7090` Mobile PDP · `1627:11756` Mobile · `1629:11987` Job listing | 360 wide | (same) | (same) | Complete |
| PDP `605:17532` Desktop · `1171:9676` Mobile · `1280:10398` PDP V1 | 1440 / 360 / 393 | `showcase/screens/pdp/` | 303 checks (3 frames) | Complete |
| PDP `1214:11887`, `1218:13662` (earlier V1 iterations) | 393 × 4388 | — | — | Superseded (differences documented) |

## 4. Archived / duplicate content

| Figma | Maps to | Status |
|---|---|---|
| Archive › Checkbox `1351:18310` (126 + legacy 8 + Dropdown/Item 40) | Active Checkbox `1504:53300`, Dropdown/Item `1451:25092` | Archived (`raw/archive-diff.md`) |
| Archive › Radio `1489:5449`, Toggle `1351:18313` | Active Radio, Toggle | Archived |
| "EMPTY PAGE" `479:4` (Core Button Components) | Button `887:2492` | Archived duplicate |
| Archive › Component Source `556:2` (64,800 icon components) | Icon source candidate S3 | Not UI; icon blocker |


## 5. Scope decisions (2026-11-20, Design Team)

| Item | Elements | Status |
|---|---:|---|
| Solar screen icons (page `375:10889`; 11 icons, including the 2 "Play Circle") | 68 placeholders + Gallery Minimalistic = 69 | **Not required: out of scope** |
| "Icons" slot artworks in the Lab Cards (`5:26` and the card-internal groups) | 24 | **Not required: out of scope** |

Evidence is kept in `docs/figma-audit/r9-0-icon-export-manifest.*`. The elements remain placeholders on purpose and are excluded from completion counts.


**R11 update 2026-11-20.** All 108 product-imagery placeholders (PDP `pdp-v1`, `mobile`, `desktop-bg-colours`; Sample Screen Desktop PDP,
Mobile PDP, Mobile putaway) hold the original Figma images: `showcase/screens/assets/images/`, mapping per placeholder in
`docs/figma-audit/r11-0-product-imagery-manifest.json` (`elements[].implemented`). Fixtures: Sample 1,441 / 0, PDP 306 / 0.

**Closure update 2026-11-20.** The screens now hold all in-scope artwork except the 5 third-party logos:
- **Census:** 248 / 363 placeholders filled (`closure-placeholder-census.json`). That is 241 / 246 in scope; the rest are 96 not required, 14 not applicable (phone system UI) and 5 rights-blocked.
- **Icons and logotype:** `docs/figma-audit/closure-icons-logo-manifest.md`.
- **Images:** served as A/B-verified WebP copies (`showcase/screens/assets/images-web/`); the originals are unchanged.
- **New suite:** the closure accessibility suite (147 / 0).

Final status: `FINAL-PROJECT-COMPLETION-REPORT.md`.
