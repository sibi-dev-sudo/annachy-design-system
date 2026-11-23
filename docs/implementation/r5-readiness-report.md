# R5 Readiness Report — Icons

| Item | Value |
|---|---|
| Date | 2026-11-20 |
| Verdict | **Infrastructure READY. Icon implementation BLOCKED** by four design-owner, access and licensing decisions plus export approval. No icon source was chosen. |
| Figma | Not accessed. No exports, downloads, third-party imports or `create_session` |
| Library state | 464 tokens unchanged. R1–R4 are validated (full regression, §5). `src/` contains **no icon artwork** |

---

## 1. What is completed

| Work | Result |
|---|---|
| **AUD-1** Dropdown listener lifecycle | Fixed. Listeners are bound to an `AbortSignal`; the document listener exists only while a dropdown is open; added `destroy()`, `destroyDropdowns(root)` and `getDropdown(el)`; `initDropdowns` is unchanged. New lifecycle and leak test: 40 checks. 3 new mutants are all caught |
| **AUD-3** Test tooling preserved | 22 tools in `tests/tools/` with a README: a sequential runner, a committed integrity baseline, and a guarded mutation runner with crash recovery (verified with a hard kill). No temporary profiles, bytecode or mutation state are left behind |
| R5 slot contract | Spec §2: 15 slot cases across 7 components |
| R5 manifest | Schema (draft 2020-12) and an empty manifest that is `blocked` |
| R5 validators | SVG safety and normalisation rules (V01–V11), policy (P01–P09), naming (N01), duplicates (D01–D02), integrity (I01–I03); every rule self-tested |
| R5 architecture | Component API and integration (spec §4); 6-stage local pipeline (spec §5) |

## 2. Infrastructure ready to use

| Asset | Path | State |
|---|---|---|
| Slot contract fixture | `tests/fixtures/r5-icon-slot-check.html` | 73 checks PASS. All 15 slot cases accept an unsized `currentColor` SVG today, so **no component CSS change is needed** to receive icons |
| Manifest schema / manifest | `src/icons/manifest.schema.json`, `src/icons/manifest.json` | Valid; `status: "blocked"`; all gates `"open"` |
| Validator library | `tests/tools/icons_lib.py` | Pure stdlib functions, ready for the pipeline |
| Static suite | `tests/tools/r5_icons_static.py` | 53 checks PASS (includes self-test fixtures `tests/fixtures/r5-icons/`) |
| Regression and safety | `tests/tools/run_all.py`, `baseline.py`, `mutate.py` | R5 suites included in the full run |

**Not yet written (needs real exports to test against):** the pipeline script `tests/tools/icons_pipeline.py` (spec §5, stages 1–6) and its round-trip test.

## 3. What requires design-owner or licensing confirmation

| ID | Decision | Who |
|---|---|---|
| **D-12** | The canonical icon source: S1 catalogue, S2 pilots, S3 Component Source, S4 Brainstorming, S5 Annachy Icons File or S6 UI Icons. Also the style or styles, and **one** size scale: 14/16/20/24/28/32/36/38/42 (S2/S3) or 16/20/24/32/40 (S5). Today, Input already mixes S2 (Filled) and S5 (Outline) | Design owner |
| **D-14** | Whether "Design System" (`lk-483b…`) and "UI Icons" (`lk-c918…`) are Annachy-owned and current | Design owner |
| **D-15** | Licence and redistribution rights for Solar (SUS-07 name match), Iconly Pro (commercial), Lucide (`badge-check`), and a ruling on Amazon/Flipkart logos | Legal + design owner |
| D-27 / G12 | Checkbox glyph, radio ring, toggle strokes and tooltip arrow polygon. These are *component geometry*, separate from the icon library | Design owner (spec or export approval) |
| Delivery mode | Whether a CSS-mask utility is wanted in addition to inline SVG. Only possible for single-tone styles (depends on D-12) | Design owner / maintainers |
| RTL mirroring | Whether directional icons mirror in right-to-left layouts | Design owner |

## 4. Exactly what is needed to unblock icon implementation

1. **A D-12 decision record.** It should state the source ID, the style slug(s), the size scale, and which categories are in scope. A first scope of "icons used by Button / Input / Dropdown" is enough to start.
2. **D-13 access (only if S5 is chosen).**
   - The Annachy Icons File URL or file key.
   - Read access for the account used by the read-only Figma tools.
3. **D-14 ownership statement** for the "Design System" and "UI Icons" libraries, if either is a candidate.
4. **D-15 licence evidence** for the chosen source:
   - the licence name and text or URL;
   - whether redistribution in this library is allowed;
   - whether attribution is required, and its exact wording.

   These go straight into `sources[].licence`.
5. **Explicit export approval** for read-only `download_assets` of the listed icons into local staging (`%TEMP%/annachy-icon-staging/`), and the scope of that approval (icon list or category). If the Figma tooling requires `create_session` first, approval for that too, or independent confirmation that it is read-only.
6. **For D-27 / G12 (optional, independent of 1–5):** owner-supplied geometry (path data or dimensions) or export approval for those specific vectors.

Once items 1, 4 and 5 are provided (plus 2 or 3 depending on the source), the work is:
- **R5-1:** inventory.
- **R5-2:** export to staging and byte-preserved originals.
- **R5-3:** pipeline and round-trip tests.
- **R5-4:** fill the default slots in Button, Input and Dropdown markup and add the Icons showcase page.

All of it runs through the gates already enforced by `r5_icons_static.py`.

## 5. Validation at hand-over

Full sequential regression (`python -I tests/tools/run_all.py`) after AUD-1, the tooling migration and the R5 infrastructure: **24 / 24 suites PASS**, 0 leftovers.

| Area | Result |
|---|---|
| Tokens | 464 (457 originals hash-identical) |
| R1–R3 | R3 browser 34,214 / 0 · R3 real input 232 / 0 · statics PASS |
| R4 | Dropdown 469 / 82 / lifecycle 40 / init 10 · Tooltip 1,441 / 39 · showcases 15 / 13: all 0 failures |
| R5 | static 53 / 0 · slot contract 73 / 0 |
| Mutation | 19 / 19 caught, all restored byte-identical |

Details: `r4-final-closure-audit.md` §10. Open test-environment observation TOOL-1 (one non-reproducible connection-refused log line in an earlier run) is recorded there.
