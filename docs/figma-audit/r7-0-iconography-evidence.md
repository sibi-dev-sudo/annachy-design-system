# R7-0: Iconography evidence (live file, 2026-11-20)

File `rM3ixSG6i3DFfKZFWuxzs4`. All Figma access was read-only: `get_metadata` and `get_design_context` (always with `excludeScreenshot: true`). No assets were fetched, downloaded or saved. Machine-readable data is in `r7-0-iconography-inventory.json`.

## 0. Headline: the new icons are not on the Iconography page

- **`375:10889` "③ Iconography" has not changed.** The live page-level `get_metadata` matches the saved snapshot `raw/metadata/375-10889.xml` exactly: 23,242 nodes, with 0 added, 0 removed and 0 changed (all ids, names and attributes compared). Node-level reads inside this page (`478:68261`, `561:36135`) now return "invalid node selection".
- **The new icons are on a new page, `1801:5142` "② Icons ✓"**, under ③ COMPONENTS. The page list shows it between ② Input and ③ Input Dropdown. It is the Annachy Outline/Filled icon catalogue, the model previously called S5 / "Annachy Icons File", now built as **local components in this file**.

## 1. Totals

| Page | Component sets | Variants (components) | Unique icon names | Categories | Styles | Sizes |
|---|---:|---:|---:|---:|---|---|
| **1801:5142 ② Icons (NEW)** | **5,128** (4,869 without the duplicate frame) | **35,890** | **4,839** | 33 frames (32 distinct names) | Outline, Filled | XS 16, S 20, M 24, L 32, XL 40 |
| 375:10889 ③ Iconography: Solar catalogue | 1,252 | 7,512 | 1,226 | 37 | Linear, Bold, Bold Duotone, Broken, Line Duotone, Outline | 24 only |
| 375:10889 ③ Iconography: Solar pilots | 52 | 14,040 | 52 | — | the same 6 | 14, 16, 20, 24, 28, 32, 36, 38, 42 × 5 semantic states |

Style breakdown on the new page:

| Style | Sets |
|---|---:|
| Outline + Filled pairs (10 variants each) | 2,050 |
| Outline only, with a `Style` property | 2,340 |
| Outline only, size-only sets with no `Style` property ("Outline Only" groups) | 462 |
| Filled only, with a `Style` property | 264 |
| Filled only, size-only sets | 12 |

Every set has all five sizes (16/20/24/32/40). The old audit counted 1,243 Solar catalogue slots. This count of 1,252 uses the rule "frame whose children are all components". 3 sets misspell the style ("Bold Doutone", "Bold Duotine"), and `Arrows Action/Login 3` has no Style property.

## 2. Categories on the new page (sets / variants)

| Category | Sets | Variants | Category | Sets | Variants |
|---|---:|---:|---|---:|---:|
| Message `1802:83` | 977 | 5,275 | Arrow `1802:210466` | 707 | 4,195 |
| Brands `1802:185706` | 624 | 3,930 | Calender & date `1802:121134` | 259 | 1,460 |
| Calender & date (duplicate) `1802:138448` | 259 | 1,460 | Chart & Analytics `1802:96820` | 179 | 1,110 |
| Transport `1802:34747` | 168 | 1,045 | Security `1802:109815` | 163 | 1,400 |
| User `1802:83547` | 158 | 1,175 | Editor `1802:55641` | 147 | 1,370 |
| Fashion `1802:91157` | 136 | 680 | Audio `1802:168218` | 117 | 1,170 |
| Locations `1802:162401` | 106 | 1,040 | Design `1802:71034` | 102 | 1,020 |
| Documentation `1802:77823` | 98 | 980 | Shopping `1802:179912` | 94 | 910 |
| Banking `1802:175229` | 73 | 730 | Home `1802:65556` | 70 | 620 |
| Search `1802:135542` | 69 | 565 | Alerts `1802:155436` | 66 | 660 |
| Filters & Setting `1802:43168` | 66 | 655 | Hand `1802:46777` | 61 | 550 |
| Star `1802:52385` | 58 | 415 | Delivery `1802:104425` | 55 | 530 |
| Heart & Love `1802:50041` | 45 | 390 | Bookmark `1802:158845` (nested in Alerts) | 44 | 410 |
| Home and Applances `1802:107304` | 43 | 380 | Email `1802:63411` | 42 | 375 |
| Time `1802:68739` | 36 | 350 | Call `1802:152856` | 31 | 300 |
| Building `1802:119276` | 29 | 280 | Bath & WC `1802:160705` | 27 | 270 |
| Airports `1802:154541` | 19 | 190 | | | |

