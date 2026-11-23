# R10-0 — Structural Screen Vectors: Export Manifest (PLAN ONLY — nothing exported)

| Item | Value |
|---|---|
| Date | 2026-11-20 |
| Scope | **50 elements:** 33 divider / stroke lines, 12 rating stars, 4 simple shapes, 1 small vector frame. These are Annachy's own design layers on the Sample Screen and PDP pages |
| Data | `r10-0-structural-vector-manifest.json`: per element, page / screen / parent / path, size, position, colour evidence, stroke hint, rotation, opacity, visibility, artwork ID, destination |
| Inspection | Read-only, 138 calls: `get_metadata` ×51, `get_design_context` ×51 (screenshots excluded; asset URLs **not** fetched, only short artwork IDs recorded), `get_variable_defs` ×36. One independent spot-check (`1375:31154` → artwork `4ff1b`, as recorded) |

## 1. Source summary

| Check | Result |
|---|---|
| Found | **50 / 50** (0 unreadable) |
| Visible in Figma | **50 / 50** (no hidden node or ancestor) |
| Pages | `1375:30857` "› ① Sample Screen" (**46** elements), `581:11523` "› ② PDP" (**4** elements) |
| Screens (elements) | mobile-pdp-1608-7090.html 21, desktop-pdp-1375-30858.html 14, job-listing-page-1629-11987.html 6, mobile-putaway-1627-11756.html 5, pdp-v1.html 3, mobile.html 1 |
| Rotation / flip / scale | **None** in any node's code. The two diagonal lines (`42e60`, 57 × 54, about 43.45°) carry the angle inside their SVG geometry |
| Opacity | None set on any node |
| Artwork | Each element renders as **exactly one SVG asset**. **28 distinct artworks**; 8 are shared by several elements (e.g. `4ff1b` ×6, `c6cc8` stars ×7) |

## 2. Artwork → element mapping (28 files)

| Artwork | Group | Asset ID | Figma size (px) | Uses | Elements | Export node | Method | Destination (`showcase/screens/assets/vectors/`) |
|---|---|---|---|---:|---|---|---|---|
| R01 | line | `c4a54` | 610 × 0 | 2 | V01, V04 | `1375:30923` | download_assets | `line-c4a54-610x0.svg` |
| R02 | line | `600fb` | 0 × 27 | 1 | V02 | `1375:30933` | download_assets | `line-600fb-0x27.svg` |
| R03 | line | `65fb2` | 0 × 17 | 1 | V03 | `1375:30937` | download_assets | `line-65fb2-0x17.svg` |
| R04 | line | `3adb7` | 610 × 0 | 1 | V05 | `1375:31002` | download_assets | `line-3adb7-610x0.svg` |
| R05 | line | `63f38` | 610 × 0 | 1 | V06 | `1375:31076` | download_assets | `line-63f38-610x0.svg` |
| R06 | line | `4ff1b` | 270 × 0 | 6 | V07, V08, V09, V10, V11, V12 | `1375:31127` | download_assets | `line-4ff1b-270x0.svg` |
| R07 | line | `8879d` | 1200 × 0 | 1 | V13 | `1375:31393` | download_assets | `line-8879d-1200x0.svg` |
| R08 | line | `4c2ad` | 328 × 0 | 3 | V14, V31, V32 | `1629:12011` | download_assets | `line-4c2ad-328x0.svg` |
| R09 | line | `31c80` | 306 × 0 | 1 | V15 | `1629:12566` | download_assets | `line-31c80-306x0.svg` |
| R10 | line | `06fc3` | 304 × 0 | 4 | V16, V17, V18, V33 | `1629:12126` | download_assets | `line-06fc3-304x0.svg` |
| R11 | line | `2e905` | 30 × 0 | 4 | V19, V20, V21, V22 | `I1608:7152;1539:30179;1539:28950` | asset URL | `line-2e905-30x0.svg` |
| R12 | line | `42e60` | 57 × 54 | 2 | V23, V36 | `I1608:7153;1546:27123;1546:27436;1010:22241` | asset URL | `line-42e60-57x54.svg` |
| R13 | line | `64c45` | 54 × 0 | 1 | V24 | `1608:7182` | download_assets | `line-64c45-54x0.svg` |
| R14 | line | `6aff8` | 328 × 0 | 1 | V25 | `1608:7272` | download_assets | `line-6aff8-328x0.svg` |
| R15 | line | `abbb0` | 362 × 0 | 1 | V26 | `I1608:7274;1548:33550` | asset URL | `line-abbb0-362x0.svg` |
| R16 | line | `22d2c` | 328 × 0 | 1 | V27 | `I1608:7348;1548:33550` | asset URL | `line-22d2c-328x0.svg` |
| R17 | line | `1f27c` | 0 × 18 | 1 | V28 | `1608:7363` | download_assets | `line-1f27c-0x18.svg` |
| R18 | line | `f1aa6` | 328 × 0 | 1 | V29 | `1608:7389` | download_assets | `line-f1aa6-328x0.svg` |
| R19 | line | `9d56e` | 362 × 0 | 1 | V30 | `1608:7390` | download_assets | `line-9d56e-362x0.svg` |
| R20 | star | `2834b` | 16 × 16 | 1 | V34 | `1201:9800` | download_assets | `star-2834b-16x16.svg` |
| R21 | star | `0c3c4` | 16 × 16 | 1 | V35 | `I1280:10408;1528:26138;1523:25927` | asset URL | `star-0c3c4-16x16.svg` |
| R22 | star | `2efa9` | 18 × 18 | 2 | V37, V40 | `1280:10629` | download_assets | `star-2efa9-18x18.svg` |
| R23 | vector-frame | `ab45f` | 47.65 × 47.65 | 1 | V38 | `1375:30871` | download_assets | `vector-frame-ab45f-47_65x47_65.svg` |
| R24 | shape | `bcf26` | 12 × 12 | 1 | V39 | `1629:12007` | download_assets | `shape-bcf26-12x12.svg` |
| R25 | star | `c2e28` | 17.81 × 17.81 | 1 | V41 | `I1608:7387;1321:18884` | asset URL | `star-c2e28-17_81x17_81.svg` |
| R26 | star | `c6cc8` | 9.54 × 9.54 | 7 | V42, V43, V44, V45, V46, V47, V48 | `1608:7439` | download_assets | `star-c6cc8-9_54x9_54.svg` |
| R27 | shape | `58769` | 15 × 1.25 | 1 | V49 | `1627:11933` | download_assets | `shape-58769-15x1_25.svg` |
| R28 | shape | `a6156` | 15 × 15 | 1 | V50 | `1627:11938` | download_assets | `shape-a6156-15x15.svg` |

