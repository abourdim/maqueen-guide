# Visual tour

What you'll see when you open `index.html`.

> 💡 This guide is a single HTML file — open it in any browser to see everything live. This doc describes the visuals in words since screenshots would go stale with every theme/content update.

## Cover page

On first load, you land on a splash with:
- **Big title** — "Maqueen Lite · Guide Terrain" with the current Hijri date (بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ on top, Hijri date below)
- **Four CTAs** — 🚀 Commencer · 📘 Exemples officiels · 🗺️ Parcours · 📚 Ressources
- **Theme-dependent decorative elements** — zellige tiles, stars, geometric patterns

## Top bar (always visible)

Left → right:
- 🛠️ **Brand badge** with pixel cat that animates on click
- 📊 **Progress indicator** — `X / 85 activités` (green dot when at 85)
- 🇫🇷 🇬🇧 🇩🇿 **Language flags** — click to switch instantly
- 🎲 **Random** — pick any activity
- 📖 **Aide** — opens help panel (pinout, cheatsheet, FAQ)
- 🗺️ **Parcours** — opens learning paths panel
- 📚 **Ressources** — opens resources/links panel
- 🔍 **Rechercher** — opens ⌘K command palette
- ⚙️ **Settings** — theme, sound, easter eggs list

## Sidebar (left)

Collapsible list of 9 categories with activity counts:

```
🌱 Démarrer (1)
📘 Officiel (15)
🚗 Mouvement (7)
💡 LEDs & son (8)
📡 Capteurs (8)
🎮 Interactivité (6)
🤖 Robotique (18)
🎯 Défis (10)
🧠 IA (12)
```

Each activity shows: `[#] Title  ★★☆`. Scroll-spy highlights the active activity as you scroll. Click to jump.

## Activity card (main area)

Each of the 85 activities is one vertical card with:

1. **Colored header bar** — category-color accent + big number badge
2. **Title** in current language
3. **Tag chips** — difficulty (★ stars + label), duration (⏱), OFFICIEL/V2/IA if applicable
4. **🎯 Objectif** — the pedagogical goal in ~2 sentences
5. **🧰 Matériel** — material pills (cards you can scan at a glance)
6. **📋 Étapes** — numbered step list
7. **💡 Astuce** — teacher's tip (yellow highlight box)
8. **🔀 Algorithme** — auto-generated flowchart (colored nodes: start/loop/decision/io/process/end)
9. **📝 Pseudo-code** — human-readable pseudo-code box
10. **💻 Code** — JavaScript and Python side-by-side with copy buttons and syntax highlighting
11. **🎯 Défis** — 1-3 challenge bullets (green=easy, yellow=medium, red=hard)
12. **✓ Marquer comme fait** — checkbox that persists to localStorage

## Panels (right side, slide-in)

### 🗺️ Parcours panel
6 curated learning paths:
- 🐣 Débutant (8-10 ans, ~2h, 10 activités)
- 🎓 Junior (10-12 ans, ~4h, 12 activités)
- 🚀 Ado (12-15 ans, ~8h, 12 activités)
- 🧠 IA (12+, ~6h, 10 activités)
- 🏆 Compétition (11+, ~5h, 8 activités)
- 🎨 Créatif (9+, ~5h, 8 activités)

Each card shows the activities in order with direct click-through.

### 📚 Ressources panel
21 curated links in 4 sections:
- 🔧 Outils en ligne (5) — MakeCode, Python Editor, CreateAI, Teachable Machine, Mind+
- 🧩 Extensions MakeCode (5) — pxt-maqueen, Plus v20, neopixel, Arduino lib, etc.
- 📘 Documentation officielle (6) — DFRobot wiki, micro:bit classroom, etc.
- 💬 Communauté & support (5) — MakeCode forum, DFRobot forum, etc.

Each item: icon, name, description, animated ↗ arrow on hover. Opens in new tab.

### 📖 Aide panel
Three tabs:

**📐 Matériel** — annotated SVG of the Maqueen Lite (one per language) with every port labeled in the active language. Below: a specs table with 11 rows.

**⚡ Antisèche** — 24 copy-paste code patterns organized into 9 sections:
- 🚗 Moteurs · 💡 LEDs avant · 🌈 LEDs RGB · 📡 Capteurs
- 🔧 Servo · 🎵 Son · 📻 Radio · 🎮 Interaction · 📺 Affichage

Each pattern shows: descriptive name, JavaScript code, Python code, explanatory note.

**🆘 FAQ** — 10 expandable entries for the most common classroom problems:
- Robot doesn't move, won't follow line, ultrasound gives nonsense, RGB LEDs off, radio pairing, IR remote, AI model fails, jerky motion, error codes, printing the guide…

### ⚙️ Settings panel
- **Thème** — 3×3 grid of colored swatches (Mosque, Zellige, Andalus, Space, Jungle, Robot, Riad, Medina, Retro if unlocked)
- **Son** — toggle for UI sound effects
- **Easter eggs** — hints about hidden features (Konami code, pixel pet, ⌘K)

## ⌘K / Ctrl+K command palette

Overlay modal with a fuzzy-search input. Type anything (activity title, category, keyword) and you get ranked results. Enter to jump.

## Themes preview

Each theme completely changes the color palette:
- **🕌 Mosque** — deep blue with gold accents (the default)
- **🎨 Zellige** — purple/teal on dark, zellige pattern accents
- **🏛️ Andalus** — emerald green on cream, Moorish elegance
- **🚀 Space** — black + purple + magenta gradients, starry feel
- **🌴 Jungle** — lime green + deep green, natural
- **🤖 Robot** — blue + steel gray, tech feel
- **🏠 Riad** — light cream + terracotta, reading-friendly
- **🕋 Medina** — light sand + teal, soft
- **🕹️ Retro** — CRT scanlines + phosphor green (unlocked by Konami code: ↑↑↓↓←→←→BA)

## Responsive layout

- **Desktop** (>1024px): sidebar left, activity content center, panels slide from right
- **Tablet** (768-1024px): sidebar collapsible, narrower content
- **Mobile** (<768px): sidebar becomes bottom drawer, top bar compact, panels full-screen
- **RTL** when Arabic is selected — entire layout flips left/right automatically

## Print

Ctrl+P / Cmd+P generates a clean print preview:
- All UI chrome removed (sidebar, panels, buttons)
- Each activity starts on a new page
- Colors simplified for readability on paper
- Flowcharts and code blocks kept legible
- Works for A4 portrait (and letter, landscape too, but A4 portrait is ideal)

Recommended: print the current language, or switch to your students' language before printing.
