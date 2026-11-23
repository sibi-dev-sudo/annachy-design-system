# Screens — ② PDP (Figma page `581:11523`)

Static HTML/CSS reproductions of the product-detail-page frames from file `rM3ixSG6i3DFfKZFWuxzs4`.
Each page links `../../../src/annachy.css` (library) and `./pdp.css` (screen styles, class prefix `scr-`).
Each frame root carries `data-figma-node` and is sized exactly to the Figma frame. Every reproduced layer carries
its Figma node id in `data-figma-node`.

## Frames

| Figma frame | File | Status |
|---|---|---|
| `605:17532` Desktop /BG Colours, 1440×1024 | `desktop-bg-colours.html` | **complete**. The frame is one screenshot image plus one yellow "Button 26" label frame; the screenshot is a placeholder. |
| `1171:9676` Mobile, 360×1536 | `mobile.html` | **complete** |
| `1280:10398` PDP V1, 393×4683 (latest iteration) | `pdp-v1.html` | **complete**, with the limits listed under "Not reproduced / unverified" below |
| `1214:11887` PDP V1, 393×4388 | — | **superseded** by `1280:10398` (see below) |
| `1218:13662` PDP V1, 393×4388 | — | **superseded** by `1280:10398` (see below) |

### Superseded iterations (compared using the saved metadata only, no Figma calls)

`1214:11887` and `1218:13662` are near-identical to each other. Both differ from `1280:10398` structurally, not just in minor ways:

| Area | 1214:11887 / 1218:13662 | 1280:10398 (reproduced) |
|---|---|---|
| Frame height | 4388 | 4683 |
| Side buttons (`…:11898` / `…:13673`) | "Icons Frame" with *Share* icon on top, Watchlist button below | Watchlist button on top, an `All Buttons` icon-only instance below (`1283:2695`) |
| Product info block | 361×156 (title 24 tall, price frame 246 wide) / 361×144 | 361×132 (title 21, price frame 226) |
| Variants block | colour tabs 177 / 178 tall, sizes 94 / 92 | 172, 92 |
| Delivery details | custom frame `Frame 2121454286` (362×90 / 88): *Map Point* icon, address and a "Change" link | library **Input Field / Outline** instance `1280:10448` (360×71) |
| Delivery block y / height | 1152, 146 / 144 | 1111, 127 |
| Top Highlights | 361×378 / 380 (collapsed) | 361×632 (expanded, "See Less") |
| Product Information | 361×988 | 361×1301 (spec grid expanded, Rating & Reviews block) |
| Content wrapper | 393×2516 | 393×3081 |
| Bottom nav | plain instance (`1214:12125`) / detached frame (`1242:19319`) | detached frame `1280:10763` with library buttons |

These two frames were not reproduced: they are earlier versions of the same screen, and `1280:10398` replaces them.

## Components reused (from `src/components/*`)

| Library component | Used for (Figma node) | Markup |
|---|---|---|
| Button (`All Buttons` 887:2492) | `1283:2695` secondary-grey 40, Hover, icon-only; `1280:10535`, `1280:10615` secondary 32 "See Less"; `1280:10546` primary 36 (fill overridden to Brand/Base/Black, see below); `1280:10547` secondary-grey 36; `1280:10548` secondary-grey 36 Disabled; `1280:10657` secondary 46 "See More"; `1280:10697` secondary 38 icon-only; `1281:7303` etc. secondary 36 "Add To Cart" (×7); `1280:10768` secondary 48 "Buy Now" | `.annachy-button` + type + size classes; widths fixed to the Figma instance width |
| Button gradient (`Button` 1153:3370) | `1280:10769` size 48 "Add To Cart" | `.annachy-button-gradient--size-48`, width 203 |
| Input Field / Outline (1066:37962) | `1280:10448` Size 46, Radius 4, value entered | `.annachy-input--outline --size-46 --radius-4` |

Instance overrides that are reproduced in `pdp.css` (scoped under the screen classes, not changing the library):
- `1280:10448`: the Top Section hugs its content with gap 7 (the library default is a fixed Size + 42, IN-12). Label colour is Brand/Blue-Black/500 and the field border is Brand/Base/Black. The instance is clipped at 360×71.
- `1280:10546`: the fill is Brand/Base/Black (`--annachy-color-base-black`) on the Primary type.
- `1283:2695`: the instance is 40 wide with padding 12.

Checkbox, Radio, Toggle, Dropdown and Tooltip do not appear in these frames.

## Fonts and heights

All text uses `var(--annachy-base-font-family-render)` (Proxima Nova is not available). The Mobile frame also uses Inter in
`1201:9799`, `1201:9803` and `1201:9834`; those render in the same stack. Text widths therefore differ from Figma.
Every section, row and card has its Figma height set explicitly, so frame and section heights match Figma exactly
(0px difference in the check). Text that needs more room with the fallback font is clipped or ellipsised inside its
Figma box instead of pushing the layout.

## Not reproduced / unverified

- **PDP V1 root fill.** `get_design_context` was not called on the whole 393×4683 frame (budget), so the root fill is
  not confirmed. It uses `--annachy-color-background-primary`, the fill of the sibling Mobile frame. The wrapper frames
  `1280:10506/10507/10508/10509` have no fill (also not confirmed).
