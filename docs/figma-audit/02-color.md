# 02 — Colour

| Item | Value |
|---|---|
| Source page | › ① Colour ✓ `273:10649` |
| Sections | Brand Colours `1557:23523` · Supporting Colours `1557:25193` · Colour Usage `1557:31595` · COLOUR SYSTEM PROMPT `1557:37808` (documentation text) |
| Method | `get_variable_defs` on each section (read-only) |
| Status | Values extracted. Collection names and modes **not obtainable** with available read-only tools (see §6). |

All hex values below are **[EXTRACTED]** — returned verbatim by `get_variable_defs`. Observations on them are **[DERIVED]**.

---

## 1. Variables bound in "Colour Usage" `1557:31595` (primary set — 130 colour variables: 6 base/gradient + 40 brand-scale + 36 status-scale + 27 semantic + 9 button + 12 supporting)

### 1.1 Base & gradient

| Variable | Value |
|---|---|
| `Brand/Base/Black` | `#0b0c0f` |
| `Brand/Base/Blue` | `#004feb` |
| `Brand/Base/Grey` | `#1f242e` |
| `Brand/Base/White` | `#fafcff` |
| `Brand/Gradient/Color 1` | `#3a79f7` |
| `Brand/Gradient/Color 2` | `#1746a2` |

### 1.2 Tonal scales

| Step | `Brand/Blue` | `Brand/Blue-White` | `Brand/Blue-Black` | `Brand/Blue-Grey` |
|---|---|---|---|---|
| 50 | `#f3f7ff` | `#fafcff` | `#202d47` | `#f6f7f9` |
| 100 | `#e6edfd` | `#f5f9ff` | `#1d2432` | `#edeff2` |
| 200 | `#ccdcfb` | `#f0f5fe` | `#171e2a` | `#dcdfe5` |
| 300 | `#99b9f7` | `#ebf2ff` | `#1f242e` | `#bfc4cf` |
| 400 | `#3372ef` | `#c6d6f6` | `#181b21` | `#98a0ae` |
| 500 | `#004feb` | `#b3c7ef` | `#121417` | `#707a8f` |
| 600 | `#003fbc` | `#a1b9e8` | `#030a14` | `#555d6d` |
| 700 | `#002f8d` | `#88a4dd` | `#00050f` | `#3d4451` |
| 800 | `#00205e` | `#7393d3` | `#060707` | `#272b35` |
| 900 | `#00102f` | `#5b7fc8` | `#000204` | `#15181e` |

| Step | `Brand/Success` | `Brand/Warning` | `Brand/Error` | `Brand/Info` |
|---|---|---|---|---|
| 100 | `#f4fbef` | `#fff8f1` | `#fff7f6` | `#f6faff` |
| 200 | `#d6f3c9` | `#ffddb3` | `#ffe6e2` | `#dbedfd` |
| 300 | `#93e281` | `#ffbd6b` | `#ffc1b6` | `#a6d3f9` |
| 400 | `#5ecb55` | `#f88f33` | `#ff9c8c` | `#71b9f7` |
| 500 | `#14a047` | `#f26e2d` | `#ff614e` | `#186eb5` |
| 600 | `#276732` | `#b9512e` | `#e72b23` | `#165d99` |
| 700 | `#20572c` | `#9d4520` | `#9d4520` | `#154f81` |
| 800 | `#184626` | `#6c2e18` | `#7a2515` | `#124067` |
| 900 | `#11331c` | `#4c2213` | `#521e11` | `#102e48` |

### 1.3 Semantic

