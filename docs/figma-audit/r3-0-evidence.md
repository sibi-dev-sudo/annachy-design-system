# R3-0 — Evidence Completion (read-only Figma inspection)

| Item | Value |
|---|---|
| Date | 2026-11-19 |
| File | `rM3ixSG6i3DFfKZFWuxzs4` (not modified) |
| Operations | `get_design_context` (screenshot excluded), `get_metadata`, `get_variable_defs` — all read-only. No downloads/exports. `create_session` not used. |
| Plan | `docs/implementation/r3-components-spec.md` §5 |
| Tag | **[APPLIED]** = value rendered by `get_design_context`; **[META]** = `get_metadata`; **[BOUND]** = variable binding |

---

## 1. Button (All Buttons) — sizes 26–52 [APPLIED]

| Size | Node | Height | Padding (x / y) | Gap | Radius | Text style | Font / LH |
|---|---|---|---|---|---|---|---|
| 26 | `887:339` | `Height/26` | 10 / 4 | 4 | `Radius/4` | Body XS — Semibold (`XXS-Semibold` vars) | 12 / 18 |
| 28 | `887:344` | `Height/28` | 10 / **8** | 4 | `Radius/4` | Body S - Semi (`XS-Semibold` vars) | 14 / 18 |
| 36 | `887:354` | `Height/36` | **12 / 10** | **6** | `Radius/8` | H7 — Semibold | 16 / 18 |
| 38 | `887:359` | `Height/38` | **14 / 10** | 6 | `Radius/8` | H7 — Semibold | 16 / 18 |
| 42 | `887:369` | `Height/42` | 16 / 12 | 6 | `Radius/12` | H7 — Semibold | 16 / 18 |
| 46 | `887:374` | `Height/46` | **16 / 16** | 8 | `Radius/12` | H6 — Semibold (`Line Height 2`) | 18 / 20 |
| 52 | `887:384` | `Height/52` | **18 / 18** | 8 | `Radius/12` | H5 — Semibold | 20 / 24 |

Combined with Phase 4 (24, 32, 40, 48, 56) the full size table is now complete — see §7.

## 2. Button Secondary Default border [APPLIED]

`887:664` (Secondary, Default, 40): **`border: 1px solid Brand/Button/Secondary/Border/Default #004feb`**, no background, padding 16/12, gap 6, `Radius/8`. → Secondary Focus (`887:784`, 2px same colour) differs from Default by **border width 1 → 2px only** (confirms B2).

## 3. Button focus border widths [APPLIED]

| Type | Node | Focus border |
|---|---|---|
| Secondary Grey | `887:1084` | **2px** `Button/Secondary-Grey/Border/Focus` `#004feb`; no fill; content `#1f242e` |
| Tertiary | `887:1384` | **2px** `Button/Tertiary/Border/Focus` `#004feb`; no fill |
| Tertiary Grey | `887:1684` | **2px** `Button/Tertiary Grey/Border/Focus` `#004feb`; no fill |
| Link | `887:1984` | **2px** `Button/Link/Border/Focus` `#004feb`; no fill |

All Focus variants keep padding 16/12, gap 6, `Radius/8` (size 40). With Primary/Secondary (Phase 4) all six types now confirmed: **Focus = 2px border**.

## 4. Button Loading [APPLIED + BOUND]

- `887:2163` "Loading Dots" renders as a single vector image (3 ellipses 6×6 at x 0/11/22, `887:2164–2166`).
- Dot fill bound: `887:2164` → **`Brand/Button/Primary/Content/Loading` `#fafcff`** [BOUND].
- Loading variables per type (size 40) [BOUND] — **4 extra read-only `get_variable_defs` calls beyond the 60-call plan** (`887:2282`, `887:2342`, `887:2402`, `887:2462`) plus `887:2162`, `887:2222`:

| Type | Node | Content/Loading (dots) | Background/Loading | Border |
|---|---|---|---|---|
| Primary | `887:2162` | `Brand/Button/Primary/Content/Loading` `#fafcff` | `Primary/Background/Default` `#004feb` | — |
| Secondary | `887:2222` | `Brand/Button/Secondary/Content/Loading` `#004feb` | `Brand/Button/Secondary/Background/Loading` `#fafcff` | `Secondary/Border/Default` |
| Secondary Grey | `887:2282` | `Brand/Button/Secondary-Grey/Content/Loading` `#1f242e` | `Brand/Button/Secondary-Grey/Background/Loading` `#fafcff` | `Secondary-Grey/Border/Default` |
| Tertiary | `887:2342` | `Brand/Button/Tertiary/Content/Loading` `#004feb` | — | — |
| Tertiary Grey | `887:2402` | `Brand/Button/Tertiary Grey/Content/Loading` `#1f242e` | — | — |
| Link | `887:2462` | `Brand/Button/Link/Content/Loading` `#004feb` | — | — |

**New variables not in the R1 token set (7):** `Brand/Button/Secondary/Content/Loading`, `Brand/Button/Secondary/Background/Loading`, `Brand/Button/Secondary-Grey/Content/Loading`, `Brand/Button/Secondary-Grey/Background/Loading`, `Brand/Button/Tertiary/Content/Loading`, `Brand/Button/Tertiary Grey/Content/Loading`, `Brand/Button/Link/Content/Loading`. → R1 token addendum required before R3-1 (see plan).

## 5. Button (gradient) — states at size 40 [APPLIED]

Common: height `Height/40`, padding-x **12** (no padding-y), gap **8**, radius **8 (raw)**, label H7 — Semibold 16/18. Shadows are emitted by `get_design_context` as CSS `drop-shadow()` (blur = Figma radius ÷ 2 — same style as the size-24 `box-shadow`, `1153:3371`).

| State | Node | Border | Background | Shadow | Label colour |
|---|---|---|---|---|---|
| Default | `1153:3621` | 1.5px `Brand/Blue/300` `#99b9f7` | `linear-gradient(28.425170856311397deg, Gradient/Color 1 13.397%, Gradient/Color 2 86.603%)` | drop-shadow `-2px 4px 1px rgba(23,25,28,0)`, `-1px 3px 0.5px rgba(23,25,28,.02)`, `-1px 2px 0.5px rgba(23,25,28,.08)`, `0 1px 0.5px rgba(23,25,28,.13)` | `Brand/Base/White` |
| Hover | `1153:3631` | 1.5px `Blue/300` | `linear-gradient(-20.615418727966116deg, rgba(23,70,162,0.85) 9.5862%, rgba(58,111,247,0.92) 76.342%)` — **raw colours** (`#1746a2` @85 %, `#3a6ff7` @92 % — the lowercase `gradient-start`) | drop-shadow `0 0 1.5px rgba(50,92,179,.01)`, `0 0 1.5px rgba(50,92,179,.05)`, `0 0 1.5px rgba(50,92,179,.16)`, `0 0 1px rgba(50,92,179,.27)`, `0 0 0.5px rgba(50,92,179,.31)` | `Brand/Text/White` |
| Focus | `1153:3641` | **2px `Brand/Blue/500` `#004feb`** | `linear-gradient(-4.625122076747715deg, Blue/600 43.833%, Blue/400 94.947%)` | none | `Brand/Text/White` |
| Pressed | `1153:3651` | 1.5px `Blue/300` | `linear-gradient(28.425170856311397deg, Blue/500 13.397%, Gradient/Color 2 86.603%)` | drop-shadow `1px 2px 3px rgba(0,79,235,.12)`, `0 4px 6px rgba(0,79,235,.4)` | `Brand/Base/White` |
| Disabled | `1153:3661` | 1.5px `Blue/300` | `linear-gradient(28.425170856311397deg, Blue/500 @ 19 % 13.397%, Gradient/Color 2 @ 19 % 86.603%)` | none | `Brand/Button/Primary/Content/Disabled` `#fafcff` |

