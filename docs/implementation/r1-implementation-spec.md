# R1 Implementation Specification — Design Tokens

| Item | Value |
|---|---|
| Phase | **R1 — Tokens** (roadmap `docs/figma-audit/10-summary-and-roadmap.md` §7) |
| Status | Specification — **implemented 2026-11-19** (457 tokens; static and browser validation PASS — see `tests/manual/r1-token-checklist.md`, `tests/fixtures/r1-token-check.html`). |
| Source of truth | Figma file `rM3ixSG6i3DFfKZFWuxzs4` (immutable). This spec uses only local audit evidence; Figma was not accessed. |
| Token mapping | `r1-token-mapping.md` (every token: Figma name → value → CSS custom property → evidence) |
| Date | 2026-11-19 |

---

## 1. Inputs

### 1.1 Decisions applied

| ID | Decision (as given) | How R1 applies it |
|---|---|---|
| D-01 | `Brand/*` is the canonical colour scheme | All colour tokens derive from `Brand/*`. Lowercase scheme and `Supporting/*` are excluded (mapping §5). Non-`Brand` variables that components **bind** (icon-state, foreign compat) are kept in separate namespaces for fidelity (mapping §4). |
| D-02 | Preserve `Error/700 #9d4520` until owner confirmation | Token `--annachy-color-error-700: #9d4520`, flagged in mapping and `tokens.json`. |
| D-03 | Light theme for V1; dark-ready architecture | Theme-dependent tokens isolated in `themes/light.css`, scoped so a `dark.css` can override them later. Observed dark values documented, not shipped. |
| D-04 | Typography System (Scale A) selected | 28 Scale A styles tokenised; Scale B not tokenised. |
| D-07 | Do not invent breakpoint values | Grid values shipped as reference tokens; **no media queries, ranges or max-width**. |
| D-08 | Preserve evidenced spacing values; no invented scale | **No spacing tokens.** Evidenced padding/gap values stay component-local (R3) with node IDs. |

### 1.2 Decisions not given — handling without inventing values

| ID | Topic | R1 handling | Blocks R1? |
|---|---|---|---|
| D-05 | Mobile→Desktop type switch width | Active type tokens use **Mobile** values — the values components resolve in Figma (`03` T12). Desktop values shipped as reference tokens, not activated. | No |
| D-06 | Font licence / fallback | Family token = `"Proxima Nova"` only; no fallback appended; no font files. | No (blocks R2) |
| D-09 | Input radius 6/10 | Not tokenised; component-local in R3. Radius scale 4–34 tokenised as documented. | No |
| D-10 | Canonical shadow family | All evidenced effect styles tokenised under their own names; *which* component uses which is an R3 concern. | No |
| D-11 | Blur values at radius 0 | Preserved as `0px` (exact Figma value). | No |
| D-19 | Foreign tokens | Kept in `compat.css` (bound by Checkbox/Radio), flagged. | No |
| D-23 | Theme mechanism | Variable-mode architecture (follows D-03 "dark-ready CSS variables"). | No |
| D-24 | Status colours 500 vs 600 | Both sets exist as Figma variables → both tokenised (`feedback-*` and `icon-state-*`). | No |

---

## 2. Project inspection (2026-11-19)

| Path | State |
|---|---|
| `src/annachy.css` | Comment only — "Planned import order: tokens -> themes -> base -> components" |
| `src/annachy.js` | `export {};` placeholder |
| `src/tokens/`, `src/tokens/themes/`, `src/base/`, `src/components/`, `src/core/`, `src/icons/`, `src/assets/fonts/` | Empty (`.gitkeep`) |
| `showcase/index.html` | Placeholder page linking `../src/annachy.css` and `../src/annachy.js` |
| `tests/manual/`, `tests/fixtures/` | Empty |
| `docs/figma-audit/` | Complete audit (00–13, components, raw evidence) |

No build tooling, no dependencies, no Git repository (as instructed earlier).

---

## 3. Token architecture

### 3.1 Layers

| Layer | Contents | Theme-dependent? | File |
|---|---|---|---|
| **Primitives** | Colour scales & base colours; font family/weights/letter-spacing; heights; radius; border widths; grid reference values | No | `src/tokens/primitives.css` |
| **Semantic (theme)** | `Brand/Text/*`, `Background/*`, `Border/*`, `Icon/*`, `Action/*`, `Feedback/*` | **Yes** | `src/tokens/themes/light.css` |
| **Typography styles** | Scale A styles: active (Mobile) + Mobile/Desktop reference values | No | `src/tokens/typography.css` |
| **Component tokens** | `Brand/Button/*`; icon semantic state (`brand`, `disabled`, `error`, `success`, `warning`) | Not in V1 (overridable later) | `src/tokens/component-tokens.css` |
| **Effects** | Documented shadows, component effect styles, blur, glass radii/fills, brand gradient | No | `src/tokens/effects.css` |
| **Compatibility** | Foreign variables bound by components (`surface-bg`, `border-default`, `Colors/alpha/50`, `Blur/blur-0/2`, `shadow/sm`) | No | `src/tokens/compat.css` |

