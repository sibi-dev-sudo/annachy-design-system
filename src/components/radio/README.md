# Radio Button — R3-5

Figma: `.Selection Controls / Radio Button` `1504:52363`: 6 States × 3 Sizes × 2 Positions × 3 Alignments = **108 variants**, all implemented.
Evidence: `docs/figma-audit/components/radio.md` and `docs/figma-audit/r3-0-evidence.md` §11, §12, §19, §25.

## API

| Figma property | Markup |
|---|---|
| `Size` | `.annachy-radio--small` (circle 20, dot 8) · `--medium` (24 / 10) · `--large` (28 / 12) |
| `Position` | Left (default) · `.annachy-radio--control-right` |
| `Alignment` | `.annachy-radio--align-top` · Center (default) · `--align-bottom` |
| `State=Unselected` | default |
| `State=Selected` | `checked` |
| `State=Pressed` | `:active` (test class `.is-pressed`) |
| `State=Focus` | `:focus-visible` (test class `.is-focus`) |
| `State=Disabled Unselected` | `disabled` |
| `State=Disabled Selected` | `disabled` + `checked` |

## Values (§25)

| State | Fill | Border | Shadow | Dot |
|---|---|---|---|---|
| Selected | `#004feb` | **not drawn (ring width D-27)** | `Button/Default` | `Background/Primary` |
| Unselected | `surface-bg` (compat) | 2px `border-default` (compat) | — | — |
| Disabled Unselected | `Blue-Grey/100` | 2px `Blue-Grey/200` | — | — |
| Disabled Selected | `Button/Primary/Background/Disabled` | none (no stroke bound) | — | `Content/Disabled` |
| Focus | `Blue-White/300` | 2px `#004feb` | `shadow/sm` + `Button/Focus` | — |
| Pressed | `Pressed-Active` | **not drawn (ring width D-27)** | `Button/Hover` | `Background/Primary` |

- The radius is the raw half-size value: 10 / 12 / 14.
- The dot is centred at inset 6 / 7 / 8.
- Label, subtext and layout match the Checkbox.
- In the disabled states, label and subtext are `Blue-Grey/200`.

## Unresolved (not invented)

- **D-27 ring:** Selected and Pressed have a `Blue/300` ring, but Figma flattens the control into an image, so the stroke width cannot be read. No ring is drawn.

## D-20: recommendation, not a confirmed Figma specification

Focus on a selected radio keeps the selected fill and dot and adds the Figma focus border and shadows.

## Accessibility (B-01)

- Native `<input type="radio">`, transparent and positioned over the circle.
- `<label for>`, plus `aria-describedby` for the subtext.
- Group radios with a shared `name` in a `<fieldset>` + `<legend>`; the browser's native arrow-key behaviour and exclusivity apply.

## Validation

`tests/fixtures/r3-radio-check.html` checks all 108 variants. **2,423 checks, 0 failures.** It covers:
- root size, circle size and radius;
- alignment and position, content offset and text padding;
- typography, fill, border (and that no ring is drawn), shadow, label and subtext colours;
- dot visibility, size, inset and colour;
- native semantics and the input covering the circle;
- the D-20 recommendation;
- group exclusivity, label click, focus, and blocked disabled selection;
- the cascade layer.

Mutation tests caught 36, 18 and 18 failures.
