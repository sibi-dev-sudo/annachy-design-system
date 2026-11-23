# Component Spec — Navigation

| Item | Value |
|---|---|
| Pages | › ⑥ Navigation · Mobile ○ `1351:18314` · › ⑦ Navigation · Desktop ○ `1556:7200` |
| Status | **[MISSING] — both pages are empty** (`get_metadata` returned a canvas with no children). Page markers "○" (not started). |

## Related material found elsewhere (not specifications)

| Location | Node | Content | Status |
|---|---|---|---|
| Research › Brainstorming › Icons section | `5:12734` | Bottom tab-bar exploration — variants `Selected=Home / Category / Cart / Profile`, 393 px wide | Exploration [EXTRACTED names only] |
| Patterns › Sample Screen, PDP | `1627:11756`, `1214:11887` … | Mobile screens likely containing headers/tab bars as instances or frames | Not inspected; reference only |

## Implication

Navigation cannot be implemented from the Figma source of truth. Options for the design owner: (a) design Navigation in Figma before implementation, or (b) approve the Brainstorming tab-bar exploration as an interim spec. No values will be invented.

## Phase 5 update

See `11-dependencies-and-sources.md` §6.1. Summary:
- Desktop header frame **"Main navigation"** `1311:7548` (1440 × 88): logo 170 × 51, delivery-location selector, search 704 × 44 (with mic), profile menu, cart — a frame, not a component.
- Mobile "Top Nav Bar" frames (`1201:9774` 360 × 58), "TOP NAV" (`1214:12126` 393 × 97), Breadcrumb frames on PDP.
- "Bottom Nav Bar/Default" `1242:19336` is a **bottom action bar** (two buttons + home indicator), not tab navigation.
- PDP instance "Bottom Nav Bar" `1214:12125` references a master (`1633:30319`) that is **not in this file** and not in any searchable library [INACCESSIBLE].
