/*
 * Annachy Design System — Tooltip behaviour (R4-2)
 * WAI-ARIA APG Tooltip pattern + WCAG 2.2 SC 1.4.13 (dismissible, hoverable, persistent).
 * Approved: docs/implementation/r4-behaviour-spec.md §2 — R4-Q1 (pattern), R4-Q4 (show 500 ms on hover,
 * hide 150 ms, immediate on keyboard focus), R4-Q5 (touch: tap that focuses the trigger shows it).
 *
 * Markup: a focusable trigger with data-annachy-tooltip="<tooltip id>" and aria-describedby="<tooltip id>",
 * and a non-interactive .annachy-tooltip element with role="tooltip" and the `hidden` attribute.
 * Placement follows the tooltip's Figma Arrow modifier (arrow side → tooltip on the opposite side of the trigger);
 * on viewport collision only the 10 Figma placements are tried (T8).
 */
const SHOW_DELAY = 500;   // R4-Q4
const HIDE_DELAY = 150;   // R4-Q4
const ARROW_TIP_GAP = 12; // DERIVED: arrow box protrudes 13px; polygon tip sits 1px inside the box (5% of 20) → tip touches the trigger
const PLACEMENTS = ['left', 'left-center', 'right', 'right-center', 'top', 'top-left', 'top-right', 'bottom', 'bottom-left', 'bottom-right'];
const SIDE = { left: 'left', 'left-center': 'left', right: 'right', 'right-center': 'right', top: 'top', 'top-left': 'top', 'top-right': 'top',
  bottom: 'bottom', 'bottom-left': 'bottom', 'bottom-right': 'bottom' };
const OPPOSITE = { left: 'right', right: 'left', top: 'bottom', bottom: 'top' };
const BY_SIDE = { left: ['left', 'left-center'], right: ['right', 'right-center'], top: ['top', 'top-left', 'top-right'], bottom: ['bottom', 'bottom-left', 'bottom-right'] };

let current = null;            // currently visible controller (T17: one at a time)
let lastPointer = 'mouse';
const controllers = new WeakMap();

if (typeof document !== 'undefined') {
  document.addEventListener('pointerdown', (e) => {
    lastPointer = e.pointerType || 'mouse';
    if (current && !current.trigger.contains(e.target) && !current.tip.contains(e.target)) current.hide();   // T3: tap outside
  }, true);
  document.addEventListener('keydown', (e) => {           // T5: Escape dismisses without moving focus
    if (e.key === 'Escape' && current) { current.dismissed = true; current.hide(); e.stopPropagation(); }
  }, true);
}

const arrowOf = (tip) => (PLACEMENTS.find((p) => tip.classList.contains(`annachy-tooltip--arrow-${p}`)) || 'left');

class Tooltip {
  constructor(trigger, tip) {
    this.trigger = trigger;
    this.tip = tip;
    this.preferred = arrowOf(tip);
    this.timer = 0;
    this.dismissed = false;
    this.overTrigger = false;
    this.overTip = false;
    tip.hidden = true;
    // A new hover always re-arms the tooltip after an Escape dismissal (T5: "reappears on the next hover or focus").
    trigger.addEventListener('pointerenter', (e) => { if (e.pointerType === 'touch') return; this.overTrigger = true; this.dismissed = false; this.schedule(true); });
    trigger.addEventListener('pointerleave', (e) => { if (e.pointerType === 'touch') return; this.overTrigger = false; this.dismissed = false; this.schedule(false); });
    tip.addEventListener('pointerenter', () => { this.overTip = true; clearTimeout(this.timer); });              // T6 hoverable
    tip.addEventListener('pointerleave', () => { this.overTip = false; this.schedule(false); });
    trigger.addEventListener('focus', () => {                                                                   // T2 / T3
      if (trigger.matches(':focus-visible') || lastPointer === 'touch') { this.dismissed = false; this.show(); }
    });
    trigger.addEventListener('blur', () => { if (!this.overTrigger && !this.overTip) this.hide(); });
  }

