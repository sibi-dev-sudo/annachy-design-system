# 12 — Design Decision Review

| Item | Value |
|---|---|
| Purpose | Present the 27 open decisions (D-01 … D-27) from `10-summary-and-roadmap.md` §5 with evidence, options and impact, so the design owner can decide. |
| Basis | Local audit files only (`02`–`11`, `components/*.md`, `raw/*`). **No Figma access. No decisions made.** |
| "Evidence-supported option" | Shown only where collected Figma data clearly favours one option. It is **not a decision** — every item still needs explicit confirmation as indicated. Where evidence does not favour an option, the field says **None — owner choice**. |
| Status values | **Owner confirmation required:** Yes (design owner) · Yes (legal/procurement) · Action (access/admin task, not a design choice) |

---

## 0. Phase-gate summary

### 0.1 Decisions that block R1 (Tokens)

| Type | Decisions | Why |
|---|---|---|
| **Hard blockers** — R1 cannot start | **D-01, D-02, D-04, D-07, D-08** | Colour names/values, type scale, breakpoints (needed for responsive tokens), spacing scale are the token set itself. |
| **Scope decisions** — must be answered, but "defer to later release" is a valid answer | **D-03, D-05, D-09, D-10, D-11, D-23, D-24** | Each determines whether a token group is included in R1 or postponed. |

### 0.2 Decisions that block R2 (Base)

| Decisions | Why |
|---|---|
| **D-06** | Font files/licence and fallback stack are required for base typography. |
| **D-05, D-07** | Responsive type classes need the breakpoint and switch point. |
| **D-21** | The base layer includes the shared focus-ring utility. |
| (all R1 hard blockers) | R2 consumes R1 tokens. |

### 0.3 Note on the roadmap gate

`10-summary-and-roadmap.md` §7 lists D-12 and D-13 in the R0 gate. On review, **icon decisions do not block R1/R2**; they block R3 (components that embed icons) and R5 (icon pipeline). The roadmap gate is therefore *more conservative* than strictly necessary; this document records the refinement but does not change the roadmap. **Update 2026-11-19:** the refinement has now been applied to `10-summary-and-roadmap.md` §7 (R0, R3) and §8 (blocker 4).

---

## 1. Global blockers — tokens, typography, layout

### D-01 · Canonical colour naming scheme and the 8 value conflicts

*[Corrected 2026-11-19 — heading previously said "6 value conflicts"; the two "Also" items below are conflicts 7–8 (`02` §2.2).]*

| Field | Detail |
|---|---|
| Figma evidence | 130 `Brand/*` variables in Colour Usage `1557:31595`. A lowercase scheme on docs pages (`1557:23523`, `1557:39451`, `1557:44867`, `1558:51715`). **Components bind `Brand/*`** (all Phase 4 inspections). Light/Dark values observed for `Brand/*`. |
| Conflicts | `text/primary #000204` vs `Brand/Text/Primary #0b0c0f` · `text/secondary #030a14` vs `#555d6d` · `text/tertiary #181b21` vs `#707a8f` · `brand/blue-grey/300 #1f242e` vs `Brand/Blue-Grey/300 #bfc4cf` · gradient start `#3a6ff7` vs `#3a79f7` · base black `#0b0d0f` vs `#0b0c0f`. Also `background/secondary #f5f9ff` vs `#f6f7f9`, `icon/primary #000204` vs `#0b0c0f`. |
| Affected | All tokens (R1) and every component. |
| Evidence-supported option | **`Brand/*`** — it is the scheme bound by all production components and the only one with an observed Dark mode. |
| Risk of delay | R1 cannot start; any token work would need rework. |
| Owner confirmation | **Yes (design owner)** — including whether lowercase variables are deprecated. |

### D-02 · `Brand/Error/700 = #9d4520`

