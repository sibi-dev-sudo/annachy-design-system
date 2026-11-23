# 00 — Figma Audit Plan

| Item | Value |
|---|---|
| Project | `annachy-design-system` |
| Figma file | Annachy CF — Design System |
| File key | `rM3ixSG6i3DFfKZFWuxzs4` |
| Entry URL | https://www.figma.com/design/rM3ixSG6i3DFfKZFWuxzs4/Annachy-CF----Design-System-?node-id=375-10891 |
| Entry node | `375:10891` |
| Expected pages | 39 (to be verified in Phase 3) |
| Access mode | **Read-only** via the official Figma MCP server |
| Plan status | Approved 2026-11-19 · **Audit complete** (Phases 1–6, decision reviews `12`–`13`, corrections applied) — awaiting design-owner decisions and implementation approval (updated 2026-11-19) |

---

## 1. Objective

Produce a complete, evidence-based record of the Annachy Figma design system (foundations, components, patterns, assets) to serve as the single specification for a vanilla HTML/CSS/JS component library. No implementation begins until this audit is approved.

## 2. Read-Only Policy

The original Figma file must never be modified.

### 2.1 Tools permitted (read-only)

| Tool | Purpose |
|---|---|
| `whoami` | Confirm the authenticated account and plan/seat (affects rate limits). |
| ~~`create_session`~~ | **Not used.** Its definition ("record the user's current work") does not prove it is free of server-side writes, so it is skipped per the strict read-only rule. All read tools work without a `sessionId`. |
| `get_metadata` | Page/frame/node tree: names, IDs, types, positions, sizes. Used for inventory and sectioning. |
| `get_variable_defs` | Variables and styles (colour, typography, spacing, radius, effects) bound to a node. |
| `get_design_context` | Detailed node styling and structure (reference code output is used as **data only**, never copied as implementation). |
| `get_screenshot` | Visual reference captures, saved to `screenshots/`. |
| `search_design_system` | Locate components, variables and styles across the file and linked libraries. |
| `get_libraries` | Identify linked/published libraries the file depends on. |
| `get_comments` | Read designer annotations/notes that may carry specs or decisions. |
| `get_code_connect_map` | Read any existing component-to-code mappings (expected to be none). |
| `download_assets` | Schema reviewed: inputs are fileKey/nodeId/optional format+scale; returns temporary download URLs; no upload or edit inputs. Will be used **without** `defaultFormat`/`defaultScale` (those "override" node export settings — wording ambiguous, so avoided). Staging: `docs/figma-audit/raw/assets/`. |

### 2.2 Tools prohibited (write-capable)

`use_figma`, `generate_figma_design`, `send_code_to_figma`, `upload_assets`, `create_branch`, `create_new_file`, `add_code_connect_map`, `send_code_connect_mappings`, `generate_diagram`, `generate_image`, `generate_vector_illustration`, `create_shader`, `update_shader`, `create_generative_plugin`, `update_generative_plugin`, `export_video`, all `weave_*` tools, and any other tool that creates, edits, moves, deletes, publishes or uploads.

If any read tool turns out to have side effects, its use stops immediately and the issue is reported.

## 3. Scope

All pages in the file, classified into five groups. Exact page-to-group mapping is produced in Phase 3 (`01-file-inventory.md`) — none is assumed here.

| Group | Expected contents | Primary reports |
|---|---|---|
| A. Research | Research, references, explorations | `01` (inventory only; not specification) |
| B. Foundations | Colours, Typography, Iconography, Grid & Layout, Radius, Shadows, Blur | `02`–`06` |
| C. Components | Button, Input, Input Dropdown, Checkbox, Radio, Toggle, Tooltip, Navigation, plus any others discovered | `07`, `components/*.md` |
| D. Patterns & Screens | Composed patterns, example screens | `01`, `07` (usage/relationships) |
| E. Archive | Deprecated or superseded work | `01`, `08` (never treated as current without evidence) |

## 4. Method

### Phase 3 — Pages & Foundations
1. `whoami` → confirm access and rate-limit tier.
2. ~~`create_session`~~ — skipped (see §2.1).
3. `get_metadata` at document level → list every page (name, node ID, top-level frames). Verify page count against the expected 39.
4. Classify each page into groups A–E; record in `01-file-inventory.md`.
5. For each Foundations page: `get_variable_defs` + `get_design_context` on each foundation frame; capture screenshots.
6. Record variable collections, modes (e.g. light/dark), names and resolved values.

### Phase 4 — Components
1. For each component page: `get_metadata` → list component sets, variants, node IDs.
2. Large pages are processed **frame by frame** (one component set at a time) to avoid truncated responses.
3. For each component set: `get_design_context` + `get_variable_defs` on the set and on representative variants per state.
4. Write one `components/<name>.md` per component, then summarise in `07-component-inventory.md`.

### Phase 5 — Assets & Inconsistencies
1. Inventory icons, logos, illustrations, images and fonts with original names/categories.
2. Download original SVG artwork locally (staging only — not into `src/icons/` until approved).
3. Cross-check components against foundations to find hardcoded values, detached styles, duplicates, naming drift and missing states.

