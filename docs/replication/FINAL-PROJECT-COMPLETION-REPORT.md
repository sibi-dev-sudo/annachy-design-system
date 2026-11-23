# Annachy Design System — Final Project Completion Report

Date: 2026-11-20 · Source of truth: Figma `rM3ixSG6i3DFfKZFWuxzs4` (read-only throughout; never modified) · Stack: vanilla HTML, CSS, ES modules.

Companion reports: [FINAL-TEST-REPORT](FINAL-TEST-REPORT.md) · [FINAL-PENDING-ITEMS](FINAL-PENDING-ITEMS.md) · [FINAL-DESIGN-TEAM-ACTION-LIST](FINAL-DESIGN-TEAM-ACTION-LIST.md)

## 1. Four separate conclusions

| Question | Answer |
|---|---|
| **Core design system implementation complete?** | **Yes.** 464 tokens, 1,397 component variants and 35,890 icon variants are implemented and verified (baseline unchanged in the closure). Two documented exceptions come from the Figma source itself: Navigation pages are empty, and there is no Select trigger component |
| **Browser showcase ready for internal use?** | **Yes.** It has 25 pages, search and filtering, no console errors or failed requests, accessible names on every control, visible keyboard focus, and alt on every image (34/34 suites) |
| **Full visual replication complete?** | **No, but every remaining gap is documented.** 241 of 246 in-scope screen placeholders are filled. The 5 left are third-party logos blocked on rights. Text renders in a fallback font until Proxima Nova is licensed. Icons the Design Team declared not required stay as empty slots |
| **Public / commercial distribution legally cleared?** | **No.** Rights for 43 screen images are unverified; the Proxima Nova web licence is missing; the Iconly licence text is not on file. All are external blockers |

## 2. Completed deliverables

| Deliverable | State | Evidence |
|---|---|---|
| Design tokens | 464 (457 original plus 7 approved), byte-pinned | `tests/tools/baseline.py`, R1 suite |
| Components | 1,397 variants: Button, Button Gradient, Input, Checkbox, Radio, Toggle, Dropdown (Light, Dark, Footer), Tooltip | R3, R4 and R6 suites (33,000+ browser checks) |
| Icons | 35,890 variants (Iconly, internal licence restriction) with catalogue and helper | R5 and R7 suites, 7,100 / 7,105 matching Figma |
| Screens | 8 Figma frames reproduced (PDP V1, Mobile, BG Colours, Desktop PDP, Mobile PDP, Mobile putaway, Job listing, Desktop `1608:9891`, which has an empty source) | Screen suites 1,441 / 0 and 306 / 0 |
| Structural vectors (R10) | 28 original artworks filling 50 elements | `r10-0-structural-vector-manifest.md` |
| Product imagery (R11) | 52 original files filling 108 placeholders, internal use only | `r11-0-product-imagery-manifest.md` |
| **Closure: screen icons and logotype** | 37 original SVGs plus 1 library reuse filling 50 icon placeholders and the Annachy logotype; 7 card stars reuse the R10 star | `docs/figma-audit/closure-icons-logo-manifest.md` |
| **Closure: image optimisation** | 43 WebP web copies; 42 in use after A/B verification; originals byte-identical | `showcase/screens/assets/images-web/README.md` |
| **Closure: accessibility suite** | All 25 pages: errors, names, alt, focus, ids, language and title | `tests/tools/closure_a11y_cdp.py` (147 / 0) |
| Showcase | Searchable catalogue of foundations, components, icons and screens | Showcase crawl, catalogue and accessibility suites |

## 3. What the closure changed

1. **Icons.** All 50 remaining in-scope icon placeholders and the Annachy logotype were read verbatim from Figma (one call per node), exported as originals and placed with Figma's own insets.
   - Parent transforms were read from the parents' design context: a mirror on `1375:30955`, a vertical flip on `1375:31088`, and −90° on `1375:31227`.
   - The library was searched for each artwork across 6,098 icons. One exact match is reused (the hamburger icon, coloured `#3D4451`); no other artwork matched exactly.
   - The desktop product badge reuses R11 artwork `73565`. The 7 desktop card stars reuse the R10 star `c6cc8`, matching the mobile cards.
2. **Logos.** The Annachy logotype is integrated. The 5 third-party "logo 2" marks are excluded: no authorised files and no rights evidence. They were not exported.
3. **Images.** Web copies were made and checked A/B at real display sizes; 42 of 43 are in use. Screen image weight across all screens fell from **192.3 MB to 22.0 MB (−88.5 %)**. The originals were not modified (§6).
4. **Visual defects fixed using existing evidence:**
   - Library icons in the screens still showed placeholder chrome (dashed outline or inset border); this gap dated back to R7.
   - The PDP V1 delivery field's instance override hid the Figma Focused border, leaving keyboard focus invisible.
5. **Tests.**
   - New: the accessibility suite (34th suite) and mutants CL-ICON and CL-FOCUS.
   - The R11-SRC and R11-SCALE mutants were updated for the web copies.
   - The fixtures accept a web copy only when it is linked to its declared original.
6. **Fonts.** Unchanged (see §7).

## 4. Completion figures (placeholder census, `closure-placeholder-census.json`)

| Category | Placeholders |
|---|---:|
| Filled with original Figma artwork or an exact library icon | **248** (241 in scope plus 7 reused stars from the not-required group) |
| Not required (Design Team R9: Solar, Brainstorming, Gallery Minimalistic) | 96 |
| Not applicable: phone system UI (status bar, including the 6 nodes that cannot be read) | 14 |
| Externally blocked: third-party brand logos | 5 |
| Unclassified | **0** |
| **Total** | **363** |

