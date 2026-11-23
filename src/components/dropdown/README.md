# Dropdown (Menu + Item) — R4-1, R6

Figma: `Dropdown / Item` `1451:25092` and `Dropdown / Menu` `1451:25521`.
Evidence: `docs/figma-audit/components/dropdown.md`, `docs/figma-audit/r4-0-evidence.md` §1–§3, §6, and `docs/figma-audit/r6-0-evidence.md` (Dark, Footer).
Behaviour: `docs/implementation/r4-behaviour-spec.md` (approved R4-Q1, Q2, Q4, Q6).

## Scope

| Implemented | Variants |
|---|---|
| Item: Single / Multiple × Desktop / Mobile × **Light / Dark** × Default, Hover, Focus, Selected, Disabled | **40 of 40** |
| Menu: Single / Multiple × Desktop / Mobile × **Light / Dark** × Search Off / On × **Footer None / Label / Icon + label** | **48 of 48** |

Not implemented: the Select trigger, because no such component exists in this Figma file (B4-1).

### Theme=Dark (R6)

Put `data-annachy-theme="dark"` on the menu, the item, or any ancestor.
- **Mode values.** The Brand Dark-mode values (`src/tokens/themes/dark.css`) re-map the same tokens: menu `#181b21`, Hover `#1f242e`, stroke `#171e2a`, label `#fafcff`, placeholder and indicator `#98a0ae`.
- **Selected state.** Dark Selected binds different variables: `Blue/500` fill, with `Base/White` label and indicator.
- **Unchanged.** Geometry and typography are the same as Light.

### Footer (R6)

```html
<div class="annachy-dropdown-menu__footer">
  <div class="annachy-dropdown-menu__divider"></div>
  <button type="button" class="annachy-button annachy-button--primary annachy-button--size-40 annachy-dropdown-menu__footer-button">
    <span class="annachy-button__icon" aria-hidden="true"></span>   <!-- Footer=Icon + label only (20 × 20, Home/Home 54) -->
    <span class="annachy-button__label">Apply selection</span>
  </button>
</div>
```

**Layout.** Footer: padding-top 4, gap 12, 1px `Border/Secondary` divider. The button is the R3 Primary Button, size **40** on Desktop and **48** on Mobile. Only its label typography changes, as in Figma (D4): Label Small 14/20 on Desktop, Label Medium 16/21 on Mobile.

**Markup.** With a footer, use `aria-haspopup="dialog"` on the trigger and `role="dialog" aria-modal="false"` on the menu: the popup contains a button.

**Commit model (R4-Q3, decided 2026-11-20): staged.**
- Choices show immediately but are committed only by "Apply selection". Apply fires `annachy-change`, closes, and returns focus to the trigger.
- Escape, an outside click, tabbing past the button, or `destroy()` restore the last committed selection.
- Single selection does not close the popup when there is a footer.
- Keyboard: Tab from the trigger or search field moves to Apply. Shift+Tab returns. Escape on Apply cancels.

## API

| Figma property | Markup |
|---|---|
| Platform | `.annachy-dropdown-menu--desktop` (320) / `--mobile` (352) on the menu, and `.annachy-dropdown-item--desktop` / `--mobile` on every item. There are no breakpoints (D-07); the consumer chooses. |
| Selection=Single / Multiple | listbox without / with `aria-multiselectable="true"` |
| Search=On | include `.annachy-dropdown-menu__search`; the trigger uses `aria-haspopup="dialog"` and the menu `role="dialog" aria-modal="false"` |
| Item State | Default; **Hover** = `:hover` (test class `.is-hover`); **Focus** = the active option (`.is-active`, set by JS; test class `.is-focus`); **Selected** = `aria-selected="true"`; **Disabled** = `aria-disabled="true"` |
| Trigger | Consumer-supplied, for example an R3 Button: `role="combobox"` (plain) or `aria-haspopup="dialog"` (search), plus `aria-controls` → menu id |
| Change event | `annachy-change` (bubbles from `[data-annachy-dropdown]`), `detail.values` = the `data-value` of every selected option |
| Announcement text | `data-status-selected` / `data-status-results` on the menu (default `"{count} selected"` / `"{count} results"`; localisable) |

### JavaScript lifecycle (AUD-1, 2026-11-20)

```js
import { initDropdowns, destroyDropdowns, getDropdown } from '../../src/annachy.js';
initDropdowns(root);            // idempotent: repeated calls return the same controllers (no duplicate listeners)
getDropdown(wrapperEl);         // the controller, or undefined
destroyDropdowns(root);         // destroy every dropdown in root (or root itself); returns the number destroyed
getDropdown(wrapperEl).destroy();
```

| Rule | Behaviour |
|---|---|
| Listeners | Every element listener is registered with an `AbortSignal`; `destroy()` removes them all |
| Document listener | The outside-click `pointerdown` (capture) listener exists **only while a dropdown is open**, and is removed on every close path (selection, Escape, Tab, outside click, `destroy()`) |
| `destroy()` | Closes the popup **without moving focus**, clears the active option and `aria-activedescendant`, resets the search field, cancels a pending announcement, releases the controller. Calling it twice is a no-op. Selection markup (`aria-selected`) is left as-is |
| After destroy | The markup is inert; `initDropdowns()` creates a fresh controller |
| SPA removal | Call `destroyDropdowns(container)` before removing markup. A *closed* dropdown removed without `destroy()` holds no document listener and is garbage-collected (verified) |

`initDropdowns` is unchanged (same signature and return value), so existing code needs no changes.

## Values

