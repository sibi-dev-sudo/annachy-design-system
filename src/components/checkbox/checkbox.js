/*
 * Annachy Design System — Checkbox (R3-4)
 * The only JavaScript in R3 (spec §2.5): HTML cannot express an indeterminate checkbox in markup,
 * so Figma State=Multi-select is declared with data-indeterminate="true" and applied here.
 * Native behaviour is otherwise untouched; a user click clears the indeterminate state as usual.
 */
const SELECTOR = '.annachy-checkbox__input[data-indeterminate="true"]';

/** Apply data-indeterminate to every matching checkbox inside `root` (default: document). */
export function initCheckboxes(root = document) {
  for (const input of root.querySelectorAll(SELECTOR)) {
    input.indeterminate = true;
  }
}

if (typeof document !== 'undefined') {
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', () => initCheckboxes());
  else initCheckboxes();
}
