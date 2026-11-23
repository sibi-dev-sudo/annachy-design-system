# Closure — screen icons and Annachy logotype (implemented)

| Item | Value |
|---|---|
| Date | 2026-11-20 |
| Scope | The 50 remaining in-scope screen icon placeholders and the Annachy logotype `1375:31293`. Solar, Brainstorming and Gallery Minimalistic stay **not required** (R9 decision); status-bar glyphs are phone system UI (**N/A**); the five third-party "logo 2" marks are excluded (no rights evidence, not exported) |
| Figma | Subagent: `get_design_context` ×51 (screenshots excluded, one verbatim call per node), `get_metadata` ×52 (incl. `1608:9891`: frame only, no children). Main session: `get_design_context` ×3 on parents `1375:30951`, `1375:31080`, `1375:31225` for transforms. **No writes, no `create_session`, Figma unchanged** |
| Delivered | 37 original SVGs in `showcase/screens/assets/vectors/` (`icon-<id>.svg`, `logo-annachy-b8420.svg`), byte-identical to the export; 49 placeholders + the logotype |
| Library reuse | `1375:31369` → library `editor-hamburger-menu` (outline), colour `#3D4451` as in the Figma artwork — exact geometry at the 24 px slot. No other artwork matched exactly (`docs/replication/closure-icon-match.json`) |
| Existing artwork reused | `1280:10674` badge = R11 artwork `73565`; 7 desktop card stars = R10 `star-c6cc8` (Figma card code references `c6cc8`) |
| Transforms (from the parents' design context) | `1375:30955` rotate(180°) scaleY(−1) (= mirror); `1375:31088` scaleY(−1); `1375:31227` rotate(−90°) |
| Validation | Screen fixtures (R10 vector contract: declared file, loaded, drawn at the Figma size); mutation CL-ICON; visual check of the desktop header / product info |

| Node | Screen | Placeholder title | Figma size | Artwork | Delivered | Transform |
|---|---|---|---|---|---|---|
| `1201:9829` | mobile.html | loyalty 1 [Vectorized] | 24 × 24 | `66f60` | icon-66f60.svg | — |
| `1280:10436` | pdp-v1.html | loyalty 1 [Vectorized] | 24 × 24 | `66f60` | icon-66f60.svg | — |
| `I1280:10449;1546:27825` | pdp-v1.html | Car (Group 1171275299) | 34.3044 × 22 | `65d38` | icon-65d38.svg | — |
| `1280:10453` | pdp-v1.html | Group 1171275304 (inset-positioned, approx. 32.7x24.5) | 31.2116 × 23.3849 | `05b35` | icon-05b35.svg | — |
| `1280:10467` | pdp-v1.html | Group 1171275306 (inset-positioned, approx. 31x24.3) | 30.7896 × 23.9378 | `f0734` | icon-f0734.svg | — |
| `1280:10486` | pdp-v1.html | Group 1171275306 (inset-positioned, approx. 31x24.3) | 30.7896 × 23.9378 | `f0734` | icon-f0734.svg | — |
| `1280:10674` | pdp-v1.html | Frame 2121454395 (genuine product badge, one vector) | 42 × 42 | `73565` | icon-73565.svg | — |
| `1375:31338` | desktop-pdp-1375-30858.html | Frame (location) | 30 × 30 | `23ffe` | icon-23ffe.svg | — |
| `1375:31344` | desktop-pdp-1375-30858.html | Frame (chevron) | 20 × 20 | `a7ef6` | icon-a7ef6.svg | — |
| `1375:31350` | desktop-pdp-1375-30858.html | Frame (profile) | 30 × 30 | `fecd1` | icon-fecd1.svg | — |
| `1375:31355` | desktop-pdp-1375-30858.html | Frame (chevron) | 20 × 20 | `f8078` | icon-f8078.svg | — |
| `1375:31358` | desktop-pdp-1375-30858.html | Frame (cart) | 30 × 30 | `dfeff` | icon-dfeff.svg | — |
| `1375:31369` | desktop-pdp-1375-30858.html | Frame (category) | 24 × 24 | `b25e9` | library icon editor-hamburger-menu (outline) | — |
| `I1375:31375;17:1154` | desktop-pdp-1375-30858.html | Frame (chevron) | 20 × 20 | `92e22` | icon-92e22.svg | — |
| `I1375:31376;17:1154` | desktop-pdp-1375-30858.html | Frame (chevron) | 20 × 20 | `92e22` | icon-92e22.svg | — |
| `I1375:31377;17:1154` | desktop-pdp-1375-30858.html | Frame (chevron) | 20 × 20 | `92e22` | icon-92e22.svg | — |
| `I1375:31378;17:1154` | desktop-pdp-1375-30858.html | Frame (chevron) | 20 × 20 | `92e22` | icon-92e22.svg | — |
| `1375:31381` | desktop-pdp-1375-30858.html | Frame (deals) | 30 × 30 | `09a96` | icon-09a96.svg | — |
| `1375:31388` | desktop-pdp-1375-30858.html | Frame (offers) | 30 × 30 | `c7454` | icon-c7454.svg | — |
| `1375:30900` | desktop-pdp-1375-30858.html | Frame (share) | 30 × 30 | `2e83b` | icon-2e83b.svg | — |
| `1375:30902` | desktop-pdp-1375-30858.html | Frame (wishlist) | 30 × 30 | `622db` | icon-622db.svg | — |
| `1375:30912` | desktop-pdp-1375-30858.html | Frame (star) | 12 × 12 | `292cb` | icon-292cb.svg | — |
| `1375:30914` | desktop-pdp-1375-30858.html | Frame (star) | 12 × 12 | `9a2c8` | icon-9a2c8.svg | — |
| `1375:30916` | desktop-pdp-1375-30858.html | Frame (star) | 12 × 12 | `9a2c8` | icon-9a2c8.svg | — |
| `1375:30918` | desktop-pdp-1375-30858.html | Frame (star) | 12 × 12 | `9a2c8` | icon-9a2c8.svg | — |
| `1375:30920` | desktop-pdp-1375-30858.html | Frame (info) | 20 × 20 | `eee0a` | icon-eee0a.svg | — |
| `1375:30940` | desktop-pdp-1375-30858.html | Frame (info) | 15 × 15 | `63b26` | icon-63b26.svg | — |
| `1375:30952` | desktop-pdp-1375-30858.html | Frame (previous) | 38 × 38 | `049f3` | icon-049f3.svg | — |
| `1375:30955` | desktop-pdp-1375-30858.html | Frame (next, mirrored) | 38 × 38 | `55cba` | icon-55cba.svg | rotate(180deg) scaleY(-1) |
| `1375:31010` | desktop-pdp-1375-30858.html | badge-percent | 25 × 25 | `b0df9` | icon-b0df9.svg | — |
| `1375:31020` | desktop-pdp-1375-30858.html | badge-percent | 25 × 25 | `b0df9` | icon-b0df9.svg | — |
| `1375:31051` | desktop-pdp-1375-30858.html | Frame (perk icon) | 30 × 30 | `8264d` | icon-8264d.svg | — |
| `1375:31059` | desktop-pdp-1375-30858.html | Frame (perk icon) | 30 × 30 | `50625` | icon-50625.svg | — |
| `1375:31069` | desktop-pdp-1375-30858.html | Frame (perk icon) | 30 × 30 | `96cb2` | icon-96cb2.svg | — |
| `1375:31082` | desktop-pdp-1375-30858.html | Frame (details) | 30 × 30 | `3198d` | icon-3198d.svg | — |
| `1375:31088` | desktop-pdp-1375-30858.html | Frame (collapse, mirrored) | 30 × 30 | `cbc6c` | icon-cbc6c.svg | scaleY(-1) |
| `1375:31116` | desktop-pdp-1375-30858.html | Frame (specifications) | 30 × 30 | `cbccb` | icon-cbccb.svg | — |
| `1375:31159` | desktop-pdp-1375-30858.html | Frame (chevron) | 30 × 30 | `61bfd` | icon-61bfd.svg | — |
| `1375:31227` | desktop-pdp-1375-30858.html | Frame (arrow, rotated -90°) | 30 × 30 | `e7481` | icon-e7481.svg | rotate(-90deg) |
| `1375:31283` | desktop-pdp-1375-30858.html | Group 1000001479 (previous arrow) | 66.6667 × 66.6667 | `e9d0f` | icon-e9d0f.svg | — |
| `1375:31286` | desktop-pdp-1375-30858.html | Group 1000001482 (next arrow) | 66.6667 × 66.6667 | `1f6fa` | icon-1f6fa.svg | — |
| `1375:31293` | desktop-pdp-1375-30858.html | Logotype (Group) | 156.74 × 38.7224 | `b8420` | logo-annachy-b8420.svg | — |
| `1629:11992` | job-listing-page-1629-11987.html | ArrowLeft | 24 × 24 | `8d51b` | icon-8d51b.svg | — |
| `1629:12002` | job-listing-page-1629-11987.html | Frame | 24 × 24 | `f87a7` | icon-f87a7.svg | — |
| `1629:12009` | job-listing-page-1629-11987.html | Frame (chevron) | 16 × 16 | `cac65` | icon-cac65.svg | — |
| `1608:7143` | mobile-pdp-1608-7090.html | loyalty 1 [Vectorized] | 24 × 24 | `66f60` | icon-66f60.svg | — |
| `1608:7186` | mobile-pdp-1608-7090.html | Group (perk icon) | 31.2116 × 23.3849 | `05b35` | icon-05b35.svg | — |
| `1608:7200` | mobile-pdp-1608-7090.html | Group (perk icon) | 30.7896 × 23.9378 | `10b90` | icon-10b90.svg | — |
| `1608:7219` | mobile-pdp-1608-7090.html | Group (perk icon) | 30.7896 × 23.9378 | `10b90` | icon-10b90.svg | — |
| `1627:11761` | mobile-putaway-1627-11756.html | ArrowLeft | 24 × 24 | `8d51b` | icon-8d51b.svg | — |
| `1627:11771` | mobile-putaway-1627-11756.html | Frame | 24 × 24 | `f87a7` | icon-f87a7.svg | — |
