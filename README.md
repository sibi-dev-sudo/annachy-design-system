# Annachy Design System

Enterprise-grade, framework-free component library built with vanilla HTML5, CSS3 and JavaScript (native ES Modules).

**Status (2026-11-20):** a browser replica of the Figma file. Traceability is in [`docs/replication/`](docs/replication/).

| Area | State |
|---|---|
| Foundations | Done: 464 tokens (457 + 7 R3-0a) and a partial Dark mode (`themes/dark.css`, the 7 Dark values Figma defines). Base styles |
| Components | **1,397 of 1,397 Figma variants**: Button 432, Gradient 55, Input 325, Checkbox 126, Radio 108, Toggle 180, Selection Controls 3, Dropdown Menu 48 + Item 40 (Light/Dark, Search, Footer with staged commit), Tooltip 80. Navigation: the Figma pages are empty |
| Patterns & screens | 8 frames reproduced (Sample Screen 5, PDP 3) in `showcase/screens/`; 2 superseded PDP iterations documented |
| Icons | **5,128 sets / 35,890 variants from Figma page `1801:5142`** (6,890 SVG assets, exported with the owner's approval, Iconly-derived, **internal use only**). Catalogue: `showcase/icons/`; helper: `src/icons/icons.js`. Third-party Brands are kept in `restricted/` (rights not verified). Solar icons on `375:10889` are not exported |
| Showcase | `showcase/index.html`: searchable catalogue of foundations, components and screens. Serve the root over HTTP |

Release history: R1 tokens, R2 base, R3 core controls, R4 Dropdown / Tooltip, R5 icon infrastructure, R6 Dropdown Dark + Footer, plus screens and showcase (see `CHANGELOG.md`).

Remaining blockers and owner decisions: [`docs/replication/04-gaps-and-blockers.md`](docs/replication/04-gaps-and-blockers.md). Fonts: Proxima Nova is not included (licence pending), so a system fallback is used.

**Completion:** [`docs/replication/08-final-completion-report.md`](docs/replication/08-final-completion-report.md) (88.0 % of matrix rows; 99.13 % of design units; 33/33 suites, 24/24 mutants). **Run the showcase:** `python -m http.server 8000` in the project root, then open http://localhost:8000/showcase/index.html.

**Tests:** run `python -I tests/tools/run_all.py` from the project root for the full sequential regression. See [`tests/tools/README.md`](tests/tools/README.md).

- Design source: Figma file `rM3ixSG6i3DFfKZFWuxzs4` (Annachy CF — Design System), inspected read-only.
- Audit reports: [`docs/figma-audit/`](docs/figma-audit/)
- Tech constraints: no frameworks (React/Angular/Vue/Next.js), no Tailwind/Bootstrap, no bundlers.

**Final status (2026-11-20):** see [`docs/replication/FINAL-PROJECT-COMPLETION-REPORT.md`](docs/replication/FINAL-PROJECT-COMPLETION-REPORT.md).
- The core design system is complete.
- The showcase is ready for internal use: `python -m http.server 8000` from the project root, then open `http://localhost:8000/showcase/index.html`.
- 241 / 246 in-scope screen placeholders are filled.
- **Not cleared for public distribution** (image rights, font and Iconly licences): see `FINAL-PENDING-ITEMS.md`.
