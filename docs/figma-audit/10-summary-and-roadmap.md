# 10 — Audit Summary & Implementation Roadmap

| Item | Value |
|---|---|
| File audited | Annachy CF — Design System · `rM3ixSG6i3DFfKZFWuxzs4` |
| Audit period | 2026-11-19 (Phases 1–6) |
| Access | **Read-only throughout.** Operations used: `get_metadata`, `get_variable_defs`, `get_design_context` (screenshots excluded), `search_design_system`, `get_libraries`, MCP skill resource read. **Never used:** `create_session` (read-only nature unproven), `download_assets` (not authorised), any write-capable tool. The Figma file was not modified. |
| Status | **Audit complete — awaiting approval.** Implementation **not started**. |

---

## 1. Deliverables

| # | Required deliverable | File |
|---|---|---|
| — | Audit plan | `00-audit-plan.md` |
| 1 | File & page inventory (39/39 pages) + operations log | `01-file-inventory.md` |
| 2 | Design tokens — colour | `02-color.md` |
| 2 | Design tokens — spacing, grid, layout, radius | `04-spacing-layout.md` |
| 2 | Design tokens — elevation & effects | `05-elevation-effects.md` (+ `raw/effects.json`) |
| 3 | Typography | `03-typography.md` |
| 4 | Component inventory | `07-component-inventory.md` |
| 5 | Component variants & states | `components/button.md`, `input.md`, `dropdown.md`, `checkbox.md`, `radio.md`, `toggle.md`, `selection-controls.md`, `tooltip.md`, `navigation.md` |
| 6 | Asset inventory | `06-iconography-assets.md` |
| 7 | Inconsistency report | `08-inconsistencies.md` |
| 8 | Accessibility observations | `09-accessibility.md` |
| 9 | Final audit summary | this file |
| 10 | Implementation roadmap | this file §7 |
| + | Dependencies & sources | `11-dependencies-and-sources.md` |
| + | Progress log | `audit-progress-log.md` |
| + | Raw evidence | `raw/metadata/*.xml` (15 pages), `raw/variant-matrices.md`, `raw/archive-diff.md`, `raw/effects.json`, `raw/phase3-working-notes.md` |

---

## 2. Findings at a glance

| Area | Headline | Report |
|---|---|---|
| File structure | 39 pages; 2 Navigation pages empty; "EMPTY PAGE" holds a divergent button set; ~97.7 % of 99,196 components are icons. | `01` |
| Colour | 130 `Brand/*` variables + conflicting lowercase scheme (**8** value conflicts — corrected 2026-11-19, was 6); Dark mode exists but only partially observed; probable copy error `Error/700`. | `02` |
| Typography | Proxima Nova (commercial licence). Two scales; components bind **Scale A** values and resolve the **Mobile** column where it differs. Duplicate H3; Body S naming collision (both weights used). *[Corrected 2026-11-19, was "Duplicate H3/Body S definitions".]* | `03` |
| Layout | Grid defined (360/4/16/16 · 1440/12/120/32 · 1920/12/140/32). **No spacing scale, no breakpoint ranges.** | `04` |
| Radius | Scale 4–34 documented but unbound; components use 4/8/12 (+ Input 6/10). | `04` |
| Effects | 32 documented shadows unused by components; components use undocumented `Button/*`, `Toggle/*`; 4 blurs have radius 0. | `05`, `11` |
| Icons | Six candidate sources; three used in production, including an **external library** and a Research-page Lucide icon. | `06`, `11` |
| Components | 11 sets, 1,397 variants inspected representatively. Missing: Navigation, Select trigger. ~20 screen-component masters not found. | `07`, `11` |
| Inconsistencies | **58 confirmed (19 High)**, 16 suspected *(updated 2026-11-19; was 56 / 15)*. | `08` |
| Accessibility | 3 text pairs fail AA (Primary Pressed 4.26, gradient label 3.89, Filled placeholder 1.25); Hover missing on 3 components; Error missing on 4; focus inconsistent; behaviour unverified. | `09` |

---

## 3. Confirmed specifications (usable once decisions in §5 do not affect them)