Anomalies:
- "Calender & date" appears twice, with identical names: 259 + 259 sets.
- The in-file labels disagree with the actual set counts: Design says 116 identities but has 102 sets; Documentation says 104 but has 98; Brands says 625 but has 624.
- Category names contain typos: "Calender", "Applances".
- There is a stray instance `1802:82` "Arrows/Up Square 1" at page root.
- A header section `1802:30` contains a non-component "Logotype" frame `1802:40`.
- The **Brands** category holds 624 third-party brand icons (e.g. Adobe After Effects, Admob). These may raise licensing questions.

The 37 Solar categories on 375:10889 are unchanged from `06-iconography-assets.md` §4. Per-category counts are in the JSON.

## 3. Component descriptions (plugin output)

Sampled sets carry builder descriptions:

| Kind | Description pattern |
|---|---|
| Matched pair | "Matched Outline/Filled icon … Outline source "X" (id) · Filled source "Y" (id) · match: primary-visual" |
| Manual split | "Manually split Outline-only icon … Original pair source mapping preserved in plugin data" |
| Single style | "Single-style Filled icon … match: auto-confirmed-single" |
| Size-only | "Outline only; size-only set, no Style property" |

Each variant also has its own description, e.g. "Home/Home 54 · Outline · 16x16 · source layer "Home " (370:50569)".

## 4. Icons used by library components (task 2)

| Need | Old node | Found on new page? | New set | Styles / sizes | Notes |
|---|---|---|---|---|---|
| Home/Home 54 | `1777:9468` / `1777:12415` | **Yes** | `1802:68148` | Outline+Filled / XS–XL | The Filled variants are "Home 35" artwork (`261:12274`). |
| User/User Curved | `1779:36485` / `1779:37533` | **Yes** | `1802:86130` | Outline+Filled / XS–XL | Same description as the old set. |
| Arrow/Chevron Up | `1779:38813` / `1779:38814` | **Yes** | `1802:211244` | Outline+Filled / XS–XL | Filled = "Down" layer flipped with scale-y(-1). |
| Arrow/Chevron Down | `1779:39438` / `1779:39439` | **Yes** | `1802:211124` | Outline+Filled / XS–XL | Filled = "Up" layer flipped. |
| Alerts/Error circle | `1780:40127` / `1780:40128` | **Yes** | `1802:155982` | Outline+Filled / XS–XL | In the Alerts "Matched" group. |
| Cloud (Solar pilot) | `561:36135` (set `561:36765`) | Not on the new page | still listed on 375:10889 | 6 styles / 9 sizes | Node-level reads fail. Input Filled `1066:40783` now shows S5 icons, not Cloud. |
| Dropdown "Selected" check | instance `1451:24796` | No | — | — | Still a Lucide badge-check instance. No main name is exposed. Name-only candidates: Alerts/Check badge `1802:155448`, Alerts/Checkmark `1802:155740`. |
| Dropdown "checkbox" | instance `1454:7202` | No | — | — | Name-only candidate: Alerts/Check square `1802:155698`. |
| Checkbox functional/check | frame `1504:53703` | No | — | — | A local frame, not an icon component. |

**Important:** the components have **not been relinked** to the new sets.
- Button `887:364` still instances `1777:12415`.
- Input Outline `1066:38089` and Input Filled `1066:40783` still instance `1779:37533`, `1779:38814`, `1779:39439` and `1780:40128`.
- Those old main nodes return "invalid node selection" when queried directly, so they are not on a visible page.

The new sets have identical descriptions to the old ones. Their asset-URL file tokens for the used variants are also identical:

| Icon variant | Asset token |
|---|---|
| Home S/Outline | `7d88c` |
| User Curved M/Outline | `4ff9d` |
| Chevron Up M/Filled | `1a900` |
| Chevron Down M/Filled | `4ff27` |
| Error circle XS/Outline | `7064b` |

The old copies are probably the same artwork, but this is inferred from the tokens and was not verified by fetching.

## 5. Screen placeholders (task 3)

The parser found 362 `scr-asset` placeholders: 215 icons, 141 images and 6 logos.

| File | EXACT | NAME_ONLY | NO_MATCH | Images | Logos |
|---|---:|---:|---:|---:|---:|
| pdp/pdp-v1.html | 38 | 18 | 29 | 40 | 0 |
| pdp/mobile.html | 1 | 5 | 6 | 1 | 0 |
| pdp/desktop-bg-colours.html | 0 | 0 | 0 | 1 | 0 |
| sample-screen/desktop-pdp-1375-30858.html | 4 | 0 | 35 | 32 | 6 |
| sample-screen/mobile-pdp-1608-7090.html | 19 | 17 | 29 | 58 | 0 |
| sample-screen/job-listing-page-1629-11987.html | 0 | 0 | 7 | 5 | 0 |
| sample-screen/mobile-putaway-1627-11756.html | 0 | 0 | 7 | 4 | 0 |
| **Total** | **62** | **40** | **113** | **141** | **6** |

