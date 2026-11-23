# R5 Planning Proposal — Icons

| Item | Value |
|---|---|
| Date | 2026-11-20 |
| Status | Proposal. **Update 2026-11-20:** the approval-free work in §5 is now done (see §7). Icon implementation remains blocked. No Figma access, exports or downloads. |
| Roadmap definition | "R5 — Icons: icon export (read-only `download_assets`, local staging) and SVG pipeline · D-12, D-13, D-15 · explicit export approval · `src/icons/` (original SVG preserved), icon usage docs · exit: single approved source; licences recorded" (`10-summary-and-roadmap.md` §R5) |
| Prerequisite | R4 closed (see `r4-final-closure-audit.md`) ✅ |

---

## 1. Blockers: icon source and licensing

| ID | Decision | Current evidence | Who decides | What it blocks |
|---|---|---|---|---|
| **D-12** | Canonical icon source and size scale | Six candidates. **S1** Iconography catalogue (1,243 slots, 24 px). **S2** Iconography pilots (52 icons; Style 6 × Size 9 × state 5; used by Input/Filled). **S3** Archive Component Source (240 icons, same matrix). **S4** Brainstorming (Lucide etc.; `badge-check` in Dropdown). **S5** external "Annachy Icons File" (used by Button, Input/Outline, Dropdown; XS 16 to XL 40). **S6** external "UI Icons" (no observed use). Two conflicting size scales: 14–42 (S2/S3) vs 16/20/24/32/40 (S5). **No source is recommended.** | Design owner | Everything that ships an SVG |
| **D-13** | Access to the Annachy Icons File | Library key `lk-826bf23d…`; file key not exposed; masters are hidden internal copies. It can't be inspected or exported | Access/admin (provide file URL/key with read access) | Any evaluation of S5. D-12 would otherwise be decided on incomplete data |
| **D-14** | Ownership of the "Design System" and "UI Icons" libraries | Neither is linked to the file; ownership can't be determined | Design owner | S6 as a candidate; also D-10 / D-17 (Select) |
| **D-15** | Licences | Iconography names match the public **Solar** set (SUS-07); **Iconly Pro** (commercial) frames; **Lucide** `badge-check` in Dropdown; Amazon/Flipkart logos on research pages | Legal + design owner | Redistributing any icon in this library |
| **Export approval** | `download_assets` (and D-27) | Explicitly **not approved** (R3 and R4 instructions). It is the only route from Figma to SVG in the roadmap | User / design owner | Pipeline step 2 onward |

**Tool note:** the Figma MCP server advises calling `create_session` before file tools. This project has never used it: its read-only nature isn't confirmed, and the immutability rule says "do not execute any operation if its read-only nature is uncertain". Any R5 step that needs it also needs explicit approval.

## 2. Missing icon assets and geometry (current empty slots)

Every slot below is already implemented as an **empty, sized, `aria-hidden` slot** with its state colour wired through `currentColor`. Nothing is invented.

| Component | Slot | Size (confirmed) | Source seen in Figma | Blocker |
|---|---|---|---|---|
| Button (R3) | leading / trailing / icon-only | per size (from evidence) | S5 instances | D-12, D-13, D-15 |
| Input (R3) | User, chevrons, error circle, cloud | 24 / per evidence | S2 (Filled) and S5 (Outline): **two sources in one component** | D-12 |
| Checkbox (R3) | check and indeterminate glyphs | box confirmed; glyph image-only | Vector image only | **D-27** (geometry / export) |
| Radio (R3) | selected ring / dot | outer confirmed; inner image-only | Vector image only | **D-27** |
| Toggle (R3) | knob radius / strokes (TG-1) | track confirmed | Vector image only | **D-27** |
| Dropdown (R4) | search icon | 24 × 24 | S5 | D-12 |
| Dropdown (R4) | Single check / Multiple indicator (G8 / G9) | 20 × 20 | Research-page assets; Lucide `badge-check` | D-12, D-15 |
| Tooltip (R4) | arrow polygon (G12) | 20 × 20 slot, per-variant transform confirmed | Vector only; polygon not specified | Owner geometry, or export approval |

**Note:** D-27 and G12 are *component geometry*, not icon-library icons. They could be resolved by an owner-supplied specification (path data or dimensions) **without** adopting an icon source.

## 3. External library access needed

1. **Annachy Icons File (S5):** a file URL or key, with read access granted to the account used for the read-only tools (D-13).
2. **"Design System" (`lk-483b…`) and "UI Icons" (`lk-c918…`):** an ownership statement. If either is a candidate, also its file key and read access (D-14).
3. **Licence records** for Solar, Iconly Pro and Lucide (and a ruling on the brand logos): licence text, attribution requirements, and permission to redistribute in this library (D-15).