- **In-scope screen placeholders: 241 / 246 = 98.0 %.** The in-scope total excludes the not-required and not-applicable groups.
- All screen placeholders: 248 / 363 = 68.3 %. The remainder is almost entirely the Design Team's not-required decision.

Earlier reports used a 269-placeholder basis, which counted Figma elements and treated the status bar as in scope. The census above counts actual placeholders and is reproducible from the HTML. It supersedes the earlier figures.

**Design units.** Tokens, component variants and icon variants are 37,751 of 37,751 implemented (100 % of what Figma defines). Adding the 246 in-scope screen placeholders gives 37,992 / 37,997 = **99.99 %**.

**Traceability matrix rows:** 23 / 25 (92 %). Navigation is empty in Figma; the Select trigger has no Figma component.

## 5. Visual fidelity: known differences

| Difference | Cause | Status |
|---|---|---|
| All text renders in `system-ui` instead of Proxima Nova | No web licence (personal-use ZIP) | External; drop-in ready (§7) |
| Empty icon slots on the PDP screens (Solar, Brainstorming, Gallery Minimalistic) | Design Team: not required | Not required |
| Empty status-bar glyphs | Phone system UI | N/A |
| 5 empty brand-logo slots (Desktop PDP related products) | No rights or authorised files | External |
| Desktop frame `1608:9891` is empty | Figma returns the frame without children | Figma limitation |
| 7 dashed lines differ in dash phase; 3 vertical dashed lines have unknown direction; 4 artworks export empty; 0.24 px offset on V23 | R10-U1 to U4 | Recorded |
| R11 images: 61 compared with Figma's render (median difference 4.2/255); 3 reviewed exceptions; 34 had no usable Figma render | R11-U2 | Recorded |
| Web copies differ from the rendered originals by at most 6.7/255 mean (blurred ≤ 2.0) | Resampling and compression | Verified A/B (§6) |
| 5 Filled Arrow icons have artwork outside their frames | Figma defect FIG-ICON-1 | Reproduced as is; Figma fix needed |
| Contrast findings A04, A14, A16, A38 to A41 | As designed in Figma | Documented in `09-accessibility.md` |

## 6. Image performance

| Screen | Before (originals) | After | Image requests | Failed | Local load |
|---|---:|---:|---:|---:|---:|
| PDP V1 | 89.87 MB | 10.41 MB | 47 | 0 | 0.77 s |
| Mobile PDP | 89.87 MB | 10.41 MB | 50 | 0 | 0.83 s |
| Desktop PDP | 8.13 MB | 0.64 MB | 53 | 0 | 0.63 s |
| Mobile (PDP) | 2.43 MB | 0.16 MB | 3 | 0 | 0.44 s |
| Desktop BG Colours | 1.68 MB | 0.41 MB | 1 | 0 | 0.52 s |
| Mobile putaway | 0.27 MB | 0.01 MB | 7 | 0 | 0.48 s |
| **All screens** | **192.3 MB** | **22.0 MB (−88.5 %)** | | **0** | |

- **Source of the figures:** `docs/replication/closure-image-weight.json`. Load times are wall-clock on the local HTTP server with the cache disabled, so they are indicative only.
- **Folders:** the originals (`assets/images/`, 102.3 MB) are untouched; the web copies (`assets/images-web/`) total 2.7 MB.
- **Remaining 9 MB:** one image, `62f2c` (9.05 MB, shown on two screens), failed the strict A/B rule and keeps its original. Its handling is recorded in [FINAL-PENDING-ITEMS](FINAL-PENDING-ITEMS.md).

## 7. Fonts

- **Status:** the Proxima Nova ZIP is "Free for Personal Use" and is not embedded. The token `--annachy-font-family-sans: "Proxima Nova"` stays unchanged, and the render stack falls back to `system-ui, sans-serif`.
- **Ready to drop in:** with licensed WOFF2 files, add `@font-face` rules for family `"Proxima Nova"` (weights 300, 400, 500, 600 and 700, as used by the tokens), for example in a new `src/base/fonts.css` imported first in `src/annachy.css`. No token, size, weight or line-height changes are needed.
- **Afterwards:** rerun the regression and record the font licence in `07-licences-and-fonts.md`.

## 8. Rights and licences

| Asset | Restriction |
|---|---|
| 43 R11 raster images and their web copies | **Internal use only**; rights unverified per image (`data-img-rights`, `assets/images/README.md`) |
| Iconly icon artwork (35,890 variants) | Owner states the library is purchased; licence text not on file. Internal use until it is |
| Proxima Nova | Not licensed for web; not embedded |
| Third-party brand logos (5) | Not integrated |
| Annachy logotype, screen icons, R10 vectors | Taken from the Annachy Figma file. Ownership is assumed to be the company's but not independently verified |

## 9. Launching the showcase locally

```sh
cd "<project root>"            # the folder that contains src/, showcase/, tests/
python -m http.server 8000
# open http://localhost:8000/showcase/index.html
```

An HTTP server is required, because ES modules and the icon loader don't work from `file://`. To run the tests: `python -I tests/tools/run_all.py` (sequential, about 5 minutes; needs Chrome).

## 10. Readiness

- **Ready for internal management review:**
  - the showcase (foundations, components, icons, screens);
  - all reports;
  - the full test suite (34/34; 30/30 mutants).
- **Required before any public or commercial distribution:**
  1. Image rights for every R11 file, or replacements supplied by the owner.
  2. A Proxima Nova web licence, then font integration.
  3. The Iconly licence text on file.
  4. Third-party logo rights (or removal of the logo slots).
  5. Design Team fixes in Figma ([action list](FINAL-DESIGN-TEAM-ACTION-LIST.md)).
  6. A decision on optimising the last original image.