Every element's exact screen placeholder (`screenFile` + `placeholderNode`) is in the JSON. Each placeholder would render its artwork file at its own Figma box. Shared artwork is reused, never redrawn.

## 3. Unresolved / not observable (not invented)

| Item | Detail |
|---|---|
| **Colours (48 / 50)** | Not exposed read-only. The vectors are delivered only as SVG assets; no colour classes and no bound variables. They become known only from the exported SVG, which preserves them exactly |
| Colour variables on V01, V04 | `get_variable_defs` returns `Brand/Blue-Grey/400 #98a0ae` and `Brand/Blue-Grey/300 #bfc4cf`; which one (if either) is the stroke is not confirmed. The export settles it |
| Stroke widths | Not exposed. Wrapper insets suggest **1 px** for most lines and **1.5 px** for the diagonals. These are inferences, marked as such; the exact width is inside each SVG |
| Parent frame unknown (14 elements) | V01, V02, V03, V04, V05, V06, V07, V08, V09, V10, V11, V12, V13, V38: nodes inside Desktop `1375:30858`, whose children Figma does not return. Page and screen are known; the immediate parent is not |
| V38 "View More" | A frame **flattened into one SVG** with negative insets (artwork extends beyond the frame, probably a baked-in effect). Exported as-is |
| Layer names | V26 and V27 are named "Line 137" in Figma (the placeholder titles said "Line"). Recorded as in Figma |
| Near-zero sizes | Several lines have Figma heights or widths of ~1e-6 px (true hairlines whose thickness is the stroke). The exact values are kept in the JSON |

## 4. File safety

