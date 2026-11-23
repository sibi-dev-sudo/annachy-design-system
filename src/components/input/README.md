# Input Field (Outline & Filled) — R3-3

Figma: file `rM3ixSG6i3DFfKZFWuxzs4`.
- **Outline** `1066:37962`: 6 States × 5 Sizes × 5 Radii = 150 variants.
- **Filled** `1066:40663`: 7 States × 5 Sizes × 5 Radii = 175 variants.

Evidence: `docs/figma-audit/components/input.md` and `docs/figma-audit/r3-0-evidence.md` §7 (sizes), §8 (Outline states), §9 (Filled states) and §23 (radius, verification, full mapping).

## API

| Figma property | Markup |
|---|---|
| Set | `.annachy-input--outline` / `.annachy-input--filled` |
| `Size` (field height) | `.annachy-input--size-46` · 48 · 50 · 54 · 56 |
| `Radius` | `.annachy-input--radius-4` · 6 · 8 · 10 · 12 |
| `State=Default` | — |
| `State=Hover` (Filled only) | field `:hover` (test class `.is-hover`) |
| `State=Focused` | control `:focus-visible` (test class `.is-focus`) |
| `State=Filled` | control has a value (`:not(:placeholder-shown)`; test class `.is-filled`) |
| `State=Error` | `aria-invalid="true"` on the control |
| `State=Success` | `.annachy-input--success` on the root |
| `State=Disabled` | `disabled` on the control |
| `showLabel`, `showDescription`, `showSubText`, `show*Icon` | presence of the element |

When several states apply at once, the precedence is: Disabled > Success > Error > Focused > Filled > Hover > Default. All state selectors are wrapped in `:where()`, so they share one specificity and source order alone sets the precedence. Two precedence bugs found by the fixture were fixed this way: `:has()` had raised the specificity of some state selectors.

## Values

| Item | Source |
|---|---|
| Colours | R1 tokens (§23.4 mapping). Outline Focused border is the raw `#3a6ff7` (IN2). |
| Typography | Label: H7 Semibold 16/18. Description and sub-text: Body S 14/20. Value: Body M-Medium 16/24. |
| Geometry | Field: padding-x 14, gap 6, 1px border, height = Size. Root gap 2. Top Section gap 4 at a fixed height of Size + 42. Right-icon gap 8. Sub-text gap 4 (Outline) / 2 (Filled). |
| Radius | `Radius/4/8/12` → R1 tokens. **`Radius/6` and `Radius/10` are Figma variables with no R1 token**, so they are component-local `6px` / `10px` (D-09). Adding them is a token-addendum decision for you. |
| Icons | Slots only (no assets, D-12/D-13). 24px; sub-text icon 16 (Outline) / 14 (Filled). Filled slots use the `brand` icon colour and 30% opacity in Default, Hover and Disabled. |
| Width | `100%` of the container. Figma's 337px is the documentation frame width. |

## Figma characteristics reproduced, not fixed

| Flag | Behaviour |
|---|---|
| IN1 / A16 | Placeholder `#dcdfe5` has 1.25:1 contrast on the Filled fill |
| IN-13 / A38 (new, **confirmed accessibility issue**) | Filled Hover placeholder `#98a0ae` has 2.46:1 contrast on its fill (fails WCAG 1.4.3). The design value is unchanged pending approval. |
| IN2 | The Outline focus border is the raw `#3a6ff7`; Filled uses `Blue/600`. Focus is indicated by the 1px border colour only (D-21). |
| IN3 | Outline has no Hover state |
| IN4 | Error and Success use the icon-state variables (`#e72b23`, `#276732`) |
| IN5 | Outline always includes the error-circle icon slot |
| IN-12 | The Top Section keeps a fixed height (Size + 42) even when the label or description is hidden |

## Accessibility (B-01)

- Native `<input>` with a `<label for>`.
- The description and sub-text are linked with `aria-describedby`.
- Error is `aria-invalid="true"`; put the message in the sub-text.
- The browser outline on the control is suppressed because the Figma field border is the focus indicator (Focused state).

## Coverage and validation

- **Inspected individually** (≈ 35 of 325 variants):
  - all 13 state mappings at 48/R8;
  - every radius in both sets;
  - sizes 46–56;
  - 7 cross-combinations.
- **The remaining variants** follow the verified model: State → colours; Size → height; Radius → corner. `tests/fixtures/r3-input-check.html` renders **all 325** variants and checks each one against that model:
  - geometry: root / Top / field heights, which match the Figma META heights exactly, plus icon positions, padding, gaps and radius;
  - typography and colours, including the placeholder;
  - icon opacity;
  - label association, `aria-describedby`, `aria-invalid` and `disabled`;
  - contrast;
  - native focus and value-entry transitions.
- The fixture also checks:
  - Disabled behaviour: the control cannot take focus, matches `:disabled`, shows the not-allowed cursor, and Disabled wins over Hover, Focus, Error and Success;
  - state precedence;
  - that Radius 6 and 10 render their exact values with no R1 token involved.
- Results: **11,952 checks, 0 failures**.
- Mutation tests: radius and Hover border (90 failures), padding (975), label typography (325), Disabled fill (26), Success/Error order (1). All were caught.
