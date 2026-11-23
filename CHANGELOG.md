# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- Project folder structure.
- Figma audit plan (`docs/figma-audit/00-audit-plan.md`).
- Phase 3: complete page inventory of all 39 Figma pages (`docs/figma-audit/01-file-inventory.md`), raw metadata evidence in `docs/figma-audit/raw/`.
- Phase 3 foundations audit: colour, typography, spacing/grid/radius, elevation/effects, iconography (`docs/figma-audit/02`–`06`).
- Phase 4 component audit: specs for Button, Input, Dropdown, Checkbox, Radio, Toggle, Selection Controls, Tooltip, Navigation (gap) in `docs/figma-audit/components/`; `07-component-inventory.md`; `audit-progress-log.md`.
- Phase 5 dependency & source investigation (`docs/figma-audit/11-dependencies-and-sources.md`); corrections to 01, 06, 07 and component specs.
- Phase 6 final audit reports: `08-inconsistencies.md`, `09-accessibility.md`, `10-summary-and-roadmap.md` (`10-audit-summary.md` now a pointer). Audit complete, awaiting approval.
- Design decision review (`docs/figma-audit/12-design-decision-review.md`).
- Global token decision evidence review (`docs/figma-audit/13-global-token-decisions.md`).

### Changed
- Audit reports corrected per `13-global-token-decisions.md` (dated correction notes, originals preserved): `01`, `02`, `03`, `04`, `07`, `08`, `10`, `12`, `13`. Inconsistency totals now 58 confirmed / 16 suspected.
- Remaining documentation corrections (dated notes, originals preserved): `components/input.md`, `01`, `05`, `06`, `10`, `12`, `13`.
- Housekeeping: icon source naming standardised to S5; `00-audit-plan.md` deliverables updated to include reports 10–13. Audit complete — awaiting design-owner decisions.

### Added (planning)
- R1 implementation specification and token mapping (`docs/implementation/`). No tokens or CSS created yet.

## [0.1.0-r1] — 2026-11-19

### Added
- R1 design tokens from the Figma source of truth: `src/tokens/tokens.json` (457 tokens), `primitives.css`, `typography.css`, `effects.css`, `component-tokens.css`, `compat.css`, `themes/light.css`.
- Cascade layers (`annachy.tokens`, `annachy.base`, `annachy.components`) and token imports in `src/annachy.css`.
- Foundations showcase: `showcase/showcase.css`, `showcase/foundations/` (colours, typography, effects, grid, dimensions).
- Browser token check `tests/fixtures/r1-token-check.html` and manual checklist `tests/manual/r1-token-checklist.md`.

### Changed
- `showcase/index.html` links the foundations pages.
- `docs/implementation/r1-token-mapping.md`: H3 Semibold note now carries the D-04 flag ID (no value change).

## [0.2.0-r2] — 2026-11-19

### Added
- R2 base styles in layer `annachy.base`: `src/base/reset.css`, `document.css` (Body M defaults, semantic colours, temporary system-font render fallback — not a Proxima Nova replacement), `typography.css` (28 `.annachy-text-*` classes, Mobile values), `utilities.css` (61 token utilities + `.annachy-visually-hidden`).
- `docs/implementation/r2-base-spec.md`, `showcase/foundations/base.html`, `tests/fixtures/r2-base-check.html`.

### Changed
- `src/annachy.css` imports the four base files after the token imports.
- Foundations showcase pages link the base page; typography samples use the text classes; `showcase/showcase.css` no longer overrides the body font.
- Manual checklist extended with an R2 section.

### Not changed
- All 457 R1 tokens (re-validated). No global focus style, no fonts, no spacing/breakpoint utilities.

### Added (planning)
- R3 core-controls implementation plan (`docs/implementation/r3-components-spec.md`). No component code yet.

### Added (R3-0 evidence)
- `docs/figma-audit/r3-0-evidence.md`: read-only Figma evidence for Button, gradient Button, Input, Checkbox, Radio, Toggle and the Selection Controls wrapper (79 read-only calls; no writes, no exports).

### Changed (R3-0)
- `docs/implementation/r3-components-spec.md`: gaps resolved, B-01 approved, D-20 recommendation (not a Figma spec), R3-0a token addendum step (7 Loading variables), readiness updated.
- `docs/figma-audit/12-design-decision-review.md`, `audit-progress-log.md`, component specs: dated R3-0 notes.
- No source, token or showcase files changed. No component code.

