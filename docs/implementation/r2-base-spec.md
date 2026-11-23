# R2 Implementation Specification — Base Styles

| Item | Value |
|---|---|
| Phase | **R2 — Base** (roadmap `docs/figma-audit/10-summary-and-roadmap.md` §7) |
| Depends on | R1 tokens (457, validated) — **unchanged by R2** |
| Source of truth | Figma file `rM3ixSG6i3DFfKZFWuxzs4` via the audit and R1 token register |
| Date | 2026-11-19 |
| Status | **Implemented 2026-11-19** — static and browser validation PASS (`tests/fixtures/r2-base-check.html`); R1 regression PASS (457/457). |

## 1. Decisions applied

| Topic | Decision (given) | R2 implementation |
|---|---|---|
| Typography (D-05/D-07) | Keep Mobile values active; Desktop as reference; no breakpoint | Text classes use the active (Mobile) tokens only. No `@media`. |
| Font (D-06) | Temporary system-font fallback for browser rendering only; not a Proxima Nova replacement; no unlicensed fonts | No `@font-face`, no font files. A **base-layer** variable `--annachy-base-font-family-render: var(--annachy-font-family-sans), system-ui, sans-serif` is used for rendering. The R1 token `--annachy-font-family-sans` stays `"Proxima Nova"`. |
| Focus (D-21) | No universal focus style; preserve component-specific focus for R3; no global focus token | **No `:focus` / `:focus-visible` rules** in R2. The reset does not remove browser focus indicators. Component focus specs remain in `docs/figma-audit/components/*.md` for R3. |
| Base styles | Only foundations supported by audit + R1 | See §2. No spacing, breakpoints or layout values. |
| Theme | Light V1, dark-ready | Base rules reference **semantic** tokens only for theme-dependent colour, so a future `[data-annachy-theme="dark"]` override applies automatically. |

## 2. Scope

| File | Contents | Evidence / justification |
|---|---|---|
| `src/base/reset.css` | `box-sizing: border-box`; `body { margin: 0 }`; media elements `display: block; max-width: 100%`; form controls inherit font; `-webkit-text-size-adjust: 100%` | Technical normalisation; introduces no design values. **Does not touch outlines or focus.** |
| `src/base/document.css` | `:root` `color-scheme: light`; `body` font (render stack), default text style **Body M** (16/24, Regular), colour `Text/Primary`, background `Background/Primary`, letter-spacing token | Body M usage "Default body text" (`03` §2.2, row `1558:49005`); semantic colours (`02` §1.3) |
| `src/base/typography.css` | 28 classes `.annachy-text-<style>` (font family, active size, line-height, weight, letter-spacing) | Scale A (D-04), active Mobile tokens (`03` T12) |
| `src/base/utilities.css` | Text colour (7), background (3), radius (11), shadow (33 documented + 6 component effects), brand gradient (1), `.annachy-visually-hidden` (1) | One class per existing R1 token; visually-hidden is a standard technical accessibility utility (no design values) |

### Explicitly out of scope

| Not implemented | Reason |
|---|---|
| `@font-face` / font files | No licensed files (D-06) |
| Global focus ring / focus utility / focus token | D-21 unresolved; user decision |
| Spacing utilities, margin/padding scales | No spacing scale (D-08) |
| Breakpoints, responsive classes, container/max-width | Not defined (D-07) |
| Grid layout utilities | Grid tokens are reference values without breakpoints |
| Element-level heading styles (`h1`–`h6` → H1–H6) | Mapping HTML levels to Scale A styles is not specified in Figma; classes are provided instead |
| Dark theme file | V1 Light only (D-03) |
| Compat (foreign) utilities | D-19 pending; tokens remain available to R3 |

## 3. Cascade

`src/annachy.css` adds, after the six token imports:

```
@import url("base/reset.css")      layer(annachy.base);
@import url("base/document.css")   layer(annachy.base);
@import url("base/typography.css") layer(annachy.base);
@import url("base/utilities.css")  layer(annachy.base);
```

## 4. Validation

| Check | Method | Pass criterion |
|---|---|---|
| R1 tokens unchanged | R1 static validator + `tests/fixtures/r1-token-check.html` | 457/457, 0 mismatches |
| Base references | Static scan of `src/base/*.css` | Every `var(--annachy-…)` resolves to an R1 token or the documented render variable; only one new custom property defined |
| Forbidden content | Static scan | 0 `@media`, 0 `@font-face`, 0 `:focus`, 0 `outline` rules, 0 non-zero margin/padding values |
| Class counts | Static scan | 28 text classes + 62 utilities (61 token utilities + visually-hidden) |
| Browser | `tests/fixtures/r2-base-check.html` in headless Chrome | 10 imports loaded in correct layers; body computed style matches Body M + semantic colours; all 28 text classes compute to token values; utility classes compute equal to their tokens; no author focus rules in loaded sheets |

## 5. Unresolved dependencies (carried forward)

| ID | Item |
|---|---|
| D-06 | Licensed Proxima Nova files and an approved fallback stack (current system fallback is temporary) |
| D-21 | Focus-indicator standard (R3 will apply per-component Figma focus specs) |
| D-05 / D-07 | Breakpoint / switch width for Desktop typography and layout |
| D-08 | Spacing scale (none) |
| D-19 | Foreign compat tokens |
