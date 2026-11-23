/*
 * Annachy Design System — main JS entry (native ES Module).
 * R3: Checkbox (indeterminate state). R4: Dropdown and Tooltip behaviour (approved r4-behaviour-spec.md).
 * AUD-1 (2026-11-20): Dropdown lifecycle — destroyDropdowns(root), getDropdown(el), controller.destroy().
 */
export { initCheckboxes } from './components/checkbox/checkbox.js';
export { initDropdowns, destroyDropdowns, getDropdown } from './components/dropdown/dropdown.js';
export { initTooltips } from './components/tooltip/tooltip.js';
