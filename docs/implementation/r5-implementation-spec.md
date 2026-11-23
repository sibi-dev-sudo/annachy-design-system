# R5 Implementation Specification — Icon Infrastructure

| Item | Value |
|---|---|
| Date | 2026-11-20 |
| Status | **Infrastructure ready; icon implementation BLOCKED** on D-12, D-13, D-14, D-15 and export approval |
| Scope of this spec | Slot contract, manifest schema and metadata, component API and integration, local pipeline architecture, validation rules. **No icon source is chosen. No icon artwork exists in the repository.** |
| Figma | Not accessed. No exports, downloads or third-party imports. `create_session` not used (its read-only behaviour is not independently verified) |
| Related | `r5-planning-proposal.md` (scope, blockers), `r5-readiness-report.md` (status), `06-iconography-assets.md`, `12-design-decision-review.md` D-12–D-15 |

Status labels: **CONFIRMED** (implemented in validated components or recorded Figma evidence) · **DEFINED** (infrastructure decision made here; reversible; no design authority required) · **BLOCKED** (needs a design-owner, access or licence decision).

---

## 1. Gates

| Gate | Question | Blocks |
|---|---|---|
| D-12 | Which source (S1–S6), which style(s), which size scale (14–42 vs 16/20/24/32/40)? | Every icon; `sizeScale`, `styles`, `categories` in the manifest |
| D-13 | Read access to the Annachy Icons File (library `lk-826bf23d…`, file key not exposed) | Evaluating / exporting S5 |
| D-14 | Ownership of "Design System" (`lk-483b…`) and "UI Icons" (`lk-c918…`) | S6 as a candidate |
| D-15 | Licences: Solar (SUS-07), Iconly Pro (commercial), Lucide (`badge-check`), brand logos | Redistribution of any icon |
| Export | Approval of read-only `download_assets` to local staging (and of `create_session` if the tool requires it) | Pipeline stage 1 |

The manifest records these gates (`decisions`); while any is `"open"` the manifest must stay `status: "blocked"` and empty (policy P01/P02, enforced by `tests/tools/r5_icons_static.py`).

## 2. Universal icon slot specification — DEFINED (derived from CONFIRMED slots)

Every component that shows an icon exposes a **slot element**; the consumer (or, after R5, the library) places one inline `<svg>` inside it.

| Rule | Specification |
|---|---|
| Element | `<span class="annachy-<component>__<slot>" aria-hidden="true">` — decorative by default |
| Size | Fixed by the slot (`inline-size` / `block-size` in px, from Figma evidence). The SVG carries **no `width`/`height`**; an unsized inline SVG with a `viewBox` fills the slot (verified in all 15 slot cases) |
| Colour | The slot sets (or inherits) `color`; artwork uses `fill="currentColor"` / `stroke="currentColor"`. State colours therefore come from the component, never from the icon file |
| Multi-tone | Duotone layers keep their `opacity` and use `currentColor` (`06` §2: "Duotone opacity preserved from source"). Such icons are flagged `multicolor: true` and must be inlined |
| Accessibility | Icon is hidden from assistive technology. **Icon-only controls** take their name from `aria-label` / `aria-labelledby` on the control (e.g. tooltip triggers, R4). Meaningful standalone icons (none today) would use `role="img"` + `aria-label` on the `<svg>` and drop `aria-hidden` |
| Focus | `focusable="false"` on the `<svg>` (legacy engines); the slot is never focusable |
| Forced colours | `currentColor` follows system colours automatically; no extra rule needed |
| Direction | Directional icons (chevrons, arrows) are not auto-mirrored; mirroring needs a per-icon `mirrorInRtl` decision (BLOCKED with D-12 — not in the schema until decided) |
| Loading | Button: the slot is hidden while `aria-busy="true"` (CONFIRMED, R3) |

### 2.1 Slot inventory (CONFIRMED sizes; verified by `tests/fixtures/r5-icon-slot-check.html`, 73 checks)

