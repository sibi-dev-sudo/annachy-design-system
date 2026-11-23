# Tooltip — R4-2

Figma: `tooltip` `1448:16825`: Device 2 × Mode 2 × Arrow 10 × Format 2 = **80 variants**, all implemented.
Evidence: `docs/figma-audit/components/tooltip.md` and `docs/figma-audit/r4-0-evidence.md` §4 (per-variant geometry for all 80).
Behaviour: `docs/implementation/r4-behaviour-spec.md` §2 (approved R4-Q1, Q4, Q5).

## API

| Figma property | Markup |
|---|---|
| Device | `.annachy-tooltip--mobile` / `--desktop` (no breakpoints; the consumer chooses) |
| Mode | `.annachy-tooltip--dark` / `--light` |
| Format | Text only (default, `.annachy-tooltip__text`) / `.annachy-tooltip--heading` (`__heading` + `__description`) |
| Arrow | `.annachy-tooltip--arrow-left`, `-left-center`, `-right`, `-right-center`, `-top`, `-top-left`, `-top-right`, `-bottom`, `-bottom-left`, `-bottom-right` |
| Trigger | a focusable element with `data-annachy-tooltip="<id>"` and `aria-describedby="<id>"`; the tooltip has `role="tooltip"` and `hidden` |

## Values

| Item | Desktop | Mobile |
|---|---|---|
| Text only | Body XS — Medium 12/18 (500); hug width, max 300 | Body S - Semi 14/18 (600); hug width, max 300 |
| Heading format | **fixed 240 × 59**; heading Body S - Semi 14/18, description Label XSmall Regular 12/17 | **fixed 260 × 62**; heading H7 Semibold 16/18, description Body S Regular 14/20 |

| Item | Dark | Light |
|---|---|---|
| Fill / text | `Base/Black` / `Base/White` | `Base/White` / `Base/Black` |

- Common to all variants: padding 10, raw radius 4, heading gap 4. **No border or shadow.**
- **Arrow box:** 20 × 20, protruding 13px, with each variant's exact offset and transform. `left` / `right` sit 9px from the top; `*-center` are centred; corner arrows sit 12px from the edge. The top/bottom centring offsets are reproduced exactly per variant: Mobile dark −0.43px, Mobile light −1px, Desktop light text −0.5px, Desktop dark text +0.07px, Desktop light heading −1px, Desktop dark heading −0.43px. Desktop heading `*-center` arrows sit at +0.5px.
- **Arrow glyph:** empty. The slot's `color` is the body colour (the polygon's fill binding), so a consumer SVG using `currentColor` will match.

## Behaviour (approved)

| # | Behaviour |
|---|---|
| T1 / T4 | Hover shows after **500 ms**; leaving hides after **150 ms** |
| T2 | Keyboard focus (`:focus-visible`) shows **immediately**; blur hides |
| T3 | Touch: a tap that focuses the trigger shows the tooltip; tapping outside hides it (R4-Q5) |
| T5 | **Escape** hides the tooltip without moving focus. The next hover or focus shows it again |
| T6 | Hoverable: the pointer can move onto the tooltip without it closing (WCAG 1.4.13) |
| T7 | Placement: the arrow side is the side of the body, so the tooltip goes on the **opposite side of the trigger**, with the arrow box centred on the trigger |
| T8 | Collision: only the 10 Figma placements are tried (same side first, then the opposite side, then the rest). If none fits, the preferred placement is kept. The preferred arrow is restored on hide |
| T11 / T12 | `aria-describedby` → tooltip (description). Icon-only triggers take their **name** from `aria-label` |
| T13 | Natively `disabled` triggers can't show a tooltip; use `aria-disabled="true"` and guard activation (R3 BTN-3) |
| T17 | Only one tooltip shows at a time; moving between triggers shows the next one immediately (warm-up) |

## Known limitations and reproduced design defects

| Flag | Item |
|---|---|
| **G12** | **The arrow glyph is not implemented.** The Figma `regular-polygon`'s point count and rounding can't be read. The slot is positioned and transformed exactly, but it's empty |
| **TT-POS (derived)** | The trigger-to-tooltip spacing isn't designed. A 12px gap is **derived** from the arrow geometry (the box protrudes 13px and the polygon tip sits 1px inside it, so the tip touches the trigger) |
| G5 / TT1 | Light tooltip: `#fafcff` with no border or shadow, so it's invisible on light surfaces. Reproduced |
| G7 / TT5 | The Heading format is fixed-size; longer text overflows the body (there is no clip in Figma). Reproduced |
| TT3 | Raw radius 4 (not the `Radius/4` variable) |
| Mobile / Desktop | Visual variants only; no automatic device switching (D-07) |

## Validation

- **`tests/fixtures/r4-tooltip-check.html`:** all 80 variants, **1,441 checks**. Each variant is compared with its own Figma-emitted arrow offsets and transform matrix. Also covered: padding, radius, max-width, fill and text colours, no border or shadow, the role, fixed heading sizes and text positions (10 / 32, Figma META), typography, the 38px single-line height and hug width, the arrow colour and its empty, `aria-hidden` slot.
- **`tests/fixtures/r4-tooltip-interaction.html`**, driven with real mouse, keyboard and touch through the Chrome DevTools Protocol: **39 checks**. Covers the 500 / 150 ms timings, hoverable persistence, warm-up, one-at-a-time, placement and the derived gap, keyboard focus, Escape (and re-hover), blur, the `aria-disabled` trigger, touch tap and tap-outside, collision flips at the right and bottom viewport edges, and the accessibility description / name / role.
- **Mutation tests 8 / 8 caught:**
  - M1 centring offset: 2 failures
  - M2 arrow mirror: 8
  - M3 heading height: 20
  - M4 text weight: 20
  - M5 show delay: 1
  - M6 hide delay: 1
  - M7 Escape: 1
  - M8 arrow gap: 2
