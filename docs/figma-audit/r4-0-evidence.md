# R4-0 — Evidence Completion (read-only Figma inspection)

| Item | Value |
|---|---|
| Date | 2026-11-20 |
| File | `rM3ixSG6i3DFfKZFWuxzs4` (not modified) |
| Approval | R4-Q7 (approved), about 16 read-only inspections |
| Operations | **13 read-only calls:** `get_design_context` ×5 (screenshot excluded), `get_metadata` ×3, `get_variable_defs` ×5. No writes, screenshots, exports, downloads or annotations. The Tooltip set output (137k characters) was saved by the tool and parsed locally (0 extra calls). |
| Tags | **[APPLIED]** = rendered by `get_design_context` · **[META]** = `get_metadata` · **[BOUND]** = `get_variable_defs` · **[DERIVED]** = computed from those |

| # | Call | Node | Purpose |
|---|---|---|---|
| 1 | `get_design_context` | `1451:25092` Dropdown / Item set | All 40 Item variants (full code returned) |
| 2 | `get_design_context` | `1448:16825` Tooltip set | All 80 Tooltip variants (full code returned, parsed locally) |
| 3 | `get_design_context` | `1451:25521` Dropdown / Menu set | Variant list (sparse) |
| 4 | `get_design_context` | `1451:25415` Menu Single · Mobile · Light · Search On · Footer Label | Mobile spacing |
| 5 | `get_design_context` | `1454:1254` Menu Multiple · Desktop · Light · Search Off · Footer None | Multiple menu |
| 6 | `get_metadata` | `1448:88` Tooltip Desktop dark left Heading | Heading height check |
| 7 | `get_metadata` | `1446:32` Tooltip Desktop light left Text only | Arrow node type |
| 8 | `get_variable_defs` | `1446:32` | Tooltip bindings |
| 9 | `get_metadata` | `1454:7212` Multiple indicator (Selected) | Indicator structure |
| 10–12 | `get_variable_defs` | `1454:7202` / `1454:7212` / `1454:7215` | Multiple indicator colours (Default / Selected / Disabled) |
| 13 | `get_variable_defs` | `1451:24796` Single Selected icon | Check icon colour |

---

## 1. Dropdown / Item: all 40 variants [APPLIED]

| Platform | Row | Padding | Min-height | Gap | Radius | Label style |
|---|---|---|---|---|---|---|
| Desktop | 320 wide | **12 / 10** (x / y) | 40 | 12 | `Radius/8` | **Label Small — Medium 14/20** |
| Mobile | 352 wide | **12** (all sides) | **48** | 12 | `Radius/8` | **Body M — Regular 16/24** (not Label Small) |

Selection indicator: 20 × 20 box, left of the label, in every variant (`Selection indicator` nodes `1451:24783`…`1454:1253`).

| State (Light) | Fill | Label | Extra |
|---|---|---|---|
| Default | `Background/Secondary` `#f6f7f9` | `Text/Primary` `#0b0c0f` | — |
| Hover | `Background/Tertiary` `#edeff2` | `Text/Primary` | — |
| Focus | `Background/Secondary` | `Text/Primary` | 2px `Button/Primary/Border/Focus` `#003fbc` + `Button/Focus` effect |
| Selected | `Blue/50` `#f3f7ff` | `Blue/500` `#004feb` | Single: check icon; Multiple: checked indicator |
| Disabled | `Background/Secondary` | `Text/Tertiary` `#707a8f` | — |

Single and Multiple rows are **identical** except for the indicator (`1451:25072`–`25076` vs `1454:1190`–`1203`).

Dark (out of scope; recorded for B4-2):
- Default and Disabled fill `#181b21`; Hover `Background/Tertiary` = **`#1f242e`**.
- **Selected fill `Blue/500` `#004feb` with label `Base/White` `#fafcff`**.
- Labels `Text/Primary` = `#fafcff`.
- Focus is identical in structure.

## 2. Multiple-selection indicator [META + BOUND]

| State | Indicator node | Bound colour |
|---|---|---|
| Default / Hover / Focus | `1454:7202` / `1454:7205` / `1454:7208` | **`Brand/Icon/Secondary` `#555d6d`** (`1454:7202`) |
| Selected | `1454:7212` | **`Brand/Blue/500` `#004feb`** |
| Disabled | `1454:7215` | **`Brand/Border/Primary` `#bfc4cf`** |

- **It is an icon instance named "checkbox", not the R3 Checkbox component.**
- Structure (`1454:7212`): a 20 × 20 instance with two vectors: a box 13.33 × 13.33 at (3.33, 3.33) and a check 9.17 × 6.67 at (7.5, 5).
- The child IDs `I1454:7212;5:32040` and `5:32041` show the master lives in the `5:*` range, i.e. the **Brainstorming / research page (S4)** [DERIVED]. That is the same source issue as the Single check icon (`lucide:badge-check`, `5:15330`).
- It renders as an image, so the vector paths and stroke width are **not readable**.
- Tokens: `--annachy-color-icon-secondary`, `--annachy-color-blue-500`, `--annachy-color-border-primary` all exist in R1.
- **Consequence:** R4 does **not** reuse the R3 Checkbox (so the R3 D-27 glyph gap does not carry over). The indicator is an **icon slot** whose colour changes with state, like the Single check icon (`1451:24796` → `Blue/500`).

