# Visual tour

What you'll see when you open `index.html`.

> 💡 This guide is a single HTML file — open it in any browser to see everything live. This doc describes visuals in prose since screenshots would go stale with every update.

## Cover page

On first load, a splash with:
- **Big title** "Maqueen Lite · Guide Terrain" with bismillah + Hijri date
- **Four CTAs**: 🚀 Commencer · 📘 Exemples officiels · 🗺️ Parcours · 📚 Ressources
- Theme-dependent decorative elements (zellige tiles, stars, geometric patterns)

## Top bar

Left → right:
- 🛠️ Brand badge with pixel cat
- 📊 Progress `X / 85 activités` (green dot when complete)
- 🇫🇷 🇬🇧 🇩🇿 Language flags
- 🎲 Random activity
- 📖 Aide (help panel)
- 🗺️ Parcours
- 📚 Ressources
- 🔍 Search (⌘K)
- ⚙️ Settings

## Sidebar

Collapsible list of 9 categories with counts:
```
🌱 Démarrer (1)     📘 Officiel (15)    🚗 Mouvement (7)
💡 LEDs & son (8)   📡 Capteurs (8)     🎮 Interactivité (6)
🤖 Robotique (18)   🎯 Défis (10)       🧠 IA (12)
```

Each activity: `[#] Title  ★★☆`. Scroll-spy highlights the active activity.

## Activity card

Every activity has:
1. Colored header bar (category color) + number badge
2. Trilingual title
3. Tag chips: difficulty, duration, OFFICIEL/V2/IA badges
4. 🎯 Objectif
5. 🧰 Matériel pills
6. 📋 Étapes numbered list
7. 💡 Astuce (yellow tip box)
8. 🔀 Auto-generated flowchart (colored nodes)
9. 📝 Pseudo-code
10. 💻 JavaScript + Python side-by-side with copy buttons
11. 🎯 Défis (green/yellow/red challenges)
12. ✓ Marquer comme fait checkbox

## Panels

### 🗺️ Parcours — 6 curated learning paths
- 🐣 Débutant (8-10 ans, ~2h, 10 activités)
- 🎓 Junior (10-12 ans, ~4h, 12 activités)
- 🚀 Ado (12-15 ans, ~8h, 12 activités)
- 🧠 IA (12+, ~6h, 10 activités)
- 🏆 Compétition (11+, ~5h, 8 activités)
- 🎨 Créatif (9+, ~5h, 8 activités)

### 📚 Ressources — 21 curated links in 4 sections
- 🔧 Outils en ligne (5) — MakeCode, Python Editor, CreateAI, Teachable Machine, Mind+
- 🧩 Extensions MakeCode (5) — pxt-maqueen, Plus v20, neopixel, etc.
- 📘 Documentation officielle (6) — DFRobot wiki, micro:bit classroom, etc.
- 💬 Communauté & support (5) — MakeCode forum, DFRobot forum, etc.

### 📖 Aide — 3 tabs
**📐 Matériel** — Annotated SVG pinout (one per language) + 11-row specs table

**⚡ Antisèche** — 9 sections, 24 verified code patterns:
- 🚗 Moteurs (motorRun, motorStop, pivot, stop)
- 💡 LEDs avant (writeLED)
- 🌈 LEDs RGB (strip setup + showColor + clear + setPixelColor)
- 📡 Capteurs (readPatrol, Ultrasonic, lightLevel)
- 🔧 Servo (servoRun)
- 🎵 Son (playTone, builtInMelody)
- 📻 Radio (setGroup, send, receive)
- 🎮 Interaction (onButtonPressed, onGesture)
- 📺 Affichage (showString, showNumber, showIcon, clearScreen)

**🆘 FAQ** — 10 expandable entries for common classroom problems

### ⚙️ Settings
- **Thème** — 9 swatches (+1 Retro unlocked via Konami)
- **Son** — toggle for UI effects
- **Easter eggs** — hints about hidden features

## ⌘K / Ctrl+K command palette

Overlay modal with fuzzy search across all activities. Enter to jump.

## Themes

- **🕌 Mosque** — deep blue + gold (default)
- **🎨 Zellige** — purple/teal on dark
- **🏛️ Andalus** — emerald green on cream
- **🚀 Space** — black + purple + magenta gradients
- **🌴 Jungle** — lime + deep green
- **🤖 Robot** — blue + steel gray
- **🏠 Riad** — light cream + terracotta
- **🕋 Medina** — light sand + teal
- **🕹️ Retro** — CRT scanlines + phosphor (Konami-locked)

## Responsive

- **Desktop** (>1024px): sidebar left, content center, panels slide right
- **Tablet** (768-1024px): sidebar collapsible
- **Mobile** (<768px): sidebar → bottom drawer, compact topbar
- **RTL** auto-flips when Arabic is selected

## Print

Ctrl+P / Cmd+P generates clean A4 output:
- UI chrome removed
- Each activity starts on a new page
- Print-friendly colors
- Code blocks remain legible