| Check | Result |
|---|---|
| Destinations | 28 new files under `showcase/screens/assets/vectors/`. **That folder does not exist yet**, and none of the 28 paths exists, so **nothing can be overwritten** |
| Library untouched | Nothing goes into `src/`. The 464 tokens, the 35,890 icon variants and the existing SVGs are not involved |
| Staging | `%TEMP%nnachy-vector-staging\`: outside the repository and absent now. Created at export, deleted after integration. No asset URL is ever written into a file |
| Export methods | **22 × `download_assets` (svg)** on plain node IDs. **6 × asset URL from `get_design_context`**, needed for nested instance IDs, which `download_assets` does not accept. Both are read-only on Figma and need the same approval |
| Figma | Unchanged (no write tool, no `create_session`) |

## 5. Risks

| Risk | Level | Mitigation |
|---|---|---|
| Intellectual property | **Low**: Annachy's own screen layers (lines, stars, simple shapes); no third-party library or brand mark | — |
| Colour or stroke not as expected | Low | The export *is* the source of truth; a pixel check compares each placed SVG with its export |
| Hairline rendering at fractional sizes | Low / medium | The SVG `viewBox` is kept, and lines are placed at their Figma boxes with the same −1 / −1.5 px wrapper offsets |
| V38 flattened effect | Low | Exported and placed exactly; noted in its README entry |
| Screen fixtures | Low | The screen checks are updated to require each placeholder to contain its SVG at the Figma box, as was done for the icons |

## 6. Effort (after approval)

Export of 28 artworks, plus integration into 50 placeholders across 6 screens, plus fixture updates and a full sequential regression with mutation tests: **about 1.5 h.**


---

## Implementation (2026-11-20) — approved export and integration

**Export (approved).**
- 22 by `download_assets` (svg), using each node's single per-vector SVG, and 6 by the Figma-provided asset links.
- All 28 asset IDs match the manifest.
- Staging: `%TEMP%\annachy-vector-staging\`.
- Whole-node exports include the surrounding page (backdrop and ancestors), so they were **not used**.
- **Disclosure:** for a comparison check only, the export step also fetched Figma's design-context copy of the 22 direct-export artworks. That copy is beyond the two approved methods. It was kept in staging only, used solely for the fidelity comparison below, and deleted at cleanup.

**Delivered.** 28 files in `showcase/screens/assets/vectors/`, each **byte-identical** to its Figma export (SHA-256 checked). They fill **50 placeholders, one occurrence each**, across 6 screens. Each placeholder:
- keeps its exact Figma node box (no layout change; all screen-geometry checks unchanged);
- gets `data-annachy-vector` / `data-vec-artwork`;
- places the original SVG with Figma's own wrapper (inset −1 / −1.5 px, the star insets, V38's negative insets with overflow visible);
- for the vertical lines and V36, uses Figma's rotation (90°; 43.45° for the diagonal, taken from Figma's parent design context).

Tool: `tests/tools/r10_integrate_vectors.py` (idempotent; refuses to overwrite).

### Actual SVG properties (read from the exported files; nothing approximated)

| Artwork | Uses | Source node | Method | SVG size | Fill | Stroke | Stroke width | Opacity | Dashed | Fidelity vs Figma's 2nd rendering | File |
|---|---:|---|---|---|---|---|---|---|---|---|---|
| R01 | 2 | `1375:30923` | direct | 610 × 1 | — | #BFC4CF | None | — | yes | dash phase differs (1986/2200 px) | `line-c4a54-610x0.svg` |
| R02 | 1 | `1375:30933` | direct | 27 × 1 | — | #6E7B84 | None | — | yes | dash phase differs (316/432 px) | `line-600fb-0x27.svg` |
| R03 | 1 | `1375:30937` | direct | 17 × 1 | — | #6E7B84 | None | — | yes | dash phase differs (64/272 px) | `line-65fb2-0x17.svg` |
| R04 | 1 | `1375:31002` | direct | 610 × 1 | — | #6E7B84 | None | — | yes | dash phase differs (1722/2200 px) | `line-3adb7-610x0.svg` |
| R05 | 1 | `1375:31076` | direct | 32 × 32 | — | — | — | — |  | both empty | `line-63f38-610x0.svg` |
| R06 | 6 | `1375:31127` | direct | 270 × 1 | — | url(#paint0_linear_0_4) | None | — |  | exact (0 px) | `line-4ff1b-270x0.svg` |
| R07 | 1 | `1375:31393` | direct | 1200 × 1 | — | #6E7B84 | None | — | yes | dash phase differs (600/1200 px) | `line-8879d-1200x0.svg` |
| R08 | 3 | `1629:12011` | direct | 328 × 1 | — | #F5F5F5 | None | — |  | exact (0 px) | `line-4c2ad-328x0.svg` |
| R09 | 1 | `1629:12566` | direct | 306 × 1 | — | #F5F5F5 | None | — |  | exact (0 px) | `line-31c80-306x0.svg` |
| R10 | 4 | `1629:12126` | direct | 304 × 1 | — | #F5F5F5 | None | — |  | exact (0 px) | `line-06fc3-304x0.svg` |
| R11 | 4 | `I1608:7152;1539:30179;1539:28950` | link | 30 × 1 | — | #575D62 | None | — |  | no 2nd reference | `line-2e905-30x0.svg` |
| R12 | 2 | `I1608:7153;1546:27123;1546:27436;1010:22241` | link | 78.5175 × 1.5 | — | #CDCDCD | 1.5 | — |  | no 2nd reference | `line-42e60-57x54.svg` |
| R13 | 1 | `1608:7182` | direct | 54 × 1 | — | #DBE1E4 | None | — |  | exact (0 px) | `line-64c45-54x0.svg` |
| R14 | 1 | `1608:7272` | direct | 32 × 32 | — | — | — | — |  | both empty | `line-6aff8-328x0.svg` |
| R15 | 1 | `I1608:7274;1548:33550` | link | 32 × 32 | — | — | — | — |  | both empty | `line-abbb0-362x0.svg` |
| R16 | 1 | `I1608:7348;1548:33550` | link | 32 × 32 | — | — | — | — |  | both empty | `line-22d2c-328x0.svg` |
| R17 | 1 | `1608:7363` | direct | 18 × 1 | — | #EAEBEC | None | — | yes | dash phase differs (208/288 px) | `line-1f27c-0x18.svg` |
| R18 | 1 | `1608:7389` | direct | 328 × 1 | — | #E5E7E8 | None | — |  | exact (0 px) | `line-f1aa6-328x0.svg` |
| R19 | 1 | `1608:7390` | direct | 362 × 1 | — | #E5E7E9 | None | — | yes | dash phase differs (2610/3300 px) | `line-9d56e-362x0.svg` |
| R20 | 1 | `1201:9800` | direct | 13.7418 × 13.1184 | #FDD349 | — | — | — |  | exact (0 px) | `star-2834b-16x16.svg` |
| R21 | 1 | `I1280:10408;1528:26138;1523:25927` | link | 13.7418 × 13.1184 | #FDD349 | — | — | — |  | no 2nd reference | `star-0c3c4-16x16.svg` |
| R22 | 2 | `1280:10629` | direct | 15.0449 × 14.3777 | #FDD349 | — | — | — |  | exact (0 px) | `star-2efa9-18x18.svg` |
| R23 | 1 | `1375:30871` | direct | 61.9467 × 73.0653 | #F0F7FE, white | #141B34, #D5EAFE | 0.794188, 1.19128 | — |  | exact (0 px) | `vector-frame-ab45f-47_65x47_65.svg` |
| R24 | 1 | `1629:12007` | direct | 12 × 12 | #00D34D | — | — | — |  | exact (0 px) | `shape-bcf26-12x12.svg` |
| R25 | 1 | `I1608:7387;1321:18884` | link | 15.2975 × 14.6035 | #FDD349 | — | — | — |  | no 2nd reference | `star-c2e28-17_81x17_81.svg` |
| R26 | 7 | `1608:7439` | direct | 8.18956 × 7.81803 | #FDD349 | — | — | — |  | exact (0 px) | `star-c6cc8-9_54x9_54.svg` |
| R27 | 1 | `1627:11933` | direct | 15 × 1.25 | black | — | — | — |  | exact (0 px) | `shape-58769-15x1_25.svg` |
| R28 | 1 | `1627:11938` | direct | 15 × 15 | black | — | — | — |  | exact (0 px) | `shape-a6156-15x15.svg` |

### Validation

| Check | Result |
|---|---|
| Byte integrity: 28 delivered files equal to their Figma exports | **28 / 28** |
| Pixel fidelity: delivered file vs Figma's independent design-context rendering (22 with a 2nd reference; exact colour comparison at up to 4×) | **13 / 13 solid artworks with ink: exact (0 px)**. 2 empty artworks: both empty. **7 dashed artworks differ in dash phase only** (see below). 6 asset-link artworks have no second reference |
| Screen fixtures: every vector placeholder holds exactly its declared artwork, loaded, at the exported SVG size (or the node box for no-wrapper artworks); no other image or SVG allowed | Sample Screen **1,363 / 0**, PDP **303 / 0** |

### Unresolved differences (recorded, not corrected)

| ID | Item | Detail |
|---|---|---|
| R10-U1 | **Dash phase** of the 7 dashed artworks (R01–R04, R07, R17, R19; 8 elements) | Figma's two outputs disagree. The SVG export uses `stroke-dasharray="2 2"` starting at the line start; the design-context rendering draws the same dashes shifted by half a dash, with half-length end dashes. Dash count and ink are equal. Which one Figma's canvas shows cannot be determined without a screenshot (not permitted). **Delivered: the approved direct export.** |
| R10-U2 | Rotation direction of the 3 vertical dashed lines (R02, R03, R17) | The 90° turn sits in an ancestor that Figma does not return. Placed at +90°; −90° would move the dash phase by up to one dash. A solid line would look identical either way |
| R10-U3 | 4 empty artworks (R05, R14, R15, R16) | Figma's own export of these nodes contains no visible geometry. Reproduced as Figma renders them: nothing visible, and the placeholder preview is removed |
| R10-U4 | V23 placeholder offset | The screen reproduction places the rotated line box at left −11 px. Figma's centring would give −10.76 px. Pre-existing screen geometry, left unchanged (0.24 px) |
