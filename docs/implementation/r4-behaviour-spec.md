# R4 Behaviour Specification — Dropdown and Tooltip (DRAFT FOR APPROVAL)

| Item | Value |
|---|---|
| Implementation | **Implemented 2026-11-20** (R4-1 Dropdown, R4-2 Tooltip): see `r4-completion-report.md`. Implementation notes: TT-POS (12px gap derived from the arrow geometry), DD-1 (search focus border derived from the Input instance), live-region writes without animation frames, a new hover re-arms the tooltip after Escape (T5) |
| Status | **Specification only; no implementation code.** Approved 2026-11-20: R4-Q1, Q2, Q4, Q5, Q6, Q7. **Still open:** R4-Q3 (Apply commit model) and R4-Q8 (all design-owner items). Updated with the R4-0 read-only evidence (`docs/figma-audit/r4-0-evidence.md`, 13 calls). |
| Date | 2026-11-19 (draft) · 2026-11-20 (approvals + R4-0 evidence) |
| Inputs | `docs/implementation/r4-components-spec.md`; `docs/figma-audit/components/dropdown.md`, `tooltip.md`; `09-accessibility.md`; R1–R3 conventions (`r3-components-spec.md` §2, B-01); WAI-ARIA Authoring Practices Guide (APG) patterns: **Listbox**, **Combobox (select-only and with listbox popup)**, **Dialog (modal / non-modal)**, **Tooltip**; WCAG 2.2 SC 1.4.3, 1.4.11, **1.4.13 Content on Hover or Focus**, 2.1.1, 2.1.2, 2.4.3, 2.4.7, 4.1.2, 4.1.3 |
| Approval needed | Every **PROPOSED** item; every **BLOCKED** item needs a decision before it can be built |

## 0. Approval record (2026-11-20)

| Decision | Result |
|---|---|
| R4-Q1 Patterns (§1.1, §2) | **APPROVED** |
| R4-Q2 Disabled options: focusable by arrow keys, never selectable, disabled state exposed | **APPROVED** |
| R4-Q3 Apply commit model | **DECIDED 2026-11-20 (R6): staged commit.** The user's master mission asks for reasonable technical decisions; the label "Apply selection" implies the choice is not applied until pressed. Implemented and tested (`r6_dropdown_footer_cdp.py`) |
| R4-Q4 Timing: show 500 ms, hide 150 ms, keyboard focus immediate, typeahead 500 ms | **APPROVED** |
| R4-Q5 Touch (T3) | **APPROVED** |
| R4-Q6 Polite announcements (A8 a, b) | **APPROVED** (A8 c depends on the empty state, G1) |
| R4-Q7 Read-only inspections | **DONE**: `docs/figma-audit/r4-0-evidence.md` (13 calls) |
| R4-Q8 Design-owner items | **OPEN**; no approval assumed |

Items approved under Q1, Q2, Q4, Q5 and Q6 are **APPROVED behaviour**: they were PROPOSED and are now accepted. They remain *not Figma-confirmed*; the tag column shows `APPROVED (Qn)` to keep that distinction.

## 0.1 Classification

| Tag | Meaning |
|---|---|
| **CONFIRMED** | Directly supported by Figma evidence (a variant, property, binding, component description or measured value) |
| **PROPOSED** | Recommended accessible behaviour (APG / WCAG based) that the design does not specify; **requires approval** |
| **UNKNOWN** | Insufficient evidence; a read-only inspection could resolve it |
| **BLOCKED** | Requires a design-owner decision or missing design input; it cannot be built until resolved. *(Your message was cut off after "requires a"; this definition is assumed and can be corrected.)* |

**Important context:** Figma contains **no interaction or prototype data** for these components. B-01 / `09` §6 inspected no prototype connections, and the audit found no trigger component (D1). Every timing, keyboard, focus and announcement rule below is therefore **PROPOSED** unless it is marked otherwise. CONFIRMED items describe *what exists visually* (states, regions, properties), not how they behave.

