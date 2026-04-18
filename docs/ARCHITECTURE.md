# Architecture

How this guide is built from Python sources into a single self-contained HTML file.

## Design goals

1. **Zero runtime dependencies** — works offline, from a USB stick, with no server
2. **Single file deliverable** — one `index.html` that teachers can email, host anywhere
3. **No build toolchain** — Python stdlib only. No npm, no webpack
4. **Trilingual-first** — baked into every node from the start
5. **Fast language switching** — CSS does the work, no JS re-render
6. **Verified API** — all MakeCode code compiles against the real `pxt-maqueen`

## Module layout

```
src/
├── assembler.py         # main() — orchestrates the build
├── build.py             # 16 activities (Phase 1) + CATS list
├── phase2.py            # 29 activities (IDs 17-45)
├── phase3.py            # 40 activities (IDs 46-85)
├── phase4.py            # 6 learning paths
├── translations.py      # EN + AR translations for IDs 1-16
├── translations_p2.py   # EN + AR translations for IDs 17-45
├── translations_p3.py   # EN + AR translations for IDs 46-85
├── i18n_module.py       # UI strings (FR/EN/AR) + FLAGS
├── css_module.py        # CSS: 9 themes + layout + print
├── js_module.py         # JavaScript runtime
└── help_module.py       # Pinout SVG + cheatsheet + FAQ (trilingual)
```

## Build pipeline

```
Python dicts ─→ assembler.py ─→ single index.html (1.2 MB)
```

1. Load activities — merge `build.py` + `phase2.py` + `phase3.py` → 85 dicts
2. Load translations — merge 3 translation files → dict keyed by activity ID
3. Render each activity three times (FR/EN/AR) with `lang`-attributed children
4. Render panels — sidebar, parcours, resources, help — all trilingual
5. Inline CSS and JS
6. Write HTML

## The trilingual trick

Every translatable element is rendered three times:

```html
<div class="goal-text" lang="fr">Objectif en français…</div>
<div class="goal-text" lang="en">Objective in English…</div>
<div class="goal-text" lang="ar">الهدف بالعربية…</div>
```

A single CSS rule determines visibility:

```css
html[lang="fr"] [lang]:not([lang="fr"]) { display: none !important; }
html[lang="en"] [lang]:not([lang="en"]) { display: none !important; }
html[lang="ar"] [lang]:not([lang="ar"]) { display: none !important; }
```

Switching language is one JS line:

```js
document.documentElement.setAttribute('lang', 'ar');
document.documentElement.setAttribute('dir', 'rtl');
```

**Why this approach?**
- ✅ Zero JS on switch (fast, no flicker)
- ✅ SEO indexes all three languages
- ✅ Print captures the visible language naturally
- ✅ Screen readers get correct language context per element

**Trade-off:** ~3× file size vs single language. Acceptable for 1.2 MB.

## MakeCode API surface (verified)

The code in every activity is written against the actual `pxt-maqueen` API from [DFRobot/pxt-maqueen](https://github.com/DFRobot/pxt-maqueen):

### `maqueen` namespace (works on all Maqueen Lite hardware)

```typescript
maqueen.motorRun(Motors.M1|M2|All, Dir.CW|CCW, speed 0-255)
maqueen.motorStop(Motors.M1|M2|All)
maqueen.Ultrasonic() : number               // cm, no argument
maqueen.readPatrol(Patrol.PatrolLeft|PatrolRight) : 0|1
maqueen.writeLED(LED.LEDLeft|LEDRight, LEDswitch.turnOn|turnOff)
maqueen.servoRun(Servos.S1|S2, angle 0-180)
maqueen.IR_Read(IR_Pin.P16)
maqueen.IR_ReadValue() : number             // inside IR_Callback
```

### `neopixel` (separate extension for RGB LEDs on P15)

```typescript
let strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)
strip.showColor(neopixel.colors(NeoPixelColors.Red))
strip.showColor(neopixel.rgb(255, 100, 0))
strip.setPixelColor(index, color); strip.show()
strip.clear(); strip.show()
```

### Common errors (DO NOT USE)

```typescript
❌ maqueen.showColor(...)           // doesn't exist
❌ maqueen.clear()                  // doesn't exist
❌ maqueen.Ultrasonic(PingUnit.Centimeters)  // no argument
```

These were present in v1.0.0 and fixed in v1.0.1 — see [CHANGELOG](../CHANGELOG.md).

## Per-activity card structure

```html
<section class="act-section" id="act-{N}">
  <div class="act-header-bar">
    <div class="act-title-text" lang="fr">…</div>
    <div class="act-title-text" lang="en">…</div>
    <div class="act-title-text" lang="ar">…</div>
  </div>

  <!-- Objective, Materials, Steps, Tip: 3 langs each -->
  <div class="goal-text" lang="fr">…</div>
  <ol class="steps-list" lang="fr">…</ol>
  ...

  <!-- Flowchart + pseudo-code: auto-generated per language -->
  <div lang="fr"><div class="flowchart">…</div><div class="pseudo-box">…</div></div>
  <div lang="en">…</div>
  <div lang="ar">…</div>

  <!-- Code is universal -->
  <div class="code-grid">
    <div class="code-panel js-header">…</div>
    <div class="code-panel py-header">…</div>
  </div>

  <!-- Challenges: 3 langs -->
  <div class="chal-list" lang="fr">…</div>
</section>
```

## Auto-generated flowcharts

Each activity's step list becomes a flowchart via `gen_flowchart()`. Heuristics detect node types (loop/decision/io/process) from keywords in multiple languages. Labels translate per language:

- FR: `DÉBUT` / `FIN`
- EN: `START` / `END`
- AR: `البداية` / `النهاية`

Total: **85 activities × 3 languages = 255 flowcharts + 255 pseudo-code boxes**.

## State management

```js
const STATE = {
  lang: 'fr',          // persisted in localStorage
  theme: 'mosque',     // persisted
  sound: true,         // persisted
  progress: Set<int>,  // activity IDs marked done, persisted
};
```

No framework, no reactivity. State changes trigger direct DOM mutations and localStorage writes.

## Print CSS

Ctrl+P activates the print stylesheet:
- Hides sidebar, topbar, panels, buttons
- Page break before each activity
- Print-friendly flowchart colors
- Keeps only the active language

## Size budget

```
index.html           ~1.22 MB uncompressed
├── HTML structure   ~740 KB  (85 activities × 3 languages)
├── Inline CSS       ~46 KB
├── Inline JS        ~50 KB
└── Everything else  ~380 KB  (pinout SVGs ×3, cheatsheet ×3, FAQ ×3, parcours, resources)
```

With gzip (GitHub Pages auto): ~230 KB over the wire.

## What's intentionally NOT in this project

- ❌ No React/Vue/Svelte — vanilla JS suffices
- ❌ No TypeScript source — Python generates JS by templating
- ❌ No CSS-in-JS or Tailwind — raw CSS with variables
- ❌ No bundler — single file, ship it
- ❌ No analytics — respects student/teacher privacy
- ❌ No automated tests — a regression guard in CI catches API backslides

This is boring, unfashionable, and it will still work in 15 years.
