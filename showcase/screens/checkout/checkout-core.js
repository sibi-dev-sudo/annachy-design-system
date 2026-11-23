/*
 * Mixed-cart checkout prototype — shared core (data, state, rules, component markup helpers).
 * Brief: docs (Downloads/design-brief.pdf) "Mixed-Cart Checkout". Uses ONLY Annachy core components
 * (Button, Button Gradient, Radio, Toggle) and library icons; values come from tokens (see checkout.css).
 * Sample data only: generic product names, no product photography (R11 images are restricted to the PDP screens).
 */
import { fillIconSlots } from '../../../src/icons/icons.js';

export const FREE_AT = 299;          // free delivery threshold, per group (brief)
export const FEE = 40;               // sample delivery fee below the threshold (brief)
export const EXPRESS_FEE = 79;       // sample same-day price for non-grocery (prototype value)
const KEY = 'annachy-checkout-proto-v1';

const SHIRT = '../assets/images-web/8ced0.webp';   // R11 asset 010834LOLI_1 (internal-use image, rights unverified): the Derkley T-shirt of the PDP screens
const ITEMS = {
  grocery: [
    { id: 'g1', name: 'Toned Milk', unit: '1 L pouch', price: 68, mrp: 74, qty: 2, icon: 'shopping-shopping-basket', pack: '1 L' },
    { id: 'g2', name: 'Whole Wheat Atta', unit: '5 kg pack', price: 249, mrp: 289, qty: 1, icon: 'shopping-shopping-basket', pack: '5 kg' },
    { id: 'g3', name: 'Fresh Tomatoes', unit: '1 kg', price: 27, mrp: 32, qty: 1, icon: 'shopping-shopping-basket', pack: '1 kg' },
    { id: 'g4', name: 'Fresh Paneer', unit: '200 g', price: 95, mrp: 105, qty: 1, icon: 'shopping-shopping-basket', pack: '200 g', unavailableIn: 'unavailable' },
  ],
  other: [
    { id: 'o1', name: "Derkley Men's Camouflage Print T-shirt", unit: 'Olive · Size M', price: 249, mrp: 499, qty: 1, icon: 'shopping-bag', img: SHIRT, alt: "Derkley Men's Camouflage Print T-shirt, Olive" },
  ],
};
export const GROUPS = {
  grocery: { title: 'Grocery', icon: 'shopping-shopping-basket', shipment: 'Grocery delivery' },
  other: { title: 'Other items', icon: 'shopping-bag', shipment: 'Other items delivery' },
};

/* ---------- scenario (edge cases from the brief) ---------- */
export const SCENARIOS = {
  default: 'One group below ₹299, the other above',
  'both-free': 'Both groups qualify for free delivery',
  unavailable: 'An item becomes unavailable',
  'slot-soldout': 'A grocery slot sells out while choosing',
  'payment-fail': 'Payment fails (first attempt)',
};
export const scenario = (() => { const s = new URLSearchParams(location.search).get('scenario'); return s in SCENARIOS ? s : 'default'; })();

/* ---------- dates & slots ---------- */
const DAY_MS = 864e5;
const fmtDay = (d, i) => (i === 0 ? 'Today' : i === 1 ? 'Tomorrow' : d.toLocaleDateString('en-IN', { weekday: 'short' }));
const fmtDate = (d) => d.toLocaleDateString('en-IN', { weekday: 'short', day: 'numeric', month: 'short' });
export const days = [0, 1, 2].map((i) => { const d = new Date(Date.now() + i * DAY_MS); return { id: `d${i}`, label: fmtDay(d, i), date: fmtDate(d), short: d.toLocaleDateString('en-IN', { day: 'numeric', month: 'short' }) }; });
const SLOT_TIMES = ['7–9 AM', '9–11 AM', '12–2 PM', '4–6 PM', '6–8 PM', '8–10 PM'];
const FULL = { d0: ['7–9 AM', '9–11 AM', '12–2 PM'], d1: ['9–11 AM'], d2: [] };   // sample availability
export const slots = Object.fromEntries(days.map((d) => [d.id, SLOT_TIMES.map((t, k) => ({ id: `${d.id}-s${k}`, time: t, full: FULL[d.id].includes(t) }))]));
export const OTHER_OPTIONS = [
  { id: 'standard', title: 'Standard delivery', promise: () => `By ${fmtDate(new Date(Date.now() + 3 * DAY_MS))}`, price: (sub) => (sub >= FREE_AT ? 0 : FEE) },
  { id: 'express', title: 'Same-day delivery', promise: () => 'Today by 9 PM', price: () => EXPRESS_FEE },
];

