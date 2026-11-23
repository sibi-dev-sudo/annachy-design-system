# R1 Token Mapping — Figma → CSS custom properties

| Item | Value |
|---|---|
| Status | **Specification only — no CSS/JSON created.** Generated from audit evidence on 2026-11-19. |
| Companion | `r1-implementation-spec.md` (architecture, rules, readiness) |
| Prefix | `--annachy-` |
| Evidence tags | **BIND** bound on a component (`get_variable_defs`/`get_design_context`) · **VAR** Figma variable/style returned on a Foundations node · **DOC** documented text/table only (no variable binding observed) · **APPLIED** raw value rendered by `get_design_context` |
| Values | Exact Figma resolved values (Light mode). Hex lower-case as returned. **No value is invented or rounded.** |

## 1. Colour — primitives (`src/tokens/primitives.css`)

| Figma variable | Value | CSS custom property | Evidence |
|---|---|---|---|
| `Brand/Base/Black` | `#0b0c0f` | `--annachy-color-base-black` | BIND (Input, `1066:38989`) |
| `Brand/Base/Blue` | `#004feb` | `--annachy-color-base-blue` | VAR `1557:31595` |
| `Brand/Base/Grey` | `#1f242e` | `--annachy-color-base-grey` | BIND (Input, `1066:38539`) |
| `Brand/Base/White` | `#fafcff` | `--annachy-color-base-white` | BIND (Tooltip, gradient Button) |
| `Brand/Gradient/Color 1` | `#3a79f7` | `--annachy-color-gradient-color-1` | BIND (gradient Button `1153:3371`) |
| `Brand/Gradient/Color 2` | `#1746a2` | `--annachy-color-gradient-color-2` | BIND (gradient Button `1153:3371`) |

### 1.1 Tonal scales

| Figma variable | Value | CSS custom property | Evidence |
|---|---|---|---|
| `Brand/Blue/50` | `#f3f7ff` | `--annachy-color-blue-50` | BIND — Dropdown Selected, Input/Filled |
| `Brand/Blue/100` | `#e6edfd` | `--annachy-color-blue-100` | VAR `1557:31595` |
| `Brand/Blue/200` | `#ccdcfb` | `--annachy-color-blue-200` | VAR `1557:31595` |
| `Brand/Blue/300` | `#99b9f7` | `--annachy-color-blue-300` | BIND — Checkbox, Radio, gradient Button |
| `Brand/Blue/400` | `#3372ef` | `--annachy-color-blue-400` | VAR `1557:31595` |
| `Brand/Blue/500` | `#004feb` | `--annachy-color-blue-500` | BIND — Dropdown, Input/Filled |
| `Brand/Blue/600` | `#003fbc` | `--annachy-color-blue-600` | BIND — Input/Filled Focused |
| `Brand/Blue/700` | `#002f8d` | `--annachy-color-blue-700` | VAR `1557:31595` |
| `Brand/Blue/800` | `#00205e` | `--annachy-color-blue-800` | VAR `1557:31595` |
| `Brand/Blue/900` | `#00102f` | `--annachy-color-blue-900` | VAR `1557:31595` |
| `Brand/Blue-White/50` | `#fafcff` | `--annachy-color-blue-white-50` | VAR `1557:31595` |
| `Brand/Blue-White/100` | `#f5f9ff` | `--annachy-color-blue-white-100` | VAR `1557:31595` |
| `Brand/Blue-White/200` | `#f0f5fe` | `--annachy-color-blue-white-200` | VAR `1557:31595` |
| `Brand/Blue-White/300` | `#ebf2ff` | `--annachy-color-blue-white-300` | BIND — Checkbox/Radio Focus |
| `Brand/Blue-White/400` | `#c6d6f6` | `--annachy-color-blue-white-400` | VAR `1557:31595` |
| `Brand/Blue-White/500` | `#b3c7ef` | `--annachy-color-blue-white-500` | VAR `1557:31595` |
| `Brand/Blue-White/600` | `#a1b9e8` | `--annachy-color-blue-white-600` | VAR `1557:31595` |
| `Brand/Blue-White/700` | `#88a4dd` | `--annachy-color-blue-white-700` | VAR `1557:31595` |
| `Brand/Blue-White/800` | `#7393d3` | `--annachy-color-blue-white-800` | VAR `1557:31595` |
| `Brand/Blue-White/900` | `#5b7fc8` | `--annachy-color-blue-white-900` | VAR `1557:31595` |
| `Brand/Blue-Black/50` | `#202d47` | `--annachy-color-blue-black-50` | BIND — Input/Filled |
| `Brand/Blue-Black/100` | `#1d2432` | `--annachy-color-blue-black-100` | VAR `1557:31595` |
| `Brand/Blue-Black/200` | `#171e2a` | `--annachy-color-blue-black-200` | VAR `1557:31595` |
| `Brand/Blue-Black/300` | `#1f242e` | `--annachy-color-blue-black-300` | VAR `1557:31595` |
| `Brand/Blue-Black/400` | `#181b21` | `--annachy-color-blue-black-400` | VAR `1557:31595` |
| `Brand/Blue-Black/500` | `#121417` | `--annachy-color-blue-black-500` | BIND — Input label |
| `Brand/Blue-Black/600` | `#030a14` | `--annachy-color-blue-black-600` | VAR `1557:31595` |
| `Brand/Blue-Black/700` | `#00050f` | `--annachy-color-blue-black-700` | VAR `1557:31595` |
| `Brand/Blue-Black/800` | `#060707` | `--annachy-color-blue-black-800` | VAR `1557:31595` |
| `Brand/Blue-Black/900` | `#000204` | `--annachy-color-blue-black-900` | VAR `1557:31595` |
| `Brand/Blue-Grey/50` | `#f6f7f9` | `--annachy-color-blue-grey-50` | BIND — Input/Filled, Toggle |
| `Brand/Blue-Grey/100` | `#edeff2` | `--annachy-color-blue-grey-100` | BIND — Input, Checkbox, Toggle |
| `Brand/Blue-Grey/200` | `#dcdfe5` | `--annachy-color-blue-grey-200` | BIND — Input, Checkbox, Toggle |
| `Brand/Blue-Grey/300` | `#bfc4cf` | `--annachy-color-blue-grey-300` | BIND — Input/Outline border |
| `Brand/Blue-Grey/400` | `#98a0ae` | `--annachy-color-blue-grey-400` | BIND — Input/Filled |
| `Brand/Blue-Grey/500` | `#707a8f` | `--annachy-color-blue-grey-500` | BIND — Input sub-text |
| `Brand/Blue-Grey/600` | `#555d6d` | `--annachy-color-blue-grey-600` | VAR `1557:31595` |
| `Brand/Blue-Grey/700` | `#3d4451` | `--annachy-color-blue-grey-700` | BIND — Input description |
| `Brand/Blue-Grey/800` | `#272b35` | `--annachy-color-blue-grey-800` | BIND — Input label |
| `Brand/Blue-Grey/900` | `#15181e` | `--annachy-color-blue-grey-900` | BIND — Input sub-text |
| `Brand/Success/100` | `#f4fbef` | `--annachy-color-success-100` | VAR `1557:31595` |
| `Brand/Success/200` | `#d6f3c9` | `--annachy-color-success-200` | VAR `1557:31595` |
| `Brand/Success/300` | `#93e281` | `--annachy-color-success-300` | VAR `1557:31595` |
| `Brand/Success/400` | `#5ecb55` | `--annachy-color-success-400` | VAR `1557:31595` |
| `Brand/Success/500` | `#14a047` | `--annachy-color-success-500` | VAR `1557:31595` |
| `Brand/Success/600` | `#276732` | `--annachy-color-success-600` | VAR `1557:31595` |
| `Brand/Success/700` | `#20572c` | `--annachy-color-success-700` | VAR `1557:31595` |
| `Brand/Success/800` | `#184626` | `--annachy-color-success-800` | VAR `1557:31595` |
| `Brand/Success/900` | `#11331c` | `--annachy-color-success-900` | VAR `1557:31595` |
| `Brand/Warning/100` | `#fff8f1` | `--annachy-color-warning-100` | VAR `1557:31595` |
| `Brand/Warning/200` | `#ffddb3` | `--annachy-color-warning-200` | VAR `1557:31595` |
| `Brand/Warning/300` | `#ffbd6b` | `--annachy-color-warning-300` | VAR `1557:31595` |
| `Brand/Warning/400` | `#f88f33` | `--annachy-color-warning-400` | VAR `1557:31595` |
| `Brand/Warning/500` | `#f26e2d` | `--annachy-color-warning-500` | VAR `1557:31595` |
| `Brand/Warning/600` | `#b9512e` | `--annachy-color-warning-600` | VAR `1557:31595` |
| `Brand/Warning/700` | `#9d4520` | `--annachy-color-warning-700` | VAR `1557:31595` |
| `Brand/Warning/800` | `#6c2e18` | `--annachy-color-warning-800` | VAR `1557:31595` |
| `Brand/Warning/900` | `#4c2213` | `--annachy-color-warning-900` | VAR `1557:31595` |
| `Brand/Error/100` | `#fff7f6` | `--annachy-color-error-100` | VAR `1557:31595` |
| `Brand/Error/200` | `#ffe6e2` | `--annachy-color-error-200` | VAR `1557:31595` |
| `Brand/Error/300` | `#ffc1b6` | `--annachy-color-error-300` | VAR `1557:31595` |
| `Brand/Error/400` | `#ff9c8c` | `--annachy-color-error-400` | VAR `1557:31595` |
| `Brand/Error/500` | `#ff614e` | `--annachy-color-error-500` | VAR `1557:31595` |
| `Brand/Error/600` | `#e72b23` | `--annachy-color-error-600` | VAR `1557:31595` |
| `Brand/Error/700` | `#9d4520` | `--annachy-color-error-700` | VAR `1557:31595` — **⚠ D-02: preserved as-is pending owner confirmation (equals Warning/700)** |
| `Brand/Error/800` | `#7a2515` | `--annachy-color-error-800` | VAR `1557:31595` |
| `Brand/Error/900` | `#521e11` | `--annachy-color-error-900` | VAR `1557:31595` |
| `Brand/Info/100` | `#f6faff` | `--annachy-color-info-100` | VAR `1557:31595` |
| `Brand/Info/200` | `#dbedfd` | `--annachy-color-info-200` | VAR `1557:31595` |
| `Brand/Info/300` | `#a6d3f9` | `--annachy-color-info-300` | VAR `1557:31595` |
| `Brand/Info/400` | `#71b9f7` | `--annachy-color-info-400` | VAR `1557:31595` |
| `Brand/Info/500` | `#186eb5` | `--annachy-color-info-500` | VAR `1557:31595` |
| `Brand/Info/600` | `#165d99` | `--annachy-color-info-600` | VAR `1557:31595` |
| `Brand/Info/700` | `#154f81` | `--annachy-color-info-700` | VAR `1557:31595` |
| `Brand/Info/800` | `#124067` | `--annachy-color-info-800` | VAR `1557:31595` |
| `Brand/Info/900` | `#102e48` | `--annachy-color-info-900` | VAR `1557:31595` |