## [0.3.0-r3.1] — 2026-11-19

### Added
- R3-0a: 7 Button Loading colour tokens (`--annachy-color-button-{secondary,secondary-grey}-{content,background}-loading`, `--annachy-color-button-{tertiary,tertiary-grey,link}-content-loading`); total 464.
- R3-1 Button (All Buttons, 432 variants): `src/components/button/button.css`, `button.html`, `README.md`; `showcase/components/button.html`; `tests/fixtures/r3-button-check.html`.
- R3-0b evidence (`docs/figma-audit/r3-0-evidence.md` §17–§21).

### Changed
- `src/annachy.css` imports the Button in `annachy.components`.
- R2 fixture invariants scoped to tokens and base; checklist §7 added; token counts updated (464).

## [0.3.1-r3.2] — 2026-11-19

### Added
- R3-2 Button (gradient), 55 variants: `src/components/button-gradient/` (css, html, README), `showcase/components/button-gradient.html`, `tests/fixtures/r3-button-gradient-check.html`.
- R3-0c evidence: all 55 gradient variants (`r3-0-evidence.md` §22).

### Changed
- `src/annachy.css` imports the gradient button in `annachy.components`; showcase index and Button page link it.

## [0.3.2-r3.3] — 2026-11-19

### Added
- R3-3 Input Field (Outline 150 + Filled 175 variants): `src/components/input/` (css, html, README), `showcase/components/input.html`, `tests/fixtures/r3-input-check.html`.
- R3-0d evidence (`r3-0-evidence.md` §23).

### Changed
- `src/annachy.css` imports the Input in `annachy.components`; showcase navigation links it.
- Input state selectors use `:where()` so the documented precedence holds (fixes Success-over-Error and forced Focus-over-Filled).
- `09-accessibility.md`: A38 added (Filled Hover placeholder 2.46:1, confirmed).

## [0.4.0-r3] — 2026-11-19

### Added
- R3-4 Checkbox (126 variants): `src/components/checkbox/` (css, `checkbox.js` for indeterminate, html, README), `showcase/components/checkbox.html`, `tests/fixtures/r3-checkbox-check.html`.
- R3-5 Radio (108): `src/components/radio/`, `showcase/components/radio.html`, `tests/fixtures/r3-radio-check.html`.
- R3-6 Toggle (180): `src/components/toggle/`, `showcase/components/toggle.html`, `tests/fixtures/r3-toggle-check.html`.
- `src/components/selection-controls/README.md` (wrapper = Small variants, no CSS).
- Evidence `r3-0-evidence.md` §24–§26; `09-accessibility.md` A39.

### Changed
- `src/annachy.css` imports checkbox, radio and toggle; `src/annachy.js` re-exports `initCheckboxes`.
- Showcase index and navigation link all component pages.

## [0.4.1-r3-closure] — 2026-11-19

### Added
- `docs/implementation/r3-closure-report.md`; `docs/implementation/r4-components-spec.md` (plan only, no R4 code).
- `tests/fixtures/r3-interaction.html`: a real keyboard / mouse / accessibility-tree fixture for the closure audit.
- `r3-0-evidence.md` §23.5 (Input element node index).

### Changed
- Button and Input READMEs list evidence sections explicitly; the Button README documents BTN-3 (guard clicks on Loading buttons).

### Added (R4 planning)
- `docs/implementation/r4-behaviour-spec.md`: draft R4 behaviour specification for approval (no code).

### Added (R4-0)
- `docs/figma-audit/r4-0-evidence.md`; R4 behaviour spec and plan updated with approvals and readiness (no code).

## [0.5.0-r4] — 2026-11-20

### Added
- R4-1 Dropdown (Light, Footer=None: 20 Item + 8 Menu variants): `src/components/dropdown/` (css, `dropdown.js`, html, README), `showcase/components/dropdown.html`, `tests/fixtures/r4-dropdown-check.html`, `tests/fixtures/r4-dropdown-interaction.html`.
- R4-2 Tooltip (80 variants): `src/components/tooltip/` (css, `tooltip.js`, html, README), `showcase/components/tooltip.html`, `tests/fixtures/r4-tooltip-check.html`, `tests/fixtures/r4-tooltip-interaction.html`.
- `src/annachy.js` exports `initDropdowns` and `initTooltips`; `src/annachy.css` imports both stylesheets in `annachy.components`.
- `docs/implementation/r4-completion-report.md`; `09-accessibility.md` A40 and A41.

