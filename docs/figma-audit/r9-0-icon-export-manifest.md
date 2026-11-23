# R9-0 — Missing Screen Icons: Export Manifest — **CANCELLED (not required)**

> **Decision 2026-11-20 (Design Team):** all three categories are **not required** for the project.
> - A: 11 Solar icons / 69 elements
> - B: 10 Brainstorming artworks / 24 elements
> - C: Gallery Minimalistic
>
> No export or download was made, and none will be. No replacement or alternative artwork will be created. This report and `r9-0-icon-export-manifest.json` are **kept as audit evidence only**. The affected screen elements stay as documented placeholders and are counted as **out of scope**, not incomplete.

| Item | Value |
|---|---|
| Date | 2026-11-20 |
| Data | `r9-0-icon-export-manifest.json`: every source node, destination path and affected element, with its export route |
| Inspection | Read-only. `get_design_context` ×21 (screenshots excluded; asset URLs **not** fetched) and `get_metadata` ×5. Plus the recorded R8-0 evidence |
| Destinations | All destination paths are new; none collides with an existing file. The 35,890 icon variants, the existing SVGs and the 464 tokens are untouched |

## A. Solar icons: 11 icons → 69 screen elements

| ID | Solar icon (style) | Elements | Exact / scaled | Screen sizes (px) | Library destination (normalised) |
|---|---|---:|---|---|---|
| A01 | Play Circle (Outline) | 2 | 0 / 2 | 18 | `src/icons/svg/outline/solar-play-circle.svg` |
| A02 | Users Group Two Rounded (Outline) | 2 | 1 / 1 | 23.1, 24 | `src/icons/svg/outline/solar-users-group-two-rounded.svg` |
| A03 | Shop (Linear) | 2 | 2 / 0 | 24 | `src/icons/svg/linear/solar-shop.svg` |
| A04 | Cart Large 2 (Outline) | 3 | 0 / 3 | 28 | `src/icons/svg/outline/solar-cart-large-2.svg` |
| A05 | Shield Check (Linear) | 2 | 1 / 1 | 23.1, 24 | `src/icons/svg/linear/solar-shield-check.svg` |
| A06 | Magnifer (Linear) | 3 | 3 / 0 | 24 | `src/icons/svg/linear/solar-magnifer.svg` |
| A07 | Map Point (Outline) | 1 | 1 / 0 | 24 | `src/icons/svg/outline/solar-map-point.svg` |
| A08 | Like (Outline) | 2 | 0 / 2 | 18 | `src/icons/svg/outline/solar-like.svg` |
| A09 | Heart (Linear) | 25 | 8 / 17 | 19.2, 24, 28 | `src/icons/svg/linear/solar-heart.svg` |
| A10 | Arrow Right (Linear) | 2 | 2 / 0 | 24 | `src/icons/svg/linear/solar-arrow-right.svg` |
| A11 | Alt Arrow Left (Line Duotone, multi-tone) | 25 | 12 / 13 | 16, 18, 20, 24, 28 | `src/icons/svg/line-duotone/solar-alt-arrow-left.svg` |

**Originals.** Byte-preserved originals go to `src/icons/originals/solar/<style>/<name>.svg`. The naming follows the existing `<style>/<slug>.svg` convention, with a `solar-` prefix so nothing collides with the Icons-page names.

**Finding.** The Solar catalogue node IDs in the saved snapshot of page `375:10889` (variants `478:70344`…, sets `478:70334`…, category frame `478:68250`) return **"not found"** in the live file today.

**Proposed source instead.** The screen elements themselves. They are detached Solar copies whose Figma layer names state style, category and name; for example `1280:10652` is "Outline / Video, Audio, Sound / Play Circle". This also captures each element's **exact screen colour and size**.

Export routes, per element (in the JSON):

| Route | Elements |
|---|---:|
| `download_assets` (svg) on the plain screen node | 38 |
| Asset URL from `get_design_context` for a child layer | 10 |
| Asset URL from `get_design_context` on a nested instance ID (`download_assets` accepts plain IDs only) | 21 |

The library file per icon comes from an exact 24 px element where one exists (A03, A06, A07, A10 and the exact halves of the others). Otherwise it is normalised from a scaled element, recording its scale.

## B. "Icons" slot: 24 elements = 6 distinct icons, 10 distinct artworks (not one component)