### 3.2 Value rules

1. **Values are copied exactly** from `r1-token-mapping.md`. No rounding, no colour-format conversion (Figma `#RRGGBBAA` kept), no px→rem conversion. Fractional Figma values (e.g. `1.9500000476837158px` in `Shadow Scale/SM/01`) are kept as returned.
2. **Semantic tokens hold literal values**, not `var()` references to primitives: Figma alias chains are not retrievable (`02` §6), so linking them would be an assumption. Only composite tokens reference other tokens where the composition itself is evidenced (e.g. `--annachy-gradient-brand` uses Gradient Color 1/2, exactly as `1153:3371` binds them).
3. **Units:** px for all dimensions, matching Figma. (Root-relative units are an accessibility consideration for R2 — `09` §4 — not an R1 change.)
4. **No token without evidence.** Each token carries an evidence tag (BIND / VAR / DOC / APPLIED) in `tokens.json`.

### 3.3 Naming convention

`--annachy-<category>-<figma-path-in-kebab-case>`

| Category | Rule | Example (Figma → CSS) |
|---|---|---|
| `color` | Drop the `Brand/` root; kebab-case remaining path; spaces and hyphens normalise to `-` | `Brand/Blue-Grey/300` → `--annachy-color-blue-grey-300`; `Brand/Button/Tertiary Grey/Background/Hover` → `--annachy-color-button-tertiary-grey-background-hover` |
| `color-icon-state` | Bare icon variables | `error` → `--annachy-color-icon-state-error` |
| `font-*` | Figma typography primitives | `Weight/Semibold` → `--annachy-font-weight-semibold` |
| `type-<style>-<prop>` | Scale A style name in kebab-case | H7 → `--annachy-type-h7-font-size`; Body S (Semibold) → `--annachy-type-body-s-semibold-*` |
| `size-height` / `radius` / `border-width` | Variable suffix | `Height/40` → `--annachy-size-height-40`; `Radius/8` → `--annachy-radius-8`; `Border/S` → `--annachy-border-width-s` |
| `grid-<class>-<prop>` | Grid class + property | `--annachy-grid-desktop-margin` |
| `shadow-scale-*`, `shadow-effects-*`, `effect-*`, `blur-*`, `glass-*` | Effect style path | `Shadow Effects/SM/Top Light` → `--annachy-shadow-effects-sm-top-light`; `Button/Focus` → `--annachy-effect-button-focus` |
| `compat-*` | Foreign variables | `surface-bg` → `--annachy-compat-color-surface-bg` |

Original Figma names are preserved verbatim in `tokens.json` (`figma` field) — CSS names are derived, never the reverse.

Naming collisions handled explicitly (no value change): Scale A has two "H3" rows → `h3-bold`, `h3-semibold`; two "Body S" rows → `body-s` (Regular), `body-s-semibold` (Semibold; Figma style "Body S - Semi", variables `Body/XS-Semibold`). Body XS — Semibold uses Figma variables named `XXS-Semibold`; CSS follows the **Scale A style name** (`body-xs-semibold`) to avoid colliding with Scale A "Body XXS" (10/15). All mappings recorded in `tokens.json`.

### 3.4 Typography token pattern

For each Scale A style (28):

```
--annachy-type-<style>-font-size            (active — Mobile value)
--annachy-type-<style>-line-height          (active — Mobile value)
--annachy-type-<style>-font-weight
--annachy-type-<style>-font-size-mobile     (reference)
--annachy-type-<style>-line-height-mobile   (reference)
--annachy-type-<style>-font-size-desktop    (reference — not activated; D-05/D-07)
--annachy-type-<style>-line-height-desktop  (reference — not activated)
```

Rationale: in Figma, every component resolves the Mobile column (6 of 6 cases where Mobile ≠ Desktop — `03` §4.1). Activating Desktop requires a switch width that does not exist (D-05) — R1 does not invent one. When D-05 is decided, only the *active* tokens are re-pointed inside a media query; no token is renamed.

Text-style composition (font shorthand, utility classes) belongs to **R2 base**, not R1.

### 3.5 Theming (dark-ready)

```
src/tokens/themes/light.css
  :root,
  [data-annachy-theme="light"] { …27 semantic colour tokens… }
```

- V1 ships **light only**. `dark.css` is **not created** — the full dark value set is not available (only 3 changed values observed, `13` §D-03).
- Future dark theme = a second file with `[data-annachy-theme="dark"] { … }` overriding the same 27 semantic names (and, if designed, component tokens). No consumer markup or token names change.
- The attribute name `data-annachy-theme` is an implementation convention, not a design value.