| Variable | Value | Matches primitive [DERIVED] |
|---|---|---|
| `Brand/Text/Primary` | `#0b0c0f` | Base/Black |
| `Brand/Text/Secondary` | `#555d6d` | Blue-Grey/600 |
| `Brand/Text/Tertiary` | `#707a8f` | Blue-Grey/500 |
| `Brand/Text/Black` | `#0b0c0f` | Base/Black |
| `Brand/Text/Brand` | `#004feb` | Blue/500 |
| `Brand/Text/Grey` | `#1f242e` | Base/Grey |
| `Brand/Text/White` | `#fafcff` | Base/White |
| `Brand/Background/Primary` | `#fafcff` | Base/White |
| `Brand/Background/Secondary` | `#f6f7f9` | Blue-Grey/50 |
| `Brand/Background/Tertiary` | `#edeff2` | Blue-Grey/100 |
| `Brand/Border/Primary` | `#bfc4cf` | Blue-Grey/300 |
| `Brand/Border/Secondary` | `#dcdfe5` | Blue-Grey/200 |
| `Brand/Icon/Primary` | `#0b0c0f` | Base/Black |
| `Brand/Icon/Secondary` | `#555d6d` | Blue-Grey/600 |
| `Brand/Icon/Tertiary` | `#98a0ae` | Blue-Grey/400 |
| `Brand/Action/Primary` | `#004feb` | Blue/500 |
| `Brand/Action/Hover` | `#003fbc` | Blue/600 |
| `Brand/Action/Active` | `#002f8d` | Blue/700 |
| `Brand/Action/Disabled` | `#bfc4cf` | Blue-Grey/300 |
| `Brand/Feedback/Success` | `#14a047` | Success/500 |
| `Brand/Feedback/Success Light` | `#f4fbef` | Success/100 |
| `Brand/Feedback/Warning` | `#f26e2d` | Warning/500 |
| `Brand/Feedback/Warning Light` | `#fff8f1` | Warning/100 |
| `Brand/Feedback/Error` | `#ff614e` | Error/500 |
| `Brand/Feedback/Error Light` | `#fff7f6` | Error/100 |
| `Brand/Feedback/Info` | `#186eb5` | Info/500 |
| `Brand/Feedback/Info Light` | `#f6faff` | Info/100 |

### 1.4 Component-scoped (Button)

| Variable | Value |
|---|---|
| `Brand/Button/Primary/Background/Default` | `#004feb` |
| `Brand/Button/Primary/Content/Default` | `#fafcff` |
| `Brand/Button/Secondary/Background/Default` | `#fafcff` |
| `Brand/Button/Secondary/Content/Default` | `#004feb` |
| `Brand/Button/Gradient Start` | `#3a79f7` |
| `Brand/Button/Gradient End` | `#1746a2` |
| `Brand/Button/Success` | `#14a047` |
| `Brand/Button/Warning` | `#f26e2d` |
| `Brand/Button/Error` | `#ff614e` |

Only *Default* state values exist as variables for buttons. Hover/Focus/Pressed/Disabled button colours are **not** variables here → to be extracted per variant in Phase 4.

### 1.5 `Supporting/*` (duplicates of Brand values)

| Variable | Value | Same as |
|---|---|---|
| `Supporting/Success/100`, `/500`, `/800` | `#f4fbef`, `#14a047`, `#184626` | Brand/Success/100, 500, 800 |
| `Supporting/Warning/100`, `/500`, `/800` | `#fff8f1`, `#f26e2d`, `#6c2e18` | Brand/Warning/… |
| `Supporting/Error/100`, `/500`, `/800` | `#fff7f6`, `#ff614e`, `#7a2515` | Brand/Error/… |
| `Supporting/Info/100`, `/500`, `/800` | `#f6faff`, `#186eb5`, `#124067` | Brand/Info/… |

---

## 2. Variables bound in "Brand Colours" `1557:23523` (second naming scheme)

| Variable | Value | Conflict with primary set [DERIVED] |
|---|---|---|
| `brand/blue-primary/100` | `#e6edfd` | = `Brand/Blue/100` (different name) |
| `brand/blue-grey/300` | `#1f242e` | **≠ `Brand/Blue-Grey/300` (`#bfc4cf`)** — same name, different value |
| `brand/base/gradient-start` | `#3a6ff7` | **≠ `Brand/Gradient/Color 1` (`#3a79f7`)** |
| `brand/base/gradient-end` | `#1746a2` | = `Brand/Gradient/Color 2` |
| `text/primary` | `#000204` | **≠ `Brand/Text/Primary` (`#0b0c0f`)** |
| `text/inverse` | `#fafcff` | = Base/White |
| `background/primary` | `#fafcff` | = Brand/Background/Primary |
| `Brand/Blue-Black/500` | `#121417` | consistent |
| `Brand/Blue-White/400` | `#c6d6f6` | consistent |
| `Gradient` | *(empty value)* | Paint style with no resolvable value |
| `Shadow` | 5-layer drop shadow (below) | Effect style used on swatch cards |

`Shadow` effect [EXTRACTED]:

