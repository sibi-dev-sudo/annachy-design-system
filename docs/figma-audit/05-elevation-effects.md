# 05 — Elevation & Effects (Shadow, Blur, Glass, Border, Opacity)

| Item | Value |
|---|---|
| Source pages | › ⑥ Shadow ✓ `1351:18308` · › ⑦ Blur ✓ `1351:18312` · Brand Colours swatches `1557:23523` |
| Method | `get_variable_defs` on `1561:57814` (Shadow Scale), `1561:58161` (Shadow Effects), `1563:58676` (Blur & Glass). Read-only. |
| Raw evidence | `raw/effects.json` — every effect string copied verbatim from Figma |
| Status | 32 shadow styles + 5 blur + 3 glass extracted. |

Figma `radius` on shadows = CSS blur radius; Figma colours are `#RRGGBBAA`. CSS columns are a mechanical conversion **[DERIVED]**; layer values themselves are **[EXTRACTED]**. Inner shadows map to `inset`.

---

## 1. Shadows

Two separate shadow families exist: **Shadow Scale** (size-graded, 17 styles) and **Shadow Effects** (named, 15 styles).

### Shadow Scale

| Style | Layers | CSS `box-shadow` equivalent [DERIVED] |
|---|---:|---|
| `Shadow Scale/SM/01` | 1 | `1.95px 1.95px 2.6px 0px rgb(0 0 0 / 14.9%)` |
| `Shadow Scale/SM/02` | 1 | `0px 1px 4px 0px rgb(0 0 0 / 16.1%)` |
| `Shadow Scale/SM/03` | 2 | `0px 1px 4px 0px rgb(0 0 0 / 16.1%), 0px 0px 0px 3px #333333` |
| `Shadow Scale/SM/04` | 2 | `0px 1px 3px 0px rgb(0 0 0 / 2%), 0px 0px 0px 1px rgb(27 31 35 / 14.9%)` |
| `Shadow Scale/SM/05` | 2 | `0px 2px 5px -1px rgb(50 50 93 / 25.1%), 0px 1px 3px -1px rgb(0 0 0 / 30.2%)` |
| `Shadow Scale/MD/01` | 1 | `0px 3px 8px 0px rgb(0 0 0 / 25.1%)` |
| `Shadow Scale/MD/02` | 1 | `0px 2px 8px 0px rgb(99 99 99 / 20%)` |
| `Shadow Scale/MD/03` | 1 | `0px 4px 12px 0px rgb(0 0 0 / 10.2%)` |
| `Shadow Scale/LG/01` | 1 | `0px 8px 24px 0px rgb(149 157 165 / 20%)` |
| `Shadow Scale/LG/02` | 1 | `0px 5px 15px 0px rgb(0 0 0 / 34.9%)` |
| `Shadow Scale/LG/03` | 2 | `0px 6px 24px 0px rgb(0 0 0 / 5.1%), 0px 0px 0px 1px rgb(0 0 0 / 7.8%)` |
| `Shadow Scale/XL/01` | 1 | `0px 7px 29px 0px rgb(100 100 111 / 20%)` |
| `Shadow Scale/XL/02` | 2 | `0px 0px 0px 1px rgb(0 0 0 / 5.9%), 0px 10px 36px 0px rgb(0 0 0 / 16.1%)` |
| `Shadow Scale/XL/03` | 2 | `0px 13px 27px -5px rgb(50 50 93 / 25.1%), 0px 8px 16px -8px rgb(0 0 0 / 30.2%)` |
| `Shadow Scale/XXL/01` | 1 | `0px 48px 100px 0px rgb(17 12 46 / 14.9%)` |
| `Shadow Scale/XXL/02` | 3 | `0px 50px 100px -20px rgb(50 50 93 / 25.1%), 0px 30px 60px -30px rgb(0 0 0 / 30.2%), inset 0px -2px 6px 0px rgb(10 37 64 / 34.9%)` |
| `Shadow Scale/XXL/03` | 3 | `inset 0px 1px 1px 0px rgb(255 255 255 / 10.2%), 0px 50px 100px -20px rgb(50 50 93 / 25.1%), 0px 30px 60px -30px rgb(0 0 0 / 30.2%)` |

### Shadow Effects

