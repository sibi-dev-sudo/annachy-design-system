# 08 — Inconsistencies

| Item | Value |
|---|---|
| Basis | Consolidation of findings in `01`–`07`, `09`, `11`, `components/*.md`, `raw/*`. **No new Figma access.** |
| Structure | §A **Confirmed** — directly observed in Figma data (tags EXTRACTED / APPLIED / BOUND / META / COMPUTED). §B **Suspected** — interpretations of confirmed data that need design-owner confirmation. |
| Severity | **High** — blocks or materially distorts implementation/accessibility · **Medium** — causes rework or visual drift · **Low** — hygiene/naming |
| Ref | Original finding ID and report (e.g. `02` C1 = `02-color.md` finding C1) |

---

## A. Confirmed inconsistencies

### A1. Sources of truth & duplication

| ID | Issue | Affected | Node IDs | Sev. | Ref |
|---|---|---|---|---|---|
| INC-01 | Icons stored in **six** candidate sources (4 in file + 2 external libraries); production components already use **three** of them (Annachy Icons File, Iconography pilot, Lucide exploration). | Button, Input, Dropdown | `375:10889`, `556:2`, `0:1`/`5:15330`, `561:36765`, `1777:9468`, `lk-826bf23d…`, `lk-c918…` | High | `06` I1, `11` §2–3 |
| INC-02 | Production components depend on an **external library (Annachy Icons File)** not reported by `get_libraries`; file key unavailable. | Button, Input/Outline, Dropdown | `1777:12415`, `1779:37533`, `1779:38814`, `1779:39439`, `1780:40128` | High | `11` §1 |
| INC-03 | **Two type scales** (Typography System: 28 rows, mobile/desktop; Specimen sheet: 11 styles, single size). | All text | `1557:39451`, `1557:44867` | High | `03` T1 |
| INC-04 | **Two colour naming schemes** with **eight** value conflicts (`text/primary` `#000204` vs `Brand/Text/Primary` `#0b0c0f`; `text/secondary` `#030a14` vs `#555d6d`; `text/tertiary` `#181b21` vs `#707a8f`; `brand/blue-grey/300` `#1f242e` vs `#bfc4cf`; gradient start `#3a6ff7` vs `#3a79f7`; base black `#0b0d0f` vs `#0b0c0f`; `background/secondary` `#f5f9ff` vs `#f6f7f9`; `icon/primary` `#000204` vs `#0b0c0f`). *[Corrected 2026-11-19 — `13-global-token-decisions.md` §D-01; originally "six value conflicts".]* | Docs pages vs components | `1557:23523`, `1557:39451`, `1557:44867`, `1557:31595`, `1558:51715`, `1561:56909`, `1561:57340` | High | `02` C1, §2.2 |
| INC-05 | **Two shadow systems** (Shadow Scale 17, Shadow Effects 15) — **neither used by any component**; components use undocumented `Button/*`, `Toggle/*`, foreign `shadow/sm`. | Effects | `1561:57736`, `1561:57961`; components `1504:*`, `1451:25074` | High | `05` E1, `11` §4.3 |
| INC-06 | Checkbox, Radio, Toggle, Dropdown/Item duplicated in Archive (structural copies; property `X Position` vs `Position`). | Selection controls, Dropdown | `1500:25474`, `1493:3`, `1438:5542`, `1464:2972` | Medium | `raw/archive-diff.md` |
| INC-07 | "EMPTY PAGE" contains a 432-variant button set with identical names but **360 variants of different size**. | Button | `479:4` › `1590:19040` vs `887:2492` | Medium | `raw/archive-diff.md` |
| INC-08 | Legacy 8-variant "check box" set coexists with the 126-variant Checkbox. | Checkbox | `1464:10379` | Low | `variant-matrices` |
| INC-09 | `Supporting/*` colour variables duplicate `Brand/*` values. | Colour | `1557:31595` | Medium | `02` C6 |
| INC-10 | Gradient defined three ways (`Brand/Gradient/Color 1/2`, `Brand/Button/Gradient Start/End`, `brand/base/gradient-*`). | Colour, gradient Button | `1557:31595`, `1557:23523`, `1153:3371` | Medium | `02` C8 |

### A2. Token / value conflicts