/* ---------- state ---------- */
const fresh = () => ({
  scenario,
  qty: Object.fromEntries(Object.values(ITEMS).flat().map((i) => [i.id, scenario === 'both-free' && i.id === 'o1' ? 2 : i.qty])),
  removed: [], slot: null, day: 'd0', other: 'standard', payMode: 'together', method: 'upi', paid: { grocery: false, other: false },
  payAttempts: 0, soldOut: [],
});
export const state = (() => {
  try { const s = JSON.parse(localStorage.getItem(KEY)); if (s && s.scenario === scenario) return s; } catch { /* ignore */ }
  return fresh();
})();
export const save = () => localStorage.setItem(KEY, JSON.stringify(state));
export const reset = () => { localStorage.removeItem(KEY); location.reload(); };

/* ---------- derived values ---------- */
export const items = (g) => ITEMS[g].filter((i) => !state.removed.includes(i.id) && (!i.unavailableIn || i.unavailableIn === scenario))
  .map((i) => ({ ...i, qty: state.qty[i.id], unavailable: i.unavailableIn === scenario }));
export const subtotal = (g) => items(g).filter((i) => !i.unavailable).reduce((s, i) => s + i.price * i.qty, 0);
export const count = (g) => items(g).filter((i) => !i.unavailable).reduce((s, i) => s + i.qty, 0);
export const mrpTotal = (g) => items(g).filter((i) => !i.unavailable).reduce((t, i) => t + i.mrp * i.qty, 0);
export const savings = (g) => (g ? mrpTotal(g) - subtotal(g) : savings('grocery') + savings('other'));
export const off = (i) => Math.round((1 - i.price / i.mrp) * 100);
export const isFree = (g) => subtotal(g) >= FREE_AT;
export const toFree = (g) => Math.max(0, FREE_AT - subtotal(g));
export const progress = (g) => Math.min(100, Math.round((subtotal(g) / FREE_AT) * 100));
export const fee = (g) => {
  if (!count(g)) return 0;
  if (g === 'other') return OTHER_OPTIONS.find((o) => o.id === state.other).price(subtotal(g));
  return isFree(g) ? 0 : FEE;
};
export const groupTotal = (g) => (count(g) ? subtotal(g) + fee(g) : 0);
export const total = () => groupTotal('grocery') + groupTotal('other');
export const activeGroups = () => Object.keys(GROUPS).filter((g) => count(g) > 0);
export const slotObj = () => (state.slot ? Object.values(slots).flat().find((s) => s.id === state.slot) : null);
export const dayOf = (slotId) => days.find((d) => slotId && slotId.startsWith(d.id + '-'));
export const isFull = (s) => s.full || state.soldOut.includes(s.id);

/* ---------- formatting & markup helpers (core components only) ---------- */
export const rs = (n) => '₹' + n.toLocaleString('en-IN');
export const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
export const icon = (slug, size = 24, style = 'outline', label = '') =>
  `<span class="co-icon" data-annachy-icon="${slug}" data-annachy-icon-style="${style}" style="inline-size:${size}px;block-size:${size}px"${label ? ` role="img" aria-label="${esc(label)}"` : ' aria-hidden="true"'}></span>`;
export const button = ({ label, variant = 'primary', size = 48, attrs = '', left = '', right = '', full = false, aria = '' }) =>
  `<button type="button" class="annachy-button annachy-button--${variant} annachy-button--size-${size}${full ? ' co-full' : ''}" ${attrs}${aria ? ` aria-label="${esc(aria)}"` : ''}>`
  + (left ? `<span class="annachy-button__icon" data-annachy-icon="${left}" data-annachy-icon-style="outline" aria-hidden="true"></span>` : '')
  + `<span class="annachy-button__label">${label}</span>`
  + (right ? `<span class="annachy-button__icon" data-annachy-icon="${right}" data-annachy-icon-style="outline" aria-hidden="true"></span>` : '')
  + '<span class="annachy-button__loading" aria-hidden="true"><span class="annachy-button__dot"></span><span class="annachy-button__dot"></span><span class="annachy-button__dot"></span></span></button>';
export const gradient = ({ label, size = 48, attrs = '', full = false }) =>
  `<button type="button" class="annachy-button-gradient annachy-button-gradient--size-${size}${full ? ' co-full' : ''}" ${attrs}><span class="annachy-button-gradient__label">${label}</span></button>`;