## 2. Colour — semantic, theme-dependent (`src/tokens/themes/light.css`)

Semantic tokens hold **literal resolved values** (alias chains in Figma are not retrievable — `02` §6). Dark values observed in Figma are listed for the future dark theme but are **not shipped in V1** (D-03).

| Figma variable | Light value (V1) | CSS custom property | Evidence | Observed Dark value (not shipped) |
|---|---|---|---|---|
| `Brand/Text/Primary` | `#0b0c0f` | `--annachy-color-text-primary` | BIND (Dropdown, Checkbox, Toggle) | `#fafcff` |
| `Brand/Text/Secondary` | `#555d6d` | `--annachy-color-text-secondary` | BIND (Dropdown search) | — |
| `Brand/Text/Tertiary` | `#707a8f` | `--annachy-color-text-tertiary` | BIND (Dropdown, Checkbox) | `#707a8f` |
| `Brand/Text/Black` | `#0b0c0f` | `--annachy-color-text-black` | VAR | — |
| `Brand/Text/Brand` | `#004feb` | `--annachy-color-text-brand` | VAR | — |
| `Brand/Text/Grey` | `#1f242e` | `--annachy-color-text-grey` | VAR | — |
| `Brand/Text/White` | `#fafcff` | `--annachy-color-text-white` | VAR | — |
| `Brand/Background/Primary` | `#fafcff` | `--annachy-color-background-primary` | BIND (Checkbox, Radio) | — |
| `Brand/Background/Secondary` | `#f6f7f9` | `--annachy-color-background-secondary` | BIND (Dropdown, Input/Filled) | `#181b21` |
| `Brand/Background/Tertiary` | `#edeff2` | `--annachy-color-background-tertiary` | BIND (Dropdown Item Hover) | — |
| `Brand/Border/Primary` | `#bfc4cf` | `--annachy-color-border-primary` | BIND (Dropdown Menu) | `#171e2a` |
| `Brand/Border/Secondary` | `#dcdfe5` | `--annachy-color-border-secondary` | BIND (Dropdown dividers) | — |
| `Brand/Icon/Primary` | `#0b0c0f` | `--annachy-color-icon-primary` | VAR | — |
| `Brand/Icon/Secondary` | `#555d6d` | `--annachy-color-icon-secondary` | VAR | — |
| `Brand/Icon/Tertiary` | `#98a0ae` | `--annachy-color-icon-tertiary` | VAR | — |
| `Brand/Action/Primary` | `#004feb` | `--annachy-color-action-primary` | VAR | — |
| `Brand/Action/Hover` | `#003fbc` | `--annachy-color-action-hover` | VAR | — |
| `Brand/Action/Active` | `#002f8d` | `--annachy-color-action-active` | VAR | — |
| `Brand/Action/Disabled` | `#bfc4cf` | `--annachy-color-action-disabled` | VAR | — |
| `Brand/Feedback/Success` | `#14a047` | `--annachy-color-feedback-success` | VAR | — |
| `Brand/Feedback/Success Light` | `#f4fbef` | `--annachy-color-feedback-success-light` | VAR | — |
| `Brand/Feedback/Warning` | `#f26e2d` | `--annachy-color-feedback-warning` | VAR | — |
| `Brand/Feedback/Warning Light` | `#fff8f1` | `--annachy-color-feedback-warning-light` | VAR | — |
| `Brand/Feedback/Error` | `#ff614e` | `--annachy-color-feedback-error` | VAR | — |
| `Brand/Feedback/Error Light` | `#fff7f6` | `--annachy-color-feedback-error-light` | VAR | — |
| `Brand/Feedback/Info` | `#186eb5` | `--annachy-color-feedback-info` | VAR | — |
| `Brand/Feedback/Info Light` | `#f6faff` | `--annachy-color-feedback-info-light` | VAR | — |

