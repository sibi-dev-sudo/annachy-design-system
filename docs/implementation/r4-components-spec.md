# R4 Implementation Plan — Composite Components (Dropdown, Tooltip, Select)

| Item | Value |
|---|---|
| Phase | **R4 — Composite** (roadmap `docs/figma-audit/10-summary-and-roadmap.md` §7) |
| Behaviour | **Draft behaviour specification:** `r4-behaviour-spec.md` (awaiting approval) |
| Status | **Plan only. No code. No Figma access for this plan** (built from the original audit evidence). |
| Depends on | R1 tokens (464), R2 base, R3 (closed: `r3-closure-report.md`), reused by R4: Input (search field), Button (footer), Checkbox (Multiple indicator) |
| Evidence | `docs/figma-audit/components/dropdown.md`, `tooltip.md`; `07` §1; `11` §2, §6.2; `12` D-14, D-17, D-23; `09` |
| Rules carried from R3 | Exact Figma values only; component-local evidenced values; faithful reproduction of flagged defects; native semantics first (B-01); read-only Figma inspection only; no asset export; `:where()` state precedence; per-variant browser fixtures + mutation tests + real-input CDP audit |

---

## 1. Scope and evidence status

| Component | Figma set | Variants | Inspected so far | Status |
|---|---|---:|---|---|
| Dropdown / Item | `1451:25092` | 40 (Selection × Platform × Theme × State) | Desktop Light Single: Default, Focus, Selected, Disabled [APPLIED]; Hover, Multiple/Selected [BOUND]; Dark (variables) | **Partial** |
| Dropdown / Menu | `1451:25521` | 48 (Selection × Platform × Theme × Search × Footer) | Desktop Light, Search On, Footer Label [APPLIED]; sizes for all groups [META] | **Partial** |
| Tooltip | `1448:16825` | 80 (Device × Mode × Arrow × Format) | Mobile dark Text-only, Desktop light Heading [APPLIED]; Mobile light [BOUND] | **Partial** |
| Select (closed trigger) | — | — | **Does not exist in this file** (D1, X9). Only candidate: the external library "Design System" › `Select` (ownership unknown, not linked: `11` §6.2) | **Blocked (D-17, D-14)** |

## 2. Confirmed specification (from the audit)

### 2.1 Dropdown / Item (`dropdown.md` §3–§4)
- **Row:** gap 12, padding 12 / 10, min-height 40 (Desktop), radius `Radius/8`, full width.
- **Indicator:** 20 × 20.
- **Label:** Label Small Medium 14/20, flex 1.
- **States (Desktop, Light, Single):**
  - Default: `Background/Secondary` fill, `Text/Primary` label.
  - Hover: `Background/Tertiary` fill [BOUND].
  - Focus: 2px `Button/Primary/Border/Focus` border + `Button/Focus` effect.
  - Selected: `Blue/50` fill, `Blue/500` label, check icon (`lucide:badge-check`, S4).
  - Disabled: `Text/Tertiary` label.
- **Tokens:** every one exists in R1: `blue-50`, `background-secondary`, `background-tertiary`, `text-primary`, `text-tertiary`, `effect-button-focus`, `button-primary-border-focus`, `radius-8`.

