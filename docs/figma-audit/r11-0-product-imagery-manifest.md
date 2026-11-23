# R11-0 — Product Imagery: Audit, Export Manifest and Implementation

> **Status 2026-11-20: IMPLEMENTED** under the owner's consolidated approval (internal reproduction only). Sections 1–7 are the
> read-only audit as written before export; corrections found during implementation are added as dated notes. See **§8 Implementation**.

| Item | Value |
|---|---|
| Date | 2026-11-20 |
| Scope | **108 placeholders**: the image-related placeholders remaining after R10 (141 image placeholders minus the 33 lines delivered in R10) |
| Data | `r11-0-product-imagery-manifest.json`: per element, node, screen, size, classification, image layers with crop / position classes, background colours, radius, rights class, plan; per unique artwork, uses and destination |
| Inspection | Read-only: `get_metadata` ×108 + `get_design_context` ×108 (screenshots excluded), plus 2 independent spot-checks. **No export, no download, no asset URL fetched or stored** (short artwork IDs only) |

## 1. Totals

| Measure | Count |
|---|---:|
| Placeholders | **108** (all resolved to their screen placeholder; I001–I003 are `<div>` placeholders) |
| By kind | product photo 85 · composite card / overlay 8 · ribbon / badge vector 6 · decorative vector 5 · colour fill 2 · screenshot 1 · other (emoji raster) 1 |
| **Unique raster images** | **43** (all PNG) |
| **Unique vectors** | **14** (of which 3 are already in the project or cancelled, and 5 are status-bar parts; see §3) |
| Elements with no image at all | 5: 3 "Air" streaks (CSS gradients) and 2 device-chrome fills ("Bottom Edge", "Home Indicator") |
| Shared artwork | 28 groups cover 78 elements. `9b5e5.png` is used 16× (including inside the cards). The Mobile PDP galleries repeat the PDP V1 galleries |
| Existing project assets | **0 raster files in the project**. `showcase/screens/assets/images/` does not exist, so no duplicates and no overwrites are possible |

## 2. Rights and ownership (from Figma layer names; nothing here grants rights)

| Rights class (raster) | Unique images | Evidence | Concern |
|---|---:|---|---|
| **AI-generated (Gemini file name)** | 8 | Layers named "Gemini_Generated_Image_1xd3lh…", "…4h4hcm…", "…cfwhol…", "…nwrqcf…" (24 elements) | AI-generated images sitting **in the Figma source** (not substitutes). The design team should confirm they are approved for this use. Google's terms and any brand or likeness content need checking |
| **Product photos (SKU file names)** | 12 | "010834LBLU_1…_4", "010834LBLA_1", "010834LOLI_1", "010834LGRE_1", "010834LRED2_1", "003372XLOFFWHI_1", "01135542DARGRE_1", "01135542MUS_1" | Retailer-style SKU names. **Whose photography?** If it is Annachy's own catalogue, it can be used; if it was copied from another retailer's site, it cannot |
| **Web downloads (generic names)** | 8 | "unnamed (2)…(7) 1", "BL / Orginal Image" | Typical of images saved from the web. **Source unknown: high risk** |
| Screenshot | 1 | "Screenshot 2026-09-23 at 4.46.29 PM 1" (Desktop / BG Colours, 1440 × 931) | What it shows (and whose UI) is unknown; it may be a third-party site |
| Emoji raster | 1 | "🥽 Goggles (Swimming, Diving, Gear)" (48 px) | Emoji artwork belongs to its vendor (Apple, Google, Microsoft…) |
| Unattributed | 13 | Names like "Product Image", "Component 102", product titles | No provenance in the file |

**No watermarks or third-party brand names appear in any text.** Hidden layers on 4 cards contain different product titles ("Cotton Blend Printed Kurti for Women") from the visible text: a sign the cards were reused templates.

## 3. Unique artwork

### Raster (43)