Additional observed Dark values for primitives (`1451:25265`): `Brand/Blue/500` `#004feb` (unchanged), `Brand/Base/White` `#fafcff` (unchanged).

## 3. Colour — component tokens, Button (`src/tokens/component-tokens.css`)

Figma variable paths are preserved exactly in the mapping column (note `Secondary-Grey` hyphen vs `Tertiary Grey` space — both normalise to `…-grey` in CSS).

| Figma variable | Value | CSS custom property | Evidence |
|---|---|---|---|
| `Brand/Button/Primary/Background/Default` | `#004feb` | `--annachy-color-button-primary-background-default` | BIND `887:364` |
| `Brand/Button/Primary/Background/Hover` | `#003fbc` | `--annachy-color-button-primary-background-hover` | BIND `887:424` |
| `Brand/Button/Primary/Background/Focus` | `#004feb` | `--annachy-color-button-primary-background-focus` | BIND `887:484` |
| `Brand/Button/Primary/Background/Pressed-Active` | `#3372ef` | `--annachy-color-button-primary-background-pressed-active` | BIND `887:544` |
| `Brand/Button/Primary/Background/Disabled` | `#bfc4cf` | `--annachy-color-button-primary-background-disabled` | BIND `887:604` |
| `Brand/Button/Primary/Border/Focus` | `#003fbc` | `--annachy-color-button-primary-border-focus` | BIND `887:484` |
| `Brand/Button/Primary/Content/Default` | `#fafcff` | `--annachy-color-button-primary-content-default` | BIND `887:364` |
| `Brand/Button/Primary/Content/Disabled` | `#fafcff` | `--annachy-color-button-primary-content-disabled` | BIND `887:604` |
| `Brand/Button/Primary/Content/Loading` | `#fafcff` | `--annachy-color-button-primary-content-loading` | BIND (Toggle thumb `1504:54652`) |
| `Brand/Button/Secondary/Background/Default` | `#fafcff` | `--annachy-color-button-secondary-background-default` | VAR `1557:31595` |
| `Brand/Button/Secondary/Background/Hover` | `#f3f7ff` | `--annachy-color-button-secondary-background-hover` | BIND `887:724` |
| `Brand/Button/Secondary/Background/Pressed-Active` | `#e8f0ff` | `--annachy-color-button-secondary-background-pressed-active` | BIND `887:844` — off-palette |
| `Brand/Button/Secondary/Background/Loading` | `#fafcff` | `--annachy-color-button-secondary-background-loading` | BIND `887:2222` (R3-0a addendum, `r3-0-evidence.md` §4) |
| `Brand/Button/Secondary/Border/Default` | `#004feb` | `--annachy-color-button-secondary-border-default` | BIND `887:664` |
| `Brand/Button/Secondary/Border/Disabled` | `#bfc4cf` | `--annachy-color-button-secondary-border-disabled` | BIND `887:904` |
| `Brand/Button/Secondary/Content/Default` | `#004feb` | `--annachy-color-button-secondary-content-default` | BIND `887:664` |
| `Brand/Button/Secondary/Content/Disabled` | `#bfc4cf` | `--annachy-color-button-secondary-content-disabled` | BIND `887:904` |
| `Brand/Button/Secondary/Content/Loading` | `#004feb` | `--annachy-color-button-secondary-content-loading` | BIND `887:2222` (R3-0a addendum, `r3-0-evidence.md` §4) |
| `Brand/Button/Secondary-Grey/Background/Hover` | `#f6f7f9` | `--annachy-color-button-secondary-grey-background-hover` | BIND `887:1024` |
| `Brand/Button/Secondary-Grey/Background/Pressed-Active` | `#dcdfe5` | `--annachy-color-button-secondary-grey-background-pressed-active` | BIND `887:1144` |
| `Brand/Button/Secondary-Grey/Background/Loading` | `#fafcff` | `--annachy-color-button-secondary-grey-background-loading` | BIND `887:2282` (R3-0a addendum, `r3-0-evidence.md` §4) |
| `Brand/Button/Secondary-Grey/Border/Default` | `#bfc4cf` | `--annachy-color-button-secondary-grey-border-default` | BIND `887:964` |
| `Brand/Button/Secondary-Grey/Border/Focus` | `#004feb` | `--annachy-color-button-secondary-grey-border-focus` | BIND `887:1084` |
| `Brand/Button/Secondary-Grey/Border/Disabled` | `#dcdfe5` | `--annachy-color-button-secondary-grey-border-disabled` | BIND `887:1144`, `887:1204` (⚠ SUS-03 binding on Pressed) |
| `Brand/Button/Secondary-Grey/Content/Default` | `#1f242e` | `--annachy-color-button-secondary-grey-content-default` | BIND `887:964` |
| `Brand/Button/Secondary-Grey/Content/Disabled` | `#bfc4cf` | `--annachy-color-button-secondary-grey-content-disabled` | BIND `887:1204` |
| `Brand/Button/Secondary-Grey/Content/Loading` | `#1f242e` | `--annachy-color-button-secondary-grey-content-loading` | BIND `887:2282` (R3-0a addendum, `r3-0-evidence.md` §4) |
| `Brand/Button/Tertiary/Background/Hover` | `#f3f7ff` | `--annachy-color-button-tertiary-background-hover` | BIND `887:1324` |
| `Brand/Button/Tertiary/Background/Pressed-Active` | `#e8f0ff` | `--annachy-color-button-tertiary-background-pressed-active` | BIND `887:1444` — off-palette |
| `Brand/Button/Tertiary/Border/Focus` | `#004feb` | `--annachy-color-button-tertiary-border-focus` | BIND `887:1384` |
| `Brand/Button/Tertiary/Content/Default` | `#004feb` | `--annachy-color-button-tertiary-content-default` | BIND `887:1264` |
| `Brand/Button/Tertiary/Content/Pressed-Active` | `#003fbc` | `--annachy-color-button-tertiary-content-pressed-active` | BIND `887:1444` |
| `Brand/Button/Tertiary/Content/Disabled` | `#bfc4cf` | `--annachy-color-button-tertiary-content-disabled` | BIND `887:1504` |
| `Brand/Button/Tertiary/Content/Loading` | `#004feb` | `--annachy-color-button-tertiary-content-loading` | BIND `887:2342` (R3-0a addendum, `r3-0-evidence.md` §4) |
| `Brand/Button/Tertiary Grey/Background/Hover` | `#f3f4f7` | `--annachy-color-button-tertiary-grey-background-hover` | BIND `887:1624` — off-palette |
| `Brand/Button/Tertiary Grey/Background/Pressed-Active` | `#e4e7ec` | `--annachy-color-button-tertiary-grey-background-pressed-active` | BIND `887:1744` — off-palette |
| `Brand/Button/Tertiary Grey/Border/Focus` | `#004feb` | `--annachy-color-button-tertiary-grey-border-focus` | BIND `887:1684` |
| `Brand/Button/Tertiary Grey/Content/Default` | `#1f242e` | `--annachy-color-button-tertiary-grey-content-default` | BIND `887:1564` |
| `Brand/Button/Tertiary Grey/Content/Disabled` | `#bfc4cf` | `--annachy-color-button-tertiary-grey-content-disabled` | BIND `887:1804` |
| `Brand/Button/Tertiary Grey/Content/Loading` | `#1f242e` | `--annachy-color-button-tertiary-grey-content-loading` | BIND `887:2402` (R3-0a addendum, `r3-0-evidence.md` §4) |
| `Brand/Button/Link/Border/Focus` | `#004feb` | `--annachy-color-button-link-border-focus` | BIND `887:1984` |
| `Brand/Button/Link/Content/Default` | `#004feb` | `--annachy-color-button-link-content-default` | BIND `887:1864` |
| `Brand/Button/Link/Content/Pressed-Active` | `#003fbc` | `--annachy-color-button-link-content-pressed-active` | BIND `887:2044` |
| `Brand/Button/Link/Content/Disabled` | `#bfc4cf` | `--annachy-color-button-link-content-disabled` | BIND `887:2104` |
| `Brand/Button/Link/Content/Loading` | `#004feb` | `--annachy-color-button-link-content-loading` | BIND `887:2462` (R3-0a addendum, `r3-0-evidence.md` §4) |
| `Brand/Button/Gradient Start` | `#3a79f7` | `--annachy-color-button-gradient-start` | VAR `1557:31595` |
| `Brand/Button/Gradient End` | `#1746a2` | `--annachy-color-button-gradient-end` | VAR `1557:31595` |
| `Brand/Button/Success` | `#14a047` | `--annachy-color-button-success` | VAR `1557:31595` |
| `Brand/Button/Warning` | `#f26e2d` | `--annachy-color-button-warning` | VAR `1557:31595` |
| `Brand/Button/Error` | `#ff614e` | `--annachy-color-button-error` | VAR `1557:31595` |

