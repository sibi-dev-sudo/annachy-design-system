// Showcase: put the Figma-mapped icons (src/icons/figma-icon-map.json) into the component slots, then fill them with the
// library helper. Unmapped slots (Dropdown indicators, Input Filled, Checkbox glyph, Tooltip arrow) stay empty by design.
import { fillIconSlots } from '../src/icons/icons.js';

const RULES = [   // selector -> [slug, style]   (figma-icon-map.json: setNodeId, iconSize, style)
  ['.annachy-button__icon', 'home-home-54', 'outline'],                                                    // 1802:68148 S Outline
  ['.annachy-button-gradient__icon', 'home-home-54', 'outline'],                                           // 1802:68148 S Outline
  ['.annachy-input--outline .annachy-input__field > .annachy-input__icon', 'user-user-curved', 'outline'], // 1802:86130 M Outline
  ['.annachy-input--outline .annachy-input__icons > .annachy-input__icon:nth-child(1)', 'arrow-chevron-up', 'filled'],    // 1802:211244 M Filled
  ['.annachy-input--outline .annachy-input__icons > .annachy-input__icon:nth-child(2)', 'arrow-chevron-down', 'filled'],  // 1802:211124 M Filled
  ['.annachy-input--outline .annachy-input__subtext-icon', 'alerts-error-circle', 'outline'],              // 1802:155982 XS Outline
  ['.annachy-dropdown-menu__search-icon', 'user-user-curved', 'outline'],                                  // 1802:86130 M Outline
];

function mark(root) {
  for (const [sel, slug, style] of RULES) {
    for (const el of root.querySelectorAll(sel)) {
      if (el.hasAttribute('data-annachy-icon') || el.children.length) continue;
      el.dataset.annachyIcon = slug;
      el.dataset.annachyIconStyle = style;
    }
  }
  return fillIconSlots(root);
}

let pending = null;
const run = () => { pending = pending || Promise.resolve().then(() => mark(document)).finally(() => { pending = null; document.documentElement.dataset.iconsFilled = String(Date.now()); }); return pending; };
new MutationObserver(run).observe(document.body, { childList: true, subtree: true });
run();
