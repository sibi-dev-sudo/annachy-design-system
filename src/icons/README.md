# src/icons — icon assets (R7-1)

**Status: ACTIVE — internal use only.** Artwork exported read-only from Figma page `1801:5142` "② Icons"
(file `rM3ixSG6i3DFfKZFWuxzs4`) with the project owner's export approval (2026-11-20, local internal implementation only).
Artwork is Iconly-derived: Iconly licence purchased by the project owner, licence text not on file — **do not publish
or redistribute**. Keep the Iconly attribution with the assets.

| Gate | Record (see `manifest.json`) |
|---|---|
| D-12 | Icon source = in-file page 1801:5142 |
| D-13 | Icons readable with read-only tools |
| D-14 | Not applicable to this source (concerns only the external "Design System" / "UI Icons" libraries; still open for them) |
| D-15 | Iconly purchased by the project owner; internal use only; licence text not on file |
| Export | Approved by the project owner for page 1801:5142, local internal use only |

| Path | Content |
|---|---|
| `originals/iconly-annachy/<category>.svg` | 32 byte-preserved category exports (never edited; SHA-256 in `manifest.json`) |
| `svg/outline/<slug>.svg`, `svg/filled/<slug>.svg` | Normalised assets: `viewBox="0 0 24 24"` (M reference), geometry untouched, `currentColor`, no ids / width / height |
| `svg/<style>/<slug>--<size>.svg` | Extra file for a size that is not scale-equivalent to M (4 files) |
| `catalogue.json` | Browser catalogue: categories → sets → styles → files + Figma variant node ids per size |
| `manifest.json` / `manifest.schema.json` | Inventory, provenance, licence and integrity record (schema extensions E1–E8 documented in the schema) |
| `figma-icon-map.json` | Component slot → Figma icon set |

The **Brands** category (624 third-party brand marks) is **not** here: it lives in `restricted/brands/` outside `src/`
(rights not verified). The duplicated "Calender & date" frame (`1802:138448`) reuses the files of `1802:121134`.

Pipeline and validation: `tests/tools/icons_export/` (export ingest, split, report) and
`python -I tests/tools/r7_icons_static.py`. Report: `docs/figma-audit/r7-1-icon-export-report.md`.