| ID | Issue | Affected | Node IDs | Sev. | Ref |
|---|---|---|---|---|---|
| INC-11 | Radius usage tables disagree (Button/Input → Radius/8 vs Buttons → Radius/12 vs "Standard 12 px"); components actually use size-dependent 4/8/12. | Button, Input | `1561:57590`, `1561:57673`, `1561:57530`; `887:*` | Medium | `04` L5, `button.md` B10 |
| INC-12 | Input `Radius` property includes **6 and 10** (not in the radius scale). | Input | `1066:37962`, `1066:40663` | Medium | `04` L6 |
| INC-13 | Radius variables documented but **not bound** on the radius page (raw px). | Radius docs | `1561:57341` | Low | `04` L4 |
| INC-14 | **H3** defined twice with different values (Bold 26/34 vs Semibold 26/30); no component binds either. *[Corrected 2026-11-19 — `13-global-token-decisions.md` §D-04. Originally also listed "Body S (Regular 14/20 vs Semibold 14/18)" as a value conflict — reclassified as a naming collision, see INC-57.]* | Typography | `1558:48900`/`48908` | High | `03` T3 |
| INC-15 | Type-scale header counts contradict rows (26 vs 28; 8 vs 9; 10 vs 11). | Typography docs | `1557:39451` | Low | `03` T2 |
| INC-16 | Text-style names mismatch their variables: "Body XS — Semibold" → `XXS-Semibold` vars; "Body S - Semi" → `XS-Semibold`; H6 uses `Line Height 2`. | Button, Tooltip | `887:333`, `1429:2` | Low | `button.md` B7 |
| INC-17 | H1 specimen rendered 36 px vs documented 32/48; specimens use auto line-height. | Typography docs | `1558:48865` | Medium | `03` T4–T5 |
| INC-18 | Status colours: components use icon vars (`error #e72b23`, `success #276732` — 600 shades) while `Brand/Feedback/*` are 500 shades (`#ff614e`, `#14a047`). | Input, icons | `1066:39889`, `1106:12812` | Medium | `06` I3, `input.md` IN4 |
| INC-19 | Off-palette colours in components: `#e8f0ff`, `#f3f4f7`, `#e4e7ec` (Button), `#3a6ff7` raw (Input focus), `#ffffff` / `#e1e1e2` (Checkbox/Radio), `#0141C0` / `#325CB3` (effects), `#6b7280` (docs). | Button, Input, Checkbox, Radio | `887:844`, `887:1624`, `887:1744`, `1066:38544`, `1504:53819`, `1504:52738` | Medium | `07` X8 |
| INC-20 | **Foreign token sets** in file/components: Simple Design System (`--sds-*`, `Text/Neutral/*`, `Background/Neutral/*`), unidentified kit (`surface-bg`, `border-default`, `shadow/sm`, `Blur/blur-*`, `Colors/alpha/50`). | Checkbox, Radio, effect docs | `1504:53819`, `1504:53976`, `1561:57814` | High | `05` E7, `checkbox.md` CB1, CB6 |
| INC-21 | Third naming variant `Brand / Blue-Grey / 600` (spaces). | Effect docs | `1561:57814` | Low | `05` E8 |
| INC-22 | Button variable path spelling: `Secondary-Grey` vs `Tertiary Grey`. | Button | `887:964`, `887:1564` | Low | `button.md` §1.4 |
| INC-23 | Icon size scales differ: Solar pilot 14–42 (9 steps) vs Annachy Icons File 16–40 (XS–XL). Button icon fixed 20 px at all sizes. | Icons, Button | `556:190`, `1777:9468` | Medium | `11` §3, `button.md` B6 |
| INC-24 | 4 of 5 Blur styles have radius **0**. | Blur | `1563:58676` | Medium | `05` E6 |
| INC-25 | Toggle thumb bound to `Button/Primary/Content/Loading`. | Toggle | `1504:54652` | Medium | `toggle.md` T2 |
| INC-57 | **Body S naming collision**: two Scale A rows named "Body S" (Regular 14/20 `1558:49021`; Semibold 14/18 `1558:49069`), both used by components; text-style names "Body S — Regular" vs "Body S - Semi", variables `Body/S` vs `Body/XS-Semibold`. *[Added 2026-11-19 — split from INC-14; `13` §D-04.]* | Input, Checkbox, Radio, Toggle (Regular); Button, Tooltip (Semibold) | `1558:49021`, `1558:49069`, `887:348`, `1429:2` | Low | `03` T3, §4.1 |
| INC-58 | **Mobile reference width inconsistent**: 360 (Foundations grid/layout, Sample Screen) vs 393 (PDP V1 screens). *[Added 2026-11-19 — `13` §D-07.]* | Layout, Patterns | `1558:55670`, `1561:56879`, `1214:11887`, `1218:13662`, `1280:10398` | Medium | `04` L12 |

### A3. Component state & model inconsistencies

