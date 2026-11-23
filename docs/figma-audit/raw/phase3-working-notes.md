# Phase 3 — Working Notes (raw observations, pre-report)

Source: `get_metadata` (read-only) on file `rM3ixSG6i3DFfKZFWuxzs4`. `create_session` NOT used (read-only nature not provable). No write tools used.

Raw XML saved for large pages in `raw/metadata/<page-id>.xml`. Small pages returned inline and are summarised here only.

## Inline-returned pages (raw XML not saved; summarised)

- `375:10885` ⓪ START — empty canvas (section header).
- `375:10886` ① Cover — 1 frame `1556:2` "thumbnail" 1611×976 containing image `1556:3`.
- `375:10888`, `1556:23522` — divider pages, empty.
- `367:12000` ① RESEARCH, `1556:5` ② FOUNDATIONS — section-header pages, empty.
- `373:12671` Play Store Reviews — frame `373:12672` 1920×3423 "Play Store Review Analysis" (text research board, no components). Data period Jan–Aug 2026, 2,512 reviews.
- `373:12818` Survey Overview — frame `373:12819` 1920×6820 (survey screenshots + verbatim text, no components).
- `373:12745` Survey Insights — frame `373:12746` 1920×3423 (frame name duplicates "Survey Research Overview" — naming issue).
- `254:13410` User Personas — section `254:13526` > frame `254:13412` 4058×2067. Contains third-party logos (Amazon raster `254:13503`, Flipkart vectors `254:13504`), Unsplash image `254:13413`, icon frames user/map-pin/shopping-bag/smartphone/scale (`254:13477`…`254:13493`).

## Radius `365:11441` (inline)
- Section `1561:56908` > frame `1561:56909` "RADIUS SYSTEM".
- Token names in doc text: `variables.collection2ColourUsage.Radius/{4,8,12,14,16,18,24,26,28,32,34}` [EXTRACTED as text labels — variable binding not yet verified].
- Values 4/8/12/14/16/18/24/26/28/32/34 px; Mobile = Desktop for all (table `1561:57646`).
- Groups: Small / Standard / Large / Extra Large (`1561:57412`).
- Section 04 table (`1561:57523`): Standard Elements 12px, Large Elements 16px, Extra Large Surfaces 24px.
- **Conflict:** Variables table row `1561:57590` maps Radius/8 → "Small / Button / Input"; documentation table `1561:57673` maps Radius/12 → "Buttons, cards" and Radius/8 → "Inputs, small cards".
- **Mislabel:** `_Status` header text `1561:57266` reads "COLOUR SYSTEM" on the Radius page.
- Collection name `collection2ColourUsage` holds radius values — naming oddity.
- Status label: "Defined & Verified", updated "September 2026", "Mobile + Desktop Shared".

## Shadow `1351:18308` (inline)
- Section `1561:57735`. Two frames: "Shadow Scale" `1561:57736`, "Shadow Effects" `1561:57961`.
- Shadow Scale header claims "18 variants" (`1561:57818`); counted specimens: SM-01..05 (5), MD-01..03 (3), LG-01..03 (3), XL-01..03 (3), XXL-01..03 (3) = **17** → count mismatch.
- Shadow Effects claims "15 variants" (`1561:58165`); counted: Small 8 (Peck, Stub, Popup, Raised, Top light, Bottom light, Left light, Right light), Medium 2 (Lozenge, Stub inset), Large 4 (Bubble, Hard inset, Hard lift, Soft inset), XXL 1 (Dialog) = 15 ✓. No "Extra Large" group in Effects.
- Specimen nodes (shadow carriers): SM `1561:57835,57842,57849,57856,57863`; MD `57945,57952,57959`; LG `57873,57880,57887`; XL `57897,57904,57911`; XXL `57921,57928,57935`. Effects carriers `1561:58182,58189,58196,58203,58210,58217,58224,58231,58241,58248,58255,58262,58272,58282,58289`.
- Effect values not yet extracted (need `get_design_context`/`get_variable_defs`).

## Blur `1351:18312` (inline)
- Section `1563:58295` > frame `1563:58296` "Blur & Glass Effects".
- **Mislabel:** `_Status` text `1563:58298` reads "Shadow Scale" on the Blur page.
- Header claims "2 variants" (`1563:58680`); page shows Blur: SM-1, SM-2, MD-1, MD-2, "XS" (under Large); Glass: SM, MD, "XS" (under Large).
- **Mislabel:** Large group specimens labelled "XS" (`1563:58729`, `1563:58765`).
- Blur carriers: `1563:58696,58704,58715,58723,58733`; Glass carriers `1563:58748,58759,58769`. Unsplash background images used.

