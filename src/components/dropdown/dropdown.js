/*
 * Annachy Design System — Dropdown behaviour (R4-1)
 * Approved behaviour: docs/implementation/r4-behaviour-spec.md (R4-Q1 patterns, R4-Q2 disabled options,
 * R4-Q4 typeahead 500 ms, R4-Q6 polite announcements). No dependencies; native ES module.
 *
 *   Plain Single / Multiple (D-S, D-M): select-only combobox (trigger role="combobox") + listbox popup.
 *   Searchable (D-SR): trigger button aria-haspopup="dialog" opens a non-modal popup whose search input is the
 *   combobox (aria-autocomplete="list") controlling the listbox.
 *   Footer (R6, R4-Q3 decided 2026-11-20 — staged commit): with an .annachy-dropdown-menu__footer-button
 *   ("Apply selection") option changes are STAGED: shown immediately (aria-selected) but committed — and
 *   `annachy-change` fired — only by Apply, which also closes and returns focus to the trigger. Closing any other way
 *   (Escape, outside pointer, Tab out, destroy) restores the last committed selection. Keyboard: Tab from the trigger /
 *   search moves to the footer button; Shift+Tab returns; Escape on it cancels and closes.
 *
 * Markup contract (see dropdown.html): a [data-annachy-dropdown] wrapper containing the trigger
 * ([aria-controls] → menu id) and the .annachy-dropdown-menu popup with a [role="listbox"] of [role="option"] items.
 * Emits a bubbling `annachy-change` CustomEvent on the wrapper: detail = { values: string[] }.
 *
 * Lifecycle (AUD-1, 2026-11-20): every listener is registered with an AbortSignal. The document-level outside-click
 * listener exists only while a dropdown is open (added on open, removed on close). `controller.destroy()` /
 * `destroyDropdowns(root)` close the popup without moving focus, remove every listener and timer, clear the active
 * option, and release the element so a later `initDropdowns()` creates a fresh controller.
 */
const TYPEAHEAD_MS = 500;      // R4-Q4
const ANNOUNCE_DEBOUNCE_MS = 500;
const controllers = new WeakMap();

const fmt = (tpl, count) => tpl.replace('{count}', String(count));
const labelOf = (opt) => (opt.querySelector('.annachy-dropdown-item__label') || opt).textContent.trim();
const isDisabled = (opt) => opt.getAttribute('aria-disabled') === 'true';

class Dropdown {
  constructor(root) {
    this.root = root;
    this.trigger = root.querySelector('[aria-controls][aria-haspopup]');
    this.menu = this.trigger && document.getElementById(this.trigger.getAttribute('aria-controls'));
    if (!this.trigger || !this.menu) throw new Error('annachy-dropdown: trigger with aria-controls and a menu are required');
    this.listbox = this.menu.querySelector('[role="listbox"]');
    this.search = this.menu.querySelector('.annachy-dropdown-menu__search-input');
    this.status = this.menu.querySelector('.annachy-dropdown-menu__status');
    this.multi = this.listbox.getAttribute('aria-multiselectable') === 'true';
    this.footer = this.menu.querySelector('.annachy-dropdown-menu__footer-button');   // staged commit when present
    this.committed = null;                               // ids selected when the popup opened (footer mode)
    this.host = this.search || this.trigger;           // element holding DOM focus + aria-activedescendant
    this.active = null;
    this.typed = '';
    this.typedAt = 0;
    this.announceTimer = 0;
    this.lifetime = new AbortController();               // all element listeners; aborted by destroy()
    this.openScope = null;                               // document listener while open; aborted by close()
    this.destroyed = false;
    this.trigger.setAttribute('aria-expanded', 'false');
    this.menu.hidden = true;
    this.bind();
  }

  get isOpen() { return !this.menu.hidden; }
  get triggerDisabled() { return this.trigger.disabled || this.trigger.getAttribute('aria-disabled') === 'true'; }
  options() { return [...this.listbox.querySelectorAll('[role="option"]')].filter((o) => !o.hidden); }
  selected() { return [...this.listbox.querySelectorAll('[role="option"][aria-selected="true"]')]; }