| ID | Issue | Affected | Node IDs | Sev. | Ref |
|---|---|---|---|---|---|
| INC-26 | **Focus treatment differs per component** (2 px border; width-only; 1 px colour swap; border + glow; unchecked-only). | All interactive | see `09` §3 | High | `07` X1 |
| INC-27 | **Hover missing** (Input/Outline, Checkbox, Radio); Toggle and Input/Filled have Hover. | Inputs, selection controls | `1066:37962`, `1504:53300`, `1504:52363` | High | `07` X2 |
| INC-28 | **Link Hover identical to Default**. | Button Link | `887:1924` | High | `button.md` B1 |
| INC-29 | **Error state missing** for Checkbox, Radio, Toggle, Dropdown. | Selection controls, Dropdown | `1504:*`, `1451:*` | High | `07` X3 |
| INC-30 | Checkbox/Radio Focus is a single state value (no Focus+Checked); State mixes check-state and interaction. | Checkbox, Radio | `1504:53976`, `1504:52889` | High | `checkbox.md` CB2 |
| INC-31 | Disabled state naming: `Disabled`/`Disabled On` (Checkbox) vs `Disabled Unselected/Selected` (Radio) vs `Disabled Off/On` (Toggle). | Selection controls | `1504:*` | Low | `checkbox.md` CB7 |
| INC-32 | Theme modelled three ways: variable Dark mode, `Theme=Light/Dark` (Dropdown), `Mode=dark/light` (Tooltip, lower-case, raw Base colours). | Dropdown, Tooltip | `1451:25265`, `1448:16825` | Medium | `07` X5 |
| INC-33 | Input/Outline vs Input/Filled: different icon sources, property models (fixed icons vs slots), sub-text gap (4 vs 2), focus colour (`#3a6ff7` vs `#003fbc`). | Input | `1066:38089`, `1066:40783` | Medium | `input.md` IN2, IN6 |
| INC-34 | Gradient button vs All Buttons: different boolean property names, raw radius/shadow, no Size 38, no Loading. | Button | `1153:3370` | Low | `button.md` B9 |
| INC-35 | Selection Controls wrapper label 14/20 vs core sets 16/21. | Selection controls | `1504:57178` | Medium | `selection-controls.md` SC1 |
| INC-36 | Dropdown footer button overrides Button typography (14/20 Medium vs 16/18 Semibold). | Dropdown | `1451:23803` | Low | `dropdown.md` D4 |
| INC-37 | Primary Pressed (`#3372ef`) is **lighter** than Hover (`#003fbc`); Tertiary/Link Pressed are darker. | Button | `887:544`, `887:1444` | Medium | `button.md` B4 |
| INC-38 | Radio dot and Toggle track are **flattened vectors** (not tokenised). | Radio, Toggle | `1504:52686`, `1504:54624` | High | `07` X6 |
| INC-39 | Input/Outline shows Error-circle icon in all states (no boolean). | Input | `1066:38103` | Medium | `input.md` IN5 |
| INC-40 | Tooltip Mobile wider than Desktop for same content (182 vs 157); Desktop Heading fixed height 59. | Tooltip | `1448:16825` | Low | `tooltip.md` TT5, TT7 |

### A4. Missing specifications & masters

| ID | Issue | Node IDs | Sev. | Ref |
|---|---|---|---|---|
| INC-41 | **Navigation (Mobile & Desktop) pages empty**; navigation exists only as screen frames. | `1351:18314`, `1556:7200`; frames `1311:7548`, `1201:9774`, `1214:12126` | High | `navigation.md`, `11` §6.1 |
| INC-42 | **No closed Select trigger** component. | `1351:18309` | High | `dropdown.md` D1 |
| INC-43 | **Masters not found** for screen components: Bottom Nav Bar (`1633:30319`), Product card (`1471:36870`), and ~20 others (Lab Card, Size option, Status Bar/iOS …). | `1214:12125`, `1311:7795` | High | `11` §6.3 |
| INC-44 | **No spacing scale**. | — | High | `04` L1 |
| INC-45 | **No breakpoint ranges** (only frame widths 360/1440/1920); no tablet. | `1558:51715` | High | `04` L2 |
| INC-46 | Variable collection/mode names not retrievable; full Dark-mode value set not collected. | — | Medium | `02` §6, C9 |
| INC-47 | No opacity tokens; no focus-ring token; no elevation→component mapping. | — | Medium | `05` E9–E10 |
| INC-48 | No font fallback stack; Proxima Nova licence required. | — | High | `03` T10 |
| INC-49 | Default/neutral icon colour state missing. | `1106:12812` | Medium | `06` I4 |

