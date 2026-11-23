# Button (gradient) — R3-2

Figma: file `rM3ixSG6i3DFfKZFWuxzs4`, component set **Button** `1153:3370`: 11 Sizes × 5 States = **55 variants**. **Every variant was inspected individually**, so nothing is extrapolated.
Evidence: `docs/figma-audit/r3-0-evidence.md` §5, §6, §17, §18, §22 (full matrix in §22.1).

## API

| Figma property | Markup |
|---|---|
| `Size` | `.annachy-button-gradient--size-24` · 26 · 28 · 32 · 36 · 40 · 42 · 46 · 48 · 52 · 56 (no 38). Without a size class, the button uses size 40 values. |
| `State` | Default · Hover `:hover` / `.is-hover` · Focus `:focus-visible` / `.is-focus` · Pressed `:active` / `.is-pressed` · Disabled `disabled` / `aria-disabled="true"` |
| `leftIcon` / `rightIcon` / `labelText`, `label` | presence of `.annachy-button-gradient__icon` / `__label` |

The set has no Loading state.

## Values

| Item | Implementation |
|---|---|
| Fills | Default: `Gradient/Color 1` → `Color 2`. Focus: `Blue/600` → `Blue/400`. Pressed: `Blue/500` → `Color 2`. Disabled: Pressed stops at 19% (`color-mix`). Hover: raw rgba (GB-4). |
| Angle | The Figma CSS angle for each Size × State (`--_gb-angle-*`). Pressed and Disabled share the Default angle at every size. |
| Stroke | 1.5px `Blue/300`; Focus 2px `Blue/500`. Drawn as an inset `box-shadow` because the Figma stroke is inside and not part of the layout (frame widths exclude it and are equal across states). |
| Shadows | Raw Figma values as `box-shadow` (blur = Figma radius). Focus and Disabled have none. |
| Typography | R1 tokens. Sizes 24 / 26–28 / 32–42 / 46–48 / 52–56 use Body XS-Semibold / Body S-Semi / H7 / Subheading L / H5. **Exception:** size 24 Focus uses Label XSmall Semibold 12/17. |
| Padding / gap / radius | Component-local (raw in Figma): 8/4/4 (24–28), 12/8/8 (32–40), 16/12/12 (42–56). Vertical padding is 0; height comes from `Height/N`. |

## Figma characteristics reproduced, not normalised

| Flag | Behaviour |
|---|---|
| GB-1 | Size 26 label is 14/18. All Buttons 26 is 12/18. |
| GB-2 | The gradient angle depends on the frame aspect ratio (tan θ = k·H/W). The CSS uses the documented angle, which is exact at the documented width. Labels of other widths keep that angle. |
| GB-3 | Size 24 Focus label is Label XSmall Semibold 12/17; the other size-24 states are 12/18. |
| GB-4 / B9 | The Hover fill and all shadows are raw values, not variables or effect styles. |
| A14 / D-22 | Label contrast against the light gradient end is 3.89:1. |
| D-21 | Focus is shown by the Figma 2px stroke; the browser outline is suppressed while it shows. |

## Accessibility (B-01)

Native `<button type="button">`. Icon-only buttons need an `aria-label`. Disabled uses the native `disabled` attribute.

## Validation

`tests/fixtures/r3-button-gradient-check.html` checks all 55 variants:
- height, padding, gap, radius, icon slots, and width structure (stroke not part of the layout);
- font size, line height, weight, family and letter-spacing;
- label colour;
- gradient angle (±0.001°), stops and positions;
- inset stroke width and colour, and every shadow layer;
- native button, accessible name, disabled state and focus outline;
- native `:focus-visible` (the size-24 typography exception applies and reverts on blur);
- the cascade layer.

A mutation test (one angle changed and one typography token swapped) produced the expected 3 failures.