### 0.2 Confirmed design facts used by this spec

| # | Fact | Evidence | Tag |
|---|---|---|---|
| F1 | Item states: Default, Hover, Focus, Selected, Disabled | Item set `1451:25092` property `State` | CONFIRMED |
| F2 | Selection model: `Selection = Single / Multiple` on both Menu and Item | properties | CONFIRMED |
| F3 | "Multiple rows may independently use State=Selected" | Item component description [EXTRACTED] | CONFIRMED |
| F4 | "Checkboxes and selection indicators sit left of option labels" | Menu description [EXTRACTED] | CONFIRMED |
| F5 | Menu has an optional **Search** region (Input Field / Outline, placeholder "Search teams") and optional **Footer** (`None`, `Label`, `Icon + label`) containing **one** Primary Button ("Apply selection") | Menu `1451:25250` [APPLIED] | CONFIRMED |
| F6 | "Responsive width and content-driven height" | Menu description | CONFIRMED (no max-height given) |
| F7 | Single Selected shows a check icon (`lucide:badge-check`, 20 × 20); Selected label `Blue/500`, fill `Blue/50` | Item `1451:25175` | CONFIRMED (visual) |
| F8 | Focus item: 2px `Button/Primary/Border/Focus` + `Button/Focus` effect | `1451:25074` | CONFIRMED (visual) |
| F9 | Disabled item: label `Text/Tertiary`, background unchanged | Item | CONFIRMED (visual) |
| F10 | **No** trigger (closed Select), **no** Cancel button, **no** Select-all / Clear control, **no** empty / loading / group-header / scroll state | absence across the Dropdown page (D1, D7) | CONFIRMED (absence) |
| F11 | Tooltip: 10 arrow positions, 2 formats, 2 modes, 2 devices; body max-width 300; no shadow or border | `1448:16825` | CONFIRMED |
| F12 | Tooltip content is static text (content, or heading + description); **no interactive content** | `tooltip.md` §3 | CONFIRMED |
| F13 | Mobile Item: padding 12, min-height 48, **Body M Regular 16/24**; Desktop Item: 12 / 10, min-height 40, Label Small 14/20 | `r4-0-evidence.md` §1 (`1451:25082`, `1451:25072`) | CONFIRMED |
| F14 | Multiple indicator = icon instance "checkbox" (research-page master), colours `Icon/Secondary` / `Blue/500` / `Border/Primary` | `r4-0-evidence.md` §2 (`1454:7202`, `7212`, `7215`) | CONFIRMED |
| F15 | Tooltip arrow: 10 positions with exact offsets and transforms; `regular-polygon` filled with the body colour; text wraps within max-width 300; heading variants have a fixed size (Mobile 260 × 62, Desktop 240 × 59) | `r4-0-evidence.md` §4 | CONFIRMED |
| F16 | Desktop Text-only tooltip uses Body XS Medium 12/18 | `1446:34` | CONFIRMED |

---

## 1. Dropdown

Scope: **Desktop, Light**. The four configurations below come from the Menu properties `Selection × Search × Footer` (F2, F5).

| Config | Menu properties |
|---|---|
| D-S | Selection=Single, Search=Off, Footer=None |
| D-M | Selection=Multiple, Search=Off, Footer=None |
| D-SR | Search=On (Single or Multiple) |
| D-F | Footer=Label or Icon + label (Single or Multiple; with or without Search) |

Mobile and Dark are **out of scope** for this draft (Mobile: UNKNOWN, B4-5; Dark: BLOCKED, B4-2).

### 1.1 Pattern selection (PROPOSED)

