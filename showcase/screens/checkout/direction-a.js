/*
 * Direction A — "Classic marketplace". The pattern shoppers already know (Jakob): app header, delivery address bar,
 * one card per shipment with its own free-delivery meter (Miller, goal-gradient), product rows with photo / price / MRP /
 * % off, a price-details card and a sticky thumb-zone bar (Fitts). Choices are core Radio buttons in 48 px tiles with
 * defaults pre-selected (Hick).
 */
import * as C from './checkout-core.js';

const screen = document.body.dataset.screen;
const root = document.getElementById('co-root');
const page = { cart: 'a-cart.html', delivery: 'a-delivery.html', confirmation: 'a-confirmation.html' };
C.protoBar(page[screen]);

const nItems = () => C.count('grocery') + C.count('other');
const progress = (n) => `<ol class="co-prog annachy-text-caption-small co-mobile-only" aria-label="Checkout steps">${['Cart', 'Delivery & payment', 'Done']
  .map((s, i) => `<li${i < n ? ' class="is-done"' : ''}${i === n ? ' aria-current="step"' : ''}>${s}</li>`).join('')}</ol>`;
const crumb = (...parts) => `<nav class="co-crumb co-desktop-only annachy-text-body-xs" aria-label="Breadcrumb"><ol>${parts.map((p, i) => `<li${i === parts.length - 1 ? ' aria-current="page"' : ''}>${p}</li>`).join('')}</ol></nav>`;
const backBtn = (attr, label) => C.button({ label: '', variant: 'tertiary-grey', size: 46, attrs: attr, aria: label, left: 'arrow-chevron-left' });
const sub = () => `${C.activeGroups().length} shipment${C.activeGroups().length === 1 ? '' : 's'} · ${nItems()} item${nItems() === 1 ? '' : 's'}`;
const shipNo = (g) => C.activeGroups().indexOf(g) + 1;

