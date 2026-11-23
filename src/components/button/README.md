# Button (All Buttons) — R3-1

Figma: file `rM3ixSG6i3DFfKZFWuxzs4`, component set **All Buttons** `887:2492`: 6 Types × 6 States × 12 Sizes = **432 variants**, all implemented.
Evidence: `docs/figma-audit/components/button.md` and `docs/figma-audit/r3-0-evidence.md` §1 (sizes), §2 (Secondary border), §3 (focus widths), §4 (Loading) and §21 (border widths, Loading geometry).
The gradient "Button" set (`1153:3370`) is a separate component (R3-2).

## API

| Figma property | Markup |
|---|---|
| `Type` | `.annachy-button--primary` · `--secondary` · `--secondary-grey` · `--tertiary` · `--tertiary-grey` · `--link` (required) |
| `Size` | `.annachy-button--size-24` · `26` · `28` · `32` · `36` · `38` · `40` · `42` · `46` · `48` · `52` · `56` (without a size class, the button uses size 40 values) |
| `State=Default` | — |
| `State=Hover` | `:hover` (test class `.is-hover`) |
| `State=Focus` | `:focus-visible` (test class `.is-focus`) |
| `State=Pressed` | `:active` (test class `.is-pressed`) |
| `State=Disabled` | native `disabled` (or `aria-disabled="true"` on `<a>`) |
| `State=Loading` | `aria-busy="true"` (+ `aria-disabled="true"`) |
| `showLeftIcon` / `showRightIcon` | presence of `.annachy-button__icon` before / after the label |
| `showLabel`, `label` | presence and text of `.annachy-button__label` |

Always include `.annachy-button__loading` with its three `.annachy-button__dot` children. It is hidden except in the Loading state. See `button.html`.

## Values

| Item | Source |
|---|---|
| Height, radius, typography, colours | R1 tokens (`--annachy-size-height-*`, `--annachy-radius-*`, `--annachy-type-*`, `--annachy-color-button-*`) |
| Padding, gap, border widths, dot geometry | Component-local `--_button-*`: Figma measurements with node IDs in `button.css` |
| Icon slot | 20 × 20 at every size (`1777:12415`). Consumers supply an inline SVG using `currentColor`; no icon assets are shipped (D-12/D-13). |

Border widths, derived from the Figma variant widths (`r3-0-evidence.md` §21.1):

| Types | Border |
|---|---|
| Primary, Tertiary, Tertiary Grey, Link | none; Focus 2px |
| Secondary, Secondary Grey | 1px in every state; Focus 2px |

The border is part of the box (`box-sizing: border-box`), so Focus variants are 4px wider (2px wider for Secondary types), as in Figma.

## Accessibility (B-01, approved)

- Native `<button type="button">`. Use `<a>` only for navigation.
- Icon-only buttons need an `aria-label`.
- **Loading:** the dots are `aria-hidden`. The label stays in the accessibility tree (visually hidden), so the button keeps its name. `aria-busy="true"` is set, with `aria-disabled="true"` rather than `disabled`, so focus is not lost.
- **Focus:** the Figma 2px focus border replaces the browser outline (D-21, component-specific). Loading buttons have no Figma focus variant, so they keep the browser outline.
- **Contrast** (label vs fill, computed in the fixture): only Primary Pressed falls below 4.5:1 (4.26:1, A04), as documented.
- **BTN-3 (R3 closure audit):** a Loading button (`aria-busy` + `aria-disabled`) stays focusable and **still fires `click`**, because `aria-disabled` does not block activation. Consumers must ignore clicks while busy, e.g. `if (btn.getAttribute('aria-busy') === 'true') return;`. This was verified with real Enter key input.

## Figma defects reproduced, not fixed

| Flag | Behaviour |
|---|---|
| B1 | Link Hover is identical to Default |
| B4 / D-22 | Primary Pressed `#3372ef` is lighter than Hover; label 4.26:1 |
| SUS-03 | Secondary Grey Pressed border is bound to `Border/Disabled` |
| BTN-2 | Secondary Grey Hover border is the raw `#dcdfe5` (no variable) |
| D-21 | Primary focus border `#003fbc` on `#004feb` (1.36:1) |
| BTN-1 | Primary Loading at size 24 binds `Primary/Background/Loading`, which is not an R1 token. The implementation uses `primary-background-default`, which has the identical value `#004feb`. |

## Known limitations

- **Loading dots at sizes 26 and 28:** derived from the variant widths (38px means an 18px dot frame). The dot geometry is assumed to match size 24 (4×4, gap 3), which was inspected.
- **Loading dots at sizes 32–56:** derived from the widths (28px frame); size 40 was inspected (6×6, gap 5).
- **Vertical padding:** nominal. Padding plus line height exceeds the height at several sizes, so the height governs and the content is centred, as in Figma.
- **Font:** text uses the temporary system fallback (D-06), so label widths differ from Figma.

## Validation

- `tests/fixtures/r3-button-check.html` checks all 432 variants: height, radius, padding, gap, typography, background, colour, border width and colour, icon slots, loading dots and widths, the Figma width relations, accessible name and native element, contrast set, native `:focus-visible`, and the cascade layer.
- Static checks: token references resolve, only private custom properties are defined, only allow-listed raw colours appear, and every forced state class is paired with its native state.