| Config | APG pattern | Rationale |
|---|---|---|
| D-S, D-M (no search, no footer) | **Select-only combobox** (trigger `role="combobox"`) controlling a **listbox** popup (`role="listbox"`; `aria-multiselectable="true"` for Multiple) | The popup contains only options; this is the APG recommendation for single- and multi-select pickers |
| D-SR (search, no footer) | **Combobox with listbox popup**: the search field inside the popup is the `role="combobox"` input (`aria-autocomplete="list"`, `aria-controls` → listbox, `aria-activedescendant` → active option); the trigger is a button with `aria-haspopup="dialog"` | Keeps DOM focus in the text field while the arrow keys move through options |
| D-F (footer present) | **Non-modal dialog popup** (`role="dialog"`, `aria-modal="false"`, labelled by the trigger) containing [search combobox] + listbox + footer button | The popup holds several interactive elements (listbox + button), so APG recommends a dialog popup |

Alternative considered: `role="menu"` with `menuitemcheckbox` / `menuitemradio`. **Not proposed**, because the design is a value picker ("Selection", "Apply selection"), not an action menu.

### 1.2 Trigger

| Behaviour | Spec | Tag |
|---|---|---|
| Trigger component | No Select / trigger exists in Figma | **BLOCKED** (B4-1, D-17) |
| Interim API (until B4-1) | The menu is opened by a consumer-supplied trigger, for example an R3 Button, carrying `aria-haspopup="listbox"` (or `"dialog"` for D-SR / D-F), `aria-expanded`, `aria-controls`. Its visual design is **not** specified by R4. | PROPOSED |
| Trigger name | The visible label of the trigger. If it shows the current value, the name = field label and the value is exposed via the combobox value (select-only combobox) | PROPOSED |

### 1.3 Opening and closing

| # | Behaviour | Spec | Tag |
|---|---|---|---|
| O1 | Activate trigger | Click, Enter, Space or Alt+ArrowDown open the popup. ArrowDown and ArrowUp also open it (select-only combobox): ArrowDown → first / selected option active, ArrowUp → last / selected option active | APPROVED (Q1) |
| O2 | Initial active item on open | D-S / D-M: the selected option (first selected for Multiple); if none is selected, the first **enabled** option. D-SR / D-F with search: focus goes to the **search field** and no option is active until an arrow key is pressed | PROPOSED |
| O3 | Toggle | Activating the trigger while it is open closes the popup | PROPOSED |
| O4 | Outside click | Closes the popup. D-S / D-M: selection made so far is kept (immediate commit). D-F: see S7 (commit model) | PROPOSED; D-F part **BLOCKED** |
| O5 | Escape | Closes the popup and returns focus to the trigger. D-SR: if the search field has text, the **first** Escape clears the text and the second closes (APG combobox) | PROPOSED |
| O6 | Tab / Shift+Tab out of the popup | D-S / D-M: Tab closes the popup; focus continues to the next element after the trigger (select-only combobox; focus never leaves the trigger). D-SR / D-F: see K-Tab | PROPOSED |
| O7 | Focus restoration | On any close that the user initiated inside the popup (Escape, single selection, Apply), focus returns to the trigger. On outside click, focus goes where the user clicked | PROPOSED |
| O8 | Reopening | Reopening resets search text, shows all options and makes the current selection active (O2) | PROPOSED |
| O9 | Close after single selection | D-S: selecting an option commits it and closes the popup (focus → trigger) | PROPOSED |
| O10 | Multiple selection stays open | D-M: toggling an option does **not** close the popup | PROPOSED (consistent with F3) |
| O11 | Disabled trigger | Native `disabled` (or `aria-disabled="true"` when it must stay discoverable): it cannot open and gets no hover/press styling. **The visual disabled trigger is BLOCKED (B4-1)** | PROPOSED / BLOCKED |
| O12 | Popup position | Below the trigger; flips above if there is no space. Width: "responsive" (F6), proposed min = trigger width, max = the documented 320 (Desktop) | Placement PROPOSED; widths 320 CONFIRMED [META] |
| O13 | Scroll when there are many options | No max-height or scroll state is designed (F10) | **BLOCKED** (B4-11) |

