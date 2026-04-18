# Changelog

All notable changes to this project are documented here.
Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), versioning follows [SemVer](https://semver.org).

## [1.0.0] — 2026-04-18

First public release.

### Added
- **85 activities** across 9 categories (Démarrer, Officiel, Mouvement, LEDs, Capteurs, Interactivité, Robotique, Défis, IA)
- **15 official DFRobot examples** (IDs 1-16) reproduced from the ROB0148 wiki
- **70 creative extensions** (IDs 17-85) covering motion, sensors, radio, AI, robotics, and hacker challenges
- **6 curated learning paths** (parcours): Beginner, Junior, Teen, AI, Competition, Creative
- **Full trilingual content** — French / English / Modern Standard Arabic, for every activity and every panel
- **9 themes** — Mosque, Zellige, Andalus, Space, Jungle, Robot, Riad, Medina, Retro (hidden, unlocked by Konami code)
- **Help panel** with interactive pinout SVG (one per language), code cheatsheet (9 sections, 24 patterns), and 10-entry troubleshooting FAQ
- **Resources panel** with 21 curated external links (MakeCode, CreateAI, extensions, forums, documentation)
- **⌘K / Ctrl+K** command palette with fuzzy search across all 85 activities
- **🎲 Random** button for spontaneous activity discovery
- **Progress tracking** — X/85 completion persisted in localStorage
- **Print CSS** optimized for A4 classroom handouts
- **Responsive layout** with mobile drawer and automatic RTL for Arabic
- **Konami code easter egg** unlocks CRT-Retro theme; pixel-pet and bismillah splash

### Technical
- Single HTML file, 1.2 MB, zero runtime dependencies (only Google Fonts + flagcdn for typography/flags)
- Pure Python stdlib build (no npm, no bundler)
- Language switching via single CSS rule on 2,500+ `lang`-attributed blocks — no JS re-rendering
- HTML balanced, JS parses clean, all Arabic UTF-8 intact

### Credits
- Hardware: DFRobot Maqueen Lite (ROB0148)
- Platform: Microsoft MakeCode + micro:bit Educational Foundation
- AI: micro:bit CreateAI + Google Teachable Machine
- Design inspiration: [abourdim/bit-54-activities](https://github.com/abourdim/bit-54-activities) and [abourdim/tools](https://github.com/abourdim/tools)