| Field | Detail |
|---|---|
| Figma evidence | `Brand/Error/700 #9d4520` is identical to `Brand/Warning/700`; Error ramp goes `#e72b23` (600) → `#9d4520` (700) → `#7a2515` (800). |
| Options | (a) Value is intended · (b) Copy error — owner supplies the correct value. |
| Affected | Error colour scale (R1); any dark-red usage. |
| Evidence-supported option | Evidence *suggests* (b) (SUS-01), but the correct value **cannot be derived** from the file. |
| Risk of delay | Low immediate impact (700 not observed in component bindings); risk of shipping a wrong token. |
| Owner confirmation | **Yes (design owner)** — and the replacement value if (b). |

### D-03 · Dark theme scope for v1

| Field | Detail |
|---|---|
| Figma evidence | Dark mode exists in variables: `Background/Secondary #181b21`, `Text/Primary #fafcff`, `Border/Primary #171e2a` (Dropdown Dark `1451:25265`). Full Dark set **not collected** (mode values only visible per Dark variant). Tooltip uses raw Base Black/White for dark. |
| Options | (a) Light only in v1 · (b) Light + Dark in v1 (requires full Dark value set and read-only collection from Dark variants or owner export). |
| Affected | R1 theme files, every component's colour layer, accessibility testing scope. |
| Evidence-supported option | None — owner choice (product scope). |
| Risk of delay | If decided later as (b), semantic token structure may need refactoring unless R1 is built mode-ready. |
| Owner confirmation | **Yes (design owner / product)** |

### D-04 · Canonical type scale; duplicate H3; Body S naming

*[Corrected 2026-11-19 — Body S is a naming collision (both rows used), not a value conflict (`13` §D-04).]*

| Field | Detail |
|---|---|
| Figma evidence | Scale A "Typography System" `1557:39451` (28 rows, mobile/desktop). Scale B specimen sheet `1557:44867` (11 styles, single size, generic Proxima Nova specimen). **All component text styles match Scale A values** (`07` §4). |
| Conflicts | H3: Bold 26/34 (`1558:48900`) vs Semibold 26/30 (`1558:48908`). Body S: Regular 14/20 (`1558:49021`) and Semibold 14/18 (`1558:49069`) — **both used by components** (naming collision). Header counts 26 vs 28 rows. Components resolve Mobile values where Mobile ≠ Desktop (`03` T12). H1 specimen rendered 36 px. |
| Affected | Type tokens (R1), base typography (R2), all components. |
| Evidence-supported option | **Scale A** as canonical (component bindings). Body S: **both rows are bound** (Regular 14/20 by Input/selection controls; Semibold 14/18 as "Body S - Semi" by Button/Tooltip) → only naming needs a decision. H3: no component binding → **no evidence-supported option**. *[Corrected 2026-11-19; previously cited only the Semibold binding.]* |
| Risk of delay | R1/R2 blocked; risk of two parallel scales in code. |
| Owner confirmation | **Yes (design owner)** |

### D-05 · Mobile → Desktop typography switch point

| Field | Detail |
|---|---|
| Figma evidence | Scale A gives separate Mobile and Desktop sizes; no switch width documented. Design frames: 360 / 1440 / 1920 (PDP V1: 393). Components resolve the **Mobile** values where they differ (`03` T12) *(added 2026-11-19)*. |
| Options | Any breakpoint value — none present in file. |
| Affected | Responsive type tokens (R1), typography classes (R2). |
| Evidence-supported option | None — owner choice (depends on D-07). |
| Risk of delay | Responsive typography cannot be implemented; mobile-only or desktop-only fallback would be an assumption. |
| Owner confirmation | **Yes (design owner)** |

### D-06 · Proxima Nova licence and fallback stack

| Field | Detail |
|---|---|
| Figma evidence | Typeface Proxima Nova; file states "Commercial only", "Google Fonts: N/A", "Adobe Fonts: Included", web use needs "a licensed web embed" (`1557:44867`). Fonts are not exportable from Figma. No fallback stack. |
| Options | (a) Adobe Fonts kit · (b) Self-hosted licensed web fonts in `src/assets/fonts/` · (c) Different typeface (would change the design) · plus a fallback stack. |
| Affected | R2 base, all components, visual QA. |
| Evidence-supported option | None — owner/procurement choice. |
| Risk of delay | R2 blocked; implementing with a substitute font would invalidate visual QA. |
| Owner confirmation | **Yes (legal/procurement + design owner for fallback)** |