### A5. Documentation hygiene

| ID | Issue | Node IDs | Sev. |
|---|---|---|---|
| INC-50 | Copy-paste headers: Radius page "COLOUR SYSTEM"; Blur page "Shadow Scale"; Grid footer "COLOUR SYSTEM"; Mobile grid labelled "Desktop". | `1561:57266`, `1563:58298`, `1558:55670`, `1558:51715` | Low |
| INC-51 | Variant counts wrong: Shadow Scale "18" (17); Blur "2" (8 specimens); Blur Large labelled "XS". | `1561:57818`, `1563:58680`, `1563:58729` | Low |
| INC-52 | Input column headings mismatch columns ("Active" vs Filled; Success/Disabled swapped). | `1567:2352`, `1567:2359` | Low |
| INC-53 | Typos: "Input Feild", "Typrography", "Clound Cross", "Essentional, UI", "CoreTooltip", "Bank Carrd", "Top Lablel". | `1567:1642`, `5:10905`, `561:20856`, `478:86765`, `1568:38568` | Low |
| INC-54 | Documentation chrome uses Montserrat (not the product font). | `1561:57345` | Low |
| INC-55 | Section "Button Master Components" contains selection controls. | `1568:36951` | Low |
| INC-56 | Sub-pixel width drift (Input 336/337). | `1066:37962` | Low |

---

## B. Suspected issues (interpretation — confirm with design owner)

| ID | Suspicion | Basis (confirmed data) | Sev. |
|---|---|---|---|
| SUS-01 | `Brand/Error/700` = `#9d4520` is a **copy error** (identical to `Warning/700`, breaks the red ramp). | `02` C2 | High |
| SUS-02 | `Brand/Blue-Black` scale is mis-ordered (non-monotonic lightness). | `02` C3 | Medium |
| SUS-03 | Secondary Grey **Pressed** border bound to `Border/Disabled` and **Hover** missing border are **mis-bindings**. | `button.md` B3 | Medium |
| SUS-04 | Secondary button Focus is unintentionally weak (same colour as Default border). | `button.md` B2 | High |
| SUS-05 | Scale B (specimen sheet) is reference material, not the product scale — components bind Scale A values only. | `03` §6, `07` §4 | Info |
| SUS-06 | EMPTY PAGE button set is an older/alternate version (differs in 360 sizes). | `raw/archive-diff.md` | Medium |
| SUS-07 | Iconography category icons originate from the public **Solar** set (style names, "Essentional, UI" typo). | `06` §3 | High (licence) |
| SUS-08 | `17xx` IDs are Figma's hidden internal copies of remote library components (node exists but "not on a visible page"). | `11` §1.1 | Info |
| SUS-09 | Bottom Nav Bar / Product card masters were **deleted** or live in an unpublished file. | `11` §6.3 | High |
| SUS-10 | Grid variables have per-breakpoint modes (only Desktop values returned). | `04` L3 | Medium |
| SUS-11 | Grid overlay field "24" means opacity %. | `04` §1.2 | Low |
| SUS-12 | Input chevron Up/Down pair is a numeric stepper, not a select affordance. | `11` §6.2 | Low |
| SUS-13 | Leading "." on `.Selection Controls / *` means intentionally hidden/unpublished sets. | `checkbox.md` | Info |
| SUS-14 | External "Design System" library (Select, Pagination, focus shadows) belongs to Annachy. | `11` §6.2 | Medium |
| SUS-15 | Widths of Selection Controls wrapper (216/228) indicate it defaults to Small size. | `selection-controls.md` SC3 | Info |
| SUS-16 | Typography variables have Mobile/Desktop modes, with Mobile active on component pages (components resolve Mobile values in all 6 cases where they differ; Desktop layout frame resolves Desktop grid values). *[Added 2026-11-19 — `13` §D-05.]* | `03` §4.1, T12; `04` §1.1 | Medium |

---

## C. Totals

| Category | Confirmed | High |
|---|---:|---:|
| A1 Sources & duplication | 10 | 5 |
| A2 Token/value conflicts | 17 | 2 |
| A3 Component states & model | 15 | 6 |
| A4 Missing specs & masters | 9 | 6 |
| A5 Documentation hygiene | 7 | 0 |
| **Confirmed total** | **58** | **19** |
| Suspected | 16 | 4 High |

*Totals updated 2026-11-19 (previously 56 confirmed / 15 suspected): +INC-57, +INC-58, +SUS-16; INC-14 narrowed to H3 (remains High).*
