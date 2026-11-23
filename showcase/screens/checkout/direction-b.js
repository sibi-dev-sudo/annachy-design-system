/*
 * Direction B — "Quick commerce". Delivery promise first: a banner says how the order arrives; everything sits in ONE
 * compact sheet with grey shipment headers (Miller); the bill is tucked into an expandable row on mobile; the primary
 * action is the brand Gradient Button. Delivery is a numbered sequence of single decisions (Hick) where same-day and
 * "pay separately" are Toggles over sensible defaults; the confirmation is a delivery timeline (peak-end).
 */
import * as C from './checkout-core.js';

const screen = document.body.dataset.screen;
const root = document.getElementById('co-root');
const page = { cart: 'b-cart.html', delivery: 'b-delivery.html', confirmation: 'b-confirmation.html' };
C.protoBar(page[screen]);
let billOpen = false;
const std = C.OTHER_OPTIONS[0]; const same = C.OTHER_OPTIONS[1];
const eta = (g) => {
  const s = C.slotObj();
  if (g === 'grocery') return s ? `${C.dayOf(s.id).label} · ${s.time}` : 'Pick a slot below';
  return C.state.other === 'express' ? same.promise() : std.promise();
};

/* ---------- 1. Cart ---------- */
function row(i) {
  const act = i.unavailable
    ? C.button({ label: 'Remove', variant: 'secondary-grey', size: 46, attrs: `data-remove="${i.id}"`, aria: `Remove ${i.name}` })
    : `<div class="co-stepper" role="group" aria-label="Quantity of ${i.name}">
        ${C.button({ label: i.qty === 1 ? '' : '−', variant: 'tertiary-grey', size: 46, attrs: `data-qty="${i.id}" data-d="-1"`, aria: i.qty === 1 ? `Remove ${i.name}` : `Decrease ${i.name}`, left: i.qty === 1 ? 'editor-delete-trash' : '' })}
        <output class="annachy-text-body-s-semibold" aria-live="polite">${i.qty}</output>
        ${C.button({ label: '+', variant: 'tertiary-grey', size: 46, attrs: `data-qty="${i.id}" data-d="1"${i.qty >= 10 ? ' disabled' : ''}`, aria: `Increase ${i.name}` })}</div>
      ${i.qty > 1 ? `<p class="annachy-text-body-s-semibold">${C.rs(i.price * i.qty)}</p>` : ''}`;
  return `<li class="co-b-row${i.unavailable ? ' is-unavailable' : ''}">${C.thumb(i)}<div class="co-b-row__main">
    <p class="annachy-text-body-s-medium co-item__title">${i.name}</p>
    ${i.unavailable ? '<p class="annachy-text-caption-small co-error">No longer available · not charged</p>'
      : `<p class="annachy-text-caption-small co-muted">${i.unit}</p>${C.priceTag(i)}`}
    <div class="co-b-row__actions">${act}</div></div></li>`;
}
function section(g) {
  const list = C.items(g); if (!list.length) return '';
  return `<section class="co-sect" aria-labelledby="h-${g}"><div class="co-sect__head"><span class="co-ship__tile">${C.icon(C.GROUPS[g].icon, 24)}</span>
      <div><h2 id="h-${g}" class="annachy-text-h8">Shipment ${C.shipNo(g)} · ${C.GROUPS[g].title}</h2><p class="annachy-text-caption-small co-muted">${C.count(g)} item${C.count(g) === 1 ? '' : 's'} · ${g === 'grocery' ? 'Slot delivery' : 'Standard or same-day'}</p></div>${C.feePill(g)}</div>
    <div class="co-sect__body"><ul>${list.map(row).join('')}</ul></div><div class="co-sect__foot">${C.meter(g, true)}</div></section>`;
}
const promise = () => `<div class="co-promise">${C.icon('delivery-truck-time-clock', 28)}<div><p class="annachy-text-body-m-medium">Your order arrives in ${C.activeGroups().length} shipment${C.activeGroups().length > 1 ? 's' : ''}</p>
  <p class="annachy-text-caption-small">${C.activeGroups().map((g) => `${C.GROUPS[g].title}: ${g === 'grocery' ? 'pick a slot' : `by ${std.promise().replace('By ', '')}`}`).join(' · ')}</p></div></div>`;