### D-07 · Breakpoint ranges, tablet, max content width

| Field | Detail |
|---|---|
| Figma evidence | Grid frames only: Mobile 360 (4 col, 16/16), Desktop 1440 (12 col, 120/32), Large 1920 (12 col, 140/32). Grid variables `grid/*` exist (Desktop values returned). No ranges, no tablet, no max width. PDP V1 mobile screens use **393** wide (`04` L12) *(added 2026-11-19)*. |
| Options | Owner defines ranges (e.g. where Mobile ends / Desktop begins) — no values in file. |
| Affected | R1 layout tokens, R2 base, every responsive component, D-05. |
| Evidence-supported option | None — owner choice. |
| Risk of delay | Layout and responsive behaviour cannot be specified; reflow accessibility (1.4.10) unverifiable. |
| Owner confirmation | **Yes (design owner)** |

### D-08 · Spacing scale

| Field | Detail |
|---|---|
| Figma evidence | No spacing page or spacing variables. Raw padding/gap values observed in components: **2, 4, 6, 8, 10, 12, 14, 16, 18, 20** (Button, Input, Dropdown, Tooltip, Checkbox specs). Variable `S = 8` exists on effect pages. |
| Options | (a) Define a scale (owner chooses steps) · (b) No scale — components keep raw values. |
| Affected | R1 tokens, all components. |
| Evidence-supported option | None — observed values are listed as input only; choosing a scale is a design decision. |
| Risk of delay | Inconsistent spacing in code; later refactor of every component. |
| Owner confirmation | **Yes (design owner)** |

### D-09 · Radius per component; Input radii 6 and 10

| Field | Detail |
|---|---|
| Figma evidence | Documented scale 4–34 (`1561:57646`), unbound on its page. Components bind `Radius/4` (Button 24–28, Checkbox), `Radius/8` (Button 32–40, Input, Dropdown Item), `Radius/12` (Button 42–56, Dropdown Menu); raw 4 (Tooltip, gradient Button). Input `Radius` property offers 4/**6**/8/**10**/12. Docs disagree (Button 8 vs 12). |
| Options | Keep Input 6/10 (add to scale) · remove them · reduce Input radius options to scale values. |
| Affected | R1 radius tokens; Input (R3). |
| Evidence-supported option | For current components, bindings to `Radius/4/8/12` are unambiguous. **6/10 — none (owner choice).** |
| Risk of delay | Low for R1 (4/8/12 confirmed); Input variants remain undefined. |
| Owner confirmation | **Yes (design owner)** for 6/10 and for the docs-table conflict. |

### D-10 · Shadow/elevation system and focus-ring token

| Field | Detail |
|---|---|
| Figma evidence | Documented: Shadow Scale (17) + Shadow Effects (15) — **not used by any component**. Used by components: `Button/Default`, `Button/Hover`, `Button/Focus`, `Toggle/On/Off/Press`, foreign `shadow/sm`. External library "Design System" has `Shadow/xs…3xl` and focus shadows (ownership unknown). |
| Options | (a) Documented Scale/Effects as canonical (components to be remapped) · (b) Component-used styles as canonical (document them) · (c) External library styles · (d) Combination. |
| Affected | R1 effect tokens, R2 focus utility, Checkbox, Radio, Toggle, Dropdown. |
| Evidence-supported option | None — evidence shows *usage* of (b) but documentation favours (a); this is a design-system governance choice. |
| Risk of delay | Effect tokens and focus styling cannot be finalised; inconsistent elevation. |
| Owner confirmation | **Yes (design owner)** |

### D-11 · Blur values (4 styles at radius 0)

| Field | Detail |
|---|---|
| Figma evidence | `Blur/SM-01`, `SM-02`, `MD-01`, `MD-02` = FOREGROUND_BLUR radius **0**; `Blur/XS-01` = 4; Glass XS/SM/MD = 5/10/20 (`1563:58676`). No component uses blur. |
| Options | Supply intended values · drop the four styles · defer blur tokens. |
| Affected | R1 effect tokens only. |
| Evidence-supported option | None — intended values unknown. |
| Risk of delay | Low — no component depends on blur; can be deferred. |
| Owner confirmation | **Yes (design owner)** |

