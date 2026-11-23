# Checkbox — R3-4

Figma: `.Selection Controls / Checkbox` `1504:53300`: 7 States × 3 Sizes × 2 Positions × 3 Alignments = **126 variants**, all implemented.
Evidence: `docs/figma-audit/components/checkbox.md` and `docs/figma-audit/r3-0-evidence.md` §10, §11, §19, §24.

## API

| Figma property | Markup |
|---|---|
| `Size` | `.annachy-checkbox--small` (box 20, glyph 16) · `--medium` (24 / 20) · `--large` (28 / 20) |
| `Position` | Left (default) · `.annachy-checkbox--control-right` (content first; 12px padding moves to the right) |
| `Alignment` | `.annachy-checkbox--align-top` · Center (default) · `--align-bottom` |
| `State=Unchecked` | default |
| `State=Checked` | `checked` |
| `State=Multi-select` | `data-indeterminate="true"` (applied by `checkbox.js` / `initCheckboxes()`) |
| `State=Pressed` | `:active` (test class `.is-pressed`) |
| `State=Focus` | `:focus-visible` (test class `.is-focus`) |
| `State=Disabled` | `disabled` |
| `State=Disabled On` | `disabled` + `checked` |
| `showLabel`, `showSubtext` | presence of `__label` / `__subtext` |

When several states apply, the precedence is: Unchecked < Checked < Multi-select < Pressed < Focus < Disabled < Disabled On.

## Values (§24)

| State | Box fill | Border | Shadow | Glyph slot | Text |
|---|---|---|---|---|---|
| Checked, Multi-select | `Button/Primary/Background/Default` | 1px `Blue/300` | `Button/Default` | shown, `Background/Primary` | `Text/Primary` / `Text/Tertiary` |
| Unchecked | `surface-bg` (compat) | 2px `border-default` (compat) | — | — | same |
| Focus | `Blue-White/300` | 2px `#004feb` | `shadow/sm` + `Button/Focus` | — | same |
| Pressed | `Pressed-Active` `#3372ef` | 1px `Blue/300` | `Button/Hover` | shown | same |
| Disabled | `Blue-Grey/100` | 2px `Blue-Grey/200` | — | — | `Blue-Grey/200` (both) |
| Disabled On | `Button/Primary/Background/Disabled` | none | — | shown, `Content/Disabled` | `Blue-Grey/200` (both) |

The box radius is `Radius/4` at every size. The label is Label Medium 16/21 at every size. The subtext is Body S 14/20 at a fixed width of 184 (CB8).

## Unresolved (not invented)

- **D-27 glyph:** the `functional/check` and `functional/remove` glyphs are images in Figma, with no readable geometry. **The glyph slot ships empty.** Its size (16/20/20), centring and colour (`#fafcff`, derived from the only unassigned binding) are implemented, so a glyph can be added once the design owner supplies the geometry. Until then, Checked and Multi-select are shown by fill, border and shadow only, and by the native checked/indeterminate state for assistive technology.
- **Disabled + indeterminate:** this combination is not a Figma variant. It uses the Disabled On paint.

## D-20: recommendation, not a confirmed Figma specification

Figma has one Focus variant, with an unchecked appearance. Focus on a **checked or indeterminate** checkbox keeps the checked fill and glyph slot and adds the Figma focus border and shadows.

## Reproduced, not fixed

- CB1 / D-19: foreign compat tokens on the Unchecked box and the focus shadow.
- CB3: no Hover state.
- CB4: no Error state.
- CB5: Pressed uses the `Button/Hover` effect.

## Accessibility (B-01)

- Native `<input type="checkbox">`, transparent and positioned exactly over the box, so the box is the click target.
- `<label for>` holds the name; `aria-describedby` points to the subtext.
- Indeterminate is set through the DOM property.
- The browser focus outline is not shown because the input is transparent. The Figma Focus box treatment is the indicator (D-21).

## Validation

`tests/fixtures/r3-checkbox-check.html` checks all 126 variants. **3,108 checks, 0 failures.** It covers:
- root size (box + 196 × 41, the Figma META size);
- box size, position for each Alignment and Position, and content position;
- text padding, subtext width and radius;
- typography;
- fill, border and shadow (compared with the literal Figma effect values);
- text colours;
- glyph-slot visibility, size, inset, colour and emptiness;
- native semantics, label association, the description, and the input covering the box;
- indeterminate through `checkbox.js` and disabled;
- the D-20 recommendation;
- native focus, click, label click, indeterminate clearing and blocked disabled toggling;
- the cascade layer.

Mutation tests (glyph size, Disabled On border, Right padding, Pressed effect) caught 48, 18, 189 and 18 failures.