const bill = (cta) => `<div class="co-bill-wrap"><button type="button" class="co-bill-toggle co-mobile-only co-card" aria-expanded="${billOpen}" aria-controls="bill-body" data-bill style="inline-size:100%;font:inherit;color:inherit;text-align:start;cursor:pointer;min-block-size:var(--co-touch)">
    <span class="co-between" style="padding:var(--co-s8) var(--co-s16)"><span><span class="annachy-text-body-s-semibold">Price details</span><span class="annachy-text-caption-small co-success" style="display:block">You save ${C.rs(C.savings())}</span></span>
    <span class="co-row"><span class="annachy-text-body-m-medium">${C.rs(C.total())}</span>${C.icon(billOpen ? 'arrow-chevron-down' : 'arrow-chevron-right', 20)}</span></span></button>
  <div id="bill-body" class="co-bill-body"${billOpen ? '' : ' hidden'}>${C.priceDetails(cta)}</div></div>`;
function renderCart() {
  const cta = C.gradient({ label: 'Choose delivery', size: 52, full: true, attrs: 'data-next' });
  root.innerHTML = `${C.appHeader({ title: 'Cart', sub: C.subline(), back: C.backBtn('data-home', 'Back to shopping') })}${C.stepBar(0)}${C.crumb('Home', 'Cart')}
    <div class="co-wrap"><div class="co-pagehead"><h1 class="annachy-text-h4">Cart <span class="annachy-text-body-m co-muted">(${C.subline()})</span></h1></div>
    ${C.activeGroups().length ? `<div class="co-grid"><div class="co-main">${promise()}${C.addressBar()}<div class="co-sheet">${Object.keys(C.GROUPS).map(section).join('')}</div></div>
      <aside class="co-aside" aria-label="Order total">${bill(`<div class="co-desktop-only">${cta}</div>`)}${C.trust()}</aside></div>`
      : '<div class="co-card co-card__body"><h2 class="annachy-text-h5">Your cart is empty</h2></div>'}</div>
    <div class="co-bar co-mobile-only"><div><span class="annachy-text-caption-small co-muted">To pay</span><span class="annachy-text-h8">${C.rs(C.total())}</span></div>${C.gradient({ label: 'Choose delivery', size: 48, full: true, attrs: 'data-next' })}</div>`;
}

/* ---------- 2. Delivery & payment ---------- */
const stepHead = (n, title, done) => `<div class="co-card__head"><span class="co-b-num annachy-text-body-s-semibold${done ? ' is-done' : ''}" aria-hidden="true">${done ? C.icon('alerts-checkmark', 16) : n}</span>
  <h2 id="s-${n}" class="annachy-text-h8">${title}</h2>${done ? `<span class="co-pill annachy-text-caption-small is-free">${C.icon('alerts-check-circle', 16)}Done</span>` : ''}</div>`;