### D-23 · Theme mechanism

| Field | Detail |
|---|---|
| Figma evidence | Variable Dark mode on `Brand/*` (Dropdown). Variant properties: Dropdown `Theme=Light/Dark`, Tooltip `Mode=dark/light` (raw Base Black/White, not semantic tokens). |
| Options | (a) Variable modes → CSS theme classes/attributes · (b) Per-component variant properties · (c) Mixed. |
| Affected | R1 theme structure, Dropdown, Tooltip. |
| Evidence-supported option | **(a)** — the variables already resolve per mode, and Dropdown's Dark variant uses the same semantic names; Tooltip would need re-binding. |
| Risk of delay | Theme architecture in R1 may need rework. |
| Owner confirmation | **Yes (design owner)** — only relevant if D-03 includes Dark (otherwise defer). |

### D-24 · Status colours: 600 (icons) vs 500 (Feedback)

| Field | Detail |
|---|---|
| Figma evidence | Icon semantic vars `error #e72b23`, `success #276732`, `warning #b9512e` (600 shades, `1106:12812`) — used by Input Error/Success. `Brand/Feedback/*` = `#ff614e`, `#14a047`, `#f26e2d` (500 shades) — not observed in component bindings. |
| Options | (a) 600 shades for status text/borders · (b) 500 shades · (c) Separate roles (e.g. fills vs text). |
| Affected | R1 semantic tokens, Input, future Alerts/validation. |
| Evidence-supported option | None — usage evidence favours 600 but Feedback tokens exist explicitly; owner choice. Contrast of either on page background not computable (`09` §1.2). |
| Risk of delay | Inconsistent error colours across components. |
| Owner confirmation | **Yes (design owner)** |

---

## 2. Icons and external dependencies

### D-12 · Canonical icon source and size scale

| Field | Detail |
|---|---|
| Figma evidence | Six candidates (`11` §3): S1 Iconography catalogue (1,243 slots), S2 Iconography pilots (52 icons, used by Input/Filled), S3 Archive Component Source (240 icons), S4 Brainstorming (Lucide etc., `badge-check` used by Dropdown), S5 **Annachy Icons File** external (used by Button, Input/Outline, Dropdown; updated 2026-11-19), S6 "UI Icons" external (no observed use). Size scales: 14–42 (S2/S3) vs XS 16–XL 40 (S5). |
| Options | S1–S6, or a combination; one size scale. |
| Affected | R3 (Button, Input, Dropdown), R5 icon pipeline. **Not R1/R2.** |
| Evidence-supported option | **None — per instruction, no icon source is recommended.** |
| Risk of delay | R3 components with icons and R5 blocked; risk of mixed icon styles. |
| Owner confirmation | **Yes (design owner)** |

### D-13 · Access to Annachy Icons File

| Field | Detail |
|---|---|
| Figma evidence | Library key `lk-826bf23d…`; file key not exposed; components' masters are hidden internal copies (`11` §1). |
| Options | Provide file URL/key with read access · decline (icons from S5 cannot be audited/exported). |
| Affected | D-12 evaluation, R5. |
| Evidence-supported option | Providing read access (procedural; needed for any S5 evaluation). |
| Risk of delay | S5 cannot be assessed; D-12 is decided with incomplete data. |
| Owner confirmation | **Action (access/admin)** |

### D-14 · Ownership of "Design System" and "UI Icons" libraries

| Field | Detail |
|---|---|
| Figma evidence | "Design System" (`lk-483b…`): `Select`, `Pagination`, `Shadow/*` incl. focus shadows; updated 2026-05/07. "UI Icons" (`lk-c918…`): kebab-case icons, updated 2026-04-16. Neither linked to the file. |
| Options | Annachy-owned and current · Annachy-owned but legacy · third-party/unrelated. |
| Affected | D-10, D-12, D-17. |
| Evidence-supported option | None — ownership cannot be determined from the file. |
| Risk of delay | Options for Select and shadows remain open. |
| Owner confirmation | **Yes (design owner)** |

