# R8-0 — Remaining Screen Assets: Exact Sources and Export Requirements

| Item | Value |
|---|---|
| Date | 2026-11-20 |
| Scope | Every screen placeholder not yet filled: **328 placeholders = 330 page elements** (2 Figma nodes appear twice) |
| Method | Saved metadata, 131 `get_metadata` lookups (3 nodes unreadable), 1 `get_design_context` (screenshot excluded), 9 `get_variable_defs`. **No exports** (`download_assets` not used; no asset URL fetched) |
| Data | `r8-0-remaining-assets.json` (every element with its evidence) |

## 1. Solar icons (70 elements = 68 placeholders + 2 repeated elements) — source page `375:10889`

| Mapping | Elements | Meaning |
|---|---:|---|
| EXACT | 30 | Same set, style and size (24 px) |
| SCALED_24 | 39 | The screen uses the same Solar artwork resized (16, 18, 19.2, 20 or 28 px). The catalogue holds 24 px only, so the source is the 24 px variant, scaled |
| UNRESOLVED | 1 | `1280:10643` "Gallery Minimalistic", 18 px. The name exists on the page, but the style of this detached copy is not recorded |

**"Play Circle" (the 2 candidates):** resolved to Solar `478:70344` (Outline, scaled 18/24). The screen layers use Solar naming and style vocabulary, not the Icons page's "Audio/Play Circle".

**Minimal export list: 11 Solar variants**

| Variant node | Icon | Style | Category | Set |
|---|---|---|---|---|
| `478:70344` | Play Circle | Outline | Video, Audio, Sound | `478:70334` |
| `478:71460` | Users Group Two Rounded | Outline | Users | `478:71438` |
| `478:74888` | Shop | Linear | Shopping, Ecommerce | `478:74878` |
| `478:75026` | Cart Large 2 | Outline | Shopping, Ecommerce | `478:75010` |
| `478:76191` | Shield Check | Linear | Security | `478:76184` |
| `478:77183` | Magnifer | Linear | Search | `478:77176` |
| `478:82716` | Map Point | Outline | Map & Location | `478:82706` |
| `478:83926` | Like | Outline | Like | `478:83918` |
| `478:84069` | Heart | Linear | Like | `478:84063` |
| `478:96800` | Arrow Right | Linear | Arrow | `478:96794` |
| `478:96898` | Alt Arrow Left | Line Duotone | Arrow | `478:96895` |

## 2. Unidentified screen layers (113)

| Classification (evidence) | Count | Reproducible by |
|---|---:|---|
| empty icon frame (vector content not in metadata) | 41 | export of the node (vector) |
| component instance | 29 | export of the master component |
| local shape: star | 12 | export of the node (vector) |
| frame (saved metadata) | 11 | export of the node (vector) |
| status-bar glyph | 6 | status bar: system UI, out of design-system scope |
| unreadable (invalid node selection) | 6 | cannot be read with the allowed tools |
| frame with instances | 3 | export of the node (vector) |
| local shape: vector | 2 | export of the node (vector) |
| local shape: line | 1 | export of the node (vector) |
| frame with frame×1, vector×1 | 1 | export of the node (vector) |
| local shape: ellipse | 1 | export of the node (vector) |

- **24 of the component instances** are "Icons" instances. `get_design_context` on one shows the main component **`5:26` "Icons / Property 1=1"** (Brainstorming page `0:1`): a single 24 px icon reused by those 24 elements. One export of `5:26` would fill them all.
- The remaining instances are "Similar Products- Card" (4) and one frame group. They are composite cards whose icon content is vector artwork inside the instance.
- **"Empty icon frame":** frames 12–38 px whose vector children are not in the saved metadata (detached icon copies). They need export of the frame.
- **No replacement was invented** for any of them.

## 3. Images (141) and logos (6)

| Source layer type | Count |
|---|---:|
| image · slot | 48 |
| image · line | 33 |
| image · instance | 22 |
| image · rounded-rectangle | 21 |
| image · frame | 12 |
| image · vector | 5 |
| logo · rounded-rectangle | 5 |
| logo · frame | 1 |

| Group | Detail |
|---|---|
| Product photos | `rounded-rectangle` image fills (e.g. "010834LBLU_1", ~268×402 / 106×159), "Similar Products - Images" (185×247), "Product Image", "Image-2/3/4", "Images", "Component 102" (colour-variant swatches) |
| Image slots | 48 `slot` layers (image areas inside instances) |
| Divider / stroke lines (33) | Not images: vector lines whose stroke colour is **only** in their SVG. Their variables are unbound (7 lines) or ambiguous (two colours on 1 line), so the colour cannot be taken without export. **Export needed** (or an owner-confirmed colour) |
| Decorative vectors | "Vector 1 (offer ribbon)" × 5 and others |
| Logos (6) | "Logotype (Group)" ×1 = **Annachy's own logotype**; "logo 2" ×5 (Desktop PDP) = brand logos in a strip (third-party marks; **rights needed**) |

Duplicates: 141 image elements come from 67 distinct layer names. Repeated card images (e.g. "Similar Products - Images" × 14) can share one export per distinct image.

## 4. Consolidated export requirement (owner approval needed)

| # | Page | What | Nodes | Fills |
|---|---|---|---:|---:|
| A | `375:10889` Iconography (Solar) | 11 Solar 24 px variants (table §1) | 11 | 69 icon elements |
| B | `0:1` Brainstorming | "Icons" master `5:26` | 1 | 24 icon elements |
| C | `1375:30857` Sample Screen / `581:11523` PDP | Image fills (photos, slots, swatches, ribbons) | ≤ 108 (67 distinct names) | 108 image elements |
| D | same | 33 divider / stroke lines (or an owner-confirmed colour per line) | 33 | 33 elements |
| E | same | Annachy logotype (own mark) | 1 | 1 |
| F | same | 5 third-party brand logos ("logo 2") | 5 | 5, **plus brand rights** |
| G | same | Detached icon frames / local vector groups / stars (§2) | ≤ 76 | ≤ 76 |
| — | — | 6 status-bar glyphs: system UI (time, signal, Wi-Fi, battery) | — | **N/A** (out of design-system scope) |
| — | — | 6 unreadable nodes ("invalid node selection") + "Gallery Minimalistic" style | — | **Blocked** (not readable) |