### Not implemented (blocked)
- Footer Dropdown (R4-Q3), Dark theme (B4-2), Select (B4-1), tooltip arrow glyph (G12), research-page icons (G8 / G9).

## [0.5.1-r4-closure] — 2026-11-20

### Added (documentation only; no source changes)
- `docs/implementation/r4-final-closure-audit.md`: R4 CLOSED, PASS. AUD-1 (Dropdown listener teardown) is open for decision.
- `docs/implementation/r5-planning-proposal.md`: R5 icons proposal (not started).
- `docs/figma-audit/r4-0-evidence.md` §7: element node index (AUD-2).

## [0.6.0-r5-infra] — 2026-11-20

### Added
- Dropdown lifecycle API (AUD-1): `destroyDropdowns(root)`, `getDropdown(el)` and `controller.destroy()`, exported from `src/annachy.js`. The `initDropdowns` API is unchanged.
- `tests/tools/` (AUD-3): validators, real-input drivers, the integrity baseline (`baseline.json`), the sequential runner (`run_all.py`) and the guarded mutation runner (`mutate.py`, 19 mutants, crash recovery); README with commands.
- `tests/tools/r4_dropdown_lifecycle_cdp.py`: listener-count and garbage-collection regression test (40 checks).
- R5 infrastructure: `src/icons/manifest.schema.json`, `src/icons/manifest.json` (blocked, empty) and `src/icons/README.md`; `tests/tools/icons_lib.py` and `r5_icons_static.py`; `tests/fixtures/r5-icon-slot-check.html`; `tests/fixtures/r5-icons/` (synthetic probes, not icons).
- Docs: `r5-implementation-spec.md`, `r5-readiness-report.md`.

### Changed
- `dropdown.js`: the outside-click document listener is registered only while a dropdown is open (previously one listener per dropdown, never removed).
- Test harnesses delete their temporary Chrome profiles and write no bytecode cache.
- README status table corrected (it previously said components were not yet built).

### Not done (blocked)
- Icon source, export and artwork: D-12, D-13, D-14, D-15 and export approval.

## [0.7.0-replication] — 2026-11-20

### Added
- **Dropdown: Theme=Dark and Footer.** Adds 20 Item + 40 Menu variants, so all 88 Dropdown variants are now implemented.
  - `src/tokens/themes/dark.css`: the Brand Dark-mode values Figma defines, re-mapping existing names under `data-annachy-theme="dark"`.
  - Dark Selected bindings.
  - Footer: an R3 Primary Button with the label typography override.
  - Staged-commit behaviour (R4-Q3 decided): Apply commits; Escape, outside click or Tab-out discard.
  - Evidence: `docs/figma-audit/r6-0-evidence.md` (15 read-only calls).
- Tests:
  - `tests/fixtures/r6-dropdown-check.html` (757 checks);
  - `tests/tools/r6_dropdown_footer_cdp.py` (38);
  - 5 new mutants, 24 in total.
- Pattern screens in `showcase/screens/`:
  - Sample Screen: 5 frames, 1,363 checks;
  - PDP: 3 frames, 303 checks;
  - exact-size placeholders for images and icons.
- Showcase:
  - searchable, filterable catalogue (`showcase/index.html` + `index.js`);
  - Iconography foundation page;
  - Dropdown Dark/Footer section with live demos and markup;
  - `tests/tools/showcase_catalogue_cdp.py`.
- `docs/replication/`:
  - source inventory;
  - traceability matrix and coverage;
  - screens and showcase;
  - gaps and blockers;
  - icon inventory and Iconly mapping;
  - final regression report.

### Changed
- The V1 "Light only" rule (D-03) is superseded. Validators and the R1/R2 fixtures now accept `dark.css` only as a re-map of existing light-theme token names.
- README status rewritten.

### Blocked
- Icon artwork (no Iconly access), image and logo assets (export not authorised), and the Proxima Nova font.

## [0.7.1-icons-identified] — 2026-11-20