| ID | Inner group | Source node | Artwork ID | Elements (screen) | Export via |
|---|---|---|---|---|---|
| B01 | Group 1171275310 | **`5:26` → `5:27`** (the Brainstorming master) | 2a822 | 4 (PDP V1 2, Mobile PDP 2) | `I1280:10517;1548:31174` |
| B02 | Group 1171275308 | `1548:31118` | ab583 | 4 (2 + 2) | `I1280:10518;1548:31174` |
| B03 | Group 1171275309 | `1548:31123` | f36c2 | 2 (PDP V1) | `I1280:10520;1548:31174` |
| B07 | Group 1171275309 | `1548:31123` | 562f9 | 2 (Mobile PDP) | `I1608:7251;1548:31174` |
| B04 | Group 1171275312 | `1548:31127` | c9d0a | 3 (2 + 1) | `I1280:10521;1548:31174` |
| B08 | Group 1171275312 | `1548:31127` | c2b02 | 1 (Mobile PDP) | `I1608:7252;1548:31174` |
| B05 | Group 1171275311 | `1548:31132` | b43ba | 2 (PDP V1) | `I1280:10523;1548:31174` |
| B09 | Group 1171275311 | `1548:31132` | 91ca8 | 2 (Mobile PDP) | `I1608:7254;1548:31174` |
| B06 | Group 1171275313 | `1548:31160` | a10ea | 2 (PDP V1) | `I1280:10524;1548:31174` |
| B10 | Group 1171275313 | `1548:31160` | e0056 | 2 (Mobile PDP) | `I1608:7255;1548:31174` |

- **Geometry.** Every slot is 24 × 24 with clipping. The vector group is inset per icon; for example B01 is inset 16.66 / 21.05 / 17 / 20.83 %.
- **Destination.** Screen-only artwork: `showcase/screens/assets/icons/brainstorm-group-<group>-<artwork>.svg`. These are not library icons: no style property, no names, and not on the Icons page.
- **Style.** None defined in Figma (the "Property 1 = 1" variant only).
- **Correction.** Only **4 of the 24** elements use `5:26`. The other 20 show icon groups defined inside the parent card component (`1548:…`). The same group carries different artwork per screen (likely colour or state overrides), so each distinct artwork is exported once.

## Unresolved (kept as placeholders)

- `1280:10643` "Gallery Minimalistic", 18 px: the Solar style of this detached copy isn't recorded. Exporting the screen layer itself (`download_assets` on `1280:10643`) would reproduce it exactly **without** naming a style. Its library mapping stays unresolved.

## Execution plan (after approval)

1. **Export** 69 Solar screen elements and 10 "Icons" artworks (79 exports, plus 1 optional for Gallery Minimalistic) to `%TEMP%/annachy-icon-staging/` (outside the repository). No asset URL is written into any file.
2. **Preserve** byte-identical originals and record SHA-256 in `manifest.json`, with source `solar` (*licence to confirm*) and source `figma-screen` for B.
3. **Normalise** 11 Solar library files (`currentColor`; duotone opacity kept for A11), then validate them with `icons_lib` V01–V11.
4. **Fill the screens.** Each placeholder renders its **own exported artwork**, so screen colour and scale are exact. The `data-figma-node` attribute is kept.
5. **Test.**
   - Screen fixtures: placeholders now filled, sized to their Figma boxes.
   - A fidelity check of each normalised Solar file against its exact 24 px export.
   - `r7_icons_static` extended.
   - The full sequential regression and the mutation tests.

Estimate: about 1.5 h.


---

## Investigation (2026-11-20, read-only): findings and approval matrix

**Evidence calls.**
- Figma: `get_metadata` ×76 and `get_design_context` ×17 (screenshots excluded; no asset URL fetched).
- Web: the Iconify page and the Iconify API.

**Nothing was exported, downloaded or modified.** Per-element evidence is in the JSON (`verification`, `exportRoute.resolvedIconLayer`, `hiddenInFigma`).

### 1. Solar licence

| Source | Result |
|---|---|
| Iconify API `api.iconify.design/collection?prefix=solar&info=true` (fetched) | author `480 Design` (url = Figma Community file 1166831539721848736); license title `CC BY 4.0`, spdx `CC-BY-4.0`, url `https://creativecommons.org/licenses/by/4.0/` |
| Iconify page `icon-sets.iconify.design/solar/` (fetched) | "CC BY 4.0 (Attribution required, commercial use is allowed)" |
| Author's Figma Community file 1166831539721848736 | **HTTP 403: not readable** |
| Author site (480design.figma.site / 480design.com) | 404 / DNS failure |
| Creative Commons BY 4.0 licence text | TLS error: **not read** (no clause is quoted from memory) |
| The Annachy file's Solar layers | **No licence, author or copyright text** in any layer name or description |

**Verdict: UNVERIFIED.**
- CC BY 4.0 is stated only by a third-party aggregator (Iconify). The author's own statement and the licence text could not be read.
- These Annachy layers are linked to the 480 Design set **by naming only** ("Style / Category / Icon", the same Solar style names). The file records no provenance.
- *If* CC BY 4.0 applies, internal commercial use and adaptation are allowed with attribution. That must be confirmed from the primary source.

### 2. Solar screen layers (the export source)

- **67 / 69 CONFIRMED.** Each layer name states the expected style, category and icon (the arrow category is "Arrows"). There are 0 mismatches.
- **4 Heart elements are hidden in Figma.** Their parent "Watchlist / Small Button" is hidden.
  - 2 nested IDs do not resolve: `I1608:7528;1548:40637;1548:40450` and `I1608:7529;1548:40637;1548:40450`.
  - 2 are hidden: `1280:10701` and `1280:10702`.
  - Figma does not display them, so they are **excluded** (no export, no display). **65 elements remain.**