export const radio = ({ name, id, label, sub = '', checked = false, disabled = false, size = 'medium' }) =>
  `<div class="annachy-radio annachy-radio--${size}"><input class="annachy-radio__input" type="radio" name="${name}" id="${id}" value="${id}"${checked ? ' checked' : ''}${disabled ? ' disabled' : ''}${sub ? ` aria-describedby="${id}-s"` : ''}>`
  + `<span class="annachy-radio__circle" aria-hidden="true"><span class="annachy-radio__dot"></span></span><span class="annachy-radio__content"><label class="annachy-radio__label" for="${id}">${label}</label>`
  + (sub ? `<span class="annachy-radio__subtext" id="${id}-s">${sub}</span>` : '') + '</span></div>';
export const toggle = ({ id, label, sub = '', checked = false }) =>
  `<div class="annachy-toggle annachy-toggle--medium annachy-toggle--control-right"><input class="annachy-toggle__input" type="checkbox" role="switch" id="${id}"${checked ? ' checked' : ''}${sub ? ` aria-describedby="${id}-s"` : ''}>`
  + `<span class="annachy-toggle__track" aria-hidden="true"><span class="annachy-toggle__thumb"></span></span><span class="annachy-toggle__content"><label class="annachy-toggle__label" for="${id}">${label}</label>`
  + (sub ? `<span class="annachy-toggle__subtext" id="${id}-s">${sub}</span>` : '') + '</span></div>';
/* Free-delivery progress (goal-gradient). Track pattern from the Figma Desktop PDP progress bar (1375:31181): 6 px track,
   tertiary background, filled in the success colour once the group qualifies (brand blue while in progress). */
export const meter = (g, compact = false) => {
  const free = isFree(g);
  return `<div class="co-meter${free ? ' is-free' : ''}${compact ? ' is-compact' : ''}"><div class="co-meter__row">${icon(free ? 'alerts-check-circle' : 'delivery-truck', 20)}`
    + `<p class="annachy-text-body-xs-semibold">${free ? 'Free delivery unlocked' : `Add ${rs(toFree(g))} more for free delivery`}</p>`
    + `<span class="annachy-text-caption-small co-meter__goal">${rs(Math.min(subtotal(g), FREE_AT))} / ${rs(FREE_AT)}</span></div>`
    + `<span class="co-meter__track" role="progressbar" aria-label="${GROUPS[g].title}: progress to free delivery" aria-valuemin="0" aria-valuemax="${FREE_AT}" aria-valuenow="${Math.min(FREE_AT, subtotal(g))}"><span class="co-meter__fill" style="inline-size:${progress(g)}%"></span></span></div>`;
};
/* Product thumbnail: the real Annachy product photo where one exists in the design file; otherwise a neutral pack tile
   (grocery photography is not part of the design file — it must be supplied). */
export const thumb = (i, cls = '') => i.img
  ? `<span class="co-thumb co-thumb--photo ${cls}"><img src="${i.img}" alt="${esc(i.alt || i.name)}" loading="lazy" width="88" height="110"></span>`
  : `<span class="co-thumb co-thumb--pack ${cls}" aria-hidden="true">${icon(i.icon, 28)}<span class="annachy-text-caption-xsmall">${i.pack}</span></span>`;
/* Price block as on the PDP: selling price, struck-through MRP, green "% off". */
export const priceTag = (i, total = false) => {
  const q = total ? i.qty : 1;
  return `<span class="co-price"><span class="annachy-text-body-m-medium co-strong">${rs(i.price * q)}</span>`
    + `<s class="annachy-text-caption-small co-muted"><span class="co-sr">MRP </span>${rs(i.mrp * q)}</s><span class="annachy-text-caption-small co-success co-off">${off(i)}% off</span></span>`;
};
/* App chrome. Desktop: logo, delivery location, search, profile, cart (Figma header 1375:31289). Mobile: back, title, secure. */
const LOGO = '<img class="co-logo" src="../assets/vectors/logo-annachy-b8420.svg" alt="Annachy" width="157" height="39">';
export const appHeader = ({ title, sub = '', back = '', right = '' }) => `
  <header class="co-app">
    <div class="co-app__desk co-desktop-only"><a href="../../index.html" class="co-app__logo" aria-label="Annachy home">${LOGO}</a>
      <div class="co-app__loc">${icon('locations-pin', 24)}<div><p class="annachy-text-caption-small co-muted">Deliver to</p><p class="annachy-text-body-s-semibold">Chennai 600042</p></div></div>
      <div class="co-app__search">${icon('search-search-1', 20)}<input type="search" aria-label="Search" placeholder="Search for groceries, fashion and more" disabled></div>
      <nav class="co-app__nav" aria-label="Account"><span class="co-app__navitem">${icon('user-user-curved', 24)}<span class="annachy-text-body-s-medium">Profile</span></span>
        <span class="co-app__navitem">${icon('shopping-shopping-cart', 24)}<span class="annachy-text-body-s-medium">Cart</span><span class="co-badge annachy-text-caption-xsmall" aria-label="${count('grocery') + count('other')} items">${count('grocery') + count('other')}</span></span></nav></div>
    <div class="co-app__mob co-mobile-only">${back}<div class="co-app__title"><h1 class="annachy-text-h7">${title}</h1>${sub ? `<p class="annachy-text-caption-small co-muted">${sub}</p>` : ''}</div>
      <span class="co-app__secure annachy-text-caption-xsmall">${icon('security-shield-done', 16)}100% secure</span></div>
    ${right}
  </header>`;