## 4. Proposed R5 scope and dependencies

| Step | Work | Depends on |
|---|---|---|
| R5-0 | Decision record: the chosen source, one size scale, the style (e.g. Linear / Outline), the licence and attribution | D-12, D-14, D-15 |
| R5-1 | Read-only inventory of the chosen source: names, node IDs, sizes and styles, **used-by-components first** | D-13 (if S5); read-only tools |
| R5-2 | Export of only the icons the components use, to local staging, with the original SVG preserved byte-for-byte | **Explicit export approval** (`download_assets`) |
| R5-3 | SVG pipeline, vanilla with no build tools: a documented normalisation step (`currentColor`, `viewBox` kept, no inline sizes), originals kept next to the normalised files, a manifest (name → node ID → licence) | R5-2 |
| R5-4 | Fill the existing slots (Button, Input, Dropdown); validate size, colour per state and rendering; full regression | R5-3 |
| R5-5 | D-27 / G12 geometry, only if the owner provides a spec or export is approved | Owner decision |

**Proposed delivery format (to be confirmed in R5-0):** individual SVG files in `src/icons/`, used either inline or through a CSS `mask-image` with `background: currentColor`. Inline gives exact colour per path (for example duotone opacity) and no network fetch. The mask approach keeps markup small but can't reproduce multi-tone icons. **This choice depends on the D-12 style**: duotone styles need inline SVG.

## 5. Work that can proceed without icon-source approval

| Item | Why it's safe |
|---|---|
| Icon-slot contract document: one table of every slot (component, size, colour token per state, `aria-hidden` rule, naming for icon-only triggers) | Consolidates already-confirmed values; adds no assets |
| Slot validation fixture (`tests/fixtures/r5-icon-slot-check.html`): asserts every slot's size and `currentColor` per state with a neutral test square (not an icon) | Test-only; makes R5-4 a drop-in |
| Icon manifest schema (`name`, `source`, `nodeId`, `licence`, `sizes`, `styles`), empty | Structure only |
| Usage inventory from **already recorded** read-only outputs: which icon names each component instance references | No new Figma calls needed |
| Resolve **AUD-1** (dropdown listener teardown) and **AUD-3** (move test drivers into `tests/tools/`) | Independent of icons; **each needs your approval** because AUD-1 changes validated source |

## 6. Questions for the owner (to unblock R5)

1. D-12: which source (S1–S6) and which size scale?
2. D-13: can read access to the Annachy Icons File be granted?
3. D-14: are "Design System" and "UI Icons" Annachy-owned and current?
4. D-15: are the Solar, Iconly Pro and Lucide licences confirmed for redistribution? What is the ruling on the brand logos?
5. Is read-only `download_assets` to local staging approved for R5-2? If so, is `create_session` permitted?
6. D-27 / G12: will the owner provide geometry specs, or approve exporting those vectors?

## 7. Update 2026-11-20 — approved safe work completed

The user approved AUD-1, AUD-3 and the §5 infrastructure. D-12, D-13, D-14, D-15 and export approval stay **blocked**: no icon source was chosen.

| §5 item | Delivered |
|---|---|
| Icon-slot contract | `r5-implementation-spec.md` §2: 15 slot cases, all CONFIRMED sizes and colours |
| Slot validation fixture | `tests/fixtures/r5-icon-slot-check.html`: 73 checks, PASS, using a neutral test square (not an icon) |
| Manifest schema + empty manifest | `src/icons/manifest.schema.json`, `src/icons/manifest.json` (`status: "blocked"`, all gates `"open"`) |
| Metadata | category, style, size, source, licence, attribution, Figma node, hashes (spec §3) |
| SVG validation, naming, duplicate and integrity tests | `tests/tools/icons_lib.py` + `r5_icons_static.py`: 53 checks, PASS; every rule self-tested with synthetic probes |
| API and integration architecture | Spec §4: inline SVG by default; the CSS mask mode is deferred until D-12 |
| Pipeline architecture | Spec §5: 6 stages; stages 1–2 (export, preserve) are gated |
| AUD-1 / AUD-3 | Fixed / done (see `r4-final-closure-audit.md` §10) |

**Correction to §5:** "Usage inventory from already recorded read-only outputs" is folded into spec §2.1, the slot inventory with the source seen per slot. A per-icon name inventory needs the source decision (D-12), so it was not produced.

Consolidated status: `r5-readiness-report.md`. **Icon implementation (R5-1 onward) has not been started.**