### D-15 · Icon licences

| Field | Detail |
|---|---|
| Figma evidence | Iconography style/category names match the public Solar set (SUS-07); "Iconly Pro" (commercial) frames on Sample Screen; Lucide `badge-check` used in Dropdown; Amazon/Flipkart logos on research pages. |
| Options | Confirm licences and attribution per source · replace unlicensed icons. |
| Affected | R5; Dropdown (Lucide); legal compliance. |
| Evidence-supported option | None — legal determination. |
| Risk of delay | Cannot redistribute icons in the library. |
| Owner confirmation | **Yes (legal + design owner)** |

### D-18 · Missing masters for screen components

| Field | Detail |
|---|---|
| Figma evidence | Bottom Nav Bar master child `1633:30319` and Product card `1471:36870` **not found**; ~20 screen components (Lab Card, Size option, Status Bar/iOS, …) have no local masters and no library match (`11` §6.3). |
| Options | Provide the source file · confirm deleted (out of scope) · re-create in Figma. |
| Affected | Patterns/screens — **not in v1 component scope** per inventory. |
| Evidence-supported option | None. |
| Risk of delay | Low for v1 components; high if patterns are expected in the library. |
| Owner confirmation | **Yes (design owner)** |

---

## 3. Component-specific decisions

### D-16 · Navigation

| Field | Detail |
|---|---|
| Figma evidence | Navigation · Mobile `1351:18314` and · Desktop `1556:7200` are **empty**. Screen frames only: Desktop "Main navigation" `1311:7548` (1440 × 88), mobile Top Nav Bar `1201:9774`, TOP NAV `1214:12126`; Brainstorming tab-bar explorations `5:12734`. "Bottom Nav Bar/Default" is an action bar, not navigation. |
| Options | (a) Design Navigation in Figma first · (b) Approve existing screen frames as interim spec · (c) Exclude from v1. |
| Affected | R6. |
| Evidence-supported option | None — owner choice. |
| Risk of delay | R6 blocked; app shells can't use library navigation. |
| Owner confirmation | **Yes (design owner)** |

### D-17 · Select trigger

| Field | Detail |
|---|---|
| Figma evidence | No closed Select component; Dropdown provides menu and items only. External "Design System" has `Select` (ownership unknown, D-14). Header frames "Delivery location" `1311:7550` / "Profile" `1311:7564` show label + chevron patterns. |
| Options | (a) Design in this file · (b) Adopt external `Select` (after D-14) · (c) Implement Dropdown without a trigger (menu only). |
| Affected | R4 Dropdown/Select. |
| Evidence-supported option | None — owner choice. |
| Risk of delay | A usable form select cannot be delivered. |
| Owner confirmation | **Yes (design owner)** |

### D-19 · Foreign tokens in Checkbox/Radio

| Field | Detail |
|---|---|
| Figma evidence | Unchecked Checkbox/Radio bind `surface-bg #ffffff`, `border-default #e1e1e2`; Focus binds `shadow/sm`, `Blur/blur-0/2`, `Colors/alpha/50`; `--sds-*` variables on docs pages. None belong to the Annachy palette. |
| Options | Replace with Annachy tokens (owner specifies which) · keep as-is · add them to the Annachy set. |
| Affected | Checkbox, Radio (R3). |
| Evidence-supported option | None for the replacement values (closest palette white is `#fafcff`; no palette match for `#e1e1e2`). |
| Risk of delay | Checkbox/Radio would ship with tokens outside the system. |
| Owner confirmation | **Yes (design owner)** |

### D-25 · EMPTY PAGE button set and Archive duplicates

