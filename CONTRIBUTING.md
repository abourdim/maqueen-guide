# Contributing

Thanks for your interest in improving the Maqueen Lite Guide Terrain!

## Quick start

```bash
git clone https://github.com/abourdim/maqueen-activities.git
cd maqueen-activities
./build.sh              # rebuild index.html from src/
open index.html         # macOS · or xdg-open on Linux, start on Windows
```

No dependencies. Requires Python 3.8+ (standard library only).

---

## Adding an activity

Activities live in `src/build.py` (IDs 1-16), `src/phase2.py` (17-45), or `src/phase3.py` (46-85). Append to the appropriate `PHASE*` list with the template below, then add EN + AR translations to the corresponding `translations*.py` file.

### ⚠️ Use the verified API

All code must use the API documented in [DFRobot/pxt-maqueen](https://github.com/DFRobot/pxt-maqueen):

```javascript
// Motors
maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 150)
maqueen.motorStop(maqueen.Motors.All)

// Front LEDs (P8 left, P12 right)
maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOn)

// Line sensors
maqueen.readPatrol(maqueen.Patrol.PatrolLeft)   // returns 0 (white) or 1 (black)

// Ultrasonic — NO argument, returns cm
maqueen.Ultrasonic()

// Servo
maqueen.servoRun(maqueen.Servos.S1, 90)

// RGB LEDs — require the separate 'neopixel' extension
let strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)
strip.showColor(neopixel.colors(NeoPixelColors.Red))
strip.clear()
strip.show()
```

**Do NOT use** (these don't exist on the Maqueen namespace):
- ❌ `maqueen.showColor(...)` — use `strip.showColor(...)` after creating a neopixel strip
- ❌ `maqueen.clear()` — use `strip.clear(); strip.show()`
- ❌ `maqueen.Ultrasonic(PingUnit.Centimeters)` — no argument needed

**Best practice**: before committing, paste your `js` code into [MakeCode](https://makecode.microbit.org) with the `maqueen` and `neopixel` extensions loaded. If it compiles without red underlines, ship it.

### Activity template

```python
{
    'id': 86,  # next available number
    'cat': 'mouvement',  # start, officiel, mouvement, leds, capteurs, interact, robot, defis, ia
    'stars': 2,  # 1=beginner, 2=intermediate, 3=advanced
    'time': '20 min',
    'v2': False,  # True if requires micro:bit v2
    'ai': False,  # True if uses AI (CreateAI or Teachable Machine)
    'official': False,  # True if reproduces a DFRobot wiki example
    'title_fr': "Ton titre",
    'title_en': "Your title",
    'title_ar': "عنوانك",
    'objectif_fr': "La description pédagogique…",
    'materiel': ['Maqueen Lite', 'MakeCode'],
    'etapes_fr': ["Première étape", "Deuxième étape"],
    'tip_fr': "Le conseil du prof.",
    'js': "// TypeScript code using verified API",
    'py': "# Python equivalent",
    'defis_fr': [
        {'level': 'easy', 'text': "Défi facile"},
        {'level': 'med',  'text': "Défi intermédiaire"},
        {'level': 'hard', 'text': "Défi avancé"},
    ],
},
```

Then add EN + AR translations to the corresponding `translations*.py` file:

```python
86: {
    'en': {
        'objectif': "...",
        'materiel': ['Maqueen Lite', 'MakeCode'],
        'etapes': [...],
        'tip': "...",
        'defis': [...],
    },
    'ar': {
        'objectif': "...",
        'materiel': [...],
        'etapes': [...],
        'tip': "...",
        'defis': [...],
    },
},
```

---

## Fixing a translation

1. Find the entry in `src/translations*.py` (by activity ID) or `src/i18n_module.py` (for UI strings)
2. Edit the `'en'` or `'ar'` sub-dict
3. `./build.sh`
4. Open `index.html`, switch via flag, verify

---

## Adding a learning path

Append to `PARCOURS` in `src/phase4.py` with trilingual `name`, `desc`, `age`, `duration`.

---

## Reporting a bug

Open an [issue](https://github.com/abourdim/maqueen-activities/issues/new) with:
- Browser + version
- Language / theme active
- Activity ID (if applicable)
- Screenshot if visual
- Expected vs actual behavior
- For code bugs: paste the MakeCode error

---

## PR checklist

- [ ] `./build.sh` runs without errors
- [ ] `index.html` is committed (regenerated)
- [ ] Code compiles in MakeCode with the right extensions loaded
- [ ] Tested in at least 2 browsers
- [ ] Tested in all 3 languages if content was added
- [ ] Print preview (Ctrl+P) looks clean
- [ ] No new external dependencies

---

## License

By contributing, you agree that your contributions will be released under the [MIT License](./LICENSE).