Values below were extracted directly and are **not** contested by conflicting sources.

| Area | Confirmed specification | Evidence |
|---|---|---|
| Font family / weights in use | Proxima Nova; Regular 400, Medium 500, Semibold 600, Bold 700 | `03`, components [BOUND] |
| Type styles used by components | Body XS—Semibold 12/18; Body S-Semi 14/18; H7 Semibold 16/18; H6 Semibold 18/20; H5 Semibold 20/24; Body S Regular 14/20; Body M Medium/Regular 16/24; Label Small Medium 14/20; Label Medium Medium 16/21; Label XSmall Regular 12/17; letter-spacing 0 — these are the **Mobile** Scale A values where Mobile ≠ Desktop; Desktop values are documented but not observed on components | `07` §4, `03` §4.1 |
| Brand primitive scales | `Brand/Blue`, `Blue-White`, `Blue-Grey`, `Success`, `Warning`, `Info` (all steps); `Error` except 700 | `02` §1.2 |
| Semantic colours bound by components | `Brand/Text/*`, `Background/*`, `Border/*`, `Button/*` (Light values); partial Dark values (`Background/Secondary #181b21`, `Text/Primary #fafcff`, `Border/Primary #171e2a`) | `02`, `dropdown.md` §5 |
| Grid | Mobile 360 · 4 col · 16/16; Desktop 1440 · 12 col · 120/32; Large 1920 · 12 col · 140/32 | `04` §1 |
| Button | 6 types × 6 states × 12 sizes; height = `Height/N`; radius 4 (24–28) / 8 (32–40) / 12 (42–56); padding/gap at 24, 32, 40, 48, 56; state colours per type | `button.md` |
| Input | Anatomy, 5 sizes, 14 px padding, typography, Default/Focused/Error colours | `input.md` |
| Dropdown | Menu 320/352 wide, padding 8, radius 12; Item 40/48 h, padding 12/10, gap 12; state colours; `Button/Focus` effect values | `dropdown.md` |
| Checkbox/Radio/Toggle | Variant matrices, Medium dimensions, typography, bound state colours, effect style values | component specs |
| Tooltip | 80-variant matrix, padding 10, radius 4, max-width 300, typography, dark/light colours | `tooltip.md` |
| Effect values | All 32 shadows, 5 blurs, 3 glass, `Button/*`, `Toggle/*` layers (verbatim) | `05`, `raw/effects.json` |

## 4. Assumptions currently in the documentation (to be confirmed — not specifications)

| # | Assumption | Where |
|---|---|---|
| AS-01 | Page markers ✓/◐/○ mean complete/in progress/not started. | `01` §1 |
| AS-02 | Checkbox/Radio Small = 20 px, Large = 28 px controls (from widths and Radio doc text). | `checkbox.md` §2 |
| AS-03 | Vertical padding on Buttons is nominal; height variable governs. | `button.md` §1.3 |
| AS-04 | Element mapping of some bound colours (e.g. Input Disabled/Success/Hover, Toggle Hover Off) inferred from variable lists. | `input.md`, `toggle.md` |
| AS-05 | Glass effects approximated by CSS `backdrop-filter`. | `05` §2 |
| AS-06 | CSS `box-shadow` strings are mechanical conversions of Figma effects. | `05` |
| AS-07 | All suspected items SUS-01…15. | `08` §B |

---

## 5. Unresolved design-owner decisions