## 3. Dropdown / Menu [APPLIED / META]

All 48 variant IDs are listed in `1451:25521`:
- Single: `1451:25175`–`1451:25520`.
- Multiple: `1454:1254`–`1454:2149`.

### 3.1 Mobile spacing (`1451:25415`, Mobile Light Single Search On Footer Label, 352 × 366)

| Element | Value |
|---|---|
| Menu | padding 8, gap 8, `Radius/12`, 1px `Border/Primary`, `Background/Secondary`, width 352, clip (same as Desktop) |
| Search region | gap 8, padding-bottom 8; Input Field 48 tall, px 14, gap 6, `Radius/8`, 1px `Border/Primary`; icon User Curved 24; placeholder "Search teams" **Body M — Regular 16/24 `Text/Secondary` `#555d6d`**; divider 1px `Border/Secondary` |
| Options | gap 4; Mobile rows (§1) |
| Footer | padding-top 4, gap 12; divider 1px `Border/Secondary`; **button 48 tall, px 16, py 18, gap 8, `Radius/12`**, `Button/Primary/Background/Default`, label "Apply selection" **Label Medium — Medium 16/21** `Button/Primary/Content/Default` |

Desktop footer (from the audit, `1451:25250`): 40-tall Primary button, label Label Small Medium 14/20.

### 3.2 Multiple menu (`1454:1254`, Desktop Light, Search Off, Footer None, 320 × 188)

- Menu padding 8; **no gap** (it contains a single region); Options gap 4.
- Four sample rows: **two** Selected (independent selection, confirms F3), one Default, one Disabled.

## 4. Tooltip: all 80 variants [APPLIED, parsed locally from call 2]

### 4.1 Body and typography

| Device · Format | Size [META / APPLIED] | Text style | Colour (dark / light) |
|---|---|---|---|
| Mobile · Text only | hug, max-width 300 (182 × 38 at the default text) | **Body S - Semi** (`XS-Semibold` vars) 14/18, 600 | `Base/White` on `Base/Black` / `Base/Black` on `Base/White` |
| **Desktop · Text only** | hug, max-width 300 (**157 × 38**) | **Body XS — Medium 12/18, 500** (`1446:34`; R1 `--annachy-type-body-xs-*`) | same |
| Mobile · Heading | **fixed 260 × 62**, gap 4 | heading **H7 — Semibold 16/18**; description **Body S — Regular 14/20** | same |
| Desktop · Heading | **fixed 240 × 59**, gap 4 | heading Body S - Semi 14/18; description **Label XSmall — Regular 12/17** | same |

- All variants: padding 10, raw radius 4, `max-width: 300`, **no border or shadow**.
- Heading variants have a **fixed height in all 40** (verified via `1448:88` [META] 240 × 59), so text clips (TT5 applies to Mobile too: 62).
- Text uses `min-width: 100%`, `width: min-content`, with word breaking: it **wraps** inside the 300 max.
- **TT7 resolved:** Desktop Text-only is narrower because it uses **12px Body XS Medium** where Mobile uses 14px Body S-Semi.
- Variant node IDs:
  - Desktop light Text-only `1446:32`–`1446:59`;
  - Mobile light Text-only `1429:16131`, `1429:16137`, `1430:5150`, `1433:16214`–`1433:16304`;
  - Heading `1448:8`–`1448:164`.

### 4.2 Arrow: all 10 positions [APPLIED + META]

- **Node:** a `regular-polygon` "Polygon 1", 20 × 20 (`1446:33` [META]).
- **Fill:** bound to the body colour: `Base/White` (light) or `Base/Black` (dark) (`1446:32` [BOUND]).
- **Visible polygon:** inside the 20 × 20 box at insets **top 5%, right 10.35%, bottom 25%, left 10.35%**, i.e. 15.86 × 14 [DERIVED], pointing toward the trigger. This is the same in all 80 variants.