/* ---------- 1. Cart ---------- */
function itemRow(i) {
  if (i.unavailable) {
    return `<li class="co-item is-unavailable">${C.thumb(i)}<div class="co-item__main"><p class="annachy-text-body-s-medium co-item__title">${i.name}</p>
      <p class="annachy-text-caption-small co-error">No longer available — not included in your total</p>
      <div class="co-item__actions">${C.button({ label: 'Remove', variant: 'secondary-grey', size: 46, attrs: `data-remove="${i.id}"`, aria: `Remove ${i.name}` })}</div></div></li>`;
  }
  return `<li class="co-item">${C.thumb(i)}<div class="co-item__main">
    <div><p class="annachy-text-body-s-medium co-item__title">${i.name}</p><p class="annachy-text-caption-small co-muted">${i.unit}</p></div>
    ${C.priceTag(i)}
    <div class="co-item__actions"><div class="co-stepper" role="group" aria-label="Quantity of ${i.name}">
      ${C.button({ label: i.qty === 1 ? '' : '−', variant: 'tertiary-grey', size: 46, attrs: `data-qty="${i.id}" data-d="-1"`, aria: i.qty === 1 ? `Remove ${i.name}` : `Decrease ${i.name}`, left: i.qty === 1 ? 'editor-delete-trash' : '' })}
      <output class="annachy-text-body-s-semibold" aria-live="polite">${i.qty}</output>
      ${C.button({ label: '+', variant: 'tertiary-grey', size: 46, attrs: `data-qty="${i.id}" data-d="1"${i.qty >= 10 ? ' disabled' : ''}`, aria: `Increase ${i.name}` })}</div>
      ${i.qty > 1 ? `<p class="annachy-text-body-s-semibold">${C.rs(i.price * i.qty)}</p>` : ''}</div></div></li>`;
}
function shipHead(g, subline, pill) {
  return `<div class="co-ship__head"><span class="co-ship__tile">${C.icon(C.GROUPS[g].icon, 24)}</span><div class="co-ship__title"><h2 id="h-${g}" class="annachy-text-h8">Shipment ${shipNo(g)} · ${C.GROUPS[g].title}</h2>
    <p class="annachy-text-caption-small co-muted">${subline}</p></div>${pill}</div>`;
}
const feePill = (g) => `<span class="co-pill annachy-text-caption-small ${C.isFree(g) ? 'is-free' : 'is-fee'}">${C.isFree(g) ? 'FREE delivery' : `${C.rs(C.FEE)} delivery`}</span>`;
function groupCard(g) {
  const list = C.items(g); if (!list.length) return '';
  return `<section class="co-card co-ship co-ship--${g}" aria-labelledby="h-${g}">${shipHead(g, `${C.count(g)} item${C.count(g) === 1 ? '' : 's'} · ${g === 'grocery' ? 'delivered in a time slot you choose' : 'standard or same-day'}`, feePill(g))}
    <div class="co-card__body">${C.meter(g)}<ul>${list.map(itemRow).join('')}</ul></div>
    <div class="co-card__foot annachy-text-body-s"><div class="co-between"><span class="co-muted">Subtotal</span><span>${C.rs(C.subtotal(g))}</span></div>
      <div class="co-between"><span class="co-muted">Delivery</span><span>${C.isFree(g) ? '<span class="co-success">Free</span>' : C.rs(C.FEE)}</span></div></div></section>`;
}
function renderCart() {
  const cta = C.button({ label: 'Continue to delivery', size: 52, full: true, attrs: 'data-next', right: 'arrow-chevron-right' });
  const groups = Object.keys(C.GROUPS).map(groupCard).join('');
  root.innerHTML = `${C.appHeader({ title: 'My cart', sub: sub(), back: backBtn('data-home', 'Back to shopping') })}${progress(0)}${crumb('Home', 'Cart')}
    <div class="co-wrap">${groups ? `<div class="co-pagehead"><h1 class="annachy-text-h4">My cart <span class="annachy-text-body-m co-muted">(${sub()})</span></h1></div>
      ${C.addressBar()}${C.savingsStrip()}
      <div class="co-grid"><div class="co-main">${groups}</div><aside class="co-aside" aria-label="Order total">${C.priceDetails(`<div class="co-desktop-only">${cta}</div>`)}${C.trust()}</aside></div>`
      : `<div class="co-card co-hero" style="background:none;color:inherit"><h2 class="annachy-text-h5">Your cart is empty</h2></div>`}</div>
    <div class="co-bar co-mobile-only"><div><span class="annachy-text-caption-small co-muted">Total</span><span class="annachy-text-h8">${C.rs(C.total())}</span></div>${cta}</div>`;
}