## 4. Colour — non-`Brand/*` variables bound by components (preserved for fidelity)

D-01 makes `Brand/*` canonical. The variables below are **not** `Brand/*` but are **bound by production components**; omitting them would break visual fidelity. They are kept in clearly separated namespaces.


### 4.1 Icon semantic state (`src/tokens/component-tokens.css`)

| Figma variable | Value | CSS custom property | Evidence |
|---|---|---|---|
| `brand` | `#004feb` | `--annachy-color-icon-state-brand` | BIND Input/Filled; icon pilot `1106:12812` |
| `disabled` | `#bfc4cf` | `--annachy-color-icon-state-disabled` | VAR `1106:12812` |
| `error` | `#e72b23` | `--annachy-color-icon-state-error` | BIND Input Error `1066:39889` |
| `success` | `#276732` | `--annachy-color-icon-state-success` | BIND Input Success `1066:40339` |
| `warning` | `#b9512e` | `--annachy-color-icon-state-warning` | VAR `1106:12812` |

### 4.2 Foreign compatibility tokens (`src/tokens/compat.css`) — ⚠ D-19 open

| Figma variable | Value | CSS custom property | Evidence |
|---|---|---|---|
| `surface-bg` | `#ffffff` | `--annachy-compat-color-surface-bg` | BIND Checkbox/Radio Unchecked `1504:53819`, `1504:52738` |
| `border-default` | `#e1e1e2` | `--annachy-compat-color-border-default` | BIND Checkbox/Radio Unchecked |
| `Colors/alpha/50` | `#1a1a1a14` | `--annachy-compat-color-alpha-50` | BIND Checkbox/Radio Focus `1504:53976` |
| `Blur/blur-0` | `0` | `--annachy-compat-blur-0` | BIND (used inside `shadow/sm`) |
| `Blur/blur-2` | `3` | `--annachy-compat-blur-2` | BIND (used inside `shadow/sm`) |

## 5. Colour — excluded from V1 tokens (documented, not shipped)

| Figma variable(s) | Reason | Source |
|---|---|---|
| Lowercase scheme (`text/*`, `brand/*`, `background/*`, `border/*`, `icon/primary`, `grid` colours) | Non-canonical per D-01; never bound by components; 8 value conflicts | `02` §2.2 |
| `Supporting/*` (12) | Duplicates of `Brand/*` values; not in canonical scheme | `02` §1.5 |
| `Gradient`, `Brand/Blue/Gradient/04`, `/08`, `/09` | Paint styles with no resolvable value | `02` §2, `05` §2 |
| `Text/Neutral/*`, `Background/Neutral/*`, `Border/Neutral/*`, `--sds-*` | Simple Design System variables on documentation pages only | `05` E7 |
| `Brand / Blue-Grey / 600` (spaced) | Documentation-only duplicate of `Brand/Blue-Grey/600` | `05` E8 |
| Raw `#3a6ff7` (Input/Outline focus border) | Unbound raw value; belongs to R3 component spec, not a token | `components/input.md` IN2 |