- **Vector line colours.** `Line 137/142/143` (`1280:10541`, `1280:10632`, `1280:10658`, `1280:10659`, the section-header
  lines) and the strike-through `Line 122` (MRP prices) were returned only as SVG assets. They are drawn as 1px lines in
  `#e5e7e8` (the `1280:10539` border colour) and `currentColor` respectively. **The colours are unverified.**
- **Decorative "air" streaks.** These are small gradient bars at 15% opacity: `I1280:10449;1546:27833/27836/27839` in the
  Delivery Animation and `I1280:10723;1519:26185/26188/26192` on the blue collection label. They are omitted.
- **Gradient stop order.** `1280:10450` and `1280:10661` have Figma stops listed in descending position (e.g. `#005aaa`
  at 960.47%, `#fafdff` at 50.213%). CSS needs ascending stops, so the same stops are written in ascending order.
- **Similar-product cards.** Cards `1280:10699`–`1280:10702` sit at x ≥ 558 inside a 361-wide row, so they are clipped by the
  frame, as in Figma. Card `1281:7311` is 371 tall in Figma but renders 360 tall here (same content as the other cards).
- **Rating bar width.** `1280:10625` is 261.45 wide in Figma; here it is content-sized and depends on the fallback font.
  Its width is not checked.
- **Placeholder ids.** Some placeholders sit inside component instances whose inner layer ids were not returned
  (library-button icon slots, similar-card images/stars/hearts, the review card). Their `data-figma-node` is
  the instance id plus a role suffix (e.g. `1281:7272 image`, `1280:10546 left-icon`), not a real Figma layer id.
- **Placeholder styling.** Image placeholders use the Background/Tertiary token as a fill. Icon placeholders use a 1px
  inset Border/Secondary outline. Both are placeholder chrome only, not Figma values.

## Non-colour literal values (no R1 token)

| Value | Where (node) |
|---|---|
| radius 9px | icon boxes `1280:10452`, `1280:10663`, `1280:10680`, `1280:10706` |
| radius 6px | `scr-vcard` `I1280:10445;1539:30180`, `scr-size` `1546:26984`, media tiles `1280:10635`, similar card media `1281:7274`, collection tiles/labels `1519:25227`, `1519:26199`, Rating Card, review score `6.679px` |
| radius 5px | Review BT `1281:7277` |
| radius 10px / 12px | Mobile / Desktop frame strokes `1171:9676`, `605:17532` (12 equals `--annachy-radius-12` but is the frame corner, kept literal) |
| radius 50px / 100px | avatar (`1280:10656`), home indicators `1171:9679`, `1280:10766` |
| font 15px/24px regular | MRP `1280:10430` |
| font 14px/14px bold; letter-spacing 0.42px | Mobile review score `1201:9799`; bonus text `1201:9834` |
| border 0.68px / 0.85px / 1.113px | `Watchlist/Small Button` `1281:7285`, `Watchlist/ Width Big Button` `I1280:10723;1519:26498`, review score `1280:10656` |
| gradient angles 110.403°, 108.673°, 3.187°, 162.860° | `1280:10433`, `1201:9826`, `1280:10449`, icon boxes |
| radial label gradients (r 66 / 104 at 63,4.5) | `I1280:10736;1519:26199`, `I1280:10749;1519:26199` (from the SVG gradientTransform) |

## Figma calls made (16 total; all read-only)

| # | Tool | Node |
|---|---|---|
| 1 | get_design_context (excludeScreenshot) | `605:17532` Desktop /BG Colours |
| 2 | get_design_context (excludeScreenshot) | `1171:9676` Mobile |
| 3 | get_design_context (excludeScreenshot) | `1280:10770` TOP NAV |
| 4 | get_design_context (excludeScreenshot) | `1280:10400` like + review row |
| 5 | get_design_context (excludeScreenshot) | `1280:10409` side buttons |
| 6 | get_design_context (excludeScreenshot) | `1280:10418` product info |
| 7 | get_design_context (excludeScreenshot) | `1280:10399` YL hero |
| 8 | get_design_context (excludeScreenshot) | `1280:10444` colours + sizes |
| 9 | get_design_context (excludeScreenshot) | `1280:10447` delivery |
| 10 | get_design_context (excludeScreenshot) | `1280:10450` services |
| 11 | get_design_context (excludeScreenshot) | `1280:10510` Top Highlights |
| 12 | get_design_context (excludeScreenshot) | `1280:10763` Bottom Nav Bar |
| 13 | get_design_context (excludeScreenshot) | `1280:10660` assurances + brand |
| 14 | get_design_context (excludeScreenshot) | `1280:10536` Product Information |
| 15 | get_design_context (excludeScreenshot) | `1280:10694` Similar Products |
| 16 | get_design_context (excludeScreenshot) | `1280:10703` New Collections |

get_metadata: 0 calls (the saved `docs/figma-audit/raw/metadata/581-11523.xml` was used). get_variable_defs: 0 calls.
No asset URLs were fetched or referenced.

## Validation

`tests/fixtures/screens-pdp-check.html` (run `python -I tests/tools/browser_check.py screens-pdp-check.html`) checks:
- the root size of each frame;
- position and size of 76 sections, rows and cards against the metadata (tolerance 1px; no height tolerance was needed);
- the stylesheet links;
- that every placeholder is empty and typed, and that no `img`/`svg` element or Figma asset URL is present.

