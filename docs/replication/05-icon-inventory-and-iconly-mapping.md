# 05 — Icon Inventory and Iconly Mapping

> **R7-1 (2026-11-20): the icons are implemented.** The owner approved exporting page `1801:5142` for local internal use.
>
> **Export.** 33 category-frame exports, all 35,890 variants paired one-to-one with Figma names (`docs/figma-audit/r7-1-icon-export-report.md`).
> - 6,890 unique normalised assets: 6,103 library in `src/icons/svg/` + 787 restricted Brands in `restricted/brands/`.
> - 7,174 of 7,178 set × style combinations are scale-equivalent across the 5 sizes; 4 have a separate XS file.
> - 38 groups of identical artwork across different sets are kept separate.
> - The duplicate "Calender & date" frame reuses its twin's files.
>
> **Browser catalogue.** `showcase/icons/` shows all 5,128 sets × styles × sizes, with search (name, category, set or variant node ID), category, style and size filters, paging, and a restricted-Brands toggle.
>
> **Components.** The Button, Gradient, Input Outline and Dropdown search / footer slots render their exact Figma icons, through `src/icons/icons.js` (`data-annachy-icon`).
>
> **Screens.** The 32 exact library-instance placeholders (34 elements) now render their icons.
> - Still placeholders: 30 "exact" + 38 name-only **Solar** icons (artwork on page `375:10889`, outside the export approval), 2 "Play Circle" name-only candidates, and 113 unidentifiable layers.
> - Images (141) and logos (6) remain placeholders.
>
> **Licence.** Iconly (purchased), internal use only, licence text not on file. Brands rights are not verified (kept outside `src/`).

> **UPDATE 2026-11-20 (R7). This supersedes §1, §4 and the "BLOCKED" status below.** The owner added the icons to the design-system file.
>
> **Where the icons are.** Page **`1801:5142` "② Icons"**, not the Iconography page `375:10889`, which is unchanged.
>
> **What the page contains** (`docs/figma-audit/r7-0-iconography-evidence.md`, `r7-0-iconography-inventory.json`):
> - 5,128 local component sets: 35,890 variants, 4,839 unique names.
> - 33 category frames, 32 distinct names; "Calender & date" appears twice.
> - Outline / Filled styles, at XS 16 / S 20 / M 24 / L 32 / XL 40.
> - Built from Iconly artwork, as shown by the component descriptions.
>
> **Component icons.** The 5 S5 component icons are now local and mapped in `src/icons/figma-icon-map.json`:
> - Home/Home 54 `1802:68148`
> - User/User Curved `1802:86130`
> - Chevron Up `1802:211244`
> - Chevron Down `1802:211124`
> - Error circle `1802:155982`
>
> Not on the Icons page: the Dropdown "Selected" check (a Lucide master in Brainstorming), the "checkbox" indicator, the Checkbox glyph (a frame) and the Tooltip arrow. These are exceptions E-2 and E-3. Cloud is still a Solar pilot icon on `375:10889`.
>
> **Screen placeholders (362):** 215 icons, 141 images, 6 logos.
> - Icons: **62 EXACT** (32 library instances + 30 Solar-named 24 px frames), **40 NAME_ONLY**, **113 NO_MATCH** (24 plain shapes, 34 unnamed "Frame" layers, the rest custom groups and status-bar glyphs).
> - Images and logos are not icons.
>
> **Artwork.** Every icon is exposed only as temporary SVG asset URLs. Fetching them is an **export**. So **artwork needs explicit export authorisation**; no Iconly credentials are needed any more.

| Item | Value |
|---|---|
| Date | 2026-11-20 |
| Directive | Use the purchased **Iconly** library as the icon source; exact matches only; record exceptions; brand logos separate |
| Result | **BLOCKED: no Iconly access is available in this environment.** The inventory and the mapping evidence are complete. Artwork matching, download and integration wait for access |
| Manifest | `src/icons/manifest.json` stays `status: "blocked"`. D-12 is now resolved in principle by the directive ("Iconly"); D-13 / D-15 are recorded as the access and licence items below |

## 1. What was searched (Iconly access)

| Looked for | Where | Found |
|---|---|---|
| Iconly API key / token / credentials | Environment variables; `.env` files under Documents, Downloads, OneDrive, Desktop (depth 5) | **None** |
| Iconly SVG packs (downloaded purchase) | Same folders: `*iconly*` archives / folders | **None** (only plugin builds and diagnostics) |
| Existing Iconly download / metadata tools | `Documents/MCP/iconly-plugin/` (Iconly Universal Component Builder v5.4–v6.1.2), `Downloads/iconly-component-builder*` | **Figma plugins, not downloaders.** They pair Outline/Filled artwork already inside a Figma file and build component sets. They have no Iconly API client (network access is limited to jsDelivr and Hugging Face for the ML matcher) |
| Exported artwork from those tools | `Downloads/iconly-*-artwork-fixture.json`, `*-matching-diagnostics-*.json` | 1,023 SVGs from test categories ("fghj" arrows, "shopping"). Searched for the S5 source nodes `379:123577`, `268:20421`, `370:50569`: **not present**. These are from a different file, so they cannot be used as verified Iconly assets for this system |