## 6. Typography (`src/tokens/primitives.css` + `src/tokens/typography.css`)


### 6.1 Primitives

| Figma variable | Value | CSS custom property | Evidence |
|---|---|---|---|
| `Font Family/Sans Serif` | `Proxima Nova` | `--annachy-font-family-sans` | BIND (all components). Fallback stack **not defined** (D-06) |
| `Weight/Regular` | 400 | `--annachy-font-weight-regular` | BIND |
| `Weight/Medium` | 500 | `--annachy-font-weight-medium` | BIND |
| `Weight/Semibold` | 600 | `--annachy-font-weight-semibold` | BIND |
| Bold (Typography System) | 700 | `--annachy-font-weight-bold` | DOC `1557:39451` (H1–H3, H8) |
| Light (Typography System) | 300 | `--annachy-font-weight-light` | DOC `1557:39451` — listed, used by no style |
| letterSpacing (all text styles) | 0 | `--annachy-font-letter-spacing` | BIND (`letterSpacing: 0`) + DOC rule |

### 6.2 Type styles — Typography System (Scale A, `1557:39451`)

Each style produces: `--annachy-type-<style>-font-size`, `-line-height`, `-font-weight` (**active = Mobile value**, as resolved by components — `03` T12), plus reference tokens `-font-size-mobile`, `-line-height-mobile`, `-font-size-desktop`, `-line-height-desktop`. Desktop values are **not activated** in R1 (no switch width — D-05/D-07). Values in px.

| Style (Figma) | CSS style key | Weight | Mobile size / LH (active) | Desktop size / LH (reference) | Row node | Evidence | Used by / note |
|---|---|---|---|---|---|---|---|
| H1 | `h1` | Bold | 32 / 38 | 48 / 58 | `1558:48884` | DOC | — |
| H2 | `h2` | Bold | 28 / 36 | 40 / 48 | `1558:48892` | DOC | — |
| H3 (Bold) | `h3-bold` | Bold | 26 / 34 | 36 / 42 | `1558:48900` | DOC | ⚠ duplicate H3 (D-04 sub-item) — both rows preserved |
| H3 (Semibold) | `h3-semibold` | Semibold | 26 / 30 | 36 / 42 | `1558:48908` | DOC | ⚠ duplicate H3 (D-04 sub-item) — both rows preserved *(flag ID added 2026-11-19 for consistency with H3 Bold; no value change)* |
| H4 | `h4` | Semibold | 24 / 26 | 32 / 38 | `1558:48916` | DOC | — |
| H5 | `h5` | Semibold | 20 / 24 | 28 / 34 | `1558:48924` | BIND `Heading/H5/Semibold/*` | Button 52–56 |
| H6 | `h6` | Semibold | 18 / 20 | 24 / 28 | `1558:48932` | BIND `Heading/H6/Semibold/*` (LH var `Line Height 2`) | Button 46–48 |
| H7 | `h7` | Semibold | 16 / 18 | 20 / 24 | `1558:48940` | BIND `Heading/H7/Semibold/*` | Button 36–42, Input label |
| H8 | `h8` | Bold | 14 / 18 | 14 / 18 | `1558:48948` | DOC | — |
| Subheading L | `subheading-l` | Semibold | 18 / 25 | 20 / 28 | `1558:48989` | DOC (specimen 20 px APPLIED `1558:48970`) | — |
| Body L | `body-l` | Regular | 18 / 27 | 18 / 27 | `1558:48997` | DOC | — |
| Body M | `body-m` | Regular | 16 / 24 | 16 / 24 | `1558:49005` | BIND `Subheading & Body/Body/M/*` | Dropdown search |
| Body M — Medium | `body-m-medium` | Medium | 16 / 24 | 16 / 24 | `1558:49013` | BIND `Subheading & Body/Body/M-Medium/*` | Input value |
| Body S | `body-s` | Regular | 14 / 20 | 14 / 21 | `1558:49021` | BIND `Subheading & Body/Body/S/*` (style "Body S — Regular") | Input, Checkbox, Radio, Toggle |
| Body S — Medium | `body-s-medium` | Medium | 14 / 20 | 14 / 21 | `1558:49029` | DOC | — |
| Body S (Semibold) | `body-s-semibold` | Semibold | 14 / 18 | 14 / 18 | `1558:49069` | BIND `Subheading & Body/Body/XS-Semibold/*` (style "Body S - Semi") | Button 28–32, Tooltip — naming collision INC-57 |
| Body XS | `body-xs` | Medium | 12 / 18 | 12 / 18 | `1558:49037` | DOC | — |
| Body XS — Semibold | `body-xs-semibold` | Semibold | 12 / 18 | 12 / 18 | `1558:49045` | BIND `Subheading & Body/Body/XXS-Semibold/*` (style "Body XS — Semibold") | Button 24–26 — variable named XXS |
| Body XXS | `body-xxs` | Medium | 10 / 15 | 10 / 15 | `1558:49053` | DOC | — |
| Body Micro | `body-micro` | Semibold | 8 / 12 | 8 / 12 | `1558:49061` | DOC | — |
| Label Large | `label-large` | Medium | 18 / 22 | 18 / 25 | `1558:49114` | DOC (specimen 18 px APPLIED `1558:49092`) | — |
| Label Medium | `label-medium` | Medium | 16 / 21 | 16 / 22 | `1558:49122` | BIND `Labels & Captions/Label/Medium/*` | Checkbox, Radio, Toggle |
| Label Small | `label-small` | Medium | 14 / 20 | 14 / 20 | `1558:49130` | BIND `Labels & Captions/Label/Small/*` | Dropdown Item, wrapper |
| Label XSmall | `label-xsmall` | Regular | 12 / 17 | 12 / 18 | `1558:49138` | BIND `Labels & Captions/Label/XSmall/*` | Tooltip description |
| Label XSmall — SB | `label-xsmall-semibold` | Semibold | 12 / 17 | 12 / 18 | `1558:49146` | DOC | — |
| Caption Small | `caption-small` | Semibold | 11 / 15 | 11 / 15 | `1558:49154` | DOC | — |
| Caption XSmall | `caption-xsmall` | Regular | 10 / 14 | 10 / 14 | `1558:49162` | DOC | — |
| Caption Micro | `caption-micro` | Medium | 8 / 10 | 8 / 12 | `1558:49170` | DOC | — |

Specimen-sheet styles (Scale B, `1557:44867`: Display XL, Display L, Subtitle, Caption 12/16, Label 11/14, …) are **not tokenised** (D-04).

## 7. Dimensions (`src/tokens/primitives.css`)