### Added
- `docs/figma-audit/r7-0-iconography-evidence.md` + `r7-0-iconography-inventory.json`. These are a read-only inventory of the new Figma page `1801:5142` "② Icons": 5,128 sets, 35,890 variants, Outline/Filled × XS–XL, Iconly-derived. They also re-check the Iconography page `375:10889` (unchanged) and map all 362 screen placeholders.
- `src/icons/figma-icon-map.json`: 8 component icon slots mapped to local Figma icon sets, plus 5 documented exceptions. It is validated by `r5_icons_static.py` (now 87 checks).

### Changed
- Manifest: D-12 (source) and D-13 (access) recorded as resolved. It stays `blocked` while export authorisation and D-15 (licence record) are open.
- Docs 01, 02, 04 and 05, the R5 spec §8, and the Iconography showcase page now reflect the new evidence.

## [0.8.0-icons] — 2026-11-20

### Added
- **Icons (R7-1).** Approved export of Figma page `1801:5142`, for internal use only.
  - Byte-preserved category originals, plus 6,890 normalised SVGs: `src/icons/svg/`, and the restricted Brands in `restricted/brands/`.
  - `src/icons/catalogue.json`, an active manifest (schema extensions E1–E8) and the pipeline scripts `tests/tools/icons_export/`.
- `src/icons/icons.js`: `fillIconSlots()`, `loadIcon()` and `iconUrl()`, using `data-annachy-icon` / `data-annachy-icon-style`.
- `showcase/icons/`: the full icon catalogue. `showcase/icon-slots.js` fills the mapped component slots on the showcase pages.
- Screens: 32 exact icon placeholders (34 elements) render their library icons.
- Tests:
  - `r7_icons_static.py` (7,292 checks);
  - `r7_icon_catalogue_cdp.py` (20);
  - `r7_icon_fidelity_cdp.py`, a vector pixel comparison against the Figma originals.

### Changed
- The R4 closure audit now permits SVG artwork under `src/icons/` only, and excludes icon data from its framework-word scan.
- The screen fixtures verify filled icons instead of requiring empty placeholders.
- The showcase catalogue test reflects the active manifest.

## [0.8.1-verification] — 2026-11-20

### Added
- Memory-safe, resumable icon pixel-fidelity verification (`r7_icon_fidelity_cdp.py`): 7,105 variants, negative controls, 2× → 8× re-examination. 5 Figma defects (FIG-ICON-1) flagged in `catalogue.json` and in the catalogue UI.
- `tests/tools/showcase_crawl_cdp.py`: every showcase page, its links, icons and Dark regions.
- `docs/figma-audit/r8-0-remaining-assets.{md,json}`: exact sources for all 328 remaining screen placeholders and the consolidated export requirement.
- `docs/replication/07-licences-and-fonts.md`, `08-final-completion-report.md`.

### Fixed
- `src/icons/icons.js`: a failed icon load is no longer cached; it retries once and fills each slot independently, with `data-annachy-icon-error` on a slot that still fails.

## [0.9.0-r10-vectors] — 2026-11-20

### Added
- `showcase/screens/assets/vectors/`: 28 original structural-vector SVGs exported from Figma (approved R10-0), placed in 50 screen placeholders using Figma's own insets and rotation.
- `tests/tools/r10_integrate_vectors.py` (idempotent integration that refuses to overwrite) and `tests/tools/r10_vector_fidelity_once.py` (a one-time integrity and fidelity check that needs the export staging folder).

### Changed
- The screen fixtures verify placed vectors strictly: the declared artwork, loaded, at the exact exported size.
- The screen CSS gained placement rules for vectors (additive only).

## [0.10.0-r11-imagery] — 2026-11-20

### Added
- `showcase/screens/assets/images/`: 52 original Figma image files (38 PNG, 5 JPEG, 9 SVG; byte-identical, not re-compressed), approved R11-0. **Internal use only**: the folder README records each file's source and rights status (unverified).
- All 108 R11 placeholders filled.
  - 103 use Figma's own image wrappers (crops, offsets, stacked colour variants, instance scaling, ribbon rotation).
  - 5 are CSS-only fills.
  - Each image placeholder has `data-annachy-image`, `data-img-layers` and `data-img-rights`.
- Tools:
  - `tests/tools/r11_jsx.py`: reads Figma design-context JSX and converts its Tailwind classes;
  - `tests/tools/r11_integrate_images.py`: idempotent, refuses to overwrite, has a `--refill` mode;
  - `tests/tools/r11_image_fidelity_once.py`: one-time check against Figma's originals and renders;
  - `tests/tools/r11_image_geometry.py`: records the geometry lock.
