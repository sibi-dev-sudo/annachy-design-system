# 03 — Patterns & Screens, and the Browser Showcase

## 1. Screens reproduced (Figma pages B: Sample Screen `1375:30857`, PDP `581:11523`)

Each page has a root frame sized exactly to the Figma frame. Sections are placed at their Figma metadata coordinates. The pages reuse the library components (Button, Button Gradient, Input Outline / Filled) instead of re-styling them. Per-frame detail (placeholders, literal values, overrides, Figma calls) is in each folder's `README.md`.

| Figma frame | Size | Page | Status | Validation |
|---|---|---|---|---|
| `1375:30858` Desktop PDP | 1440 × 3533 | `screens/sample-screen/desktop-pdp-1375-30858.html` | Complete (2 tiny layers omitted: one with an unknown parent, one clipped) | `screens-sample-check.html` |
| `1608:9891` Desktop | 1440 × 1073 | `screens/sample-screen/desktop-1608-9891.html` | **Partial:** the frame box only. Figma returns no children for this frame through the read-only tools (probed; documented) | same |
| `1608:7090` Mobile PDP | 360 × 4683 | `screens/sample-screen/mobile-pdp-1608-7090.html` | Complete | same |
| `1627:11756` Mobile | 360 × 800 | `screens/sample-screen/mobile-putaway-1627-11756.html` | Complete (hidden layers omitted, as in Figma) | same |
| `1629:11987` Job listing | 360 × 800 | `screens/sample-screen/job-listing-page-1629-11987.html` | Complete | same |
| `605:17532` Desktop / BG Colours | 1440 × 1024 | `screens/pdp/desktop-bg-colours.html` | Complete (one screenshot placeholder + "Button 26" frame) | `screens-pdp-check.html` |
| `1171:9676` Mobile | 360 × 1536 | `screens/pdp/mobile.html` | Complete | same |
| `1280:10398` PDP V1 (latest) | 393 × 4683 | `screens/pdp/pdp-v1.html` | Complete, with limits listed in the README | same |
| `1214:11887`, `1218:13662` PDP V1 (earlier) | 393 × 4388 | — | **Superseded iterations.** They differ structurally from the latest, and the differences are tabulated in `screens/pdp/README.md` | — |

**Validation.**
- Sample Screen: **1,363 checks / 0**.
- PDP: **303 checks / 0**.
- Coverage: root sizes, the position and size of 157 sections / rows / cards within 1px, stylesheet links, placeholder labelling, and the absence of `img` / `svg` / asset URLs / external resources.
- I re-ran both independently after the agents reported back.

**Placeholders (not substitutes).**
- Totals: 362 = 141 images, 215 icons, 6 logos.
- Each has the exact Figma size, `class="scr-asset"`, `data-figma-node`, `data-asset` and a title naming the layer.
- They are filled once ASSET-1 / ICON-1 are unblocked (doc 04).

**Known fidelity limits.**
- Text widths: fallback font (FONT-1).
- Vector line and divider colours exist only as SVG assets. They are approximated from neighbouring strokes or drawn as dashed `data-stroke` placeholders; each is listed.
- A few frame fills are unverified; these are listed in the READMEs.

**Figma calls for screens.** 57, all read-only: `get_design_context` 43 (screenshots excluded), `get_metadata` 14. No assets fetched.

## 2. Browser showcase

Serve the project root over HTTP, for example `python -m http.server`, and open `/showcase/index.html`.

| Area | Page | What a developer gets |
|---|---|---|
| Catalogue | `showcase/index.html` + `index.js` | Search by name, category or **Figma node ID**; category filters (Foundations / Components / Patterns & screens); 23 cards with variant counts and node references. Built from the library's own Input and Button |
| Foundations | `foundations/colors · typography · iconography · effects · grid · dimensions · base` | Live swatches, type specimens, effects, grid values, dimensions; the Iconography page shows the icon model, every slot and the live manifest status |
| Components | `components/button · button-gradient · input · checkbox · radio · toggle · dropdown · tooltip` | Every Figma variant rendered from the library CSS, forced states, interactive examples, markup references, values with node IDs |
| Dropdown R6 | `components/dropdown.html#dark-footer` (+ `dropdown-r6.js`) | 20 Dark Items, 40 Dark / Footer Menus, 3 interactive staged-commit demos, markup |
| Screens | `screens/sample-screen/*`, `screens/pdp/*` | The pattern screens built with the library; 34 icon placeholders render exact library icons |
| **Icon catalogue** | `icons/index.html` + `icons.js` | All 5,128 icon sets on the Figma Icons page: every style and size, search, filters, paging, restricted Brands |

Tests for the showcase:
- `showcase_catalogue_cdp.py` (search, filters, links, Iconography);
- `r4_showcase_dropdown_cdp.py` (20 checks, including all 48 menu heights against META and a live staged commit);
- `r4_showcase_tooltip_cdp.py`;
- `r3_closure_cdp.py` (every component page);
- `browser_check.py` (link check over the foundations pages).