### 2.2 Dropdown / Menu (`dropdown.md` §2–§3)
- **Container:** padding 8, gap 8, `Radius/12`, 1px `Border/Primary`, `Background/Secondary`, clip, **no shadow** (D2).
- **Search region:** an Input Field / Outline instance (48, R8) with placeholder `Text/Secondary` (D6 differs from Input's own), then a 1px `Border/Secondary` divider and padding-bottom 8.
- **Options:** column, gap 4.
- **Footer:** padding-top 4, gap 12, divider, then an All Buttons Primary 40 with its label overridden to Label Small Medium 14/20 (D4).
- **Sizes (Desktop / Mobile):**
  - Item: 320 × 40 / 352 × 48.
  - Menu heights: 188 / 253 / 261 / 326 (Desktop) and 220 / 293 / 293 / 366 (Mobile).

### 2.3 Tooltip (`tooltip.md` §2–§3)
- **Body:** column, padding 10, raw radius 4 (TT3), max-width 300; Heading format gap 4.
- **Paint:** dark = `Base/Black` bg with `Base/White` text; light = the reverse. **No shadow or border** (TT1).
- **Typography:** text Body S-Semi 14/18 600; heading Body S-Semi; description Label XSmall Regular 12/17.
- **Arrow:** a polygon in a 20 × 20 box, rotated, offset outside the body (`left: −13px; top: 9px` for `left`).
- **Sizes:**
  - Text-only: 182 × 38 (Mobile), 157 × 38 (Desktop).
  - Heading: 260 × 62 (Mobile), 240 × 59 fixed (Desktop, TT5).

## 3. Missing specifications: R4 blockers

| # | Gap | Affects | Resolution route | Type |
|---|---|---|---|---|
| **B4-1** | **No Select trigger** in the file (closed field + chevron that opens the menu) | Select | Owner: design it in the file, or adopt the external "Design System › Select" (D-17, D-14) | **Owner decision, hard blocker for Select** |
| **B4-2** | **Dark theme**: Dropdown `Theme=Dark` resolves the same variables to Dark-mode values. R1 is Light-only (D-03); only 3 Dark values are known (`Background/Secondary #181b21`, `Text/Primary #fafcff`, `Border/Primary #171e2a`). Dark Hover / Focus / Selected are uninspected (D8). | Dropdown Dark (half the variants) | Owner: approve a V1 dark scope (D-23); then read-only inspection of the Dark variable mode | **Owner decision + inspection** |
| **B4-3** | **Behaviour unspecified** (TT6, D7, B-01): menu open/close, roving focus vs `aria-activedescendant`, typeahead, Escape/Tab handling, scroll/max-height, tooltip trigger, delay, dismiss and positioning/collision | Dropdown, Tooltip, Select | Engineering proposal based on WAI-ARIA APG (listbox / menu / tooltip patterns) for owner approval, like B-01 | **Owner approval of the behaviour spec** |
| B4-4 | Multiple-selection checkbox indicator (Item `Selection=Multiple`) not inspected: whether it reuses the R3 Checkbox (and its D-27 glyph gap) | Dropdown Item/Menu Multiple | Read-only inspection (~2 calls) | Inspection |
| B4-5 | Mobile paddings, Item 48 min-height, Mobile menu typography | Dropdown Mobile | Read-only inspection (~4 calls) | Inspection |
| B4-6 | Tooltip: Desktop Text-only padding/typography (why Mobile is wider, TT7); exact arrow geometry and offset for each of the 10 positions; arrow polygon shape (image-only, likely D-27-like) | Tooltip | Read-only inspection (~12 calls); the arrow shape may need owner geometry (CSS triangle approximation **not** allowed without approval) | Inspection, possibly owner |
| B4-7 | Selected check icon source is `lucide:badge-check` from the **Brainstorming/research page** (S4) | Dropdown Selected | Icon decision D-12/D-13; R4 ships an icon slot (as in R3) | Owner (non-blocking: slot) |
| B4-8 | Theme mechanisms differ: Dropdown `Theme=Light/Dark` + variable modes vs Tooltip `Mode=dark/light` + raw Base colours (D5, TT2) | API naming | Proposal: keep the Figma property names per component (traceability rule); document the inconsistency | Non-blocking |
| B4-9 | Light tooltip is invisible on light backgrounds (TT1); Menu has no elevation (D2) | Visual / a11y | Reproduce and flag (D-22-style decision) | Non-blocking (flag) |
| B4-10 | Desktop Heading tooltip has a fixed height of 59, so long text clips (TT5) | Tooltip | Reproduce and flag, or owner decision | Non-blocking (flag) |
| B4-11 | Empty, loading and group-header states and max-height/scroll are not designed (D7) | Dropdown | Owner, or out of scope for V1 | Non-blocking (documented absence) |
| **B4-12** | **Commit model with the footer "Apply selection"**: staged until Apply, or immediate? No Cancel button exists | Dropdown with footer | Owner decision (`r4-behaviour-spec.md` S7, R4-Q3) | **Owner decision, blocks Footer variants** |

## 4. Proposed architecture (after blockers resolve)

| Item | Proposal |
|---|---|
| Files | `src/components/dropdown/` (`dropdown.css`, `dropdown.js`, html, README), `src/components/tooltip/` (`tooltip.css`, `tooltip.js`), `src/components/select/` (only after B4-1) |
| Shared JS | `src/core/` utilities (roadmap R4): focus management (roving tabindex), outside-click/Escape dismissal, positioning (no library; CSS anchor positioning where supported with a JS fallback). Pure ES modules, no dependencies. |
| Semantics (B4-3 proposal) | Dropdown Menu as `role="listbox"` (Single → `aria-selected`; Multiple → `aria-multiselectable`) or `role="menu"` with `menuitemcheckbox`/`menuitemradio`, per the decided pattern; Tooltip with `role="tooltip"` + `aria-describedby`, shown on hover and focus, dismissed with Escape; Select as a button with `aria-haspopup="listbox"` and `aria-expanded` |
| Reuse | Search field = R3 Input Outline (48/R8) with the D6 placeholder override flagged; Footer = R3 Button Primary 40 with the D4 label override; Multiple indicator = R3 Checkbox (if B4-4 confirms) |
| Variant classes | Dropdown: `--single`/`--multiple`, `--desktop`/`--mobile`, `--light`/`--dark`, `--search`, `--footer-label`/`--footer-icon-label`; Tooltip: `--mobile`/`--desktop`, `--dark`/`--light`, `--arrow-<position>`, `--heading` |
| Validation | Per-variant fixtures (Item 40, Menu 48, Tooltip 80; Select per its set), mutation tests, CDP real-input audit (keyboard navigation, Escape, typeahead, hover/focus tooltip timing), accessibility tree, showcase over HTTP, full R1–R3 regression |

## 5. Readiness

| Part | Status |
|---|---|
| Dropdown Item + Menu, **Desktop Light** (Single and Multiple, Search, Footer) | **Ready after B4-3 (behaviour approval) and B4-4 (2 read-only calls)** |
| Dropdown Mobile Light | After B4-5 (read-only) |
| Dropdown Dark | **Blocked: B4-2** (dark scope decision D-23 + inspection) |
| Tooltip (all 80) | After B4-6 (read-only) and B4-3; the arrow shape may need owner geometry |
| Select | **Blocked: B4-1** (no component in the file; D-17 / D-14) |

**Estimated read-only inspection before coding:** about 20 calls (B4-4, B4-5, B4-6), plus the Dark-mode variable reads if B4-2 is approved.


---

## 6. Update after R4-0 (2026-11-20)

Approvals: R4-Q1, Q2, Q4, Q5, Q6, Q7. **Open:** R4-Q3 (B4-12) and R4-Q8. Details: `r4-behaviour-spec.md` §0 and §4.

| Blocker | Status after R4-0 | Evidence |
|---|---|---|
| B4-1 Select trigger | **BLOCKED** (unchanged) | — |
| B4-2 Dark theme | **BLOCKED** (unchanged). Recorded for later: Dark Item Selected = `Blue/500` fill + white label; Hover `#1f242e` | `r4-0-evidence.md` §1 |
| B4-3 Behaviour spec | ✅ **APPROVED** (Q1, Q2, Q4, Q5, Q6) | `r4-behaviour-spec.md` |
| B4-4 Multiple indicator | ✅ **RESOLVED**: an icon instance (research-page master), not the R3 Checkbox; colours `Icon/Secondary` / `Blue/500` / `Border/Primary` | `1454:7202`, `7212`, `7215` |
| B4-5 Mobile spacing | ✅ **RESOLVED**: Item padding 12 / min-height 48 / Body M 16/24; Mobile footer button 48 / Label Medium 16/21 | `1451:25415` |
| B4-6 Tooltip sizing and arrows | ✅ Desktop Text-only = Body XS Medium 12/18; all 10 arrow positions, offsets and transforms recorded; ⚠ the polygon shape is unknown, so the arrow glyph is BLOCKED | `1448:16825`, `1446:32`–`59`, `1448:88` |
| B4-7 Icon source | **BLOCKED** (now covers both the Single check and the Multiple indicator) | — |
| B4-12 Apply commit model | **BLOCKED** (R4-Q3) | — |

### 6.1 Implementation readiness

| Part | Variants covered | Ready |
|---|---|---|
| Dropdown Item, Light (Desktop + Mobile, Single + Multiple, 5 states) | 20 of 40 | ✅ (Dark 20 blocked) |
| Dropdown Menu, Light, Footer=None (Desktop + Mobile, Single + Multiple, Search Off/On) | 8 of 48 | ✅ |
| Dropdown Menu, Light, Footer=Label / Icon + label | 16 of 48 | ❌ R4-Q3 |
| Dropdown Menu, Dark | 24 of 48 | ❌ B4-2 |
| Tooltip (all) | 80 of 80 | ✅ (arrow glyph slot empty; G5 / G7 flagged) |
| Select | — | ❌ B4-1 |

**Ready for implementation on approval:** 20 Item + 8 Menu + 80 Tooltip = **108 variants**. **Blocked:** 20 Item + 40 Menu (Dark or Footer) and Select.


## 7. Implementation status (2026-11-20)

| Step | Status | Validation |
|---|---|---|
| R4-1 Dropdown (20 Item + 8 Menu, Light, Footer=None) | ✅ | visual 469 / 0 · real input 82 / 0 · showcase 15 / 0 · mutations 8 / 8 caught |
| R4-2 Tooltip (80) | ✅ | visual 1,441 / 0 · real input 39 / 0 · showcase 13 / 0 · mutations 8 / 8 caught |
| Blocked, not started | — | Footer Dropdown (R4-Q3), Dark (B4-2), Select (B4-1), arrow glyph (G12), icons (G8 / G9) |

Full report: `r4-completion-report.md`.