| Component | Slot class | Size | Colour | Figma source seen | Blocker |
|---|---|---|---|---|---|
| Button (all sizes) | `annachy-button__icon` | 20 × 20 | inherits label colour | S5 instance ("Home 54") | D-12/13/15 |
| Button Gradient | `annachy-button-gradient__icon` | 20 × 20 | inherits label colour | S5 | D-12/13/15 |
| Input Outline | `annachy-input__icon` | 24 × 24 | inherits | S5 (User, Chevron Up/Down) | D-12/13/15 |
| Input Outline | `annachy-input__subtext-icon` | 16 × 16 | inherits | S5 (Error circle) | D-12/13/15 |
| Input Filled | `annachy-input__icon` | 24 × 24 | `icon-state-brand` (opacity per state) | S2 (Cloud) | D-12 |
| Input Filled | `annachy-input__subtext-icon` | 14 × 14 | `icon-state-brand` | S2 | D-12 |
| Checkbox | `annachy-checkbox__glyph` | 16 (small) / 20 (medium, large) | `background-primary` | vector, image-only | **D-27** (geometry, not an icon-library icon) |
| Dropdown search | `annachy-dropdown-menu__search-icon` | 24 × 24 | inherits | S5 ("User Curved") | D-12/13/15 |
| Dropdown item | `annachy-dropdown-item__indicator` | 20 × 20 | `icon-secondary` / `blue-500` (selected) / `border-primary` (disabled) | research page; Lucide `badge-check` | D-12, D-15 (G8/G9) |
| Tooltip | `annachy-tooltip__arrow` | 20 × 20, positioned per variant | = body background | vector polygon, unspecified | **G12** (geometry) |

Radio ring and Toggle strokes (D-27) are drawn by CSS where confirmed and are **not** icon slots.

## 3. Manifest — DEFINED

Files: `src/icons/manifest.schema.json` (JSON Schema draft 2020-12) and `src/icons/manifest.json` (current: `status "blocked"`, all gates `"open"`, all lists empty).