/* ---------- 2. Delivery & payment ---------- */
const option = (inner, extra = '') => `<div class="co-option"${extra}>${inner}</div>`;
const strip = C.strip;
let slotNote = '', payError = '';
function slotSection() {
  const day = C.state.day; const pick = C.slotObj();
  return `<section class="co-card co-ship co-ship--grocery" aria-labelledby="h-grocery">${shipHead('grocery', `${C.count('grocery')} items · pick a slot`, feePill('grocery'))}
    <div class="co-card__body">${strip('grocery')}${slotNote}
      ${pick ? `<div class="co-eta">${C.icon('time-circle-clock', 20)}<p class="annachy-text-body-s-semibold">Arrives ${C.dayOf(pick.id).label} · ${pick.time}</p></div>` : ''}
      <fieldset class="co-stack" style="border:0;padding:0;margin:0"><legend class="annachy-text-body-s-semibold" style="margin-block-end:var(--co-s8)">Choose a day</legend>
        <div class="co-days">${C.days.map((d) => option(C.radio({ name: 'day', id: d.id, label: d.label, sub: d.short, checked: d.id === day, size: 'small' }))).join('')}</div></fieldset>
      <fieldset class="co-stack" style="border:0;padding:0;margin:0"><legend class="annachy-text-body-s-semibold" style="margin-block-end:var(--co-s8)">Choose a time slot</legend>
        <div class="co-slots">${C.slots[day].map((s) => option(C.radio({ name: 'slot', id: s.id, label: s.time, sub: C.isFull(s) ? 'Full' : 'Available', checked: C.state.slot === s.id, disabled: C.isFull(s), size: 'small' }))).join('')}</div></fieldset>
      ${pick ? '' : '<p class="annachy-text-caption-small co-muted" id="slot-hint">Choose a slot to continue. Full slots can\'t be picked.</p>'}</div></section>`;
}
function otherSection() {
  if (!C.count('other')) return '';
  return `<section class="co-card co-ship co-ship--other" aria-labelledby="h-other">${shipHead('other', `${C.count('other')} item · choose delivery speed`, feePill('other'))}
    <div class="co-card__body">${strip('other')}<div class="co-options" role="radiogroup" aria-labelledby="h-other">${C.OTHER_OPTIONS.map((o) => {
      const p = o.price(C.subtotal('other'));
      return option(C.radio({ name: 'other', id: o.id, label: o.title, sub: o.promise(), checked: C.state.other === o.id })
        + `<span class="co-option__side">${o.id === 'express' ? '<span class="co-tag annachy-text-caption-xsmall">FASTEST</span>' : ''}<span class="annachy-text-body-s-semibold${p ? '' : ' co-success'}">${p ? C.rs(p) : 'FREE'}</span></span>`);
    }).join('')}</div>${C.isFree('other') || C.state.other === 'express' ? '' : C.meter('other')}</div></section>`;
}
function paySection() {
  const methods = [['upi', 'UPI', 'Pay with any UPI app', 'banking-wallet-add-funds'], ['card', 'Debit or credit card', 'Visa, Mastercard, RuPay', 'banking-bank-card'], ['cod', 'Cash on delivery', 'Pay when each shipment arrives', 'delivery-delivery-box']];
  return `<section class="co-card" aria-labelledby="h-pay"><div class="co-card__head">${C.icon('banking-bank-card', 24)}<h2 id="h-pay" class="annachy-text-h8">Payment</h2></div>
    <div class="co-card__body"><div class="co-options" role="radiogroup" aria-label="How to pay">
      ${option(C.radio({ name: 'mode', id: 'together', label: 'Pay for both together', sub: 'One payment for the whole order (recommended)', checked: C.state.payMode === 'together' }))}
      ${option(C.radio({ name: 'mode', id: 'separate', label: 'Pay for each shipment separately', sub: 'Grocery and other items as two payments', checked: C.state.payMode === 'separate' }))}</div>
      <div class="co-options" role="radiogroup" aria-label="Payment method">${methods.map(([id, l, s, ic]) => option(`<span class="co-method">${C.icon(ic, 24)}</span>` + C.radio({ name: 'method', id, label: l, sub: s, checked: C.state.method === id }))).join('')}</div>
      <p class="co-row annachy-text-caption-small co-muted">${C.icon('security-shield-done', 16)} Secure payment. You're only charged once your order is placed.</p></div></section>`;
}
function payButtons() {
  const sep = C.state.payMode === 'separate'; const can = !!C.state.slot || !C.count('grocery');
  const dis = can ? '' : ' aria-disabled="true" aria-describedby="slot-hint"';
  if (!sep) return C.button({ label: `Pay ${C.rs(C.total())}`, size: 52, full: true, attrs: `data-pay="all"${dis}`, left: 'security-lock' });
  return C.activeGroups().map((g) => (C.state.paid[g]
    ? `<p class="co-row annachy-text-body-s co-success">${C.icon('alerts-check-circle', 20)} ${C.GROUPS[g].title} paid</p>`
    : C.button({ label: `Pay ${C.rs(C.groupTotal(g))} · ${C.GROUPS[g].title}`, variant: g === 'grocery' ? 'primary' : 'secondary', size: 52, full: true, attrs: `data-pay="${g}"${dis}` }))).join('');
}
function renderDelivery() {
  const addr = `<section class="co-card" aria-labelledby="h-addr"><div class="co-card__head">${C.icon('locations-pin', 24)}<h2 id="h-addr" class="annachy-text-h8">Delivering to</h2>
      ${C.button({ label: 'Change', variant: 'link', size: 46, aria: 'Change delivery address' })}</div>
    <div class="co-card__body"><div><p class="annachy-text-body-s-semibold">Home · Priya Raman</p><p class="annachy-text-body-s co-muted">12, 3rd Street, TNHB Colony, Velachery, Chennai 600042</p></div>
    <p class="annachy-text-caption-small co-muted">Both shipments go to this address.</p></div></section>`;
  root.innerHTML = `${C.appHeader({ title: 'Delivery & payment', sub: sub(), back: backBtn('data-back', 'Back to cart') })}${progress(1)}${crumb('Home', 'Cart', 'Delivery &amp; payment')}
    <div class="co-wrap"><div class="co-pagehead"><h1 class="annachy-text-h4">Delivery &amp; payment</h1></div>
    <div class="co-grid"><div class="co-main">${addr}${C.count('grocery') ? slotSection() : ''}${otherSection()}${paySection()}</div>
    <aside class="co-aside" aria-label="Order summary">${payError}${C.priceDetails(`<div class="co-stack co-desktop-only">${payButtons()}</div>`)}${C.trust()}</aside></div></div>
    <div class="co-bar co-mobile-only"><div><span class="annachy-text-caption-small co-muted">To pay</span><span class="annachy-text-h8">${C.rs(C.total())}</span></div><div class="co-stack">${payButtons()}</div></div>`;
}