### 7.1 Component heights

| Figma variable | Value | CSS custom property | Evidence |
|---|---|---|---|
| `Height/24` | 24px | `--annachy-size-height-24` | BIND (Button `887:*`, Dropdown footer) |
| `Height/26` | 26px | `--annachy-size-height-26` | BIND (Button `887:*`, Dropdown footer) |
| `Height/28` | 28px | `--annachy-size-height-28` | BIND (Button `887:*`, Dropdown footer) |
| `Height/32` | 32px | `--annachy-size-height-32` | BIND (Button `887:*`, Dropdown footer) |
| `Height/36` | 36px | `--annachy-size-height-36` | BIND (Button `887:*`, Dropdown footer) |
| `Height/38` | 38px | `--annachy-size-height-38` | BIND (Button `887:*`, Dropdown footer) |
| `Height/40` | 40px | `--annachy-size-height-40` | BIND (Button `887:*`, Dropdown footer) |
| `Height/42` | 42px | `--annachy-size-height-42` | BIND (Button `887:*`, Dropdown footer) |
| `Height/46` | 46px | `--annachy-size-height-46` | BIND (Button `887:*`, Dropdown footer) |
| `Height/48` | 48px | `--annachy-size-height-48` | BIND (Button `887:*`, Dropdown footer) |
| `Height/52` | 52px | `--annachy-size-height-52` | BIND (Button `887:*`, Dropdown footer) |
| `Height/56` | 56px | `--annachy-size-height-56` | BIND (Button `887:*`, Dropdown footer) |

### 7.2 Radius

| Figma variable | Value | CSS custom property | Evidence | Documented usage |
|---|---|---|---|---|
| `Radius/4` | 4px | `--annachy-radius-4` | BIND (Button 24–28, Checkbox `1504:53701`) | Small UI elements |
| `Radius/8` | 8px | `--annachy-radius-8` | BIND (Button 32–40, Input, Dropdown Item) | Inputs, small cards |
| `Radius/12` | 12px | `--annachy-radius-12` | BIND (Button 42–56, Dropdown Menu) | Buttons, cards |
| `Radius/14` | 14px | `--annachy-radius-14` | DOC `1561:57646` | Medium components |
| `Radius/16` | 16px | `--annachy-radius-16` | DOC | Cards, containers |
| `Radius/18` | 18px | `--annachy-radius-18` | DOC | Larger cards |
| `Radius/24` | 24px | `--annachy-radius-24` | DOC | Large surfaces |
| `Radius/26` | 26px | `--annachy-radius-26` | DOC | Large visual components |
| `Radius/28` | 28px | `--annachy-radius-28` | DOC | Large cards / promotional UI |
| `Radius/32` | 32px | `--annachy-radius-32` | DOC | Large containers |
| `Radius/34` | 34px | `--annachy-radius-34` | DOC | Special large components |

Not tokenised: Input `Radius` variant values **6** and **10** (not in the scale — component-local in R3, D-09); `Radius/S = 8` (meaning unknown; duplicates `Radius/8`).

### 7.3 Border widths

| Figma variable | Value | CSS custom property | Evidence |
|---|---|---|---|
| `Border/XS` | 0.5px | `--annachy-border-width-xs` | VAR `1563:58676` |
| `Border/S` | 1px | `--annachy-border-width-s` | VAR `1563:58676` |
| `Border/M` | 1.5px | `--annachy-border-width-m` | VAR `1563:58676` |

Observed in components but not variables: 1px (Input, Dropdown), 1.5px (gradient Button), 2px (focus states) — component-local in R3.

### 7.4 Grid (no breakpoints — D-07)

| Figma variable / doc | Mobile | Desktop | Large Desktop | CSS custom properties | Evidence |
|---|---|---|---|---|---|
| `grid/width` · frame width | 360px | 1440px | 1920px | `--annachy-grid-{mobile,desktop,large}-frame-width` | VAR (Desktop) + DOC `1558:55670` |
| `grid/columns` | 4 | 12 | 12 | `--annachy-grid-{…}-columns` | VAR (Desktop) + DOC |
| `grid/margin` | 16px | 120px | 140px | `--annachy-grid-{…}-margin` | VAR (Desktop) + DOC |
| `grid/gutter` | 16px | 32px | 32px | `--annachy-grid-{…}-gutter` | VAR (Desktop) + DOC |
| `grid/height` | — | 1024px | — | `--annachy-grid-desktop-frame-height` | VAR (Desktop only) |

These are **reference values only**. No media queries, no breakpoint ranges and no max-width are defined (D-07). Mobile reference width 360 vs PDP 393 is unresolved (`04` L12).

### 7.5 Spacing (D-08)

**No spacing tokens.** Figma defines no spacing scale. Evidenced padding/gap values (2, 4, 6, 8, 10, 12, 14, 16, 18, 20 px) are preserved **per component** in R3, each with its node ID (`13` §D-08). The variable `S = 8` (`1563:58676`) is not tokenised (meaning unknown).

## 8. Effects (`src/tokens/effects.css`)


### 8.1 Documented shadow styles (Shadow page) — values exact, colours kept as Figma `#RRGGBBAA`

Not used by any inspected component (`05` §3.1). Preserved for fidelity. Fractional Figma values are kept unrounded.