**Gradient angle is size-dependent** in CSS output (Default: 22.57° @24, 23.41° @32, 28.43° @40, 28.99° @48, 31.87° @56) because Figma stores the gradient as a transform relative to the box. CSS must reproduce per-size angles (or an equivalent transform); a single `--annachy-gradient-brand` (22.57°) is exact only for size 24.

## 6. Button (gradient) — sizes [APPLIED]

| Size | Node | Padding-x | Gap | Radius (raw) | Text style | Font / LH | Angle (Default) |
|---|---|---|---|---|---|---|---|
| 24 | `1153:3371` (Phase 4) | 8 | 4 | 4 | Body XS — Semibold | 12 / 18 | 22.572274294652743° |
| 32 | `1153:3521` | 12 | 8 | 8 | **H7 — Semibold** (All Buttons 32 uses Body S-Semi) | 16 / 18 | 23.413224071387774° |
| 40 | `1153:3621` | 12 | 8 | 8 | H7 — Semibold | 16 / 18 | 28.425170856311397° |
| 48 | `1153:3771` | 16 | **12** | 12 | **Subheading L — Semibold** (`Subheading & Body/Subheading/L/*`) | 18 / 25 | 28.99768564862803° |
| 56 | `1153:3871` | 16 | 12 | 12 | H5 — Semibold | 20 / 24 | 31.87177113855379° |

Sizes **26, 28, 36, 42, 46, 52** remain uninspected (not in the 60-call plan).

New text-style binding: **Subheading L — Semibold** (Scale A row `1558:48989`, Mobile 18/25) is bound by the gradient button — previously DOC-only; R1 token `--annachy-type-subheading-l-*` already covers its values.

## 7. Input — sizes [APPLIED + META]

| Size | Node | Field height | Padding-x | Gap | Top Section height | Root width | Method |
|---|---|---|---|---|---|---|---|
| 46 | `1066:37999` (field `1066:38004`) | 46 | **14** | 6 | 88 | 336 | APPLIED |
| 48 | `1066:38089` (Phase 4) | 48 | 14 | 6 | 90 | 337 | APPLIED |
| 50 | field `1066:38184` | 50 | **14** | 6 | — | 337 | META: icon x = 15 = 14 padding + 1px stroke included in layout; icon y = 13 = (50 − 24)/2 |
| 54 | field `1066:38274` | 54 | **14** | 6 | — | 337 | META: icon x = 15, y = 15 = (54 − 24)/2 |
| 56 | `1066:38359` (field `1066:38364`) | 56 | **14** | 6 | 98 | 336 | APPLIED |

Padding-x 14 and gap 6 are **constant across all sizes**; only field height changes. Right-icon group: gap 8, width 56 (2 × 24 + 8). Top Section height = field height + 42. Note: `get_metadata` was used instead of `get_design_context` for 50/54 (same evidence, smaller payload).

## 8. Input / Outline — remaining states @48/R8 [APPLIED]

| State | Node | Label | Description | Field border | Value / placeholder | Sub-text |
|---|---|---|---|---|---|---|
| Filled | `1066:38989` | `Blue-Black/500` `#121417` (container colour) | `Blue-Black/500` | 1px **`Brand/Base/Black` `#0b0c0f`** | `Brand/Base/Grey` `#1f242e` | `Blue-Grey/900` `#15181e` |
| Disabled | `1066:39439` | **`Blue-Grey/200` `#dcdfe5`** | **`Blue-Grey/100` `#edeff2`** | 1px **`Blue-Grey/200`** | `Blue-Grey/200` | **`Blue-Grey/100`** |
| Success | `1066:40339` | `Blue-Black/500` | `Blue-Black/500` | 1px **`success` `#276732`** | `Base/Grey` | **`success`** |

No field fill in any Outline state. Error-circle icon present in all three (confirms IN5). Disabled root width 336 (others 337).

## 9. Input / Filled — remaining states @48/R8 [APPLIED]

| State | Node | Label | Description | Field fill | Field border | Value / placeholder | Icons | Sub-text |
|---|---|---|---|---|---|---|---|---|
| Hover | `1066:43333` | `Blue-Grey/800` | `Blue-Grey/700` | `Background/Secondary` `#f6f7f9` | 1px **`Blue/500` `#004feb`** | **`Blue-Grey/400` `#98a0ae`** | opacity **30 %** | `Blue-Grey/500` |
| Filled | `1066:41633` | `Blue-Black/500` | `Blue-Black/500` | `Background/Secondary` | 1px **`Blue-Grey/300` `#bfc4cf`** | **`Blue-Black/50` `#202d47`** | 100 % | `Blue-Grey/900` |
| Error | `1066:42483` | `Blue-Black/500` | `Blue-Black/500` | `Background/Secondary` | 1px **`error` `#e72b23`** | `Base/Grey` `#1f242e` | 100 % | **`error`** |
| Disabled | `1066:42058` | `Blue-Grey/200` | `Blue-Grey/100` | **none** | 1px `Blue-Grey/200` | `Blue-Grey/200` | 30 % | `Blue-Grey/100` |
| Success | `1066:42908` | `Blue-Black/500` | `Blue-Black/500` | `Background/Secondary` | 1px **`success` `#276732`** | `Base/Grey` | 100 % | **`success`** |

Filled set — complete state matrix now known (Default/Focused from Phase 4). Notes: Filled **Disabled has no fill** (only Filled state without `Background/Secondary`); icon slots are 30 % opacity in Default, Hover, Disabled and 100 % in Focused, Filled, Error, Success; slot wrappers have `border-radius: 4px` (raw) and sub-text icon wrapper `border-radius: 7px` (raw).

## 10. Checkbox [APPLIED + META]

| Variant | Node | Box | Box fill | Box border | Radius | Glyph | Effect | Label / subtext |
|---|---|---|---|---|---|---|---|---|
| Checked · Small | `1504:53311` | **20 × 20** | `Button/Primary/Background/Default` | 1px `Blue/300` | `Radius/4` | `functional/check` **16 × 16** | `Button/Default` | Label Medium 16/21 `Text/Primary`; Body S 14/20 `Text/Tertiary` w184 (same as Medium) |
| Checked · Medium | `1504:53701` (Phase 4) | 24 × 24 | same | 1px `Blue/300` | `Radius/4` | check **20 × 20** | `Button/Default` | same |
| Checked · Large | `1504:54091` | **28 × 28** | same | 1px `Blue/300` | `Radius/4` | check **20 × 20** | `Button/Default` | same |
| Multi-select · Medium | `1504:53761` | 24 | same | 1px `Blue/300` | `Radius/4` | **`functional/remove`** 20 × 20 | `Button/Default` | same |
| Unchecked · Medium | `1504:53819` | 24 | `surface-bg` (`white`) | **2px** `border-default` `#e1e1e2` | `Radius/4` | — | none | same |
| Disabled · Medium | `1504:53867` | 24 | `Blue-Grey/100` `#edeff2` | **2px** `Blue-Grey/200` `#dcdfe5` | `Radius/4` | — | none | label & subtext **`Blue-Grey/200`** |

