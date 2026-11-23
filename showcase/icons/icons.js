// Icon catalogue: renders every Figma icon set × style × size from src/icons/catalogue.json (vanilla ES module).
// SVGs are fetched once each and inlined so colour follows currentColor. Pages of PAGE sets keep the DOM small.
const BASE = '../../src/icons/';
const PAGE = 48;
const SIZES = { XS: 16, S: 20, M: 24, L: 32, XL: 40 };
const $ = (id) => document.getElementById(id);
const svgCache = new Map();
let all = [];        // flattened sets: { name, slug, nodeId, category, catSlug, restricted, duplicateOf, styles }
let view = [];
let page = 0;

async function svg(file) {
  if (!svgCache.has(file)) {
    svgCache.set(file, fetch(BASE + file).then((r) => { if (!r.ok) throw new Error(`${r.status} ${file}`); return r.text(); }));
  }
  return svgCache.get(file);
}

function fileFor(style, size) {
  return (style.perSize && style.perSize[size]) || style.file;
}

function matches(set, q, cat, sty, brands) {
  if (set.restricted && !brands) return false;
  if (cat && set.catSlug !== cat) return false;
  if (sty && !set.styles[sty]) return false;
  if (!q) return true;
  const hay = `${set.name} ${set.category} ${set.nodeId} ${Object.values(set.styles).flatMap((s) => Object.values(s.variants || {})).join(' ')}`.toLowerCase();
  return q.split(/\s+/).every((t) => hay.includes(t));
}

function apply(resetPage = true) {
  const q = $('ic-q').value.trim().toLowerCase(), cat = $('ic-cat').value, sty = $('ic-style').value, brands = $('ic-brands').checked;
  $('ic-brands-note').hidden = !brands;
  view = all.filter((s) => matches(s, q, cat, sty, brands));
  if (resetPage) page = 0;
  render();
}

async function render() {
  const sty = $('ic-style').value, size = $('ic-size').value;
  const pages = Math.max(1, Math.ceil(view.length / PAGE));
  page = Math.min(page, pages - 1);
  const slice = view.slice(page * PAGE, page * PAGE + PAGE);
  const variants = view.reduce((n, s) => n + Object.entries(s.styles).filter(([k]) => !sty || k === sty).reduce((m, [, st]) => m + Object.keys(st.variants || {}).filter((z) => !size || z === size).length, 0), 0);
  $('ic-count').textContent = `${view.length} icon sets · ${variants} variants match`;
  $('ic-page').textContent = `Page ${page + 1} of ${pages}`;
  $('ic-prev').disabled = page === 0;
  $('ic-next').disabled = page >= pages - 1;
  const grid = $('ic-grid');
  grid.textContent = '';
  for (const set of slice) {
    const li = document.createElement('li');
    li.className = 'ic-card';
    li.dataset.node = set.nodeId;
    li.innerHTML = `<h2 class="ic-card__name">${set.name}</h2><p class="ic-card__meta">${set.category}${set.restricted ? ' · restricted' : ''} · <code>${set.nodeId}</code></p>`;
    for (const [styleName, style] of Object.entries(set.styles)) {
      if (sty && styleName !== sty) continue;
      const row = document.createElement('div');
      row.className = 'ic-row';
      row.innerHTML = `<span class="ic-row__style">${styleName}${style.implicit ? ' (implicit)' : ''}</span>`;
      for (const [z, px] of Object.entries(SIZES)) {
        if (size && z !== size) continue;
        if (!style.variants || !style.variants[z]) continue;
        const cell = document.createElement('span');
        cell.className = 'ic-icon';
        cell.style.inlineSize = cell.style.blockSize = `${px}px`;
        cell.title = `${set.name} · ${styleName} · ${z} ${px} · ${style.variants[z]}`;
        cell.dataset.size = z;
        cell.dataset.style = styleName;
        cell.dataset.file = fileFor(style, z);
        if (style.figmaDefect) { cell.classList.add('ic-icon--defect'); cell.title += ` · ${style.figmaDefect}`; }
        row.appendChild(cell);
      }
      li.appendChild(row);
    }
    grid.appendChild(li);
  }
  await Promise.all([...grid.querySelectorAll('.ic-icon')].map(async (cell) => {
    try { cell.innerHTML = await svg(cell.dataset.file); } catch (e) { cell.classList.add('ic-icon--missing'); cell.textContent = ''; cell.dataset.error = String(e.message); }
  }));
  grid.dataset.rendered = String(Date.now());
}

const data = await fetch(BASE + 'catalogue.json').then((r) => r.json());
for (const c of data.categories) {
  const opt = document.createElement('option');
  opt.value = c.slug;
  opt.textContent = `${c.name}${c.duplicateOf ? ' (duplicate frame)' : ''}${c.restricted ? ' — restricted' : ''} (${c.sets.length})`;
  $('ic-cat').appendChild(opt);
  for (const s of c.sets) all.push({ ...s, category: c.name, catSlug: c.slug, restricted: !!c.restricted, duplicateOf: c.duplicateOf });
}
const open = all.filter((s) => !s.restricted);
const vcount = (list) => list.reduce((n, s) => n + Object.values(s.styles).reduce((m, st) => m + Object.keys(st.variants || {}).length, 0), 0);
$('ic-summary').textContent = `${all.length} icon sets (${open.length} library + ${all.length - open.length} restricted Brands) · ${vcount(all)} Figma variants · ${new Set(all.map((s) => s.name)).size} unique names · ${data.categories.length} category frames`;
$('ic-q').addEventListener('input', () => apply());
for (const id of ['ic-cat', 'ic-style', 'ic-size', 'ic-brands']) $(id).addEventListener('change', () => apply(id !== 'ic-size'));
$('ic-prev').addEventListener('click', () => { page--; render(); });
$('ic-next').addEventListener('click', () => { page++; render(); });
window.__icons = { all, data };
apply();
