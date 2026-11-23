# Mixed-cart checkout — design brief, round 2 (live-app look, 2 directions)

Brief: *Design Brief: Mixed-Cart Checkout* (grocery and non-grocery, India, ₹, mobile 390 and desktop 1440).
Ask for this round: **2 distinct directions for each screen on mobile and desktop**. Refining comes after you pick one.

**Open:** serve the project root (`python -m http.server 8000`), then open
`http://localhost:8000/showcase/screens/checkout/index.html`. The review board shows all six screens at 390 px and at
1440 px (scaled to 50 %), plus scenario links. Every screen is a working prototype (`a-*.html`, `b-*.html`).

This is a **new design built from the system**, not a Figma reproduction. Product names, prices, the address and the
order number are sample data.

## Directions

| | A — Classic marketplace | B — Quick commerce |
|---|---|---|
| Idea | The marketplace pattern shoppers know: one card per shipment | Delivery promise first, one compact sheet, folded bill |
| Cart | Group cards with their own meter, items, subtotal and delivery. Mobile: sticky total and CTA bar. Desktop: 8 / 4 columns with a sticky summary | Both free-delivery meters up front. Desktop: twin columns and a full-width "to pay" bar. Mobile: collapsible shipment sections |
| Delivery & payment | Sections for address, grocery slot (day tiles, slot grid with full slots disabled), other items (radio: standard or same-day with price and date) and payment (pay together by default, or separately; method) | Numbered steps, one decision each. Days as tiles with only the free slots listed (full ones summarised). Same-day is a single **Toggle** on top of the default. "Pay separately" is a Toggle, off by default. The right column shows "Your 2 shipments" |
| Confirmation | Success card, one card per shipment (when, how, contents, amount), "What's next" panel | Success banner and a delivery **timeline** (grocery slot, then other items) with expandable contents and a row of next steps |
| Primary action | Core **Button** (Primary) | **Button Gradient** (the brand CTA used on the PDP screens) |


## Round 2: what changed to make it look like a live storefront

- **App chrome.** Annachy logotype header (desktop: delivery pincode, search, profile, cart badge, as in the Figma header; mobile: back, title, "100% secure"), breadcrumb and a 3-step progress bar.
- **Real product presentation.** Photo, name, variant, selling price, struck-through MRP and green "% off" (the PDP price pattern), quantity stepper, a "you're saving ₹X" banner and a **Price details** card (MRP total, discount, delivery per group, total).
- **Delivery promise and ETA** on every shipment, address bar with Change, trust row, a gradient hero on the confirmation (A) or a delivery timeline (B).
- **Content.** The "Other items" sample is the Derkley T-shirt from the PDP screens, so the photo is real design-file artwork (the ₹249 price and the totals are unchanged).

**Still needed from you for a fully photographic result:**
- **Grocery photos.** The design file has none, and I did not create or source any, so grocery rows show a neutral pack tile with the size.
- **Image rights.** The T-shirt photo is one of the R11 images (rights unverified, internal use only), as is the logotype.
- **Real catalogue data**, if you want names, prices and offers to match your products. All content here is sample data.

## Brief coverage (verified by `tests/tools/checkout_proto_cdp.py`: 91 checks, 0 failures)

| Requirement | Where |
|---|---|
| Two groups, each with items, quantity, subtotal and delivery status; instant totals | Cart (both). Totals change on the same frame, and the change is announced to screen readers |
| Free delivery **≥ ₹299 per group**, ₹40 below it, cue "Add ₹X more for free delivery" | `checkout-core.js` (`FREE_AT`, `FEE`); meter per group |
| Grocery: pick a day and slot; full slots shown | Delivery (both); full slots can't be chosen |
| Non-grocery: standard or same-day, with price and promised date | Delivery (A radio, B toggle) |
| One address for both | Delivery (both) |
| Pay together (default) or one group at a time, with one order summary | Delivery (A radio, B toggle) |
| Confirmation: two shipments, slot and date, contents; track, edit and support | Confirmation (both) |
| **Edge cases** | `?scenario=` |
| — one group below ₹299, the other above | `default` (grocery ₹412 free; other items ₹249 + ₹40) |
| — slot sells out while choosing | `slot-soldout`: the chosen slot fills 1.2 s later; the **nearest later** free slot is selected, with a warning, announced |
| — item becomes unavailable | `unavailable`: shown, excluded from totals, removable |
| — payment fails | `payment-fail`: loading state, then an error alert saying nothing was charged and everything is kept; retry succeeds |

## UX laws

| Law | A | B |
|---|---|---|
| Hick's | Only the relevant options per group; defaults pre-selected (standard delivery, pay together, UPI) | Fewer visible choices: same-day and pay-separately are single toggles; only free slots are listed |
| Miller's | One card per shipment; short sections | Numbered steps; "Your 2 shipments" chunks |
| Goal-gradient | Meter in each group card | Both meters first, side by side |
| Fitts's | All targets ≥ 44 px (48 px tiles); thumb-zone sticky bar on mobile | Same; full-width CTA in the sticky bar |
| Jakob's | Classic cart, then delivery, then pay | Step-numbered checkout pattern |
| Peak-end | Warm success message and a clear "What's next" | Delivery timeline: what arrives, and when |
| Doherty | Instant recalculation; Button loading state while paying | Instant recalculation; "Processing…" state |

## Constraints

- **Tokens only:** colours, type, radii, shadows, border widths and heights all use tokens. No raw colour exists in the CSS or JS (tested).
  - The system has **no spacing scale** (decision D-08), so every gap is derived from the grid tokens: 16 px gutter (×¼, ½, ¾, 1, 1.5), 32 px desktop gutter, frame margins 16 / 120 px.
  - The free-delivery bar reuses the Figma progress pattern from the Desktop PDP (`1375:31181`).
- **Core components:** Button, Button Gradient, Radio and Toggle, plus library icons. Nothing new was added to `src/`.
- **Accessibility:**
  - All 7 pages pass the closure accessibility suite: names, alt text, visible focus, no console errors.
  - Touch targets are ≥ 44 px, with no horizontal overflow at 390 px.
  - Changes are announced through a polite live region; payment errors use `role="alert"`.

## Design-system gaps this brief exposed (input for the Design Team)

| Gap | Effect here |
|---|---|
| **Toggle Off state is nearly invisible**: A39, Off track 1.04:1, square track (D-27) | Weakens Direction B's toggles. Fix in the system, or choose A |
| Checkbox ships without a check glyph (D-27) | Checkboxes avoided; radios used instead |
| No plus/minus icons in the library | The quantity stepper uses "−" / "+" text labels, with a trash icon at quantity 1 (A) |
| No progress, stepper, badge, segmented-control or card components | Built from tokens as screen-level patterns |
| Mobile frame token is 360 px; the brief says 390 | Layouts are fluid at the 16 px margin and verified at 390 |
| Typography classes use the mobile sizes (D-05/D-07) | Only the page title switches to the desktop size token |
| Figma/token still say Proxima Nova; the design team confirmed **Inter** | Inter is self-hosted and renders on every screen; the R1 token is unchanged, so Figma should be updated to match |

## Recommendation

**Direction A** is the safer pick for round 2. It is the more familiar pattern for an Indian grocery and e-commerce audience, and it doesn't depend on the weak Toggle Off state. **Direction B** shows the two shipments more clearly. If B is preferred, its toggles should become radios, or the Toggle contrast should be fixed in the system first.

Tell me which direction (or which parts of each) to refine.
