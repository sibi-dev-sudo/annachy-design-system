# R6-0 Evidence — Dropdown Dark theme and Footer (read-only)

| Item | Value |
|---|---|
| Date | 2026-11-20 |
| Purpose | Close the remaining Dropdown gap: Theme=Dark (20 Item + 24 Menu variants) and Footer=Label / Icon + label (16 Light + 16 Dark Menu variants) |
| Calls (15, all read-only) | `get_design_context` ×4 (screenshot excluded): `1451:25325`, `1464:3069`, `1451:25205`, `1451:24212`. `get_variable_defs` ×9: `1451:25325`, `1464:3057`, `1464:3061`, `1464:3065`, `1464:3069`, `1464:3073`, `1464:3071`, `1451:24822`, `1451:24212`. `get_metadata` ×2: `1451:25385`, and `I1451:24212;887:363` (not found; no data) |
| Not used | No `create_session`, screenshots, asset downloads (the temporary asset URLs in responses were **not fetched**), writes or comments |
| Variant IDs | Taken from saved metadata `raw/metadata/1351-18309.xml`. Dark Menu: Single `1451:25265`…`25520`, Multiple `1454:1490`…`2149`. Dark Item: `1451:25077`–`25081`, `1464:2989`…`3113`. Light Footer Menu: `1451:25190`, `25205`, `25235`, `25250`, `25370`, `25385`, `25415`, `25430`, `1454:1283`, `1317`, `1394`, `1441`, `1755`, `1789`, `1866`, `1913` |

## 1. Dark mode values (the same Brand variables in the Dark mode) [BOUND]

| Variable | Light (R1 token) | **Dark** | Seen on |
|---|---|---|---|
| `Brand/Background/Secondary` | `#f6f7f9` | **`#181b21`** | menu fill, item Default / Focus / Disabled (`1451:25325`, `1464:3057`, `3065`, `3073`) |
| `Brand/Background/Tertiary` | `#edeff2` | **`#1f242e`** | item Hover (`1464:3061`) |
| `Brand/Text/Primary` | `#0b0c0f` | **`#fafcff`** | item label |
| `Brand/Text/Secondary` | `#555d6d` | **`#98a0ae`** | search placeholder |
| `Brand/Text/Tertiary` | `#707a8f` | `#707a8f` (same) | Disabled label |
| `Brand/Border/Primary` | `#bfc4cf` | **`#171e2a`** | menu stroke, search field stroke, Disabled indicator |
| `Brand/Border/Secondary` | `#dcdfe5` | **`#1f242e`** | search divider, footer divider |
| `Brand/Icon/Secondary` | `#555d6d` | **`#98a0ae`** | Default / Hover / Focus indicator |
| `Brand/Blue/500`, `Brand/Base/White` | `#004feb`, `#fafcff` | same | — |
| `Brand/Button/Primary/Background/Default`, `/Content/Default`, `/Border/Focus` | `#004feb`, `#fafcff`, `#003fbc` | same | footer button, item Focus |

## 2. Dark variant differences (different variables, not mode values) [BOUND]

| Element | Light | **Dark** |
|---|---|---|
| Selected fill | `Blue/50` | **`Blue/500`** (`1451:25080`, `1464:3069`) |
| Selected label | `Blue/500` | **`Base/White`** |
| Selected indicator (Single check `1451:24822`; Multiple checkbox `1464:3071`) | `Blue/500` | **`Base/White`** |
| Focus | 2px `Button/Primary/Border/Focus` + `Button/Focus` | identical (`1464:3065`) |

Geometry, typography and spacing are identical to Light (same auto-layout values in `1451:25325`).

## 3. Footer [APPLIED + BOUND]

| Platform | Structure |
|---|---|
| Both | Footer frame: padding-top 4, gap 12. Divider 1px `Border/Secondary`. Then "Footer button", full width, `Button/Primary/Background/Default`, label "Apply selection" `Button/Primary/Content/Default` |
| Desktop (footer frame `1451:23575` in `1451:25205`; `1451:25325`) | Button 40 tall, px 16, py 12, gap 6, `Radius/8`. Label **Label Small — Medium 14/20** |
| Mobile (footer frame `1451:24210`, button `1451:24212`) | Button 48 tall, px 16, py 18, gap 8, `Radius/12`. Label **Label Medium — Medium 16/21** |
| Icon + label | Adds the icon `Home/Home 54`, Outline, **S 20 × 20** (`1777:12415`) before the label, on both platforms |
| Menu heights (META, `1451:25385` etc.) | Desktop: Search Off 253 / Search On 326. Mobile: Search Off 293 / Search On 366. Footer frame on Mobile = 65 (4 + 1 + 12 + 48) |

## 4. Icon provenance discovered (relevant to the icon blocker)

Instance descriptions on the S5 icons record how they were built:
- `User/User Curved` (`1779:36485`): *"Matched Outline/Filled icon … Outline source 'User curved' (379:123577) · Filled source 'user' (268:20421) · match: primary-visual"*.
- `Home/Home 54` (`1777:9468`): *"Manually verified Outline + Filled pair … user-confirmed during catalogue review"*; source layer "Home " (`370:50569`).

This wording is the output of the project's own "Iconly Universal Component Builder" Figma plugin (`Documents/MCP/iconly-plugin`). The S5 "Annachy Icons File" was therefore assembled from source artwork in another file; the source node IDs (`379:123577`, `268:20421`, `370:50569`) are not in this file.

## 5. Not observed (not invented)

- Mobile Dark variants were not opened individually. They use the same component, the same variables in Dark mode, and the Mobile geometry recorded for Light (`r4-0-evidence.md` §3.1). They are implemented by combining those two facts and checked for consistency with the Light Mobile META sizes.
- Footer button hover, focus and pressed states are not drawn in the Dropdown. The footer button is an instance of the R3 Primary Button, so its states come from that component.