- **Detached copies.** 68 / 69 are detached frames, several inside this file's own components (Button, Watchlist / Small Button, Product Details Sections). A07 Map Point `1375:31037` is an instance of a local component. No Solar library is linked.
- **Child-layer routes (10).** None has a child with the planned name; each resolves to a nested icon layer with the expected Solar name (recorded in `resolvedIconLayer`).
- **Rotated arrows.** `1280:10543` and `1280:10617` are drawn rotated 90° and flipped, so they display as a chevron. Exporting the screen layer keeps that transform.
- **Artwork.** Each element is one SVG asset, with no colour classes in the code. The exported SVG carries the actual colour and transform, so exporting the screen layer preserves artwork, colour and size exactly. The 12 elements whose placeholder size differed from the Figma layer now record `figmaSizePx`.
- **Routes for the 65.** 38 via `download_assets` (plain IDs) and 27 via `get_design_context` asset URLs (nested or instance IDs; `download_assets` accepts plain IDs only). **Both are exports**: they need the same approval and no additional access.

### 3. Brainstorming artworks (10 → 24 elements)

- **All 24 verified individually.** Every slot is the "Icons" instance at x 8, y 5, 24 × 24, inside a **"Lab Card"** instance: PDP V1 `1280:10517…10534` (12) and Mobile PDP `1608:7248…7265` (12).
- **Sources.** Master `5:26` → `5:27` (4 elements) and card-internal groups `1548:31118`, `1548:31123`, `1548:31127`, `1548:31132`, `1548:31160`.
- **Per-screen artwork IDs:**
  - 309: f36c2 / 562f9
  - 311: b43ba / 91ca8
  - 313: a10ea / e0056
  - 312: c9d0a ×3 / c2b02 ×1
- **No names or styles exist in Figma** ("Group 117127530x", "Property 1 = 1"), and none were invented.
- **Ownership: UNVERIFIED.** `5:26` sits on the Brainstorming page, where the team compared third-party icon libraries (Lucide, Tabler, Huge Icons, Phosphor, Solar). The origin of these six glyphs is not recorded: they may be the team's own drawings or copies of third-party icons.

### 4. Gallery Minimalistic `1280:10643`

- **What it is.** An 18 × 18 frame named "Gallery Minimalistic". Unlike the other Solar layers it has no style prefix. It is exposed as **one SVG asset**.
- **Export.** It can be exported as a **screen-only asset** (`download_assets` on the plain ID) **without assigning a style**, to `showcase/screens/assets/icons/gallery-minimalistic-1280-10643.svg`. No library entry would be created.
- **Licence.** The same open question as A (it uses a Solar icon name).

### 5. Export and file safety

| Check | Result |
|---|---|
| 33 destination paths | **None exists**, so nothing can be overwritten. New folders: `src/icons/originals/solar/{linear,outline,line-duotone}`, `src/icons/svg/{linear,line-duotone}`, `showcase/screens/assets/icons` |
| Existing assets | The 35,890 variants, existing SVGs and the 464 tokens are untouched (the plan adds files only) |
| Staging | `%TEMP%\annachy-icon-staging\`: outside the repository and absent now. Removed after integration; asset URLs are never written into any file |
| Methods | `download_assets` (plain IDs): 38 Solar + 1 Gallery. `get_design_context` asset URLs: 27 Solar + 10 Brainstorming. Both leave Figma unchanged (no write tool, no `create_session`) |
| Batch size | **76 exports** (65 + 10 + 1). The earlier figure of 80 included the 4 hidden Hearts |

### 6. Final approval matrix

| Category | Source verified? | Licence verified? | Export technically possible? | Internal-use permission established? | Destination safe? | Remaining concerns | **Status** |
|---|---|---|---|---|---|---|---|
| **A** Solar: 11 icons / 65 elements (4 hidden excluded) | **Yes**: 67/69 layer names confirm style, category and icon; the 4 hidden are excluded | **No**: CC BY 4.0 per Iconify only; primary source and licence text unreadable | **Yes**: 38 `download_assets` + 27 asset URL | **No**: depends on the licence and its attribution | **Yes** | Licence confirmation; attribution wording; provenance by name only | **UNVERIFIED** |
| **B** Brainstorming: 10 artworks / 24 elements | **Yes**: node IDs, Lab Card parents, per-screen artwork | **No**: origin unknown (possibly third-party copies) | **Yes**: 10 asset URLs | **No**: ownership not recorded | **Yes** | Design team must confirm the 6 glyphs are Annachy-owned or cleared | **UNVERIFIED** |
| **C** Gallery Minimalistic: 1 element | **Yes**: node, size, single SVG | **No**: same as A | **Yes**: `download_assets` | **No**: same as A | **Yes** | Style not recorded (exported without one) | **UNVERIFIED** |

**Conclusion.** All 76 exports are technically ready and file-safe, but **none is licence-verified**. Approving the batch now would rest on two confirmations:
- the design team or legal accepting Solar = CC BY 4.0 (480 Design), with attribution;
- the design team confirming ownership or clearance of the 6 Brainstorming glyphs.
