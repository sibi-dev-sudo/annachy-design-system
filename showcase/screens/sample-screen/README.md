# Sample Screen — static reproductions

Figma file `rM3ixSG6i3DFfKZFWuxzs4`, page **› ① Sample Screen** (`1375:30857`), section `1608:11615`.
Vanilla HTML/CSS. Every page links `../../../src/annachy.css` and `./sample-screen.css` (class prefix `scr-`). Nothing under `src/` was changed.
Navigation links to these pages are not added (the lead engineer integrates them).

## Frames

| Figma frame | Size | File | Status |
|---|---|---|---|
| `1375:30858` Desktop | 1440 × 3533 | `desktop-pdp-1375-30858.html` | **complete**, with these exceptions: line `1375:31162` (x200 y1612.5, parent unknown) is omitted; `1375:31275` (inside `1375:31222`, at y414, past that frame's 382px height) is omitted; the frame fill is not exposed by the MCP responses, so no frame background is set |
| `1608:9891` Desktop | 1440 × 1073 | `desktop-1608-9891.html` | **partial**. Only the frame box is reproduced. `get_metadata` and `get_design_context` return the frame with no children ("too large", sparse metadata), and the saved page metadata lists it with no children. Probing ids `1608:9890`, `1608:9892` and `1608:9893` returned "not found", so no child id could be obtained with the authorised read-only tools |
| `1608:7090` Mobile | 360 × 4683 | `mobile-pdp-1608-7090.html` | **complete**. The frame fill is not exposed, so no frame background is set. Home Indicator Bar `1608:7091` fills were not fetched and are placeholders |
| `1627:11756` Mobile | 360 × 800 | `mobile-putaway-1627-11756.html` | **complete**. Hidden layers `1627:11781`, `1627:11794`, `1627:11813` and `1627:11891` are omitted because they are not in the design context |
| `1629:11987` Job - Listing page | 360 × 800 | `job-listing-page-1629-11987.html` | **complete**. Content runs past the 800px frame (the last card ends at y835) and is clipped, as in Figma |

**Frame size.** Each root `#frame` has the exact Figma width and height. Top-level sections are absolutely positioned at their metadata x, y, width and height, so reflow from the fallback font cannot move them.

**Fonts.** All text uses `var(--annachy-base-font-family-render)` (Proxima Nova → system-ui → sans-serif). Inter (`1627:*`, `1629:*`, `1375:31224/31226`) and SF Pro (iOS status bars) are not loaded. Text widths therefore differ from Figma. Text-width-dependent x positions (breadcrumb width, header search x) are not asserted. Text boxes `1375:31087` and `1375:31120` are fixed at 144px in Figma, and the fallback font wraps them, so they get `white-space: nowrap` to keep the Figma single line and height.

## Verification

`python -I tests/tools/browser_check.py screens-sample-check.html` (run from the project root): **STATUS: PASS — checks: 1363 · failures: 0** (5 frames, tolerance 1px).
The fixture `tests/fixtures/screens-sample-check.html` loads every page in a same-origin iframe and checks the following:
- root frame width and height;
- x, y, width and height of 81 major sections and child blocks, measured against the root, using values from the metadata (saved XML plus the `get_metadata` reads below). A `null` axis is skipped only where the value depends on text width;
- the stylesheet links and the render font stack;
- library component reuse (`.annachy-button`, `.annachy-button-gradient`, `.annachy-input`);
- the placeholder contract: `data-figma-node` is a Figma id, `data-asset` is one of image, icon or logo, `title` is present, the element is empty;
- the page has no `img`, `svg` or media elements, no Figma MCP asset URL, no external `http(s)` resource and no inline `url()`;
- every `data-figma-node` value is a real Figma id format.

No height tolerance beyond 1px was needed.

## Components reused (library classes, markup per each README)

| Component | Where (node id) | Classes / overrides |
|---|---|---|
| Button (All Buttons `887:2492`) | `1608:7266`, `1608:7346` "See Less" | `annachy-button--secondary --size-32` |
| | `1608:7278` "Specifications", `1608:7279` "Other Details" (disabled) | `--secondary-grey --size-36`. Figma `1608:7278` has fill `#fafcff`, while the library Secondary Grey Default is transparent |
| | `1608:7428` (icon-only, both icon slots visible: 14+20+6+20+14 = 74 + 2 border = 76 = Figma width) | `--secondary --size-38`, `aria-label` |
| | Similar-product "Add To Cart" `1608:7461`, `1608:7493`, `1608:7525` | `--secondary --size-36`, width 100% |
| | `1608:7388` "See More" | `--secondary --size-46`, width 100% |
| | `1608:7592` "Buy Now" | `--secondary --size-48`, width 134 |
| | `1375:31044` "Check" | `--link --size-36`. Figma padding is 10/8 and the library size-36 padding is 12/10. Not asserted |
| Button gradient (`1153:3370`) | `1608:7593` "Add To Cart" | `annachy-button-gradient--size-48` |
| | `1375:30934` "50% Off" | `--size-32` with `--_gb-radius: var(--annachy-radius-4)` (instance radius 4) |
| | `1375:31000` "ADD TO CART" | `--size-56` with `--_gb-radius: var(--annachy-radius-8)` (instance radius 8). The instance gradient (`#3a6ff7 → #1746a2`, to top) differs from the library default (`#3a79f7 → #1746a2`), and the library value is kept |
| Input Outline (`1066:37962`) | `1608:7155` Delivery Details | `annachy-input--outline --size-46 --radius-4`. `__top` is set to `block-size:auto; gap:7px` (instance top section `I1608:7155;1066:38864`), and the root is clipped to 71px as in Figma |
| Input Filled (`1066:40663`) | `1375:31346` header search | `--filled --size-48 --radius-4`, `__top` `block-size:48px` (no label), `--_input-border: var(--annachy-color-border-secondary)` (`#dcdfe5` in Figma) |
| | `1375:31031` Delivery Options | `--filled --size-48 --radius-4` with `--_input-height:63px` (instance field 63), `__top` `block-size:auto; gap:8px`, `--_input-border: var(--annachy-color-border-primary)` (`#bfc4cf`) |

Checkbox, Radio, Toggle, Dropdown and Tooltip are not used on these frames. Not reused:
- The size buttons `1375:30985`–`30989` (62 × 62), WISHLIST `1375:31001` (62 tall) and tertiary "See More" `1375:31155` (54 tall, 30px icon) do not match a library size, so they are styled with `scr-` classes and tokens.
- The dark tab `1608:7277` (`#0b0c0f` fill) matches no library Type, so it is also styled with `scr-` classes and tokens.

**Hidden icon slots.** Several instances carry `Home/Home 54` (`1777:12415`) icon slots in the design context. In these instances the slots cannot be visible, because the Figma instance widths only fit the label:
- size buttons: 62 = 23 + label + 23;
- "50% Off": 106;
- "Buy Now": 134;
- "See Less" and others.

These slots are omitted. The only exception is `1608:7428`, which has no label, and its icon slots are kept as placeholders.

**Inside strokes.** Figma inside strokes are not part of the auto-layout. Where the metadata shows children at the padding offset (`1627:11841`, `1629:12102`: children at x/y 12 with p12 and a 1px stroke; `1375:30959`: 1.5px stroke), the CSS padding is reduced by the border width so the boxes match. `1629:12556` includes its stroke (children at 11/9 with px10/py8), so it keeps its full padding.

## Figma calls made (41 total, all read-only)

| Tool | Count | Node ids |
|---|---|---|
| `get_design_context` (always `excludeScreenshot: true`) | 27 | `1629:11987`, `1375:30858` (sparse: too large), `1608:9891` (sparse: too large), `1627:11756`, `1608:7112`, `1608:7124`, `1608:7125`, `1608:7151`, `1608:7154`, `1608:7183`, `1608:7590`, `1608:7094`, `1608:7241`, `1608:7391`, `1608:7267`, `1608:7425` (output saved to file by the client), `1608:7530`, `1375:31289`, `1375:30893`, `1375:31003`, `1375:31077`, `1375:31164`, `1375:30877`, `1375:30860`, `1375:31223`, `1375:31393`, `1375:31230` |
| `get_metadata` | 14 | `1375:30858`, `1608:9891` (both returned only the frame). Then sequential id probes to locate children: `1375:30859` (main), `1375:31160`, `1375:31162`, `1375:31163` (ratings + related), `1375:31170`, `1375:31282` (arrows), `1375:31289` (header), `1375:31393` (line), `1375:31394` (not found), `1608:9892` / `1608:9893` / `1608:9890` (not found) |
| `get_variable_defs` | 0 | — |

No other Figma tool was called (no `create_session`, `get_screenshot`, `download_assets` or `use_figma`). No asset URL was fetched or referenced. Method note: because the two Desktop frames return no children, the children of `1375:30858` were found by reading node ids that follow the frame id in sequence. Their parentage was inferred from their positions inside the 1440 × 3533 frame. This was confirmed for `1375:30859`, `1375:31163`, `1375:31282`, `1375:31289` and `1375:31393`, but it is an inference, not a tree read.

## Values that could not be verified

- `1608:9891`: all content (see above).
- Frame fills of `1375:30858` and `1608:7090` (not exposed by the MCP responses).
- Stroke colours of every vector line (`Line *` nodes). They exist only inside SVG assets, so they are dashed `data-stroke` placeholders at the Figma length.
- Fills of `1608:7092` / `1608:7093` (Home Indicator Bar, not fetched).
- The Home Indicator `1608:7093` is at x250 with width 139, so it overflows the 360px frame in the metadata. It is reproduced as-is.
- The parent of `1375:31162`.

## Token mapping

These Figma values are used through tokens:
- colours: `#004feb`, `#0b0c0f`, `#555d6d`, `#707a8f`, `#fafcff`, `#14a047`, `#f6f7f9`, `#dcdfe5`, `#bfc4cf`, `#edeff2`, `#121417`, `#181b21`, `#202d47`, `#030a14`, `#003fbc`, `#002f8d`, `#98a0ae`, `#1f242e`, `#f5f9ff`, `#f0f5fe`, `#ebf2ff`;
- radii: 4, 8 and 12;
- the semantic tokens in the `.scr-c-*` classes;
- font weights 400, 500, 600 and 700.

Typography sizes and line heights are literal Figma values: the R1 `--annachy-type-*` tokens are role tokens with desktop and mobile variants. Each text element carries its own `data-figma-node`.

## Generated inventories

Generated from the HTML and CSS sources: every `.scr-asset` placeholder and every literal value with its node id.

### Placeholder assets

| File | Node id | Figma layer (title) | Size (w × h px) | Kind |
|---|---|---|---|---|
| desktop-pdp-1375-30858.html | `1375:31293` | Logotype (Group) | 156.74 × 38.722 | logo |
| desktop-pdp-1375-30858.html | `1375:31338` | Frame (location) | 30 × 30 | icon |
| desktop-pdp-1375-30858.html | `1375:31344` | Frame (chevron) | 20 × 20 | icon |
| desktop-pdp-1375-30858.html | `1779:37533` | User/User Curved | 24 × 24 | icon |
| desktop-pdp-1375-30858.html | `1779:38814` | Arrow/Chevron Up | 24 × 24 | icon |
| desktop-pdp-1375-30858.html | `1779:39439` | Arrow/Chevron Down | 24 × 24 | icon |
| desktop-pdp-1375-30858.html | `1375:31350` | Frame (profile) | 30 × 30 | icon |
| desktop-pdp-1375-30858.html | `1375:31355` | Frame (chevron) | 20 × 20 | icon |
| desktop-pdp-1375-30858.html | `1375:31358` | Frame (cart) | 30 × 30 | icon |
| desktop-pdp-1375-30858.html | `1375:31369` | Frame (category) | 24 × 24 | icon |
| desktop-pdp-1375-30858.html | `I1375:31375;17:1154` | Frame (chevron) | 20 × 20 | icon |
| desktop-pdp-1375-30858.html | `I1375:31376;17:1154` | Frame (chevron) | 20 × 20 | icon |
| desktop-pdp-1375-30858.html | `I1375:31377;17:1154` | Frame (chevron) | 20 × 20 | icon |
| desktop-pdp-1375-30858.html | `I1375:31378;17:1154` | Frame (chevron) | 20 × 20 | icon |
| desktop-pdp-1375-30858.html | `1375:31381` | Frame (deals) | 30 × 30 | icon |
| desktop-pdp-1375-30858.html | `1375:31388` | Frame (offers) | 30 × 30 | icon |
| desktop-pdp-1375-30858.html | `1375:30863` | 010834LBLU_1 1 | 268.259 × 402.389 | image |
| desktop-pdp-1375-30858.html | `1375:30865` | 010834LBLU_2 1 | 268.259 × 402.389 | image |
| desktop-pdp-1375-30858.html | `1375:30868` | 010834LBLU_3 1 | 268.259 × 402.389 | image |
| desktop-pdp-1375-30858.html | `1375:30870` | 010834LBLU_4 1 | 268.259 × 402.389 | image |
| desktop-pdp-1375-30858.html | `1375:30871` | View More | 47.651 × 47.651 | icon |
| desktop-pdp-1375-30858.html | `1375:30900` | Frame (share) | 30 × 30 | icon |
| desktop-pdp-1375-30858.html | `1375:30902` | Frame (wishlist) | 30 × 30 | icon |
| desktop-pdp-1375-30858.html | `1375:30912` | Frame (star) | 12 × 12 | icon |
| desktop-pdp-1375-30858.html | `1375:30914` | Frame (star) | 12 × 12 | icon |
| desktop-pdp-1375-30858.html | `1375:30916` | Frame (star) | 12 × 12 | icon |
| desktop-pdp-1375-30858.html | `1375:30918` | Frame (star) | 12 × 12 | icon |
| desktop-pdp-1375-30858.html | `1375:30920` | Frame (info) | 20 × 20 | icon |
| desktop-pdp-1375-30858.html | `1375:30923` | Line 23 (stroke colour only in SVG asset) | 610 × 0 | image (stroke) |
| desktop-pdp-1375-30858.html | `1375:30933` | Line 16 (vertical stroke, colour only in SVG asset) | 0 × 27 | image |
| desktop-pdp-1375-30858.html | `1375:30937` | Line 16 (vertical stroke, colour only in SVG asset) | 0 × 17 | image |
| desktop-pdp-1375-30858.html | `1375:30940` | Frame (info) | 15 × 15 | icon |
| desktop-pdp-1375-30858.html | `1375:30944` | Line 15 (stroke colour only in SVG asset) | 610 × 0 | image (stroke) |
| desktop-pdp-1375-30858.html | `1375:30952` | Frame (previous) | 38 × 38 | icon |
| desktop-pdp-1375-30858.html | `1375:30955` | Frame (next, mirrored) | 38 × 38 | icon |
| desktop-pdp-1375-30858.html | `1375:30961` | 010834LBLA_1 1 | 106 × 159 | image |
| desktop-pdp-1375-30858.html | `1375:30965` | 010834LOLI_1 1 | 106 × 159 | image |
| desktop-pdp-1375-30858.html | `1375:30969` | 010834LGRE_1 1 | 106 × 159 | image |
| desktop-pdp-1375-30858.html | `1375:30974` | 010834LBLUGRE_1 1 | 106 × 159 | image |
| desktop-pdp-1375-30858.html | `1375:30978` | 010834LRED2_1 1 | 106 × 159 | image |
| desktop-pdp-1375-30858.html | `1375:31002` | Line 21 (stroke colour only in SVG asset) | 610 × 0 | image (stroke) |
| desktop-pdp-1375-30858.html | `1375:31010` | badge-percent | 25 × 25 | icon |
| desktop-pdp-1375-30858.html | `1375:31020` | badge-percent | 25 × 25 | icon |
| desktop-pdp-1375-30858.html | `1375:31037` | Outline / Map & Location / Map Point | 24 × 24 | icon |
| desktop-pdp-1375-30858.html | `1375:31051` | Frame (perk icon) | 30 × 30 | icon |
| desktop-pdp-1375-30858.html | `1375:31059` | Frame (perk icon) | 30 × 30 | icon |
| desktop-pdp-1375-30858.html | `1375:31069` | Frame (perk icon) | 30 × 30 | icon |
| desktop-pdp-1375-30858.html | `1375:31076` | Line 24 (stroke colour only in SVG asset) | 610 × 0 | image (stroke) |
| desktop-pdp-1375-30858.html | `1375:31082` | Frame (details) | 30 × 30 | icon |
| desktop-pdp-1375-30858.html | `1375:31088` | Frame (collapse, mirrored) | 30 × 30 | icon |
| desktop-pdp-1375-30858.html | `1375:31116` | Frame (specifications) | 30 × 30 | icon |
| desktop-pdp-1375-30858.html | `1375:31127` | Line (stroke colour only in SVG asset) | 270 × 0 | image (stroke) |
| desktop-pdp-1375-30858.html | `1375:31132` | Line (stroke colour only in SVG asset) | 270 × 0 | image (stroke) |
| desktop-pdp-1375-30858.html | `1375:31138` | Line (stroke colour only in SVG asset) | 270 × 0 | image (stroke) |
| desktop-pdp-1375-30858.html | `1375:31143` | Line (stroke colour only in SVG asset) | 270 × 0 | image (stroke) |
| desktop-pdp-1375-30858.html | `1375:31149` | Line (stroke colour only in SVG asset) | 270 × 0 | image (stroke) |
| desktop-pdp-1375-30858.html | `1375:31154` | Line (stroke colour only in SVG asset) | 270 × 0 | image (stroke) |
| desktop-pdp-1375-30858.html | `1375:31159` | Frame (chevron) | 30 × 30 | icon |
| desktop-pdp-1375-30858.html | `1375:31393` | Line 18 (stroke colour only in SVG asset) | 1200 × 0 | image (stroke) |
| desktop-pdp-1375-30858.html | `1375:31227` | Frame (arrow, rotated -90°) | 30 × 30 | icon |
| desktop-pdp-1375-30858.html | `1375:31231` | 003372XLOFFWHI_1 1 | 257.33 × 385.995 | image |
| desktop-pdp-1375-30858.html | `1375:31233` | Vector 1 (offer ribbon) | 38.699 × 72.611 | image |
| desktop-pdp-1375-30858.html | `1375:31238` | logo 2 | 28.426 × 8.483 | logo |
| desktop-pdp-1375-30858.html | `1375:31240` | 01135542DARGRE_1 1 | 257.333 × 386 | image |
| desktop-pdp-1375-30858.html | `1375:31242` | Vector 1 (offer ribbon) | 38.699 × 72.611 | image |
| desktop-pdp-1375-30858.html | `1375:31247` | logo 2 | 28.426 × 8.483 | logo |
| desktop-pdp-1375-30858.html | `1375:31249` | 01135542MUS_1 1 | 257.33 × 385.995 | image |
| desktop-pdp-1375-30858.html | `1375:31251` | Vector 1 (offer ribbon) | 38.699 × 72.611 | image |
| desktop-pdp-1375-30858.html | `1375:31256` | logo 2 | 28.426 × 8.483 | logo |
| desktop-pdp-1375-30858.html | `1375:31258` | 010834LOLI_1 1 | 257.33 × 385.995 | image |
| desktop-pdp-1375-30858.html | `1375:31260` | Vector 1 (offer ribbon) | 38.699 × 72.611 | image |
| desktop-pdp-1375-30858.html | `1375:31265` | logo 2 | 28.426 × 8.483 | logo |
| desktop-pdp-1375-30858.html | `1375:31267` | 01135542DARGRE_1 1 | 257.333 × 386 | image |
| desktop-pdp-1375-30858.html | `1375:31269` | Vector 1 (offer ribbon) | 38.699 × 72.611 | image |
| desktop-pdp-1375-30858.html | `1375:31274` | logo 2 | 28.426 × 8.483 | logo |
| desktop-pdp-1375-30858.html | `1375:31283` | Group 1000001479 (previous arrow) | 66.667 × 66.667 | icon |
| desktop-pdp-1375-30858.html | `1375:31286` | Group 1000001482 (next arrow) | 66.667 × 66.667 | icon |
| mobile-pdp-1608-7090.html | `1608:7096` | Phone Camara | 18 × 18 | icon |
| mobile-pdp-1608-7090.html | `1608:7101` | Wifi | 17 × 18 | icon |
| mobile-pdp-1608-7090.html | `1608:7106` | Signal | 17 × 18 | icon |
| mobile-pdp-1608-7090.html | `1608:7109` | Battery | 8 × 15.882 | icon |
| mobile-pdp-1608-7090.html | `1608:7114` | Line Duotone / Arrows / Alt Arrow Left | 28 × 28 | icon |
| mobile-pdp-1608-7090.html | `1608:7118` | Linear / Search / Magnifer | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `1608:7122` | Outline / Shopping, Ecommerce / Cart Large 2 | 28 × 28 | icon |
| mobile-pdp-1608-7090.html | `1608:7124` | YL (product image I1608:7124;1486:38899) | 360 × 525 | image |
| mobile-pdp-1608-7090.html | `1608:7129` | Line Duotone / Arrows / Alt Arrow Left (rotated) | 20 × 20 | icon |
| mobile-pdp-1608-7090.html | `1608:7143` | loyalty 1 [Vectorized] | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `1608:7149` | Line Duotone / Arrows / Alt Arrow Left (rotated) | 20 × 20 | icon |
| mobile-pdp-1608-7090.html | `I1608:7152;1539:30179;1539:28349` | Component 102 (colour variant image) | 75.969 × 101.292 | image |
| mobile-pdp-1608-7090.html | `I1608:7152;1539:30179;1539:28950` | Line 122 (stroke colour only in SVG asset) | 30 × 0 | image (stroke) |
| mobile-pdp-1608-7090.html | `I1608:7152;1539:30180;1539:28349` | Component 102 (colour variant image) | 75.969 × 101.292 | image |
| mobile-pdp-1608-7090.html | `I1608:7152;1539:30180;1539:28950` | Line 122 (stroke colour only in SVG asset) | 30 × 0 | image (stroke) |
| mobile-pdp-1608-7090.html | `I1608:7152;1539:30181;1539:28349` | Component 102 (colour variant image) | 75.969 × 101.292 | image |
| mobile-pdp-1608-7090.html | `I1608:7152;1539:30181;1539:28950` | Line 122 (stroke colour only in SVG asset) | 30 × 0 | image (stroke) |
| mobile-pdp-1608-7090.html | `I1608:7152;1539:30182;1539:28349` | Component 102 (colour variant image) | 75.969 × 101.292 | image |
| mobile-pdp-1608-7090.html | `I1608:7152;1539:30182;1539:28950` | Line 122 (stroke colour only in SVG asset) | 30 × 0 | image (stroke) |
| mobile-pdp-1608-7090.html | `I1608:7153;1546:27139` | Line Duotone / Arrows / Alt Arrow Left (rotated) | 18 × 18 | icon |
| mobile-pdp-1608-7090.html | `I1608:7153;1546:27123;1546:27436;1010:22241` | Line 1 (diagonal 78.518, rotated 43.45°) (stroke colour only in SVG asset) | 78.518 × 0 | image (stroke) |
| mobile-pdp-1608-7090.html | `I1608:7155;1066:38868` | User/User Curved (1779:37533) | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `1779:38814` | Arrow/Chevron Up | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `1779:39439` | Arrow/Chevron Down | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `1780:40128` | Alerts/Error circle | 16 × 16 | icon |
| mobile-pdp-1608-7090.html | `1608:7160` | Car (Group 1171275299) | 31.344 × 22 | image |
| mobile-pdp-1608-7090.html | `1608:7168` | AIR - 1 (decorative streaks) | 43.557 × 12.955 | image |
| mobile-pdp-1608-7090.html | `1608:7171` | Air - 2 (decorative streaks) | 20.657 × 4.441 | image |
| mobile-pdp-1608-7090.html | `1608:7174` | Air 3 (decorative streaks) | 43.124 × 7.806 | image |
| mobile-pdp-1608-7090.html | `1608:7182` | Line 122 (stroke colour only in SVG asset) | 54 × 0 | image (stroke) |
| mobile-pdp-1608-7090.html | `1608:7186` | Group (perk icon) | 31.2 × 23.4 | icon |
| mobile-pdp-1608-7090.html | `1608:7196` | Line Duotone / Arrows / Alt Arrow Left (rotated) | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `1608:7200` | Group (perk icon) | 30.79 × 23.93 | icon |
| mobile-pdp-1608-7090.html | `1608:7215` | Line Duotone / Arrows / Alt Arrow Left (rotated) | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `1608:7219` | Group (perk icon) | 30.79 × 23.93 | icon |
| mobile-pdp-1608-7090.html | `1608:7235` | Line Duotone / Arrows / Alt Arrow Left (rotated) | 18 × 18 | icon |
| mobile-pdp-1608-7090.html | `1608:7237` | Line Duotone / Arrows / Alt Arrow Left (rotated) | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `I1608:7248;1548:31174` | Icons | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `I1608:7249;1548:31174` | Icons | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `I1608:7251;1548:31174` | Icons | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `I1608:7252;1548:31174` | Icons | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `I1608:7254;1548:31174` | Icons | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `I1608:7255;1548:31174` | Icons | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `I1608:7258;1548:31174` | Icons | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `I1608:7259;1548:31174` | Icons | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `I1608:7261;1548:31174` | Icons | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `I1608:7262;1548:31174` | Icons | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `I1608:7264;1548:31174` | Icons | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `I1608:7265;1548:31174` | Icons | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `1608:7272` | Line 137 (stroke colour only in SVG asset) | 328 × 0 | image (stroke) |
| mobile-pdp-1608-7090.html | `I1608:7274;1548:33548` | Line Duotone / Arrows / Alt Arrow Left (rotated 90°) | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `I1608:7274;1548:33550` | Line (stroke colour only in SVG asset) | 362 × 0 | image (stroke) |
| mobile-pdp-1608-7090.html | `I1608:7348;1548:33548` | Line Duotone / Arrows / Alt Arrow Left (rotated 90°) | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `I1608:7348;1548:33550` | Line (stroke colour only in SVG asset) | 362 × 0 | image (stroke) |
| mobile-pdp-1608-7090.html | `1608:7360` | Star | 18 × 18 | icon |
| mobile-pdp-1608-7090.html | `1608:7363` | Line (vertical 18, stroke colour only in SVG asset) | 0 × 18 | image |
| mobile-pdp-1608-7090.html | `1608:7367` | Review photo (Frame 2121454585) | 187 × 161 | image |
| mobile-pdp-1608-7090.html | `1608:7370` | Images | 178 × 237 | image |
| mobile-pdp-1608-7090.html | `1608:7380` | Product Image -2 | 190 × 139 | image |
| mobile-pdp-1608-7090.html | `1608:7383` | Outline / Video, Audio, Sound / Play Circle | 18 × 18 | icon |
| mobile-pdp-1608-7090.html | `I1608:7387;1321:18884` | Star | 17.811 × 17.811 | icon |
| mobile-pdp-1608-7090.html | `I1608:7387;1363:26813;1363:25114` | Outline / Like / Like | 18 × 18 | icon |
| mobile-pdp-1608-7090.html | `1608:7389` | Line 137 (stroke colour only in SVG asset) | 328 × 0 | image (stroke) |
| mobile-pdp-1608-7090.html | `1608:7390` | Line 143 (stroke colour only in SVG asset) | 362 × 0 | image (stroke) |
| mobile-pdp-1608-7090.html | `1608:7395` | Outline / Users / Users Group Two Rounded | 23.1 × 22.8 | icon |
| mobile-pdp-1608-7090.html | `1608:7400` | Linear / Security / Shield Check | 23.1 × 22.8 | icon |
| mobile-pdp-1608-7090.html | `1608:7405` | Frame 2121454395 (badge tile) | 42 × 42 | image |
| mobile-pdp-1608-7090.html | `1608:7412` | Linear / Shopping, Ecommerce / Shop | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `1608:7422` | Line Duotone / Arrows / Alt Arrow Left (rotated) | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `1777:12415` | Home/Home 54 (icon slot) | 20 × 20 | icon |
| mobile-pdp-1608-7090.html | `1777:12415` | Home/Home 54 (icon slot) | 20 × 20 | icon |
| mobile-pdp-1608-7090.html | `1608:7433` | Similar Products - Images | 185 × 247 | image |
| mobile-pdp-1608-7090.html | `1608:7439` | Star | 9.535 × 9.535 | icon |
| mobile-pdp-1608-7090.html | `I1608:7443;1548:40450` | Linear / Like / Heart | 19.2 × 19.2 | icon |
| mobile-pdp-1608-7090.html | `1608:7465` | Similar Products - Images | 185 × 247 | image |
| mobile-pdp-1608-7090.html | `1608:7471` | Star | 9.535 × 9.535 | icon |
| mobile-pdp-1608-7090.html | `I1608:7475;1548:40450` | Linear / Like / Heart | 19.2 × 19.2 | icon |
| mobile-pdp-1608-7090.html | `1608:7497` | Similar Products - Images | 185 × 247 | image |
| mobile-pdp-1608-7090.html | `1608:7503` | Star | 9.535 × 9.535 | icon |
| mobile-pdp-1608-7090.html | `I1608:7507;1548:40450` | Linear / Like / Heart | 19.2 × 19.2 | icon |
| mobile-pdp-1608-7090.html | `I1608:7526;1471:36949` | Similar Products - Images | 185 × 247 | image |
| mobile-pdp-1608-7090.html | `I1608:7526;1471:37248` | Star | 9.535 × 9.535 | icon |
| mobile-pdp-1608-7090.html | `I1608:7526;1548:40637;1548:40450` | Linear / Like / Heart | 19.2 × 19.2 | icon |
| mobile-pdp-1608-7090.html | `I1608:7527;1471:36949` | Similar Products - Images | 185 × 247 | image |
| mobile-pdp-1608-7090.html | `I1608:7527;1471:37248` | Star | 9.535 × 9.535 | icon |
| mobile-pdp-1608-7090.html | `I1608:7527;1548:40637;1548:40450` | Linear / Like / Heart | 19.2 × 19.2 | icon |
| mobile-pdp-1608-7090.html | `I1608:7528;1471:36949` | Similar Products - Images | 185 × 247 | image |
| mobile-pdp-1608-7090.html | `I1608:7528;1471:37248` | Star | 9.535 × 9.535 | icon |
| mobile-pdp-1608-7090.html | `I1608:7528;1548:40637;1548:40450` | Linear / Like / Heart | 19.2 × 19.2 | icon |
| mobile-pdp-1608-7090.html | `I1608:7529;1471:36949` | Similar Products - Images | 185 × 247 | image |
| mobile-pdp-1608-7090.html | `I1608:7529;1471:37248` | Star | 9.535 × 9.535 | icon |
| mobile-pdp-1608-7090.html | `I1608:7529;1548:40637;1548:40450` | Linear / Like / Heart | 19.2 × 19.2 | icon |
| mobile-pdp-1608-7090.html | `1608:7534` | Linear / Arrows / Arrow Right | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `I1608:7550;1519:25227` | Images | 125 × 158 | image |
| mobile-pdp-1608-7090.html | `I1608:7550;1519:25228` | Image-2 | 125 × 70 | image |
| mobile-pdp-1608-7090.html | `I1608:7550;1519:25229` | Image-3 | 52 × 52 | image |
| mobile-pdp-1608-7090.html | `I1608:7550;1519:25230` | Image-4 | 52 × 52 | image |
| mobile-pdp-1608-7090.html | `I1608:7550;1519:25233` | Image-5 | 52 × 52 | image |
| mobile-pdp-1608-7090.html | `I1608:7550;1519:25231` | Image-6 | 52 × 52 | image |
| mobile-pdp-1608-7090.html | `I1608:7550;1519:26498;1519:26469` | Linear / Like / Heart | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `I1608:7563;1519:25227` | Images | 125 × 158 | image |
| mobile-pdp-1608-7090.html | `I1608:7563;1519:25228` | Image-2 | 125 × 70 | image |
| mobile-pdp-1608-7090.html | `I1608:7563;1519:25229` | Image-3 | 52 × 52 | image |
| mobile-pdp-1608-7090.html | `I1608:7563;1519:25230` | Image-4 | 52 × 52 | image |
| mobile-pdp-1608-7090.html | `I1608:7563;1519:25233` | Image-5 | 52 × 52 | image |
| mobile-pdp-1608-7090.html | `I1608:7563;1519:25231` | Image-6 | 52 × 52 | image |
| mobile-pdp-1608-7090.html | `I1608:7563;1519:26498;1519:26469` | Linear / Like / Heart | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `I1608:7576;1519:25227` | Images | 125 × 158 | image |
| mobile-pdp-1608-7090.html | `I1608:7576;1519:25228` | Image-2 | 125 × 70 | image |
| mobile-pdp-1608-7090.html | `I1608:7576;1519:25229` | Image-3 | 52 × 52 | image |
| mobile-pdp-1608-7090.html | `I1608:7576;1519:25230` | Image-4 | 52 × 52 | image |
| mobile-pdp-1608-7090.html | `I1608:7576;1519:25233` | Image-5 | 52 × 52 | image |
| mobile-pdp-1608-7090.html | `I1608:7576;1519:25231` | Image-6 | 52 × 52 | image |
| mobile-pdp-1608-7090.html | `I1608:7576;1519:26498;1519:26469` | Linear / Like / Heart | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `I1608:7589;1519:25227` | Images | 125 × 158 | image |
| mobile-pdp-1608-7090.html | `I1608:7589;1519:25228` | Image-2 | 125 × 70 | image |
| mobile-pdp-1608-7090.html | `I1608:7589;1519:25229` | Image-3 | 52 × 52 | image |
| mobile-pdp-1608-7090.html | `I1608:7589;1519:25230` | Image-4 | 52 × 52 | image |
| mobile-pdp-1608-7090.html | `I1608:7589;1519:25233` | Image-5 | 52 × 52 | image |
| mobile-pdp-1608-7090.html | `I1608:7589;1519:25231` | Image-6 | 52 × 52 | image |
| mobile-pdp-1608-7090.html | `I1608:7589;1519:26498;1519:26469` | Linear / Like / Heart | 24 × 24 | icon |
| mobile-pdp-1608-7090.html | `1608:7092` | Bottom Edge | 360 × 15 | image |
| mobile-pdp-1608-7090.html | `1608:7093` | Home Indicator | 139 × 3 | image |
| mobile-putaway-1627-11756.html | `1627:11761` | ArrowLeft | 24 × 24 | icon |
| mobile-putaway-1627-11756.html | `1627:11771` | Frame | 24 × 24 | icon |
| mobile-putaway-1627-11756.html | `1627:11780` | Line 1 (stroke colour only in SVG asset) | 328 × 0 | image (stroke) |
| mobile-putaway-1627-11756.html | `1627:11792` | Line 1 (stroke colour only in SVG asset) | 328 × 0 | image (stroke) |
| mobile-putaway-1627-11756.html | `1627:11860` | 🥽 Goggles (Swimming, Diving, Gear) | 48 × 48 | image |
| mobile-putaway-1627-11756.html | `1627:11876` | Line (stroke colour only in SVG asset) | 304 × 0 | image (stroke) |
| mobile-putaway-1627-11756.html | `1627:11933` | Vector (minus) | 15 × 1.25 | icon |
| mobile-putaway-1627-11756.html | `1627:11938` | Vector (plus) | 15 × 15 | icon |
| mobile-putaway-1627-11756.html | `1627:11654` | Cellular Signal | 18 × 10 | icon |
| mobile-putaway-1627-11756.html | `1627:11690` | Wifi | 16 × 11.619 | icon |
| mobile-putaway-1627-11756.html | `1627:11720` | Battery | 24 × 12 | icon |
| job-listing-page-1629-11987.html | `1629:11992` | ArrowLeft | 24 × 24 | icon |
| job-listing-page-1629-11987.html | `1629:12002` | Frame | 24 × 24 | icon |
| job-listing-page-1629-11987.html | `1629:12007` | Ellipse (status dot) | 12 × 12 | icon |
| job-listing-page-1629-11987.html | `1629:12009` | Frame (chevron) | 16 × 16 | icon |
| job-listing-page-1629-11987.html | `1629:12011` | Line 1 (stroke colour only in SVG asset) | 328 × 0 | image (stroke) |
| job-listing-page-1629-11987.html | `1629:12566` | Line (stroke colour only in SVG asset) | 306 × 0 | image (stroke) |
| job-listing-page-1629-11987.html | `1629:12126` | Line (stroke colour only in SVG asset) | 304 × 0 | image (stroke) |
| job-listing-page-1629-11987.html | `1629:12203` | Line (stroke colour only in SVG asset) | 304 × 0 | image (stroke) |
| job-listing-page-1629-11987.html | `1629:12282` | Line (stroke colour only in SVG asset) | 304 × 0 | image (stroke) |
| job-listing-page-1629-11987.html | `1627:11654` | Cellular Signal | 18 × 10 | icon |
| job-listing-page-1629-11987.html | `1627:11690` | Wifi | 16 × 11.619 | icon |
| job-listing-page-1629-11987.html | `1627:11720` | Battery | 24 × 12 | icon |

Total placeholders: **223** (icon: 118, image: 99, logo: 6).

### Literal values set inline in the HTML (per element, with node id)

Positions (`left/top/width/height`) of top-level sections are the Figma metadata x / y / size. Gaps, paddings and other values are the Figma auto-layout values from get_design_context.

| File | Node id | Inline declarations |
|---|---|---|
| desktop-pdp-1375-30858.html | `1375:31289` | `left:0; top:0; width:1440px; height:180px;` |
| desktop-pdp-1375-30858.html | `1375:31291` | `gap:50px;` |
| desktop-pdp-1375-30858.html | `1375:31292` | `width:156.5px;` |
| desktop-pdp-1375-30858.html | `1375:31334` | `gap:32px;` |
| desktop-pdp-1375-30858.html | `1375:31335` | `gap:6px;` |
| desktop-pdp-1375-30858.html | `1375:31337` | `gap:10px;` |
| desktop-pdp-1375-30858.html | `1375:31342` | `gap:8px;` |
| desktop-pdp-1375-30858.html | `1375:31346` | `width:381px; --_input-border: var(--annachy-color-border-secondary);` |
| desktop-pdp-1375-30858.html | `I1375:31346;1066:41600` | `block-size:48px;` |
| desktop-pdp-1375-30858.html | `1375:31347` | `gap:24px; justify-content:flex-end;` |
| desktop-pdp-1375-30858.html | `1375:31348` | `gap:8px;` |
| desktop-pdp-1375-30858.html | `1375:31349` | `gap:10px;` |
| desktop-pdp-1375-30858.html | `1375:31357` | `gap:10px;` |
| desktop-pdp-1375-30858.html | `1375:31367` | `gap:48px;` |
| desktop-pdp-1375-30858.html | `1375:31368` | `gap:8px;` |
| desktop-pdp-1375-30858.html | `1375:31374` | `gap:28px;` |
| desktop-pdp-1375-30858.html | `1375:31375` | `gap:8px;` |
| desktop-pdp-1375-30858.html | `1375:31376` | `gap:8px;` |
| desktop-pdp-1375-30858.html | `1375:31377` | `gap:8px;` |
| desktop-pdp-1375-30858.html | `1375:31378` | `gap:8px;` |
| desktop-pdp-1375-30858.html | `1375:31379` | `gap:24px;` |
| desktop-pdp-1375-30858.html | `1375:31380` | `gap:4px;` |
| desktop-pdp-1375-30858.html | `1375:31387` | `gap:4px;` |
| desktop-pdp-1375-30858.html | `1375:30859` | `left:120px; top:233px; width:1200px; height:2407px;` |
| desktop-pdp-1375-30858.html | `1375:30860` | `left:0; top:0; width:546px; height:2407px; gap:9.53px;` |
| desktop-pdp-1375-30858.html | `1375:30861` | `gap:9.53px;` |
| desktop-pdp-1375-30858.html | `1375:30866` | `gap:9.53px; position:relative;` |
| desktop-pdp-1375-30858.html | `1375:30876` | `left:590px; top:0; width:610px; height:808px;` |
| desktop-pdp-1375-30858.html | `1375:30877` | `left:0; top:0; height:20px; gap:12px;` |
| desktop-pdp-1375-30858.html | `1375:30878` | `gap:4px;` |
| desktop-pdp-1375-30858.html | `1375:30881` | `gap:4px;` |
| desktop-pdp-1375-30858.html | `1375:30884` | `gap:4px;` |
| desktop-pdp-1375-30858.html | `1375:30887` | `gap:4px;` |
| desktop-pdp-1375-30858.html | `1375:30891` | `white-space:pre;` |
| desktop-pdp-1375-30858.html | `1375:30893` | `left:0; top:45px; width:610px; height:753px; gap:24px;` |
| desktop-pdp-1375-30858.html | `1375:30894` | `gap:24px;` |
| desktop-pdp-1375-30858.html | `1375:30895` | `gap:8px;` |
| desktop-pdp-1375-30858.html | `1375:30896` | `gap:6px; position:relative;` |
| desktop-pdp-1375-30858.html | `1375:30899` | `left:520px; top:0; width:84px; gap:18px; justify-content:flex-end;` |
| desktop-pdp-1375-30858.html | `1375:30907` | `gap:2px;` |
| desktop-pdp-1375-30858.html | `1375:30908` | `gap:2px;` |
| desktop-pdp-1375-30858.html | `1375:30910` | `gap:4px;` |
| desktop-pdp-1375-30858.html | `1375:30911` | `gap:2px;` |
| desktop-pdp-1375-30858.html | `1375:30922` | `white-space:pre;` |
| desktop-pdp-1375-30858.html | `1375:30924` | `gap:24px;` |
| desktop-pdp-1375-30858.html | `1375:30925` | `gap:4px; height:90px; width:367px; justify-content:center;` |
| desktop-pdp-1375-30858.html | `1375:30926` | `gap:8px;` |
| desktop-pdp-1375-30858.html | `1375:30928` | `gap:8px;` |
| desktop-pdp-1375-30858.html | `1375:30929` | `gap:8px;` |
| desktop-pdp-1375-30858.html | `1375:30934` | `width:106px; --_gb-radius: var(--annachy-radius-4);` |
| desktop-pdp-1375-30858.html | `1375:30935` | `gap:4px;` |
| desktop-pdp-1375-30858.html | `1375:30938` | `gap:4px;` |
| desktop-pdp-1375-30858.html | `1375:30945` | `gap:24px;` |
| desktop-pdp-1375-30858.html | `1375:30946` | `gap:38px;` |
| desktop-pdp-1375-30858.html | `1375:30947` | `gap:42px;` |
| desktop-pdp-1375-30858.html | `1375:30948` | `gap:18px; align-items:flex-end;` |
| desktop-pdp-1375-30858.html | `1375:30951` | `gap:12px;` |
| desktop-pdp-1375-30858.html | `1375:30958` | `gap:24px;` |
| desktop-pdp-1375-30858.html | `1375:30959` | `border-color:rgba(36, 35, 42, 0.5);` |
| desktop-pdp-1375-30858.html | `1375:30960` | `border-radius:var(--annachy-radius-8);` |
| desktop-pdp-1375-30858.html | `1375:30962` | `text-align:center;` |
| desktop-pdp-1375-30858.html | `1375:30963` | `border-color:rgba(97, 104, 101, 0.5);` |
| desktop-pdp-1375-30858.html | `1375:30966` | `text-align:center;` |
| desktop-pdp-1375-30858.html | `1375:30967` | `border-color:rgba(173, 182, 197, 0.5);` |
| desktop-pdp-1375-30858.html | `1375:30970` | `text-align:center;` |
| desktop-pdp-1375-30858.html | `1375:30971` | `border-color:rgba(100, 138, 155, 0.5);` |
| desktop-pdp-1375-30858.html | `1375:30973` | `left:-6px; top:-1px; width:93px; height:105px; overflow:clip; background:#034784; border-radius:var(--annachy-radius-12);` |
| desktop-pdp-1375-30858.html | `1375:30975` | `text-align:center;` |
| desktop-pdp-1375-30858.html | `1375:30976` | `border-color:rgba(134, 24, 32, 0.5);` |
| desktop-pdp-1375-30858.html | `1375:30979` | `text-align:center;` |
| desktop-pdp-1375-30858.html | `1375:30980` | `gap:18px;` |
| desktop-pdp-1375-30858.html | `1375:30982` | `width:101px;` |
| desktop-pdp-1375-30858.html | `1375:30983` | `width:92px; text-align:right;` |
| desktop-pdp-1375-30858.html | `1375:30984` | `gap:24px;` |
| desktop-pdp-1375-30858.html | `1375:30991` | `gap:16px; height:71px;` |
| desktop-pdp-1375-30858.html | `1375:31000` | `width:373px; --_gb-radius: var(--annachy-radius-8);` |
| desktop-pdp-1375-30858.html | `1375:31003` | `left:0; top:840px; width:610px; height:603px; gap:24px;` |
| desktop-pdp-1375-30858.html | `1375:31004` | `gap:14px; height:276px; overflow:clip;` |
| desktop-pdp-1375-30858.html | `1375:31008` | `gap:18px;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `gap:8px; width:520px;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `gap:6px;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `gap:14px;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `width:144px;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `width:124px;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `gap:8px; width:520px;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `gap:6px;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `gap:14px;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `white-space:nowrap;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `width:124px;` |
| desktop-pdp-1375-30858.html | `1375:31029` | `gap:20px;` |
| desktop-pdp-1375-30858.html | `1375:31030` | `gap:12px;` |
| desktop-pdp-1375-30858.html | `1375:31031` | `width:610px; --_input-height: 63px; --_input-border: var(--annachy-color-border-primary);` |
| desktop-pdp-1375-30858.html | `1375:31032` | `block-size:auto; gap:8px;` |
| desktop-pdp-1375-30858.html | `1375:31039` | `width:56px; height:24px;` |
| desktop-pdp-1375-30858.html | `1375:31045` | `gap:2px;` |
| desktop-pdp-1375-30858.html | `1375:31048` | `gap:30px; padding:0 14px; align-items:flex-start;` |
| desktop-pdp-1375-30858.html | `1375:31056` | `text-align:center;` |
| desktop-pdp-1375-30858.html | `1375:31077` | `left:0; top:1485px; width:610px; height:1036px; gap:51px; align-items:flex-end;` |
| desktop-pdp-1375-30858.html | `1375:31078` | `gap:25px;` |
| desktop-pdp-1375-30858.html | `1375:31079` | `gap:18px;` |
| desktop-pdp-1375-30858.html | `1375:31081` | `gap:8px;` |
| desktop-pdp-1375-30858.html | `1375:31087` | `width:144px;` |
| desktop-pdp-1375-30858.html | `1375:31091` | `overflow:clip;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `width:140px; flex:none;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `width:140px; flex:none;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `width:140px; flex:none;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `width:140px; flex:none;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `width:140px; flex:none;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `width:140px; flex:none;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `width:140px; flex:none;` |
| desktop-pdp-1375-30858.html | `1375:31113` | `gap:20px; align-items:flex-end;` |
| desktop-pdp-1375-30858.html | `1375:31114` | `gap:18px;` |
| desktop-pdp-1375-30858.html | `1375:31115` | `gap:8px;` |
| desktop-pdp-1375-30858.html | `1375:31120` | `width:144px;` |
| desktop-pdp-1375-30858.html | `1375:31121` | `gap:42px;` |
| desktop-pdp-1375-30858.html | `1375:31122` | `gap:65px;` |
| desktop-pdp-1375-30858.html | `1375:31123` | `gap:18px; width:270px;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `gap:8px;` |
| desktop-pdp-1375-30858.html | `1375:31128` | `gap:18px; width:270px;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `gap:8px;` |
| desktop-pdp-1375-30858.html | `1375:31133` | `gap:65px;` |
| desktop-pdp-1375-30858.html | `1375:31134` | `gap:18px; width:270px;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `gap:8px;` |
| desktop-pdp-1375-30858.html | `1375:31139` | `gap:18px; width:270px;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `gap:8px;` |
| desktop-pdp-1375-30858.html | `1375:31144` | `gap:65px;` |
| desktop-pdp-1375-30858.html | `1375:31145` | `gap:18px; width:270px;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `gap:8px;` |
| desktop-pdp-1375-30858.html | `1375:31150` | `gap:18px; width:270px;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `gap:8px;` |
| desktop-pdp-1375-30858.html | `1375:31163` | `left:120px; top:2779px; width:1200px; height:731px;` |
| desktop-pdp-1375-30858.html | `1375:31164` | `left:0; top:0; width:1200px; height:313px; gap:28px;` |
| desktop-pdp-1375-30858.html | `1375:31165` | `height:1px; background:#e2e5e9;` |
| desktop-pdp-1375-30858.html | `1375:31166` | `overflow:clip;` |
| desktop-pdp-1375-30858.html | `1375:31168` | `height:232px;` |
| desktop-pdp-1375-30858.html | `1375:31169` | `gap:4px; width:260px; overflow:clip; flex:none;` |
| desktop-pdp-1375-30858.html | `1375:31175` | `width:1px; height:168px; background:var(--annachy-color-border-secondary); flex:none;` |
| desktop-pdp-1375-30858.html | `1375:31176` | `gap:20px; overflow:clip;` |
| desktop-pdp-1375-30858.html | `1375:31178` | `gap:14px; overflow:clip;` |
| desktop-pdp-1375-30858.html | `1375:31179` | `gap:12px; overflow:clip;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `width:86px; flex:none;` |
| desktop-pdp-1375-30858.html | `1375:31182` | `width:97.44px;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `width:35px; flex:none; text-align:right;` |
| desktop-pdp-1375-30858.html | `1375:31184` | `gap:12px; overflow:clip;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `width:86px; flex:none;` |
| desktop-pdp-1375-30858.html | `1375:31187` | `width:63.945px;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `width:35px; flex:none; text-align:right;` |
| desktop-pdp-1375-30858.html | `1375:31189` | `gap:12px; overflow:clip;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `width:86px; flex:none;` |
| desktop-pdp-1375-30858.html | `1375:31192` | `width:63.945px;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `width:35px; flex:none; text-align:right;` |
| desktop-pdp-1375-30858.html | `1375:31194` | `gap:12px; overflow:clip;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `width:86px; flex:none;` |
| desktop-pdp-1375-30858.html | `1375:31197` | `width:36.54px;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `width:35px; flex:none; text-align:right;` |
| desktop-pdp-1375-30858.html | `1375:31199` | `gap:20px; overflow:clip;` |
| desktop-pdp-1375-30858.html | `1375:31201` | `gap:14px; overflow:clip;` |
| desktop-pdp-1375-30858.html | `1375:31202` | `gap:12px; overflow:clip;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `width:86px; flex:none;` |
| desktop-pdp-1375-30858.html | `1375:31205` | `width:54.81px;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `width:35px; flex:none; text-align:right;` |
| desktop-pdp-1375-30858.html | `1375:31207` | `gap:12px; overflow:clip;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `width:86px; flex:none;` |
| desktop-pdp-1375-30858.html | `1375:31210` | `width:82.215px;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `width:35px; flex:none; text-align:right;` |
| desktop-pdp-1375-30858.html | `1375:31212` | `gap:12px; overflow:clip;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `width:86px; flex:none;` |
| desktop-pdp-1375-30858.html | `1375:31215` | `width:103.53px;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `width:35px; flex:none; text-align:right;` |
| desktop-pdp-1375-30858.html | `1375:31217` | `gap:12px; overflow:clip;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `width:86px; flex:none;` |
| desktop-pdp-1375-30858.html | `1375:31220` | `width:18.27px;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `width:35px; flex:none; text-align:right;` |
| desktop-pdp-1375-30858.html | `1375:31222` | `left:0; top:349px; width:1200px; height:382px;` |
| desktop-pdp-1375-30858.html | `1375:31223` | `left:0; top:0; width:1200px; height:30px; align-items:flex-start;` |
| desktop-pdp-1375-30858.html | `1375:31224` | `width:206px; text-transform:capitalize;` |
| desktop-pdp-1375-30858.html | `1375:31225` | `gap:8px; width:172px; justify-content:flex-end;` |
| desktop-pdp-1375-30858.html | `1375:31226` | `width:134px; text-align:right; text-transform:capitalize;` |
| desktop-pdp-1375-30858.html | `1375:31229` | `left:0; top:62px; width:1200px; height:320px; gap:28px;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `left:16.54px; top:15.4px; width:28.426px; height:39.278px; gap:4.738px; align-items:center; justify-content:center;` |
| desktop-pdp-1375-30858.html | `1375:31236` | `align-items:center; font-size:10.66px; line-height:normal; font-weight:var(--annachy-font-weight-bold); text-align:center;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `color:#fafdff; text-decoration:underline;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `color:#badefd;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `left:16.54px; top:15.4px; width:28.426px; height:39.278px; gap:4.738px; align-items:center; justify-content:center;` |
| desktop-pdp-1375-30858.html | `1375:31245` | `align-items:center; font-size:10.66px; line-height:normal; font-weight:var(--annachy-font-weight-bold); text-align:center;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `color:#fafdff; text-decoration:underline;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `color:#badefd;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `left:16.54px; top:15.4px; width:28.426px; height:39.278px; gap:4.738px; align-items:center; justify-content:center;` |
| desktop-pdp-1375-30858.html | `1375:31254` | `align-items:center; font-size:10.66px; line-height:normal; font-weight:var(--annachy-font-weight-bold); text-align:center;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `color:#fafdff; text-decoration:underline;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `color:#badefd;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `left:16.54px; top:15.4px; width:28.426px; height:39.278px; gap:4.738px; align-items:center; justify-content:center;` |
| desktop-pdp-1375-30858.html | `1375:31263` | `align-items:center; font-size:10.66px; line-height:normal; font-weight:var(--annachy-font-weight-bold); text-align:center;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `color:#fafdff; text-decoration:underline;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `color:#badefd;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `left:16.54px; top:15.4px; width:28.426px; height:39.278px; gap:4.738px; align-items:center; justify-content:center;` |
| desktop-pdp-1375-30858.html | `1375:31272` | `align-items:center; font-size:10.66px; line-height:normal; font-weight:var(--annachy-font-weight-bold); text-align:center;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `color:#fafdff; text-decoration:underline;` |
| desktop-pdp-1375-30858.html | `(child of preceding node)` | `color:#badefd;` |
| desktop-pdp-1375-30858.html | `1375:31282` | `left:91px; top:3326px; width:1259px; height:66.667px;` |
| mobile-pdp-1608-7090.html | `1608:7094` | `left:0; top:0; width:360px; height:35px;` |
| mobile-pdp-1608-7090.html | `1608:7095` | `gap:8px; align-items:flex-end;` |
| mobile-pdp-1608-7090.html | `1608:7099` | `width:51px; height:17px; text-align:center;` |
| mobile-pdp-1608-7090.html | `1608:7112` | `left:0; top:35px; width:360px; height:58px;` |
| mobile-pdp-1608-7090.html | `1608:7116` | `gap:8px;` |
| mobile-pdp-1608-7090.html | `1608:7125` | `left:16px; top:647px; width:330px; height:132px; gap:10px;` |
| mobile-pdp-1608-7090.html | `1608:7126` | `gap:4px;` |
| mobile-pdp-1608-7090.html | `1608:7127` | `gap:2px;` |
| mobile-pdp-1608-7090.html | `1608:7131` | `gap:2px;` |
| mobile-pdp-1608-7090.html | `1608:7133` | `gap:2px;` |
| mobile-pdp-1608-7090.html | `1608:7134` | `gap:12px;` |
| mobile-pdp-1608-7090.html | `1608:7135` | `gap:5px;` |
| mobile-pdp-1608-7090.html | `1608:7136` | `width:63px; height:20px; white-space:pre;` |
| mobile-pdp-1608-7090.html | `1608:7141` | `gap:4px; padding:0 10px;` |
| mobile-pdp-1608-7090.html | `1608:7147` | `gap:2px; align-self:stretch;` |
| mobile-pdp-1608-7090.html | `1608:7151` | `left:0; top:797px; width:360px; height:288px;` |
| mobile-pdp-1608-7090.html | `1608:7152` | `left:0; top:0; width:360px; height:172px; padding:0 17px;` |
| mobile-pdp-1608-7090.html | `I1608:7152;1546:26671` | `gap:12px; width:337px;` |
| mobile-pdp-1608-7090.html | `I1608:7152;1546:26551` | `gap:2px; align-items:flex-end;` |
| mobile-pdp-1608-7090.html | `I1608:7152;1546:26607` | `gap:11px;` |
| mobile-pdp-1608-7090.html | `I1608:7152;1539:30179;1010:21647` | `left:-1px; bottom:-1px;` |
| mobile-pdp-1608-7090.html | `I1608:7152;1539:30179;1010:21649` | `height:17px;` |
| mobile-pdp-1608-7090.html | `I1608:7152;1539:30179;1539:28948` | `position:relative; height:10px;` |
| mobile-pdp-1608-7090.html | `I1608:7152;1539:30179;1539:28949` | `margin-top:-2px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `width:67px; height:16px; display:flex; align-items:center;` |
| mobile-pdp-1608-7090.html | `I1608:7152;1539:30180;1010:21647` | `left:0; bottom:0;` |
| mobile-pdp-1608-7090.html | `I1608:7152;1539:30180;1010:21649` | `height:17px;` |
| mobile-pdp-1608-7090.html | `I1608:7152;1539:30180;1539:28948` | `position:relative; height:10px;` |
| mobile-pdp-1608-7090.html | `I1608:7152;1539:30180;1539:28949` | `margin-top:-2px;` |
| mobile-pdp-1608-7090.html | `I1608:7152;1539:30181;1010:21647` | `left:0; bottom:0;` |
| mobile-pdp-1608-7090.html | `I1608:7152;1539:30181;1010:21649` | `height:17px;` |
| mobile-pdp-1608-7090.html | `I1608:7152;1539:30181;1539:28948` | `position:relative; height:10px;` |
| mobile-pdp-1608-7090.html | `I1608:7152;1539:30181;1539:28949` | `margin-top:-2px;` |
| mobile-pdp-1608-7090.html | `I1608:7152;1539:30182;1010:21647` | `left:0; bottom:0;` |
| mobile-pdp-1608-7090.html | `I1608:7152;1539:30182;1010:21649` | `height:17px;` |
| mobile-pdp-1608-7090.html | `I1608:7152;1539:30182;1539:28948` | `position:relative; height:10px;` |
| mobile-pdp-1608-7090.html | `I1608:7152;1539:30182;1539:28949` | `margin-top:-2px;` |
| mobile-pdp-1608-7090.html | `1608:7153` | `left:0; top:196px; width:360px; height:92px; gap:18px; padding:0 16px;` |
| mobile-pdp-1608-7090.html | `I1608:7153;1546:27167` | `white-space:pre;` |
| mobile-pdp-1608-7090.html | `I1608:7153;1546:27137` | `gap:2px;` |
| mobile-pdp-1608-7090.html | `I1608:7153;1546:27123` | `gap:14px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `width:45px; text-align:left;` |
| mobile-pdp-1608-7090.html | `1608:7154` | `left:16px; top:1111px; width:328px; height:127px;` |
| mobile-pdp-1608-7090.html | `1608:7155` | `left:0; top:0; width:328px; height:71px; overflow:clip;` |
| mobile-pdp-1608-7090.html | `I1608:7155;1066:38864` | `block-size:auto; gap:7px;` |
| mobile-pdp-1608-7090.html | `1608:7156` | `left:-16px; top:89px;` |
| mobile-pdp-1608-7090.html | `1608:7157` | `left:44px; top:10px; width:157px; text-align:right;` |
| mobile-pdp-1608-7090.html | `1608:7177` | `left:240px; top:10px; width:114px; height:20px; gap:6px; align-items:center;` |
| mobile-pdp-1608-7090.html | `1608:7179` | `white-space:pre;` |
| mobile-pdp-1608-7090.html | `1608:7180` | `position:relative; display:flex;` |
| mobile-pdp-1608-7090.html | `1608:7183` | `left:0; top:1238px; width:360px; height:231px;` |
| mobile-pdp-1608-7090.html | `1608:7184` | `align-items:center;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:4px;` |
| mobile-pdp-1608-7090.html | `1608:7195` | `height:20px;` |
| mobile-pdp-1608-7090.html | `1608:7198` | `align-items:flex-end;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:4px;` |
| mobile-pdp-1608-7090.html | `1608:7213` | `height:20px;` |
| mobile-pdp-1608-7090.html | `1608:7217` | `align-items:flex-end;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:4px;` |
| mobile-pdp-1608-7090.html | `1608:7232` | `height:20px;` |
| mobile-pdp-1608-7090.html | `1608:7233` | `gap:2px;` |
| mobile-pdp-1608-7090.html | `1608:7239` | `left:0; top:1469px; width:360px; height:2234px;` |
| mobile-pdp-1608-7090.html | `1608:7241` | `left:16px; top:30px; width:328px; height:632px; gap:26px;` |
| mobile-pdp-1608-7090.html | `1608:7244` | `gap:24px; align-items:flex-end; height:582px;` |
| mobile-pdp-1608-7090.html | `1608:7245` | `gap:26px; overflow:clip; min-height:1px;` |
| mobile-pdp-1608-7090.html | `1608:7246` | `gap:26px;` |
| mobile-pdp-1608-7090.html | `1608:7247` | `align-items:flex-start;` |
| mobile-pdp-1608-7090.html | `I1608:7248;1548:30751` | `width:124.788px;` |
| mobile-pdp-1608-7090.html | `I1608:7249;1548:30751` | `width:124.788px;` |
| mobile-pdp-1608-7090.html | `1608:7250` | `align-items:flex-start;` |
| mobile-pdp-1608-7090.html | `I1608:7251;1548:30751` | `width:124.788px;` |
| mobile-pdp-1608-7090.html | `I1608:7252;1548:30751` | `width:124.788px;` |
| mobile-pdp-1608-7090.html | `1608:7253` | `align-items:flex-start;` |
| mobile-pdp-1608-7090.html | `I1608:7254;1548:30751` | `width:124.788px;` |
| mobile-pdp-1608-7090.html | `I1608:7255;1548:30751` | `width:124.788px;` |
| mobile-pdp-1608-7090.html | `1608:7256` | `gap:26px;` |
| mobile-pdp-1608-7090.html | `1608:7257` | `align-items:flex-start;` |
| mobile-pdp-1608-7090.html | `I1608:7258;1548:30751` | `width:124.788px;` |
| mobile-pdp-1608-7090.html | `I1608:7259;1548:30751` | `width:124.788px;` |
| mobile-pdp-1608-7090.html | `1608:7260` | `align-items:flex-start;` |
| mobile-pdp-1608-7090.html | `I1608:7261;1548:30751` | `width:124.788px;` |
| mobile-pdp-1608-7090.html | `I1608:7262;1548:30751` | `width:124.788px;` |
| mobile-pdp-1608-7090.html | `1608:7263` | `align-items:flex-start;` |
| mobile-pdp-1608-7090.html | `I1608:7264;1548:30751` | `width:124.788px;` |
| mobile-pdp-1608-7090.html | `I1608:7265;1548:30751` | `width:124.788px;` |
| mobile-pdp-1608-7090.html | `1608:7267` | `left:16px; top:698px; width:328px; height:1301px; gap:26px;` |
| mobile-pdp-1608-7090.html | `1608:7269` | `position:relative; height:1251px;` |
| mobile-pdp-1608-7090.html | `1608:7270` | `left:0; top:0; width:328px; height:688px; padding-bottom:18px; border-bottom:1px solid #e5e7e8; overflow:clip;` |
| mobile-pdp-1608-7090.html | `1608:7274` | `gap:8px; width:362px;` |
| mobile-pdp-1608-7090.html | `I1608:7274;1548:33544` | `height:24px; align-items:flex-start;` |
| mobile-pdp-1608-7090.html | `I1608:7274;1548:33545` | `gap:10px; width:236px;` |
| mobile-pdp-1608-7090.html | `I1608:7274;1548:33547` | `height:22px; color:transparent;` |
| mobile-pdp-1608-7090.html | `1608:7275` | `gap:18px; margin-top:8px; min-height:1px; flex:1 0 0;` |
| mobile-pdp-1608-7090.html | `1608:7276` | `gap:12px; overflow-x:auto; overflow-y:clip;` |
| mobile-pdp-1608-7090.html | `1608:7280` | `gap:16px; align-items:flex-end; min-height:1px;` |
| mobile-pdp-1608-7090.html | `1608:7281` | `overflow:clip; min-height:1px;` |
| mobile-pdp-1608-7090.html | `1608:7282` | `gap:26px; align-items:flex-end;` |
| mobile-pdp-1608-7090.html | `1608:7283` | `gap:20px; align-items:flex-start;` |
| mobile-pdp-1608-7090.html | `1608:7292` | `gap:20px; align-items:center;` |
| mobile-pdp-1608-7090.html | `1608:7301` | `gap:20px; align-items:center;` |
| mobile-pdp-1608-7090.html | `1608:7310` | `gap:20px; align-items:flex-start;` |
| mobile-pdp-1608-7090.html | `1608:7319` | `gap:20px; align-items:center;` |
| mobile-pdp-1608-7090.html | `1608:7328` | `gap:20px; align-items:center;` |
| mobile-pdp-1608-7090.html | `1608:7337` | `gap:20px; align-items:center;` |
| mobile-pdp-1608-7090.html | `1608:7347` | `left:0; top:706px; width:328px; height:545px; gap:12px;` |
| mobile-pdp-1608-7090.html | `1608:7348` | `gap:8px; width:362px;` |
| mobile-pdp-1608-7090.html | `I1608:7348;1548:33544` | `height:24px; align-items:flex-start;` |
| mobile-pdp-1608-7090.html | `I1608:7348;1548:33545` | `gap:10px; width:236px;` |
| mobile-pdp-1608-7090.html | `I1608:7348;1548:33547` | `height:22px; color:transparent;` |
| mobile-pdp-1608-7090.html | `1608:7349` | `position:relative; height:496px;` |
| mobile-pdp-1608-7090.html | `1608:7350` | `left:0; top:0; width:328px; height:491px; gap:24px; overflow:clip;` |
| mobile-pdp-1608-7090.html | `1608:7352` | `gap:20px;` |
| mobile-pdp-1608-7090.html | `1608:7354` | `width:236px; white-space:pre;` |
| mobile-pdp-1608-7090.html | `1608:7355` | `gap:16px;` |
| mobile-pdp-1608-7090.html | `1608:7361` | `gap:8px; width:173px;` |
| mobile-pdp-1608-7090.html | `1608:7365` | `gap:8px; height:130px;` |
| mobile-pdp-1608-7090.html | `1608:7366` | `height:100%;` |
| mobile-pdp-1608-7090.html | `1608:7368` | `gap:8px; height:100%;` |
| mobile-pdp-1608-7090.html | `1608:7372` | `inset:18.99% -0.56% 53.59% -0.56%;` |
| mobile-pdp-1608-7090.html | `1608:7381` | `left:50%; top:50%; width:180px; height:65px; transform:translate(-50%,-50%);` |
| mobile-pdp-1608-7090.html | `1608:7382` | `gap:2px; left:50%; top:50%; transform:translate(-50%,-50%);` |
| mobile-pdp-1608-7090.html | `1608:7386` | `gap:16px;` |
| mobile-pdp-1608-7090.html | `1608:7387` | `gap:20px; height:186px; padding:8px 0; overflow:clip;` |
| mobile-pdp-1608-7090.html | `I1608:7387;1321:18878` | `gap:16px;` |
| mobile-pdp-1608-7090.html | `I1608:7387;1321:18879` | `gap:14px;` |
| mobile-pdp-1608-7090.html | `I1608:7387;1321:18881` | `gap:4.453px; width:57px; height:26px; background:#027a48; border:1.113px solid #eaebec; border-radius:6.679px; overflow:clip;` |
| mobile-pdp-1608-7090.html | `I1608:7387;1321:18885` | `width:73px;` |
| mobile-pdp-1608-7090.html | `I1608:7387;1321:18886` | `gap:8px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `width:38px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `width:84px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `width:23px;` |
| mobile-pdp-1608-7090.html | `I1608:7387;1321:18910` | `overflow:hidden; text-overflow:ellipsis;` |
| mobile-pdp-1608-7090.html | `I1608:7387;1321:18912` | `gap:4px;` |
| mobile-pdp-1608-7090.html | `I1608:7387;1321:18915` | `width:76px;` |
| mobile-pdp-1608-7090.html | `1608:7388` | `width:100%;` |
| mobile-pdp-1608-7090.html | `1608:7391` | `left:0; top:2012px; width:360px; height:198px;` |
| mobile-pdp-1608-7090.html | `1608:7393` | `gap:8px; width:110px; align-items:center;` |
| mobile-pdp-1608-7090.html | `1608:7397` | `text-align:center;` |
| mobile-pdp-1608-7090.html | `1608:7398` | `gap:8px; width:110px; align-items:center;` |
| mobile-pdp-1608-7090.html | `1608:7403` | `text-align:center;` |
| mobile-pdp-1608-7090.html | `1608:7404` | `gap:8px; width:110px; align-items:center;` |
| mobile-pdp-1608-7090.html | `1608:7409` | `text-align:center;` |
| mobile-pdp-1608-7090.html | `1608:7410` | `height:76px;` |
| mobile-pdp-1608-7090.html | `1608:7419` | `gap:4px;` |
| mobile-pdp-1608-7090.html | `1608:7420` | `height:20px;` |
| mobile-pdp-1608-7090.html | `1608:7424` | `left:0; top:3703px; width:360px; height:842px;` |
| mobile-pdp-1608-7090.html | `1608:7425` | `left:0; top:0; width:360px; height:477px;` |
| mobile-pdp-1608-7090.html | `1608:7426` | `height:40px;` |
| mobile-pdp-1608-7090.html | `1608:7429` | `gap:14px; width:328px; height:371px;` |
| mobile-pdp-1608-7090.html | `1608:7430` | `align-self:flex-start;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:2px;` |
| mobile-pdp-1608-7090.html | `1608:7443` | `left:134px; top:13px; width:32px; height:32px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `opacity:0.9;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `height:19px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:4px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:2px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `width:62px;` |
| mobile-pdp-1608-7090.html | `1608:7461` | `width:100%;` |
| mobile-pdp-1608-7090.html | `1608:7462` | `align-self:flex-start;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:2px;` |
| mobile-pdp-1608-7090.html | `1608:7475` | `left:134px; top:13px; width:32px; height:32px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `opacity:0.9;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `height:19px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:4px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:2px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `width:62px;` |
| mobile-pdp-1608-7090.html | `1608:7493` | `width:100%;` |
| mobile-pdp-1608-7090.html | `1608:7494` | `align-self:flex-start;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:2px;` |
| mobile-pdp-1608-7090.html | `1608:7507` | `left:134px; top:13px; width:32px; height:32px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `opacity:0.9;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `height:19px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:4px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:2px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `width:62px;` |
| mobile-pdp-1608-7090.html | `1608:7525` | `width:100%;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:2px;` |
| mobile-pdp-1608-7090.html | `I1608:7526;1548:40637` | `left:134px; top:13px; width:32px; height:32px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:10px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:4px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `opacity:0.9;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `height:19px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:2px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:4px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:2px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `width:62px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:2px;` |
| mobile-pdp-1608-7090.html | `I1608:7527;1548:40637` | `left:134px; top:13px; width:32px; height:32px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:10px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:4px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `opacity:0.9;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `height:19px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:2px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:4px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:2px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `width:62px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:2px;` |
| mobile-pdp-1608-7090.html | `I1608:7528;1548:40637` | `left:134px; top:13px; width:32px; height:32px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:10px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:4px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `opacity:0.9;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `height:19px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:2px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:4px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:2px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `width:62px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:2px;` |
| mobile-pdp-1608-7090.html | `I1608:7529;1548:40637` | `left:134px; top:13px; width:32px; height:32px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:10px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:4px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `opacity:0.9;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `height:19px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:2px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:4px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:2px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `width:62px;` |
| mobile-pdp-1608-7090.html | `1608:7530` | `left:0; top:477px; width:360px; height:365px;` |
| mobile-pdp-1608-7090.html | `1608:7531` | `height:40px;` |
| mobile-pdp-1608-7090.html | `1608:7536` | `gap:8px; align-items:flex-end; width:328px; height:259px;` |
| mobile-pdp-1608-7090.html | `1608:7550` | `height:238px;` |
| mobile-pdp-1608-7090.html | `I1608:7550;1519:25347` | `gap:10px; align-items:flex-end; position:relative;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:10px; width:125px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:4px; width:52px; align-items:center; position:relative;` |
| mobile-pdp-1608-7090.html | `I1608:7550;1519:26498` | `left:0; top:-39px; width:52px; height:32px; border-width:0.85px;` |
| mobile-pdp-1608-7090.html | `I1608:7550;1519:26199` | `top:-21px;` |
| mobile-pdp-1608-7090.html | `1608:7563` | `height:259px;` |
| mobile-pdp-1608-7090.html | `I1608:7563;1519:25347` | `gap:10px; align-items:flex-end; position:relative;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:10px; width:125px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:4px; width:52px; align-items:center; position:relative;` |
| mobile-pdp-1608-7090.html | `I1608:7563;1519:26498` | `left:0; top:-39px; width:52px; height:32px; border-width:0.85px;` |
| mobile-pdp-1608-7090.html | `I1608:7563;1519:26199` | `top:-21px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `text-align:center;` |
| mobile-pdp-1608-7090.html | `1608:7576` | `height:259px;` |
| mobile-pdp-1608-7090.html | `I1608:7576;1519:25347` | `gap:10px; align-items:flex-end; position:relative;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:10px; width:125px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:4px; width:52px; align-items:center; position:relative;` |
| mobile-pdp-1608-7090.html | `I1608:7576;1519:26498` | `left:0; top:-39px; width:52px; height:32px; border-width:0.85px;` |
| mobile-pdp-1608-7090.html | `I1608:7576;1519:26199` | `top:-21px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `text-align:center;` |
| mobile-pdp-1608-7090.html | `1608:7589` | `height:259px;` |
| mobile-pdp-1608-7090.html | `I1608:7589;1519:25347` | `gap:10px; align-items:flex-end; position:relative;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:10px; width:125px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `gap:4px; width:52px; align-items:center; position:relative;` |
| mobile-pdp-1608-7090.html | `I1608:7589;1519:26498` | `left:0; top:-39px; width:52px; height:32px; border-width:0.85px;` |
| mobile-pdp-1608-7090.html | `I1608:7589;1519:26199` | `top:-21px;` |
| mobile-pdp-1608-7090.html | `(child of preceding node)` | `text-align:center;` |
| mobile-pdp-1608-7090.html | `1608:7590` | `left:0; top:4560px; width:360px; height:106px;` |
| mobile-pdp-1608-7090.html | `1608:7591` | `gap:14px;` |
| mobile-pdp-1608-7090.html | `1608:7592` | `width:134px;` |
| mobile-pdp-1608-7090.html | `1608:7091` | `left:0; top:4668px; width:360px; height:15px;` |
| mobile-putaway-1627-11756.html | `1627:11757` | `left:16px; top:52px; width:328px; height:58px;` |
| mobile-putaway-1627-11756.html | `1627:11758` | `align-items:center;` |
| mobile-putaway-1627-11756.html | `1627:11768` | `white-space:pre;` |
| mobile-putaway-1627-11756.html | `1627:11793` | `left:16px; top:134px; width:328px; height:168px; gap:8px;` |
| mobile-putaway-1627-11756.html | `1627:11796` | `height:168px;` |
| mobile-putaway-1627-11756.html | `1627:11798` | `gap:4px;` |
| mobile-putaway-1627-11756.html | `1627:11802` | `gap:4px;` |
| mobile-putaway-1627-11756.html | `1627:11809` | `width:57px;` |
| mobile-putaway-1627-11756.html | `1627:11840` | `left:16px; top:314px; width:328px; height:256px;` |
| mobile-putaway-1627-11756.html | `1627:11841` | `height:256px;` |
| mobile-putaway-1627-11756.html | `1627:11856` | `gap:12px; width:304px;` |
| mobile-putaway-1627-11756.html | `1627:11857` | `gap:8px;` |
| mobile-putaway-1627-11756.html | `1627:11862` | `gap:4px;` |
| mobile-putaway-1627-11756.html | `1627:11866` | `gap:5px; height:64px;` |
| mobile-putaway-1627-11756.html | `1627:11867` | `align-items:flex-start;` |
| mobile-putaway-1627-11756.html | `1627:11868` | `width:77px;` |
| mobile-putaway-1627-11756.html | `1627:11870` | `align-items:flex-start;` |
| mobile-putaway-1627-11756.html | `1627:11873` | `align-items:flex-start;` |
| mobile-putaway-1627-11756.html | `1627:11874` | `width:77px;` |
| mobile-putaway-1627-11756.html | `1627:11883` | `gap:4px; width:304px;` |
| mobile-putaway-1627-11756.html | `1627:11884` | `height:24px;` |
| mobile-putaway-1627-11756.html | `1627:11890` | `width:13px;` |
| mobile-putaway-1627-11756.html | `1627:11930` | `left:16px; top:582px; height:20px;` |
| mobile-putaway-1627-11756.html | `1627:11931` | `left:16px; top:614px; width:328px; height:56px;` |
| mobile-putaway-1627-11756.html | `1627:11932` | `width:60px;` |
| mobile-putaway-1627-11756.html | `1627:11937` | `width:60px;` |
| mobile-putaway-1627-11756.html | `1627:11986` | `left:-3px; top:720px; width:363px; height:80px;` |
| job-listing-page-1629-11987.html | `1629:11988` | `left:16px; top:52px; width:328px; height:58px;` |
| job-listing-page-1629-11987.html | `1629:12006` | `gap:8px;` |
| job-listing-page-1629-11987.html | `1629:12012` | `left:16px; top:122px; width:328px; height:44px;` |
| job-listing-page-1629-11987.html | `1629:12013` | `height:44px;` |
| job-listing-page-1629-11987.html | `1629:12556` | `left:16px; top:178px; width:328px; height:135px;` |
| job-listing-page-1629-11987.html | `1629:12557` | `gap:9px; align-items:center;` |
| job-listing-page-1629-11987.html | `1629:12559` | `gap:6px; width:196px;` |
| job-listing-page-1629-11987.html | `1629:12562` | `gap:6px; width:112px; align-items:flex-end;` |
| job-listing-page-1629-11987.html | `1629:12564` | `padding:4px 12px;` |
| job-listing-page-1629-11987.html | `1629:12573` | `gap:4px;` |
| job-listing-page-1629-11987.html | `1629:12574` | `height:24px;` |
| job-listing-page-1629-11987.html | `1629:12578` | `width:112px;` |
| job-listing-page-1629-11987.html | `1629:12101` | `left:16px; top:325px; width:328px; height:162px;` |
| job-listing-page-1629-11987.html | `1629:12102` | `height:162px;` |
| job-listing-page-1629-11987.html | `1629:12117` | `gap:12px;` |
| job-listing-page-1629-11987.html | `1629:12119` | `gap:4px;` |
| job-listing-page-1629-11987.html | `1629:12133` | `gap:4px; width:304px;` |
| job-listing-page-1629-11987.html | `1629:12134` | `height:24px;` |
| job-listing-page-1629-11987.html | `1629:12138` | `width:112px;` |
| job-listing-page-1629-11987.html | `1629:12178` | `left:16px; top:499px; width:328px; height:162px;` |
| job-listing-page-1629-11987.html | `1629:12179` | `height:162px;` |
| job-listing-page-1629-11987.html | `1629:12194` | `gap:12px;` |
| job-listing-page-1629-11987.html | `1629:12196` | `gap:4px;` |
| job-listing-page-1629-11987.html | `1629:12210` | `gap:4px; width:304px;` |
| job-listing-page-1629-11987.html | `1629:12211` | `height:24px;` |
| job-listing-page-1629-11987.html | `1629:12217` | `width:13px;` |
| job-listing-page-1629-11987.html | `1629:12257` | `left:16px; top:673px; width:328px; height:162px;` |
| job-listing-page-1629-11987.html | `1629:12258` | `height:162px;` |
| job-listing-page-1629-11987.html | `1629:12273` | `gap:12px;` |
| job-listing-page-1629-11987.html | `1629:12275` | `gap:4px;` |
| job-listing-page-1629-11987.html | `1629:12289` | `gap:4px; width:304px;` |
| job-listing-page-1629-11987.html | `1629:12290` | `height:24px;` |
| job-listing-page-1629-11987.html | `1629:12294` | `width:112px;` |

Inline style elements: 510.

### Literal values in sample-screen.css (rule → node id)

| Selector | Literal declarations | Node id(s) |
|---|---|---|
| `.scr-page` | `margin: 0; padding: 24px` | shared helper (no single node) |
| `.scr-frame` | `margin: 0 auto` | shared helper (no single node) |
| `.scr-frame p` | `margin: 0` | shared helper (no single node) |
| `.scr-sr-only` | `inline-size: 1px; block-size: 1px; clip-path: inset(50%)` | shared helper (no single node) |
| `.scr-asset` | `outline: 1px dashed var(--annachy-color-border-primary); outline-offset: -1px` | shared helper (no single node) |
| `.scr-asset[data-stroke]` | `outline: 0; border-top: 1px dashed var(--annachy-color-border-primary)` | shared helper (no single node) |
| `.scr-fill` | `flex: 1 0 0; min-inline-size: 1px` | shared helper (no single node) |
| `.scr-t-8-12` | `font-size: 8px; line-height: 12px` | shared helper (no single node) |
| `.scr-t-10-14` | `font-size: 10px; line-height: 14px` | shared helper (no single node) |
| `.scr-t-12-16` | `font-size: 12px; line-height: 16px` | shared helper (no single node) |
| `.scr-t-12-17` | `font-size: 12px; line-height: 17px` | shared helper (no single node) |
| `.scr-t-12-18` | `font-size: 12px; line-height: 18px` | shared helper (no single node) |
| `.scr-t-13-18` | `font-size: 13px; line-height: 18px` | shared helper (no single node) |
| `.scr-t-14-18` | `font-size: 14px; line-height: 18px` | shared helper (no single node) |
| `.scr-t-14-20` | `font-size: 14px; line-height: 20px` | shared helper (no single node) |
| `.scr-t-14-n` | `font-size: 14px; line-height: normal` | shared helper (no single node) |
| `.scr-t-15-24` | `font-size: 15px; line-height: 24px` | shared helper (no single node) |
| `.scr-t-16-18` | `font-size: 16px; line-height: 18px` | shared helper (no single node) |
| `.scr-t-16-20` | `font-size: 16px; line-height: 20px` | shared helper (no single node) |
| `.scr-t-16-21` | `font-size: 16px; line-height: 21px` | shared helper (no single node) |
| `.scr-t-16-24` | `font-size: 16px; line-height: 24px` | shared helper (no single node) |
| `.scr-t-18-20` | `font-size: 18px; line-height: 20px` | shared helper (no single node) |
| `.scr-t-18-25` | `font-size: 18px; line-height: 25px` | shared helper (no single node) |
| `.scr-t-20-24` | `font-size: 20px; line-height: 24px` | shared helper (no single node) |
| `.scr-t-24-n` | `font-size: 24px; line-height: normal` | shared helper (no single node) |
| `.scr-t-28-36` | `font-size: 28px; line-height: 36px` | shared helper (no single node) |
| `.scr-t-48-58` | `font-size: 48px; line-height: 58px` | shared helper (no single node) |
| `.scr-c-black` | `color: #000` | `1629:12561`, `1627:11800` |
| `.scr-c-141414` | `color: #141414` | `1629:11995` |
| `.scr-c-737373` | `color: #737373` | `1629:11999`, `1627:11768` |
| `.scr-c-011425` | `color: #011425` | `1375:30962`, `1375:30982`, `1375:31224` |
| `.scr-c-202631` | `color: #202631` | `1375:31006` |
| `.scr-ios-status` | `inset-block-start: 0; inset-inline-start: 0; inline-size: 360px; block-size: 48px; padding: 16px 20px 16px 35px; background: #fff` | `1627:11941` |
| `.scr-ios-status__time` | `font-size: 14px; line-height: normal; color: #000` | `I1627:11941;179:118` |
| `.scr-ios-status__icons` | `gap: 8.5px` | `I1627:11941;179:296` |
| `.scr-ops` | `inline-size: 360px; block-size: 800px; background: #fff` | `1627:11756`, `1629:11987` |
| `.scr-ops-head` | `gap: 16px` | `1627:11757` |
| `.scr-ops-head__left` | `gap: 8px; inline-size: 168px` | `1627:11759` |
| `.scr-ops-back` | `inline-size: 40px; block-size: 40px; padding: 7px 8px 9px; border: 1px solid #ebebeb` | `1627:11760` |
| `.scr-ops-head__titles` | `gap: 4px; flex: 1 0 0; min-inline-size: 1px` | `1627:11763` |
| `.scr-ops-head__right` | `gap: 8px` | `1629:12000` |
| `.scr-ops-iconbtn` | `inline-size: 32px; block-size: 32px; padding: 8px` | `1629:12001` |
| `.scr-ops-avail` | `gap: 4px; block-size: 40px; padding: 4px 8px; background: #fff; border: 1px solid #ebebeb; border-radius: 84px` | `1629:12005` |
| `.scr-ops-ls-1875` | `letter-spacing: 0.1875px` | `1629:11995` |
| `.scr-ops-ls-1641` | `letter-spacing: 0.1641px` | `1629:11999` |
| `.scr-ops-ls-1523` | `letter-spacing: 0.1523px` | `1629:12560` |
| `.scr-ops-ls-1406` | `letter-spacing: 0.1406px` | `1629:12008` |
| `.scr-ops-tabs` | `gap: 8px` | `1629:12013` |
| `.scr-ops-tab` | `padding: 12px; border-radius: 30px` | `1629:12016` |
| `.scr-ops-tab--active` | `background: #f5f4ff; color: #4338ca` | `1629:12014` |
| `.scr-ops-tab--d1d5db` | `border: 1px solid #d1d5db; color: #737373` | `1629:12016` |
| `.scr-ops-tab--f2f2f2` | `border: 1px solid #f2f2f2; color: #737373` | `1629:12020` |
| `.scr-ops-summary` | `gap: 20px; padding: 8px 10px; background: #fff; border: 1px solid #e2e2e2` | `1629:12556` |
| `.scr-ops-card` | `gap: 8px; padding: 11px; background: #fff; border: 1px solid #d4d4d4; inline-size: 328px` | `1629:12102` |
| `.scr-ops-pill` | `padding: 6px 12px; border-radius: 30px` | `1629:12106` |
| `.scr-ops-pill--progress` | `background: #4338ca; color: #fff` | `1629:12106` |
| `.scr-ops-pill--idle` | `background: #f3f3f3; color: #000` | `1629:12183` |
| `.scr-ops-progress` | `block-size: 12px; background: rgba(95, 97, 97, 0.08); border-radius: 33554400px` | `1629:12577` |
| `.scr-ops-progress__bar` | `block-size: 12px; border-radius: 99px; background: #4338ca` | `1629:12578` |
| `.scr-ops-bin` | `gap: 12px; padding: 11px; background: #fff; border: 1px solid #d4d4d4` | `1627:11841`, `1627:11796` |
| `.scr-ops-c-22c55e` | `color: #22c55e` | `1627:11801` |
| `.scr-ops-thumb` | `inline-size: 60px; block-size: 60px; background: #f5f5f5` | `1627:11858` |
| `.scr-ops-qty` | `gap: 10px` | `1627:11931` |
| `.scr-ops-qty__step` | `gap: 2px; block-size: 56px; padding: 10px 12px; background: #f2f2f2` | `1627:11932` |
| `.scr-ops-qty__value` | `block-size: 56px; padding: 10px 12px; border: 1px solid #d4d4d4; flex: 1 0 0; min-inline-size: 1px` | `1627:11935` |
| `.scr-ops-footer` | `background: #691f1f` | `1627:11986` |
| `.scr-ops-action` | `inline-size: 328px; block-size: 56px; padding: 10px 20px; background: #142333; border: 0; color: #fff; filter: drop-shadow(0 1px 1px rgba(0, 0, 0, 0.05))` | `1627:11940` |
| `.scr-mpdp` | `inline-size: 360px; block-size: 4683px` | `1608:7090` |
| `.scr-mstatus` | `padding: 0 16px 10px` | `1608:7094` |
| `.scr-mstatus__icons` | `inline-size: 46px; block-size: 18px` | `1608:7100` |
| `.scr-mnav` | `padding: 8px 16px; background: #fff; border-bottom: 1px solid #e0e2e4` | `1608:7112` |
| `.scr-mnav__icon` | `inline-size: 42px; block-size: 42px` | `1608:7113` |
| `.scr-mbonus` | `padding: 4px; border: 1px solid #d17515; background-image: linear-gradient(108.78deg, rgb(220, 104, 3) 98.385%, rgb(249, 174, 60) 179.9%)` | `1608:7140` |
| `.scr-mcolour-card` | `inline-size: 75px; block-size: 139px; border-radius: 6px; background: #f0f2f3; border: 1px solid rgba(235, 237, 238, 0.6)` | `I1608:7152;1539:30180` |
| `.scr-mcolour-card--active` | `border-color: #131415; box-shadow: 0 0 3px 0 rgba(0, 0, 0, 0.01), 0 0 3px 0 rgba(0, 0, 0, 0.04), 0 0 2px 0 rgba(0, 0, 0, 0.15), 0 0 2px 0 rgba(0, 0, 0, 0.26), 0 0 1px 0 rgba(0, 0, 0, 0.29)` | `I1608:7152;1539:30179` |
| `.scr-mcolour-card__info` | `inset-inline-start: 0; inset-block-end: 0; inline-size: 75px; padding: 4px 8px 8px; background: #fff; border-top: 1px solid #eeeded` | `1010:21647` |
| `.scr-mcolour-card__badge` | `inset-inline-start: -1px; inset-block-start: 83px; inline-size: 75px; block-size: 16px; padding: 2px 8px; background: #027a48` | `1010:21645` |
| `.scr-msize` | `block-size: 56px; min-inline-size: 56px; padding: 10px 12px; border: 1px solid rgba(172, 177, 180, 0.5); border-radius: 6px` | `I1608:7153;1546:27123;1546:26984` |
| `.scr-msize--oos` | `border-color: #f0f0f0` | `1546:27436` |
| `.scr-msize__oos` | `inset-inline-start: -1px; inset-block-start: 39px; inline-size: 57px; block-size: 16px; padding: 10px 8px; background: #b42318; border-top: 1px solid rgba(251, 195, 191, 0.86)` | `1546:27405` |
| `.scr-mdelivery-anim` | `inline-size: 360px; block-size: 38px; background-image: linear-gradient(3.49deg, rgb(58, 111, 247) 13.397%, rgb(23, 70, 162) 86.603%)` | `1608:7156` |
| `.scr-mperks` | `gap: 24px; padding: 24px 16px; background-image: linear-gradient(to bottom, #005aaa 960.47%, #fafdff 50.213%)` | `1608:7183` |
| `.scr-mperk` | `gap: 16px; block-size: 45px` | `1608:7184` |
| `.scr-mtile` | `inline-size: 42px; block-size: 42px; border: 1px solid #def0ff; border-radius: 9px; background-image: linear-gradient(162.86deg, rgb(220, 238, 253) 18.401%, rgb(240, 248, 255) 88.214%)` | `1608:7185` |
| `.scr-mlab` | `gap: 8px; inline-size: 170px` | `1608:7248` |
| `.scr-mlab--first` | `margin-inline-end: -12px` | `1608:7248` |
| `.scr-mlab__head` | `gap: 4px; block-size: 34px; padding: 0 8px; background: #f5faff` | `I1608:7248;1548:30745` |
| `.scr-mlab__desc` | `padding: 0 6px` | `I1608:7248;1548:30752` |
| `.scr-mtab-dark` | `block-size: 36px; padding: 10px 12px` | `1608:7277` |
| `.scr-mspec` | `gap: 4px; inline-size: 172px` | `1608:7284` |
| `.scr-mspec__bullet` | `margin: 0; padding-inline-start: 21px` | `1608:7285` |
| `.scr-mspec__value` | `padding: 0 6px 6px; border-bottom: 1px dashed #e5e7e8` | `1608:7286` |
| `.scr-mrev-badge` | `gap: 16px; padding-inline-end: 10px; background: #fff; border: 1px solid #f3f4f4; border-radius: 6px` | `1608:7356` |
| `.scr-mrev-score` | `gap: 4.453px; block-size: 35px; padding: 4px 8px; background: #027a48; border-radius: 6px 0 0 6px` | `1608:7357` |
| `.scr-mrev-media` | `border: 1px solid #f1f1f1; border-radius: 6px` | `1608:7366` |
| `.scr-mrev-overlay` | `background: rgba(22, 24, 25, 0.8)` | `1608:7372` |
| `.scr-mrev-chip` | `gap: 6px; block-size: 26px; padding: 2px 6px; border: 1px solid #f3f4f5` | `I1608:7387;1321:18887` |
| `.scr-mrev-chip__bar` | `inset-inline-start: -1px; inset-block-start: 22px; block-size: 2px; background: #027a48` | `1321:18890` |
| `.scr-mrev-chip__bar--low` | `background: #e6190a` | `1321:18898` |
| `.scr-mrev-avatar` | `inline-size: 24px; block-size: 24px; padding: 10px; border-radius: 50px; background: #005aaa` | `1321:18913` |
| `.scr-mrev-helpful` | `gap: 4px; padding: 4px 10px; border: 1px solid #f3f4f5` | `1363:26813` |
| `.scr-mtrust` | `block-size: 122px; padding: 20px 16px; border: 1px solid #d7ebfb; background-image: linear-gradient(to bottom, #fff 960.47%, #f6fbff 84.016%)` | `1608:7392` |
| `.scr-mbrand` | `gap: 20px; padding: 16px; background: rgba(252, 252, 253, 0.98)` | `1608:7410` |
| `.scr-msimilar` | `gap: 18px; padding: 24px 16px; border-top: 1px solid #e4f2fd; background-image: linear-gradient(to bottom, #f5faff 3.445%, #f7fbff 360.96%)` | `1608:7425` |
| `.scr-mcard` | `gap: 8px; inline-size: 172px` | `1608:7431` |
| `.scr-mcard__media` | `block-size: 240px; border-radius: 6px` | `1608:7432` |
| `.scr-mcard__review` | `inset-inline-start: 0; inset-block-end: 0; inline-size: 172px; padding: 15px 10px` | `1608:7434` |
| `.scr-mcard__rbt` | `background: #eff1f0; border: 1px solid #d0d1d2; border-radius: 5px` | `1608:7435` |
| `.scr-mcard__rscore` | `gap: 2px; padding: 4px 6px; background: #027a48; border: 1px solid #d0d1d2; border-radius: 5px` | `1608:7436` |
| `.scr-mcard__rcount` | `padding: 4px 4px 4px 2px; background: #eff1f0` | `1608:7440` |
| `.scr-watch` | `padding: 0; background: #fafdff; border: 0.68px solid #edeff0; border-radius: 6px; box-shadow: 0 0 3px 0 rgba(0, 0, 0, 0.01), 0 0 3px 0 rgba(0, 0, 0, 0.05), 0 0 2px 0 rgba(0, 0, 0, 0.18)` | `1608:7443` |
| `.scr-mcard__body` | `gap: 7px; padding: 0 3px` | `1608:7444` |
| `.scr-mcard__cta-alt` | `block-size: 38px; padding: 14px 24px; border: 1px solid #3196ef; background-image: linear-gradient(174.77deg, rgb(0, 90, 170) 11.116%, rgb(56, 153, 239) 299.83%); filter: drop-shadow(0 9px 1px rgba(14, 105, 186, 0)) drop-shadow(0 6px 1px rgba(14, 105, 186, 0.01)) drop-shadow(0 3px 1px rgba(14, 105, 186, 0.05)) drop-shadow(0 1px 0.5px rgba(14, 105, 186, 0.09)) drop-shadow(0 0 0.5px rgba(14, 105, 186, 0.1))` | `I1608:7526;1471:36895` |
| `.scr-mnew` | `gap: 18px; padding: 24px 16px; border-top: 1px solid #e4f2fd` | `1608:7530` |
| `.scr-mnew__tile` | `inline-size: 38px; block-size: 38px` | `1608:7533` |
| `.scr-mcoll` | `inline-size: 195px; block-size: 259px; border-radius: 6px` | `1608:7563` |
| `.scr-mcoll__img` | `background: #fff; border: 1px solid #edeff0; border-radius: 6px` | `I1608:7550;1519:25227` |
| `.scr-mcoll__label` | `inset-inline-start: 0; inline-size: 125px; block-size: 28px; padding: 8px 6px; border-radius: 6px 6px 0 0` | `I1608:7550;1519:26199` |
| `.scr-mcoll__label--blue` | `background: #005aaa` | `I1608:7550;1519:26199` |
| `.scr-mcoll__label--gold` | `background: radial-gradient(66px 66px at 63px 4.5px, rgb(255, 234, 193) 0%, rgb(255, 222, 159) 50%, rgb(255, 210, 124) 100%)` | `I1608:7563;1519:26199` |
| `.scr-mcoll__label--pale` | `background: radial-gradient(104px 104px at 63px 4.5px, rgb(246, 246, 246) 0%, rgb(255, 234, 193) 100%)` | `I1608:7576;1519:26199` |
| `.scr-mbottom` | `padding: 32px 16px 26px; background: #fff; border-top: 1px solid rgba(153, 159, 163, 0.2); filter: drop-shadow(-1px -3px 0.5px rgba(24, 25, 26, 0)) drop-shadow(-1px -2px 0.5px rgba(24, 25, 26, 0.01)) drop-shadow(0 -1px 0.5px rgba(24, 25, 26, 0.02))` | `1608:7590` |
| `.scr-dpdp` | `inline-size: 1440px; block-size: 3533px` | `1375:30858` |
| `.scr-dhead` | `filter: drop-shadow(0 0 0.5px rgba(0, 0, 0, 0)) drop-shadow(0 0 0.5px rgba(0, 0, 0, 0.01)) drop-shadow(0 0 0.5px rgba(0, 0, 0, 0.05)) drop-shadow(0 0 0.5px rgba(0, 0, 0, 0.09))` | `1375:31289` |
| `.scr-dhead__top` | `block-size: 100px; padding: 0 120px` | `1375:31290` |
| `.scr-dhead__bottom` | `block-size: 80px; padding: 0 120px; border-bottom: 1px solid rgba(108, 156, 199, 0.1)` | `1375:31366` |
| `.scr-dgal-tile` | `inline-size: 268.259px; block-size: 367.091px; background: #d9d9d9; border: 2.383px solid #eff7fe; border-radius: 6.354px` | `1375:30862` |
| `.scr-dsize` | `inline-size: 62px; block-size: 62px; padding: 20px 23px; border: 1px solid var(--annachy-color-border-primary)` | `1375:30986` |
| `.scr-dwish` | `flex: 1 0 0; min-inline-size: 1px; block-size: 62px; padding: 20px 23px; border: 1px solid var(--annachy-color-border-primary)` | `1375:31001` |
| `.scr-dswatch` | `gap: 12px; inline-size: 100px; padding: 2.5px 4.5px; border: 1.5px solid` | `1375:30959` |
| `.scr-dswatch__img` | `block-size: 100px; background: #034784` | `1375:30964` |
| `.scr-doffer` | `gap: 8px; padding: 16px 18px; border: 1px solid var(--annachy-color-blue-grey-100)` | `1375:31009` |
| `.scr-dperk` | `gap: 12px; inline-size: 100px` | `1375:31049` |
| `.scr-dperk__icon` | `inline-size: 60px; block-size: 60px; border: 1px solid var(--annachy-color-blue-white-300); border-radius: 40px` | `1375:31050` |
| `.scr-dfeature` | `gap: 24px; padding: 16px 0; border-bottom: 1px solid #e2e5e9` | `1375:31092` |
| `.scr-dlink` | `gap: 4px; padding: 12px 10px` | `1375:31155` |
| `.scr-drating` | `gap: 40px; padding: 32px; border: 1px solid var(--annachy-color-border-secondary)` | `1375:31168` |
| `.scr-dbar` | `flex: 1 0 0; min-inline-size: 1px; block-size: 6px; border-radius: 3px` | `1375:31181` |
| `.scr-dbar__fill` | `block-size: 6px; border-radius: 3px` | `1375:31182` |
| `.scr-dc-045dad` | `color: #045dad` | `1375:31226` |
| `.scr-drelated` | `inline-size: 250px; block-size: 320px; background: #044f92` | `1375:31230` |
| `.scr-d2` | `inline-size: 1440px; block-size: 1073px` | `1608:9891` |

## R11 product imagery (2026-11-20)

Image placeholders marked `data-annachy-image` show the **original Figma images** from `../assets/images/`. These are byte-identical copies, approved
for **internal reproduction only**, and their rights are unverified (see that folder's README and `data-img-rights`). The crops, offsets,
stacked colour variants and instance scaling are Figma's own, converted from the design context. Do not publish these screens with the images
until the rights are resolved. Mapping: `docs/figma-audit/r11-0-product-imagery-manifest.json`.
