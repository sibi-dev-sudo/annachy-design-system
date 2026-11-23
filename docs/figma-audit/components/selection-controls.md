# Component Spec — Selection Controls (public wrapper)

| Item | Value |
|---|---|
| Page | › ④ Checkbox /Radio/Toggle ✓ `375:10893` |
| Component set | **Selection Controls** `1504:57173` (3 variants) |
| Location | Section `1568:36951` "Button Master Components (Radio/ Checkbox/ Toggle)" |
| Method | `get_variable_defs` on `1504:57178` (Toggle). Dimensions from metadata. Read-only. |

| Variant | Node | Size [META] |
|---|---|---|
| Control Type=Radio Button | `1504:57174` | 216 × 41 |
| Control Type=Checkbox | `1504:57176` | 216 × 41 |
| Control Type=Toggle | `1504:57178` | 228 × 40 |

Role [DERIVED]: public entry point wrapping the hidden `.Selection Controls / *` sets (leading "." = unpublished). Nested property exposure not inspected.

Toggle variant `1504:57178` [BOUND]: track `Button/Primary/Background/Default` `#004feb` (confirms Toggle **On** track colour), thumb `Button/Primary/Content/Loading` `#fafcff`, effect `Toggle/On`; label **Label Small — Medium 14/20** (the core Toggle set uses Label Medium 16/21) — typography differs between wrapper and core.

| # | Finding | Severity |
|---|---|---|
| SC1 | Wrapper label style (14/20) differs from core sets (16/21). | Medium |
| SC2 | Section is named "Button Master Components" but contains selection controls. | Low |
| SC3 | Widths 216 / 228 match the *Small* core variants, suggesting the wrapper defaults to Small. | Info |


## R3-0 update (2026-11-19)

Read-only inspection; full evidence with node IDs in `../r3-0-evidence.md`. Original findings above are preserved.

- **SC3 confirmed:** each wrapper variant is a single instance named "Control" of the core set's *Small* variant (`1504:57174`, `57176`, `57178`, §14). The wrapper has no own styling.
- **SC1 corrected:** the 14/20 label is the Toggle *Small* label style (Label Small), not a wrapper-specific inconsistency.

## R3 update (2026-11-19)

Documented as an alias in `src/components/selection-controls/README.md`: each wrapper variant = the Small core variant. No CSS.
