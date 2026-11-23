# 09 — Accessibility Observations

| Item | Value |
|---|---|
| Basis | Evidence already collected in `02`–`07`, `11`, `components/*.md`. **No new Figma access.** |
| Standard | WCAG 2.2 Level AA — 1.4.1 Use of Colour, 1.4.3 Contrast (Minimum), 1.4.4 Resize Text, 1.4.11 Non-text Contrast, 2.4.7 Focus Visible, 2.5.8 Target Size (Minimum) |
| Method | Contrast ratios computed with the WCAG relative-luminance formula **only where both colours are explicitly recorded** for the same element and state. |
| Scope limit | Figma data contains no behaviour. Keyboard interaction, focus order, ARIA roles/names, screen-reader output, motion and zoom behaviour are **[UNVERIFIED]** for every component. |

Tags: **[COMPUTED]** ratio from recorded hex values · **[EXTRACTED]** observed in Figma data · **[UNVERIFIED]** no evidence · **[MISSING]** state/spec absent.

---

## 1. Contrast — explicit colour pairs [COMPUTED]

Thresholds: text 4.5:1 (normal) / 3:1 (large ≥ 24 px regular or ≥ 18.66 px bold); non-text UI 3:1. Disabled controls are exempt under WCAG and listed for information only.

| ID | Component | Element | Foreground | Background | Ratio | AA normal text (4.5) | AA large text (3.0) / non-text (3.0) | Source |
|---|---|---|---|---|---:|---|---|---|
| A01 | Button Primary | label Default | `#fafcff` | `#004feb` | 6.16:1 | Pass | Pass | button.md §1.4 |
| A02 | Button Primary | label Hover | `#fafcff` | `#003fbc` | 8.38:1 | Pass | Pass | button.md §1.4 |
| A03 | Button Primary | label Focus | `#fafcff` | `#004feb` | 6.16:1 | Pass | Pass | button.md §1.4 |
| A04 | Button Primary | label Pressed | `#fafcff` | `#3372ef` | 4.26:1 | **Fail** | Pass | button.md §1.4 |
| A05 | Button Primary | label Disabled | `#fafcff` | `#bfc4cf` | 1.70:1 | exempt (disabled) | exempt | button.md §1.4 |
| A06 | Button Secondary | label Hover | `#004feb` | `#f3f7ff` | 5.89:1 | Pass | Pass | button.md §1.4 |
| A07 | Button Secondary | label Pressed | `#004feb` | `#e8f0ff` | 5.53:1 | Pass | Pass | button.md §1.4 |
| A08 | Button Secondary Grey | label Hover | `#1f242e` | `#f6f7f9` | 14.51:1 | Pass | Pass | button.md §1.4 |
| A09 | Button Secondary Grey | label Pressed | `#1f242e` | `#dcdfe5` | 11.65:1 | Pass | Pass | button.md §1.4 |
| A10 | Button Tertiary | label Hover | `#004feb` | `#f3f7ff` | 5.89:1 | Pass | Pass | button.md §1.4 |
| A11 | Button Tertiary | label Pressed | `#003fbc` | `#e8f0ff` | 7.52:1 | Pass | Pass | button.md §1.4 |
| A12 | Button Tertiary Grey | label Hover | `#1f242e` | `#f3f4f7` | 14.14:1 | Pass | Pass | button.md §1.4 |
| A13 | Button Tertiary Grey | label Pressed | `#1f242e` | `#e4e7ec` | 12.55:1 | Pass | Pass | button.md §1.4 |
| A14 | Button (gradient) | label vs gradient start | `#fafcff` | `#3a79f7` | 3.89:1 | **Fail** | Pass | button.md §2 |
| A15 | Button (gradient) | label vs gradient end | `#fafcff` | `#1746a2` | 8.39:1 | Pass | Pass | button.md §2 |
| A16 | Input / Filled | placeholder Default | `#dcdfe5` | `#f6f7f9` | 1.25:1 | **Fail** | **Fail** | input.md §3.2 |
| A17 | Input / Filled | value Focused | `#1f242e` | `#f6f7f9` | 14.51:1 | Pass | Pass | input.md §3.2 |
| A18 | Input / Filled | field border Default vs field fill | `#edeff2` | `#f6f7f9` | 1.07:1 | n/a | **Fail** | input.md §3.2 |
| A19 | Input / Filled | field border Focused vs field fill | `#003fbc` | `#f6f7f9` | 8.04:1 | n/a | Pass | input.md §3.2 |
| A20 | Dropdown Item | label Default | `#0b0c0f` | `#f6f7f9` | 18.25:1 | Pass | Pass | dropdown.md §4 |
| A21 | Dropdown Item | label Hover | `#0b0c0f` | `#edeff2` | 16.98:1 | Pass | Pass | dropdown.md §4 |
| A22 | Dropdown Item | label Selected | `#004feb` | `#f3f7ff` | 5.89:1 | Pass | Pass | dropdown.md §4 |
| A23 | Dropdown Item | label Disabled | `#707a8f` | `#f6f7f9` | 4.02:1 | exempt (disabled) | exempt | dropdown.md §4 |
| A24 | Dropdown Item | Focus border vs item fill | `#003fbc` | `#f6f7f9` | 8.04:1 | n/a | Pass | dropdown.md §4 |
| A25 | Dropdown Menu | search placeholder vs menu fill | `#555d6d` | `#f6f7f9` | 6.17:1 | Pass | Pass | dropdown.md §3 |
| A26 | Dropdown Menu | border vs menu fill | `#bfc4cf` | `#f6f7f9` | 1.63:1 | n/a | **Fail** | dropdown.md §3 |
| A27 | Dropdown (Dark) | label Default | `#fafcff` | `#181b21` | 16.78:1 | Pass | Pass | dropdown.md §5 |
| A28 | Dropdown (Dark) | label Disabled | `#707a8f` | `#181b21` | 4.00:1 | exempt (disabled) | exempt | dropdown.md §5 |
| A29 | Checkbox/Radio | Unchecked border vs box fill | `#e1e1e2` | `#ffffff` | 1.31:1 | n/a | **Fail** | checkbox.md §4 |
| A30 | Checkbox | Disabled On icon vs box | `#fafcff` | `#bfc4cf` | 1.70:1 | exempt (disabled) | exempt | checkbox.md §4 |
| A31 | Checkbox/Radio | Focus border vs box fill | `#004feb` | `#ebf2ff` | 5.63:1 | n/a | Pass | checkbox.md §4 |
| A32 | Toggle | thumb vs track On | `#fafcff` | `#004feb` | 6.16:1 | n/a | Pass | toggle.md §3 |
| A33 | Toggle | thumb vs track Hover On | `#fafcff` | `#003fbc` | 8.38:1 | n/a | Pass | toggle.md §3 |
| A34 | Toggle | thumb vs track Pressed On | `#fafcff` | `#3372ef` | 4.26:1 | n/a | Pass | toggle.md §3 |
| A35 | Toggle | Disabled On track vs Disabled Off track | `#edeff2` | `#f6f7f9` | 1.07:1 | n/a | informational (state distinguishability) | toggle.md §3 |
| A36 | Tooltip (dark) | text | `#fafcff` | `#0b0c0f` | 19.03:1 | Pass | Pass | tooltip.md §3 |
| A37 | Tooltip (light) | text | `#0b0c0f` | `#fafcff` | 19.03:1 | Pass | Pass | tooltip.md §3 |
| A40 | Tooltip (light) | body `#fafcff` vs light page `#fafcff` (no border / shadow) | `#fafcff` | `#fafcff` | **1.00:1** | n/a | **Fail** (1.4.11) | TT1 / G5; R4-2, *added 2026-11-20* |
| A41 | Dropdown Menu | boundary vs page: border `#bfc4cf` / fill `#f6f7f9` on `#fafcff` (no shadow, D2) | `#bfc4cf` | `#fafcff` | **1.70:1** (border), 1.04:1 (fill) | n/a | **Fail** (1.4.11, 3:1) | D2 / G6; R4-1, *added 2026-11-20* |
| A39 | Toggle | Off track vs page `Background/Primary`; thumb vs Off track | `#f6f7f9` | `#fafcff` | **1.04:1** | n/a | **Fail** (1.4.11 non-text, 3:1) | `r3-0-evidence.md` §26 — *added 2026-11-19 (R3-6); the Off track fill is derived (TG-1)* |
| A38 | Input / Filled | placeholder Hover | `#98a0ae` | `#f6f7f9` | **2.46:1** | **Fail** | **Fail** | `r3-0-evidence.md` §23.4 (`1066:43333`, `1066:43486`) — *added 2026-11-19 (R3-3); confirmed in the browser and by independent calculation (2.4566)* |

