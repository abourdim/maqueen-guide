# Maqueen Lite · Guide Terrain

[![GitHub Pages](https://img.shields.io/badge/GitHub-Pages-222?logo=github)](https://pages.github.com)
[![Single HTML](https://img.shields.io/badge/Single-HTML-e34c26?logo=html5&logoColor=white)](./index.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Trilingual](https://img.shields.io/badge/🇫🇷_🇬🇧_🇩🇿-FR_·_EN_·_AR-5865F2)](#languages)

> **A complete field guide for the DFRobot Maqueen Lite (ROB0148) micro:bit robot — 85 activities in French, English and Arabic, packed in a single 1.2 MB HTML file with zero dependencies.**

🇫🇷 **Français** · 🇬🇧 **English** · 🇩🇿 **العربية** (fuṣḥā · MSA)

---

## 🚀 Demo

Open [`index.html`](./index.html) in any modern browser — no build, no server, no dependencies required. Works offline.

For GitHub Pages hosting, just enable Pages on this repo and point to the root folder. The file will serve at `https://<user>.github.io/<repo>/`.

---

## ✨ Features

### 📚 Content
- **85 activities** spread across 9 categories (Démarrer, Officiel, Mouvement, LEDs & Son, Capteurs, Interactivité, Robotique, Défis, IA)
- **15 official DFRobot examples** faithfully reproduced from the [wiki ROB0148](https://wiki.dfrobot.com/rob0148-en/)
- **70 creative extensions** — from first LED blink to autonomous swarm behavior and Q-learning
- **6 curated learning paths** — Beginner (8-10 y/o), Junior, Teen, AI, Competition, Creative
- **21 curated external links** — MakeCode, CreateAI, Teachable Machine, extensions, forums
- **24 code cheatsheet patterns** — copy-paste-ready for motors, LEDs, sensors, radio, AI
- **10 troubleshooting FAQ entries** for common classroom problems

### 🌍 Trilingual
Every visible string in every panel is available in:
- 🇫🇷 **French** (default)
- 🇬🇧 **English**
- 🇩🇿 **Modern Standard Arabic** (الفصحى / العربية الأدبية), with automatic RTL layout

Language switching is instant: one CSS rule swaps visibility across 2,500+ `lang`-attributed blocks.

### 🎨 Interface
- **9 themes** — Mosque, Zellige, Andalus, Space, Jungle, Robot, Riad (light), Medina (light), Retro CRT (unlocked via Konami code)
- **⌘K / Ctrl+K** command palette with fuzzy search
- **Scroll-spy sidebar** with progress tracking (X/85 persisted in localStorage)
- **Print CSS** optimized for A4 classroom handouts
- **Responsive** — sidebar becomes drawer on mobile, Arabic flips RTL automatically
- **Pixel pet 🐱** easter egg, per-theme melodies, splash screen with bismillah

### 🧠 Per-activity sections
Each activity card contains:
- 🎯 Objective · 🧰 Materials (pills) · 📋 Numbered steps
- 💡 Teaching tip · 🔀 Auto-generated flowchart (colored nodes)
- 📝 Pseudo-code box · 💻 JavaScript + Python code side-by-side with syntax highlighting and copy buttons
- 🚀 Graduated challenges (easy/medium/hard color-coded dots)
- ✓ Mark-as-done button (progress tracking)

---

## 📂 Structure

```
.
├── index.html              # The guide itself — ready to use, 1.2 MB
├── src/                    # Python source modules that build index.html
│   ├── assembler.py        # Main builder — emits the HTML
│   ├── build.py            # Phase 1 activities (1-16): Getting Started + 15 Official
│   ├── phase2.py           # Phase 2 activities (17-45): Movement, LEDs, Sensors, Interactivity
│   ├── phase3.py           # Phase 3 activities (46-85): Robotics, Communication, Challenges, AI
│   ├── phase4.py           # Learning paths (parcours)
│   ├── translations.py     # EN + AR translations for activities 1-16
│   ├── translations_p2.py  # EN + AR translations for activities 17-45
│   ├── translations_p3.py  # EN + AR translations for activities 46-85
│   ├── i18n_module.py      # UI strings (FR/EN/AR) + flag URLs
│   ├── css_module.py       # All CSS (themes, layout, print)
│   ├── js_module.py        # All runtime JS (state, nav, themes, ⌘K, progress)
│   └── help_module.py      # Pinout SVG + cheatsheet + FAQ (trilingual)
├── docs/
│   ├── SCREENSHOTS.md      # Visual guide
│   └── ARCHITECTURE.md     # How the build works
├── build.sh                # One-line build script
├── LICENSE                 # MIT
├── CONTRIBUTING.md         # How to add activities / translations
├── CHANGELOG.md
└── README.md               # You are here
```

---

## 🛠️ Rebuilding from source

```bash
# Requirements: Python 3.8+ (no external packages needed)
./build.sh

# Or manually:
cd src && python3 assembler.py
# → writes maqueen-guide.html to current dir
# → move/rename to ../index.html for GitHub Pages
```

The build is entirely stdlib — no npm, no pip, no build toolchain. Everything is pure Python string templating.

---

## 🏗️ Hardware

- [**DFRobot Maqueen Lite (ROB0148)**](https://www.dfrobot.com/product-1783.html) — micro:bit-based educational robot, age 8+
- **micro:bit v1 or v2** (v2 required for AI activities — needs onboard mic)
- **3× AAA batteries** (or 3.7V Li-ion)
- Optional: ultrasonic sensor (SR04), servo motor, IR remote

Pin reference:
| Component | Pin | Type |
|---|---|---|
| Front LED left | P8 | Digital ON/OFF |
| Front LED right | P12 | Digital ON/OFF |
| Line sensor left | P13 | Digital 0/1 |
| Line sensor right | P14 | Digital 0/1 |
| RGB NeoPixels (×4) | P15 | NeoPixel bus |
| IR receiver | P16 | NEC protocol |
| Servo S1 | P1 | PWM |
| Servo S2 | P2 | PWM |

---

## 🎓 Classroom usage

### For teachers
- **Ctrl+P / Cmd+P** generates a print-ready A4 handout — the print CSS strips sidebar and panels
- Browse by **📘 Official** category for the exact DFRobot wiki examples
- Use **🗺️ Parcours** (learning paths) to follow a curated sequence matching your students' age
- The **🆘 FAQ** panel has the 10 most-common classroom issues and how to fix them in 30 seconds
- Progress is saved locally in the browser (no server, no account)

### For students
- Every activity has **Blocks → JavaScript → Python** progression
- Copy button on every code block — paste directly into [MakeCode](https://makecode.microbit.org)
- Challenges (🎯 green/yellow/red) let self-directed learners push further
- The **🎲 Random** button picks any activity for spontaneous discovery

### Recommended progression
```
debutant (🐣 8-10) → junior (🎓 10-12) → ado (🚀 12-15)
                                              ↓
                             ia (🧠) · competition (🏆) · creatif (🎨)
```

---

## 📦 Dependencies

**Runtime** (loaded by `index.html`):
- `fonts.googleapis.com` — Amiri + Tajawal (Arabic typography)
- `flagcdn.com` — 🇫🇷 🇬🇧 🇩🇿 flag images (40px width)

**Build** (to regenerate from source):
- Python 3.8+ standard library only

**No npm, no webpack, no bundler.** The entire guide is one file.

---

## 🙏 Credits & attribution

- **Hardware**: [DFRobot](https://www.dfrobot.com) — Maqueen Lite (ROB0148) and `pxt-maqueen` extension
- **Platform**: [Microsoft MakeCode](https://makecode.microbit.org) and [micro:bit Educational Foundation](https://microbit.org)
- **AI tools**: [micro:bit CreateAI](https://createai.microbit.org) and [Google Teachable Machine](https://teachablemachine.withgoogle.com)
- **Design inspiration**: [abourdim/bit-54-activities](https://github.com/abourdim/bit-54-activities) — the trilingual structure and pedagogical flow of each activity card follows this excellent guide
- **Workshop-DIY Toolkit**: [abourdim/tools](https://github.com/abourdim/tools) — shared theme system and visual language

---

## 📄 License

This project is released under the [MIT License](./LICENSE).

Code examples based on the DFRobot wiki (Activities 1-16) remain under their original licensing. All creative extensions and translations (Activities 17-85, 6 learning paths, help content) are original contributions.

---

## 🤝 Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for how to add activities, fix translations, or propose new learning paths.

Issues and pull requests welcome! 🎉
