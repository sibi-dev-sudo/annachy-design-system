# 04 — Remaining Gaps and Blockers

Date 2026-11-20. **Verified completion** is in docs 02 and 06. Everything below is either externally blocked or needs a design-owner answer. Nothing here was guessed or substituted.

## 1. External blockers (cannot be resolved from this environment)

| ID | Blocked item | Why | Exactly what unblocks it |
|---|---|---|---|
| ~~ICON-1~~ **resolved (R7-1)** for page `1801:5142`. **ICON-2 (new):** the Solar icons used by the screens (30 exact + 38 name-only) live on page `375:10889`. Exporting them needs approval for that page. **ICON-3:** 113 screen layers carry no icon identity (shapes, unnamed frames, status-bar glyphs) and are kept as placeholders. *(Superseded text follows.)* | Icon **artwork** for the 8 mapped component slots and the 62 EXACT screen icons | The icons are now in the file (`1801:5142`) and fully identified, but the read-only tools expose artwork only as temporary asset URLs. Fetching them = export, which is not authorised | **Export authorisation** for the listed icon sets (read-only `download_assets`, or fetching the asset URLs returned by `get_design_context`) into local staging. No Iconly credentials are needed |
| **ASSET-1** | Product photos, illustrations and brand logos in the Sample Screen and PDP frames | Figma asset export is not authorised (`download_assets` not approved). Logos need approved brand files | Export approval for the listed nodes, or the original image files. Brand logos: approved logo assets (E-4) |
| **FONT-1** | Proxima Nova rendering | Font licence / files not supplied (D-06). A system fallback is used, so text widths and line breaks differ slightly | Licensed WOFF2 files |
| **TOOL-2** | `create_session` | Its read-only behaviour is not independently verified, so it is not used (all work used `get_metadata`, `get_design_context` with screenshots excluded, and `get_variable_defs`) | Independent verification or explicit authorisation |

## 2. Design-owner decisions still open

| ID | Question | Current implementation |
|---|---|---|
| E-1 | Input Filled uses the Solar-pilot "Cloud" icon (S2), not S5/Iconly. Should it use an Iconly icon? | Empty slot, Brand colour wired |
| E-2 | Dropdown "Selected" check and "checkbox" indicator are research-page masters. Which Iconly icons? | Empty 20 × 20 slots, state colours wired |
| E-3 | Checkbox glyph / Radio ring / Toggle strokes (D-27) and the Tooltip arrow polygon (G12) are vector-only geometry | Confirmed boxes and positions only |
| E-4 | Brand logos on screens | Placeholders |
| D-22 | Contrast findings A04, A14, A16, A38, A39, A40 (light tooltip 1.00:1), A41 (menu boundary 1.70:1) | Reproduced as designed; documented in `09-accessibility.md` |
| D-09 | Radius 6 / 10 tokens (raw values in Input) | Raw values kept, as in Figma |
| G1–G4 | Dropdown empty, loading, scroll and group-header states are not designed | Not invented |
| Dark scope | Only Dropdown and Tooltip have Dark designs | `themes/dark.css` holds just the 7 observed values |

## 3. Decisions taken in this phase (reversible, documented)

| ID | Decision | Basis |
|---|---|---|
| R4-Q3 | Footer commit model is **staged**: Apply commits, while Escape / outside / Tab-out discard | Directive to make reasonable technical decisions; the "Apply selection" label. Tested (38 checks) |
| D-03 | The V1 "Light only" rule is superseded: Dark is implemented where Figma defines it | Mission §4 "themes and modes, where defined" |
| D-12 | The icon source is Iconly (directive), consistent with S5 provenance | Mission §6; `r6-0-evidence.md` §4 |

## 4. Not applicable (with reason)

| Item | Reason |
|---|---|
| Navigation (Mobile / Desktop) | Both Figma pages are empty (0 nodes) |
| Select trigger | No component in this Figma file |
| Responsive breakpoints | Figma defines none; Desktop / Mobile are separate variants and frames |
| Research, cover and archive pages | Not design-system output, or duplicates of active sets (doc 01) |


## Scope update 2026-11-20

**ICON-2 (Solar screen icons) and the Brainstorming "Icons" artworks: NOT REQUIRED** (Design Team). They are no longer blockers; no export, no replacement.


## R11 update 2026-11-20 (product imagery implemented)

The 108 image placeholders are no longer an export blocker: they are filled with the original Figma files under the owner's
consolidated approval, **for internal reproduction only**. Remaining R11 items (`docs/figma-audit/r11-0-product-imagery-manifest.md` §8):

| ID | Gap | Blocks |
|---|---|---|
| R11-U1 | Image rights unverified (AI-generated, SKU-named, web downloads, screenshot, emoji, unattributed) | **Any public use / publication** of the screens |
| R11-U2 | 34 placeholders verified only through identical siblings (Figma returned empty renders) | Nothing (recorded) |
| R11-U3 | 102 MB of originals; web derivatives need approval | Production-weight pages |
| R11-U4 | `alt=""` on all screen images (no product descriptions in Figma) | Accessible product imagery in a real product |
| R11-U5 | 8 vectors without a raster comparison (byte-identical originals only) | Nothing (recorded) |
| R11-U6 | Empty icon slot `1608:7374` (Gallery Minimalistic, R9 out of scope) | Nothing |


---

**Superseded for final status (2026-11-20):** see `FINAL-PROJECT-COMPLETION-REPORT.md`, `FINAL-PENDING-ITEMS.md`, `FINAL-TEST-REPORT.md` and `FINAL-DESIGN-TEAM-ACTION-LIST.md` in this folder.