  bind() {
    const opts = { signal: this.lifetime.signal };
    this.trigger.addEventListener('click', () => (this.isOpen ? this.close(true) : this.open('selected')), opts);
    this.trigger.addEventListener('keydown', (e) => this.onTriggerKey(e), opts);
    if (this.search) {
      this.search.addEventListener('keydown', (e) => this.onSearchKey(e), opts);
      this.search.addEventListener('input', () => this.filter(), opts);
    }
    // pointer: keep DOM focus on the host; click selects
    this.listbox.addEventListener('mousedown', (e) => e.preventDefault(), opts);
    this.listbox.addEventListener('click', (e) => {
      const opt = e.target.closest('[role="option"]');
      if (opt && this.listbox.contains(opt)) { this.setActive(opt); this.select(opt); }
    }, opts);
    if (this.footer) {
      this.footer.addEventListener('click', () => this.apply(), opts);
      this.footer.addEventListener('keydown', (e) => this.onFooterKey(e), opts);
    }
  }

  // ---------------------------------------------------------------- footer: staged commit (R4-Q3)
  snapshot() { return this.selected().map((o) => o.id); }
  restore(ids) {
    for (const o of this.listbox.querySelectorAll('[role="option"]')) o.setAttribute('aria-selected', String(ids.includes(o.id)));
  }
  apply() {
    if (!this.isOpen) return;
    this.committed = this.snapshot();
    this.emit();
    this.close(true);
  }
  onFooterKey(e) {
    if (e.key === 'Escape') { e.preventDefault(); this.close(true); }
    else if (e.key === 'Tab' && e.shiftKey) { e.preventDefault(); this.host.focus(); }
    else if (e.key === 'Tab') this.close(false);         // focus moves on naturally; uncommitted changes discarded
  }

  /** Remove every listener and timer and release the element. Safe to call more than once. */
  destroy() {
    if (this.destroyed) return;
    this.close(false);                                   // never moves focus during teardown
    this.lifetime.abort();
    clearTimeout(this.announceTimer);
    this.typed = '';
    this.destroyed = true;
    if (controllers.get(this.root) === this) controllers.delete(this.root);
  }

  // ---------------------------------------------------------------- open / close (O1–O11)
  open(hint = 'selected') {
    if (this.destroyed || this.isOpen || this.triggerDisabled) return;
    this.menu.hidden = false;
    this.trigger.setAttribute('aria-expanded', 'true');
    if (this.footer) this.committed = this.snapshot();
    this.openScope = new AbortController();              // O4 outside pointer closes; exists only while open
    document.addEventListener('pointerdown', (e) => {
      if (this.isOpen && !this.root.contains(e.target) && !this.menu.contains(e.target)) this.close(false);
    }, { capture: true, signal: this.openScope.signal });
    if (this.search) this.search.setAttribute('aria-expanded', 'true');
    this.place();
    if (this.search) {                                   // O2: focus search, no active option
      this.search.focus();
      this.setActive(null);
      return;
    }
    const opts = this.options(), sel = this.selected()[0];
    if (hint === 'last') this.setActive(sel || opts[opts.length - 1] || null);
    else if (hint === 'first') this.setActive(sel || opts[0] || null);
    else this.setActive(sel || opts.find((o) => !isDisabled(o)) || null);
  }

  close(restoreFocus) {
    if (!this.isOpen) return;
    this.openScope?.abort();
    this.openScope = null;
    if (this.footer && this.committed) this.restore(this.committed);   // discard staged changes (Apply already committed)
    this.menu.hidden = true;
    this.trigger.setAttribute('aria-expanded', 'false');
    if (this.search) {                                   // O8: reset search on close
      this.search.setAttribute('aria-expanded', 'false');
      this.search.value = '';
      this.filter(true);
    }
    this.setActive(null);
    if (restoreFocus) this.trigger.focus();              // O7
  }

  place() {                                              // O12: below, flip above when there is no room
    this.menu.removeAttribute('data-placement');
    const r = this.menu.getBoundingClientRect(), t = this.trigger.getBoundingClientRect();
    if (r.bottom > window.innerHeight && t.top > r.height) this.menu.setAttribute('data-placement', 'top');
  }

