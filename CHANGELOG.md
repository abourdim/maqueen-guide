# Changelog

All notable changes to this project are documented here.
Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), versioning follows [SemVer](https://semver.org).

## [1.0.1] — 2026-04-18

### 🐛 Fixed
- **Critical: corrected 68 code blocks across all 85 activities.** The v1.0.0 code used invalid `maqueen.showColor()` and `maqueen.clear()` calls that don't exist in the `pxt-maqueen` API. Code is now verified against the official [DFRobot pxt-maqueen source](https://github.com/DFRobot/pxt-maqueen) and matches the [Maqueen Lite wiki](https://wiki.dfrobot.com/rob0148-en/).
- **RGB LEDs** now use the correct pattern (requires the separate `neopixel` MakeCode extension):
  ```typescript
  let strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)
  strip.showColor(neopixel.colors(NeoPixelColors.Purple))
  strip.clear(); strip.show()
  ```
- **Ultrasonic**: removed bogus `PingUnit.Centimeters` argument — `maqueen.Ultrasonic()` takes no arguments and returns cm.
- **Line sensors**: cheatsheet now recommends `maqueen.readPatrol(maqueen.Patrol.PatrolLeft)` (the official API) over raw `pins.digitalReadPin(P13)`.
- **Front LEDs**: cheatsheet now recommends `maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOn)` — the documented API.
- **Servo**: cheatsheet now uses `maqueen.servoRun(maqueen.Servos.S1, angle)` instead of raw `pins.servoWritePin`.
- **FAQ entry "RGB LEDs don't light up"** now gives correct guidance (create strip, use `strip.showColor`).

### Verification
All 68 corrections verified by automated checks: the strings `maqueen.showColor`, `maqueen.clear()`, and `PingUnit.Centimeters` now appear **zero times** in the generated HTML. Tested against real MakeCode compilation.

---

## [1.0.0] — 2026-04-18

First public release.

### Added
- **85 activities** across 9 categories
- **15 official DFRobot examples** (IDs 1-16) from the ROB0148 wiki
- **70 creative extensions** (IDs 17-85) — motion, sensors, radio, AI, robotics, hacker challenges
- **6 curated learning paths**: Beginner, Junior, Teen, AI, Competition, Creative
- **Full trilingual content** — French / English / Modern Standard Arabic
- **9 themes** including Retro CRT (Konami-unlocked)
- **Help panel** with interactive pinout SVG, code cheatsheet (9 sections, 24 patterns), 10-entry FAQ
- **Resources panel** with 21 curated external links
- **⌘K / Ctrl+K** command palette with fuzzy search
- **🎲 Random** button for spontaneous activity discovery
- **Progress tracking** persisted in localStorage
- **Print CSS** for A4 classroom handouts
- **Responsive layout** with mobile drawer and automatic RTL for Arabic

### Technical
- Single HTML file, 1.2 MB, zero runtime dependencies
- Pure Python stdlib build
- Language switching via single CSS rule on 2,500+ `lang`-attributed blocks

### Credits
- Hardware: DFRobot Maqueen Lite (ROB0148)
- Platform: Microsoft MakeCode + micro:bit Educational Foundation
- AI: micro:bit CreateAI + Google Teachable Machine
- Sibling projects: [abourdim/bit-54-activities](https://github.com/abourdim/bit-54-activities), [abourdim/tools](https://github.com/abourdim/tools)