## "EMPTY PAGE" `479:4`
- NOT empty: frame `1590:18891` "Core Button Components" 2722×7537, 432 `symbol` nodes. Possibly a full button component set outside the Components section. Status (current vs. stale) TBD.

## Brainstorming `0:1` (Research section)
- 28,082 nodes; 10,547 symbols; 2,365 instances.
- Section `5:15097` "Icons" 36936×11838 contains **10,524 components** — very likely the master icon library, located on a Research page.
- Section `5:12734` "Icons" (23 comps), `5:10905` "Typrography" (typo in name), `155:10496` "Typography Usability Test", `51:11109` Others, `51:11110` Prompt, text node `41:10537` (survey summary).

## Input `375:10892` (inline)
- Section `1567:1642` "Input Feild Component Source" (typo "Feild") > frame `1567:1643` > `1567:2351` "Inputs".
- Variant frame **"Input Field / Outline"** `1066:37962`: props `State × Size × Radius`. States: Default, Focused, Filled, Error, Disabled, Success (6). Sizes 46/48/50/54/56. Radius 4/6/8/10/12. = **150 symbols**. **No Hover state** in Outline.
- Variant frame **"Input Field / Filled"** `1066:40663`: same props, 7 states (adds Hover) = **175 symbols**.
- Symbol size: width ~336–337 (alternating 336/337 — sub-pixel inconsistency), heights 110/112/114/118/120 (includes label/helper text; field height = Size prop).
- **Radius 6 and 10 are not in the Radius token scale** (scale: 4,8,12,14,16,…).
- **Column header mismatch** Outline (`1567:2352`): labels "Default, Focused, Active, Error, Success, Disable" vs actual column order Default, Focused, Filled, Error, Disabled, Success. "Active" ≠ "Filled".
- **Column header mismatch** Filled (`1567:2359`): labels "…Error, Success, Disable" vs actual …Error, Disabled, Success.
- Note: these are metadata `symbol` nodes inside plain frames — whether they form a true component set (variant group) must be verified in Phase 4.
- Stray frame `1763:22998` outside the section, containing 3 instances of "Input Field / Outline" (`1763:26195`, `1765:27766`, `1766:36089`) — likely a scratch/test area.

## Divider/header pages (inline): `1556:74` "---", `375:10890` ③ COMPONENTS — empty.

## Tooltip `1351:18311` (inline)
- Section `1568:38568` "CoreTooltip Components" (missing space) > section `1568:40001` "Tooltip" > frame `1448:16825` "tooltip".
- **80 symbols**: `Device{Mobile,Desktop} × Mode{dark,light} × Arrow{left, left center, right, right center, top, top left, top right, bottom, bottom left, bottom right} × Format{Text only, Heading and description}` = 2×2×10×2 = 80 ✓ complete matrix.
- Sizes: Mobile Text-only 182×38; Desktop Text-only 157×38; Mobile Heading+desc 260×62; Desktop Heading+desc 240×59.
- Arrow naming asymmetric: "left center"/"right center" exist but no "top center"/"bottom center" (plain "top"/"bottom" serve as centre).
- `_Status` label "tooltip" lowercase vs other pages' title case.
- Light/dark exists as a **variant property** (Mode) here — not via variable modes. To verify against colour variables.

## Navigation · Mobile `1351:18314` and Navigation · Desktop `1556:7200`
- **Both pages are EMPTY** (no nodes). Page names carry "○" (not started) status marker. [EXTRACTED]
- → Navigation cannot be specified from this file. [MISSING]

## Divider/header pages (inline): `1556:77`, `1556:76` "---"; `1499:21976` ④ PATTERNS & SCREENS; `375:10898` ⑨ ARCHIVE — all empty.

## Archive › Radio `1489:5449` (inline)
- Section `1493:2` > frame `1493:3` "Radio Button": **108 symbols** = State{Selected, Unselected, Disabled Unselected, Disabled Selected, Focus, Pressed} × Size{Small, Medium, Large} × Radio Position{Left, Right} × Alignment{Top, Center, Bottom} = 6×3×2×3 ✓.
- Symbol widths: Small 216, Medium 220, Large 224; height 41 for all.
- **No Hover state** in Radio.
- Doc frame `1500:22374` "Pilot documentation / Radio Button": control sizes "Small 20 × 20", "Medium · 24 × 24", "Large · 28 × 28" (inconsistent label punctuation). Multiline alignment examples `1500:22495/22497/22499`.
- Lives on ARCHIVE page but has "✓" marker — status vs. Components page `375:10893` to be reconciled.
