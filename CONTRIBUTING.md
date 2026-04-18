# Contributing

Thanks for your interest in improving the Maqueen Lite Guide Terrain! This doc explains how to add activities, fix translations, report bugs, and propose new features.

## Quick start

```bash
git clone <your-fork-url>
cd maqueen-guide-terrain
./build.sh              # rebuild index.html from src/
open index.html         # macOS · or xdg-open on Linux, start on Windows
```

No dependencies to install. Requires Python 3.8+ (standard library only).

---

## Adding a new activity

Activities live in `src/build.py` (IDs 1-16), `src/phase2.py` (17-45), or `src/phase3.py` (46-85). Append to the appropriate `PHASE*` list.

**Template:**
```python
{
    'id': 86,  # next available number
    'cat': 'mouvement',  # one of: start, officiel, mouvement, leds, capteurs, interact, robot, defis, ia
    'stars': 2,  # 1 = beginner, 2 = intermediate, 3 = advanced
    'time': '20 min',
    'v2': False,  # True if requires micro:bit v2 (onboard mic, touch logo)
    'ai': False,  # True if uses AI (CreateAI or Teachable Machine)
    'official': False,  # True if reproduces a DFRobot wiki example
    'title_fr': "Ton titre",
    'title_en': "Your title",
    'title_ar': "عنوانك",
    'objectif_fr': "La description pédagogique en français…",
    'materiel': ['Maqueen Lite', 'MakeCode'],  # list of material pills
    'etapes_fr': [
        "Première étape",
        "Deuxième étape",
        "…",
    ],
    'tip_fr': "Le conseil du prof pour éviter les pièges courants.",
    'js': "// JavaScript code here",
    'py': "# Python code here",
    'defis_fr': [
        {'level': 'easy', 'text': "Un défi facile pour les plus rapides"},
        {'level': 'med',  'text': "Un défi intermédiaire"},
        {'level': 'hard', 'text': "Un défi pour aller plus loin"},
    ],
},
```

Then add the EN + AR translations to the corresponding translation file (`src/translations.py`, `src/translations_p2.py`, or `src/translations_p3.py`):

```python
86: {
    'en': {
        'objectif': "The pedagogical description in English…",
        'materiel': ['Maqueen Lite', 'MakeCode'],
        'etapes': ["First step", "Second step", "…"],
        'tip': "Teacher's tip to avoid common pitfalls.",
        'defis': [
            {'level': 'easy', 'text': "An easy bonus challenge"},
            {'level': 'med',  'text': "An intermediate challenge"},
            {'level': 'hard', 'text': "A stretch challenge"},
        ],
    },
    'ar': {
        'objectif': "…",
        'materiel': ['Maqueen Lite', 'MakeCode'],
        'etapes': ["…"],
        'tip': "…",
        'defis': [...],
    },
},
```

Then run `./build.sh` and verify the activity appears correctly in all 3 languages.

---

## Fixing a translation

1. Find the entry in `src/translations*.py` (by activity ID)
2. Edit the `'en'` or `'ar'` sub-dict
3. Run `./build.sh`
4. Open `index.html`, switch language via the 🇬🇧 or 🇩🇿 flag, verify

UI strings (buttons, labels) live in `src/i18n_module.py`.

Panel content (parcours, resources, help) lives in their respective modules:
- `src/phase4.py` for learning paths
- `src/assembler.py` for `RESOURCES` (external links)
- `src/help_module.py` for the pinout labels, cheatsheet, and FAQ

---

## Adding a learning path (parcours)

Append to `PARCOURS` in `src/phase4.py`:

```python
{
    'id': 'my_path',
    'icon': '🌟',
    'name_fr': 'Mon parcours',
    'name_en': 'My path',
    'name_ar': 'مساري',
    'desc_fr': "Description pédagogique…",
    'desc_en': "Pedagogical description…",
    'desc_ar': "…",
    'age_fr': '10+ ans', 'age_en': '10+ years', 'age_ar': '10+ سنة',
    'duration_fr': '~3h', 'duration_en': '~3h', 'duration_ar': '~3 ساعات',
    'activity_ids': [5, 12, 18, 24, 33],  # activity IDs in suggested order
},
```

---

## Adding a new theme

Edit `src/css_module.py`. Each theme is a CSS variable block:

```css
[data-theme="my-theme"] {
  --bg: #...;          /* background */
  --fg: #...;          /* foreground text */
  --panel: rgba(...);  /* sidebar / panel bg */
  --accent: #...;      /* primary accent */
  --accent2: #...;     /* secondary accent */
  /* … (see css_module.py for the full list of variables) */
}
```

Then register it in `src/js_module.py` in the `THEMES` array, and add a swatch in `render_theme_swatches()` in `src/assembler.py`.

---

## Reporting a bug

Open an [issue](https://github.com/YOUR_USERNAME/YOUR_REPO/issues/new) with:
- Browser + version
- Language / theme active when bug occurred
- Activity ID (if applicable)
- Screenshot if visual
- Expected vs actual behavior

---

## Pull request checklist

- [ ] `./build.sh` runs without errors
- [ ] `index.html` is committed (regenerated)
- [ ] Tested in at least 2 browsers (Chrome + Firefox recommended)
- [ ] Tested in all 3 languages if content was added
- [ ] Print preview (Ctrl+P) looks clean
- [ ] No new external dependencies added

---

## Code style

- **Python**: PEP 8-ish; we're loose on line length since most of the code is string templates
- **HTML**: generated; don't hand-edit `index.html`
- **CSS**: stay in `css_module.py`; use CSS variables defined in the `:root` / theme blocks
- **JavaScript**: stay in `js_module.py`; use `STATE` for mutable state, `localStorage` for persistence

---

## License

By contributing, you agree that your contributions will be released under the [MIT License](./LICENSE).