  // ---------------------------------------------------------------- active option (aria-activedescendant)
  setActive(opt) {
    if (this.active) this.active.classList.remove('is-active');
    this.active = opt;
    if (opt) {
      opt.classList.add('is-active');
      this.host.setAttribute('aria-activedescendant', opt.id);
      opt.scrollIntoView?.({ block: 'nearest' });
    } else {
      this.host.removeAttribute('aria-activedescendant');
    }
  }

  move(delta) {                                          // no wrap; disabled options are navigable (R4-Q2)
    const opts = this.options();
    if (!opts.length) return;
    const i = this.active ? opts.indexOf(this.active) : -1;
    const next = i < 0 ? (delta > 0 ? 0 : opts.length - 1) : Math.min(opts.length - 1, Math.max(0, i + delta));
    this.setActive(opts[next]);
  }

  edge(first) { const opts = this.options(); this.setActive(first ? opts[0] : opts[opts.length - 1]); }

  // ---------------------------------------------------------------- selection (S1–S12)
  select(opt) {
    if (!opt || isDisabled(opt)) return;                 // never selectable when disabled (R4-Q2)
    if (this.multi) {
      opt.setAttribute('aria-selected', opt.getAttribute('aria-selected') === 'true' ? 'false' : 'true');
      this.announce(fmt(this.menu.dataset.statusSelected || '{count} selected', this.selected().length));   // A8b
      if (!this.footer) this.emit();                     // footer: committed by Apply
    } else if (this.footer) {                            // staged single selection: stays open until Apply
      for (const o of this.listbox.querySelectorAll('[role="option"]')) o.setAttribute('aria-selected', String(o === opt));
    } else {
      for (const o of this.listbox.querySelectorAll('[role="option"]')) o.setAttribute('aria-selected', String(o === opt));
      this.emit();
      this.close(true);                                  // O9
    }
  }

  emit() {
    const values = this.selected().map((o) => o.dataset.value ?? labelOf(o));
    this.root.dispatchEvent(new CustomEvent('annachy-change', { bubbles: true, detail: { values } }));
  }

  announce(text, debounce = 0) {
    if (!this.status) return;
    clearTimeout(this.announceTimer);
    // Write directly (no animation-frame dependency: rAF does not run on hidden pages). Identical consecutive
    // messages alternate a trailing no-break space so the live region changes and is re-announced.
    const write = () => {
      const NBSP = '\u00a0';
      const current = this.status.textContent;
      const same = (current.endsWith(NBSP) ? current.slice(0, -1) : current) === text;
      this.status.textContent = same && !current.endsWith(NBSP) ? text + NBSP : text;
    };
    if (debounce) this.announceTimer = setTimeout(write, debounce); else write();
  }

  // ---------------------------------------------------------------- search (D-SR)
  filter(silent = false) {
    const q = this.search.value.trim().toLowerCase();
    let count = 0;
    for (const o of this.listbox.querySelectorAll('[role="option"]')) {
      const match = !q || labelOf(o).toLowerCase().includes(q);
      o.hidden = !match;
      if (match) count++;
    }
    this.setActive(null);
    if (!silent && q) this.announce(fmt(this.menu.dataset.statusResults || '{count} results', count), ANNOUNCE_DEBOUNCE_MS);   // A8a
  }

  // ---------------------------------------------------------------- typeahead (D-S / D-M)
  typeahead(ch) {
    const now = Date.now();
    this.typed = now - this.typedAt > TYPEAHEAD_MS ? ch : this.typed + ch;
    this.typedAt = now;
    const opts = this.options();
    if (!opts.length) return;
    const same = this.typed.split('').every((c) => c === this.typed[0]);
    const needle = (same ? this.typed[0] : this.typed).toLowerCase();
    const start = this.active ? opts.indexOf(this.active) + (same || this.typed.length === 1 ? 1 : 0) : 0;
    for (let k = 0; k < opts.length; k++) {
      const o = opts[(start + k) % opts.length];
      if (labelOf(o).toLowerCase().startsWith(needle)) { this.setActive(o); return; }
    }
  }