| Figma effect style | CSS custom property | Value (`box-shadow`) | Evidence |
|---|---|---|---|
| `Shadow Scale/SM/01` | `--annachy-shadow-scale-sm-01` | `1.9500000476837158px 1.9500000476837158px 2.5999999046325684px 0px #00000026` | VAR `1561:57814` |
| `Shadow Scale/SM/02` | `--annachy-shadow-scale-sm-02` | `0px 1px 4px 0px #00000029` | VAR `1561:57814` |
| `Shadow Scale/SM/03` | `--annachy-shadow-scale-sm-03` | `0px 1px 4px 0px #00000029, 0px 0px 0px 3px #333333` | VAR `1561:57814` |
| `Shadow Scale/SM/04` | `--annachy-shadow-scale-sm-04` | `0px 1px 3px 0px #00000005, 0px 0px 0px 1px #1b1f2326` | VAR `1561:57814` |
| `Shadow Scale/SM/05` | `--annachy-shadow-scale-sm-05` | `0px 2px 5px -1px #32325d40, 0px 1px 3px -1px #0000004d` | VAR `1561:57814` |
| `Shadow Scale/MD/01` | `--annachy-shadow-scale-md-01` | `0px 3px 8px 0px #00000040` | VAR `1561:57814` |
| `Shadow Scale/MD/02` | `--annachy-shadow-scale-md-02` | `0px 2px 8px 0px #63636333` | VAR `1561:57814` |
| `Shadow Scale/MD/03` | `--annachy-shadow-scale-md-03` | `0px 4px 12px 0px #0000001a` | VAR `1561:57814` |
| `Shadow Scale/LG/01` | `--annachy-shadow-scale-lg-01` | `0px 8px 24px 0px #959da533` | VAR `1561:57814` |
| `Shadow Scale/LG/02` | `--annachy-shadow-scale-lg-02` | `0px 5px 15px 0px #00000059` | VAR `1561:57814` |
| `Shadow Scale/LG/03` | `--annachy-shadow-scale-lg-03` | `0px 6px 24px 0px #0000000d, 0px 0px 0px 1px #00000014` | VAR `1561:57814` |
| `Shadow Scale/XL/01` | `--annachy-shadow-scale-xl-01` | `0px 7px 29px 0px #64646f33` | VAR `1561:57814` |
| `Shadow Scale/XL/02` | `--annachy-shadow-scale-xl-02` | `0px 0px 0px 1px #0000000f, 0px 10px 36px 0px #00000029` | VAR `1561:57814` |
| `Shadow Scale/XL/03` | `--annachy-shadow-scale-xl-03` | `0px 13px 27px -5px #32325d40, 0px 8px 16px -8px #0000004d` | VAR `1561:57814` |
| `Shadow Scale/XXL/01` | `--annachy-shadow-scale-xxl-01` | `0px 48px 100px 0px #110c2e26` | VAR `1561:57814` |
| `Shadow Scale/XXL/02` | `--annachy-shadow-scale-xxl-02` | `0px 50px 100px -20px #32325d40, 0px 30px 60px -30px #0000004d, inset 0px -2px 6px 0px #0a254059` | VAR `1561:57814` |
| `Shadow Scale/XXL/03` | `--annachy-shadow-scale-xxl-03` | `inset 0px 1px 1px 0px #ffffff1a, 0px 50px 100px -20px #32325d40, 0px 30px 60px -30px #0000004d` | VAR `1561:57814` |
| `Shadow Effects/SM/Peck` | `--annachy-shadow-effects-sm-peck` | `0px 1px 1px 0px #0000000d, 0px 2px 1px 0px #00000003, 0px 3px 1px 0px #00000005` | VAR `1561:58161` |
| `Shadow Effects/SM/Stub` | `--annachy-shadow-effects-sm-stub` | `0px 1px 1px 0px #00000005, 0px 2px 4px 0px #0000000a, 0px 2px 2px 0px #00000003, 0px 2px 2px 0px #00000014, 0px 1px 0px 0px #0000001f` | VAR `1561:58161` |
| `Shadow Effects/SM/Popup` | `--annachy-shadow-effects-sm-popup` | `0px 0px 1px 0px #00000014, 0px 1px 1px 0px #00000014, 0px 3px 2px 0px #0000000a, 0px 5px 2px 0px #00000003` | VAR `1561:58161` |
| `Shadow Effects/SM/Raised` | `--annachy-shadow-effects-sm-raised` | `0px 0px 1px 0px #00000014, 0px -1px 1px 0px #00000014, 0px -2px 1px 0px #0000000a, 0px -4px 1px 0px #00000003, 0px 1px 1px 0px #00000014, 0px 2px 2px 0px #00000014, 0px 6px 3px 0px #0000000a` | VAR `1561:58161` |
| `Shadow Effects/SM/Top Light` | `--annachy-shadow-effects-sm-top-light` | `0px 1px 2px 0px #00000014, 0px 3px 3px 0px #00000014, 0px 8px 4px 0px #0000000a, 0px 13px 5px 0px #00000003` | VAR `1561:58161` |
| `Shadow Effects/SM/Bottom Light` | `--annachy-shadow-effects-sm-bottom-light` | `0px -1px 2px 0px #00000014, 0px -3px 3px 0px #00000014, 0px -8px 4px 0px #0000000a, 0px -13px 5px 0px #00000003` | VAR `1561:58161` |
| `Shadow Effects/SM/Left Light` | `--annachy-shadow-effects-sm-left-light` | `0px 1px 1px 0px #00000014, 1px 2px 2px 0px #00000014, 2px 6px 4px 0px #0000000a, 4px 8px 4px 0px #00000003, 8px 12px 4px 0px #00000003` | VAR `1561:58161` |
| `Shadow Effects/SM/Right Light` | `--annachy-shadow-effects-sm-right-light` | `0px 1px 1px 0px #00000014, -1px 2px 2px 0px #00000014, -2px 6px 4px 0px #0000000a, -4px 8px 4px 0px #00000003, -8px 12px 4px 0px #00000003` | VAR `1561:58161` |
| `Shadow Effects/MD/Lozenge` | `--annachy-shadow-effects-md-lozenge` | `inset 0px 0px 1px 0px #00000029, inset 0px -1px 1px 0px #00000029, inset 0px -4px 8px 0px #00000014, inset 0px -7px 12px 0px #0000000a, inset 0px -16px 8px 0px #00000003, inset 0px -1px 1px 0px #ffffff4d, inset 0.5px 1px 1px 0px #ffffff4d, inset -0.5px 1px 8px 0px #ffffff33` | VAR `1561:58161` |
| `Shadow Effects/MD/Stub Inset` | `--annachy-shadow-effects-md-stub-inset` | `inset 0px -1px 0px 0px #00000029, inset 0px -1px 1px 0px #0000003d, inset 0px -8px 12px 0px #0000000a, inset 0px -16px 12px 0px #00000003` | VAR `1561:58161` |
| `Shadow Effects/LG/Bubble` | `--annachy-shadow-effects-lg-bubble` | `0px 1px 2px 0px #0000001a, 0px 3px 5px 0px #0000000a, 0px 7px 4px 0px #00000005, 0px 13px 5px 0px #00000005, 0px 20px 6px 0px #00000003, inset 2px 1px 8px 0px #00000014, inset 2px 3px 6px 0px #0000000f, inset 2px 7px 16px 0px #0000000a, inset 2px 13px 5px 0px #00000003, inset 2px 20px 16px 0px #0000000a` | VAR `1561:58161` |
| `Shadow Effects/LG/Hard Inset` | `--annachy-shadow-effects-lg-hard-inset` | `inset 0px 1px 4px 0px #0000003d, inset 0px 8px 16px 0px #0000001f, inset 0px 16px 8px 0px #0000000a` | VAR `1561:58161` |
| `Shadow Effects/LG/Hard Lift` | `--annachy-shadow-effects-lg-hard-lift` | `0px 1px 2px 0px #00000029, 0px 3px 3px 0px #00000029, 0px 8px 16px 0px #0000001f, 0px 13px 5px 0px #00000003` | VAR `1561:58161` |
| `Shadow Effects/LG/Soft Inset` | `--annachy-shadow-effects-lg-soft-inset` | `inset 0px 1px 2px 0px #0000001f, inset 0px 8px 16px 0px #0000000a, inset 0px 16px 8px 0px #00000003` | VAR `1561:58161` |
| `Shadow Effects/XXL/Dialog` | `--annachy-shadow-effects-xxl-dialog` | `0px 4px 12px 0px #00000024, 0px 20px 20px 0px #0000001f, 0px 48px 24px 0px #0000000a, 0px 80px 24px 0px #00000008, 0px 40px 80px 0px #00000003` | VAR `1561:58161` |
| `Shadow` | `--annachy-shadow-swatch` | `-1.3851852416992188px 2.7703704833984375px 6.925926208496094px 0px #0000001a, -2.7703704833984375px 12.466667175292969px 13.851852416992188px 0px #00000017, -6.925926208496094px 29.088890075683594px 18.007408142089844px 0px #0000000d, -12.466667175292969px 52.63703918457031px 22.1629638671875px 0px #00000003, -18.007408142089844px 81.7259292602539px 23.54814910888672px 0px #00000000` | VAR `1557:23523` (colour swatches) |