let slotNote = '', payError = '';
function renderDelivery() {
  const s = C.slotObj(); const g = C.count('grocery'); const other = C.count('other');
  const days = `<div class="co-days" role="radiogroup" aria-label="Delivery day">${C.days.map((d) => `<div class="co-option">${C.radio({ name: 'day', id: d.id, label: d.label, sub: d.short, checked: C.state.day === d.id, size: 'small' })}</div>`).join('')}</div>`;
  const avail = C.slots[C.state.day].filter((x) => !C.isFull(x)); const full = C.slots[C.state.day].filter(C.isFull);
  const slotList = `<div class="co-options" role="radiogroup" aria-label="Time slot">${avail.map((x) => `<div class="co-option">${C.radio({ name: 'slot', id: x.id, label: x.time, checked: C.state.slot === x.id })}</div>`).join('')
    || '<p class="annachy-text-body-s co-muted">No slots left on this day — pick another day.</p>'}</div>${full.length ? `<p class="annachy-text-caption-small co-muted">Full: ${full.map((x) => x.time).join(', ')}</p>` : ''}`;
  const grocery = g ? `<section class="co-card" aria-labelledby="s-1">${stepHead(1, 'Grocery · pick a delivery slot', !!s)}<div class="co-card__body">${C.strip('grocery')}${slotNote}
      ${s ? `<div class="co-eta">${C.icon('time-circle-clock', 20)}<p class="annachy-text-body-s-semibold">Arrives ${C.dayOf(s.id).label} · ${s.time}</p></div>` : ''}${days}${slotList}</div></section>` : '';
  const n2 = g ? 2 : 1;
  const otherCard = other ? `<section class="co-card" aria-labelledby="s-${n2}">${stepHead(n2, 'Other items · delivery speed', true)}<div class="co-card__body">${C.strip('other')}
      <div class="co-eta">${C.icon('delivery-truck', 20)}<div><p class="annachy-text-body-s-semibold">${C.state.other === 'express' ? same.title : std.title} · ${C.fee('other') ? C.rs(C.fee('other')) : 'Free'}</p><p class="annachy-text-caption-small co-muted">${eta('other')}</p></div></div>
      <div class="co-option">${C.toggle({ id: 'express', label: `Get it today · ${C.rs(C.EXPRESS_FEE)}`, sub: `${same.promise()} instead of ${std.promise().replace('By ', '')}`, checked: C.state.other === 'express' })}</div>
      ${C.isFree('other') || C.state.other === 'express' ? '' : C.meter('other', true)}</div></section>` : '';
  const methods = [['upi', 'UPI', 'Any UPI app', 'banking-wallet-add-funds'], ['card', 'Card', 'Debit or credit', 'banking-bank-card'], ['cod', 'Cash on delivery', 'Pay at the door', 'delivery-delivery-box']];
  const pn = n2 + (other ? 1 : 0);
  const pay = `<section class="co-card" aria-labelledby="s-${pn}">${stepHead(pn, 'Payment', false)}<div class="co-card__body">
      <div class="co-options" role="radiogroup" aria-label="Payment method">${methods.map(([id, l, sub, ic]) => `<div class="co-option"><span class="co-method">${C.icon(ic, 24)}</span>${C.radio({ name: 'method', id, label: l, sub, checked: C.state.method === id })}</div>`).join('')}</div>
      <div class="co-option">${C.toggle({ id: 'separate', label: 'Pay for each shipment separately', sub: 'Off: one payment for the whole order', checked: C.state.payMode === 'separate' })}</div></div></section>`;
  const blocked = g && !C.state.slot;
  const btns = C.state.payMode === 'separate'
    ? C.activeGroups().map((k) => (C.state.paid[k] ? `<p class="co-row annachy-text-body-s co-success">${C.icon('alerts-check-circle', 20)} ${C.GROUPS[k].title} paid</p>`
      : C.gradient({ label: `Pay ${C.rs(C.groupTotal(k))} · ${C.GROUPS[k].title}`, size: 52, full: true, attrs: `data-pay="${k}"${blocked ? ' aria-disabled="true" disabled' : ''}` }))).join('')
    : C.gradient({ label: `Pay ${C.rs(C.total())} securely`, size: 52, full: true, attrs: `data-pay="all"${blocked ? ' aria-disabled="true" disabled' : ''}` });
  const ships = `<section class="co-card" aria-labelledby="h-ships"><div class="co-card__head"><h2 id="h-ships" class="annachy-text-h8">Your ${C.activeGroups().length} shipment${C.activeGroups().length > 1 ? 's' : ''}</h2></div>
    <div class="co-card__body">${C.activeGroups().map((k) => `<div class="co-b-ship"><p class="annachy-text-body-s-semibold co-row">${C.icon(C.GROUPS[k].icon, 20)}${C.GROUPS[k].title}</p>
      <p class="annachy-text-caption-small ${k === 'grocery' && !s ? 'co-error' : 'co-muted'}">${eta(k)}</p></div>`).join('')}
      ${blocked ? '<p id="b-hint" class="annachy-text-caption-small co-muted">Pick a grocery slot to continue.</p>' : ''}</div></section>`;
  root.innerHTML = `${C.appHeader({ title: 'Delivery & payment', sub: C.subline(), back: C.backBtn('data-back', 'Back to cart') })}${C.stepBar(1)}${C.crumb('Home', 'Cart', 'Delivery &amp; payment')}
    <div class="co-wrap"><div class="co-pagehead"><h1 class="annachy-text-h4">Delivery &amp; payment</h1></div><div class="co-grid"><div class="co-main">${C.addressBar()}${grocery}${otherCard}${pay}</div>
    <aside class="co-aside">${ships}${payError}${C.priceDetails(`<div class="co-stack co-desktop-only">${btns}</div>`)}${C.trust()}</aside></div></div>
    <div class="co-bar co-mobile-only"><div><span class="annachy-text-caption-small co-muted">To pay</span><span class="annachy-text-h8">${C.rs(C.total())}</span></div><div class="co-stack">${btns}</div></div>`;
}

