/*
 * Annachy Design System — icon helper (R7). Native ES module, no dependencies.
 * Icons: src/icons/svg/<style>/<slug>.svg, exported from Figma page 1801:5142 "② Icons" (Iconly-derived; internal use only).
 *
 *   <span class="annachy-button__icon" aria-hidden="true" data-annachy-icon="home-home-54"></span>
 *   <span … data-annachy-icon="arrow-chevron-down" data-annachy-icon-style="filled"></span>
 *   import { fillIconSlots } from './icons/icons.js'; fillIconSlots(document);
 *
 * The SVG is inlined so it inherits the slot's colour (currentColor) and fills the slot's Figma size (the slot sets
 * the size; the SVG has only a viewBox). Slugs and styles: src/icons/catalogue.json. Idempotent: filled slots are skipped.
 */
const BASE = new URL('./', import.meta.url);
const cache = new Map();

/** URL of an icon file. style: 'outline' | 'filled'. */
export const iconUrl = (slug, style = 'outline') => new URL(`svg/${style}/${slug}.svg`, BASE).href;

/** Fetch an icon's SVG markup (cached). Rejects for unknown slugs/styles. */
export function loadIcon(slug, style = 'outline') {
  if (!/^[a-z0-9]+(-[a-z0-9]+)*(--[a-z0-9-]+)?$/.test(slug) || !['outline', 'filled'].includes(style)) {
    return Promise.reject(new Error(`annachy-icon: invalid icon ${style}/${slug}`));
  }
  const key = `${style}/${slug}`;
  if (!cache.has(key)) {
    const get = () => fetch(iconUrl(slug, style)).then((r) => {
      if (!r.ok) throw new Error(`annachy-icon: ${key} (${r.status})`);
      return r.text();
    });
    const p = get().catch(get)                       // one retry for a transient network failure / cancellation
      .then((text) => {
        if (!/^\s*<svg[\s>]/.test(text)) throw new Error(`annachy-icon: ${key} is not an SVG`);
        return text;
      });
    p.catch(() => cache.delete(key));                // never cache a failure: a later call tries again
    cache.set(key, p);
  }
  return cache.get(key);
}

/** Fill every [data-annachy-icon] element inside root. Each slot is filled independently; a slot that cannot be
 *  loaded gets data-annachy-icon-error (and is retried by the next call). Resolves to the number of slots filled. */
export async function fillIconSlots(root = document) {
  const slots = [...root.querySelectorAll('[data-annachy-icon]')].filter((el) => !el.querySelector('svg'));
  const results = await Promise.allSettled(slots.map(async (el) => {
    const markup = await loadIcon(el.dataset.annachyIcon, el.dataset.annachyIconStyle || 'outline');
    el.innerHTML = markup;
    const svg = el.querySelector('svg');
    svg.setAttribute('focusable', 'false');
    svg.setAttribute('aria-hidden', 'true');
    el.dataset.annachyIconLoaded = '';
    delete el.dataset.annachyIconError;
  }));
  results.forEach((r, i) => { if (r.status === 'rejected') slots[i].dataset.annachyIconError = String(r.reason?.message || r.reason); });
  return results.filter((r) => r.status === 'fulfilled').length;
}