## 2. Provenance evidence: the Figma icons are Iconly-derived (S5)

The S5 icon components carry descriptions written by the Iconly component builder (`r6-0-evidence.md` §4):
- `User/User Curved` `1779:36485`: Outline source "User curved" (`379:123577`), Filled source "user" (`268:20421`), match: primary-visual.
- `Home/Home 54` `1777:9468`: "Manually verified Outline + Filled pair", source layer "Home " (`370:50569`).

So the exact Iconly originals can be identified by those source names and node IDs once the source file or the Iconly library is reachable.

## 3. Icon inventory (every icon used by the replicated components)

| # | Figma icon | Node | Style · size used | Used by | Iconly source (from provenance) | Mapping status |
|---|---|---|---|---|---|---|
| 1 | Home/Home 54 | `1777:9468` (S `1777:12415`) | Outline · S 20 | Button (all), Button Gradient, Dropdown footer "Icon + label" | "Home " (`370:50569`) | Pending Iconly access |
| 2 | User/User Curved | `1779:36485` (M `1779:37533`) | Outline · M 24 | Input Outline leading icon, Dropdown search | Outline "User curved" (`379:123577`), Filled "user" (`268:20421`) | Pending Iconly access |
| 3 | Arrow/Chevron Up | `1779:38813` | Outline · M 24 | Input Outline trailing | not recorded in the instance (needs the S5 file) | Pending access (D-13) |
| 4 | Arrow/Chevron Down | `1779:39438` | Outline · M 24 | Input Outline trailing | (as above) | Pending access |
| 5 | Alerts/Error circle | `1780:40127` | Outline · XS 16 | Input Outline sub-text | (as above) | Pending access |
| 6 | Cloud (Solar pilot) | `561:36135` | Linear · 24 / 14, state Brand | Input Filled | **Not Iconly**: pilot S2, style names match the Solar set (SUS-07) | **Exception E-1**: Iconly equivalent needed, or keep S2 (owner) |
| 7 | "Selected" check | `1451:24796` | 20 | Dropdown Single selected indicator | research-page master | Exception E-2: identify the Iconly equivalent (owner) |
| 8 | "checkbox" | `1454:7202` | 20 | Dropdown Multiple indicator | research-page master; Lucide `badge-check` seen in exploration | Exception E-2 |
| 9 | functional/check, functional/remove | `1504:53703` | 16 / 20 | Checkbox glyph | Component geometry (D-27), not a library icon | Exception E-3: owner geometry or export approval |
| 10 | Tooltip arrow polygon | `1446:32` | 20 | Tooltip | Component geometry (G12) | Exception E-3 |
| 11 | Screen icons (Sample Screen, PDP) | see `showcase/screens/*/README.md` | various | Pattern screens | "Iconly Pro" frames on the Sample Screen page | Pending Iconly access |
| 12 | Brand logos (Amazon, Flipkart …) | research pages, screens | — | Not design-system icons | **Not Iconly**: needs approved brand assets | Exception E-4: provide approved logo files |

## 4. What is needed to finish icons (one of the following)

1. **The downloaded Iconly purchase:** the SVG pack (all styles) placed in a local folder, with its licence file. *Or*
2. **Iconly API credentials:** an API key or token in an environment variable such as `ICONLY_API_KEY`, plus the API documentation or base URL used by your account. *Or*
3. **Read access to the S5 "Annachy Icons File":** file URL or key (D-13), with **export approval** for read-only `download_assets` of the listed S5 icons only (and of `create_session` if the tool requires it).

With any of these, the prepared pipeline runs for the 5 S5 icons plus the screen icons:

| Step | Detail | Tool |
|---|---|---|
| Match | By the provenance names in §2/§3 | — |
| Preserve originals | `src/icons/originals/iconly/` | — |
| Normalise | `currentColor`, keep `viewBox` | — |
| Validate | V01–V11, P/D/I/N rules | `tests/tools/icons_lib.py` |
| Record | manifest entries (source "iconly", licence, attribution) | `src/icons/manifest.json` |
| Fill slots | the 15 slot cases | slot contract already verified, 73/0 |

**Exceptions E-1 to E-4 need a design-owner answer regardless of access.**