| Layer | Colour | Offset (x, y) | Blur | Spread |
|---|---|---|---|---|
| 1 | `#0000001A` | -1.385, 2.770 | 6.926 | 0 |
| 2 | `#00000017` | -2.770, 12.467 | 13.852 | 0 |
| 3 | `#0000000D` | -6.926, 29.089 | 18.007 | 0 |
| 4 | `#00000003` | -12.467, 52.637 | 22.163 | 0 |
| 5 | `#00000000` | -18.007, 81.726 | 23.548 | 0 |

Fractional values suggest a scaled copy of a shadow (≈ 1.385× of 1/2/5/9/13 px offsets) [DERIVED]. Layer 5 is fully transparent (no visual effect).

"Supporting Colours" `1557:25193` binds only `Gradient`, `Brand/Blue-Black/500`, `Brand/Blue-White/400` — swatch colours on that section are **not bound to variables** (likely hard-coded fills; to verify in Phase 5 via `get_design_context`).

### 2.1 Additional lowercase-scheme variables (found on Typography page `1557:39451`, `1557:44867`)

| Variable | Value | Conflict [DERIVED] |
|---|---|---|
| `brand/base/black` | `#0b0d0f` | **≠ `Brand/Base/Black` `#0b0c0f`** (1-digit drift) |
| `text/secondary` | `#030a14` | **≠ `Brand/Text/Secondary` `#555d6d`** (near-black vs mid-grey) |
| `text/tertiary` | `#181b21` | **≠ `Brand/Text/Tertiary` `#707a8f`** |
| `border/strong` | `#030a14` | no `Brand/Border/Strong` equivalent |
| `border/subtle` | `#ebf2ff` | = `Brand/Blue-White/300`; no `Brand/Border/Subtle` |
| `background/inverse` | `#0b0d0f` | no `Brand/Background/Inverse` equivalent |

The lowercase scheme is what the Typography page actually uses. Its secondary/tertiary text colours are near-black, contradicting the `Brand/Text/*` greys.

### 2.2 Consolidated value conflicts — lowercase (N2) vs `Brand/*` (N1) [added 2026-11-19]

Confirmed evidence (values returned by `get_variable_defs`). Rows 7–8 were originally recorded in `04-spacing-layout.md` L11.

| # | Lowercase variable | Value | `Brand/*` variable | Value | Lowercase found on | `Brand/*` source |
|---|---|---|---|---|---|---|
| 1 | `text/primary` | `#000204` | `Brand/Text/Primary` | `#0b0c0f` | `1557:23523`, `1557:44867` | `1557:31595` |
| 2 | `text/secondary` | `#030a14` | `Brand/Text/Secondary` | `#555d6d` | `1557:39451`, `1557:44867` | `1557:31595` |
| 3 | `text/tertiary` | `#181b21` | `Brand/Text/Tertiary` | `#707a8f` | `1557:39451`, `1557:44867` | `1557:31595` |
| 4 | `brand/blue-grey/300` | `#1f242e` | `Brand/Blue-Grey/300` | `#bfc4cf` | `1557:23523` | `1557:31595` |
| 5 | `brand/base/gradient-start` | `#3a6ff7` | `Brand/Gradient/Color 1` / `Brand/Button/Gradient Start` | `#3a79f7` | `1557:23523` | `1557:31595` |
| 6 | `brand/base/black` | `#0b0d0f` | `Brand/Base/Black` | `#0b0c0f` | `1557:39451` | `1557:31595` |
| 7 | `background/secondary` | `#f5f9ff` | `Brand/Background/Secondary` | `#f6f7f9` | `1558:51715` | `1557:31595` |
| 8 | `icon/primary` | `#000204` | `Brand/Icon/Primary` | `#0b0c0f` | `1561:56909`, `1561:57340` | `1557:31595` |

Component bindings (confirmed, `13` §D-01.3): no inspected component binds a lowercase variable; all bind `Brand/*`. The lowercase value `#3a6ff7` appears **raw (unbound)** in the Input/Outline Focused border `1066:38544`.

Interpretation: evidence favours `Brand/*` as canonical (`13` §D-01.5). **Unresolved — D-01 is not approved.**

---

## 3. Findings