Additional pair: **Button Primary focus border `#003fbc` vs its fill `#004feb` = 1.36:1** [COMPUTED].

### 1.1 Interpretation notes

- **Text size:** Button labels are 12–20 px Semibold (600). They are treated as *normal* text (4.5:1) because all are < 24 px and weight 600 is below the usual bold threshold. **A04** (Primary Pressed, 4.26:1) and **A14** (gradient button label over the light end of the gradient, 3.89:1) therefore **fail** AA normal text; they would pass only as large text.
- **A14/A15:** the gradient runs 22.57° from `#3a79f7` to `#1746a2`; contrast under the label depends on label position. Worst case reported.
- **A18, A26, A29** compare a border with its *own* fill. WCAG 1.4.11 requires contrast against the **adjacent page colour**, which the components do not define → these rows are **indicative only**.
- **A16** — Filled input placeholder 1.25:1 fails by any measure. The Outline input uses the same placeholder `#dcdfe5` on a **transparent** field; its ratio depends on the page background.
- **A35** — Toggle Disabled On vs Disabled Off differ by 1.07:1: the two disabled states are indistinguishable by colour (1.4.1 concern; disabled controls are otherwise exempt).

### 1.2 Pairs not computable (background not defined in the component)

| Component / element | Foreground(s) | Reason |
|---|---|---|
| Button Secondary / Tertiary / Link labels (Default, Focus, Disabled) | `#004feb`, `#1f242e`, `#bfc4cf` | Transparent background |
| Input / Outline: label, description, value, placeholder, sub-text, error, success | `#272b35`, `#3d4451`, `#1f242e`, `#dcdfe5`, `#707a8f`, `#e72b23`, `#276732` | No fill |
| Checkbox / Radio / Toggle labels and subtext | `#0b0c0f`, `#707a8f`, disabled `#dcdfe5` | No fill |
| Checked checkbox / selected radio vs page | `#004feb` | Page background undefined |
| Light tooltip body vs page | `#fafcff` | Page background undefined |
| Icon semantic colours (`error #e72b23`, `success #276732`, `warning #b9512e`, `disabled #bfc4cf`) | — | Usage backgrounds undefined |