Result: **PASS — 303 checks, 0 failures.**

## Placeholder assets

| File | Node id | Layer name (title) | Size (px) | Kind |
|---|---|---|---|---|
| desktop-bg-colours.html | `605:17525` | Screenshot 2026-09-23 at 4.46.29 PM 1 | 1440 × 931 | image |
| mobile.html | `1201:9772` | Image | 394.9613952636719 × 526 | image |
| mobile.html | `1171:9682` | Phone Camara | 18 × 18 | icon |
| mobile.html | `1171:9687` | Wifi | 17 × 18 | icon |
| mobile.html | `1171:9692` | Signal | 17 × 18 | icon |
| mobile.html | `1171:9695` | Battery | 8 × 15.882352828979492 | icon |
| mobile.html | `1201:9776` | Line Duotone / Arrows / Alt Arrow Left | 28 × 28 | icon |
| mobile.html | `1201:9780` | Linear / Search / Magnifer | 24 × 24 | icon |
| mobile.html | `1201:9784` | Outline / Shopping, Ecommerce / Cart Large 2 | 28 × 28 | icon |
| mobile.html | `1201:9789` | Linear / Like / Heart | 28 × 28 | icon |
| mobile.html | `1201:9800` | Star | 16 × 16 | icon |
| mobile.html | `1201:9812` | Line Duotone / Arrows / Alt Arrow Left (rotated) | 16 × 16 | icon |
| mobile.html | `1201:9829` | loyalty 1 [Vectorized] | 24 × 24 | icon |
| mobile.html | `1201:9835` | Line Duotone / Arrows / Alt Arrow Left (rotated) | 20 × 20 | icon |
| pdp-v1.html | `1280:10399` | YL (product image instance; inner Image I1280:10399;1486:38899 394x524) | 393 × 525 | image |
| pdp-v1.html | `1280:10402` | Linear / Like / Heart | 28 × 28 | icon |
| pdp-v1.html | `I1280:10408;1528:26138;1523:25927` | Star | 16 × 16 | icon |
| pdp-v1.html | `I1280:10417;1508:24970` | Linear / Like / Heart | 28 × 28 | icon |
| pdp-v1.html | `1283:2695 left-icon` | Home/Home 54 (Icon Size=S, Style=Outline) 1777:12415 | 20 × 20 | icon |
| pdp-v1.html | `1283:2695 right-icon` | Home/Home 54 (Icon Size=S, Style=Outline) 1777:12415 | 20 × 20 | icon |
| pdp-v1.html | `1280:10422` | Line Duotone / Arrows / Alt Arrow Left (rotated) | 20 × 20 | icon |
| pdp-v1.html | `1280:10436` | loyalty 1 [Vectorized] | 24 × 24 | icon |
| pdp-v1.html | `1280:10442` | Line Duotone / Arrows / Alt Arrow Left (rotated) | 20 × 20 | icon |
| pdp-v1.html | `I1280:10445;1539:30179;1539:28349` | Component 102 / YL (Yellow) | 75.969 × 101.292 | image |
| pdp-v1.html | `I1280:10445;1539:30180;1539:28349` | Component 102 / YL (Green) | 75.969 × 101.292 | image |
| pdp-v1.html | `I1280:10445;1539:30181;1539:28349` | Component 102 / YL (Blue) | 75.969 × 101.292 | image |
| pdp-v1.html | `I1280:10445;1539:30182;1539:28349` | Component 102 / Component 103 / YL | 75.969 × 101.292 | image |
| pdp-v1.html | `I1280:10446;1546:27139` | Line Duotone / Arrows / Alt Arrow Left (rotated) | 18 × 18 | icon |
| pdp-v1.html | `I1280:10446;1546:27123;1546:27436;1010:22241` | Line (diagonal strike, rotated 43.45 deg) | 57 × 54 | icon |
| pdp-v1.html | `1779:37533 (in I1280:10448)` | User/User Curved (Icon Size=M, Outline) | 24 × 24 | icon |
| pdp-v1.html | `1779:38814 (in I1280:10448)` | Arrow/Chevron Up (Icon Size=M, Filled) | 24 × 24 | icon |
| pdp-v1.html | `1779:39439 (in I1280:10448)` | Arrow/Chevron Down (Icon Size=M, Filled) | 24 × 24 | icon |
| pdp-v1.html | `1780:40128 (in I1280:10448)` | Alerts/Error circle (Icon Size=XS, Outline) | 16 × 16 | icon |
| pdp-v1.html | `I1280:10449;1546:27825` | Car (Group 1171275299) | 34.304 × 22 | icon |
| pdp-v1.html | `1280:10453` | Group 1171275304 (inset-positioned, approx. 32.7x24.5) | inset-positioned (see title / pdp.css) | icon |
| pdp-v1.html | `1280:10463` | Line Duotone / Arrows / Alt Arrow Left (rotated) | 24 × 24 | icon |
| pdp-v1.html | `1280:10467` | Group 1171275306 (inset-positioned, approx. 31x24.3) | inset-positioned (see title / pdp.css) | icon |
| pdp-v1.html | `1280:10482` | Line Duotone / Arrows / Alt Arrow Left (rotated) | 24 × 24 | icon |
| pdp-v1.html | `1280:10486` | Group 1171275306 (inset-positioned, approx. 31x24.3) | inset-positioned (see title / pdp.css) | icon |
| pdp-v1.html | `1280:10502` | Line Duotone / Arrows / Alt Arrow Left (rotated) | 18 × 18 | icon |
| pdp-v1.html | `1280:10504` | Line Duotone / Arrows / Alt Arrow Left (rotated) | 24 × 24 | icon |
| pdp-v1.html | `I1280:10517;1548:31174` | Icons / Group 1171275310 | 24 × 24 | icon |
| pdp-v1.html | `I1280:10518;1548:31174` | Icons / Group 1171275308 | 24 × 24 | icon |
| pdp-v1.html | `I1280:10520;1548:31174` | Icons / Group 1171275309 | 24 × 24 | icon |
| pdp-v1.html | `I1280:10521;1548:31174` | Icons / Group 1171275312 | 24 × 24 | icon |
| pdp-v1.html | `I1280:10523;1548:31174` | Icons / Group 1171275311 | 24 × 24 | icon |
| pdp-v1.html | `I1280:10524;1548:31174` | Icons / Group 1171275313 | 24 × 24 | icon |
| pdp-v1.html | `I1280:10527;1548:31174` | Icons / Group 1171275310 | 24 × 24 | icon |
| pdp-v1.html | `I1280:10528;1548:31174` | Icons / Group 1171275308 | 24 × 24 | icon |
| pdp-v1.html | `I1280:10530;1548:31174` | Icons / Group 1171275309 | 24 × 24 | icon |
| pdp-v1.html | `I1280:10531;1548:31174` | Icons / Group 1171275312 | 24 × 24 | icon |
| pdp-v1.html | `I1280:10533;1548:31174` | Icons / Group 1171275311 | 24 × 24 | icon |
| pdp-v1.html | `I1280:10534;1548:31174` | Icons / Group 1171275313 | 24 × 24 | icon |
| pdp-v1.html | `1280:10535 left-icon` | Home/Home 54 (Icon Size=S, Style=Outline) 1777:12415 | 20 × 20 | icon |
| pdp-v1.html | `1280:10535 right-icon` | Home/Home 54 (Icon Size=S, Style=Outline) 1777:12415 | 20 × 20 | icon |
| pdp-v1.html | `1280:10543 arrow` | Line Duotone / Arrows / Alt Arrow Left (rotated 90 deg) | 24 × 24 | icon |
| pdp-v1.html | `1280:10546 left-icon` | Home/Home 54 (Icon Size=S, Style=Outline) 1777:12415 | 20 × 20 | icon |
| pdp-v1.html | `1280:10546 right-icon` | Home/Home 54 (Icon Size=S, Style=Outline) 1777:12415 | 20 × 20 | icon |
| pdp-v1.html | `1280:10547 left-icon` | Home/Home 54 (Icon Size=S, Style=Outline) 1777:12415 | 20 × 20 | icon |
| pdp-v1.html | `1280:10547 right-icon` | Home/Home 54 (Icon Size=S, Style=Outline) 1777:12415 | 20 × 20 | icon |
| pdp-v1.html | `1280:10548 left-icon` | Home/Home 54 (Icon Size=S, Style=Outline) 1777:12415 | 20 × 20 | icon |
| pdp-v1.html | `1280:10548 right-icon` | Home/Home 54 (Icon Size=S, Style=Outline) 1777:12415 | 20 × 20 | icon |
| pdp-v1.html | `1280:10615 left-icon` | Home/Home 54 (Icon Size=S, Style=Outline) 1777:12415 | 20 × 20 | icon |
| pdp-v1.html | `1280:10615 right-icon` | Home/Home 54 (Icon Size=S, Style=Outline) 1777:12415 | 20 × 20 | icon |
| pdp-v1.html | `1280:10617 arrow` | Line Duotone / Arrows / Alt Arrow Left (rotated 90 deg) | 24 × 24 | icon |
| pdp-v1.html | `1280:10629` | Star | 18 × 18 | icon |
| pdp-v1.html | `1280:10636` | Frame 2121454585 (review photo) | 187 × 161 | image |
| pdp-v1.html | `1280:10640` | Product Image - 1 | 178 × 237 | image |
| pdp-v1.html | `1280:10643` | Gallery Minimalistic | 18 × 18 | icon |
| pdp-v1.html | `1280:10649` | Product Image -2 | 190 × 139 | image |
| pdp-v1.html | `1280:10652` | Outline / Video, Audio, Sound / Play Circle | 18 × 18 | icon |
| pdp-v1.html | `1280:10656 star` | Star | 17.811 × 17.811 | icon |
| pdp-v1.html | `1280:10656 like` | Outline / Like / Like | 18 × 18 | icon |
| pdp-v1.html | `1280:10657 left-icon` | Home/Home 54 (Icon Size=S, Style=Outline) 1777:12415 | 20 × 20 | icon |
| pdp-v1.html | `1280:10657 right-icon` | Home/Home 54 (Icon Size=S, Style=Outline) 1777:12415 | 20 × 20 | icon |
| pdp-v1.html | `1280:10664` | Outline / Users / Users Group Two Rounded (24x24) | inset-positioned (see title / pdp.css) | icon |
| pdp-v1.html | `1280:10669` | Linear / Security / Shield Check (24x24) | inset-positioned (see title / pdp.css) | icon |
| pdp-v1.html | `1280:10674` | Frame 2121454395 (genuine product badge, one vector) | 42 × 42 | icon |
| pdp-v1.html | `1280:10681` | Linear / Shopping, Ecommerce / Shop | 24 × 24 | icon |
| pdp-v1.html | `1280:10691` | Line Duotone / Arrows / Alt Arrow Left (rotated) | 24 × 24 | icon |
| pdp-v1.html | `1280:10697 left-icon` | Home/Home 54 (Icon Size=S, Style=Outline) 1777:12415 | 20 × 20 | icon |
| pdp-v1.html | `1280:10697 right-icon` | Home/Home 54 (Icon Size=S, Style=Outline) 1777:12415 | 20 × 20 | icon |
| pdp-v1.html | `1281:7272 image` | Similar Products - Images | 185 × 247 | image |
| pdp-v1.html | `1281:7272 star` | Star | 9.535 × 9.535 | icon |
| pdp-v1.html | `1281:7272 heart` | Linear / Like / Heart | 19.2 × 19.2 | icon |
| pdp-v1.html | `1283:2642 image` | Similar Products - Images | 185 × 247 | image |
| pdp-v1.html | `1283:2642 star` | Star | 9.535 × 9.535 | icon |
| pdp-v1.html | `1283:2642 heart` | Linear / Like / Heart | 19.2 × 19.2 | icon |
| pdp-v1.html | `1281:7311 image` | Similar Products - Images | 185 × 247 | image |
| pdp-v1.html | `1281:7311 star` | Star | 9.535 × 9.535 | icon |
| pdp-v1.html | `1281:7311 heart` | Linear / Like / Heart | 19.2 × 19.2 | icon |
| pdp-v1.html | `1280:10699 image` | Similar Products - Images | 185 × 247 | image |
| pdp-v1.html | `1280:10699 star` | Star | 9.535 × 9.535 | icon |
| pdp-v1.html | `1280:10699 heart` | Linear / Like / Heart | 19.2 × 19.2 | icon |
| pdp-v1.html | `1280:10700 image` | Similar Products - Images | 185 × 247 | image |
| pdp-v1.html | `1280:10700 star` | Star | 9.535 × 9.535 | icon |
| pdp-v1.html | `1280:10700 heart` | Linear / Like / Heart | 19.2 × 19.2 | icon |
| pdp-v1.html | `1280:10701 image` | Similar Products - Images | 185 × 247 | image |
| pdp-v1.html | `1280:10701 star` | Star | 9.535 × 9.535 | icon |
| pdp-v1.html | `1280:10701 heart` | Linear / Like / Heart | 19.2 × 19.2 | icon |
| pdp-v1.html | `1280:10702 image` | Similar Products - Images | 185 × 247 | image |
| pdp-v1.html | `1280:10702 star` | Star | 9.535 × 9.535 | icon |
| pdp-v1.html | `1280:10702 heart` | Linear / Like / Heart | 19.2 × 19.2 | icon |
| pdp-v1.html | `1280:10707` | Linear / Arrows / Arrow Right | 24 × 24 | icon |
| pdp-v1.html | `I1280:10723;1519:25227 (slot fill)` | BL / Orginal Image | 123 × 156 | image |
| pdp-v1.html | `I1280:10723;1519:25228 (slot fill)` | unnamed (6) 1 | 123 × 68 | image |
| pdp-v1.html | `I1280:10723;1519:25229 (slot fill)` | unnamed (3) 1 | 50 × 50 | image |
| pdp-v1.html | `I1280:10723;1519:25230 (slot fill)` | unnamed (7) 1 | 50 × 50 | image |
| pdp-v1.html | `I1280:10723;1519:25233 (slot fill)` | unnamed (5) 1 | 50 × 50 | image |
| pdp-v1.html | `I1280:10723;1519:25231 (slot fill)` | unnamed (4) 1 | 50 × 50 | image |
| pdp-v1.html | `I1280:10723;1519:26498;1519:26469` | Linear / Like / Heart | 24 × 24 | icon |
| pdp-v1.html | `I1280:10736;1519:25227 (slot fill)` | Product Image | 123 × 156 | image |
| pdp-v1.html | `I1280:10736;1519:25228 (slot fill)` | Gemini_Generated_Image_1xd3lh1xd3lh1xd3 (1) 2 | 123 × 68 | image |
| pdp-v1.html | `I1280:10736;1519:25229 (slot fill)` | Gemini_Generated_Image_1xd3lh1xd3lh1xd3 1 | 50 × 50 | image |
| pdp-v1.html | `I1280:10736;1519:25230 (slot fill)` | Gemini_Generated_Image_1xd3lh1xd3lh1xd3 (4) 1 | 50 × 50 | image |
| pdp-v1.html | `I1280:10736;1519:25233 (slot fill)` | Gemini_Generated_Image_4h4hcm4h4hcm4h4h 1 | 50 × 50 | image |
| pdp-v1.html | `I1280:10736;1519:25231 (slot fill)` | unnamed (2) 1 | 50 × 50 | image |
| pdp-v1.html | `I1280:10736;1519:26498;1519:26469` | Linear / Like / Heart | 24 × 24 | icon |
| pdp-v1.html | `I1280:10749;1519:25227 (slot fill)` | Image | 123 × 156 | image |
| pdp-v1.html | `I1280:10749;1519:25228 (slot fill)` | Gemini_Generated_Image_1xd3lh1xd3lh1xd3 (1) 2 | 123 × 68 | image |
| pdp-v1.html | `I1280:10749;1519:25229 (slot fill)` | Gemini_Generated_Image_cfwholcfwholcfwh 1 | 50 × 50 | image |
| pdp-v1.html | `I1280:10749;1519:25230 (slot fill)` | Gemini_Generated_Image_nwrqcfnwrqcfnwrq 1 | 50 × 50 | image |
| pdp-v1.html | `I1280:10749;1519:25233 (slot fill)` | Gemini_Generated_Image_4h4hcm4h4hcm4h4h 1 | 50 × 50 | image |
| pdp-v1.html | `I1280:10749;1519:25231 (slot fill)` | unnamed (2) 1 | 50 × 50 | image |
| pdp-v1.html | `I1280:10749;1519:26498;1519:26469` | Linear / Like / Heart | 24 × 24 | icon |
| pdp-v1.html | `I1280:10762;1519:25227 (slot fill)` | Product Image | 123 × 156 | image |
| pdp-v1.html | `I1280:10762;1519:25228 (slot fill)` | Gemini_Generated_Image_1xd3lh1xd3lh1xd3 (1) 2 | 123 × 68 | image |
| pdp-v1.html | `I1280:10762;1519:25229 (slot fill)` | Gemini_Generated_Image_1xd3lh1xd3lh1xd3 1 | 50 × 50 | image |
| pdp-v1.html | `I1280:10762;1519:25230 (slot fill)` | Gemini_Generated_Image_1xd3lh1xd3lh1xd3 (4) 1 | 50 × 50 | image |
| pdp-v1.html | `I1280:10762;1519:25233 (slot fill)` | Gemini_Generated_Image_4h4hcm4h4hcm4h4h 1 | 50 × 50 | image |
| pdp-v1.html | `I1280:10762;1519:25231 (slot fill)` | unnamed (2) 1 | 50 × 50 | image |
| pdp-v1.html | `I1280:10762;1519:26498;1519:26469` | Linear / Like / Heart | 24 × 24 | icon |
| pdp-v1.html | `1280:10772` | _iPhone mockup status bar | 393 × 40 | image |
| pdp-v1.html | `1280:10775` | Line Duotone / Arrows / Alt Arrow Left | 28 × 28 | icon |
| pdp-v1.html | `1280:10779` | Linear / Search / Magnifer | 24 × 24 | icon |
| pdp-v1.html | `1280:10783` | Outline / Shopping, Ecommerce / Cart Large 2 | 28 × 28 | icon |
| pdp-v1.html | `1280:10768 left-icon` | Home/Home 54 (Icon Size=S, Style=Outline) 1777:12415 | 20 × 20 | icon |
| pdp-v1.html | `1280:10768 right-icon` | Home/Home 54 (Icon Size=S, Style=Outline) 1777:12415 | 20 × 20 | icon |
| pdp-v1.html | `1280:10769 right-icon` | Home/Home 54 (Icon Size=S, Style=Outline) | 20 × 20 | icon |