| # | Finding | Severity | Tag |
|---|---|---|---|
| C1 | **Two parallel naming schemes** — `Brand/Title-Case/…` and `lowercase/kebab/…` — with **eight** value conflicts (`blue-grey/300`, gradient start, `text/primary`, `text/secondary`, `text/tertiary`, `base/black`, `background/secondary`, `icon/primary`) — full list §2.2. *[Corrected 2026-11-19 — evidence: `13-global-token-decisions.md` §D-01. Originally stated "six value conflicts"; the last two were recorded in `04` L11 but not counted here.]* | High | [EXTRACTED] |
| C2 | `Brand/Error/700` = `#9d4520` is identical to `Brand/Warning/700` — the Error scale jumps from red `#e72b23` (600) to orange-brown (700) then back to red `#7a2515` (800). Almost certainly a copy error. | High | [DERIVED] |
| C3 | `Brand/Blue-Black` scale is **not monotonic**: 300 `#1f242e` is lighter than 200 `#171e2a`; 50 `#202d47` is a saturated navy unlike the rest; 800 `#060707` is near-neutral. | Medium | [DERIVED] |
| C4 | `Brand/Blue-White` has a large jump between 300 `#ebf2ff` and 400 `#c6d6f6`; 50 duplicates `Base/White`. | Low | [DERIVED] |
| C5 | Status scales (Success/Warning/Error/Info) start at **100**; Blue/Grey scales start at **50**. | Low | [EXTRACTED] |
| C6 | `Supporting/*` duplicates `Brand/*` values under a second path. | Medium | [EXTRACTED] |
| C7 | Semantic tokens (`Text`, `Background`, `Border`, `Icon`, `Action`, `Feedback`) and component tokens (`Button`) sit in the same `Brand/` namespace as primitives — no visible primitive/semantic separation. | Medium | [EXTRACTED] |
| C8 | Gradient defined three ways: `Brand/Gradient/Color 1/2`, `Brand/Button/Gradient Start/End`, `brand/base/gradient-*` (start differs). `Gradient` style has no value via this tool. | Medium | [EXTRACTED] |
| C9 | **Corrected in Phase 4:** the Brand collection *does* have a Dark mode — Dark component variants resolve the same variables to different values (e.g. `Brand/Background/Secondary` `#181b21`, `Brand/Text/Primary` `#fafcff`, `Brand/Border/Primary` `#171e2a`; see `components/dropdown.md` §5). Full dark value set still to be collected from Dark variants. Light/dark is *also* modelled as variant properties (Dropdown `Theme`, Tooltip `Mode`). | High (for theming) | [BOUND] |
| C10 | No colour tokens for focus rings found in variables; effect styles named `Shadow/xs focused 4px brand-100` etc. exist in a published library "Design System" (`search_design_system`), not confirmed as local to this file. | Medium | [EXTRACTED] |

---

## 4. Proposed token mapping (for approval — not implemented)

> Depends on D-01, which is **open**. The mapping below illustrates a possible naming only.

Implementation would expose primitives and semantics separately as CSS custom properties, keeping Figma names traceable, e.g.:

| Figma variable | Proposed CSS custom property |
|---|---|
| `Brand/Blue/500` | `--annachy-color-blue-500` |
| `Brand/Blue-Grey/600` | `--annachy-color-blue-grey-600` |
| `Brand/Text/Primary` | `--annachy-color-text-primary` |
| `Brand/Action/Hover` | `--annachy-color-action-hover` |
| `Brand/Feedback/Error` | `--annachy-color-feedback-error` |

Conflicts C1/C2 must be resolved by the design owner before tokens are generated.

---

## 5. Open questions for design owner

1. Which naming scheme is canonical: `Brand/Text/Primary` (`#0b0c0f`) or `text/primary` (`#000204`)?
2. Is `Brand/Error/700` intentionally `#9d4520`?
3. Gradient start: `#3a79f7` or `#3a6ff7`?
4. Dark mode exists in variables (partially observed) — is dark theme in scope for the first release?
5. Are `Supporting/*` variables deprecated in favour of `Brand/*`?

---

## 6. Limitations

- `get_variable_defs` returns variables **bound within a node**, resolved to a single value. It does not return collection names, mode names, alias chains, or unbound variables. [INACCESSIBLE via current tools]
- `search_design_system` returned no results for local variables (searches published libraries only).
- The Radius page text names a collection `collection2ColourUsage` (see `04-spacing-layout.md`), suggesting at least one collection named "ColourUsage" — unconfirmed.
- Unbound (hard-coded) swatch fills will be checked in Phase 5.
