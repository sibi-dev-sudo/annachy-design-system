// Showcase catalogue: text search + category filter (vanilla ES module, no dependencies).
const q = document.getElementById('sc-q');
const count = document.getElementById('sc-q-count');
const empty = document.getElementById('sc-empty');
const buttons = [...document.querySelectorAll('.sc-filters [data-filter]')];
const cards = [...document.querySelectorAll('.sc-card')];
let category = 'all';

function apply() {
  const terms = q.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
  let shown = 0;
  for (const card of cards) {
    const text = `${card.textContent} ${card.dataset.keywords || ''}`.toLowerCase();
    const visible = (category === 'all' || card.dataset.category === category) && terms.every((t) => text.includes(t));
    card.hidden = !visible;
    if (visible) shown++;
  }
  for (const section of document.querySelectorAll('.sc-catalogue')) {
    section.hidden = ![...section.querySelectorAll('.sc-card')].some((c) => !c.hidden);
  }
  empty.hidden = shown !== 0;
  count.textContent = `${shown} of ${cards.length} entries`;
}

q.addEventListener('input', apply);
for (const b of buttons) {
  b.addEventListener('click', () => {
    category = b.dataset.filter;
    for (const x of buttons) x.setAttribute('aria-pressed', String(x === b));
    apply();
  });
}
apply();
