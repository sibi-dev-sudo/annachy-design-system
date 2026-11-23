# Archive / duplicate comparison (derived from saved get_metadata — no new Figma calls)

Variant names normalised (`Checkbox/Radio/Toggle Position` → `Position`). Compares variant name sets and frame sizes.

| Component | Current | Duplicate | Current variants | Duplicate variants | Same names | Size differences |
|---|---|---|---:|---:|---|---:|
| Button (All Buttons) | `887:2492` | `1590:19040` | 432 | 432 | yes | 360 |
|  | e.g. | | | | | `Size=24, State=Default, Type=Primary` (104, 24) vs (72, 24) |
| Checkbox | `1504:53300` | `1500:25474` | 126 | 126 | yes | 0 |
| Radio | `1504:52363` | `1493:3` | 108 | 108 | yes (from inline metadata, Phase 3 notes) | 0 (216/220/224 × 41 both) |
| Toggle | `1504:54471` | `1438:5542` | 180 | 180 | yes | 0 |
| Dropdown / Item | `1451:25092` | `1464:2972` | 40 | 40 | yes | 0 |

**Conclusion:** Archive Checkbox/Radio/Toggle and the Archive Dropdown/Item are structural copies of the current sets (only property name `X Position` differs). The EMPTY PAGE button set has identical variant names but **different dimensions in 360 of 432 variants** — it is a divergent older/alternate version, not an exact duplicate.