### 3.6 Cascade

`src/annachy.css` declares cascade layers so token, base and component styles never depend on file order:

```
@layer annachy.tokens, annachy.base, annachy.components;
@import url("tokens/primitives.css")       layer(annachy.tokens);
@import url("tokens/typography.css")       layer(annachy.tokens);
@import url("tokens/effects.css")          layer(annachy.tokens);
@import url("tokens/component-tokens.css") layer(annachy.tokens);
@import url("tokens/compat.css")           layer(annachy.tokens);
@import url("tokens/themes/light.css")     layer(annachy.tokens);
/* R2: base — R3+: components (added in their phases) */
```

Custom properties are unaffected by layer precedence for consumers; layers protect later base/component rules from accidental override.

---

## 4. Confirmed vs unresolved

### 4.1 Confirmed (ship in R1)

| Group | Count | Evidence |
|---|---:|---|
| Colour primitives (`Brand/Base`, `Brand/Gradient`, 8 tonal scales) | 82 | VAR/BIND |
| Semantic colours (light) | 27 | VAR/BIND |
| Button component colours (`Brand/Button/*`) | 43 | BIND (37) / VAR (6) |
| Icon-state colours | 5 | BIND/VAR |
| Typography primitives | 7 | BIND (5) / DOC (2) |
| Type styles (Scale A) × 7 properties | 28 styles | BIND (11) / DOC (17) |
| Heights | 12 | BIND |
| Radius | 11 | BIND (3) / DOC (8) |
| Border widths | 3 | VAR |
| Grid reference values | 13 | VAR (Desktop) / DOC |
| Documented shadows (+ swatch `Shadow`) | 33 | VAR |
| Component effect styles | 6 (+1 compat) | BIND |
| Blur / Glass radii / glass fills | 12 | VAR |
| Brand gradient | 1 | APPLIED |
| Compatibility values | 5 (+`shadow/sm`) | BIND |

### 4.2 Shipped with a flag (value preserved, owner confirmation pending — does not block R1)

| Token(s) | Flag |
|---|---|
| `--annachy-color-error-700` | D-02 suspected copy error |
| `--annachy-type-h3-bold-*`, `--annachy-type-h3-semibold-*` | Duplicate H3 in Figma; both preserved |
| `--annachy-type-*-desktop` | Reference only; activation pending D-05 |
| `--annachy-blur-sm-01/02`, `md-01/02` = 0px | D-11 |
| `compat.css` (all) | D-19 foreign tokens |
| `--annachy-color-button-secondary-grey-border-disabled` | Used on Pressed state (SUS-03) — value exact; usage is R3 |
| Off-palette Button state colours (`#e8f0ff`, `#f3f4f7`, `#e4e7ec`) | Exact Figma variable values; contrast notes in `09` |

### 4.3 Unresolved — not tokenised in R1

| Item | Reason | Owner |
|---|---|---|
| Spacing scale | Does not exist in Figma (D-08) | — (component-local in R3) |
| Breakpoints, tablet, max content width | Not defined (D-07) | Design owner |
| Mobile/Desktop type switch width | Not defined (D-05) | Design owner |
| Font fallback stack | Not defined (D-06) | Design owner |
| Full dark-theme values | Only partially observable (D-03: V1 light) | Design owner |
| Input radius 6 / 10 | Outside scale (D-09) | R3 |
| Opacity tokens | None in Figma | — |
| Focus-ring token | None in Figma (`05` E10; `Button/Focus` exists as an effect only) | D-21 (R2) |
| Glass refraction/depth/light parameters | Not retrievable via MCP | — (radius only) |
| Gradient paint styles `Gradient`, `Brand/Blue/Gradient/04/08/09` | Empty values | Design owner |
| Variables `S = 8`, `Radius/S = 8` | Meaning unknown | Design owner |
| Variable collection / mode names, alias chains | Not retrievable | — |

---

## 5. Module structure

### 5.1 CSS (R1 scope in bold)

```
src/
├── annachy.css                    entry — @layer declaration + @imports (R1 adds token imports)
├── tokens/
│   ├── tokens.json                **R1 — machine-readable token register (traceability)**
│   ├── primitives.css             **R1**
│   ├── typography.css             **R1**
│   ├── effects.css                **R1**
│   ├── component-tokens.css       **R1**
│   ├── compat.css                 **R1**
│   └── themes/
│       └── light.css              **R1**   (dark.css: future, not V1)
├── base/                          R2 — reset, typography classes, focus utility, font-face
├── components/<name>/             R3/R4 — <name>.css, <name>.js (interactive only), <name>.html, README.md
├── core/                          R4 — shared JS utilities
├── icons/                         R5
└── assets/fonts/                  R2 — Proxima Nova files (licence required)
```

