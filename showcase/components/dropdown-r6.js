// Showcase: Dropdown Theme=Dark and Footer variants (R6). Renders the 20 Dark Item variants and the 40 Menu variants
// not shown above, from the Figma variant list (node IDs and META sizes: docs/figma-audit/r6-0-evidence.md).
import { initDropdowns } from '../../src/annachy.js';

const ROWS = { single: ['Selected', 'Default', 'Default', 'Disabled'], multiple: ['Selected', 'Selected', 'Default', 'Disabled'] };
const LABELS = ['Product design', 'Engineering', 'Customer success', 'Finance (unavailable)'];
const MENUS = [
  ['single', 'desktop', 'dark', 'off', 'none', '1451:25265'], ['single', 'desktop', 'dark', 'on', 'none', '1451:25310'],
  ['single', 'mobile', 'dark', 'off', 'none', '1451:25445'], ['single', 'mobile', 'dark', 'on', 'none', '1451:25490'],
  ['multiple', 'desktop', 'dark', 'off', 'none', '1454:1490'], ['multiple', 'desktop', 'dark', 'on', 'none', '1454:1589'],
  ['multiple', 'mobile', 'dark', 'off', 'none', '1454:1962'], ['multiple', 'mobile', 'dark', 'on', 'none', '1454:2061'],
  ['single', 'desktop', 'light', 'off', 'label', '1451:25190'], ['single', 'desktop', 'light', 'off', 'icon', '1451:25205'],
  ['single', 'desktop', 'light', 'on', 'label', '1451:25235'], ['single', 'desktop', 'light', 'on', 'icon', '1451:25250'],
  ['single', 'desktop', 'dark', 'off', 'label', '1451:25280'], ['single', 'desktop', 'dark', 'off', 'icon', '1451:25295'],
  ['single', 'desktop', 'dark', 'on', 'label', '1451:25325'], ['single', 'desktop', 'dark', 'on', 'icon', '1451:25340'],
  ['single', 'mobile', 'light', 'off', 'label', '1451:25370'], ['single', 'mobile', 'light', 'off', 'icon', '1451:25385'],
  ['single', 'mobile', 'light', 'on', 'label', '1451:25415'], ['single', 'mobile', 'light', 'on', 'icon', '1451:25430'],
  ['single', 'mobile', 'dark', 'off', 'label', '1451:25460'], ['single', 'mobile', 'dark', 'off', 'icon', '1451:25475'],
  ['single', 'mobile', 'dark', 'on', 'label', '1451:25505'], ['single', 'mobile', 'dark', 'on', 'icon', '1451:25520'],
  ['multiple', 'desktop', 'light', 'off', 'label', '1454:1283'], ['multiple', 'desktop', 'light', 'off', 'icon', '1454:1317'],
  ['multiple', 'desktop', 'light', 'on', 'label', '1454:1394'], ['multiple', 'desktop', 'light', 'on', 'icon', '1454:1441'],
  ['multiple', 'desktop', 'dark', 'off', 'label', '1454:1519'], ['multiple', 'desktop', 'dark', 'off', 'icon', '1454:1553'],
  ['multiple', 'desktop', 'dark', 'on', 'label', '1454:1630'], ['multiple', 'desktop', 'dark', 'on', 'icon', '1454:1677'],
  ['multiple', 'mobile', 'light', 'off', 'label', '1454:1755'], ['multiple', 'mobile', 'light', 'off', 'icon', '1454:1789'],
  ['multiple', 'mobile', 'light', 'on', 'label', '1454:1866'], ['multiple', 'mobile', 'light', 'on', 'icon', '1454:1913'],
  ['multiple', 'mobile', 'dark', 'off', 'label', '1454:1991'], ['multiple', 'mobile', 'dark', 'off', 'icon', '1454:2025'],
  ['multiple', 'mobile', 'dark', 'on', 'label', '1454:2102'], ['multiple', 'mobile', 'dark', 'on', 'icon', '1454:2149'],
];
const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
const item = (plat, state, label, extra = '') =>
  `<li class="annachy-dropdown-item annachy-dropdown-item--${plat}${state === 'Hover' ? ' is-hover' : ''}${state === 'Focus' ? ' is-focus' : ''}" role="option"${extra}
     aria-selected="${state === 'Selected'}"${state === 'Disabled' ? ' aria-disabled="true"' : ''}><span class="annachy-dropdown-item__indicator" aria-hidden="true"></span><span class="annachy-dropdown-item__label">${label}</span></li>`;
const footer = (plat, kind, id = '') => `<div class="annachy-dropdown-menu__footer"><div class="annachy-dropdown-menu__divider"></div>
  <button type="button"${id ? ` id="${id}"` : ''} class="annachy-button annachy-button--primary annachy-button--size-${plat === 'desktop' ? 40 : 48} annachy-dropdown-menu__footer-button">${kind === 'icon' ? '<span class="annachy-button__icon" aria-hidden="true"></span>' : ''}<span class="annachy-button__label">Apply selection</span></button></div>`;
const search = (id) => `<div class="annachy-dropdown-menu__search"><div class="annachy-dropdown-menu__search-field"><span class="annachy-dropdown-menu__search-icon" aria-hidden="true"></span>
  <input class="annachy-dropdown-menu__search-input" type="search" role="combobox" aria-autocomplete="list" aria-expanded="false" aria-controls="${id}" aria-label="Search" placeholder="Search teams" autocomplete="off"></div><div class="annachy-dropdown-menu__divider"></div></div>`;