### 1.4 Keyboard navigation

DOM focus stays on the trigger (D-S / D-M) or the search field (D-SR). The active option is tracked with `aria-activedescendant` and shown with the **Figma Item Focus visual** (F8). The Figma Item **Hover** visual (F1) is applied only to the pointer-hovered option.

| Key | Spec | Tag |
|---|---|---|
| ArrowDown / ArrowUp | Move the active option to the next / previous option. **No wrap** (APG default). Disabled options: see S5 | PROPOSED |
| Home / End | First / last option. In D-SR, Home / End move the **text caret** in the search field (APG editable combobox); Ctrl+Home / Ctrl+End move to the first / last option | PROPOSED |
| Enter | D-S: select the active option and close. D-M: toggle the active option (stays open). D-SR: as above for the active option; with no active option, Enter does nothing | PROPOSED |
| Space | D-S / D-M (no search): same as Enter for D-S; toggles in D-M. D-SR: Space types a space into the search field (it does **not** select) | PROPOSED |
| Escape | O5 | PROPOSED |
| Tab / Shift+Tab (K-Tab) | D-S / D-M: O6. D-SR without footer: Tab closes and moves on (non-modal combobox). D-F: the focus order inside the dialog is search field → listbox (focusable as one stop; arrow keys inside) → footer button; Tab from the footer button closes the popup and moves to the element after the trigger; Shift+Tab from the search field returns to the trigger and closes. **No focus trap** (non-modal) | PROPOSED |
| Typeahead | D-S / D-M without search: printable characters move the active option to the next option whose label starts with the typed string (500 ms accumulation; repeated same letter cycles). D-SR: typing goes to the search field (there is no typeahead) | APPROVED (Q1, Q4: 500 ms) |
| Search field | D-SR: filters options as the user types (case-insensitive substring match on the label). The active option resets to none after each change; ArrowDown moves into the filtered results. The field keeps all standard text-editing keys. It reuses the **R3 Input Outline 48 / R8** (CONFIRMED visual), with the D6 placeholder colour `Text/Secondary` reproduced and flagged | Filtering rule PROPOSED; field visual CONFIRMED |
| PageUp / PageDown | Optional: move by 10 options | PROPOSED (low priority) |

### 1.5 Selection

| # | Behaviour | Spec | Tag |
|---|---|---|---|
| S1 | Single selection | Exactly 0 or 1 selected option; selecting another replaces it. `aria-selected="true"` on the selected option only | Single model CONFIRMED (F2); semantics PROPOSED |
| S2 | Multiple selection | Any number of options can be selected independently (F3). Each option has `aria-selected="true/false"`; the listbox has `aria-multiselectable="true"` | CONFIRMED (F3); semantics PROPOSED |
| S3 | Selected indication (Single) | Item State=Selected: `Blue/50` fill, `Blue/500` label, check icon 20 × 20 at the left (F7). The icon is an **R3-style empty slot** until the icon source is decided | Visual CONFIRMED; icon **BLOCKED** (B4-7, D-12/D-13) |
| S4 | Selected indication (Multiple) | A 20 × 20 **icon instance "checkbox"** left of the label, **not** the R3 Checkbox (F14). Colour by state: Default / Hover / Focus `Icon/Secondary` `#555d6d`; Selected `Blue/500`; Disabled `Border/Primary`. The vector geometry is image-only and the master is on the research page, so it ships as an **icon slot with state colour** (like S3). The R3 D-27 glyph gap does **not** carry over | Visual and colours **CONFIRMED**; icon asset **BLOCKED** (G8, D-12/D-13) |
| S5 | Disabled options | Item State=Disabled visual (F9). `aria-disabled="true"`; it can never be selected. Disabled options **can become the active option** with arrow keys (discoverable), but Enter / Space / click do nothing | Visual CONFIRMED; navigation **APPROVED (Q2)** |
| S6 | Select all / Clear | **Not in the design** (F10). Not implemented. Ctrl+A for select-all is **not** proposed | CONFIRMED absence |
| S7 | Commit model with footer ("Apply selection") | Is the selection **staged** until Apply (and discarded on Escape or outside click), or applied immediately with Apply just closing? The design shows only the button | **BLOCKED** (new B4-12) |
| S8 | Apply action | Activating the footer button commits per S7, closes, returns focus to the trigger and fires a `change` event | PROPOSED (depends on S7) |
| S9 | Cancel action | **No Cancel button in the design** (F10). Proposed: Escape = cancel (when staged per S7). No visual Cancel is added | Absence CONFIRMED; Escape-as-cancel PROPOSED |
| S10 | Footer "Icon + label" | Same behaviour as Label; the icon is decorative (`aria-hidden`), name = label text | PROPOSED |
| S11 | Pointer | Clicking an enabled option = Enter (S1 / S2). Hovering applies the Item Hover visual (F1) and **does not** move `aria-activedescendant` (it avoids a screen-reader jump) | Hover visual CONFIRMED; rule PROPOSED |
| S12 | Change event | Custom `annachy-change` event (detail: selected values) on commit. Single: on selection. Multiple: on each toggle (immediate model) or on Apply (staged model) | PROPOSED |