| Style | Layers | CSS `box-shadow` equivalent [DERIVED] |
|---|---:|---|
| `Shadow Effects/SM/Peck` | 3 | `0px 1px 1px 0px rgb(0 0 0 / 5.1%), 0px 2px 1px 0px rgb(0 0 0 / 1.2%), 0px 3px 1px 0px rgb(0 0 0 / 2%)` |
| `Shadow Effects/SM/Stub` | 5 | `0px 1px 1px 0px rgb(0 0 0 / 2%), 0px 2px 4px 0px rgb(0 0 0 / 3.9%), 0px 2px 2px 0px rgb(0 0 0 / 1.2%), 0px 2px 2px 0px rgb(0 0 0 / 7.8%), 0px 1px 0px 0px rgb(0 0 0 / 12.2%)` |
| `Shadow Effects/SM/Popup` | 4 | `0px 0px 1px 0px rgb(0 0 0 / 7.8%), 0px 1px 1px 0px rgb(0 0 0 / 7.8%), 0px 3px 2px 0px rgb(0 0 0 / 3.9%), 0px 5px 2px 0px rgb(0 0 0 / 1.2%)` |
| `Shadow Effects/SM/Raised` | 7 | `0px 0px 1px 0px rgb(0 0 0 / 7.8%), 0px -1px 1px 0px rgb(0 0 0 / 7.8%), 0px -2px 1px 0px rgb(0 0 0 / 3.9%), 0px -4px 1px 0px rgb(0 0 0 / 1.2%), 0px 1px 1px 0px rgb(0 0 0 / 7.8%), 0px 2px 2px 0px rgb(0 0 0 / 7.8%), 0px 6px 3px 0px rgb(0 0 0 / 3.9%)` |
| `Shadow Effects/SM/Top Light` | 4 | `0px 1px 2px 0px rgb(0 0 0 / 7.8%), 0px 3px 3px 0px rgb(0 0 0 / 7.8%), 0px 8px 4px 0px rgb(0 0 0 / 3.9%), 0px 13px 5px 0px rgb(0 0 0 / 1.2%)` |
| `Shadow Effects/SM/Bottom Light` | 4 | `0px -1px 2px 0px rgb(0 0 0 / 7.8%), 0px -3px 3px 0px rgb(0 0 0 / 7.8%), 0px -8px 4px 0px rgb(0 0 0 / 3.9%), 0px -13px 5px 0px rgb(0 0 0 / 1.2%)` |
| `Shadow Effects/SM/Left Light` | 5 | `0px 1px 1px 0px rgb(0 0 0 / 7.8%), 1px 2px 2px 0px rgb(0 0 0 / 7.8%), 2px 6px 4px 0px rgb(0 0 0 / 3.9%), 4px 8px 4px 0px rgb(0 0 0 / 1.2%), 8px 12px 4px 0px rgb(0 0 0 / 1.2%)` |
| `Shadow Effects/SM/Right Light` | 5 | `0px 1px 1px 0px rgb(0 0 0 / 7.8%), -1px 2px 2px 0px rgb(0 0 0 / 7.8%), -2px 6px 4px 0px rgb(0 0 0 / 3.9%), -4px 8px 4px 0px rgb(0 0 0 / 1.2%), -8px 12px 4px 0px rgb(0 0 0 / 1.2%)` |
| `Shadow Effects/MD/Lozenge` | 8 | `inset 0px 0px 1px 0px rgb(0 0 0 / 16.1%), inset 0px -1px 1px 0px rgb(0 0 0 / 16.1%), inset 0px -4px 8px 0px rgb(0 0 0 / 7.8%), inset 0px -7px 12px 0px rgb(0 0 0 / 3.9%), inset 0px -16px 8px 0px rgb(0 0 0 / 1.2%), inset 0px -1px 1px 0px rgb(255 255 255 / 30.2%), inset 0.5px 1px 1px 0px rgb(255 255 255 / 30.2%), inset -0.5px 1px 8px 0px rgb(255 255 255 / 20%)` |
| `Shadow Effects/MD/Stub Inset` | 4 | `inset 0px -1px 0px 0px rgb(0 0 0 / 16.1%), inset 0px -1px 1px 0px rgb(0 0 0 / 23.9%), inset 0px -8px 12px 0px rgb(0 0 0 / 3.9%), inset 0px -16px 12px 0px rgb(0 0 0 / 1.2%)` |
| `Shadow Effects/LG/Bubble` | 10 | `0px 1px 2px 0px rgb(0 0 0 / 10.2%), 0px 3px 5px 0px rgb(0 0 0 / 3.9%), 0px 7px 4px 0px rgb(0 0 0 / 2%), 0px 13px 5px 0px rgb(0 0 0 / 2%), 0px 20px 6px 0px rgb(0 0 0 / 1.2%), inset 2px 1px 8px 0px rgb(0 0 0 / 7.8%), inset 2px 3px 6px 0px rgb(0 0 0 / 5.9%), inset 2px 7px 16px 0px rgb(0 0 0 / 3.9%), inset 2px 13px 5px 0px rgb(0 0 0 / 1.2%), inset 2px 20px 16px 0px rgb(0 0 0 / 3.9%)` |
| `Shadow Effects/LG/Hard Inset` | 3 | `inset 0px 1px 4px 0px rgb(0 0 0 / 23.9%), inset 0px 8px 16px 0px rgb(0 0 0 / 12.2%), inset 0px 16px 8px 0px rgb(0 0 0 / 3.9%)` |
| `Shadow Effects/LG/Hard Lift` | 4 | `0px 1px 2px 0px rgb(0 0 0 / 16.1%), 0px 3px 3px 0px rgb(0 0 0 / 16.1%), 0px 8px 16px 0px rgb(0 0 0 / 12.2%), 0px 13px 5px 0px rgb(0 0 0 / 1.2%)` |
| `Shadow Effects/LG/Soft Inset` | 3 | `inset 0px 1px 2px 0px rgb(0 0 0 / 12.2%), inset 0px 8px 16px 0px rgb(0 0 0 / 3.9%), inset 0px 16px 8px 0px rgb(0 0 0 / 1.2%)` |
| `Shadow Effects/XXL/Dialog` | 5 | `0px 4px 12px 0px rgb(0 0 0 / 14.1%), 0px 20px 20px 0px rgb(0 0 0 / 12.2%), 0px 48px 24px 0px rgb(0 0 0 / 3.9%), 0px 80px 24px 0px rgb(0 0 0 / 3.1%), 0px 40px 80px 0px rgb(0 0 0 / 1.2%)` |