// 20 Dark Item variants
const tbody = document.getElementById('sc-dd-dark-items');
for (const sel of ['single', 'multiple']) for (const plat of ['desktop', 'mobile']) for (const state of ['Default', 'Hover', 'Focus', 'Selected', 'Disabled']) {
  tbody.insertAdjacentHTML('beforeend', `<tr><td>${sel} · ${plat} · ${state}</td><td><ul class="annachy-dropdown-menu__options sc-dd-item-cell" role="listbox" aria-label="${sel} ${plat} ${state}" data-annachy-theme="dark"${sel === 'multiple' ? ' aria-multiselectable="true"' : ''} style="inline-size:${plat === 'desktop' ? 320 : 352}px">${item(plat, state, 'Product design')}</ul></td></tr>`);
}
// 40 static Menu variants
const grid = document.getElementById('sc-dd-r6-menus');
MENUS.forEach(([sel, plat, theme, srch, foot, node], n) => {
  const lid = `sc-r6-l${n}`;
  grid.insertAdjacentHTML('beforeend', `<figure class="sc-dd-figure sc-dd-r6-figure" data-variant="${sel}/${plat}/${theme}/${srch}/${foot}">
    <figcaption>${sel} · ${plat} · ${theme} · search ${srch} · footer ${foot === 'icon' ? 'icon + label' : foot} <code>${node}</code></figcaption>
    <div class="annachy-dropdown-menu annachy-dropdown-menu--${plat}"${theme === 'dark' ? ' data-annachy-theme="dark"' : ''}>
      ${srch === 'on' ? search(lid) : ''}<ul class="annachy-dropdown-menu__options" role="listbox" id="${lid}" aria-label="Team"${sel === 'multiple' ? ' aria-multiselectable="true"' : ''}>
      ${ROWS[sel].map((st, i) => item(plat, st, LABELS[i])).join('')}</ul>${foot !== 'none' ? footer(plat, foot) : ''}</div></figure>`);
});
// Interactive demos (staged commit with the footer)
const demos = document.getElementById('sc-dd-r6-demos');
const demo = (key, title, sel, plat, theme, withSearch, foot) => {
  const ids = [1, 2, 3, 4].map((i) => `${key}-o${i}`);
  demos.insertAdjacentHTML('beforeend', `<div class="sc-dd-demo"><span class="sc-dd-label" id="${key}-t">${title}</span>
    <div class="annachy-dropdown" data-annachy-dropdown><button type="button" class="annachy-button annachy-button--secondary-grey annachy-button--size-40"
      ${withSearch ? '' : 'role="combobox"'} aria-haspopup="dialog" aria-controls="${key}" aria-labelledby="${key}-t ${key}-b" id="${key}-b"><span class="annachy-button__label">Open</span></button>
    <div class="annachy-dropdown-menu annachy-dropdown-menu--${plat}" id="${key}" hidden role="dialog" aria-modal="false" aria-labelledby="${key}-t"${theme === 'dark' ? ' data-annachy-theme="dark"' : ''} data-status-selected="{count} selected">
      ${withSearch ? search(`${key}-l`) : ''}<ul class="annachy-dropdown-menu__options" role="listbox" id="${key}-l" aria-labelledby="${key}-t"${sel === 'multiple' ? ' aria-multiselectable="true"' : ''}>
      ${ROWS[sel].map((st, i) => item(plat, st === 'Disabled' ? 'Disabled' : i === 0 ? 'Selected' : 'Default', LABELS[i], ` id="${ids[i]}" data-value="${LABELS[i]}"`)).join('')}</ul>
      ${footer(plat, foot)}<div class="annachy-dropdown-menu__status" role="status" aria-live="polite"></div></div></div>
    <output class="sc-dd-value" for="${key}-b">Committed: <span>${LABELS[0]}</span></output></div>`);
};
demo('sc-r6a', 'Single · Desktop · Dark · Footer', 'single', 'desktop', 'dark', false, 'label');
demo('sc-r6b', 'Multiple · Desktop · Dark · Search + Footer (icon)', 'multiple', 'desktop', 'dark', true, 'icon');
demo('sc-r6c', 'Multiple · Mobile · Light · Footer', 'multiple', 'mobile', 'light', false, 'label');
for (const d of demos.querySelectorAll('[data-annachy-dropdown]')) {
  d.addEventListener('annachy-change', (e) => { d.parentElement.querySelector('.sc-dd-value span').textContent = e.detail.values.join(', ') || '(none)'; });
}
initDropdowns(demos);
document.getElementById('sc-dd-r6-code').textContent = `<div class="annachy-dropdown" data-annachy-dropdown>
  <button type="button" class="annachy-button annachy-button--secondary-grey annachy-button--size-40"
          role="combobox" aria-haspopup="dialog" aria-controls="teams">…</button>
  <div class="annachy-dropdown-menu annachy-dropdown-menu--desktop" id="teams" hidden
       role="dialog" aria-modal="false" aria-label="Teams" data-annachy-theme="dark">
    <ul class="annachy-dropdown-menu__options" role="listbox" aria-label="Teams" aria-multiselectable="true">
      <li class="annachy-dropdown-item annachy-dropdown-item--desktop" role="option" id="t1" aria-selected="false" data-value="design">
        <span class="annachy-dropdown-item__indicator" aria-hidden="true"></span><span class="annachy-dropdown-item__label">Product design</span></li>
    </ul>
    <div class="annachy-dropdown-menu__footer"><div class="annachy-dropdown-menu__divider"></div>
      <button type="button" class="annachy-button annachy-button--primary annachy-button--size-40 annachy-dropdown-menu__footer-button">
        <span class="annachy-button__label">Apply selection</span></button></div>
    <div class="annachy-dropdown-menu__status" role="status" aria-live="polite"></div>
  </div>
</div>`;
void esc;