### 8.2 Effect styles used by components (undocumented on Shadow page)

| Figma effect style | CSS custom property | Value (`box-shadow`) | Evidence |
|---|---|---|---|
| `Button/Default` | `--annachy-effect-button-default` | `0px 1px 1px 0px #17191c21, -1px 2px 1px 0px #17191c14, -1px 3px 1px 0px #17191c05, -2px 4px 2px 0px #17191c00` | BIND `1504:53701`, `1504:52685` |
| `Button/Hover` | `--annachy-effect-button-hover` | `0px 0px 1px 0px #325cb34f, 0px 0px 2px 0px #325cb345, 0px 0px 3px 0px #325cb329, 0px 0px 3px 0px #325cb30d, 0px 0px 3px 0px #325cb303` | BIND `1504:54031`, `1504:52943` |
| `Button/Focus` | `--annachy-effect-button-focus` | `0px 0px 2px 0px #0141c07d, 0px 1px 3px 0px #0141c06e, -1px 2px 4px 0px #0141c040, -2px 3px 4px 0px #0141c012, -3px 4px 5px 0px #0141c003` | BIND `1451:25074`, `1504:53976`, `1504:52889` |
| `Toggle/On` | `--annachy-effect-toggle-on` | `0px 0px 1px 0px #00000017, -1px 1px 1px 0px #0000000d, -2px 1px 1px 0px #00000003, -2px 2px 1px 0px #00000000` | BIND `1504:54622` … |
| `Toggle/Off` | `--annachy-effect-toggle-off` | `0px 0px 1px 0px #3c343417, 1px 1px 1px 0px #3c34340d, 2px 2px 1px 0px #3c343403, 3px 2px 1px 0px #3c343400` | BIND `1504:54637` … |
| `Toggle/Press` | `--annachy-effect-toggle-press` | `0px 0px 1px 0px #004feb4a, 0px 1px 2px 0px #004feb42, -1px 2px 2px 0px #004feb26, -2px 4px 2px 0px #004feb0a, -3px 7px 3px 0px #004feb03` | BIND `1504:54712` |
| `shadow/sm` (foreign) | `--annachy-compat-shadow-sm` | `0px 1px 3px 0px #1a1a1a14, 0px 0.5px 0px 0px #1a1a1a14` (blur via `Blur/blur-2`=3, `Blur/blur-0`=0; colour 2 via `Colors/alpha/50`) | BIND `1504:53976`, `1504:52889` — ⚠ D-19 (in `compat.css`) |

### 8.3 Blur & Glass

| Figma style | Figma value | CSS custom property | Value | Evidence / note |
|---|---|---|---|---|
| `Blur/XS-01` | FOREGROUND_BLUR 4 | `--annachy-blur-xs-01` | 4px | VAR `1563:58676` |
| `Blur/SM-01` | FOREGROUND_BLUR **0** | `--annachy-blur-sm-01` | 0px | VAR — preserved as-is (D-11) |
| `Blur/SM-02` | FOREGROUND_BLUR **0** | `--annachy-blur-sm-02` | 0px | VAR — preserved as-is (D-11) |
| `Blur/MD-01` | FOREGROUND_BLUR **0** | `--annachy-blur-md-01` | 0px | VAR — preserved as-is (D-11) |
| `Blur/MD-02` | FOREGROUND_BLUR **0** | `--annachy-blur-md-02` | 0px | VAR — preserved as-is (D-11) |
| `Glass/XS-01` | GLASS 5 | `--annachy-glass-xs-01-radius` | 5px | VAR — radius only; other GLASS parameters not retrievable |
| `Glass/SM-01` | GLASS 10 | `--annachy-glass-sm-01-radius` | 10px | VAR — as above |
| `Glass/MD-01` | GLASS 20 | `--annachy-glass-md-01-radius` | 20px | VAR — as above |
| `Gradient/Full` | `#ffffff` | `--annachy-color-glass-gradient-full` | `#ffffff` | VAR `1563:58676` (glass fill stop) |
| `Gradient/XS` | `#ffffffbf` | `--annachy-color-glass-gradient-xs` | `#ffffffbf` | VAR |
| `Gradient/S` | `#ffffff40` | `--annachy-color-glass-gradient-s` | `#ffffff40` | VAR |
| `Gradient/M` | `#ffffff00` | `--annachy-color-glass-gradient-m` | `#ffffff00` | VAR |

### 8.4 Gradients

| Source | CSS custom property | Value | Evidence |
|---|---|---|---|
| Gradient button fill | `--annachy-gradient-brand` | `linear-gradient(22.572274294652743deg, var(--annachy-color-gradient-color-1) 13.397%, var(--annachy-color-gradient-color-2) 86.603%)` | APPLIED `1153:3371` (angle/stops exact) |

## 9. Token counts (R1)

> **R3-0a addendum (2026-11-19):** Button component colours 43 → **50** (+7 Loading variables); total 457 → **464**. No existing value changed.

| Group | Tokens |
|---|---|
| Colour primitives | 82 |
| Semantic colours (light) | 27 |
| Button component colours | 50 |
| Icon-state colours | 5 |
| Compat (foreign) values | 5 |
| Typography primitives | 7 |
| Type styles (× 7 properties each) | 28 |
| Heights | 12 |
| Radius | 11 |
| Border widths | 3 |
| Grid reference values | 13 |
| Documented shadows (incl. swatch) | 33 |
| Component effect styles (incl. compat) | 7 |
| Blur / Glass / glass fills | 12 |
| Gradients | 1 |