### 1.6 Accessibility

| # | Item | Spec | Tag |
|---|---|---|---|
| A1 | Structure | §1.1 roles. Each option is `role="option"` with the label text as its accessible name; the indicator icon / checkbox is `aria-hidden="true"` (state is conveyed by `aria-selected`) | PROPOSED |
| A2 | Accessible name | Listbox: `aria-labelledby` → trigger label (or field label). Dialog (D-F): `aria-labelledby` → trigger. Search combobox: an accessible name is required. The Figma placeholder "Search teams" is **not** a name; propose a visually hidden label "Search" or a consumer-provided label | PROPOSED |
| A3 | Description | Optional `aria-describedby` on the trigger for helper text (uses the R3 Input sub-text pattern when the trigger becomes a field) | PROPOSED |
| A4 | Expanded state | `aria-expanded="true/false"` on the trigger (and on the search combobox in D-SR) | PROPOSED |
| A5 | Selected state | `aria-selected` per option (S1 / S2). With `aria-multiselectable`, unselected options carry `aria-selected="false"` explicitly | PROPOSED |
| A6 | Active option | `aria-activedescendant` on the focused element (trigger or search field) → `id` of the active option; it is cleared when there is no active option | PROPOSED |
| A7 | Focus visibility | The active option shows the Figma Item Focus visual (2px `#003fbc` + `Button/Focus`), so the indicator is CONFIRMED visually. Contrast of `#003fbc` against `Background/Secondary` `#f6f7f9` = 8.04:1 (`09` A19 pair) | Visual CONFIRMED |
| A8 | Announcements | Rely on native combobox / listbox announcements. Proposed `aria-live="polite"` status text: (a) D-SR result count after filtering ("5 results", debounced 500 ms); (b) D-M selection count on toggle ("3 selected"); (c) "No results" when the filter is empty (requires the empty state, G1). Text must be localisable | (a)(b) **APPROVED (Q6)**; (c) BLOCKED (G1) |
| A9 | Multiple-selection state on the trigger | The trigger value text summarises the selection (for example "3 selected" or a comma list). The format is **not in the design** | **BLOCKED** (B4-1: no trigger design) |
| A10 | Disabled options | `aria-disabled="true"` (S5) | PROPOSED |
| A11 | Contrast | Selected label `#004feb` on `#f3f7ff`: computed when implemented. Disabled label `#707a8f` on `#f6f7f9` is exempt (disabled). The Menu has no shadow (D2): its boundary relies on the 1px `#bfc4cf` border, whose contrast against the page needs measuring (non-text 3:1) | UNKNOWN (measure at implementation) |
| A12 | Reduced motion | No animation is designed, so **none is added** | CONFIRMED (absence) |

