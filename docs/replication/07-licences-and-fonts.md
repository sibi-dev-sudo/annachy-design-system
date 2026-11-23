# 07 — Licences and Fonts Review

Date 2026-11-20. **This is not legal advice.** Items marked *confirm* need the licence documents or a decision from the owner.

## 1. Fonts

| Font | Used by | Available locally? | Status in the replica | What is needed |
|---|---|---|---|---|
| **Proxima Nova** (all type styles; `Font Family/Sans Serif`) | Every component and screen | **No.** Not in `C:\Windows\Fonts` or the per-user fonts folder, not in the font registry, and not in Downloads or Documents | A system fallback stack (`--annachy-base-font-family-render`). Text widths and line breaks differ slightly; screen boxes keep their Figma heights (doc 03) | *Confirm* a **web-font licence** for self-hosting, or a hosted service covering the domain(s). Proxima Nova is a commercial typeface. Desktop licences generally do not cover web embedding |
| Inter, SF Pro | Some screen layers (Sample Screen / PDP: status bars, isolated texts) | No | Fallback stack | *Confirm* whether they are intentional. SF Pro is Apple's system font, licensed for Apple-platform UI mock-ups; Inter is SIL OFL 1.1 (redistributable) |

**How to finish when the files arrive.** Place WOFF2 files in `src/fonts/` and add `@font-face` rules in `src/base/` (the R2 base layer). The token `--annachy-font-family-sans-serif` already names "Proxima Nova", so the change is additive. Then re-run the text-dependent suites (`run_all.py`).

## 2. Iconly (icon artwork in `src/icons/`)

| Item | Record |
|---|---|
| Source | Figma page `1801:5142`, built by the owner from Iconly artwork (component descriptions name the Iconly source layers) |
| Licence on file | **None.** The owner states the Iconly library is purchased; the licence text and account tier are not in the project |
| Current use | **Internal implementation only**, per the owner's export approval. `manifest.json` records `internal-only`; the READMEs say "do not publish or redistribute" |
| *Confirm* | (a) The licence tier allows use in this product's UI. (b) Whether attribution is required, and its wording; it would go into `manifest.json` `sources[].licence.attributionText`. (c) Whether the source SVGs may ship inside a distributed library (`src/icons/svg/`). Many icon licences allow embedding in a product but forbid redistributing the icon set itself. If that applies here, publish only the icons the product uses, or keep icons out of a public package |
| Size note | `src/icons/originals/` holds about 175 MB of byte-preserved category exports (provenance). If `src/` is ever packaged, exclude `originals/` |

## 3. Brands (third-party marks)

| Item | Record |
|---|---|
| What | 624 brand icon sets on the Icons page ("Brands" category), plus 6 logo placeholders in the screens (doc 03) |
| Where | **`restricted/brands/`**, outside `src/`: originals, normalised SVGs, its own `manifest.json` (status `restricted`) and a README. Not imported by the library. Shown in the showcase icon catalogue only behind an opt-in toggle with a rights notice |
| Rights | **Not verified.** Third-party logos are trademarks; using them usually needs the owner's brand guidelines or permission, and they must not be redistributed as part of a design system |
| Colour | The normalised Brands SVGs map solid colours to `currentColor`, like all icons. Brand marks that rely on their own colours are therefore **monochrome** in the catalogue. The originals keep the colours |
| *Confirm* | For each brand actually needed: the rights holder's terms, then a per-brand decision (keep / remove). Until then, keep the folder out of any build or publication |

## 4. Other assets

| Item | Status |
|---|---|
| Product photos, screenshots, illustrations (141 image placeholders) | Not exported (no approval). Their rights are part of the export decision; see `docs/figma-audit/r8-0-remaining-assets.md` |
| Annachy logotype | Annachy's own mark. Its export is part of the same approval list |
| Solar icons (page `375:10889`) | Not exported. The style names match the public Solar set (SUS-07, an open licence to *confirm*); see doc 05 / r8-0 |

## 5. Proxima Nova ZIP review (2026-11-20): fonts NOT enabled

**Source:** `Downloads\Proxima Nova (Original).zip`, inspected read-only in memory. Nothing was extracted, and the ZIP and the project are unchanged.

