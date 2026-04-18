# Architecture

How this guide is built from Python sources into a single self-contained HTML file.

## Design goals

1. **Zero runtime dependencies** — the guide must work offline, from a USB stick, with no server
2. **Single file deliverable** — one `index.html` that a teacher can email, host on any static server, or bundle into a classroom LMS
3. **No build toolchain** — Python stdlib only. No npm, no webpack, no transpilation
4. **Trilingual-first** — never bolt translations on after the fact; bake them into every node from the start
5. **Fast language switching** — no JS re-render on language change; CSS does the work

## Module layout

```
src/
├── assembler.py         # main() — orchestrates the build, writes maqueen-guide.html
├── build.py             # 16 activities + CATS list (categories with icons/colors)
├── phase2.py            # 29 activities (IDs 17-45)
├── phase3.py            # 40 activities (IDs 46-85)
├── phase4.py            # 6 learning paths (parcours)
├── translations.py      # EN + AR translations for IDs 1-16
├── translations_p2.py   # EN + AR translations for IDs 17-45
├── translations_p3.py   # EN + AR translations for IDs 46-85
├── i18n_module.py       # UI strings dict (FR/EN/AR) + FLAGS dict
├── css_module.py        # CSS string — 9 themes + layout + print rules
├── js_module.py         # JavaScript runtime (state, navigation, themes, ⌘K)
└── help_module.py       # Pinout SVG generator + cheatsheet + FAQ (trilingual)
```

## Build pipeline

```
 Python dicts ─→ assembler.py renders HTML strings ─→ single maqueen-guide.html
```

1. **Load activities** — merge `build.py` + `phase2.py` + `phase3.py` → flat list of 85 dicts
2. **Load translations** — merge `translations.py` + `translations_p2.py` + `translations_p3.py` → dict keyed by activity ID
3. **Render each activity** three times (FR / EN / AR) inside a single `<section>` with `lang`-attributed children
4. **Render panels** — sidebar, parcours, resources, help — all trilingual with `lang` attributes
5. **Inline CSS and JS** — no external CSS or JS files
6. **Write HTML** — one template-string write, ~1.2 MB output

## The trilingual trick

Every translatable element is rendered three times, each with a `lang` attribute:

```html
<div class="goal-text" lang="fr">Objectif en français…</div>
<div class="goal-text" lang="en">Objective in English…</div>
<div class="goal-text" lang="ar">الهدف بالعربية…</div>
```

A single CSS rule determines which is visible:

```css
html[lang="fr"] [lang]:not([lang="fr"]) { display: none !important; }
html[lang="en"] [lang]:not([lang="en"]) { display: none !important; }
html[lang="ar"] [lang]:not([lang="ar"]) { display: none !important; }
```

Switching language is a single line of JavaScript:

```js
document.documentElement.setAttribute('lang', 'ar');
document.documentElement.setAttribute('dir', 'rtl');
```

**Why this approach?**
- ✅ Zero JS on language switch (fast, no flicker, no re-layout storms)
- ✅ Search engines index all three languages
- ✅ Print-to-PDF captures the currently-visible language naturally
- ✅ Every element carries its own language context for screen readers

**Trade-off:** file size is ~3× vs. a single language. Acceptable for 1.2 MB — a typical image on the web is heavier.

## Per-activity card structure