---

## 2. Tooltip

Pattern: **APG Tooltip** (`role="tooltip"`; the trigger references it with `aria-describedby`) plus **WCAG 1.4.13** (dismissible, hoverable, persistent). Tooltip content is **non-interactive** (F12). No links or buttons are allowed inside, and keyboard focus never enters the tooltip.

| # | Behaviour | Spec | Tag |
|---|---|---|---|
| T1 | Hover trigger | Pointer enters the trigger: show after the show delay. Pointer leaves: hide after the hide delay unless the pointer has moved onto the tooltip (T6) | PROPOSED |
| T2 | Keyboard focus trigger | Trigger receives **keyboard** focus (`:focus-visible`): show immediately (no delay). Blur: hide immediately | PROPOSED |
| T3 | Touch | No hover on touch. Proposed: the tooltip shows when a tap **focuses** the trigger and hides on the next tap outside, on blur or on Escape. A tap that activates the trigger's own action (for example a button) is not intercepted. **Rule:** tooltip content must never be essential to completing a task | **APPROVED (Q5)** |
| T4 | Show / hide delays | Proposed show delay **500 ms** after hover; hide delay **150 ms** after pointer leave (allows T6); 0 ms for keyboard focus. While one tooltip is open, moving to another trigger shows the next one immediately ("warm-up" group behaviour) | Values **APPROVED (Q4)**: show 500 ms, hide 150 ms, keyboard focus immediate |
| T5 | Escape dismissal | Escape hides the visible tooltip **without moving focus** and without closing an enclosing popup (it stops propagation only when a tooltip was open). It reappears on the next hover or focus | PROPOSED (WCAG 1.4.13 "dismissible") |
| T6 | Pointer moving onto the tooltip | The tooltip stays open while the pointer is over the trigger **or** the tooltip, including the gap and arrow area (a hover bridge across the arrow offset). It stays visible until the pointer leaves both, focus leaves, or Escape is pressed (WCAG 1.4.13 "hoverable", "persistent") | PROPOSED |
| T7 | Positioning | Placement = the Figma `Arrow` property, read as **arrow side → tooltip placed on the opposite side of the trigger**. For example, `Arrow=left` means the tooltip sits to the right of the trigger with the arrow pointing left at it. **Confirmed by all 10 positions** (`r4-0-evidence.md` §4.2): `left` / `right` arrows sit 9px from the body top, `* center` variants are centred, `top left` / `bottom left` 12px from the left edge, `* right` 12px from the right | Mapping and offsets **CONFIRMED**; alignment to the trigger **APPROVED (Q1)** |
| T8 | Viewport collision | If the preferred placement overflows the viewport, **flip** to the opposite placement that exists among the 10 Figma positions; if that also overflows, try the remaining sides in order (top → bottom → right → left). **The tooltip body is not shifted** away from a documented arrow offset; only the 10 measured placements are used (same side with the other anchor first, e.g. `top` → `top left` / `top right`, then the opposite side, then the remaining sides; if none fits, keep the preferred one) | **APPROVED (Q1)**; offsets CONFIRMED |
| T9 | Arrow positioning | The arrow is a 20 × 20 box positioned outside the body. Exact offsets and transforms for all 10 positions in `r4-0-evidence.md` §4.2 (the ±0.5 / 1px centring differences are reproduced). Fill = body colour. Visible polygon bounds: insets top 5%, left / right 10.35%, bottom 25% (15.86 × 14) | Positions and bounds **CONFIRMED**; **polygon shape (point count, corner rounding) UNKNOWN**, so the **arrow glyph is BLOCKED**: it ships as an empty, correctly positioned slot (no CSS-triangle approximation without approval) |
| T10 | Long text | Body `max-width: 300` (CONFIRMED). Text wraps inside 300 (`width: min-content; min-width: 100%`, break-word) with no line limit. Heading format: **fixed size in all 40 heading variants**: Desktop 240 × 59, **Mobile 260 × 62**, so longer text clips (TT5, both devices) | Wrapping **CONFIRMED**; heading clipping **BLOCKED** (G7: reproduce and flag) |
| T11 | Accessible relationship | The trigger has `aria-describedby` → the tooltip `id`; the tooltip has `role="tooltip"`. The tooltip element stays in the DOM (hidden with `hidden` / `display: none` when not shown) so the description is available even when it isn't visible. Heading format: the description string is heading + description text | PROPOSED |
| T12 | Tooltip as the only label | For icon-only triggers, the accessible **name** must come from `aria-label` on the trigger (the R3 Button rule), **not** from the tooltip. The tooltip remains a description. Avoid duplicating the same text in both name and description | PROPOSED |
| T13 | Disabled controls | Native `disabled` buttons do not receive focus and do not fire pointer events reliably, so a tooltip on them is neither keyboard- nor pointer-accessible. Proposed: controls that need a tooltip while disabled use `aria-disabled="true"` (they stay focusable; the consumer guards activation, see R3 BTN-3), or the tooltip is attached to a focusable wrapper. A tooltip must not be the only explanation of why a control is disabled unless it is reachable by keyboard | PROPOSED |
| T14 | Content | Static text only (F12). No interactive content, no rich formatting beyond heading + description | CONFIRMED |
| T15 | Modes and devices | `Mode=dark/light` and `Device=Mobile/Desktop` are visual variants; behaviour is identical. Choice of device variant: proposed by viewport class (no breakpoint exists, D-07), so it is **BLOCKED** for automatic switching. The consumer selects the variant explicitly | Visual CONFIRMED; automatic switching BLOCKED (D-07) |
| T16 | Animation | None in the design, so none is added (instant show and hide after the delays) | CONFIRMED (absence) |
| T17 | One tooltip at a time | Showing a tooltip hides any other open tooltip | PROPOSED |