| Artwork | Uses | Rights class | Layer names | Note | Elements |
|---|---:|---|---|---|---|
| `9b5e5.png` | 16 | unattributed | Component 102, Floral Print Georgette Saree |  | I004, I005, I006, I011, I012, I013, I014, I030, I063, I064, I065, I075, I076, I077, I078, I094 |
| `03aef.png` | 4 | AI-generated (Gemini file name) | Gemini_Generated_Image_1xd3lh1xd3lh1xd3 (1) 2 |  | I025, I037, I089, I101 |
| `2b984.png` | 4 | AI-generated (Gemini file name) | Gemini_Generated_Image_4h4hcm4h4hcm4h4h 1 |  | I028, I040, I092, I104 |
| `402da.png` | 4 | unattributed | Product Image |  | I024, I036, I088, I100 |
| `9b8bc.png` | 4 | web download (generic file name) | unnamed (2) 1 |  | I029, I041, I093, I105 |
| `ba181.png` | 4 | AI-generated (Gemini file name) | Gemini_Generated_Image_1xd3lh1xd3lh1xd3 (4) 1 |  | I027, I039, I091, I103 |
| `cde73.png` | 4 | AI-generated (Gemini file name) | Gemini_Generated_Image_1xd3lh1xd3lh1xd3 1 |  | I026, I038, I090, I102 |
| `04813.png` | 2 | web download (generic file name) | unnamed (7) 1 |  | I021, I085 |
| `073bd.png` | 2 | AI-generated (Gemini file name) | Gemini_Generated_Image_4h4hcm4h4hcm4h4h 1 |  | I034, I098 |
| `1a18a.png` | 2 | AI-generated (Gemini file name) | Gemini_Generated_Image_cfwholcfwholcfwh 1 |  | I032, I096 |
| `1b7eb.png` | 2 | unattributed | Component 102 |  | I007, I066 |
| `1d5d1.png` | 2 | unattributed | Frame 2121454585 |  | I008, I071 |
| `33dc1.png` | 2 | AI-generated (Gemini file name) | Gemini_Generated_Image_nwrqcfnwrqcfnwrq 1 |  | I033, I097 |
| `3fba2.png` | 2 | web download (generic file name) | unnamed (6) 1 |  | I019, I083 |
| `414f3.png` | 2 | product photo (SKU-style file name) | 01135542DARGRE_1 1 |  | I054, I060 |
| `4fbd0.png` | 2 | unattributed | Embroidered Silk Saree with Intricate Design, Similar Products - Images |  | I016, I080 |
| `58f8f.png` | 2 | web download (generic file name) | unnamed (3) 1 |  | I020, I084 |
| `59c8b.png` | 2 | web download (generic file name) | unnamed (2) 1 |  | I035, I099 |
| `62f2c.png` | 2 | unattributed | Printed Georgette Saree, Similar Products - Images |  | I017, I081 |
| `7bc8a.png` | 2 | unattributed | Images, Product Image - 1 |  | I009, I072 |
| `7c131.png` | 2 | unattributed | Product Image -2 |  | I010, I073 |
| `8b1ad.png` | 2 | unattributed | Component 102 |  | I005, I064 |
| `8c432.png` | 2 | unattributed | YL |  | I003, I062 |
| `8ced0.png` | 2 | product photo (SKU-style file name) | 010834LOLI_1 1 |  | I048, I058 |
| `90500.png` | 2 | unattributed | Component 102 |  | I006, I065 |
| `aa915.png` | 2 | web download (generic file name) | BL / Orginal Image |  | I018, I082 |
| `b1e96.png` | 2 | unattributed | Elegant Linen Saree with Zari Border, Similar Products - Images |  | I015, I079 |
| `bcdd6.png` | 2 | web download (generic file name) | unnamed (4) 1 |  | I023, I087 |
| `bf527.png` | 2 | web download (generic file name) | unnamed (5) 1 |  | I022, I086 |
| `f0b93.png` | 2 | AI-generated (Gemini file name) | Gemini_Generated_Image_1xd3lh1xd3lh1xd3 (1) 2 |  | I031, I095 |
| `0fe59.png` | 1 | emoji raster | 🥽 Goggles (Swimming, Diving, Gear) |  | I108 |
| `10735.png` | 1 | product photo (SKU-style file name) | 010834LBLU_1 1 |  | I043 |
| `1c8d9.png` | 1 | product photo (SKU-style file name) | 003372XLOFFWHI_1 1 |  | I052 |
| `26d80.png` | 1 | unattributed | Image |  | I002 |
| `2aa70.png` | 1 | product photo (SKU-style file name) | 010834LBLU_4 1 |  | I046 |
| `6ee12.png` | 1 | product photo (SKU-style file name) | 010834LBLA_1 1 |  | I047 |
| `80d72.png` | 1 | product photo (SKU-style file name) | 010834LGRE_1 1 |  | I049 |
| `94028.png` | 1 | product photo (SKU-style file name) | 010834LBLU_3 1 |  | I045 |
| `a5d09.png` | 1 | product photo (SKU-style file name) | 010834LBLU_2 1 |  | I044 |
| `d4119.png` | 1 | product photo (SKU-style file name) | 01135542MUS_1 1 |  | I056 |
| `dccd6.png` | 1 | product photo (SKU-style file name) | 010834LRED2_1 1 |  | I051 |
| `f5d4e.png` | 1 | product photo (SKU-style file name) | 010834LBLUGRE_1 1 |  | I050 |
| `f8cdd.png` | 1 | screenshot | Screenshot 2026-09-23 at 4.46.29 PM 1 |  | I001 |

### Vectors (14)

| Artwork | Uses | | Layer names | Note | Elements |
|---|---:|---|---|---|---|
| `394d3.svg` | 7 | (vector) | Elegant Linen Saree with Zari Border, Embroidered Silk Saree with Intricate Design | unidentified vector inside a card: identify before export | I011, I012, I013, I014, I015, I016, I017 |
| `c6cc8.svg` | 7 | (vector) | Elegant Linen Saree with Zari Border, Embroidered Silk Saree with Intricate Design | R10 rating star (already delivered: reuse, no export) | I011, I012, I013, I014, I015, I016, I017 |
| `598fb.svg` | 5 | (vector) | Vector 1 | offer ribbon 'Vector 1' (Annachy design layer) | I053, I055, I057, I059, I061 |
| `7d14a.svg` | 5 | (vector) | Elegant Linen Saree with Zari Border, Floral Print Georgette Saree | unidentified vector inside a card: identify before export | I011, I012, I013, I014, I015 |
| `16181.svg` | 1 | (vector) | _iPhone mockup status bar | iPhone status bar (system UI: N/A recommended) | I042 |
| `2c135.svg` | 1 | (vector) | _iPhone mockup status bar | iPhone status bar (system UI: N/A recommended) | I042 |
| `45da3.svg` | 1 | (vector) | Images | Gallery Minimalistic (cancelled as not required: out of scope) | I072 |
| `50355.svg` | 1 | (vector) | Group 1171275299 | unidentified vector inside a card: identify before export | I067 |
| `73565.svg` | 1 | (vector) | Frame 2121454395 | unidentified vector inside a card: identify before export | I074 |
| `7d88c.svg` | 1 | (vector) | Floral Print Georgette Saree | Home/Home 54 Outline S (library icon already in src/icons/: reuse, no export) | I013 |
| `7e9c1.svg` | 1 | (vector) | _iPhone mockup status bar | iPhone status bar (system UI: N/A recommended) | I042 |
| `b5ccd.svg` | 1 | (vector) | _iPhone mockup status bar | iPhone status bar (system UI: N/A recommended) | I042 |
| `c1da5.svg` | 1 | (vector) | _iPhone mockup status bar | iPhone status bar (system UI: N/A recommended) | I042 |
| `f4903.svg` | 1 | (vector) | _iPhone mockup status bar | unidentified vector inside a card: identify before export | I042 |

## 4. All 108 placeholder mappings