| Field | Meaning |
|---|---|
| `status` | `blocked` (no approved source — lists must be empty) / `active` (all gates approved) |
| `decisions` | D-12, D-13, D-14, D-15, `exportApproval`: `"open"` or `{approvedBy, date, reference}` |
| `sizeScale` | Approved px sizes (D-12) |
| `styles` | Approved style slugs (D-12), e.g. `linear`, `outline` |
| `categories` | Category slugs (e.g. from the S1 catalogue's 37 categories, once a source is chosen) |
| `sources[]` | `id`, `name`, `kind` (figma-file / figma-library / owner-supplied / open-source-package), `figmaFileKey`, `figmaLibraryKey`, `owner`, `licence`, `approved` |
| `licence` | `name` (SPDX id where one exists), `url`, `redistribution` (allowed / prohibited / unknown), `attributionRequired`, `attributionText`, `evidence` |
| `icons[]` | `name` (kebab-case), `category`, `style`, `sizes`, `source`, `sourceName` (name exactly as in the source), `figmaNodeId`, `original {path, sha256}`, `normalized {path, sha256}`, `licence` (`inherit` or override), `attribution`, `multicolor`, `usedBy`, `aliases`, `deprecated` |

**Naming (N01):** icon names are lower-case kebab-case (`^[a-z0-9]+(-[a-z0-9]+)*$`). Paths are fixed by convention:
`src/icons/originals/<source-id>/<name>.svg` and `src/icons/svg/<style>/<name>.svg`. The source's own name is preserved in `sourceName`; a rename map is therefore always recoverable.

## 4. Icon component API and integration architecture — DEFINED (delivery mode partly BLOCKED)

| Layer | Design |
|---|---|
| Files | One SVG per icon per style (`src/icons/svg/<style>/<name>.svg`). Sizes are not separate files unless the source draws size-specific artwork (S2/S3 pilot model has 9 sizes — decided with D-12) |
| Default delivery | **Inline SVG inside the component slot** (copied into markup or injected by the consumer's templating). Works for single- and multi-tone icons, no network request, inherits `currentColor` |
| Optional delivery | CSS `mask-image` utility (`.annachy-icon` + `--annachy-icon-url`) for single-tone icons only. **Deferred**: depends on D-12 style (duotone sources cannot use masks) and would add CSS to `src/` — to be decided in R5-0 |
| JavaScript | None required. Components never fetch icons. (A future optional helper would read `manifest.json`; not specified until a source exists) |
| Tokens | No new tokens. Slot colours already use existing tokens; any icon-size tokens wait for the D-12 size scale |
| Components | No component CSS changes are needed to accept icons: all 15 slot cases accept an unsized SVG today. Filling the **default** icons of Button / Input / Dropdown markup is an R5-4 task after approval |
| Showcase | An "Icons" page generated from `manifest.json` (R5-4); not created while the manifest is empty |

## 5. Local pipeline architecture — DEFINED (stages 1–2 BLOCKED)

No build tools: a stdlib Python script (`tests/tools/icons_pipeline.py`, to be written in R5-3) plus the existing validator (`tests/tools/icons_lib.py`).

| Stage | Action | Gate |
|---|---|---|
| 0. Inventory | List the icons the components actually use (from recorded read-only outputs) and their candidate node IDs | none (recorded data only) |
| 1. Export | Read-only `download_assets` of **only the used icons** into a staging folder **outside the repository** (`%TEMP%/annachy-icon-staging/`) | Export approval, D-12, D-13 |
| 2. Preserve | Copy each export **byte-for-byte** to `src/icons/originals/<source>/<name>.svg`; record SHA-256 | D-14, D-15 |
| 3. Normalize | Deterministic, geometry-preserving transform → `src/icons/svg/<style>/<name>.svg`: drop root `width`/`height` (keep `viewBox`); map the single source colour to `currentColor`; keep duotone opacity; remove `id`s (and unused `defs`), comments and editor metadata. **No path simplification or re-drawing** (geometry is never altered) | — |
| 4. Validate | `icons_lib.manifest_problems()` + SVG rules (§6) + slot fixture; any failure stops the pipeline | — |
| 5. Record | Write manifest entries (hashes, provenance, licence, attribution); update `baseline.json` only after a full green regression | — |
| 6. Clean up | Delete the staging folder; verify nothing outside `src/icons/` changed | — |

Originals are never edited; normalized files are always reproducible from originals.

## 6. Validation rules — DEFINED and implemented (`tests/tools/icons_lib.py`)

| Code | Rule | Applies to |
|---|---|---|
| S | Manifest matches `manifest.schema.json` | manifest |
| P01 / P02 | `blocked` ⇒ empty lists; `active` ⇒ no open gate | manifest |
| P03 / P04 | Licence must allow redistribution; attribution text present when required | icon |
| P05 | Source exists and is approved | icon |
| P06 / P07 / P09 | Style, sizes and category are in the approved lists | icon |
| P08 | Multi-tone artwork is flagged `multicolor` | normalized |
| N01 | Path / naming convention | icon |
| D01 / D02 | No duplicate name+style; no two icons with identical artwork (whitespace- and attribute-order-independent hash) | icons |
| I01 / I02 / I03 | Hashes match; listed files exist; no orphan SVG under `src/icons/` | files |
| V01–V11 | Well-formed XML; `<svg>` root; valid `viewBox`; no root size; no script / event handlers / foreignObject / raster / external or `javascript:` references; colours only `currentColor`/`none`; no `<text>`; no `id`; no `<style>`; no DOCTYPE/entities; ≤ 16 KB | normalized (originals: V01, V02, V05, V10 only) |

Self-test: `tests/fixtures/r5-icons/` — 3 valid and 17 invalid synthetic probes (every V-rule) and 19 manifest cases (every P/D/I/N/S rule). Probes are geometric shapes written for the test, **not icon artwork**.

## 7. Test inventory

| Test | Checks | State |
|---|---:|---|
| `tests/tools/r5_icons_static.py` | 53 | PASS |
| `tests/fixtures/r5-icon-slot-check.html` | 73 | PASS |
| Pipeline round-trip (original → normalized → validate → manifest) | — | written with the pipeline (R5-3), after export approval |

## 8. Update 2026-11-20 (R7): what the Figma file now provides

| Gate | Status |
|---|---|
| D-12 source | **Resolved:** page `1801:5142` "② Icons" (Iconly-derived Outline/Filled). The size scale is XS 16 / S 20 / M 24 / L 32 / XL 40, as used by the components |
| D-13 access | **Resolved:** local components, readable with read-only tools |
| D-14 | Open: only the external libraries; no longer needed for the icons |
| D-15 licence | Open: a record of the purchased Iconly licence is needed for `sources[].licence`. The Brands category holds 624 third-party brand marks, which need their own clearance |
| Export | **Open: the only remaining blocker for artwork** |

The revised pipeline needs only export authorisation:
1. **Stage 1 (export).** Fetch the SVGs for the 5 component icon sets (Outline and Filled × 5 sizes = 50 files) plus the 62 EXACT screen icons, through read-only `download_assets` or the `get_design_context` asset URLs. They go to `%TEMP%/annachy-icon-staging/`.
2. **Stages 2–6.** Unchanged (spec §5).
3. **Slot filling.** Uses `src/icons/figma-icon-map.json`, whose 8 mappings are validated by `r5_icons_static.py`.