  // ---------------------------------------------------------------- keyboard
  onTriggerKey(e) {
    if (this.triggerDisabled) return;
    const { key } = e;
    if (this.search) {                                   // D-SR trigger: opens the dialog popup
      if (['Enter', ' ', 'ArrowDown', 'ArrowUp'].includes(key)) { e.preventDefault(); this.open(); }
      if (key === 'Escape' && this.isOpen) { e.preventDefault(); this.close(true); }
      return;
    }
    if (!this.isOpen) {
      if (key === 'ArrowDown' || key === 'Enter' || key === ' ') { e.preventDefault(); this.open('first'); }
      else if (key === 'ArrowUp') { e.preventDefault(); this.open('last'); }
      else if (key === 'Home') { e.preventDefault(); this.open(); this.edge(true); }
      else if (key === 'End') { e.preventDefault(); this.open(); this.edge(false); }
      else if (key.length === 1 && !e.ctrlKey && !e.metaKey && !e.altKey) { this.open(); this.typeahead(key); }
      return;
    }
    switch (key) {
      case 'ArrowDown': e.preventDefault(); if (e.altKey) break; this.move(1); break;
      case 'ArrowUp': e.preventDefault(); if (e.altKey) { this.select(this.active); break; } this.move(-1); break;
      case 'Home': e.preventDefault(); this.edge(true); break;
      case 'End': e.preventDefault(); this.edge(false); break;
      case 'PageDown': e.preventDefault(); this.move(10); break;
      case 'PageUp': e.preventDefault(); this.move(-10); break;
      case 'Enter': case ' ': e.preventDefault(); this.select(this.active); break;
      case 'Escape': e.preventDefault(); this.close(true); break;          // O5
      case 'Tab':
        if (this.footer && !e.shiftKey) { e.preventDefault(); this.footer.focus(); break; }
        this.close(false); break;                                           // O6: focus moves on naturally
      default:
        if (key.length === 1 && !e.ctrlKey && !e.metaKey && !e.altKey) { e.preventDefault(); this.typeahead(key); }
    }
  }

  onSearchKey(e) {
    switch (e.key) {
      case 'ArrowDown': e.preventDefault(); this.move(1); break;
      case 'ArrowUp': e.preventDefault(); this.move(-1); break;
      case 'Home': if (e.ctrlKey) { e.preventDefault(); this.edge(true); } break;     // Home/End move the caret
      case 'End': if (e.ctrlKey) { e.preventDefault(); this.edge(false); } break;
      case 'Enter': e.preventDefault(); if (this.active) this.select(this.active); break;
      case 'Escape':
        e.preventDefault();
        if (this.search.value) { this.search.value = ''; this.filter(true); }    // first Escape clears (O5)
        else this.close(true);
        break;
      case 'Tab':
        if (this.footer && !e.shiftKey) { e.preventDefault(); this.footer.focus(); break; }
        this.close(false); break;
      default: break;                                    // Space and text keys type into the field
    }
  }
}

/** Initialise every [data-annachy-dropdown] inside `root` (idempotent). Returns the controllers. */
export function initDropdowns(root = document) {
  const out = [];
  for (const el of root.querySelectorAll('[data-annachy-dropdown]')) {
    if (!controllers.has(el)) controllers.set(el, new Dropdown(el));
    out.push(controllers.get(el));
  }
  return out;
}

/** Destroy the controllers of every [data-annachy-dropdown] inside `root` (or `root` itself). Returns the count. */
export function destroyDropdowns(root = document) {
  const els = [...(root.matches?.('[data-annachy-dropdown]') ? [root] : []), ...root.querySelectorAll('[data-annachy-dropdown]')];
  let n = 0;
  for (const el of els) {
    const c = controllers.get(el);
    if (c) { c.destroy(); n++; }
  }
  return n;
}

/** The controller for a [data-annachy-dropdown] element, or undefined. */
export const getDropdown = (el) => controllers.get(el);

if (typeof document !== 'undefined') {
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', () => initDropdowns());
  else initDropdowns();
}