| Item | Desktop | Mobile |
|---|---|---|
| Size | 320 × 40 (min-height) | 352 × 48 |
| Padding | 12 / 10 | 12 |
| Gap | 12 | 12 |
| Radius | `Radius/8` | `Radius/8` |
| Label | Label Small — Medium 14/20 | Body M — Regular 16/24 |

| State (Light) | Fill | Label | Indicator colour |
|---|---|---|---|
| Default | `Background/Secondary` | `Text/Primary` | Multiple: `Icon/Secondary` |
| Hover | `Background/Tertiary` | `Text/Primary` | Multiple: `Icon/Secondary` |
| Focus | `Background/Secondary` + inset 2px `Button/Primary/Border/Focus` + `Button/Focus` | `Text/Primary` | Multiple: `Icon/Secondary` |
| Selected | `Blue/50` | `Blue/500` | `Blue/500` |
| Disabled | `Background/Secondary` | `Text/Tertiary` | `Border/Primary` |

**Menu:**
- Padding 8, gap 8 (search to options), `Radius/12`, `Background/Secondary`.
- 1px `Border/Primary` stroke drawn **inset**: the Figma stroke is outside the layout (188 = 8 + 4 × 40 + 3 × 4 + 8).
- Options gap 4.

**Search region:**
- Input Field / Outline instance: 48 tall, padding-x 14, gap 6, `Radius/8`, 1px `Border/Primary`, 24px icon slot.
- Placeholder Body M Regular `Text/Secondary` (D6); padding-bottom 8; 1px `Border/Secondary` divider.

The Focus stroke is drawn inset because the Figma Focus variant keeps the same size and content position as Default (`r4-0-evidence.md` §6).

## Behaviour (approved)

| Interaction | Plain (Single / Multiple) | Searchable |
|---|---|---|
| Open | click, Enter, Space, ArrowDown (first or selected), ArrowUp (last or selected), Home / End, typing | click, Enter, Space, ArrowDown / Up. Focus moves to the search field, with no active option |
| Navigate | ArrowUp / Down (no wrap), Home / End, PageUp / Down (10). **Disabled options can become active** (R4-Q2) | ArrowUp / Down; Ctrl+Home / End. Home / End move the text caret |
| Select | Enter / Space / click. Single commits and closes, returning focus to the trigger; Multiple toggles and stays open. Disabled options are never selected | Enter / click on the active option |
| Typeahead | 500 ms buffer; a repeated letter cycles (R4-Q4) | Typing filters (case-insensitive substring) |
| Escape | Closes and restores focus | First press clears the text, second closes and restores focus |
| Tab | Closes; focus continues | Closes; focus continues (non-modal, no focus trap) |
| Outside pointer | Closes; focus goes where the user clicked (selection kept) | Same |
| Disabled trigger | Cannot open | — |
| Placement | Below the trigger; flips above when there is no room. No trigger-to-menu spacing is designed, so none is added | Same |
| Announcements (polite) | "N selected" on each Multiple toggle (R4-Q6) | "N results" 500 ms after typing (R4-Q6); identical consecutive messages are still re-announced |

## Known limitations and reproduced design defects

| Flag | Item |
|---|---|
| G8 / G9 | The Single check icon and the Multiple "checkbox" indicator are research-page icons, so the **slots are empty**. Size and state colour are implemented (`currentColor`). |
| G13 | No Select trigger design; the consumer supplies the trigger. |
| G1–G4 | No empty, loading, scroll/max-height or group-header states, so the "No results" announcement and long-list scrolling are not provided. |
| D2 / G6 | The Menu has no shadow (border only). Reproduced. |
| D6 | Search placeholder `Text/Secondary` with Body M Regular (differs from Input's own placeholder). Reproduced. |
| DD-1 | The search field's focus border uses the Input Field / Outline Focused state (raw `#3a6ff7`, IN2). It is **derived** from the instance's main component, because the Dropdown designs no focused search field. |
| Mobile | Visual variants only. The device is chosen by class (no breakpoints). Behaviour is identical. |

## Validation

- **`tests/fixtures/r4-dropdown-check.html`:** 20 Item + 8 Menu variants, **469 checks**. Covers size, padding, gap, radius, the indicator position (x 12) and label position (x 44), typography, colours, the focus treatment, empty slots, roles and states, menu sizes **equal to the Figma META** (188 / 261 / 220 / 293), search-field geometry, the divider, placeholder, dialog/combobox roles and toggling.
- **`tests/fixtures/r4-dropdown-interaction.html`**, driven with real keyboard, mouse and touch through the Chrome DevTools Protocol: **82 checks**. Covers every row of the behaviour table, `annachy-change`, touch tap, flip placement, the disabled trigger and the accessibility tree (combobox / listbox / option / dialog roles, names, expanded, selected, multiselectable, disabled, status region).
- **`tests/fixtures/r6-dropdown-check.html`** (R6): 20 Dark Item + 40 Menu variants (Dark and Footer), **757 checks**; every menu size equals the Figma META.
- **`tests/tools/r6_dropdown_footer_cdp.py`** (R6): staged commit with real keyboard, mouse and touch, the Dark theme and footer lifecycle, **38 checks**.
- **`tests/tools/r4_dropdown_lifecycle_cdp.py`** (AUD-1): **40 checks**. Counts real listeners (`DOMDebugger.getEventListeners`) across open/close paths, 25 cycles, 10× re-init and `destroy()` (also while open); verifies garbage collection of 100 destroyed and 50 closed-then-removed dropdowns (`WeakRef` + forced GC); three lifecycle mutants are all caught.
- Static validator: token references, raw-colour allow-list (`#3a6ff7`, DD-1), state pairing.