---

## 3. Missing behaviour and design gaps

| # | Gap | Evidence | Tag | Needed |
|---|---|---|---|---|
| G1 | **Empty state** ("No results" after search; no options) | D7 / F10 | **BLOCKED** | Owner design (visual), or approval to render nothing and announce "No results" only (A8c) |
| G2 | **Loading state** (async options) | D7 | **BLOCKED** | Owner design, or out of V1 scope |
| G3 | **Scroll / max-height** for long lists | D7, F6 ("content-driven height") | **BLOCKED** | Owner max-height and scroll indicator; without it the menu grows unbounded |
| G4 | **Group headers / separators** | D7 | BLOCKED (out of V1 unless designed) | Owner |
| G5 | **Light tooltip invisible on light backgrounds** (`#fafcff` body, no shadow or border) | TT1 / `tooltip.md` §3 | **BLOCKED** (a11y, 1.4.11) | Owner: add border or shadow, or restrict Light mode to dark surfaces. Until then it is reproduced and flagged |
| G6 | **Dropdown Menu has no shadow** (border only) | D2 | **BLOCKED** (visual decision) | Owner: elevation token, or accept border-only. Reproduced as designed |
| G7 | **Desktop heading tooltip fixed height 59**, so text clips | TT5 | **BLOCKED** | Owner: auto height, or a documented max text length |
| G8 | **Selected check icon from the research page** (`lucide:badge-check`, Brainstorming S4) | `11` §2, B4-7 | **BLOCKED** (icon source D-12/D-13) | Owner icon decision; an empty 20 × 20 slot is used meanwhile |
| G9 | **Multiple-selection indicator** | D8, B4-4 | ✅ **RESOLVED** (`r4-0-evidence.md` §2): an icon instance (research-page master) with bound state colours; not the R3 Checkbox | The icon asset joins G8 |
| G10 | **Mobile spacing** | D8, B4-5 | ✅ **RESOLVED** (§1, §3.1): Item padding 12, min-height 48, Body M 16/24; Menu as Desktop; search placeholder Body M; footer button 48 / Label Medium 16/21 | — |
| G11 | **Tooltip Desktop Text-only sizing** | TT7 | ✅ **RESOLVED**: Desktop Body XS Medium 12/18 (`1446:34`) vs Mobile Body S-Semi 14/18; padding 10 in both | — |
| G12 | **Tooltip arrow positions and shape** | `r4-0-evidence.md` §4.2 | ✅ Positions, offsets, transforms and bounds **RESOLVED**; ⚠ **polygon shape UNKNOWN**, so the **arrow glyph is BLOCKED** | Owner geometry, or approval of read-only SVG export |
| G13 | **Select trigger** (closed field) | D1, B4-1 | **BLOCKED** | Owner: design in the file or adopt the external Select (D-17 / D-14) |
| G14 | **Commit model with Apply** (staged vs immediate), **no Cancel** | F5, F10 | **BLOCKED** (new B4-12) | Owner decision |
| G15 | **Dark theme** (Dropdown `Theme=Dark`) | B4-2, D-23 | **BLOCKED** | Owner scope decision + inspection |
| G16 | **Error / invalid state** for Dropdown (required field) | `07` X3 | BLOCKED (not designed) | Owner |
| G17 | **Menu border contrast** against the page (no shadow) | A11 | **UNKNOWN** | Measure at implementation |
| G18 | **Delays, typeahead timeout, live-region wording** | — | ✅ Values APPROVED (Q4, Q6); wording must be localisable | — |
| G19 | **Mobile footer button**: 48 tall, px 16 / py 18, `Radius/12`, label Label Medium 16/21 (= Button size 48 with a typography override, like D4) | `1451:24359` | CONFIRMED (reproduced as an override) | — |