| Field | Detail |
|---|---|
| Figma evidence | Archive Checkbox/Radio/Toggle/Dropdown Item are structural copies of Components-page sets. EMPTY PAGE `1590:19040` has the same 432 names but 360 differ in size. |
| Options | Treat Components-page sets as current and others as legacy · designate another set as current. |
| Affected | Which nodes R3 specs reference. |
| Evidence-supported option | **Components-page sets as current** — they sit in the Components section, carry ✓ markers, and are the sets referenced by nested instances (Dropdown footer button, wrapper). |
| Risk of delay | Low (specs already reference Components-page sets); risk of designers editing the wrong copy. |
| Owner confirmation | **Yes (design owner)** |

### D-26 · Button: Secondary Grey bindings and Primary Pressed intent

| Field | Detail |
|---|---|
| Figma evidence | Secondary Grey Pressed binds `Border/Disabled #dcdfe5`; Hover has no border bound (`887:1144`, `887:1024`). Primary Pressed `#3372ef` (Blue/400) is lighter than Hover `#003fbc` (Blue/600); Tertiary/Link Pressed are darker (`#003fbc`). |
| Options | Confirm as intended · correct bindings/colours (owner supplies). |
| Affected | Button (R3); also A04 contrast (D-22). |
| Evidence-supported option | None — intent cannot be inferred. |
| Risk of delay | Button states implemented with possible errors. |
| Owner confirmation | **Yes (design owner)** |

### D-27 · Radio and Toggle vector specs

| Field | Detail |
|---|---|
| Figma evidence | Radio Selected container is a flattened vector `1504:52686`; Toggle track/thumb flattened `1504:54624` (38 × 20 Medium). Colours partly recoverable from other states (Toggle On `#004feb`, thumb `#fafcff`). Dot diameter, ring width, thumb size and travel **not available**. |
| Options | Owner provides dimensions/tokens · permit measurement from SVG export (requires export approval) · rebuild from screenshot (assumption-based). |
| Affected | Radio, Toggle (R3). |
| Evidence-supported option | None. |
| Risk of delay | Radio/Toggle cannot be built to spec without assumptions. |
| Owner confirmation | **Yes (design owner)**; export route needs explicit approval. |

> **R3-0 update (2026-11-19, read-only inspection — `r3-0-evidence.md` §10–§13):** narrowed. Now **known**: Radio dot 8/10/12 at inset 6/7/8, fill `Background/Primary`; ring colour `Blue/300`; Toggle tracks 32×16 / 38×20 / 44×24, thumbs 12/16/20, inset 2, travel; Off track `Blue-Grey/50`. **Still not readable** (rendered as images): Checkbox check & indeterminate glyph geometry/colour; Radio selected ring stroke width; Toggle thumb stroke width, track radius, Focus Off / Pressed Off stroke element and width. Options unchanged: owner supplies values, or approves read-only SVG export of those nodes.

---

## 4. Accessibility and behaviour decisions

### D-20 · Missing states

| Field | Detail |
|---|---|
| Figma evidence | Hover missing: Input/Outline, Checkbox, Radio; Link Hover identical to Default. Error missing: Checkbox, Radio, Toggle, Dropdown. Focus+Checked missing (Checkbox/Radio). (`09` §2) |
| Options | Design the missing states in Figma · accept omissions (documented). |
| Affected | R3, R4; validation patterns. |
| Evidence-supported option | None for values. Note: WCAG requires a visible focus indicator for every focusable state (2.4.7); hover/error states are product decisions. |
| Risk of delay | Components ship with gaps or with invented states (not permitted). |
| Owner confirmation | **Yes (design owner)** |

> **R3-0 update (2026-11-19):** Focus + Checked/Selected — owner instruction applied as a **RECOMMENDATION, not a confirmed Figma specification**: preserve the checked appearance (fill, glyph/dot) and apply the focus treatment on top. Flagged in R3 CSS/README. Other missing states (Hover, Error) unchanged: reproduced as absent.

### D-21 · Focus-indicator standard