export const addressBar = () => `<div class="co-address">${icon('locations-pin', 24)}<div class="co-address__text"><p class="annachy-text-body-s"><span class="annachy-text-body-s-semibold">Deliver to Priya Raman</span> · Home</p>
  <p class="annachy-text-caption-small co-muted">12, 3rd Street, TNHB Colony, Velachery, Chennai 600042</p></div>${button({ label: 'Change', variant: 'link', size: 46, aria: 'Change delivery address' })}</div>`;
export const savingsStrip = () => (savings() > 0 ? `<div class="co-save">${icon('shopping-discount-badge', 20)}<p class="annachy-text-body-s-semibold">You're saving ${rs(savings())} on this order</p></div>` : '');
export const trust = () => `<ul class="co-trust annachy-text-caption-xsmall" aria-label="Why shop with us">
  <li>${icon('security-shield-done', 20)}<span>Secure payments</span></li><li>${icon('delivery-truck-check-complete', 20)}<span>Tracked delivery</span></li><li>${icon('alerts-check-badge', 20)}<span>100% genuine</span></li></ul>`;
/* Price details (every real checkout has one): MRP total, discount, delivery per group, total, savings. */
export const priceDetails = (cta = '') => {
  const g = activeGroups(); const n = g.reduce((t, k) => t + count(k), 0); const mrp = g.reduce((t, k) => t + mrpTotal(k), 0);
  return `<section class="co-card co-bill" aria-labelledby="h-bill"><div class="co-card__head"><h2 id="h-bill" class="annachy-text-h8">Price details</h2></div><div class="co-card__body">
    <dl class="co-lines annachy-text-body-s"><div class="co-between"><dt>Price (${n} item${n === 1 ? '' : 's'})</dt><dd>${rs(mrp)}</dd></div>
      <div class="co-between"><dt>Discount</dt><dd class="co-success">− ${rs(savings())}</dd></div>
      ${g.map((k) => `<div class="co-between"><dt>${GROUPS[k].title} delivery</dt><dd>${fee(k) ? rs(fee(k)) : '<span class="co-success">FREE</span>'}</dd></div>`).join('')}
      <div class="co-between co-total"><dt class="annachy-text-body-m-medium">Total amount</dt><dd class="annachy-text-h8 co-total__v">${rs(total())}</dd></div></dl>
    ${savings() > 0 ? `<p class="co-save annachy-text-body-xs-semibold">${icon('shopping-discount-badge', 16)}You will save ${rs(savings())} on this order</p>` : ''}
    <p class="annachy-text-caption-xsmall co-muted">Free delivery is worked out separately for each group (${rs(FREE_AT)} and above).</p>${cta}</div></section>`;
};