/* ---------- 3. Confirmation ---------- */
function renderConfirmation() {
  C.previewFill();
  const s = C.slotObj(); const d = s && C.dayOf(s.id); const o = C.OTHER_OPTIONS.find((x) => x.id === C.state.other);
  const ship = (g, when, how) => `<section class="co-card co-ship co-ship--${g}" aria-labelledby="h-c-${g}"><div class="co-ship__head"><span class="co-ship__tile">${C.icon(C.GROUPS[g].icon, 24)}</span>
      <div class="co-ship__title"><h2 id="h-c-${g}" class="annachy-text-h8">${C.GROUPS[g].shipment}</h2><p class="annachy-text-caption-small co-muted">Shipment ${shipNo(g)} of ${C.activeGroups().length}</p></div>
      <span class="co-pill annachy-text-caption-small is-free">${C.icon('alerts-check-circle', 16)}Confirmed</span></div>
    <div class="co-card__body"><div class="co-eta">${C.icon(g === 'grocery' ? 'time-circle-clock' : 'delivery-truck', 24)}<div><p class="annachy-text-body-m-medium">${when}</p><p class="annachy-text-caption-small co-muted">${how}</p></div></div>
      <ul>${C.items(g).filter((i) => !i.unavailable).map((i) => `<li class="co-item">${C.thumb(i, 'co-thumb--sm')}<div class="co-item__main"><p class="annachy-text-body-s-medium co-item__title">${i.name}</p>
        <p class="annachy-text-caption-small co-muted">${i.unit} · Qty ${i.qty}</p></div></li>`).join('')}</ul>
      <div class="co-between annachy-text-body-s"><span class="co-muted">Paid for this shipment</span><span class="annachy-text-body-s-semibold">${C.rs(C.groupTotal(g))}</span></div></div></section>`;
  root.innerHTML = `${C.appHeader({ title: 'Order placed', sub: '' })}
    <div class="co-hero"><span class="co-hero__badge">${C.icon('alerts-check-circle', 40, 'filled')}</span><h1 class="annachy-text-h4">Order placed!</h1>
      <p class="annachy-text-body-m">Thank you, Priya. It arrives in ${C.activeGroups().length} shipment${C.activeGroups().length > 1 ? 's' : ''}.</p>
      <p class="co-hero__order annachy-text-body-s-semibold">Order #AN-24816 · ${C.rs(C.total())} paid</p></div>
    <div class="co-wrap co-confirm">${C.count('grocery') ? ship('grocery', s ? `${d.label}, ${d.date} · ${s.time}` : 'Slot not chosen', 'Time-slot delivery') : ''}
      ${C.count('other') ? ship('other', o.promise(), o.title) : ''}
      <section class="co-card" aria-labelledby="h-next"><div class="co-card__head"><h2 id="h-next" class="annachy-text-h8">What's next</h2></div><div class="co-card__body"><div class="co-next co-next--row">
        ${C.button({ label: 'Track shipments', size: 52, left: 'delivery-delivery-location-2' })}
        ${C.button({ label: 'Edit order or slot', variant: 'secondary', size: 52, left: 'delivery-delivery-edit-2' })}
        ${C.button({ label: 'Get help', variant: 'tertiary', size: 52, left: 'audio-headphone' })}</div>
        <p class="annachy-text-caption-small co-muted">You can change the grocery slot until 2 hours before it starts. We'll send updates by SMS.</p></div></section>${C.trust()}</div>`;
}