**What the ZIP contains.** 27 unique font files (OTF, plus one TTF) from **three different redistributions**:
- **exFont.com:** 18 inner ZIPs, each with an `exFont-License.txt`.
- **Font2s.com:** `proxima_nova_medium.zip`, with a ReadMe that says "repository of free fonts".
- **Unlabelled bundle:** `Proxima_Nova-1.zip`, v2.003.

The fonts themselves come in four versions: v1.000/1.001 (2005), v2.003, v2.015 (Mark Simonson Studio) and Typekit v1.00.

**Licence evidence**

| Evidence | What it says |
|---|---|
| Every `exFont-License.txt` (18) | "**License: Free for Personal Use**" |
| Font2s ReadMe | A free-font download site; no licence grant |
| Embedded copyright (all files) | "Copyright (c) Mark Simonson, 2005. **All rights reserved.**" |
| Embedded licence URL | `marksimonson.com/info/licenses`, `ms-studio.com/FontSales/msslicenseagreement.html` (the foundry's commercial licences), and `typekit.com/eulas/…` (Adobe Fonts subscription EULA) |
| OS/2 `fsType` | 0 or 8. These are document-embedding bits; they do **not** grant web-font rights |

**Conclusion: web embedding is NOT permitted by anything in this ZIP.**
- The only explicit licence is "Free for Personal Use" from a third-party download site. That excludes a company product or website.
- Proxima Nova is a commercial typeface. The rights holder is Mark Simonson Studio, and the copies sold through Adobe Fonts are licensed for Adobe Fonts delivery only.
- **Per the owner's instruction ("If web licensing is unclear, stop and report it before enabling the fonts"), the fonts were not installed.**

**What is available (for when a proper licence exists)**

| Weight | Upright | Italic | Needed by the tokens |
|---|---|---|---|
| 250 Thin | ✓ | ✓ | — |
| 300 Light | ✓ | ✓ | — |
| 400 Regular | ✓ | ✓ | **yes** (5 styles) |
| 500 Medium | ✓ | ✗ (no Medium Italic) | **yes** (8 styles) |
| 600 Semibold | ✓ | ✓ | **yes** (11 styles) |
| 700 Bold | ✓ | ✓ | **yes** (4 styles) |
| 800 Extrabold | ✓ | ✓ | — |
| 900 Black | ✓ | ✓ | — |

**Data-quality notes.** Mixed versions have different metrics. Some family names are mislabelled: `Proxima-Nova-Semibold.otf` v1.000 calls itself "Proxima Nova Lt / Bold" at weight 600, and a Typekit "Thin Italic" file reports weight 300. A licensed purchase should supply one consistent version, ideally WOFF2.

**To unblock**, one of:
- a web-font licence from Mark Simonson Studio (or a reseller), with the WOFF2 files;
- an Adobe Fonts web project for the domain (served by Adobe, not self-hosted);
- or a written statement of an existing licence that covers web embedding.

The integration itself is about 1–2 h (§1).


## 6. Screen images (R11, 2026-11-20)

`showcase/screens/assets/images/` holds 52 files copied byte-for-byte from the Figma file under the owner's consolidated approval
**for internal reproduction only**. That approval does not establish ownership or a licence, and technical export access is not
proof of rights. No file is marked as owned or licensed by Annachy.

| Rights evidence (Figma layer names only) | Unique images | Needed before any public use |
|---|---:|---|
| AI-generated ("Gemini_Generated_Image…") | 8 | Design-team approval for use; check the generator's terms and any likeness / brand content |
| Retailer-style SKU file names | 12 | Confirmation that the photography is Annachy's own or licensed |
| Probable web downloads ("unnamed…", "Orginal Image") | 8 | Source and licence evidence, or replacement by the owner |
| Screenshot ("Screenshot 2026-09-23…") | 1 | What it shows and who owns it |
| Emoji raster ("🥽 Goggles") | 1 | Emoji vendor licence (third-party artwork) |
| No source recorded | 13 | Source and licence evidence |
| Vectors (ribbon, car, badge, iPhone status-bar parts) | 9 files | Origin not verified; status-bar parts are third-party device-UI mock-up artwork |

Each placeholder carries `data-img-rights`. The folder README lists every file with its source and status. **Do not publish or
redistribute** the screens with these images until each row above is resolved.