/* ---------- interaction helpers ---------- */
let live;
export const announce = (msg) => { live = live || document.getElementById('co-live'); if (live) { live.textContent = ''; setTimeout(() => { live.textContent = msg; }, 30); } };
export const icons = (root = document) => fillIconSlots(root);
export const busy = (btn, on) => { btn.setAttribute('aria-busy', on ? 'true' : 'false'); if (on) btn.setAttribute('aria-disabled', 'true'); else btn.removeAttribute('aria-disabled'); };
export const setQty = (id, delta) => {
  const n = Math.max(0, Math.min(10, state.qty[id] + delta));
  if (n === 0) state.removed.push(id); state.qty[id] = n || 1; save();
};
export const remove = (id) => { state.removed.push(id); save(); };
/* Scenario "slot-soldout": the first slot chosen sells out ~1.2 s later; the next free slot on the same day is selected. */
export const chooseSlot = (id, onChange) => {
  state.slot = id; save(); onChange();
  if (scenario === 'slot-soldout' && !state.soldOut.length) {
    setTimeout(() => {
      if (state.slot !== id) return;
      state.soldOut.push(id);
      // nearest LATER free slot (same day, then following days); an earlier slot only if nothing later is free
      const all = Object.values(slots).flat(); const k = all.findIndex((s) => s.id === id);
      const next = all.slice(k + 1).find((s) => !isFull(s)) || all.slice(0, k).reverse().find((s) => !isFull(s));
      const was = Object.values(slots).flat().find((s) => s.id === id);
      state.slot = next ? next.id : null; state.day = next ? dayOf(next.id).id : state.day; save();
      onChange({ soldOut: was, picked: next });
      announce(`${was.time} just filled up. We picked ${next ? next.time : 'no slot'} instead — you can change it.`);
    }, 1200);
  }
};
/* Payment: simulated gateway. Scenario "payment-fail" fails the first attempt. */
export const pay = (groupsToPay) => new Promise((resolve) => {
  state.payAttempts += 1; save();
  setTimeout(() => {
    const ok = !(scenario === 'payment-fail' && state.payAttempts === 1);
    if (ok) { groupsToPay.forEach((g) => { state.paid[g] = true; }); save(); }
    resolve(ok);
  }, 1400);
});
/* Prototype-only control bar (not part of the design): scenario links and reset. */
export const protoBar = (page) => {
  const bar = document.createElement('nav'); bar.className = 'co-proto'; bar.setAttribute('aria-label', 'Prototype controls (not part of the design)');
  bar.innerHTML = `<span class="annachy-text-caption-xsmall">Prototype scenario:</span> ` + Object.entries(SCENARIOS)
    .map(([k, v]) => `<a href="${page}?scenario=${k}"${k === scenario ? ' aria-current="true"' : ''} title="${esc(v)}">${k}</a>`).join(' · ')
    + ` · <button type="button" class="co-proto__reset">Reset</button>`;
  bar.querySelector('.co-proto__reset').addEventListener('click', reset);
  document.body.prepend(bar);
};
/* Opening the confirmation directly (review board): use the first available slot as a sample so the screen is complete. */
export const previewFill = () => { if (!state.slot) { const s = Object.values(slots).flat().find((x) => !isFull(x)); if (s) { state.slot = s.id; save(); } } };
export const link = (page) => `${page}${scenario === 'default' ? '' : `?scenario=${scenario}`}`;

/* ---------- shared screen pieces (both directions) ---------- */
export const stepBar = (n) => `<ol class="co-prog annachy-text-caption-small co-mobile-only" aria-label="Checkout steps">${['Cart', 'Delivery & payment', 'Done']
  .map((s, i) => `<li${i < n ? ' class="is-done"' : ''}${i === n ? ' aria-current="step"' : ''}>${s}</li>`).join('')}</ol>`;
export const crumb = (...parts) => `<nav class="co-crumb co-desktop-only annachy-text-body-xs" aria-label="Breadcrumb"><ol>${parts.map((p, i) => `<li${i === parts.length - 1 ? ' aria-current="page"' : ''}>${p}</li>`).join('')}</ol></nav>`;
export const backBtn = (attr, label) => button({ label: '', variant: 'tertiary-grey', size: 46, attrs: attr, aria: label, left: 'arrow-chevron-left' });
export const nItems = () => count('grocery') + count('other');
export const subline = () => `${activeGroups().length} shipment${activeGroups().length === 1 ? '' : 's'} · ${nItems()} item${nItems() === 1 ? '' : 's'}`;
export const shipNo = (g) => activeGroups().indexOf(g) + 1;
export const feePill = (g) => `<span class="co-pill annachy-text-caption-small ${isFree(g) ? 'is-free' : 'is-fee'}">${isFree(g) ? 'FREE delivery' : `${rs(FEE)} delivery`}</span>`;
export const strip = (g) => (items(g).some((i) => i.img)
  ? `<div class="co-strip" aria-hidden="true">${items(g).slice(0, 4).map((i) => thumb(i, 'co-thumb--sm')).join('')}${items(g).length > 4 ? `<span class="annachy-text-caption-small co-muted">+${items(g).length - 4}</span>` : ''}</div>`
  : `<p class="annachy-text-caption-small co-muted">${items(g).map((i) => i.name).join(' · ')}</p>`);   // no photos in the design file for this group: names instead of empty tiles