| Field | Detail |
|---|---|
| Figma evidence | Five different treatments (`09` §3): 2 px border (Button Primary, 1.36:1 vs fill), width-only change (Button Secondary), 1 px colour swap (Inputs), 2 px + `Button/Focus` glow (Dropdown Item), unchecked-only (Checkbox/Radio). |
| Options | Adopt one existing treatment system-wide · define a new focus ring. |
| Affected | R2 focus utility, all interactive components. |
| Evidence-supported option | None as a decision. Observation: the Dropdown Item treatment (2 px `#003fbc` + glow) has the highest measured contrast against its fill (8.04:1). |
| Risk of delay | R2 focus utility blocked; inconsistent keyboard UX; 2.4.7 risk. |
| Owner confirmation | **Yes (design owner)** |

### D-22 · Contrast failures A04, A14, A16

| Field | Detail |
|---|---|
| Figma evidence | A04 Primary Pressed label 4.26:1 · A14 gradient label vs `#3a79f7` 3.89:1 · A16 Filled placeholder `#dcdfe5` on `#f6f7f9` 1.25:1 (`09` §1). |
| Options | Adjust colours (owner supplies) · accept with documented exception. |
| Affected | Button, Input (R3). |
| Evidence-supported option | A16 at 1.25:1 is far below every WCAG threshold for text; correcting it is the only AA-compliant option. A04/A14 — owner choice of fix (both pass only as large text). |
| Risk of delay | Library would ship known AA failures. |
| Owner confirmation | **Yes (design owner)** |

### B-01 · Behaviour specification (not in D list — added for completeness)

| Field | Detail |
|---|---|
| Figma evidence | No interaction data inspected; keyboard, ARIA roles/names, tooltip trigger/dismiss, error announcements, reduced motion all **[UNVERIFIED]** (`09` §6). |
| Options | Owner/engineering writes a behaviour spec · adopt WAI-ARIA Authoring Practices patterns as the baseline (still a decision). |
| Affected | R3, R4. |
| Evidence-supported option | None. |
| Risk of delay | Components cannot be accessibility-approved. |
| Owner confirmation | **Yes (design owner + engineering)** |

> **Resolved 2026-11-19:** owner approved native HTML semantics as the behaviour baseline, including accessible names and ARIA state where required (`docs/implementation/r3-components-spec.md` §2.5).

---

## 5. Decision matrix

| ID | Group | Blocks | Evidence-supported option? | Owner confirmation |
|---|---|---|---|---|
| D-01 | Global | **R1 (hard)** | Yes — `Brand/*` | Yes |
| D-02 | Global | **R1 (hard)** | Suggests error; value unknown | Yes |
| D-03 | Global | R1 (scope) | No | Yes |
| D-04 | Global | **R1 (hard)**, R2 | Yes — Scale A; Body S both used (naming only); H3 none | Yes |
| D-05 | Global | R1 (scope), **R2** | No | Yes |
| D-06 | Global | **R2** | No | Yes (legal) |
| D-07 | Global | **R1 (hard)**, R2 | No | Yes |
| D-08 | Global | **R1 (hard)** | No | Yes |
| D-09 | Global | R1 (scope) | Partial — 4/8/12 | Yes |
| D-10 | Global | R1 (scope) | No | Yes |
| D-11 | Global | R1 (scope) | No | Yes |
| D-12 | Icons | R3, R5 | No (per instruction) | Yes |
| D-13 | Icons | R5 (and D-12) | Yes — grant access | Action |
| D-14 | Icons/external | R3–R5 | No | Yes |
| D-15 | Icons | R5 | No | Yes (legal) |
| D-16 | Component | R6 | No | Yes |
| D-17 | Component | R4 | No | Yes |
| D-18 | External | Patterns (post-v1) | No | Yes |
| D-19 | Component | R3 | No | Yes |
| D-20 | A11y | R3, R4 | No | Yes |
| D-21 | A11y | **R2**, R3 | No | Yes |
| D-22 | A11y | R3 | Partial — A16 must change | Yes |
| D-23 | Global | R1 (scope) | Yes — variable modes | Yes |
| D-24 | Global | R1 (scope) | No | Yes |
| D-25 | Component | R3 (reference) | Yes — Components-page sets | Yes |
| D-26 | Component | R3 | No | Yes |
| D-27 | Component | R3 | No | Yes |
| B-01 | Behaviour | R3, R4 | No | Yes |