- Label typography and 12px label padding **do not change with Size** — only the box (20/24/28) and glyph (16/20/20) change.
- Glyphs are rendered as images by `get_design_context`; `get_metadata` on `functional/check` `1504:53703` returns a 20 × 20 frame **with no child shapes** → glyph geometry and fill colour are **not readable** with read-only tools (D-27 remains for check and remove glyphs).

## 11. Checkbox / Radio / Toggle — layouts [APPLIED + META]

| Variant | Node | Finding |
|---|---|---|
| Checkbox Checked · Medium · **Position=Right** · Center | `1504:53731` | Order: Content → control. Text containers use **padding-right 12** (instead of padding-left 12). Root `align-items: center`. |
| Checkbox Checked · Medium · Left · **Alignment=Top** | `1504:53691` | Root `align-items: flex-start` (control at top). |
| Radio Selected · Medium · Right · Center | `1504:52712` | Content (196) then control at x 196, y 8.5; text x 0 (right padding). |
| Radio Selected · Medium · Left · Top | `1504:52676` | Control at y 0. |
| Toggle On · Medium · Right · Center | `1504:55717` | Content then Toggle Container at x 196, y 10.5. |
| Toggle On · Medium · Left · Top | `1504:55672` | Toggle Container at y 0. |

`Alignment=Bottom` was not inspected (not in plan); by naming it is `flex-end` — **unverified**.

## 12. Radio [APPLIED + META + BOUND]

| Variant | Node | Control | Selected rendering | Dot |
|---|---|---|---|---|
| Selected · Small | `1504:52373` (container `1504:52374`) | 20 × 20 | vector image (render extends for shadow) | ellipse **8 × 8 at (6, 6)** `1504:52375` |
| Selected · Medium | container `1504:52686` | 24 × 24 | vector image | ellipse **10 × 10 at (7, 7)** `1504:52687` |
| Selected · Large | `1504:52997` (container `1504:52998`) | 28 × 28 | vector image | ellipse **12 × 12 at (8, 8)** `1504:52999` |
| Unselected · Medium | `1504:52738` | 24 × 24, **radius 12 (raw, full circle)** | fill `surface-bg` (`white`), **2px** `border-default` `#e1e1e2` | — |

Bindings [BOUND]: Selected container `1504:52686` → `Button/Primary/Background/Default` `#004feb`, `Blue/300` `#99b9f7`, `Background/Primary`, effect `Button/Default`; dot `1504:52687` → **`Brand/Background/Primary` `#fafcff`**.
→ Selected = filled circle `#004feb` with `Blue/300` stroke and a `#fafcff` dot (8/10/12). **Selected ring stroke width not returned** (rendered as image) — unresolved.
Label typography identical across sizes (Label Medium 16/21, as Checkbox).

## 13. Toggle [META + BOUND]

| Size | Node (On / Off) | Root | Track | Thumb | Thumb x (Off → On) | Focus Ring layer (hidden) | Label style [BOUND] |
|---|---|---|---|---|---|---|---|
| Small | `1504:54472` / `1504:54487` | 228 × 40 | **32 × 16** | **12 × 12**, y 2 | 2 → **18** | 40 × 24 at (−4, −4) | **Label Small — Medium 14/20** |
| Medium | `1504:54622` / `1504:54637` | 234 × 41 | 38 × 20 | **16 × 16**, y 2 | 2 → **20** | 46 × 28 at (−4, −4) | Label Medium — Medium 16/21 |
| Large | `1504:54772` / `1504:54787` | 240 × 42 | **44 × 24** | **20 × 20**, y 2 | 2 → **22** | 52 × 32 at (−4, −4) | **Label Large — Medium 18/22** |

Thumb inset is 2px on all sides in every size. Track radius: not returned (pill shape visually; **unverified value**).