| ID | Screen | Figma node | Layer | Size (px) | Kind | Artwork | Rights class | Plan |
|---|---|---|---|---|---|---|---|---|
| I001 | `desktop-bg-colours.html` | `605:17525` | Screenshot 2026-09-23 at 4.46.29 PM 1 | 1440 × 931 | screenshot | f8cdd.png | screenshot | export the image layer(s) |
| I002 | `mobile.html` | `1201:9772` | Image | 394.96 × 526 | product-photo | 26d80.png | unattributed | export the image layer(s) |
| I003 | `pdp-v1.html` | `1280:10399` | YL | 393 × 525 | product-photo | 8c432.png | unattributed | export the image layer(s) |
| I004 | `pdp-v1.html` | `I1280:10445;1539:30179;1539:28349` | Component 102 | 75.97 × 101.29 | product-photo | 9b5e5.png | unattributed | export the image layer(s) |
| I005 | `pdp-v1.html` | `I1280:10445;1539:30180;1539:28349` | Component 102 | 75.97 × 101.29 | product-photo | 9b5e5.png, 8b1ad.png | unattributed | export the image layer(s) |
| I006 | `pdp-v1.html` | `I1280:10445;1539:30181;1539:28349` | Component 102 | 75.97 × 101.29 | product-photo | 9b5e5.png, 90500.png | unattributed | export the image layer(s) |
| I007 | `pdp-v1.html` | `I1280:10445;1539:30182;1539:28349` | Component 102 | 75.97 × 101.29 | product-photo | 1b7eb.png | unattributed | export the image layer(s) |
| I008 | `pdp-v1.html` | `1280:10636` | Frame 2121454585 | 187 × 161 | product-photo | 1d5d1.png | unattributed | export the image layer(s) |
| I009 | `pdp-v1.html` | `1280:10640` | Product Image - 1 | 178 × 237 | product-photo | 7bc8a.png | unattributed | export the image layer(s) |
| I010 | `pdp-v1.html` | `1280:10649` | Product Image -2 | 190 × 139 | product-photo | 7c131.png | unattributed | export the image layer(s) |
| I011 | `pdp-v1.html` | `1281:7272` | Similar Products- Card | 172 × 360 | composite | 9b5e5.png, c6cc8.svg, 7d14a.svg, 394d3.svg | unattributed | export the image layers individually (never the whole card: that would bake text into an image) |
| I012 | `pdp-v1.html` | `1283:2642` | Similar Products- Card | 172 × 360 | composite | 9b5e5.png, c6cc8.svg, 7d14a.svg, 394d3.svg | unattributed | export the image layers individually (never the whole card: that would bake text into an image) |
| I013 | `pdp-v1.html` | `1281:7311` | Similar Products- Card | 172 × 371 | composite | 9b5e5.png, c6cc8.svg, 7d14a.svg, 394d3.svg, 7d88c.svg | unattributed | export the image layers individually (never the whole card: that would bake text into an image) |
| I014 | `pdp-v1.html` | `1280:10699` | Similar Products- Card | 172 × 371 | composite | 9b5e5.png, c6cc8.svg, 7d14a.svg, 394d3.svg | unattributed | export the image layers individually (never the whole card: that would bake text into an image) |
| I015 | `pdp-v1.html` | `1280:10700` | Similar Products- Card | 172 × 371 | composite | b1e96.png, c6cc8.svg, 7d14a.svg, 394d3.svg | unattributed | export the image layers individually (never the whole card: that would bake text into an image) |
| I016 | `pdp-v1.html` | `1280:10701` | Similar Products- Card | 172 × 371 | composite | 4fbd0.png, c6cc8.svg, 394d3.svg | unattributed | export the image layers individually (never the whole card: that would bake text into an image) |
| I017 | `pdp-v1.html` | `1280:10702` | Similar Products- Card | 172 × 371 | composite | 62f2c.png, c6cc8.svg, 394d3.svg | unattributed | export the image layers individually (never the whole card: that would bake text into an image) |
| I018 | `pdp-v1.html` | `I1280:10723;1519:25227` | Images | 125 × 158 | product-photo | aa915.png | web download (generic file name) | export the image layer(s) |
| I019 | `pdp-v1.html` | `I1280:10723;1519:25228` | Image-2 | 125 × 70 | product-photo | 3fba2.png | web download (generic file name) | export the image layer(s) |
| I020 | `pdp-v1.html` | `I1280:10723;1519:25229` | Image-3 | 52 × 52 | product-photo | 58f8f.png | web download (generic file name) | export the image layer(s) |
| I021 | `pdp-v1.html` | `I1280:10723;1519:25230` | Image-4 | 52 × 52 | product-photo | 04813.png | web download (generic file name) | export the image layer(s) |
| I022 | `pdp-v1.html` | `I1280:10723;1519:25233` | Image-5 | 52 × 52 | product-photo | bf527.png | web download (generic file name) | export the image layer(s) |
| I023 | `pdp-v1.html` | `I1280:10723;1519:25231` | Image-6 | 52 × 52 | product-photo | bcdd6.png | web download (generic file name) | export the image layer(s) |
| I024 | `pdp-v1.html` | `I1280:10736;1519:25227` | Images | 125 × 158 | product-photo | 402da.png | unattributed | export the image layer(s) |
| I025 | `pdp-v1.html` | `I1280:10736;1519:25228` | Image-2 | 125 × 70 | product-photo | 03aef.png | AI-generated (Gemini file name) | export the image layer(s) |
| I026 | `pdp-v1.html` | `I1280:10736;1519:25229` | Image-3 | 52 × 52 | product-photo | cde73.png | AI-generated (Gemini file name) | export the image layer(s) |
| I027 | `pdp-v1.html` | `I1280:10736;1519:25230` | Image-4 | 52 × 52 | product-photo | ba181.png | AI-generated (Gemini file name) | export the image layer(s) |
| I028 | `pdp-v1.html` | `I1280:10736;1519:25233` | Image-5 | 52 × 52 | product-photo | 2b984.png | AI-generated (Gemini file name) | export the image layer(s) |
| I029 | `pdp-v1.html` | `I1280:10736;1519:25231` | Image-6 | 52 × 52 | product-photo | 9b8bc.png | web download (generic file name) | export the image layer(s) |
| I030 | `pdp-v1.html` | `I1280:10749;1519:25227` | Images | 125 × 158 | product-photo | 9b5e5.png | unattributed | export the image layer(s) |
| I031 | `pdp-v1.html` | `I1280:10749;1519:25228` | Image-2 | 125 × 70 | product-photo | f0b93.png | AI-generated (Gemini file name) | export the image layer(s) |
| I032 | `pdp-v1.html` | `I1280:10749;1519:25229` | Image-3 | 52 × 52 | product-photo | 1a18a.png | AI-generated (Gemini file name) | export the image layer(s) |
| I033 | `pdp-v1.html` | `I1280:10749;1519:25230` | Image-4 | 52 × 52 | product-photo | 33dc1.png | AI-generated (Gemini file name) | export the image layer(s) |
| I034 | `pdp-v1.html` | `I1280:10749;1519:25233` | Image-5 | 52 × 52 | product-photo | 073bd.png | AI-generated (Gemini file name) | export the image layer(s) |
| I035 | `pdp-v1.html` | `I1280:10749;1519:25231` | Image-6 | 52 × 52 | product-photo | 59c8b.png | web download (generic file name) | export the image layer(s) |
| I036 | `pdp-v1.html` | `I1280:10762;1519:25227` | Images | 125 × 158 | product-photo | 402da.png | unattributed | export the image layer(s) |
| I037 | `pdp-v1.html` | `I1280:10762;1519:25228` | Image-2 | 125 × 70 | product-photo | 03aef.png | AI-generated (Gemini file name) | export the image layer(s) |
| I038 | `pdp-v1.html` | `I1280:10762;1519:25229` | Image-3 | 52 × 52 | product-photo | cde73.png | AI-generated (Gemini file name) | export the image layer(s) |
| I039 | `pdp-v1.html` | `I1280:10762;1519:25230` | Image-4 | 52 × 52 | product-photo | ba181.png | AI-generated (Gemini file name) | export the image layer(s) |
| I040 | `pdp-v1.html` | `I1280:10762;1519:25233` | Image-5 | 52 × 52 | product-photo | 2b984.png | AI-generated (Gemini file name) | export the image layer(s) |
| I041 | `pdp-v1.html` | `I1280:10762;1519:25231` | Image-6 | 52 × 52 | product-photo | 9b8bc.png | web download (generic file name) | export the image layer(s) |
| I042 | `pdp-v1.html` | `1280:10772` | _iPhone mockup status bar | 393 × 40 | decorative-vector | f4903.svg, c1da5.svg, 7e9c1.svg, 16181.svg, b5ccd.svg, 2c135.svg | unattributed | N/A recommended: device / system UI (same decision basis as the 6 status-bar glyphs) |
| I043 | `desktop-pdp-1375-30858.html` | `1375:30863` | 010834LBLU_1 1 | 268.26 × 402.39 | product-photo | 10735.png | product photo (SKU-style file name) | export the image layer(s) |
| I044 | `desktop-pdp-1375-30858.html` | `1375:30865` | 010834LBLU_2 1 | 268.26 × 402.39 | product-photo | a5d09.png | product photo (SKU-style file name) | export the image layer(s) |
| I045 | `desktop-pdp-1375-30858.html` | `1375:30868` | 010834LBLU_3 1 | 268.26 × 402.39 | product-photo | 94028.png | product photo (SKU-style file name) | export the image layer(s) |
| I046 | `desktop-pdp-1375-30858.html` | `1375:30870` | 010834LBLU_4 1 | 268.26 × 402.39 | product-photo | 2aa70.png | product photo (SKU-style file name) | export the image layer(s) |
| I047 | `desktop-pdp-1375-30858.html` | `1375:30961` | 010834LBLA_1 1 | 106 × 159 | product-photo | 6ee12.png | product photo (SKU-style file name) | export the image layer(s) |
| I048 | `desktop-pdp-1375-30858.html` | `1375:30965` | 010834LOLI_1 1 | 106 × 159 | product-photo | 8ced0.png | product photo (SKU-style file name) | export the image layer(s) |
| I049 | `desktop-pdp-1375-30858.html` | `1375:30969` | 010834LGRE_1 1 | 106 × 159 | product-photo | 80d72.png | product photo (SKU-style file name) | export the image layer(s) |
| I050 | `desktop-pdp-1375-30858.html` | `1375:30974` | 010834LBLUGRE_1 1 | 106 × 159 | product-photo | f5d4e.png | product photo (SKU-style file name) | export the image layer(s) |
| I051 | `desktop-pdp-1375-30858.html` | `1375:30978` | 010834LRED2_1 1 | 106 × 159 | product-photo | dccd6.png | product photo (SKU-style file name) | export the image layer(s) |
| I052 | `desktop-pdp-1375-30858.html` | `1375:31231` | 003372XLOFFWHI_1 1 | 257.33 × 386 | product-photo | 1c8d9.png | product photo (SKU-style file name) | export the image layer(s) |
| I053 | `desktop-pdp-1375-30858.html` | `1375:31233` | Vector 1 | 38.7 × 72.61 | ribbon/badge-vector | 598fb.svg | unattributed | export the image layer(s) |
| I054 | `desktop-pdp-1375-30858.html` | `1375:31240` | 01135542DARGRE_1 1 | 257.33 × 386 | product-photo | 414f3.png | product photo (SKU-style file name) | export the image layer(s) |
| I055 | `desktop-pdp-1375-30858.html` | `1375:31242` | Vector 1 | 38.7 × 72.61 | ribbon/badge-vector | 598fb.svg | unattributed | export the image layer(s) |
| I056 | `desktop-pdp-1375-30858.html` | `1375:31249` | 01135542MUS_1 1 | 257.33 × 386 | product-photo | d4119.png | product photo (SKU-style file name) | export the image layer(s) |
| I057 | `desktop-pdp-1375-30858.html` | `1375:31251` | Vector 1 | 38.7 × 72.61 | ribbon/badge-vector | 598fb.svg | unattributed | export the image layer(s) |
| I058 | `desktop-pdp-1375-30858.html` | `1375:31258` | 010834LOLI_1 1 | 257.33 × 386 | product-photo | 8ced0.png | product photo (SKU-style file name) | export the image layer(s) |
| I059 | `desktop-pdp-1375-30858.html` | `1375:31260` | Vector 1 | 38.7 × 72.61 | ribbon/badge-vector | 598fb.svg | unattributed | export the image layer(s) |
| I060 | `desktop-pdp-1375-30858.html` | `1375:31267` | 01135542DARGRE_1 1 | 257.33 × 386 | product-photo | 414f3.png | product photo (SKU-style file name) | export the image layer(s) |
| I061 | `desktop-pdp-1375-30858.html` | `1375:31269` | Vector 1 | 38.7 × 72.61 | ribbon/badge-vector | 598fb.svg | unattributed | export the image layer(s) |
| I062 | `mobile-pdp-1608-7090.html` | `1608:7124` | YL | 360 × 525 | product-photo | 8c432.png | unattributed | export the image layer(s) |
| I063 | `mobile-pdp-1608-7090.html` | `I1608:7152;1539:30179;1539:28349` | Component 102 | 75.97 × 101.29 | product-photo | 9b5e5.png | unattributed | export the image layer(s) |
| I064 | `mobile-pdp-1608-7090.html` | `I1608:7152;1539:30180;1539:28349` | Component 102 | 75.97 × 101.29 | product-photo | 9b5e5.png, 8b1ad.png | unattributed | export the image layer(s) |
| I065 | `mobile-pdp-1608-7090.html` | `I1608:7152;1539:30181;1539:28349` | Component 102 | 75.97 × 101.29 | product-photo | 9b5e5.png, 90500.png | unattributed | export the image layer(s) |
| I066 | `mobile-pdp-1608-7090.html` | `I1608:7152;1539:30182;1539:28349` | Component 102 | 75.97 × 101.29 | product-photo | 1b7eb.png | unattributed | export the image layer(s) |
| I067 | `mobile-pdp-1608-7090.html` | `1608:7160` | Group 1171275299 | 31.34 × 22 | decorative-vector | 50355.svg | unattributed | export the image layer(s) |
| I068 | `mobile-pdp-1608-7090.html` | `1608:7168` | AIR - 1 | 43.56 × 12.95 | decorative-vector | — | n/a | no export: reproduce from the design-context gradient values (read-only) |
| I069 | `mobile-pdp-1608-7090.html` | `1608:7171` | Air - 2 | 20.66 × 4.44 | decorative-vector | — | n/a | no export: reproduce from the design-context gradient values (read-only) |
| I070 | `mobile-pdp-1608-7090.html` | `1608:7174` | Air 3 | 43.12 × 7.81 | decorative-vector | — | n/a | no export: reproduce from the design-context gradient values (read-only) |
| I071 | `mobile-pdp-1608-7090.html` | `1608:7367` | Frame 2121454585 | 187 × 161 | product-photo | 1d5d1.png | unattributed | export the image layer(s) |
| I072 | `mobile-pdp-1608-7090.html` | `1608:7370` | Images | 178 × 237 | composite | 7bc8a.png, 45da3.svg | unattributed | export the image layers individually (never the whole card: that would bake text into an image) |
| I073 | `mobile-pdp-1608-7090.html` | `1608:7380` | Product Image -2 | 190 × 139 | product-photo | 7c131.png | unattributed | export the image layer(s) |
| I074 | `mobile-pdp-1608-7090.html` | `1608:7405` | Frame 2121454395 | 42 × 42 | ribbon/badge-vector | 73565.svg | unattributed | export the image layer(s) |
| I075 | `mobile-pdp-1608-7090.html` | `1608:7433` | Similar Products - Images | 185 × 247 | product-photo | 9b5e5.png | unattributed | export the image layer(s) |
| I076 | `mobile-pdp-1608-7090.html` | `1608:7465` | Similar Products - Images | 185 × 247 | product-photo | 9b5e5.png | unattributed | export the image layer(s) |
| I077 | `mobile-pdp-1608-7090.html` | `1608:7497` | Similar Products - Images | 185 × 247 | product-photo | 9b5e5.png | unattributed | export the image layer(s) |
| I078 | `mobile-pdp-1608-7090.html` | `I1608:7526;1471:36949` | Similar Products - Images | 185 × 247 | product-photo | 9b5e5.png | unattributed | export the image layer(s) |
| I079 | `mobile-pdp-1608-7090.html` | `I1608:7527;1471:36949` | Similar Products - Images | 185 × 247 | product-photo | b1e96.png | unattributed | export the image layer(s) |
| I080 | `mobile-pdp-1608-7090.html` | `I1608:7528;1471:36949` | Similar Products - Images | 185 × 247 | product-photo | 4fbd0.png | unattributed | export the image layer(s) |
| I081 | `mobile-pdp-1608-7090.html` | `I1608:7529;1471:36949` | Similar Products - Images | 185 × 247 | product-photo | 62f2c.png | unattributed | export the image layer(s) |
| I082 | `mobile-pdp-1608-7090.html` | `I1608:7550;1519:25227` | Images | 125 × 158 | product-photo | aa915.png | web download (generic file name) | export the image layer(s) |
| I083 | `mobile-pdp-1608-7090.html` | `I1608:7550;1519:25228` | Image-2 | 125 × 70 | product-photo | 3fba2.png | web download (generic file name) | export the image layer(s) |
| I084 | `mobile-pdp-1608-7090.html` | `I1608:7550;1519:25229` | Image-3 | 52 × 52 | product-photo | 58f8f.png | web download (generic file name) | export the image layer(s) |
| I085 | `mobile-pdp-1608-7090.html` | `I1608:7550;1519:25230` | Image-4 | 52 × 52 | product-photo | 04813.png | web download (generic file name) | export the image layer(s) |
| I086 | `mobile-pdp-1608-7090.html` | `I1608:7550;1519:25233` | Image-5 | 52 × 52 | product-photo | bf527.png | web download (generic file name) | export the image layer(s) |
| I087 | `mobile-pdp-1608-7090.html` | `I1608:7550;1519:25231` | Image-6 | 52 × 52 | product-photo | bcdd6.png | web download (generic file name) | export the image layer(s) |
| I088 | `mobile-pdp-1608-7090.html` | `I1608:7563;1519:25227` | Images | 125 × 158 | product-photo | 402da.png | unattributed | export the image layer(s) |
| I089 | `mobile-pdp-1608-7090.html` | `I1608:7563;1519:25228` | Image-2 | 125 × 70 | product-photo | 03aef.png | AI-generated (Gemini file name) | export the image layer(s) |
| I090 | `mobile-pdp-1608-7090.html` | `I1608:7563;1519:25229` | Image-3 | 52 × 52 | product-photo | cde73.png | AI-generated (Gemini file name) | export the image layer(s) |
| I091 | `mobile-pdp-1608-7090.html` | `I1608:7563;1519:25230` | Image-4 | 52 × 52 | product-photo | ba181.png | AI-generated (Gemini file name) | export the image layer(s) |
| I092 | `mobile-pdp-1608-7090.html` | `I1608:7563;1519:25233` | Image-5 | 52 × 52 | product-photo | 2b984.png | AI-generated (Gemini file name) | export the image layer(s) |
| I093 | `mobile-pdp-1608-7090.html` | `I1608:7563;1519:25231` | Image-6 | 52 × 52 | product-photo | 9b8bc.png | web download (generic file name) | export the image layer(s) |
| I094 | `mobile-pdp-1608-7090.html` | `I1608:7576;1519:25227` | Images | 125 × 158 | product-photo | 9b5e5.png | unattributed | export the image layer(s) |
| I095 | `mobile-pdp-1608-7090.html` | `I1608:7576;1519:25228` | Image-2 | 125 × 70 | product-photo | f0b93.png | AI-generated (Gemini file name) | export the image layer(s) |
| I096 | `mobile-pdp-1608-7090.html` | `I1608:7576;1519:25229` | Image-3 | 52 × 52 | product-photo | 1a18a.png | AI-generated (Gemini file name) | export the image layer(s) |
| I097 | `mobile-pdp-1608-7090.html` | `I1608:7576;1519:25230` | Image-4 | 52 × 52 | product-photo | 33dc1.png | AI-generated (Gemini file name) | export the image layer(s) |
| I098 | `mobile-pdp-1608-7090.html` | `I1608:7576;1519:25233` | Image-5 | 52 × 52 | product-photo | 073bd.png | AI-generated (Gemini file name) | export the image layer(s) |
| I099 | `mobile-pdp-1608-7090.html` | `I1608:7576;1519:25231` | Image-6 | 52 × 52 | product-photo | 59c8b.png | web download (generic file name) | export the image layer(s) |
| I100 | `mobile-pdp-1608-7090.html` | `I1608:7589;1519:25227` | Images | 125 × 158 | product-photo | 402da.png | unattributed | export the image layer(s) |
| I101 | `mobile-pdp-1608-7090.html` | `I1608:7589;1519:25228` | Image-2 | 125 × 70 | product-photo | 03aef.png | AI-generated (Gemini file name) | export the image layer(s) |
| I102 | `mobile-pdp-1608-7090.html` | `I1608:7589;1519:25229` | Image-3 | 52 × 52 | product-photo | cde73.png | AI-generated (Gemini file name) | export the image layer(s) |
| I103 | `mobile-pdp-1608-7090.html` | `I1608:7589;1519:25230` | Image-4 | 52 × 52 | product-photo | ba181.png | AI-generated (Gemini file name) | export the image layer(s) |
| I104 | `mobile-pdp-1608-7090.html` | `I1608:7589;1519:25233` | Image-5 | 52 × 52 | product-photo | 2b984.png | AI-generated (Gemini file name) | export the image layer(s) |
| I105 | `mobile-pdp-1608-7090.html` | `I1608:7589;1519:25231` | Image-6 | 52 × 52 | product-photo | 9b8bc.png | web download (generic file name) | export the image layer(s) |
| I106 | `mobile-pdp-1608-7090.html` | `1608:7092` | Bottom Edge | 360 × 15 | colour-swatch | — | n/a | N/A recommended: device / system UI (same decision basis as the 6 status-bar glyphs) |
| I107 | `mobile-pdp-1608-7090.html` | `1608:7093` | Home Indicator | 139 × 3 | colour-swatch | — | n/a | N/A recommended: device / system UI (same decision basis as the 6 status-bar glyphs) |
| I108 | `mobile-putaway-1627-11756.html` | `1627:11860` | 🥽 Goggles (Swimming, Diving, Gear) | 48 × 48 | other | 0fe59.png | emoji raster | export the image layer(s) |