| # | Decision | Blocks | Ref |
|---|---|---|---|
| D-01 | Canonical colour naming scheme (`Brand/*` vs lowercase) and resolution of **8** value conflicts *(corrected 2026-11-19)* | Colour tokens | `02` C1, §2.2 |
| D-02 | Is `Brand/Error/700 #9d4520` correct? | Colour tokens | SUS-01 |
| D-03 | Dark theme in scope for v1? Provide full Dark values | Theming | `02` C9 |
| D-04 | Confirm Typography System (Scale A) as canonical; resolve duplicate H3; Body S naming *(corrected 2026-11-19)* | Type tokens | `03` T3, §4.1 |
| D-05 | Mobile→Desktop typography switch breakpoint | Type tokens, CSS | `03`, `04` |
| D-06 | Proxima Nova web licence / Adobe Fonts kit; fallback stack | Font delivery | `03` T10 |
| D-07 | Breakpoint ranges; tablet in scope? max content width; reference mobile width 360 vs 393 *(added 2026-11-19)* | Layout, all components | `04` L2, L12 |
| D-08 | Spacing scale (if intended) | Layout tokens | `04` L1 |
| D-09 | Radius: are Input radii 6/10 valid? Final radius per component | Radius tokens | `04` L5–L6 |
| D-10 | Canonical shadow/elevation system; mapping to components; focus-ring token | Effect tokens | `05`, `11` §4.3 |
| D-11 | Intended Blur values (4 at radius 0) | Effect tokens | `05` E6 |
| D-12 | **Canonical icon source** (S1–S6) and icon size scale (14–42 vs 16–40) | Icons, Button, Input, Dropdown | `06`, `11` §3 |
| D-13 | Access to **Annachy Icons File** (file key/URL) for read-only audit | Icon export | `11` §1 |
| D-14 | Ownership/status of external **"Design System"** and **"UI Icons"** libraries | Select, focus shadows, icons | `11` §6.2 |
| D-15 | Licences: Solar-derived icons, Iconly Pro, Lucide `badge-check` | Icon redistribution | `06` §3, `11` |
| D-16 | Navigation: design in Figma or approve screen frames as interim | Navigation | `navigation.md` |
| D-17 | Select trigger: design in file or adopt external `Select` | Dropdown | `dropdown.md` D1 |
| D-18 | Location of masters for Bottom Nav Bar, Product card and ~20 screen components | Patterns | `11` §6.3 |
| D-19 | Remove/replace foreign tokens (`surface-bg`, `border-default`, `shadow/sm`, `--sds-*`) | Checkbox, Radio | INC-20 |
| D-20 | Missing states: Hover (Input/Outline, Checkbox, Radio), Error (Checkbox, Radio, Toggle, Dropdown), Focus+Checked, Link Hover | Components, a11y | `09` §2 |
| D-21 | Focus-indicator standard across components | All interactive | INC-26 |
| D-22 | Fix contrast failures A04, A14, A16 (or accept) | Button, Input | `09` §1 |
| D-23 | Theme mechanism: variable modes vs `Theme`/`Mode` variant properties | Dropdown, Tooltip | INC-32 |
| D-24 | Status colours: icon 600 shades vs Feedback 500 shades | Input, icons | INC-18 |
| D-25 | Status of EMPTY PAGE button set and Archive duplicates | Housekeeping | INC-06/07 |
| D-26 | Secondary Grey border bindings and Primary Pressed colour intent | Button | SUS-03, INC-37 |
| D-27 | Radio/Toggle vector visuals — provide tokenised specs (dot size, track/thumb sizes) | Radio, Toggle | INC-38 |

---

## 6. External dependencies & missing masters

| Dependency | Status | Needed for |
|---|---|---|
| **Annachy Icons File** (external library `lk-826bf23d…`) | In use by Button, Input/Outline, Dropdown; file key **unknown**; actively updated 2026-11-19 | Icons, components |
| **"Design System"** org library (`lk-483b…`) | Has `Select`, `Pagination`, `Shadow/*` styles; not linked; ownership unknown | Select trigger, focus shadows (if adopted) |
| **"UI Icons"** org library (`lk-c918…`) | Discoverable; no evidence of use | Icons (candidate) |
| Lucide (`lucide:badge-check`, Brainstorming `5:15330`) | Used by Dropdown Item Selected | Dropdown |
| Proxima Nova font files | Not in Figma; commercial | All typography |
| Masters of Bottom Nav Bar (`1633:30319`), Product card (`1471:36870`), Lab Card, Similar Products- Card, Watchlist buttons, Top Lablel, Product Details Sections, Colour Change Tabs, Normal Size, YL, Review, Category, Colour preview, Size option, Component 30, Action Button, Status Bar/iOS, Map Point icon, Cart icon | **Not found** in file or searchable libraries | Patterns & screens (not v1 component scope) |
| Navigation component | **Missing** (pages empty) | Navigation |
| Select trigger component | **Missing** | Dropdown/Select |