### Shadow (Brand Colours swatch style)

| Style | Layers | CSS |
|---|---:|---|
| `Shadow` | 5 | `-1.39px 2.77px 6.93px 0px rgb(0 0 0 / 10.2%), -2.77px 12.47px 13.85px 0px rgb(0 0 0 / 9%), -6.93px 29.09px 18.01px 0px rgb(0 0 0 / 5.1%), -12.47px 52.64px 22.16px 0px rgb(0 0 0 / 1.2%), -18.01px 81.73px 23.55px 0px rgb(0 0 0 / 0%)` |

Specimen carriers (for Phase 5 cross-check): Scale SM `1561:57835/57842/57849/57856/57863`, MD `57945/57952/57959`, LG `57873/57880/57887`, XL `57897/57904/57911`, XXL `57921/57928/57935`; Effects `1561:58182 … 58289`.

---

## 2. Blur & Glass `1563:58296`

| Style | Figma type | Radius | CSS equivalent [DERIVED] | Note |
|---|---|---:|---|---|
| `Blur/XS-01` | FOREGROUND_BLUR (layer blur) | 4 | `filter: blur(4px)` | labelled "XS" under "Large" heading |
| `Blur/SM-01` | FOREGROUND_BLUR | **0** | none | **no effect** |
| `Blur/SM-02` | FOREGROUND_BLUR | **0** | none | **no effect** |
| `Blur/MD-01` | FOREGROUND_BLUR | **0** | none | **no effect** |
| `Blur/MD-02` | FOREGROUND_BLUR | **0** | none | **no effect** |
| `Glass/XS-01` | GLASS | 5 | approx. `backdrop-filter: blur(5px)` + translucent fill | Figma "Glass" also refracts/highlights; CSS can only approximate |
| `Glass/SM-01` | GLASS | 10 | approx. `backdrop-filter: blur(10px)` | |
| `Glass/MD-01` | GLASS | 20 | approx. `backdrop-filter: blur(20px)` | |

Glass companion fills (white gradient stops) on the same page: `Gradient/Full` `#ffffff`, `Gradient/XS` `#ffffffbf` (75%), `Gradient/S` `#ffffff40` (25%), `Gradient/M` `#ffffff00` (0%). `Brand/Blue/Gradient/04`, `/08`, `/09` returned empty values (gradient paints not resolvable by this tool).

Glass parameters other than radius (refraction, depth, light angle, dispersion) are **not returned** by `get_variable_defs` [INACCESSIBLE].

---

## 3. Border widths & opacity