### Phase 6 — Reporting
Complete reports `01`–`10`, including the implementation roadmap in `10-summary-and-roadmap.md` *(file reference updated 2026-11-19; originally `10-audit-summary.md`, now a pointer)*.

### Phase 7 — Approval gate
Stop. No tokens, components, CSS or JS are written until explicit approval.

## 5. Data Captured

### Foundations
- Colour: variable names, collections, modes, hex/RGBA values, aliasing chains (semantic → primitive).
- Typography: families, sizes, weights, line heights, letter spacing, text styles.
- Spacing, grid & layout: spacing scale, layout grids (columns, gutters, margins), breakpoints.
- Radius, borders, opacity.
- Shadows (x, y, blur, spread, colour), blur effects.

### Per component
- Name, description, component set, node ID, source page.
- Variant properties and values; boolean/instance-swap/text properties.
- States: default, hover, focus, active, disabled, error (and any others present). Missing states are recorded, not invented.
- Dimensions, padding, gaps, auto-layout settings.
- Colours, typography, radius, effects — with the token/variable bound, or flagged as hardcoded.
- Dependencies: nested component instances (e.g. icons inside buttons).

### Assets
- SVG icons, logos, images, fonts — original names, categories, sizes, node IDs.

## 6. Evidence & Accuracy Rules

Every recorded value is tagged with its provenance:

| Tag | Meaning |
|---|---|
| **[EXTRACTED]** | Value returned directly by a Figma MCP tool. Node ID cited. |
| **[DERIVED]** | Computed from extracted values (e.g. contrast ratio). Method stated. |
| **[VISUAL]** | Observed from a screenshot only; not confirmed by data. |
| **[MISSING]** | Specification not present in Figma. |
| **[INACCESSIBLE]** | Node/page could not be read; error recorded. |

- Values are never invented. Gaps are recorded as `[MISSING]`.
- Archive content is labelled as archive and excluded from the current spec unless evidence shows it is in use.
- Duplicate or conflicting definitions are listed side by side in `08-inconsistencies.md`.

## 7. Output Layout

```
docs/figma-audit/
├── 00-audit-plan.md            this document
├── 01-file-inventory.md        all pages, groups, node IDs, access status
├── 02-color.md                 colour variables, collections, modes
├── 03-typography.md            type families, scale, text styles
├── 04-spacing-layout.md        spacing, grid, breakpoints, radius
├── 05-elevation-effects.md     shadows, blur, borders, opacity
├── 06-iconography-assets.md    icons, logos, images, fonts
├── 07-component-inventory.md   all components, variants, states (summary)
├── 08-inconsistencies.md       duplicates, hardcoded values, naming drift, missing specs
├── 09-accessibility.md         contrast, focus, target size, state coverage
├── 10-audit-summary.md         pointer → 10-summary-and-roadmap.md
├── 10-summary-and-roadmap.md   findings, confirmed specs vs assumptions, decisions, roadmap
├── 11-dependencies-and-sources.md  icon sources, external libraries, nested deps, missing masters
├── 12-design-decision-review.md    27 open decisions (D-01…D-27) + B-01, R1/R2 gating
├── 13-global-token-decisions.md    evidence review for D-01…D-08
├── audit-progress-log.md       chronological log of all audit steps
├── raw/                        raw evidence (metadata XML, effects.json, variant matrices, archive diff)
├── components/                 one detailed spec per component
└── screenshots/                reference captures (<page>__<node-id>.png)
```

Mapping to required deliverables:

| # | Required deliverable | File(s) |
|---|---|---|
| 1 | File and page inventory | `01` |
| 2 | Design token documentation | `02`, `04`, `05` |
| 3 | Typography documentation | `03` |
| 4 | Component inventory | `07` |
| 5 | Component variants and states | `components/*.md` |
| 6 | Asset inventory | `06` |
| 7 | Inconsistency report | `08` |
| 8 | Accessibility observations | `09` |
| 9 | Final audit summary | `10-summary-and-roadmap.md` |
| 10 | Implementation roadmap | `10-summary-and-roadmap.md` §7 |
| + | Dependencies & source investigation | `11-dependencies-and-sources.md` |
| + | Design decision review | `12-design-decision-review.md` |
| + | Global token decision evidence | `13-global-token-decisions.md` |
| + | Progress log | `audit-progress-log.md` |

*Output layout and deliverable mapping updated 2026-11-19 to reflect the final deliverables; `10-audit-summary.md` is retained as a pointer to `10-summary-and-roadmap.md`.*

Detailed raw findings are written to these files progressively, not printed to the terminal.

## 8. Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Figma MCP rate limits (depend on plan/seat) | Check with `whoami`; batch by page; resume from last completed page recorded in `01`. |
| Very large pages truncate responses | Use `get_metadata` first, then inspect frame by frame. |
| Variables from external libraries not resolvable | Record with `get_libraries`; mark unresolved values `[INACCESSIBLE]`. |
| Screenshots inflate repo size (OneDrive-synced folder) | Capture only one representative per component set/foundation frame. |
| Archive pages mistaken for current | Classify pages before inspecting components; cross-reference usage. |

## 9. Approval

- [ ] Plan approved — proceed with Phases 3–6.