Total placeholders: **139**.

## Literal colour values (no R1 token) in pdp.css

Each row names the Figma node of the element that uses the value (or its section).

| pdp.css rule | Literal value(s) | Figma node / note |
|---|---|---|
| `.scr-c-ink` | `#18191a` | 1280:10512 et al. |
| `.scr-c-ink2` | `#222426` | 1280:10425, 1280:10623 |
| `.scr-c-grey` | `#4c555c` | 1280:10481, I1280:10517;1548:30753 |
| `.scr-c-grey2` | `#575d62` | 1280:10690 |
| `.scr-c-green` | `#027a48` | 1280:10431, 1201:9824 |
| `.scr-c-link` | `#005aaa` | 1280:10501, I1280:10446;1546:27138 |
| `.scr-c-mrp` | `rgba(110, 118, 124, 0.7)` | 1280:10430, 1201:9821 |
| `background: #fafdff; border: 1px solid #edeff0; border-radius: var(--a` | `#edeff0`, `#fafdff` |  (section: Watchlist / Icons Frame 40×40 (1280:10401, 1280:10417): fill #fafdff, 1px #edeff0, radius 8, "Icons Shadow") |
| `box-shadow: 0 0 3px 0 rgba(0, 0, 0, 0.01), 0 0 3px 0 rgba(0, 0, 0, 0.0` | `rgba(0, 0, 0, 0.01)`, `rgba(0, 0, 0, 0.05)`, `rgba(0, 0, 0, 0.18)` |  (section: Watchlist / Icons Frame 40×40 (1280:10401, 1280:10417): fill #fafdff, 1px #edeff0, radius 8, "Icons Shadow") |
| `padding: 8px 16px; background: #fff; border-bottom: 1px solid #e0e2e4;` | `#e0e2e4`, `#fff` |  (section: Top Nav Bar (1280:10773 / 1201:9774): white, border-b #e0e2e4, px16 py8) |
| `.scr-review` | `#d0d1d2`, `#eff1f0` | element node 1201:9796 (section: Review badge "Review /BT/ BIG" (I1280:10408;1528:26138, 1201:9796)) |
| `.scr-review__score` | `#027a48`, `#d0d1d2`, `#f7f7f7` | element node 1201:9797 (section: Review badge "Review /BT/ BIG" (I1280:10408;1528:26138, 1201:9796)) |
| `.scr-review__count` | `#eff1f0` | element node 1201:9801 (section: Review badge "Review /BT/ BIG" (I1280:10408;1528:26138, 1201:9796)) |
| `border: 1px solid #def0ff; border-radius: 9px;   /* radius 9: no R1 to` | `#def0ff` | radius 9: no R1 token;  (section: Icon box 42 with gradient (1280:10452, 1280:10663, 1280:10680)) |
| `background-image: linear-gradient(162.8596516811475deg, rgb(220, 238, ` | `rgb(220, 238, 253)`, `rgb(240, 248, 255)` |  (section: Icon box 42 with gradient (1280:10452, 1280:10663, 1280:10680)) |
| `border: 1px solid #d17515; border-radius: var(--annachy-radius-4);` | `#d17515` |  (section: Bonus Coins - Card (1280:10433 / 1201:9826)) |
| `background-image: linear-gradient(110.40307283154195deg, rgb(220, 104,` | `rgb(220, 104, 3)`, `rgb(249, 174, 60)` |  (section: Bonus Coins - Card (1280:10433 / 1201:9826)) |
| `.scr-bonus__txt` | `#fff` | element node 1201:9834 (section: Bonus Coins - Card (1280:10433 / 1201:9826)) |
| `.scr-desktop` | `#c0c5d2` | 605:17532 stroke #c0c5d2, radius 12 |
| `.scr-desktop__btn26` | `#000`, `#ffe11a` | 605:17549 |
| `.scr-mobile` | `#c0c5d2` | 1171:9676 |
| `.scr-m-status` | `#fff` | 1171:9680 |
| `.scr-m-image` | `#fff` | 1201:9771 |
| `.scr-m-bonus` | `rgb(220, 104, 3)`, `rgb(249, 174, 60)` | 1201:9826 |
| `.scr-m-home` | `#0b0d0f` | 1171:9677/9678 Background/Inverse #0b0d0f (no R1 token) |
| `.scr-p-phonebar` | `#fff` | 1280:10771 |
| `.scr-vcard` | `#f0f2f3`, `rgba(235, 237, 238, 0.6)` | I1280:10445;1539:30180 |
| `.scr-vcard--active` | `#131415`, `rgba(0, 0, 0, 0.01)`, `rgba(0, 0, 0, 0.04)`, `rgba(0, 0, 0, 0.15)`, `rgba(0, 0, 0, 0.26)`, `rgba(0, 0, 0, 0.29)` | I1280:10445;1539:30179 |
| `.scr-vcard__foot` | `#eeeded`, `#fff` | 1010:21647 |
| `.scr-vcard__price` | `#18191a` |  (section: Colour + size 1280:10444) |
| `.scr-vcard__mrp` | `#575d62` | 1539:28948 |
| `.scr-vcard__badge` | `#027a48`, `#fefefe` | 1010:21645 |
| `.scr-size` | `#131415`, `rgba(172, 177, 180, 0.5)` | 1546:26984 |
| `.scr-size--oos` | `#c2c2c2`, `#f0f0f0` | 1546:27436 |
| `.scr-size__oos` | `#b42318`, `#fff`, `rgba(251, 195, 191, 0.86)` | 1546:27405 |
| `.scr-dlv` | `rgb(23, 70, 162)`, `rgb(58, 111, 247)` | 1280:10449 |
| `.scr-dlv__txt` | `#fff` | I1280:10449;1546:27817 |
| `.scr-dlv__price` | `#fff` | I1280:10449;1548:27922 |
| `.scr-dlv__mrp` | `#dbe1e4` |  (section: Delivery 1280:10447) |
| `.scr-p-services` | `#005aaa`, `#fafdff` | 1280:10450 (Figma stops #005aaa@960.47%, #fafdff@50.213% — written in ascending order) |
| `.scr-lab__head` | `#f5faff` | 1548:30745 |
| `.scr-lab__name` | `#18191a` |  (section: Top Highlights 1280:10510) |
| `.scr-lab__val` | `#4c555c` | 1548:30752 (2 lines in Figma) |
| `.scr-lab__val--fit` | `#525a61` | I1280:10518;1548:30753 |
| `.scr-pds` | `#e5e7e8` | 1280:10539 |
| `.scr-line` | `#e5e7e8` | Line 137/143 vectors: stroke colour not returned (SVG); #e5e7e8 from 1280:10539 border — unverified |
| `.scr-spec__k` | `#18191a` |  (section: Product Information 1280:10536) |
| `.scr-spec__v` | `#4c555c`, `#e5e7e8` |  (section: Product Information 1280:10536) |
| `.scr-rbar` | `#f3f4f4`, `#fff` | 1280:10625 |
| `.scr-rbar__score` | `#027a48`, `#f7f7f7` | element node 1280:10626 (section: Rating & Reviews — Component 106 1280:10616) |
| `.scr-rbar__meta` | `#3a4044` | element node 1280:10630 (section: Rating & Reviews — Component 106 1280:10616) |
| `.scr-rbar__sep` | `#e5e7e8` | Line 142: colour not returned (SVG) — unverified; element node 1280:10632 (section: Rating & Reviews — Component 106 1280:10616) |
| `.scr-media__tile` | `#f1f1f1` | element node 1280:10635 (section: Rating & Reviews — Component 106 1280:10616) |
| `.scr-media__veil` | `rgba(22, 24, 25, 0.8)` | Rectangle 1954 1280:10641/10650 |
| `.scr-media__more` | `#f2f8fc` | element node 1280:10642 (section: Rating & Reviews — Component 106 1280:10616) |
| `.scr-rev__score` | `#027a48`, `#eaebec`, `#f7f7f7` |  (section: Rating & Reviews — Component 106 1280:10616) |
| `.scr-rev__date` | `#999fa3` |  (section: Rating & Reviews — Component 106 1280:10616) |
| `.scr-rcard` | `#f3f4f5` | Rating Card;  (section: Rating & Reviews — Component 106 1280:10616) |
| `.scr-rcard__bar` | `#027a48` |  (section: Rating & Reviews — Component 106 1280:10616) |
| `.scr-rcard__bar--low` | `#e6190a` |  (section: Rating & Reviews — Component 106 1280:10616) |
| `.scr-rev__text` | `#4c555c` |  (section: Rating & Reviews — Component 106 1280:10616) |
| `.scr-avatar` | `#005aaa`, `#fafdff` |  (section: Rating & Reviews — Component 106 1280:10616) |
| `.scr-helpful` | `#575d62`, `#f3f4f5` |  (section: Rating & Reviews — Component 106 1280:10616) |
| `.scr-trust__row` | `#d7ebfb`, `#f6fbff`, `#fff` | 1280:10661 (Figma stops white@960.47%, #f6fbff@84.016%) |
| `.scr-trust__item` | `#464a4e` | element node 1280:10662 (section: Trust + brand 1280:10660) |
| `.scr-brand` | `rgba(252, 252, 253, 0.98)` | 1280:10679 |
| `.scr-brand__title` | `#1e2022` |  (section: Trust + brand 1280:10660) |
| `.scr-similar` | `#e4f2fd`, `#f5faff`, `#f7fbff` | element node 1280:10694 (section: Similar products 1280:10694) |
| `.scr-rbt` | `#d0d1d2`, `#eff1f0` | Review BT;  (section: Similar products 1280:10694) |
| `.scr-rbt__score` | `#027a48`, `#d0d1d2`, `#f7f7f7` |  (section: Similar products 1280:10694) |
| `.scr-rbt__count` | `#788186` |  (section: Similar products 1280:10694) |
| `.scr-wl-s` | `#edeff0`, `#fafdff`, `rgba(0, 0, 0, 0.01)`, `rgba(0, 0, 0, 0.05)`, `rgba(0, 0, 0, 0.18)` | Watchlist/Small Button;  (section: Similar products 1280:10694) |
| `.scr-sp__tag` | `#18191a` |  (section: Similar products 1280:10694) |
| `.scr-sp__name` | `#4c555c` |  (section: Similar products 1280:10694) |
| `.scr-sp__mrp` | `rgba(110, 118, 124, 0.7)` |  (section: Similar products 1280:10694) |
| `.scr-sp__off` | `#027a48` |  (section: Similar products 1280:10694) |
| `.scr-sp__tax` | `#999fa3` |  (section: Similar products 1280:10694) |
| `.scr-coll` | `#e4f2fd` | element node 1280:10703 (section: New collections 1280:10703) |
| `.scr-coll__arrow` | `#def0ff`, `rgb(220, 238, 253)`, `rgb(240, 248, 255)`, `rgba(0, 0, 0, 0)`, `rgba(0, 0, 0, 0.03)` | 1280:10706 |
| `.scr-tile` | `#edeff0`, `#fff` | element node I1280:10723;1519:25227 (section: New collections 1280:10703) |
| `.scr-wl-w` | `#edeff0`, `#fafdff`, `rgba(0, 0, 0, 0.01)`, `rgba(0, 0, 0, 0.05)`, `rgba(0, 0, 0, 0.18)` | Watchlist/ Width Big Button; element node I1280:10723;1519:26498 (section: New collections 1280:10703) |
| `.scr-toplabel` | `#18191a` | Top Lablel; element node I1280:10723;1519:26199 (section: New collections 1280:10703) |
| `.scr-toplabel--blue` | `#005aaa`, `#fafdff` | I1280:10723;1519:26199 |
| `.scr-toplabel--gold` | `#ffd27c`, `#ffde9f`, `#ffeac1` | I1280:10736;1519:26199 (SVG radial r = 10 × 6.6) |
| `.scr-toplabel--pale` | `#f6f6f6`, `#ffeac1` | I1280:10749;1519:26199 (r = 10 × 10.4) |
| `.scr-bnav` | `#fff`, `rgba(153, 159, 163, 0.2)`, `rgba(24, 25, 26, 0)`, `rgba(24, 25, 26, 0.01)`, `rgba(24, 25, 26, 0.02)` | 1280:10764 |
| `.scr-bnav__home` | `#000` | 1280:10766 |

## R11 product imagery (2026-11-20)

Image placeholders marked `data-annachy-image` show the **original Figma images** from `../assets/images/`. These are byte-identical copies, approved
for **internal reproduction only**, and their rights are unverified (see that folder's README and `data-img-rights`). The crops, offsets,
stacked colour variants and instance scaling are Figma's own, converted from the design context. Do not publish these screens with the images
until the rights are resolved. Mapping: `docs/figma-audit/r11-0-product-imagery-manifest.json`.