| Variable | Value | Source |
|---|---|---|
| `Border/XS` | 0.5 | `1563:58676` |
| `Border/S` | 1 | `1563:58676` |
| `Border/M` | 1.5 | `1563:58676` |
| `var(--sds-size-stroke-border)` | 1 | Simple Design System (see E7) |

Opacity: no opacity variables exist [MISSING]. Opacity is embedded in shadow/gradient colours only (e.g. 2%, 14.9%, 25%, 75%).

---

## 3.1 Effect styles actually used by components (undocumented on the Shadow page) [added 2026-11-19]

> *[Correction 2026-11-19 — evidence from Phase 4 (`components/*.md`, `07` §3) and Phase 5 (`11` §4.3). The sections above describe documented Shadow/Blur page styles only.]*

**Documented vs used — summary**

| Group | Defined on Shadow/Blur page? | Used by any inspected component? |
|---|---|---|
| `Shadow Scale/*` (17), `Shadow Effects/*` (15) | Yes (`1561:57736`, `1561:57961`) | **No** |
| `Blur/*` (5), `Glass/*` (3) | Yes (`1563:58296`) | **No** |
| `Shadow` (5-layer) | No | Colour swatches only (`1557:23523`) |
| `Button/Default`, `Button/Hover`, `Button/Focus` | **No** | **Yes** — selection controls, Dropdown |
| `Toggle/On`, `Toggle/Off`, `Toggle/Press` | **No** | **Yes** — Toggle |
| `shadow/sm` (foreign) | **No** | **Yes** — Checkbox/Radio Focus |
| Raw (unstyled) shadow | n/a | Button (gradient) only |

**Used styles — values [EXTRACTED via `get_variable_defs` / `get_design_context`] and usage**

| Style | Layers (colour · x,y · blur · spread 0) | Used by (component · state) | Evidence nodes |
|---|---|---|---|
| `Button/Default` | `#17191C21` 0,1 ·1 · `#17191C14` -1,2 ·1 · `#17191C05` -1,3 ·1 · `#17191C00` -2,4 ·2 | Checkbox Checked, Multi-select; Radio Selected | `1504:53701`, `1504:53761`, `1504:52685` |
| `Button/Hover` | `#325CB34F` 0,0 ·1 · `#325CB345` 0,0 ·2 · `#325CB329` 0,0 ·3 · `#325CB30D` 0,0 ·3 · `#325CB303` 0,0 ·3 | Checkbox Pressed; Radio Pressed | `1504:54031`, `1504:52943` |
| `Button/Focus` | `#0141C07D` 0,0 ·2 · `#0141C06E` 0,1 ·3 · `#0141C040` -1,2 ·4 · `#0141C012` -2,3 ·4 · `#0141C003` -3,4 ·5 | Dropdown Item Focus; Checkbox Focus; Radio Focus | `1451:25074`, `1504:53976`, `1504:52889` |
| `Toggle/On` | `#00000017` 0,0 ·1 · `#0000000D` -1,1 ·1 · `#00000003` -2,1 ·1 · `#00000000` -2,2 ·1 | Toggle On, Hover On, Focus On, Pressed On, Disabled On; Selection Controls wrapper (Toggle) | `1504:54622`, `1504:54652`, `1504:54682`, `1504:54712`, `1504:54742`, `1504:57178` |
| `Toggle/Off` | `#3C343417` 0,0 ·1 · `#3C34340D` 1,1 ·1 · `#3C343403` 2,2 ·1 · `#3C343400` 3,2 ·1 | Toggle Off, Hover Off, Disabled Off | `1504:54637`, `1504:54667`, `1504:54757` |
| `Toggle/Press` | `#004FEB4A` 0,0 ·1 · `#004FEB42` 0,1 ·2 · `#004FEB26` -1,2 ·2 · `#004FEB0A` -2,4 ·2 · `#004FEB03` -3,7 ·3 | Toggle Pressed On (with `Toggle/On`) | `1504:54712` |
| `shadow/sm` | `#1A1A1A14` 0,1 · blur `Blur/blur-2` (3) · `Colors/alpha/50` (`#1a1a1a14`) 0,0.5 · blur `Blur/blur-0` (0) | Checkbox Focus; Radio Focus | `1504:53976`, `1504:52889` |
| Raw shadow (no style) | `-2px 4px 2px rgba(23,25,28,0)`, `-1px 3px 1px rgba(23,25,28,.02)`, `-1px 2px 1px rgba(23,25,28,.08)`, `0 1px 1px rgba(23,25,28,.13)` | Button (gradient) Size 24 Default | `1153:3371` |

