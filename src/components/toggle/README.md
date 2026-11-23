# Toggle — R3-6

Figma: `.Selection Controls / Toggle` `1504:54471`: 10 States × 3 Sizes × 2 Positions × 3 Alignments = **180 variants**, all implemented.
Evidence: `docs/figma-audit/components/toggle.md` and `docs/figma-audit/r3-0-evidence.md` §11, §13, §19, §26.

## API

| Figma property | Markup |
|---|---|
| `Size` | `.annachy-toggle--small` (track 32×16, thumb 12, Label Small 14/20) · `--medium` (38×20, 16, Label Medium 16/21) · `--large` (44×24, 20, Label Large 18/22) |
| `Position` | Left (default) · `.annachy-toggle--control-right` |
| `Alignment` | `.annachy-toggle--align-top` · Center (default) · `--align-bottom` |
| `State=On` / `Off` | `checked` / not checked |
| `Hover On/Off` | `:hover` (test class `.is-hover`) |
| `Pressed On/Off` | `:active` (test class `.is-pressed`) |
| `Focus On/Off` | `:focus-visible` (test class `.is-focus`) |
| `Disabled On/Off` | `disabled` |

When several states apply, the precedence is: Default < Hover < Pressed < Focus < Disabled.

## Values (§26)

| State | Track (On / Off) | Extra |
|---|---|---|
| Default | `#004feb` / `Blue-Grey/50`* | — |
| Hover | `#003fbc` / `Blue-Grey/200` | — |
| Pressed | `#3372ef` / `Blue-Grey/300` | On: track shadow `Toggle/Press` |
| Focus | `#004feb` / `Blue-Grey/200` | Thumb moves 1.5px inward (On) / to x 3 (Off), as in Figma. The focus border width is unresolved. |
| Disabled | `Blue-Grey/100`* / `Blue-Grey/50`* | Label and subtext `Blue-Grey/200` |

\* **TG-1 (derived):** these three tracks have no binding of their own. The value used is the only bound candidate, which the track shares with the thumb.

- **Thumb:** fill `Button/Primary/Content/Loading` `#fafcff` (T2); effect `Toggle/On` or `Toggle/Off`.
- **Thumb position:** Off x = 2; On x = track − thumb − 2; y = 2.

## Unresolved (D-27): not invented, not drawn

- **Track corner radius:** not readable, so the track renders with **square corners**. A radius can be added when the design owner supplies one.
- **Thumb stroke:** the colour is bound (`Blue-Grey/50`, `100` or `200`, depending on state), but the width is not readable.
- **Track focus border:** `Border/Focus` is bound, but the width is not readable. Focus is shown by the Figma track colour and thumb offset only (D-21).
- **Label max-width 240:** inspected at Medium only, so it is applied only at Medium.

## Reproduced, not fixed

- T2: the thumb uses the Button Loading colour.
- T3: Disabled On (`#edeff2`) and Disabled Off (`#f6f7f9`) are nearly identical.
- T4: Toggle has Hover states while Checkbox and Radio don't.

## Accessibility (B-01)

- Native `<input type="checkbox" role="switch">`, transparent and positioned over the track.
- `<label for>`, plus `aria-describedby` for the subtext.
- Space toggles it.
- Because the focus border is unresolved, the focus indication is weak (a colour and offset change only); it is flagged under D-21.

## Validation

`tests/fixtures/r3-toggle-check.html` checks all 180 variants. **4,904 checks, 0 failures.** It covers:
- root, track and thumb size and position for every state and size;
- that the track radius and strokes are not drawn;
- typography and label max-width;
- track colour and shadow, thumb fill and shadow, label and subtext colours;
- the switch role, checked state, label association and the input covering the track;
- native click, focus thumb offset and label click;
- blocked disabled toggling;
- the cascade layer.

Mutation tests caught 19, 18, 60 and 18 failures.