---

## 4. Decision status and readiness (2026-11-20)

| # | Decision | Status |
|---|---|---|
| R4-Q1, Q2, Q4, Q5, Q6 | Patterns, disabled options, timing, touch, announcements | **APPROVED** |
| R4-Q7 | Inspections | **DONE** (`r4-0-evidence.md`) |
| R4-Q3 | Apply commit model | **DECIDED (R6): staged; D-F implemented** |
| R4-Q8 | Design-owner items: Select (G13), Dark (G15), empty / loading / scroll (G1–G3), group headers (G4), Light tooltip visibility (G5), Menu shadow (G6), heading clipping (G7), icon source (G8, including the G9 indicator), tooltip arrow shape (G12), error state (G16) | **OPEN**; no approval assumed |

| Part | Implementation-ready? | Shipped limitations (flagged, not invented) |
|---|---|---|
| Dropdown Item + Menu, Desktop Light, **D-S** (Single) | ✅ Ready | Empty check-icon slot (G8); no empty / loading / scroll (G1–G3); no shadow (G6); consumer-supplied trigger (G13) |
| Dropdown, Desktop Light, **D-M** (Multiple) | ✅ Ready | Empty indicator slot with state colours (G8/G9); as above |
| Dropdown, Desktop Light, **D-SR** (Search) | ✅ Ready | "No results" announcement waits on G1 (A8c); D6 placeholder colour reproduced |
| Dropdown Mobile Light (visual variants) | ✅ Ready (visuals) | Same behaviour as Desktop; variant chosen by a consumer class (no breakpoints, D-07) |
| Dropdown **with Footer** (D-F) | ❌ BLOCKED | R4-Q3 |
| Dropdown Dark | ❌ BLOCKED | G15 / B4-2 |
| Tooltip, all 80 variants (body, typography, sizes, positions, behaviour) | ✅ Ready | **Arrow glyph empty** (G12); Light-mode visibility (G5) and heading clipping (G7) reproduced and flagged |
| Select | ❌ BLOCKED | G13 |