---

## 7. Phased implementation roadmap (proposal — not started)

Vanilla HTML/CSS/JS, native ES modules, no build step (per approved constraints). Each phase starts only when its gate is met.

| Phase | Scope | Gate (must be resolved first) | Deliverables | Exit criteria |
|---|---|---|---|---|
| **R0 — Decision gate** | Design owner resolves blocking decisions for R1/R2 | D-01–D-08 (hard: D-01, D-02, D-04, D-07, D-08; scope: D-03, D-05; R2: D-06) — see `12` §0. *[Corrected 2026-11-19 — previously also listed D-12, D-13; icon decisions block R3 and R5, not R1/R2.]* | Decision log in `docs/decisions/` (ADRs) | Signed-off decisions recorded |
| **R1 — Tokens** | `src/tokens/` primitives + semantic CSS custom properties (colour Light; Dark if D-03), typography, radius, grid, effects, spacing (if D-08) | R0 | `tokens.json` (traceable to Figma names), `primitives.css`, `semantic.css`, `themes/*` | Every token maps to a Figma variable/style or an approved decision |
| **R2 — Base** | Reset, typography classes, utilities, font loading, focus-ring utility | R1, D-06, D-21 | `src/base/*`, `src/annachy.css` | Renders specimen pages matching Scale A |
| **R3 — Core controls** | Button (+ gradient), Input (Outline/Filled), Checkbox, Radio, Toggle | R2; D-09, D-10, D-20, D-22, D-26, D-27 for affected parts; **D-12, D-13** for icon-bearing parts (Button, Input, Dropdown) *(added 2026-11-19)* | `src/components/<name>/*`, showcase pages, manual test checklists | Visual parity with specs; WCAG AA checks in `09` pass |
| **R4 — Composite** | Dropdown Menu/Item, Tooltip; Select trigger (only if D-17 resolved) | R3; D-17, D-23 | Components + `src/core/` utilities (focus management, positioning, keyboard) | Keyboard/ARIA behaviour specified and tested (currently [UNVERIFIED]) |
| **R5 — Icons** | Icon export (read-only `download_assets`, local staging) and SVG pipeline | D-12, D-13, D-15; explicit export approval | `src/icons/` (original SVG preserved), icon usage docs | Single approved source; licences recorded |
| **R6 — Navigation** | Mobile/Desktop navigation | D-16 (designed in Figma or interim approved) | Navigation component | Spec exists in Figma |
| **R7 — QA & release** | Accessibility verification, cross-browser, documentation, CHANGELOG/versioning | R3–R6 | Showcase site, test fixtures, release notes | Accessibility and visual QA sign-off |

Components that can proceed earliest (least affected by open decisions, once R1/R2 exist): **Tooltip** (dark), **Dropdown Item**, **Button Primary/Tertiary** — still subject to D-01/D-04/D-06.

---

## 8. What still prevents implementation approval

| # | Blocker | Decision(s) |
|---|---|---|
| 1 | Colour token source of truth unresolved (naming conflicts, Error/700, Dark mode extent) | D-01, D-02, D-03 |
| 2 | Typography canonical scale and responsive breakpoint unconfirmed; font licence absent | D-04, D-05, D-06 |
| 3 | No breakpoint ranges or spacing scale | D-07, D-08 |
| 4 | Canonical icon source undecided; primary icon library (Annachy Icons File) not accessible — **blocks R3 (icon-bearing components) and R5, not R1/R2** *(clarified 2026-11-19)* | D-12, D-13, D-15 |
| 5 | Shadow/focus system undecided; documented shadows unused | D-10, D-21 |
| 6 | Missing components (Navigation, Select trigger) | D-16, D-17 |
| 7 | Missing interaction/error states and 3 AA contrast failures | D-20, D-22 |
| 8 | Behavioural accessibility (keyboard, ARIA) not specified in Figma | Requires written behaviour spec (owner/engineering) |

Approval can be partial: R1–R2 may be approved once blockers 1–3 are resolved, with R3+ gated per component.