Bindings per element [BOUND]:
| Element | Node | Variables |
|---|---|---|
| Track (On) | `1504:54624` | fill `Button/Primary/Background/Default` `#004feb` (+ thumb's vars listed as descendants) |
| Track (Off) | `1504:54639` | fill **`Blue-Grey/50` `#f6f7f9`** |
| Thumb | `1504:54625` | fill `Button/Primary/Content/Loading` `#fafcff`, **`Blue-Grey/100` `#edeff2`** (stroke, width not returned), effect `Toggle/On` (On) / `Toggle/Off` (Off) |
| Focus Ring | `1504:54626` | **no variables; hidden in all inspected variants including Focus On** |

States [BOUND]:
| State | Node | Track | Extra |
|---|---|---|---|
| Off | `1504:54637` | `Blue-Grey/50` | thumb `Toggle/Off` |
| Focus Off | `1504:54697` | `Blue-Grey/50` | **`Button/Primary/Border/Focus` `#003fbc`**, `Blue-Grey/200` |
| Pressed Off | `1504:54727` | `Blue-Grey/50` | `Blue-Grey/300` |
| Focus On | `1504:54682` (META) | — | thumb x **18.5** (vs 20 in On) — focus ring layer still hidden |

Focus treatment element and stroke widths (Focus Off `#003fbc`, Pressed Off `Blue-Grey/300`) **not returned** — unresolved.

## 14. Selection Controls wrapper [META]

| Variant | Node | Content |
|---|---|---|
| Radio Button | `1504:57174` | single instance "Control" 216 × 41 |
| Checkbox | `1504:57176` | single instance "Control" 216 × 41 |
| Toggle | `1504:57178` | single instance "Control" 228 × 40 |

Each wrapper variant is **one instance of the core set's Small variant** (216/216/228 widths = Small). → Wrapper is an alias, no own styling. **Corrects `selection-controls.md` SC1**: the 14/20 label is the Toggle *Small* style, not a wrapper-specific inconsistency.

---

## 15. Call log

| Operation | Count | Notes |
|---|---:|---|
| `get_design_context` (screenshot excluded) | 41 | |
| `get_variable_defs` | 18 | incl. 4 Loading-type checks and 6 element-level binding checks beyond plan |
| `get_metadata` | 20 | used instead of `get_design_context` where geometry/structure sufficed (Input 50/54, Toggle, layouts, wrapper) |
| **Total** | **79** | Plan: 60. All planned nodes covered; extra calls were read-only, smaller payloads. Counts verified from the session transcript: only these three tools were invoked — no writes, no `download_assets`, no `get_screenshot`, no `create_session`. |

## 16. Gap resolution summary

| Gap (plan §4) | Status |
|---|---|
| Button padding/gap 26–52 | ✅ Resolved (§1) |
| Button Secondary default border | ✅ 1px (§2) |
| Button focus widths (4 types) | ✅ 2px (§3) |
| Button Loading dot colour | ✅ per-type `Content/Loading` (§4) — **7 new variables → R1 token addendum** |
| Gradient states @40 | ✅ (§5) |
| Gradient sizes 32/48/56 | ✅ (§6); 26/28/36/42/46/52 ❌ not inspected |
| Gradient CSS angle | ⚠ Size-dependent (§5) — implementation must use per-size angles |
| Input padding all sizes | ✅ 14 constant (§7) |
| Input Outline Filled/Disabled/Success mapping | ✅ (§8) |
| Input Filled Hover/Filled/Error/Disabled/Success mapping | ✅ (§9) |
| Checkbox Small/Large | ✅ 20/28 box, 16/20 glyph (§10) |
| Checkbox Unchecked/Disabled border width | ✅ 2px (§10) |
| Checkbox check / indeterminate glyph geometry | ❌ Image-only — not readable (D-27) |
| Checkbox/Radio/Toggle Right & Top layouts | ✅ (§11); Bottom ❌ unverified |
| Radio Small/Large | ✅ 20/28 (§12) |
| Radio selected geometry | ✅ dot 8/10/12, colours (§12); ring stroke width ❌ |
| Toggle Small/Large track | ✅ 32×16 / 44×24 (§13) |
| Toggle thumb size/inset/travel | ✅ 12/16/20, inset 2, travel (§13) |
| Toggle Off / Focus Off / Pressed Off | ✅ colours (§13); stroke widths & focus element ❌ |
| Toggle track radius | ❌ not returned |
| Toggle label per size | ✅ Label Small / Medium / Large (§13) — new finding |
| Wrapper styling | ✅ alias of Small variants (§14) |

---

# R3-0b — Follow-up inspection (2026-11-19, owner-approved)

Read-only only: `get_design_context` ×13 (screenshot excluded; one call on the set `1153:3370` returned sparse metadata only), `get_metadata` ×3. No writes, exports, downloads, screenshots or `create_session`. **Running total R3-0 + R3-0b: 95 read-only calls.**

## 17. Button (gradient) — remaining sizes, Default state [APPLIED]

Variant frame sizes from the set metadata (`1153:3370`): widths 24→100, 26→106, 28→106, 32→128, 36→128, 40→128, 42→144, 46→150, 48→150, 52→156, 56→156.

| Size | Node | Padding-x | Gap | Radius (raw) | Text style (bound) | Font / LH | Angle (Default) |
|---|---|---|---|---|---|---|---|
| 26 | `1153:3421` | 8 | 4 | 4 | **Body S - Semi** (`XS-Semibold` vars) | **14 / 18** | 23.01785504830842° |
| 28 | `1153:3471` | 8 | 4 | 4 | Body S - Semi | 14 / 18 | 24.585177137095087° |
| 36 | `1153:3571` | 12 | 8 | 8 | H7 — Semibold | 16 / 18 | 25.97253216191386° |
| 42 | `1153:3671` | 16 | 12 | 12 | H7 — Semibold | 16 / 18 | 26.80205998706895° |
| 46 | `1153:3721` | 16 | 12 | 12 | **Subheading L — Semibold** | 18 / 25 | 27.975552641534833° |
| 52 | `1153:3821` | 16 | 12 | 12 | H5 — Semibold | 20 / 24 | 29.999999554707948° |

All: 1.5px `Blue/300` border, Default 4-layer drop-shadow (as §5), label `Base/White`, `Height/N`.
→ Gradient **26 uses 14/18** while All Buttons 26 uses 12/18 — a Figma inconsistency, reproduced (flag **GB-1**).

## 18. Button (gradient) — state angle samples [APPLIED]

| Node | Size × State | Angle | Text style | Other |
|---|---|---|---|---|
| `1153:3381` | 24 Hover | −16.114435203849098° | Body XS — Semibold (`XXS-Semibold` vars) 12/18 | Hover shadow, raw rgba gradient as §5 |
| `1153:3881` | 56 Hover | −23.370501918258° | H5 — Semibold 20/24 | as §5 |
| `1153:3391` | 24 Focus | −3.5552594168066634° | **Label XSmall Semibold 12/17** | 2px `Blue/500`, `Blue/600`→`Blue/400`, no shadow |
| `1153:3891` | 56 Focus | −5.309282402526279° | H5 — Semibold | as §5 |
| `1153:3401` | 24 Pressed | 22.572274294652743° (= Default 24) | Body XS — Semibold 12/18 | Pressed shadow, `Blue/500`→`Color 2` |
| `1153:3911` | 56 Disabled | 31.87177113855379° (= Default 56) | H5 — Semibold | 19 % alpha stops; label `Button/Primary/Content/Disabled` |

### 18.1 Gradient angle rule [DERIVED — verified against every inspected variant]

With the variant frame `W × H`, every CSS angle emitted by Figma satisfies **tan θ = k · H / W**:

| State(s) | k | Checked at | Max error |
|---|---|---|---|
| Default, Pressed, Disabled | **√3 = 1.7320508** | Default all 11 sizes; Pressed 24, 40; Disabled 40, 56 | 5e-7° |
| Hover | **−1.2037838** (identical at 24/40/56) | 24, 40, 56 | 1e-14° |
| Focus | **−0.2588781** (identical at 24/40/56) | 24, 40, 56 | 1e-14° |

So Figma's gradient is a fixed direction in the button's normalised box. A fixed CSS angle is only exact at the documented frame width. The implementation uses the measured or derived angle for each size at the documented width and flags the dependence on label width (**GB-2**).

### 18.2 Label style varies by state (Figma inconsistency)

At size 24, Default (Phase 4) and Hover/Pressed bind Body XS-Semibold 12/18; **Focus binds Label XSmall Semibold 12/17**. State-specific text styles at sizes 26–52 (except 40, §5, and 56 Hover/Focus/Disabled) are **not inspected**. → **GB-3**: per-state typography is unresolved for 32 gradient variants (sizes 26, 28, 32, 36, 42, 46, 48, 52 × Hover/Focus/Pressed/Disabled).

## 19. Alignment = Bottom [META]

| Variant | Node | Control y | Root h |
|---|---|---|---|
| Checkbox Checked · Medium · Left · Bottom | `1504:53711` | 17 (= 41 − 24) | 41 |
| Radio Selected · Medium · Left · Bottom | `1504:52694` | 17 (= 41 − 24) | 41 |
| Toggle On · Medium · Left · Bottom | `1504:55687` | 21 (= 41 − 20) | 41 |

→ Alignment=Bottom = root `align-items: flex-end` (control bottom-aligned with the content). ✅ Resolved.

## 20. Gap status after R3-0b

| Gap | Status |
|---|---|
| Gradient sizes 26/28/36/42/46/52 (Default) | ✅ §17 |
| Gradient angle per size and state | ✅ rule §18.1 (Default/Pressed/Disabled verified at all or sampled sizes; Hover/Focus at 3 sizes) |
| Gradient per-state typography at sizes other than 24/40/56 | ❌ **GB-3**: 32 variants uninspected |
| Alignment=Bottom | ✅ §19 |
| D-27 image-only values | ❌ unchanged; export not approved |

## 21. R3-1 preparation: All Buttons borders and Loading (2026-11-19)

Read-only: saved metadata `raw/metadata/375-10891.xml` (0 calls), `get_design_context` ×2 (`887:2132`, `887:1024`), `get_metadata` ×1 (`887:2132`). **Running total: 98 read-only calls.**

### 21.1 Border widths from variant widths [DERIVED from META]

All 432 variant frames have height = Size. At every size, the widths follow one pattern, where Primary Default width = `W`:

| Type | Default | Hover | Focus | Pressed | Disabled | Loading |
|---|---|---|---|---|---|---|
| Primary, Tertiary, Tertiary Grey, Link | W | W | W + 4 | W | W | L |
| Secondary, Secondary Grey | W + 2 | W + 2 | W + 4 | W + 2 | W + 2 | L + 2 |

The stroke is included in auto-layout, so the border widths are: **Primary / Tertiary / Tertiary Grey / Link: none, except Focus 2px**; **Secondary / Secondary Grey: 1px in every state, including Hover, Pressed, Disabled and Loading; 2px at Focus**.

### 21.2 Secondary Grey Hover border [APPLIED]

`887:1024`: `border: 1px solid #dcdfe5` is a **raw colour, not a variable**. Its value equals `Blue-Grey/200` and `Secondary-Grey/Border/Disabled`. Fill `Secondary-Grey/Background/Hover`, label `Secondary-Grey/Content/Default`. Flag **BTN-2** (raw value).

### 21.3 Loading geometry

| Sizes | Loading width L | Dots frame | Dots | Evidence |
|---|---|---|---|---|
| 24 | 38 | 18 × 4 at (10, 10) | 3 × **4 × 4** at x 0 / 7 / 14 | `887:2132` [META + APPLIED] |
| 26, 28 | 38 | 18 wide (= 38 − 2 × 10) | as 24 | [DERIVED from META widths; dot geometry assumed equal to the inspected 18-wide frame] |
| 32 – 56 | 2 × padding-x + 28 | 28 wide | 3 × **6 × 6** at x 0 / 11 / 22 | `887:2163` (size 40) [APPLIED]; others [DERIVED from META widths] |

Loading uses the same padding as Default.

**Binding discrepancy (BTN-1):** Primary Loading 24 binds fill **`Brand/Button/Primary/Background/Loading`**, fallback `#004feb`. Primary Loading 40 binds `Primary/Background/Default` `#004feb`. The values are identical. `Primary/Background/Loading` is not an R1 token and was not part of the approved R3-0a addendum, so the implementation uses `--annachy-color-button-primary-background-default`, which renders an identical colour, and flags the discrepancy for a possible future token addendum.

---

# R3-0c — Gradient button: complete state × size inspection (2026-11-19, owner-approved)

Read-only `get_design_context` ×34, all with the screenshot excluded. 32 variants were planned. Two more were inspected because no earlier step had covered them: **24 Disabled** `1153:3411` and **56 Pressed** `1153:3901`. No writes, exports, downloads, screenshots or `create_session`. **Running total: 132 read-only calls.**

## 22. Gradient button: all 55 variants [APPLIED]

Common to all variants: font family `Font Family/Sans Serif` (Proxima Nova), weight `Weight/Semibold` 600, letter-spacing 0, `white-space: nowrap`, icons 20 × 20 (Home/Home 54), `Height/N`.

| Size | Frame W [META] | Padding-x | Gap | Radius (raw) |
|---|---|---|---|---|
| 24 | 100 | 8 | 4 | 4 |
| 26, 28 | 106 | 8 | 4 | 4 |
| 32, 36, 40 | 128 | 12 | 8 | 8 |
| 42 | 144 | 16 | 12 | 12 |
| 46, 48 | 150 | 16 | 12 | 12 |
| 52, 56 | 156 | 16 | 12 | 12 |

Padding, gap and radius are **identical across all five states** at each size (34 / 34 checked).

| State | Border | Fill | Shadow (Figma radius; emitted as `drop-shadow` = radius ÷ 2) | Label colour |
|---|---|---|---|---|
| Default | 1.5px `Blue/300` | `Gradient/Color 1` 13.397% → `Gradient/Color 2` 86.603% | `-2 4 2 rgba(23,25,28,0)`, `-1 3 1 .02`, `-1 2 1 .08`, `0 1 1 .13` | `Base/White` |
| Hover | 1.5px `Blue/300` | raw `rgba(23,70,162,.85)` 9.5862% → `rgba(58,111,247,.92)` 76.342% | `0 0 3 rgba(50,92,179,.01)`, `0 0 3 .05`, `0 0 3 .16`, `0 0 2 .27`, `0 0 1 .31` | `Text/White` |
| Focus | **2px `Blue/500`** | `Blue/600` 43.833% → `Blue/400` 94.947% | none | `Text/White` |
| Pressed | 1.5px `Blue/300` | `Blue/500` 13.397% → `Gradient/Color 2` 86.603% | `1 2 6 rgba(0,79,235,.12)`, `0 4 12 rgba(0,79,235,.4)` | `Base/White` |
| Disabled | 1.5px `Blue/300` | `Blue/500` @19% → `Gradient/Color 2` @19% (same stops as Pressed) | none | `Button/Primary/Content/Disabled` |

All label colours resolve to `#fafcff`. Stroke alignment: frame widths are identical across states despite 1.5px vs 2px strokes, and the frame width excludes the stroke (24: 100 = 2 × 8 + 2 × 20 + 2 × 4 + 36). The stroke is therefore **inside and not part of the layout** [DERIVED from META].

### 22.1 Per-variant label typography and gradient angle

| Size | State | Node | Text style | Font / LH | CSS angle | Source |
|---|---|---|---|---|---|---|
| 24 | Default | `1153:3371` | Body XS — Semibold | 12 / 18 | 22.572274294652743° | APPLIED |
| 24 | Hover | `1153:3381` | Body XS — Semibold | 12 / 18 | -16.114435203849098° | APPLIED |
| 24 | Focus | `1153:3391` | Label XSmall Semibold | 12 / 17 | -3.5552594168066634° | APPLIED |
| 24 | Pressed | `1153:3401` | Body XS — Semibold | 12 / 18 | 22.572274294652743° | APPLIED |
| 24 | Disabled | `1153:3411` | Body XS — Semibold | 12 / 18 | 22.572274294652743° | APPLIED (R3-0c) |
| 26 | Default | `1153:3421` | Body S - Semi | 14 / 18 | 23.01785504830842° | APPLIED |
| 26 | Hover | `1153:3431` | Body S - Semi | 14 / 18 | -16.45017005645677° | APPLIED (R3-0c) |
| 26 | Focus | `1153:3441` | Body S - Semi | 14 / 18 | -3.6333124582692164° | APPLIED (R3-0c) |
| 26 | Pressed | `1153:3451` | Body S - Semi | 14 / 18 | 23.01785504830842° | APPLIED (R3-0c) |
| 26 | Disabled | `1153:3461` | Body S - Semi | 14 / 18 | 23.01785504830842° | APPLIED (R3-0c) |
| 28 | Default | `1153:3471` | Body S - Semi | 14 / 18 | 24.585177137095087° | APPLIED |
| 28 | Hover | `1153:3481` | Body S - Semi | 14 / 18 | -17.639656364416° | APPLIED (R3-0c) |
| 28 | Focus | `1153:3491` | Body S - Semi | 14 / 18 | -3.911961106090729° | APPLIED (R3-0c) |
| 28 | Pressed | `1153:3501` | Body S - Semi | 14 / 18 | 24.585177137095087° | APPLIED (R3-0c) |
| 28 | Disabled | `1153:3511` | Body S - Semi | 14 / 18 | 24.585177137095087° | APPLIED (R3-0c) |
| 32 | Default | `1153:3521` | H7 — Semibold | 16 / 18 | 23.413224071387774° | APPLIED |
| 32 | Hover | `1153:3531` | H7 — Semibold | 16 / 18 | -16.74895550608987° | APPLIED (R3-0c) |
| 32 | Focus | `1153:3541` | H7 — Semibold | 16 / 18 | -3.7029912735815316° | APPLIED (R3-0c) |
| 32 | Pressed | `1153:3551` | H7 — Semibold | 16 / 18 | 23.413224071387774° | APPLIED (R3-0c) |
| 32 | Disabled | `1153:3561` | H7 — Semibold | 16 / 18 | 23.413224071387774° | APPLIED (R3-0c) |
| 36 | Default | `1153:3571` | H7 — Semibold | 16 / 18 | 25.97253216191386° | APPLIED |
| 36 | Hover | `1153:3581` | H7 — Semibold | 16 / 18 | -18.704260289891423° | APPLIED (R3-0c) |
| 36 | Focus | `1153:3591` | H7 — Semibold | 16 / 18 | -4.164326810102466° | APPLIED (R3-0c) |
| 36 | Pressed | `1153:3601` | H7 — Semibold | 16 / 18 | 25.97253216191386° | APPLIED (R3-0c) |
| 36 | Disabled | `1153:3611` | H7 — Semibold | 16 / 18 | 25.97253216191386° | APPLIED (R3-0c) |
| 40 | Default | `1153:3621` | H7 — Semibold | 16 / 18 | 28.425170856311397° | APPLIED |
| 40 | Hover | `1153:3631` | H7 — Semibold | 16 / 18 | -20.615418727966116° | APPLIED |
| 40 | Focus | `1153:3641` | H7 — Semibold | 16 / 18 | -4.625122076747715° | APPLIED |
| 40 | Pressed | `1153:3651` | H7 — Semibold | 16 / 18 | 28.425170856311397° | APPLIED |
| 40 | Disabled | `1153:3661` | H7 — Semibold | 16 / 18 | 28.425170856311397° | APPLIED |
| 42 | Default | `1153:3671` | H7 — Semibold | 16 / 18 | 26.80205998706895° | APPLIED |
| 42 | Hover | `1153:3681` | H7 — Semibold | 16 / 18 | -19.346358798444285° | APPLIED (R3-0c) |
| 42 | Focus | `1153:3691` | H7 — Semibold | 16 / 18 | -4.317988162566095° | APPLIED (R3-0c) |
| 42 | Pressed | `1153:3701` | H7 — Semibold | 16 / 18 | 26.80205998706895° | APPLIED (R3-0c) |
| 42 | Disabled | `1153:3711` | H7 — Semibold | 16 / 18 | 26.80205998706895° | APPLIED (R3-0c) |
| 46 | Default | `1153:3721` | Subheading L — Semibold | 18 / 25 | 27.975552641534833° | APPLIED |
| 46 | Hover | `1153:3731` | Subheading L — Semibold | 18 / 25 | -20.26214800625104° | APPLIED (R3-0c) |
| 46 | Focus | `1153:3741` | Subheading L — Semibold | 18 / 25 | -4.539150665223573° | APPLIED (R3-0c) |
| 46 | Pressed | `1153:3751` | Subheading L — Semibold | 18 / 25 | 27.975552641534833° | APPLIED (R3-0c) |
| 46 | Disabled | `1153:3761` | Subheading L — Semibold | 18 / 25 | 27.975552641534833° | APPLIED (R3-0c) |
| 48 | Default | `1153:3771` | Subheading L — Semibold | 18 / 25 | 28.99768564862803° | APPLIED |
| 48 | Hover | `1153:3781` | Subheading L — Semibold | 18 / 25 | -21.0672249647522° | APPLIED (R3-0c) |
| 48 | Focus | `1153:3791` | Subheading L — Semibold | 18 / 25 | -4.735626034276493° | APPLIED (R3-0c) |
| 48 | Pressed | `1153:3801` | Subheading L — Semibold | 18 / 25 | 28.99768564862803° | APPLIED (R3-0c) |
| 48 | Disabled | `1153:3811` | Subheading L — Semibold | 18 / 25 | 28.99768564862803° | APPLIED (R3-0c) |
| 52 | Default | `1153:3821` | H5 — Semibold | 20 / 24 | 29.999999554707948° | APPLIED |
| 52 | Hover | `1153:3831` | H5 — Semibold | 20 / 24 | -21.863680548366005° | APPLIED (R3-0c) |
| 52 | Focus | `1153:3841` | H5 — Semibold | 20 / 24 | -4.931989840246004° | APPLIED (R3-0c) |
| 52 | Pressed | `1153:3851` | H5 — Semibold | 20 / 24 | 29.999999554707948° | APPLIED (R3-0c) |
| 52 | Disabled | `1153:3861` | H5 — Semibold | 20 / 24 | 29.999999554707948° | APPLIED (R3-0c) |
| 56 | Default | `1153:3871` | H5 — Semibold | 20 / 24 | 31.87177113855379° | APPLIED |
| 56 | Hover | `1153:3881` | H5 — Semibold | 20 / 24 | -23.370501918258° | APPLIED |
| 56 | Focus | `1153:3891` | H5 — Semibold | 20 / 24 | -5.309282402526279° | APPLIED |
| 56 | Pressed | `1153:3901` | H5 — Semibold | 20 / 24 | 31.87177113855379° | APPLIED (R3-0c) |
| 56 | Disabled | `1153:3911` | H5 — Semibold | 20 / 24 | 31.87177113855379° | APPLIED |

**Typography finding (GB-3 resolved):** each size's label text style is the same in all five states, **except size 24 Focus**. That variant binds **Label XSmall Semibold 12/17** (`1153:3391`); the other size-24 states use Body XS — Semibold 12/18. This is reproduced, not normalised. Gradient 26 uses 14/18 where All Buttons 26 uses 12/18 (GB-1, reproduced).

**Angle finding:** all 55 emitted angles match tan θ = k · H / W (§18.1) to within 5 × 10⁻⁷°. The implementation uses the **emitted** angle of each variant, not the formula.

---

# R3-0d — Input: radius, size and cross-variant verification (2026-11-19)

Read-only: `get_design_context` ×10 (screenshot excluded; 2 returned an HTTP 500 server error and were retried once — no data), `get_variable_defs` ×7, `get_metadata` ×1. No writes, exports or downloads. **Running total: 150 read-only calls.** The element mappings for all 13 states at Size 48 / Radius 8 come from Phase 4 and R3-0 outputs; they were re-read from the session transcript (0 calls).

## 23. Input: full specification

### 23.1 Variant model [META]

The set listings (`1066:37962` via `get_design_context` sparse output) give the variant order: State › Size › Radius.
- Outline IDs step by 18 per variant.
- Filled IDs step by 17 per variant, in the state order Default, Focused, Filled, Disabled, Error, Success, Hover. This was verified: 7 sampled Filled IDs returned the expected State/Size/Radius.
- Root height = field height + 64 for all 150 Outline variants, in every state and radius [META].

### 23.2 Radius [APPLIED / BOUND]

| Radius | Outline node | Filled node | Binding |
|---|---|---|---|
| 4 | `1066:38053` | `1066:40749` | `Radius/4` |
| 6 | `1066:38071` | `1066:40766` | **`Radius/6` = 6**: a Figma variable with **no R1 token** (D-09) |
| 8 | `1066:38089` | `1066:40783` | `Radius/8` |
| 10 | `1066:38107` | `1066:40800` | **`Radius/10` = 10**: a Figma variable with **no R1 token** (D-09) |
| 12 | `1066:38125` | `1066:40817` | `Radius/12` |

Radius affects only the field corner radius; all other properties are identical.

### 23.3 Cross-variant verification [APPLIED / BOUND / META]

| Node | Variant | Result |
|---|---|---|
| `1066:40195` | Outline Error 56 R12 | `Blue-Black/500`, `Base/Grey`, `error`, `Radius/12`: matches the Error model |
| `1066:40447` | Outline Success 50 R10 | Top Section 92 = 50 + 42; px 14, gap 6; `success` border and sub-text: matches |
| `1066:40698` | Filled Default 46 R8 | Top Section 88; px 14, gap 6; icons at 30% opacity; sub-text gap 2: matches |
| `1066:41038` | Filled Default 56 R8 | Icon x 15 (= 14 + 1px stroke); right icons end at 321 (= 336 − 15): matches |
| `1066:43486` | Filled Hover 54 R6 | Border `Blue/500`, placeholder `Blue-Grey/400`, icons at 30%, `Radius/6`: matches |
| `1066:41939` | Filled Disabled 46 R4 | `Blue-Grey/200` / `100`, no `Background/Secondary`, `Radius/4`: matches |
| `1066:41497` | Filled Focused 56 R12 | `Blue-Black/500`, `Blue-Grey/50`, `Blue/600`, `Blue-Grey/900`, `Radius/12`: matches |

**Model (verified):** State determines colours and icon opacity; Size determines only the field height (Top Section = Size + 42, root = Size + 64); Radius determines only the corner radius. Coverage: 13 / 13 state mappings inspected at 48/R8; every radius inspected in both sets; sizes 46/48/50/54/56 inspected (Outline: R3-0 §7; Filled: 46, 48, 54, 56); 7 cross-combinations confirm. **Not individually inspected:** the remaining variants (≈ 290 of 325). They are implemented from the verified model, and the fixture checks each of them against it.

### 23.4 Element mapping (all states)

| Set · State | Label / Description | Field fill | Field border (1px) | Value & placeholder | Sub-text | Icons |
|---|---|---|---|---|---|---|
| Outline · Default | `Blue-Grey/800` / `Blue-Grey/700` | none | `Blue-Grey/300` | `Blue-Grey/200` | `Blue-Grey/500` | fixed images (User, Chevron ×2, Error circle 16) |
| Outline · Focused | `Blue-Black/500` (both) | none | **raw `#3a6ff7`** (IN2) | `Base/Grey` | `Blue-Grey/900` | same |
| Outline · Filled | `Blue-Black/500` | none | `Base/Black` | `Base/Grey` | `Blue-Grey/900` | same |
| Outline · Error | `Blue-Black/500` | none | `error` | `Base/Grey` | `error` | same |
| Outline · Disabled | `Blue-Grey/200` / `Blue-Grey/100` | none | `Blue-Grey/200` | `Blue-Grey/200` | `Blue-Grey/100` | same |
| Outline · Success | `Blue-Black/500` | none | `success` | `Base/Grey` | `success` | same |
| Filled · Default | `Blue-Grey/800` / `700` | `Background/Secondary` | `Blue-Grey/100` | `Blue-Grey/200` | `Blue-Grey/500` | `brand` Cloud, 30% |
| Filled · Hover | `Blue-Grey/800` / `700` | `Background/Secondary` | `Blue/500` | `Blue-Grey/400` | `Blue-Grey/500` | 30% |
| Filled · Focused | `Blue-Black/500` | `Blue-Grey/50` | `Blue/600` | `Base/Grey` | `Blue-Grey/900` | 100% |
| Filled · Filled | `Blue-Black/500` | `Background/Secondary` | `Blue-Grey/300` | `Blue-Black/50` | `Blue-Grey/900` | 100% |
| Filled · Error | `Blue-Black/500` | `Background/Secondary` | `error` | `Base/Grey` | `error` | 100% |
| Filled · Disabled | `Blue-Grey/200` / `100` | **none** | `Blue-Grey/200` | `Blue-Grey/200` | `Blue-Grey/100` | 30% |
| Filled · Success | `Blue-Black/500` | `Background/Secondary` | `success` | `Base/Grey` | `success` | 100% |

Layout (both sets):
- Root: column, gap 2, clip.
- Top Section: column, gap 4, **fixed height Size + 42**, clip.
- Label Container: column, nowrap. Label H7 Semibold 16/18; description Body S 14/20.
- Field: row, gap 6, padding-x 14, height Size, 1px border, clip, items centred. Value Body M-Medium 16/24, flex 1.
- Right Icons: gap 8.
- Sub-text Group: Outline gap 4, full width; Filled gap 2, hug. Sub-text Body S 14/20, nowrap.
- Icons: 24; Outline sub-text icon 16; Filled sub-text icon 14 (wrapper radius 7); Filled icon wrappers radius 4, clip.

---

# R3-0e — Checkbox: element mapping completion (2026-11-19)

Read-only: `get_design_context` ×3 (screenshot excluded), `get_metadata` ×2. Earlier outputs for `1504:53701`, `53976`, `53761`, `53819`, `53867`, `53311`, `54091`, `53917` (VD) and `54031` (VD) were re-read from the session transcript (0 calls). **Running total: 155 read-only calls.**

## 24. Checkbox: all states [APPLIED unless noted]

| State (Medium) | Node | Box fill | Box border | Box shadow | Glyph | Label / Subtext |
|---|---|---|---|---|---|---|
| Checked | `1504:53701` | `Button/Primary/Background/Default` | 1px `Blue/300` | `Button/Default` | `functional/check` 20 | `Text/Primary` / `Text/Tertiary` |
| Multi-select | `1504:53761` | same | 1px `Blue/300` | `Button/Default` | `functional/remove` 20 | same |
| Unchecked | `1504:53819` | `surface-bg` (compat) | **2px** `border-default` (compat) | none | — | same |
| Focus | `1504:53976` | `Blue-White/300` | **2px** `Button/Primary/Background/Focus` | `shadow/sm` (compat) on the box + `Button/Focus` on the container | — (unchecked look) | same |
| Pressed | `1504:54031` | `Button/Primary/Background/Pressed-Active` | 1px `Blue/300` | **`Button/Hover`** | `functional/check` 20 | same |
| Disabled | `1504:53867` | `Blue-Grey/100` | 2px `Blue-Grey/200` | none | — | `Blue-Grey/200` / `Blue-Grey/200` |
| Disabled On | `1504:53917` | `Button/Primary/Background/Disabled` | **none** | none | `functional/check` 20 | `Blue-Grey/200` / `Blue-Grey/200` |

Glyph colour [BOUND; element DERIVED]: the only binding not assigned to another element is `Brand/Background/Primary` `#fafcff` (Checked, Multi-select, Pressed) and `Button/Primary/Content/Disabled` `#fafcff` (Disabled On). **The glyph geometry is not readable** (image only; `1504:53703` has no children), so it stays unresolved (D-27).

Sizes [META]:
- Small: box 20, glyph 16 at inset 2 (`1504:53311`; Multi-select `1504:53371`).
- Medium: box 24, glyph 20 at inset 2.
- Large: box 28, glyph 20 at inset 4 (`1504:54091`; Multi-select `1504:54151`).
- Large Focus `1504:54366`: identical treatment at 28.
- Root heights are 41. Content is 196 wide: 12px padding + 184px subtext. Label is Label Medium 16/21 at every size.

Layouts (§11, §19): Position=Right reverses the order and moves the 12px padding to the right. Alignment Top / Center / Bottom = flex-start / center / flex-end.

## 25. Radio: all states (R3-0f, 2026-11-19) [APPLIED / BOUND / META]

Read-only: `get_design_context` ×6 (screenshot excluded), `get_metadata` ×2, `get_variable_defs` ×2. **Running total: 165 read-only calls** (including the 5 Checkbox calls in §24).

| State (Medium) | Node | Circle fill | Circle border | Shadow | Dot (10 @ inset 7) | Label / Subtext |
|---|---|---|---|---|---|---|
| Selected | `1504:52686` (image) | `Button/Primary/Background/Default` | `Blue/300`: **width unresolved (D-27)** | `Button/Default` | `Background/Primary` | `Text/Primary` / `Text/Tertiary` |
| Unselected | `1504:52738` | `surface-bg` (compat) | 2px `border-default` (compat) | none | none | same |
| Disabled Unselected | `1504:52786` | `Blue-Grey/100` | 2px `Blue-Grey/200` | none | none | `Blue-Grey/200` (both) |
| Disabled Selected | `1504:52835` (image) | `Button/Primary/Background/Disabled` [BOUND] | **no stroke bound** | none | `Button/Primary/Content/Disabled` (`1504:52837`) | `Blue-Grey/200` (both) |
| Focus | `1504:52889` | `Blue-White/300` | 2px `Button/Primary/Background/Focus` | `shadow/sm` + `Button/Focus` (container) | none | `Text/Primary` / `Text/Tertiary` |
| Pressed | `1504:52943` (image) | `Pressed-Active` [BOUND] | `Blue/300`: **width unresolved (D-27)** | `Button/Hover` | `Background/Primary` (`1504:52945`) | same |

Radius: raw **10 / 12 / 14**, half the size, so a full circle (`1504:52426` Small, `52738` Medium, `53050` Large). Sizes 20 / 24 / 28; dot 8 / 10 / 12 at inset 6 / 7 / 8 (§12). Layout and typography are identical to Checkbox (§24).

**Not implemented (D-27):** the Selected and Pressed ring is bound to `Blue/300`, but its stroke width is not readable (the container renders as an image). No ring is drawn; fill, dot and shadow are drawn.

## 26. Toggle: element-level states (R3-0g, 2026-11-19) [BOUND / META]

Read-only: `get_variable_defs` ×17 on individual Track / Thumb nodes, `get_metadata` ×11. No writes, exports or downloads. **Running total: 193 read-only calls.**

`get_variable_defs` on a node returns its own bindings plus those of its descendants. The Thumb is the Track's only visible child, so **Track-own = Track − Thumb**.

| State (Medium) | Track / Thumb nodes | Thumb bindings | Track-own bindings | Thumb x | Track fill (implemented) |
|---|---|---|---|---|---|
| On | `54624` / `54625` | `Content/Loading`, `Blue-Grey/100`, `Toggle/On` | `Button/Primary/Background/Default` | 20 | `#004feb` |
| Off | `54639` / `54640` | `Content/Loading`, **`Blue-Grey/50`**, `Toggle/Off` | **none** | 2 | `Blue-Grey/50` **[DERIVED, TG-1]** |
| Hover On | `54654` / `54655` | `Content/Loading`, `Blue-Grey/200`, `Toggle/On` | `Background/Hover` | 20 | `#003fbc` |
| Hover Off | `54669` / `54670` | `Content/Loading`, `Blue-Grey/50`, `Toggle/Off` | `Blue-Grey/200` | 2 | `#dcdfe5` |
| Focus On | `54684` / `54685` | `Content/Loading`, `Blue-Grey/200`, `Toggle/On` | `Background/Focus` + `Border/Focus` | **18.5** | `#004feb` (border width D-27, not drawn) |
| Focus Off | `54699` / `54700` | `Content/Loading`, `Blue-Grey/50`, `Toggle/Off` | `Blue-Grey/200` + `Border/Focus` | **3** | `#dcdfe5` (border width D-27, not drawn) |
| Pressed On | `54714` / `54715` | `Content/Loading`, `Blue-Grey/100`, `Toggle/On` | `Pressed-Active` + **`Toggle/Press`** | 20 | `#3372ef`, track shadow `Toggle/Press` |
| Pressed Off | `54729` / `54730` | `Content/Loading`, `Blue-Grey/50`, `Toggle/Off` | `Blue-Grey/300` | 2 | `#bfc4cf` |
| Disabled On | `54744` / `54745` | `Content/Loading`, `Blue-Grey/100`, `Toggle/On` | **none** | 20 | `Blue-Grey/100` **[DERIVED, TG-1]** |
| Disabled Off | `54759` / `54760` | `Content/Loading`, `Blue-Grey/50`, `Toggle/Off` | **none** | 2 | `Blue-Grey/50` **[DERIVED, TG-1]** |

- **Thumb:** fill `Button/Primary/Content/Loading` `#fafcff` (T2) and effect `Toggle/On` or `Toggle/Off`. Its secondary colour (`Blue-Grey/50`, `100` or `200`, depending on state) is presumably a stroke whose **width is not readable** (D-27). It is not drawn.
- **TG-1:** in Off, Disabled On and Disabled Off the track has no binding of its own. Its only bound candidate is the colour it shares with the thumb (`Blue-Grey/50`, `/100`, `/50`), and that matches the original audit reading (`toggle.md` §3). It is implemented as such and flagged as derived.
- **Thumb position [META]:**
  - Off states: x = 2, except **Focus Off: x = 3** at Small, Medium and Large (`54547`, `54697`, `54847`).
  - On states: x = track − thumb − 2, except **Focus On: track − thumb − 3.5** at Small, Medium and Large (`54532` 16.5, `54682` 18.5, `54832` 20.5).
  - The thumb y is 2 everywhere.
  - Hover, Pressed and Disabled were inspected at Medium (`54652`, `54667`, `54712`, `54727`, `54742`, `54757`).
- **Root:** width = track + 196; height = label line height + 20 (40 / 41 / 42); the track is vertically centred in Center alignment.
  - Label: Label Small 14/20, Label Medium 16/21 or Label Large 18/22. **max-width 240 is inspected at Medium only** (`1504:54630`).
  - Subtext: Body S 14/20, 184 wide.
  - Disabled label and subtext: `Blue-Grey/200`.
- **Not readable (D-27), not drawn:**
  - track corner radius;
  - thumb stroke width;
  - track Focus border width.

  The hidden "Focus Ring" layer (−4 inset) is hidden in every inspected variant, so it is not rendered.

### 23.5 Element node index (cited in `input.css`) [APPLIED, re-read from Phase 4 / R3-0 outputs]

| Node | Element | Source variant |
|---|---|---|
| `1066:38544` | Input Field, Outline Focused: raw `#3a6ff7` border | `1066:38539` |
| `1066:39889` | Outline Error variant (Phase 4 `get_design_context`) | — |
| `1066:40789` | Filled Default Left Icon wrapper: 24, radius 4, opacity 30% | `1066:40783` |
| `1066:40798` | Filled Default Sub-text Icon wrapper: 14, radius 7 | `1066:40783` |
| `1066:41213` | Input Field, Filled Focused: `Blue/600` border, `Blue-Grey/50` fill | `1066:41208` |
| `1780:40128` | Alerts/Error circle instance (XS 16) in every Outline variant | `1066:38053` and all inspected Outline variants |