### 5.2 `tokens.json` schema (one entry per token)

```json
{
  "css": "--annachy-color-blue-500",
  "figma": "Brand/Blue/500",
  "value": "#004feb",
  "layer": "primitive",
  "file": "primitives.css",
  "evidence": "VAR",
  "nodes": ["1557:31595"],
  "source": "docs/figma-audit/02-color.md#1.2",
  "flag": null
}
```

Optional fields: `mobile`, `desktop` (typography), `darkObserved` (semantic), `flag` (e.g. `"D-02"`).

### 5.3 JavaScript

- **R1 has no JavaScript.** Tokens are pure CSS custom properties; `src/annachy.js` remains `export {};`.
- Future (R3+, native ES modules, no bundler): `src/annachy.js` re-exports component modules; each interactive component exposes `src/components/<name>/<name>.js` with an explicit `init(root)`-style API; shared helpers in `src/core/` (focus management, keyboard, positioning). Specified in the R3/R4 specs, not here.

### 5.4 Showcase & tests (R1)

| Deliverable | Purpose |
|---|---|
| `showcase/foundations/colors.html` | Swatches for every colour token, with Figma name and value read from `tokens.json` labels |
| `showcase/foundations/typography.html` | Scale A specimen using active (Mobile) tokens; Desktop values listed as reference |
| `showcase/foundations/effects.html` | Shadow/effect specimens |
| `tests/manual/r1-token-checklist.md` | Manual verification: each CSS value equals `r1-token-mapping.md` |

---

## 6. External dependencies, files and licences

| Dependency | Status | Needed by | Blocks |
|---|---|---|---|
| **Proxima Nova font files** (400, 500, 600; 700 for Bold styles; 300 listed but unused) | **Missing** — not exportable from Figma; commercial licence (Adobe Fonts or licensed web files) | R2 base typography | **R2** (not R1 — R1 only names the family) |
| Font fallback stack | Not defined (D-06) | R2 | R2 |
| Annachy Icons File (external library, S5) | File key unknown, not accessible (D-13) | R3 icon-bearing components, R5 | R3/R5 |
| "Design System" / "UI Icons" external libraries | Ownership unverified (D-14) | Select (R4), icons | R4/R5 |
| Icon licences (Solar-derived, Iconly Pro, Lucide) | Unverified (D-15) | R5 | R5 |
| Build tools / packages | None required for R1 (native CSS) | — | — |

---

## 7. R1 work breakdown

| # | Task | Output | Acceptance |
|---|---|---|---|
| 1 | Create `tokens.json` from `r1-token-mapping.md` | `src/tokens/tokens.json` | Every mapping row present; values identical |
| 2 | Author primitives | `primitives.css` | 82 colours + font primitives + heights + radius + border widths + grid |
| 3 | Author typography | `typography.css` | 28 styles × 7 properties; active = Mobile |
| 4 | Author light theme | `themes/light.css` | 27 semantic tokens on `:root, [data-annachy-theme="light"]` |
| 5 | Author component tokens | `component-tokens.css` | 43 Button + 5 icon-state |
| 6 | Author effects | `effects.css` | 33 documented shadows, 6 component effects, blur, glass, gradient |
| 7 | Author compat | `compat.css` | 5 values + `shadow/sm`, each commented with D-19 |
| 8 | Wire entry | `src/annachy.css` | Layer declaration + imports (§3.6) |
| 9 | Foundations showcase pages | `showcase/foundations/*` | Visual check vs Figma screenshots/specs |
| 10 | Verification checklist | `tests/manual/r1-token-checklist.md` | 100 % of tokens checked against mapping |

Exit criteria (from roadmap): every token maps to a Figma variable/style or an explicit documented value; no invented values; flagged tokens listed in `tokens.json`.

---

## 8. Readiness verdict

**R1 is ready for implementation.**

All values R1 needs are either confirmed in the audit evidence or deliberately excluded by the decisions supplied (D-07, D-08). Items without owner confirmation (D-02, duplicate H3, D-05 desktop activation, D-11, D-19) are handled by preserving the exact Figma values with flags — none requires a design value to be invented.

**Genuine blockers for R1: none.**

Known limitations carried into R1 (not blockers):
- Figma alias chains and mode names are not retrievable → semantic tokens use literal values.
- Glass effects are represented by radius values only.
- Grid tokens are reference values without breakpoints.

Blockers that apply to the **next** phase (R2), for planning only:
1. **Proxima Nova font files and licence** (D-06) — required for base typography.
2. **Font fallback stack** (D-06).
3. **Focus-indicator standard** (D-21) — required for the shared focus utility.
4. **Mobile/Desktop switch width** (D-05) — required only if R2 activates Desktop type values.