| Arrow | Arrow box position (relative to the body) | Transform | Example nodes (Desktop light Text / Mobile light Text / Desktop light Heading) |
|---|---|---|---|
| left | `left: −13px; top: 9px` | rotate −90° | `1446:32` / `1429:16131` / `1448:128` |
| left center | `left: −13px; top: 50%; translateY(−50%)` (Heading Desktop: `top: calc(50% + 0.5px)`) | rotate −90° | `1446:35` / `1433:16300` / `1448:132` |
| right | `right: −13px; top: 9px` | rotate −90° + scaleY(−1) | `1446:38` / `1429:16137` / `1448:136` |
| right center | `right: −13px; top: 50%; translateY(−50%)` (Heading Desktop: `+0.5px`) | rotate −90° + scaleY(−1) | `1446:41` / `1433:16303` / `1448:140` |
| top | `top: −13px; left: calc(50% − 0.5px)` (Desktop Text) / `calc(50% − 1px)` (Mobile Text, Desktop Heading); translateX(−50%) | rotate 180° + scaleY(−1) | `1446:44` / `1430:5150` / `1448:144` |
| top left | `top: −13px; left: 12px` | rotate 180° + scaleY(−1) | `1446:47` / `1433:16248` / `1448:148` |
| top right | `top: −13px; right: 12px` | rotate 180° + scaleY(−1) | `1446:50` / `1433:16251` / `1448:152` |
| bottom | `bottom: −13px; left: calc(50% − 0.5px)` / `calc(50% − 1px)`; translateX(−50%) | rotate 180° | `1446:53` / `1433:16214` / `1448:156` |
| bottom left | `bottom: −13px; left: 12px` | rotate 180° | `1446:56` / `1433:16220` / `1448:160` |
| bottom right | `bottom: −13px; right: 12px` | rotate 180° | `1446:59` / `1433:16239` / `1448:164` |

- **Arrow side = the side of the tooltip body the arrow sits on.** So `Arrow=left` has the arrow on the left edge, and the tooltip is placed to the **right** of its trigger. This confirms the T7 reading.
- "left" and "right" are anchored 9px from the top (the first-line position), not centred; "center" variants are centred.
- The ±0.5px / 1px centring offsets differ between variants. They are reproduced per variant, not normalised.
- **Not readable:** the polygon's point count and corner rounding (it renders as an image; the metadata type is `regular-polygon`, Figma's default is 3 points). The bounding insets and orientation **are** known.

## 5. Gap status after R4-0

| Gap (behaviour spec §3) | Status |
|---|---|
| G9 Multiple-selection indicator | ✅ **Resolved:** an icon instance (S4 research source), not the R3 Checkbox; state colours bound (§2). Icon geometry is image-only, so it ships as a slot (same as G8) |
| G10 Mobile spacing | ✅ **Resolved** (§1, §3.1) |
| G11 Tooltip Desktop text-only sizing | ✅ **Resolved:** Body XS Medium 12/18 (§4.1) |
| G12 Tooltip arrow positions | ✅ **Positions, offsets, rotations and polygon bounds resolved** (§4.2); ⚠ the polygon's exact shape (point count, corner radius) is **UNKNOWN** |
| New: Mobile footer button (48 tall, Label Medium) | Recorded (§3.1). It is a **Button variant not in All Buttons** (48 / px 16 / py 18 / `Radius/12` matches Button size 48, but the label typography is overridden): reproduced as an override, like D4 |
| New: heading tooltips fixed height on Mobile too (62) | TT5 extended to Mobile |

## 6. R4-1 preparation (2026-11-20) [META]

Read-only `get_metadata` ×2. **R4-0 total: 15 read-only calls.**

| Node | Variant | Size | Indicator | Text |
|---|---|---|---|---|
| `1451:25074` | Item Single Desktop Light **Focus** | **320 × 40** | x 12, y 10, 20 × 20 | x 44, y 10, 264 × 20 |
| `1451:25084` | Item Single Mobile Light **Focus** | **352 × 48** | x 12, y 14, 20 × 20 | x 44, y 12, 296 × 24 |

The Focus variants keep the Default size and content position, so **the 2px focus stroke is not part of the layout**: it is drawn as an inset stroke plus the outer `Button/Focus` effect [DERIVED].

## 7. Element node index (cited in `dropdown.css` / `tooltip.css`)

Added by the R4 closure audit (AUD-2, 2026-11-20). Every node below appears in the recorded read-only outputs listed in the call table at the top of this file. There were no new Figma calls.

| Node | Element | Source call |
|---|---|---|
| `1066:38094` | Input Field inside the Dropdown search field (instance `I1451:24296;1066:38094`) | #4 `1451:25415` |
| `1451:24295` | Search region (gap 8, padding-bottom 8) | #4 |
| `1451:24341` | Search divider (1px `Border/Secondary`) | #4 |
| `1451:24342` | Options container (gap 4) | #4 |
| `1451:25075` | Item Single · Desktop · Light · **Selected** | #1 `1451:25092` |
| `1451:25082` | Item Single · **Mobile** · Light · Default | #1 |
| `1451:25355` | Menu Single · Mobile · Light · Search Off · Footer None (352 × 220) | #3 `1451:25521` |
| `1429:16129` | Tooltip Mobile light Text-only text node (Body S-Semi 14/18) | #2 `1448:16825` |
| `1429:16178` | Tooltip Mobile · dark · top · Text only (centring `calc(50% − 0.43px)`) | #2 |
| `1448:104` | Tooltip Desktop · dark · top · Heading (centring `calc(50% − 0.43px)`) | #2 |
| `1448:130` | Tooltip Desktop heading description node (Label XSmall Regular 12/17) | #2 |