/* ---------- 3. Confirmation ---------- */
function renderConfirmation() {
  C.previewFill();
  const s = C.slotObj(); const o = C.OTHER_OPTIONS.find((x) => x.id === C.state.other);
  const stop = (g, when, how) => `<li class="co-b-stop"><span class="co-b-dot" aria-hidden="true">${C.icon(g === 'grocery' ? 'time-circle-clock' : 'delivery-truck', 20)}</span>
    <div class="co-card"><div class="co-card__body"><div class="co-between"><div><p class="annachy-text-caption-small co-brand">${C.GROUPS[g].shipment}</p><p class="annachy-text-h8">${when}</p>
      <p class="annachy-text-caption-small co-muted">${how}</p></div><span class="annachy-text-body-s-semibold">${C.rs(C.groupTotal(g))}</span></div>${C.items(g).some((i) => i.img) ? C.strip(g) : ''}
      <details class="co-b-stopcard"><summary class="annachy-text-body-s co-brand">${C.count(g)} item${C.count(g) === 1 ? '' : 's'} in this shipment</summary><ul class="co-lines annachy-text-body-s">${C.items(g).filter((i) => !i.unavailable)
        .map((i) => `<li class="co-between"><span>${i.name} × ${i.qty}</span><span>${C.rs(i.price * i.qty)}</span></li>`).join('')}</ul></details></div></div></li>`;
  root.innerHTML = `${C.appHeader({ title: 'Order placed', sub: '' })}
    <div class="co-wrap co-confirm"><div class="co-save" style="padding:var(--co-s16);flex-direction:column;text-align:center;justify-content:center">${C.icon('alerts-check-circle', 48, 'filled')}
      <h1 class="annachy-text-h4 co-strong">You're all set, Priya</h1><p class="annachy-text-body-s co-muted">Order #AN-24816 · ${C.rs(C.total())} paid · confirmation sent by SMS</p></div>
    <h2 class="annachy-text-h8">What arrives, and when</h2>
    <ol class="co-b-timeline">${C.count('grocery') ? stop('grocery', s ? `${C.dayOf(s.id).label} · ${s.time}` : 'Slot not chosen', `${C.dayOf(s ? s.id : 'd0-').date} · time-slot delivery`) : ''}
      ${C.count('other') ? stop('other', o.promise(), o.title) : ''}</ol>
    <div class="co-next co-next--row">${C.button({ label: 'Track shipments', size: 52, left: 'delivery-delivery-location-2' })}
      ${C.button({ label: 'Edit slot or order', variant: 'secondary', size: 52, left: 'delivery-delivery-edit-2' })}
      ${C.button({ label: 'Get help', variant: 'tertiary', size: 52, left: 'audio-headphone' })}</div>
    <p class="annachy-text-caption-small co-muted">Need a different grocery slot? You can change it until 2 hours before it starts.</p>${C.trust()}</div>`;
}