**EXACT (62)**
- 32 are library instances (Home 54 ×21, User Curved ×3, Chevron Up ×3, Chevron Down ×3, Error circle ×2). They match the new sets on `1801:5142` by name, style and size. Their own main components are still the hidden 1777/1779/1780 copies.
- 30 are detached Solar-named frames at 24 px whose name and style exist in the 375:10889 catalogue: Alt Arrow Left, Heart, Magnifer, Shop, Arrow Right, Map Point and others.

**NAME_ONLY (40)**
- Solar-named frames at a non-24 size (e.g. Heart 19.2/28, Alt Arrow Left 18/20/28, Cart Large 2 28, Play Circle 18), or with no style prefix (Gallery Minimalistic).
- The catalogue has these icons only at 24 px, and the 52 pilots do not include them.

**NO_MATCH (113)**
- 24 are primitive shapes (Star polygons, ellipse, minus/plus vectors, a strike line).
- 34 are generic "Frame" layers on Desktop PDP. `get_metadata` on `1375:30858` returns no children and `1375:31338` is just "Frame", so only the replica's semantic hints are available (location, chevron, profile, cart and so on).
- 24 are "Icons / Group …" perk icons.
- The rest are status-bar glyphs (Wifi, Battery, Signal, Phone Camara) and custom vectors (loyalty 1, badge-percent, ArrowLeft, Car, Group …).

**Logos (6):** the Desktop PDP Logotype plus 5 "logo 2". 375:10889 contains no brand logos. 1801:5142 has the Annachy "Logotype" frame (not a component) and a third-party "Brands" icon category.

## 6. How artwork is exposed

`get_design_context` exposed every sampled icon only as temporary **asset URLs** (`https://www.figma.com/api/mcp/asset/…/<token>.svg`) referenced from `<img>` tags. No inline vector path data was returned.
- Sampled on the new page: 8 sets.
- Sampled elsewhere: the Button and Input instances, plus `1451:24796`, `1454:7202` and `1504:53703`.
- `get_metadata` gives only node types and sizes.
- Solar icons on 375:10889 could not be sampled (invalid node selection), so their artwork is "unknown".
- **No asset URL was fetched, opened, downloaded or copied into any file.**

## 7. Figma calls (32 in total: get_metadata 14, get_design_context 18, get_variable_defs 0; 9 failed)

| # | Tool | Node | Result |
|---:|---|---|---|
| 1 | get_metadata | `375:10889` | ok (2.6 MB, parsed from the saved tool output) |
| 2 | get_metadata | (page list) | ok |
| 3 | get_metadata | `1801:5142` | ok (9.4 MB, parsed) |
| 4 | get_design_context | `1802:68148` | ok |
| 5 | get_metadata | `1777:9468` | **invalid** |
| 6 | get_metadata | `1779:36485` | **invalid** |
| 7 | get_metadata | `1779:38813` | **invalid** |
| 8 | get_metadata | `1780:40127` | **invalid** |
| 9 | get_metadata | `1451:24796` | ok |
| 10 | get_metadata | `1454:7202` | ok |
| 11 | get_metadata | `1504:53703` | ok |
| 12 | get_design_context | `1777:12415` | **invalid** |
| 13 | get_design_context | `1779:37533` | **invalid** |
| 14 | get_metadata | `887:364` | ok |
| 15 | get_design_context | `887:364` | ok |
| 16 | get_design_context | `1066:38089` | ok |
| 17 | get_design_context | `1802:86130` | ok |
| 18 | get_design_context | `1802:211244` | ok |
| 19 | get_design_context | `1802:211124` | ok |
| 20 | get_design_context | `1802:155982` | ok |
| 21 | get_design_context | `1451:24796` | ok |
| 22 | get_design_context | `1454:7202` | ok |
| 23 | get_design_context | `1504:53703` | ok |
| 24 | get_design_context | `1802:96` | ok |
| 25 | get_design_context | `1802:194721` | ok |
| 26 | get_design_context | `1802:34193` | ok |
| 27 | get_design_context | `478:68261` | **invalid** |
| 28 | get_design_context | `561:36135` | **invalid** |
| 29 | get_metadata | `478:68261` | **invalid** |
| 30 | get_design_context | `1066:40783` | ok |
| 31 | get_metadata | `1375:30858` | ok (no children returned) |
| 32 | get_metadata | `1375:31338` | ok ("Frame") |

## 8. Not inspected / limits

- Per-set descriptions were read for only 8 of the 5,128 new sets. The other sets have `description: null` in the JSON.
- Main components were not read for the 34 generic desktop "Frame" layers or for nested `I…` instance ids in pdp-v1.
- Solar icons on 375:10889 could not be read at node level.
- Matches against the Solar catalogue are name-based, because the screens use detached frames rather than instances.