- `tests/fixtures/r11-image-geometry.json`: 112 image layers, 0.1 px.
- Mutants R11-SRC, R11-CROP, R11-SCALE and R11-OVL.
- `docs/figma-audit/r11-0-image-fidelity-results.json`.

### Changed
- Screen fixtures verify R11 images: only the declared files, all loaded, layer count, rights status and geometry. They now await the icon loader instead of relying on virtual-time polling alone; that polling was flaky on the heavier pages.
- Mobile PDP review photo (`1608:7370`): the overlay `1608:7372` is positioned against the image node as in Figma (it was against the clipping box), and the "+10" group `1608:7373` was added.
- Screen CSS: additive R11 rules (`.scr-asset[data-annachy-image]`, `.scr-img__box`, `.scr-img__art`).
- `docs/figma-audit/r11-0-product-imagery-manifest.*`: implementation record, plus dated corrections of two audit observations (ribbon offset, cards).

## [1.0.0-closure] — 2026-11-20

### Added
- **Screen icons and logotype.** 37 original Figma SVGs in `showcase/screens/assets/vectors/` (`icon-*.svg`, `logo-annachy-b8420.svg`) fill the 50 remaining in-scope icon placeholders and the Annachy logotype. Placement uses Figma's insets, and the mirror, flip and −90° transforms come from the parents' design context. One exact library icon is reused (`editor-hamburger-menu`).
- **Reuse of existing artwork.** The 7 desktop card stars use the R10 star (`c6cc8`, same Figma artwork as the mobile cards); the desktop badge uses R11 artwork `73565`.
- **Web copies.** `showcase/screens/assets/images-web/` holds 43 WebP copies (2.7 MB) and a manifest. 42 are in use after A/B verification at real display sizes; screen image weight is −88.5 %. The originals are byte-identical.
- **Tools:**
  - `closure_optimize_images.py`, `closure_web_images_ab.py`, `closure_image_weight.py`;
  - `closure_icon_match.py`, `closure_integrate_icons.py`;
  - `closure_a11y_cdp.py` (34th regression suite).
- **Mutants:** CL-ICON and CL-FOCUS.
- **Reports:** `docs/replication/FINAL-PROJECT-COMPLETION-REPORT.md`, `FINAL-PENDING-ITEMS.md`, `FINAL-TEST-REPORT.md`, `FINAL-DESIGN-TEAM-ACTION-LIST.md`.
- **Evidence:** `docs/replication/closure-*.json`.

### Fixed
- Library icons in the screens no longer show placeholder chrome (dashed outline or inset border); this was a gap since R7.
- PDP V1 delivery field: an instance border override hid the Figma Focused border, so keyboard focus is visible again. The default rendering is unchanged.

### Changed
- The screen fixtures accept a web copy only when it is linked (`data-img-original`) to its declared original. The geometry lock is unchanged.
- The R11-SRC and R11-SCALE mutant anchors now follow the web-copy references.

## [1.2.0-inter-font]
- Font: the design team confirmed **Inter**. Self-hosted `src/assets/fonts/inter/InterVariable.woff2` (SIL OFL, `OFL.txt` alongside) with an `@font-face` in `src/base/document.css`; `--annachy-base-font-family-render` is now `"Inter", system-ui, sans-serif`.
- R1 token `--annachy-font-family-sans` is unchanged (`"Proxima Nova"`, the Figma value); Figma should be updated to match.
- Checkout prototype round 2 (live-storefront look) supersedes the round-1 entry below.
- Tests: assertions for the Proxima stack updated to Inter; the Figma-geometry suites (checkbox/radio/toggle, Sample Screen, PDP) measure with system-ui metrics because Inter is wider than the fonts those sizes were calibrated on.

## [1.1.0-checkout-round1] — 2026-11-23

### Added
- `showcase/screens/checkout/`: Mixed-cart checkout from the design brief.
  - Two directions (A "Stacked shipments", B "Side by side") of Cart, Delivery & payment and Confirmation, at mobile 390 and desktop 1440.
  - Interactive, with the brief's edge cases (`?scenario=`).
  - Built only from tokens and core components (Button, Button Gradient, Radio, Toggle, library icons).
  - Review board: `index.html`; README with UX-law mapping and design-system gaps.
- `tests/tools/checkout_proto_cdp.py` (35th regression suite): 91 checks across both directions.
- Showcase catalogue card (category "prototype").