  schedule(show) {
    clearTimeout(this.timer);
    if (show) {
      if (this.dismissed) return;
      const warm = current && current !== this;                       // warm-up: another tooltip open → immediate
      this.timer = setTimeout(() => this.show(), warm ? 0 : SHOW_DELAY);
    } else {
      this.timer = setTimeout(() => { if (!this.overTrigger && !this.overTip && document.activeElement !== this.trigger) this.hide(); }, HIDE_DELAY);
    }
  }

  show() {
    clearTimeout(this.timer);
    if (current && current !== this) current.hide();
    current = this;
    this.tip.hidden = false;
    this.tip.classList.add('is-floating');
    this.place();
  }

  hide() {
    clearTimeout(this.timer);
    this.tip.hidden = true;
    this.setArrow(this.preferred);
    if (current === this) current = null;
  }

  setArrow(p) {
    for (const q of PLACEMENTS) this.tip.classList.toggle(`annachy-tooltip--arrow-${q}`, q === p);
  }

  // coordinates for a placement; the arrow box centre is aligned with the trigger centre
  coords(p, t, w, h) {
    const side = SIDE[p], cx = t.left + t.width / 2, cy = t.top + t.height / 2;
    const cs = getComputedStyle(this.tip);
    const ox = parseFloat(cs.getPropertyValue('--_tt-cx')) || 0, oy = parseFloat(cs.getPropertyValue('--_tt-cy')) || 0;
    let x, y;
    if (side === 'left' || side === 'right') {
      x = side === 'left' ? t.right + ARROW_TIP_GAP : t.left - ARROW_TIP_GAP - w;   // arrow on the left → tooltip right of trigger
      y = p.endsWith('center') ? cy - h / 2 - oy : cy - (9 + 10);                   // arrow box: top 9, 20 tall
    } else {
      y = side === 'top' ? t.bottom + ARROW_TIP_GAP : t.top - ARROW_TIP_GAP - h;   // arrow on top → tooltip below trigger
      if (p.endsWith('left')) x = cx - (12 + 10);
      else if (p.endsWith('right')) x = cx - (w - 12 - 10);
      else x = cx - w / 2 - ox;
    }
    return { x, y };
  }

  place() {
    const t = this.trigger.getBoundingClientRect(), vw = document.documentElement.clientWidth, vh = document.documentElement.clientHeight;
    const side = SIDE[this.preferred];
    const order = [this.preferred, ...BY_SIDE[side].filter((p) => p !== this.preferred), ...BY_SIDE[OPPOSITE[side]],
      ...Object.keys(BY_SIDE).filter((s) => s !== side && s !== OPPOSITE[side]).flatMap((s) => BY_SIDE[s])];
    let chosen = this.preferred, pos = null;
    for (const p of order) {                                           // T8: only Figma placements
      this.setArrow(p);
      const { width: w, height: h } = this.tip.getBoundingClientRect();
      const c = this.coords(p, t, w, h);
      if (c.x >= 0 && c.y >= 0 && c.x + w <= vw && c.y + h <= vh) { chosen = p; pos = c; break; }
    }
    if (!pos) {                                                        // nothing fits: keep the preferred placement
      this.setArrow(this.preferred);
      const { width: w, height: h } = this.tip.getBoundingClientRect();
      pos = this.coords(this.preferred, t, w, h); chosen = this.preferred;
    }
    this.setArrow(chosen);
    this.tip.style.left = `${pos.x}px`;
    this.tip.style.top = `${pos.y}px`;
    this.tip.dataset.placement = chosen;
  }
}

/** Initialise every [data-annachy-tooltip] trigger inside `root` (idempotent). */
export function initTooltips(root = document) {
  const out = [];
  for (const trigger of root.querySelectorAll('[data-annachy-tooltip]')) {
    const tip = document.getElementById(trigger.dataset.annachyTooltip);
    if (!tip) continue;
    if (!controllers.has(trigger)) controllers.set(trigger, new Tooltip(trigger, tip));
    out.push(controllers.get(trigger));
  }
  return out;
}

if (typeof document !== 'undefined') {
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', () => initTooltips());
  else initTooltips();
}
