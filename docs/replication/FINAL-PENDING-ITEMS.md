# Final Pending Items

Date: 2026-11-20. Every item that is not complete, grouped by why. Counts come from `closure-placeholder-census.json` and the reports cited.

## A. Completed in the closure (for reference)

| Item | Result |
|---|---|
| 50 remaining in-scope screen icons | Filled with Figma originals (49) or an exact library icon (1) |
| Annachy logotype `1375:31293` | Integrated (`logo-annachy-b8420.svg`) |
| Desktop card stars (7) | Filled by reusing the R10 star, the same Figma artwork `c6cc8` used in the mobile cards |
| Image weight | 42 / 43 images served as A/B-verified WebP copies; all screens together −88.5 % |
| Icon placeholder chrome; PDP V1 field focus | Fixed |
| Accessibility audit | 147 / 0 on all 25 pages |

## B. Not required / out of scope (Design Team decision R9, unchanged)

| Item | Placeholders |
|---|---:|
| Solar icons (Line Duotone / Linear / Outline / Video sets: arrows, heart, search, cart, play, shield, users, map point, like) | 70 empty (77 placeholders minus the 7 card stars filled by reuse) |
| Brainstorming "Icons" master `5:26` | 24 |
| Gallery Minimalistic (`1280:10643`, plus empty slot `1608:7374` added with the rebuilt review overlay) | 2 |
| Superseded PDP iterations, research, cover and archive pages | Not reproduced (doc 01) |

## C. Not applicable

| Item | Placeholders | Reason |
|---|---:|---|
| Phone status bar: Phone Camara, Wifi, Signal, Cellular Signal, Battery | 14 | Phone system UI, not an Annachy design-system asset. Includes the 6 nodes that Figma reports as "invalid node selection" (`1627:11654`, `1627:11690`, `1627:11720`, each used twice) |

## D. External approval required

| ID | Item | Needed from | Blocks |
|---|---|---|---|
| EXT-1 | **Image rights** for the 43 R11 raster images (8 AI-generated, 12 SKU-named, 8 likely web downloads, 1 screenshot, 1 emoji, 13 unattributed) | Owner / legal | Any public or commercial use |
| EXT-2 | **Proxima Nova web licence** (the supplied ZIP is personal-use only) | Design Team / licensing | Exact typography |
| EXT-3 | **Iconly licence text** (owner states it was purchased) | Owner | Distribution of the icon set |
| EXT-4 | **5 third-party brand logos** ("logo 2", Desktop PDP related products) | Brand owners / legal, or the Design Team (replace or remove) | 5 placeholders |
| EXT-5 | **Web optimisation of `62f2c`** (9.05 MB original kept: its WebP copy failed the strict A/B rule with 1.25 % of pixels off by more than 32). Options: accept a measured copy, or have the owner supply a smaller master | Owner decision | About 9 MB on two screens |

## E. Figma source limitations

| ID | Item |
|---|---|
| FIG-1 | Desktop frame `1608:9891` returns no children through read-only access (frame only, 1440 × 1073) |
| FIG-2 | FIG-ICON-1: Filled Arrow icons Swap Square, Swap Square 4, Turn Down Square, Turn Up Circle and Turn Up Square have artwork outside their variant frame (reproduced as is) |
| FIG-3 | 34 R11 placeholders: Figma returned empty renders, so they could only be verified against identical siblings (R11-U2) |
| FIG-4 | R10-U1 to U4: dash phase of 7 dashed artworks, direction of 3 vertical dashed lines, 4 artworks Figma exports empty, 0.24 px offset on V23 |
| FIG-5 | Navigation pages are empty; there is no Select trigger component (traceability matrix rows 24 and 25) |
| FIG-6 | Unbound or raw values reproduced as designed: input focus `#3a6ff7` (IN2), placeholder contrast (IN1/A16), Toggle Off track (TG-1, A39) and the other contrast findings A04, A14, A38, A40 and A41 |

## F. Technical blockers

| ID | Item |
|---|---|
| TECH-1 | No image encoder besides Chrome is installed, so no AVIF; WebP from Chrome's encoder was used |
| TECH-2 | Orphaned headless Chrome processes from 19 November are still running (the tool permissions didn't allow stopping them). Ending them in Task Manager is safe |
| TECH-3 | One-time verification tools (`r10_vector_fidelity_once.py`, `r11_image_fidelity_once.py`, `closure_icon_match.py`, `closure_integrate_icons.py`) need their export staging, which was deleted after validation. Re-running them needs a fresh, approved export |

## G. Remaining in-scope screen placeholders

**5**: the third-party logos (EXT-4). Nothing else in scope is unfilled.