/* ---------- events ---------- */
function render() { ({ cart: renderCart, delivery: renderDelivery, confirmation: renderConfirmation })[screen](); C.icons(root); }
root.addEventListener('click', async (e) => {
  const b = e.target.closest('button'); if (!b || b.getAttribute('aria-disabled') === 'true') return;
  if ('bill' in b.dataset) { billOpen = !billOpen; render(); root.querySelector('[data-bill]').focus(); return; }
  if (b.dataset.qty) { const id = b.dataset.qty, d = +b.dataset.d; C.setQty(id, d); render();
    C.announce(`Quantity ${C.state.removed.includes(id) ? 'removed' : C.state.qty[id]}. To pay ${C.rs(C.total())}.`);
    (root.querySelector(`[data-qty="${id}"][data-d="${d}"]`) || root).focus(); return; }
  if (b.dataset.remove) { C.remove(b.dataset.remove); render(); C.announce('Item removed. Totals updated.'); root.focus(); return; }
  if ('next' in b.dataset) { location.href = C.link(page.delivery); return; }
  if ('back' in b.dataset) { location.href = C.link(page.cart); return; }
  if ('home' in b.dataset) { location.href = 'index.html'; return; }
  if (b.dataset.pay) {
    const groups = b.dataset.pay === 'all' ? C.activeGroups() : [b.dataset.pay];
    const label = b.querySelector('span'); const was = label.textContent; label.textContent = 'Processing…'; b.setAttribute('aria-busy', 'true'); b.disabled = true;
    payError = ''; C.announce('Processing payment…');
    const ok = await C.pay(groups);
    if (!ok) { payError = `<div class="co-alert co-alert--error" role="alert">${C.icon('alerts-error-circle', 24)}<div><p class="annachy-text-body-s-semibold">Payment failed — you weren't charged</p>
      <p class="annachy-text-caption-small">Everything is saved. Try again, or switch to another method.</p></div></div>`; render(); root.querySelector('[role="alert"]').scrollIntoView({ block: 'nearest' }); return; }
    if (C.activeGroups().every((g) => C.state.paid[g])) { location.href = C.link(page.confirmation); return; }
    label.textContent = was; render(); C.announce('Payment received for one shipment.');
  }
});
root.addEventListener('change', (e) => {
  const t = e.target;
  if (t.name === 'day') { C.state.day = t.id; C.save(); render(); root.querySelector(`#${t.id}`).focus(); }
  if (t.name === 'slot') { slotNote = ''; C.chooseSlot(t.id, (ev) => {
    if (ev && ev.soldOut) slotNote = `<div class="co-alert co-alert--warn" role="status">${C.icon('alerts-error-triangle', 24)}<div><p class="annachy-text-body-s-semibold">Sorry — ${ev.soldOut.time} just sold out</p>
      <p class="annachy-text-caption-small">We moved you to ${ev.picked ? `${C.dayOf(ev.picked.id).label} ${ev.picked.time}` : 'no slot'}. Change it below if it doesn't suit you.</p></div></div>`;
    render(); const f = root.querySelector(`#${CSS.escape(C.state.slot || t.id)}`); if (f) f.focus(); }); }
  if (t.id === 'express') { C.state.other = t.checked ? 'express' : 'standard'; C.save(); render(); root.querySelector('#express').focus(); C.announce(`To pay ${C.rs(C.total())}.`); }
  if (t.id === 'separate') { C.state.payMode = t.checked ? 'separate' : 'together'; C.save(); render(); root.querySelector('#separate').focus(); }
  if (t.name === 'method') { C.state.method = t.id; C.save(); }
});
root.addEventListener('click', (e) => { const tile = e.target.closest('.co-option'); if (tile && !e.target.closest('input, label')) { const i = tile.querySelector('input'); if (i && !i.disabled) i.click(); } });
render();