---

## 2. State coverage — hover · focus · error · disabled [EXTRACTED]

| Component | Hover | Focus | Error | Disabled | Notes |
|---|---|---|---|---|---|
| Button (All Buttons) | ✓ — **Link Hover identical to Default** | ✓ | n/a | ✓ | Loading state has no label → accessible name **[UNVERIFIED]** |
| Button (gradient) | ✓ | ✓ | n/a | ✓ | No Loading |
| Input / Outline | **✗ [MISSING]** | ✓ — 1 px colour change only | ✓ | ✓ | Success ✓ |
| Input / Filled | ✓ | ✓ — 1 px colour change only | ✓ | ✓ | |
| Dropdown / Item | ✓ | ✓ — 2 px border + glow | **✗ [MISSING]** | ✓ | |
| Dropdown / Menu | n/a | n/a | **✗** | n/a | No select trigger exists |
| Checkbox | **✗ [MISSING]** | Partial — single Focus variant (unchecked look) | **✗ [MISSING]** | ✓ | Focus + Checked **[MISSING]** |
| Radio | **✗ [MISSING]** | Partial — as Checkbox | **✗ [MISSING]** | ✓ | |
| Toggle | ✓ | ✓ (On/Off) | **✗ [MISSING]** | ✓ — On/Off near-identical (A35) | |
| Tooltip | n/a | n/a | n/a | n/a | Trigger/dismiss **[UNVERIFIED]** |
| Navigation | — | — | — | — | Component **[MISSING]** |
| Select trigger | — | — | — | — | Component **[MISSING]** |

---

## 3. Focus indication [EXTRACTED]

| Component | Treatment | Observation |
|---|---|---|
| Button Primary | 2 px border `#003fbc` on `#004feb` fill | 1.36:1 against fill [COMPUTED] — weak; contrast against page **[UNVERIFIED]** |
| Button Secondary | 2 px border, same colour as the Default border | Width-only change (2.4.7 risk); Default border width **[UNVERIFIED]** |
| Button Tertiary / Tertiary Grey / Link | Border `#004feb` bound | Width **[UNVERIFIED]** |
| Input / Outline | 1 px border `#3a6ff7` (raw value) | Colour swap only |
| Input / Filled | 1 px border `#003fbc` | Colour swap only; 8.04:1 vs field fill (A19) |
| Dropdown / Item | 2 px `#003fbc` + `Button/Focus` glow | Strongest indicator; 8.04:1 vs fill (A24) |
| Checkbox / Radio | 2 px `#004feb` + `Button/Focus` + `shadow/sm` on `#ebf2ff` | 5.63:1 vs fill (A31); only for unchecked appearance |
| Toggle | Focus On: border `#003fbc` | Width **[UNVERIFIED]** |

No shared focus-ring token exists (`05-elevation-effects.md` E10). Focus treatment is **inconsistent** across components (`07` X1).

---