```
<section class="act-section" id="act-{N}">
  <div class="act-header-bar">          ← cat color accent, number badge
    <div class="act-title-text" lang="fr">…</div>  ← FR title
    <div class="act-title-text" lang="en">…</div>  ← EN title
    <div class="act-title-text" lang="ar">…</div>  ← AR title
    <div class="act-header-tags">
      <span class="tag-chip diff" lang="fr">★★☆ Intermédiaire</span>
      <span class="tag-chip diff" lang="en">★★☆ Intermediate</span>
      <span class="tag-chip diff" lang="ar">★★☆ متوسط</span>
      …
    </div>
  </div>

  <div class="glass-card">              ← Objective
    <div class="goal-text" lang="fr">…</div>
    <div class="goal-text" lang="en">…</div>
    <div class="goal-text" lang="ar">…</div>
  </div>

  <div class="needs-wrap" lang="fr">…</div>  ← Material pills per lang
  <ol class="steps-list" lang="fr">…</ol>    ← Steps per lang
  <div class="tip-box" lang="fr">…</div>     ← Tip per lang

  <!-- Flowchart + pseudo-code: one per language -->
  <div lang="fr">
    <div class="flowchart">…</div>
    <div class="pseudo-box">…</div>
  </div>
  <div lang="en">…</div>
  <div lang="ar">…</div>

  <!-- Code is universal (JS + Python are the same in any language) -->
  <div class="code-grid">…</div>

  <!-- Challenges per language -->
  <div class="chal-list" lang="fr">…</div>
  <div class="chal-list" lang="en">…</div>
  <div class="chal-list" lang="ar">…</div>
</section>
```

## Auto-generated flowcharts

Each activity's step list becomes a flowchart via `gen_flowchart()` in `assembler.py`. Heuristics detect node types:
- `répéter / repeat / كرر` → **loop** node (yellow)
- `si / if / إذا` → **decision** node (diamond, cyan)
- `lire / afficher / read / show / اقرأ` → **I/O** node (blue)
- Everything else → **process** node (green)

Flowcharts and pseudo-codes are generated once per activity per language, with translated START/END labels:
- FR: `DÉBUT` / `FIN`
- EN: `START` / `END`
- AR: `البداية` / `النهاية`

Total: 85 activities × 3 languages = **255 flowcharts, 255 pseudo-code boxes**.

## Themes

Nine themes, each defined as a CSS variable block in `css_module.py`:
- **Mosque, Zellige, Andalus** — Arabic/Andalusian aesthetics (Islamic geometric patterns)
- **Space, Jungle, Robot** — vibrant tech/nature palettes
- **Riad, Medina** — light themes (for print-friendly reading)
- **Retro** — CRT scanlines, Konami-unlocked easter egg

Each theme switches 8 core CSS variables: `--bg`, `--fg`, `--card`, `--accent`, `--accent2`, `--muted`, `--border`, `--shadow`.

## State management

All runtime state is in `js_module.py`:

```js
const STATE = {
  lang: 'fr',          // persisted in localStorage
  theme: 'mosque',     // persisted in localStorage
  sound: true,         // persisted in localStorage
  progress: Set<int>,  // activity IDs marked done, persisted in localStorage
  currentAct: null,    // scroll-spy state
};
```

No framework, no reactivity. State changes trigger direct DOM mutations and localStorage writes. For a doc this static, it's plenty.

## Print CSS

Ctrl+P / Cmd+P activates the print stylesheet which:
- Hides sidebar, topbar, all panels, all buttons
- Forces page breaks before each activity
- Converts flowchart colors to print-friendly shades
- Keeps code blocks readable on paper (smaller mono font)
- Strips the active-language filter so print captures whatever the teacher has selected

## Size budget

```
index.html           ~1.2 MB uncompressed
├── HTML structure   ~730 KB  (85 activities × 3 languages)
├── Inline CSS       ~46 KB
├── Inline JS        ~50 KB
└── Everything else  ~370 KB  (pinout SVGs, cheatsheet, FAQ, parcours, resources)
```

With gzip (served by GitHub Pages automatically): ~230 KB over the wire.

## What's intentionally NOT in this project

- ❌ No React/Vue/Svelte — vanilla JS is plenty
- ❌ No TypeScript — Python generates correct JS by string concatenation
- ❌ No CSS-in-JS or Tailwind — raw CSS with variables is clearer for theming
- ❌ No bundler — inline everything, single file, ship it
- ❌ No tests — visual inspection + HTML-balance check + JS parse-check in the build is enough for content like this
- ❌ No analytics — respect privacy of students and teachers

This is boring, unfashionable, and it will still work in 15 years.
