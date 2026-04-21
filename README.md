# Maqueen Lite · Guide Terrain

[![GitHub Pages](https://img.shields.io/badge/GitHub-Pages-222?logo=github)](https://abourdim.github.io/maqueen-activities/)
[![Single HTML](https://img.shields.io/badge/Single-HTML-e34c26?logo=html5&logoColor=white)](./index.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.1-blue.svg)](./CHANGELOG.md)
[![Trilingual](https://img.shields.io/badge/🇫🇷_🇬🇧_🇩🇿-FR_·_EN_·_AR-5865F2)](#languages)

> **A complete field guide for the DFRobot Maqueen Lite (ROB0148) micro:bit robot — 85 activities in French, English and Arabic, packed in a single 1.2 MB HTML file with zero dependencies.**

🇫🇷 **Français** · 🇬🇧 **English** · 🇩🇿 **العربية** (fuṣḥā · MSA)

**🌐 Live demo:** [abourdim.github.io/maqueen-activities](https://abourdim.github.io/maqueen-activities/)

---

## 🚀 Quick start

Open [`index.html`](./index.html) in any modern browser — no build, no server, no dependencies. Works offline.

---

## ✨ Features

### 📚 Content
- **85 activities** spread across 9 categories (Démarrer, Officiel, Mouvement, LEDs & Son, Capteurs, Interactivité, Robotique, Défis, IA)
- **15 official DFRobot examples** (IDs 1-16) faithfully reproduced from the [wiki ROB0148](https://wiki.dfrobot.com/rob0148-en/)
- **70 creative extensions** — from first LED blink to autonomous swarm behavior and Q-learning
- **6 curated learning paths** — Beginner (8-10 y/o), Junior, Teen, AI, Competition, Creative
- **21 curated external links** — MakeCode, CreateAI, Teachable Machine, extensions, forums
- **24 code cheatsheet patterns** — copy-paste-ready for motors, LEDs, sensors, radio, AI
- **10 troubleshooting FAQ entries** for common classroom problems

### 🌍 Trilingual
Every visible string in every panel is available in:
- 🇫🇷 **French** (default)
- 🇬🇧 **English**
- 🇩🇿 **Modern Standard Arabic** (الفصحى), with automatic RTL layout

Language switching is instant: one CSS rule swaps visibility across 2,500+ `lang`-attributed blocks.

### 🎨 Interface
- **9 themes** — Mosque, Zellige, Andalus, Space, Jungle, Robot, Riad, Medina, Retro CRT (unlocked via Konami code)
- **⌘K / Ctrl+K** command palette with fuzzy search
- **Scroll-spy sidebar** with progress tracking (X/85 persisted in localStorage)
- **Print CSS** optimized for A4 classroom handouts
- **Responsive** — sidebar becomes drawer on mobile, Arabic flips RTL automatically

### 🧠 Per-activity sections
Each activity card contains:
- 🎯 Objective · 🧰 Materials · 📋 Numbered steps
- 💡 Teaching tip · 🔀 Auto-generated flowchart
- 📝 Pseudo-code box · 💻 JavaScript + Python code (copy buttons)
- 🚀 Graduated challenges (easy/medium/hard)
- ✓ Mark-as-done button with persistent progress

---

## 🛠️ Code conventions (MakeCode + pxt-maqueen)

All code examples use the **actual working API** verified against [DFRobot/pxt-maqueen](https://github.com/DFRobot/pxt-maqueen):

**Motors** (`maqueen` namespace):
```javascript
maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 150)
maqueen.motorStop(maqueen.Motors.All)
```

**Front LEDs** (P8 left, P12 right):
```javascript
maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOn)
```

**RGB ambient LEDs** (require the separate `neopixel` extension):
```javascript
let strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)
strip.showColor(neopixel.colors(NeoPixelColors.Purple))
strip.clear(); strip.show()
```

**Line sensors**:
```javascript
let left = maqueen.readPatrol(maqueen.Patrol.PatrolLeft)   // 0 = white, 1 = black
```

**Ultrasonic** (SR04 in the Maqueen port):
```javascript
let distance = maqueen.Ultrasonic()   // centimeters, no argument
```

**Servos**:
```javascript
maqueen.servoRun(maqueen.Servos.S1, 90)   // angle 0-180°
```

---

## 🏗️ Hardware

- [**DFRobot Maqueen Lite (ROB0148)**](https://www.dfrobot.com/product-1783.html) — micro:bit-based educational robot, age 8+
- **micro:bit v1 or v2** (v2 required for AI activities — needs onboard mic)
- **3× AAA batteries** (or 3.7V Li-ion)
- Optional: ultrasonic sensor (SR04), servo motor, IR remote

Pin reference:
| Component | Pin | Access |
|---|---|---|
| Front LED left | P8 | `maqueen.writeLED(maqueen.LED.LEDLeft, ...)` |
| Front LED right | P12 | `maqueen.writeLED(maqueen.LED.LEDRight, ...)` |
| Line sensor left | P13 | `maqueen.readPatrol(maqueen.Patrol.PatrolLeft)` |
| Line sensor right | P14 | `maqueen.readPatrol(maqueen.Patrol.PatrolRight)` |
| RGB NeoPixels (×4) | P15 | via `neopixel` extension |
| IR receiver | P16 | `maqueen.IR_Read(IR_Pin.P16)` |
| Servo S1 | P1 | `maqueen.servoRun(maqueen.Servos.S1, ...)` |
| Servo S2 | P2 | `maqueen.servoRun(maqueen.Servos.S2, ...)` |

Required MakeCode extensions: **maqueen** + **neopixel** (for RGB).

---

## 📂 Structure

```
.
├── index.html              # The guide itself — ready to use, 1.22 MB
├── src/                    # Python source modules that build index.html
│   ├── assembler.py        # Main builder
│   ├── build.py            # Phase 1 activities (1-16): official
│   ├── phase2.py           # Phase 2 activities (17-45)
│   ├── phase3.py           # Phase 3 activities (46-85)
│   ├── phase4.py           # Learning paths
│   ├── translations.py     # EN + AR translations (1-16)
│   ├── translations_p2.py  # EN + AR translations (17-45)
│   ├── translations_p3.py  # EN + AR translations (46-85)
│   ├── i18n_module.py      # UI strings
│   ├── css_module.py       # All CSS (themes, layout, print)
│   ├── js_module.py        # Runtime JS
│   └── help_module.py      # Pinout SVG + cheatsheet + FAQ
├── docs/
│   ├── SCREENSHOTS.md      # Visual guide
│   └── ARCHITECTURE.md     # How the build works
├── build.sh                # One-line rebuild
├── LICENSE                 # MIT
├── CHANGELOG.md            # Version history
├── CONTRIBUTING.md         # How to add activities
├── .github/workflows/      # Auto-build + deploy on push
│   └── build.yml
└── README.md               # You are here
```

---

## 🛠️ Rebuilding from source

```bash
# Requirements: Python 3.8+ (no external packages needed)
./build.sh
```

The build is pure Python stdlib — no npm, no pip, no toolchain.

---

## 🎓 Classroom usage

- **Ctrl+P / Cmd+P** generates a clean print-ready A4 handout
- Browse by **📘 Official** category for exact DFRobot wiki examples
- Use **🗺️ Parcours** to follow a curated sequence matching student age
- **🆘 FAQ** panel has the 10 most-common classroom issues
- Progress saved locally in the browser (no server, no account needed)

---

## 🙏 Credits

- **Hardware**: [DFRobot](https://www.dfrobot.com) — Maqueen Lite (ROB0148) and [`pxt-maqueen`](https://github.com/DFRobot/pxt-maqueen)
- **Platform**: [Microsoft MakeCode](https://makecode.microbit.org) and [micro:bit Educational Foundation](https://microbit.org)
- **AI tools**: [micro:bit CreateAI](https://createai.microbit.org) and [Google Teachable Machine](https://teachablemachine.withgoogle.com)
- **Sibling projects**: [bit-54-activities](https://github.com/abourdim/bit-54-activities) and [Workshop-DIY Toolkit](https://github.com/abourdim/tools) — same author, complementary guides

---

## 📄 License

MIT — see [LICENSE](./LICENSE). Code examples based on the DFRobot wiki (Activities 1-16) remain under their original licensing.

---

## 🤝 Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md). Issues and pull requests welcome! 🎉