Observations [DERIVED]:
- The `Button/*` styles are **not used by the Button component** (All Buttons variants have no shadow — `components/button.md` §1.5); they are used by selection controls and Dropdown.
- The gradient Button's raw shadow uses the same base colour (`#17191C` = rgb 23,25,28) as `Button/Default` but different layer opacities; it is not bound to the style.
- No inspected component uses any `Shadow Scale/*`, `Shadow Effects/*`, `Blur/*` or `Glass/*` style.
- Coverage: only variants listed in the component specs were inspected; other variants may use additional styles [UNVERIFIED].

## 4. Focus-ring / elevation styles outside this file

`search_design_system` found published effect styles in a library named **"Design System"** (key `lk-483b…12dd12`), **not linked to this file**: `Shadow/xs`, `sm`, `md`, `lg`, `xl`, `2xl`, `3xl`, `Shadow/xs focused 4px brand-100`, `Shadow/sm focused 4px brand-100`, `Shadow/xs focused 4px error-100`, `Shadow/sm focused 4px neutral-100`, `Shadow/Portfolio mockup/*`. Values not retrieved. Whether this library is Annachy's is **unknown** — must be confirmed before use.

---

## 5. Findings

| # | Finding | Severity | Tag |
|---|---|---|---|
| E1 | **Two parallel shadow systems** (Scale SM–XXL and named Effects) with no documented mapping to components or elevation levels. **Neither is used by any inspected component; components use the undocumented `Button/*`, `Toggle/*` and `shadow/sm` styles instead (§3.1).** *[Extended 2026-11-19 — Phase 4/5 evidence.]* | High | [EXTRACTED] |
| E2 | Shadow Scale header claims 18 variants; 17 styles exist. | Low | [EXTRACTED] |
| E3 | Shadow Scale styles appear sourced from mixed origins (different colour bases: `#32325D`, `#959DA5`, `#64646F`, `#110C2E`, `#1B1F23`, `#636363`, `#0A2540`) — not derived from the Annachy palette. | Medium | [DERIVED] |
| E4 | `Shadow Scale/SM/03` contains an opaque `#333333` 3px spread ring — behaves like a focus outline, not a shadow. | Medium | [EXTRACTED] |
| E5 | `Shadow Scale/SM/01` uses fractional offsets (1.95/2.6); `Shadow` swatch style uses scaled fractional values and a fully transparent 5th layer. | Low | [EXTRACTED] |
| E6 | **4 of 5 blur styles have radius 0** (no visible effect). Header says "2 variants"; 8 specimens; "Large" specimens labelled "XS". | High | [EXTRACTED] |
| E7 | Variables from Figma's community **Simple Design System** kit are present (`--sds-*`, `Text/Neutral/Primary #1d1a22`, `Background/Neutral/Primary #ffffff`, `Background/Neutral/Secondary #f7f6f8`, `Border/Neutral/Inverse/Primary #3a3445`, `--sds-color-border-default-default #d9d9d9`). Copied documentation chrome brings foreign tokens into the file. | Medium | [EXTRACTED] |
| E8 | A third naming style `Brand / Blue-Grey / 600` (spaces around slashes) appears alongside `Brand/Blue-Grey/600`. | Low | [EXTRACTED] |
| E9 | No elevation→component mapping (which shadow does a Tooltip/Dropdown/Dialog use?) — to be derived in Phase 4 from component nodes. *[Updated 2026-11-19 — Phase 4 result: observed usage is recorded in §3.1; Dropdown Menu and Tooltip have **no** shadow; no documented mapping exists in Figma.]* | Medium | [MISSING] |
| E10 | No dedicated focus-ring token in this file; focus styling must be read per component. *[Updated 2026-11-19 — an undocumented effect style `Button/Focus` acts as a focus glow on Dropdown Item, Checkbox and Radio (§3.1); it is not used by Button itself and is not a documented focus token.]* | Medium | [MISSING] |
| E11 | Glass effect cannot be reproduced exactly in CSS; only `backdrop-filter` approximation, with browser-support caveats. | Info | [DERIVED] |

---

## 6. Open questions

1. Which shadow family is canonical for components — Scale, Effects, or the component-used `Button/*` / `Toggle/*` styles (§3.1)? *(option added 2026-11-19)*
2. Are Blur SM/MD (radius 0) placeholders? What are the intended values?
3. Is the published "Design System" library (with focus-ring shadows) Annachy's?
4. Should Simple Design System variables be removed/ignored?