/* ---------- events ---------- */
function render() { ({ cart: renderCart, delivery: renderDelivery, confirmation: renderConfirmation })[screen](); C.icons(root); }
root.addEventListener('click', async (e) => {
  const b = e.target.closest('button'); if (!b || b.getAttribute('aria-disabled') === 'true') return;
  if (b.dataset.qty) { const id = b.dataset.qty, d = +b.dataset.d; const name = b.closest('.co-item').querySelector('.co-item__title').textContent;
    C.setQty(id, d); render(); C.announce(`${name}: quantity ${C.state.removed.includes(id) ? 'removed' : C.state.qty[id]}. Total ${C.rs(C.total())}.`);
    (root.querySelector(`[data-qty="${id}"][data-d="${d}"]`) || root).focus(); return; }
  if (b.dataset.remove) { C.remove(b.dataset.remove); render(); C.announce('Item removed. Totals updated.'); root.focus(); return; }
  if ('next' in b.dataset) { location.href = C.link(page.delivery); return; }
  if ('back' in b.dataset) { location.href = C.link(page.cart); return; }
  if ('home' in b.dataset) { location.href = 'index.html'; return; }
  if (b.dataset.pay) {
    const groups = b.dataset.pay === 'all' ? C.activeGroups() : [b.dataset.pay];
    C.busy(b, true); C.announce('Processing payment…'); payError = '';
    const ok = await C.pay(groups);
    if (!ok) { payError = `<div class="co-alert co-alert--error" role="alert">${C.icon('alerts-error-circle', 24)}<div><p class="annachy-text-body-s-semibold">Payment didn't go through</p>
      <p class="annachy-text-caption-small">You haven't been charged. Your cart and slot are saved — try again or choose another method.</p></div></div>`; render(); root.querySelector('[role="alert"]').scrollIntoView({ block: 'nearest' }); return; }
    if (C.activeGroups().every((g) => C.state.paid[g])) { location.href = C.link(page.confirmation); return; }
    render(); C.announce('Payment received for one shipment.');
  }
});
root.addEventListener('change', (e) => {
  const t = e.target;
  if (t.name === 'day') { C.state.day = t.id; C.save(); render(); root.querySelector(`#${t.id}`).focus(); }
  if (t.name === 'slot') { slotNote = ''; C.chooseSlot(t.id, (ev) => {
    if (ev && ev.soldOut) slotNote = `<div class="co-alert co-alert--warn" role="status">${C.icon('alerts-error-triangle', 24)}<div><p class="annachy-text-body-s-semibold">${ev.soldOut.time} just filled up</p>
      <p class="annachy-text-caption-small">We've picked ${ev.picked ? `${C.dayOf(ev.picked.id).label} ${ev.picked.time}` : 'no slot'} for you — change it if you like.</p></div></div>`;
    render(); const f = root.querySelector(`#${CSS.escape(C.state.slot || t.id)}`); if (f) f.focus(); }); }
  if (t.name === 'other') { C.state.other = t.id; C.save(); render(); root.querySelector(`#${t.id}`).focus(); C.announce(`Total ${C.rs(C.total())}.`); }
  if (t.name === 'mode') { C.state.payMode = t.id; C.save(); render(); root.querySelector(`#${t.id}`).focus(); }
  if (t.name === 'method') { C.state.method = t.id; C.save(); }
});
root.addEventListener('click', (e) => { const tile = e.target.closest('.co-option'); if (tile && !e.target.closest('input, label')) { const i = tile.querySelector('input'); if (i && !i.disabled) i.click(); } });
render();
