# Screen images — web-delivery copies (closure) — INTERNAL USE ONLY

These are **derivatives** of the original Figma images in `../images/`. They inherit exactly the same source and rights
status as their originals (see `../images/README.md` and each placeholder's `data-img-rights`): **unverified, internal
reproduction only. Do not publish or redistribute.**

| | |
|---|---|
| Purpose | Browser delivery weight only. The originals in `../images/` remain byte-identical and are the source for any future change |
| Files | 43 WebP copies (`<assetId>.webp`), `manifest.json` (original, sizes, SHA-256, scale, quality) |
| Sizing | Each copy covers the image's largest rendered size on any screen at device-pixel-ratio 3 (4 for the two hardest cases), keeping the original aspect ratio as exactly as possible; never enlarged beyond the original |
| Encoding | Chrome's WebP encoder (alpha preserved), quality 0.92 (0.97 for `62f2c`, `bf527`) — `tests/tools/closure_optimize_images.py` |
| Verification | `tests/tools/closure_web_images_ab.py`: every image placeholder rendered with the original and with the copy, at device-pixel-ratio 1 and 2, at its real display size (190 comparisons). An image is switched only if **every** placeholder using it passes: raw mean absolute difference ≤ 3 and ≤ 1 % pixels off by > 32, or after a 3×3 blur mean absolute difference ≤ 2 with the same ≤ 1 % limit. Results: `docs/replication/closure-image-ab-results.json` |
| In use | 42 of 43 copies (`docs/replication/closure-image-switch.json`). `62f2c` (9.05 MB) **did not pass** and the screens keep its original |

A switched `<img>` carries `data-img-original="<original file>"`; `data-annachy-image` still lists the originals.