Crop and position classes for every image (`imgClasses` / `wrapperClasses`, e.g. Figma's `absolute h-[…] left-[…] max-w-none top-[…] w-[…]` image crops inside rounded slots) are recorded verbatim in the JSON. Integration would reproduce them exactly.

## 5. Observations

- **Two-layer variants.** I005/I064 and I006/I065 stack a base image (`9b5e5`) under a visible colour-variant image (`8b1ad` green, `90500` blue). Both layers must be reproduced.
- *Correction 2026-11-20: the cards' layout and text were already reproduced in HTML/CSS; each R11 placeholder was only the card's image slot (`… image`, 185 × 247). The rebuild therefore reduced to filling that slot, plus the review-photo overlay fix in §8.*
- **Composite cards (I011–I017).** The screen reproduction made the whole "Similar Products" card one placeholder. A faithful fill needs the card's **layout and text rebuilt in HTML/CSS**, with only its image layers exported. Exporting the card as one image would bake the text into a picture, which is not acceptable. This is extra implementation work beyond image placement.
- *Correction 2026-11-20: this observation was wrong. Figma's design context of the group `1375:31232` places the ribbon at x **11.21** (the existing placeholder position); the 49.80 in the metadata is the origin of a vector rotated **89.92°**. Position kept, rotation reproduced (§8).*
- **Ribbon placement.** The offer-ribbon placeholders sit at left 11.21 px, while Figma puts them at x 49.80: a pre-existing screen offset, to correct during integration.
- **No-export items.** The 3 "Air" streaks are CSS gradients and can be built from read-only values. "Bottom Edge" / "Home Indicator" and the iPhone status bar are device chrome (N/A recommended, like the status-bar glyphs).

## 6. Export strategy (if approved)

| Item | Method |
|---|---|
| Plain node IDs | `download_assets` (`rawImages` = the original uploaded image at its native resolution and format, not a re-render) |
| Nested instance IDs | The image's asset URL from `get_design_context`. Only the approved method per batch; **no extra comparison copies** |
| Staging | `%TEMP%\\annachy-image-staging\\` (outside the repository), deleted after validation |
| Destination | `showcase/screens/assets/images/<artworkId>.<ext>` (new folder; one file per unique artwork; shared artwork reused) |
| Integration | Each placeholder gets its image with Figma's exact crop classes (absolute size and offset inside a clipped, rounded slot). The two-layer variants are stacked |
| Validation | Byte integrity against the staged export; screen fixtures (each placeholder shows its declared image at Figma's crop); full sequential regression; mutation tests |
| Weight | Native-resolution PNGs can be large. File sizes will be reported before integration; **no re-compression** without approval |

## 7. Recommended batches

**Do not approve the full batch at once:** rights differ sharply between groups.

| Batch | Content | Unique assets | Placeholders | Needs | Effort |
|---|---|---:|---:|---|---|
| **R11-A** | No-export items: 3 "Air" CSS gradients | 0 | 3 | Implementation approval only (read-only values) | ~20 min |
| **R11-B** | Annachy design vectors: offer ribbon `598fb` ×5, badge tile, car illustration (`50355`/`73565`, *if* confirmed own artwork) | 3 | 7 | Export approval; confirm the car illustration is own artwork | ~45 min |
| **R11-C** | Product photos with SKU file names | 12 | 14 | **Confirmation that the photography is Annachy-owned or licensed**, plus export approval | ~1.5 h |
| **R11-D** | AI-generated gallery images (Gemini file names) | 8 | 24 | **Design-team confirmation that these AI images are approved for use**, plus export approval | ~1.5 h |
| **R11-E** | Unattributed product imagery (`9b5e5`, "Product Image", colour variants, the 8 composite cards / overlay) | 13 raster (+2 card vectors to identify) | 37 | Provenance confirmation, plus export approval; **the cards also need layout rebuilding** (~+2 h) | ~2 h + 2 h |
| **R11-F** | High-risk: web downloads "unnamed…" / "Orginal Image" (8 unique, 18 placeholders), screenshot (1), emoji raster (1) | 10 | 20 | **Rights evidence required**, or classify as not required | — |
| N/A | Device chrome: iPhone status bar I042 (5 vectors), Bottom Edge I106, Home Indicator I107. (The R10 star, Home 54 and Gallery Minimalistic vectors inside cards are reused or cancelled; no export) | — | 3 | Owner to confirm N/A | — |
| Identify | 2 unidentified card vectors (`394d3`, `7d14a`) | 2 | 7 | Read-only identification before any decision | ~20 min |

**Check:** 3 + 7 + 14 + 24 + 37 + 20 + 3 = **108 placeholders**.

**Total implementation, if every batch is approved:** about 9–10 h, including the card rebuilds.


---

## 8. Implementation (2026-11-20, approved)

**Approval.** Consolidated owner approval for R11-A to R11-F (all 108 placeholders), **for internal reproduction only**. It does not establish
third-party ownership or licensing, and no asset is marked as owned or licensed by Annachy.

**Export.**

| Item | Value |
|---|---|
| Figma calls | Subagent: `get_design_context` ×62, `download_assets` ×49, `get_metadata` ×10. Main session: `get_design_context` ×4, `download_assets` ×1 (format probe). `excludeScreenshot` on every design-context call; no `create_session`, no write tool, no screenshot tool. **Figma unchanged** |
| Method | Design-context asset links (one per unique artwork). The probe proved them **byte-identical to Figma's original upload** (`download_assets` rawImages), and every delivered raster was checked the same way |
| Staging | `%TEMP%\annachy-image-staging\` (outside the repository); deleted after validation. No asset URL was written to any file |
| Comparison copies (disclosed) | 49 whole-node renders (13 came back empty, 1 × 1) and 307 rawImages (95 equal a delivered asset; 212 are hidden or variant fills). Staging only, for verification; deleted at cleanup |
| Subagent disclosure | 40 of the 62 design-context code files written by the export subagent were derived from a sibling node by text substitution or built from a template instead of saved verbatim. Mitigation: every element's crop values were cross-checked against the independent R11-0 audit records (0 mismatches), the two files that could not be resolved or looked wrong were re-read verbatim (I1608:7529;1471:36949, 1608:7124), and every element with a usable Figma render was compared visually |

**Delivered.** `showcase/screens/assets/images/`: **52 files** (38 PNG, 5 JPEG, 9 SVG; 102.3 MB),
each a byte-identical original, plus `README.md` (source and rights status of every file; **INTERNAL USE ONLY**).
Not delivered (not R11 placeholders): `c6cc8.svg` (R10 star (separate placeholder, already delivered)), `7d14a.svg` (card heart icon (separate icon placeholder, not R11)), `394d3.svg` (card MRP strike (drawn as CSS line-through, not R11)), `7d88c.svg` (Home 54 library icon (already in src/icons)), `45da3.svg` (Gallery Minimalistic (R9 'not required')), `2963b.svg` (gallery heart icon (not R11)), `2e905.svg` (thumbnail MRP strike line: already delivered in R10 (R10 artwork id 'R11', line-2e905-30x0.svg); not an R11 placeholder).

**Integration.** All **108 placeholders** are filled by `tests/tools/r11_integrate_images.py`, which is idempotent, refuses to overwrite, and has a `--refill` mode:
- **103 image placeholders** (112 image layers) are converted from Figma's own wrappers. That covers crop boxes, offsets, clipping, the stacked colour-variant layers (I005, I006, I064, I065), instance scaling and the ribbon's 89.92° rotation.
- **5 placeholders are CSS only**: the three "Air" gradients, Bottom Edge `#0b0d0f`, and the Home Indicator (`#fafcff`, radius 100).
- Every image placeholder carries `data-annachy-image`, `data-img-layers` and `data-img-rights`.

The cards' layout and text were already HTML/CSS. The review-photo overlay was rebuilt (finding 2 below).

**Findings and corrections during implementation.**
1. Offer ribbon: the R11-0 audit claim 'left 11.21 vs Figma x 49.80' was WRONG. Figma places the group at x 11.21 (the existing placeholder position); the vector is rotated 89.92 deg inside it (design context of group 1375:31232). Position kept, rotation reproduced.
2. Review overlay 1608:7372 was positioned against the clipping box instead of image node 1608:7370 in the pre-R11 HTML, and its '+10' group 1608:7373 was missing; both rebuilt in HTML/CSS (owner instruction 6). An empty icon slot 1608:7374 (Gallery Minimalistic, out of scope) was added with the group.
3. Figma emits calc() without spaces around + and - (invalid CSS); the converter normalises them.
4. Resized component instances keep the master's px geometry in Figma's code; Figma itself scales them (scale constraints). Reproduced with a master-size box and scale(): 0.5736 (Green/Blue thumbnails), 1.0129 (Yellow), 0.808 (cards; percentage children, visually neutral). Confirmed by Figma's render: Green/Blue mean difference 70 -> 8-12.
5. Five originals are JPEG although Figma's asset link ends in .png (04813, 58f8f, 8c432, bcdd6, bf527); delivered as .jpg, bytes unchanged.
6. Originals were not compressed or resized (owner instruction 4): the image folder is 102 MB.

**Validation.**
- **One-time check against Figma** (`tests/tools/r11_image_fidelity_once.py`): **156 checks, 0 failures**.
  - 52/52 delivered files are byte-identical to their staged exports.
  - 43/43 rasters equal an original upload.
  - **61 elements** were compared with Figma's own render of the node. The median mean difference is **4.23 / 255**, at alignment offsets of 0–3 px.
  - Excluded from the comparison: pixels under other painted content (text in a different font because Proxima Nova isn't enabled, badges, borders) and the crop's 1 px edge.
  - Reviewed after exceeding the automatic threshold, with enlarged side-by-sides:
    - **I063**: mobile Yellow thumbnail: identical content; resampling of the 1.0129-scaled instance + font of the overlaid badge
    - **I065**: mobile Blue thumbnail: identical content; resampling of the 0.5736-scaled instance
    - **I092**: tile ~4 px inside the mobile carousel edge: only a sliver is visible in both renders; desktop twin I028 matches
  - Not compared: 34 elements whose Figma render was empty or missing; they share artwork and structure with compared siblings. Also 8 vector-only elements, and the 5 CSS-only fills.
  - Per-element results: `r11-0-image-fidelity-results.json`.
- **Screen fixtures**: Sample 1,441 / 0 (was 1,363); PDP 306 / 0 (was 303).
  - Each fixture checks: declared files only, all loaded, layer count, rights status, and the geometry lock `tests/fixtures/r11-image-geometry.json` (112 layers, 0.1 px).
  - The fixtures now also await the icon loader. On these heavier pages, waiting on virtual time alone sometimes ended before two icon fetches had settled; that was intermittent and was seen once in a full run.
- **Full sequential regression**: 33/33 suites PASS.
- **Mutation**: **28/28 caught** (24 existing plus R11-SRC, R11-CROP, R11-SCALE and R11-OVL), each one run alone in the foreground and restored byte-identical.
- **Baseline**: 457 + 7 = 464 tokens, 5 token CSS files, 6,183 `src/` files, all unchanged. No component, token or icon file was changed.

**Unresolved.**

| ID | Item |
|---|---|
| R11-U1 | Rights: all 43 raster images remain unverified (AI-generated 8, SKU-named 12, web download 8, screenshot 1, emoji 1, unattributed 13). Internal use only; data-img-rights on every placeholder; assets/images/README.md |
| R11-U2 | 34 placeholders have no usable Figma render (13 node exports came back 1x1). Verified by identical artwork and structure to compared siblings and by the audit crop values only |
| R11-U3 | Page weight: 102 MB of originals (up to 9 MB per file). Web derivatives need owner approval (re-compression was not approved) |
| R11-U4 | alt text: images use alt="" - Figma holds no product descriptions and none were invented |
| R11-U5 | 8 vectors (ribbon, car, badge, status-bar parts) have no raster comparison in this check: byte-identical originals only |
| R11-U6 | Gallery Minimalistic icon slot 1608:7374 added empty (R9 out of scope) |

## 9. Closure (2026-11-20): web-delivery copies

The originals are unchanged.
- **Copies:** 43 WebP copies are in `showcase/screens/assets/images-web/`. 42 are in use after A/B verification at the real display sizes (190 comparisons at 1× and 2×).
- **Kept original:** `62f2c` failed the strict rule and stays on its original.
- **Linking:** each switched `<img>` carries `data-img-original`, and `data-annachy-image` / `data-img-rights` are unchanged.
- **Rights:** the copies inherit each original's unverified, internal-use-only status.