## 4. Typography & legibility [EXTRACTED]

| Observation | Evidence | Concern |
|---|---|---|
| 8 px (Body Micro, Caption Micro) and 10 px (Body XXS, Caption XSmall) styles | `03-typography.md` §2 | Below the file's own rule "Min 12px UI / 14px Body" |
| Fixed px line-heights | `03` | Resize/text-spacing behaviour **[UNVERIFIED]** — implementation-dependent |
| Fixed button heights with `overflow: clip` | `button.md` §1.3 | Enlarged text may clip (1.4.4 risk) |
| Desktop Heading tooltip fixed height 59 px | `tooltip.md` TT5 | Long content clips |
| Proxima Nova only; no fallback stack | `03` T10 | Fallback metrics unknown |

---

## 5. Other observations

| # | Observation | Evidence | Status |
|---|---|---|---|
| AX1 | Light tooltip has no border/shadow — boundary depends on page colour. | `tooltip.md` TT1 | [EXTRACTED] |
| AX2 | Dropdown menu has a border but no shadow; border vs page **[UNVERIFIED]**. | `dropdown.md` D2 | [EXTRACTED] |
| AX3 | Input/Outline error icon is shown in **all** states, weakening its meaning as an error cue. | `input.md` IN5 | [EXTRACTED] |
| AX4 | Radio dot and Toggle track are flattened vectors — state colours not tokenised; must be rebuilt with verified contrast. | `radio.md`, `toggle.md` | [EXTRACTED] |
| AX5 | Target sizes: Button heights 24–32 px at small sizes; Checkbox/Radio Small control 20 × 20. WCAG 2.5.8 needs ≥ 24 × 24 CSS px or spacing; whether the label is part of the target is **[UNVERIFIED]**. | `button.md`, `checkbox.md` | [EXTRACTED sizes] |
| AX6 | Dark theme only partially observed; dark contrast checked for Dropdown only (A27, A28). | `dropdown.md` §5 | Partial |

---

## 6. Not verifiable from Figma — must be specified before/at implementation

| Area | Status |
|---|---|
| Keyboard operation (Tab order; Space/Enter; Arrow keys in Radio groups, Dropdown; Esc to close) | **[UNVERIFIED]** |
| Semantic roles & accessible names (`button`, `checkbox`, `radio`, `switch`, `listbox`/`option`, `combobox`, `tooltip`, navigation landmarks) | **[UNVERIFIED]** |
| Accessible names for icon-only and Loading buttons | **[UNVERIFIED]** |
| Error association and announcements (`aria-invalid`, `aria-describedby`, live regions) | **[UNVERIFIED]** |
| Tooltip trigger, delay, hover persistence and dismissal (1.4.13) | **[UNVERIFIED]** |
| Reduced-motion behaviour | **[UNVERIFIED]** — no motion specs |
| Reflow at 320 px (1.4.10) | **[UNVERIFIED]** — breakpoints missing (`04` L2) |

---

## 7. Summary

| Result | Count |
|---|---:|
| Explicit pairs computed | 37 + 1 focus-border pair |
| Text pairs failing AA normal text | **3** (A04, A14, A16) — *2026-11-19 update: **4** with A38 (Filled Hover placeholder 2.46:1, confirmed in R3-3)* |
| Non-text pairs below 3:1 (indicative, vs own fill) | 3 (A18, A26, A29) + Primary focus border 1.36:1 |
| Components missing Hover | 3 (Input/Outline, Checkbox, Radio) + Link Hover ineffective |
| Components missing Error | 4 (Checkbox, Radio, Toggle, Dropdown) |
| Components with incomplete/weak Focus | Checkbox, Radio (single variant); Button Secondary, Inputs (weak) |
| Behavioural accessibility items | 7 areas **[UNVERIFIED]** |

### R4 additions (2026-11-20)

These contrast pairs were computed during the R4 implementation; the design values are unchanged.
- **Pass:** Dropdown labels: Default 18.25:1, Hover 16.98:1, Selected `#004feb` on `#f3f7ff` 5.89:1. Search placeholder/value `#555d6d` on `#f6f7f9` 6.17:1 (D6). Item focus stroke `#003fbc` on `#f6f7f9` 8.04:1. Search focus border (DD-1) `#3a6ff7` 4.08:1. Tooltip text 19.03:1 in both modes.
- **Fail (non-text):** **A40** (light tooltip invisible on a light page, 1.00:1) and **A41** (Menu boundary 1.70:1). Both are reproduced as designed.
- **Exempt:** the disabled indicator `#bfc4cf` on `#f6f7f9` (1.63:1) and the disabled label (4.02:1).
