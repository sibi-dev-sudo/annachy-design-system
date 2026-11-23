# Design Team Action List (changes that must happen in the Figma file or outside the project)

File: `rM3ixSG6i3DFfKZFWuxzs4`. The web project never modifies Figma, so every item below needs the Design Team, the file owner or legal.
After each Figma fix, the web side re-exports and revalidates only that item (estimates in `08-final-completion-report.md` §4).

## 1. Fix in Figma

| # | Item | Where | What to do | Web follow-up |
|---|---|---|---|---|
| D1 | **FIG-ICON-1**: artwork outside the variant frame | Icons page `1801:5142`, Filled Arrow: Swap Square, Swap Square 4, Turn Down Square, Turn Up Circle, Turn Up Square | Move each artwork back inside its variant frame | Re-export 5 sets (~15 min) |
| D2 | Desktop frame with no readable content | `1608:9891` "Desktop" (1440 × 1073, Sample Screen page) | Detach or repair the frame so its children are readable, or confirm it is intentionally empty / obsolete | Reproduce, or delete the empty page |
| D3 | Empty Figma renders | 13 nodes (e.g. galleries `1280:10749`, `1280:10762`; cards `1280:10699`–`10702`; `1608:7497`, `1608:7526`–`7529`) return a 1 × 1 export | Check for hidden or zero-opacity wrappers, or fills outside the frame | Re-run the visual comparison for 34 placeholders |
| D4 | Dashed lines: dash phase and direction (R10-U1, U2) | 7 dashed artworks; 3 vertical lines `1375:30933`, `1375:30937`, `1608:7363` | Confirm the intended dash start and line direction | Update 7 artworks |
| D5 | Artworks that export empty (R10-U3) | `1375:31076`, `1608:7272`, `I1608:7274;1548:33550`, `I1608:7348;1548:33550` | Remove the empty layers or give them visible strokes | Re-export if they become visible |
| D6 | Unbound / raw values | Input focus border `#3a6ff7` (IN2); 7 divider lines with unbound colour variables | Bind to library variables if these are meant to be tokens | Token mapping update |
| D7 | Contrast findings | A04, A14, A16 (placeholder 1.25:1), A38, A39 (Toggle Off 1.04:1), A40 (light tooltip 1.00:1), A41 | Decide whether to adjust; current values are reproduced as designed | Token or component update |
| D8 | Not-required icon slots still in the screens | Solar (70 slots), Brainstorming `5:26` (24), Gallery Minimalistic (2) | Either remove these layers from the approved screens, or supply Annachy-owned replacements and approve their export | Remove the empty slots or integrate the replacements |
| D9 | Missing design-system sources | Navigation pages are empty; no Select trigger component | Design them if required | Implement |

## 2. Rights, licences and ownership (owner / legal)

| # | Item | Needed |
|---|---|---|
| L1 | 43 R11 raster images | For each image: confirm ownership or licence, or supply a replacement. AI-generated (8): approval for use. SKU-named photos (12): confirm the photography is Annachy's own or licensed. Web downloads (8), screenshot (1), emoji (1), unattributed (13): source and licence |
| L2 | Proxima Nova | A web-font licence and WOFF2 files (weights 300, 400, 500, 600, 700), or an Adobe Fonts web project. The project is ready to add them without typography changes |
| L3 | Iconly | The licence text and account tier for the purchased library |
| L4 | Five third-party brand logos ("logo 2", Desktop PDP related products) | Rights or authorised files, or remove or replace them in the design |
| L5 | Annachy logotype, screen icons, R10 vectors | Confirm company ownership (assumed; not independently verified) |
| L6 | Image `62f2c` (9.05 MB) | Accept a measured web copy, or supply a smaller master |

## 3. Confirmations requested

| # | Question |
|---|---|
| C1 | Status bar and phone chrome are treated as not applicable (phone system UI). Please confirm |
| C2 | Seven desktop card stars now reuse the Annachy star artwork already used in the mobile cards (Figma code references the same artwork `c6cc8`). Please confirm this is acceptable within the "Solar not required" decision |
