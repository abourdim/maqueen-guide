#!/usr/bin/env python3
"""
Maqueen Lite · Guide terrain — Main HTML builder
Outputs single-file HTML (bit-58-inspired).
"""
import json, pathlib, html, sys, os, re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import ACTIVITIES as PHASE1_ACTIVITIES, CATS
from phase2 import PHASE2
from phase3 import PHASE3
from phase4 import PARCOURS
from help_module import PINOUT_SVG, CHEATSHEET_SECTIONS, FAQ
from translations import TRANSLATIONS as T1
from translations_p2 import TRANSLATIONS_P2 as T2
from translations_p3 import TRANSLATIONS_P3 as T3
from css_module import CSS
from js_module import js_template
from i18n_module import I18N, FLAGS

# Merge all translations
ALL_TRANSLATIONS = {**T1, **T2, **T3}
print(f"Merged translations: {len(ALL_TRANSLATIONS)} activities (EN + AR)")

# Combine all activities
ACTIVITIES = PHASE1_ACTIVITIES + PHASE2 + PHASE3
print(f"Total activities loaded: {len(ACTIVITIES)} (Phase 1: {len(PHASE1_ACTIVITIES)}, Phase 2: {len(PHASE2)}, Phase 3: {len(PHASE3)})")

# ═══════════════════════════════════════════════════════════════
#   HELPERS
# ═══════════════════════════════════════════════════════════════

def escape(s):
    return html.escape(s, quote=False) if s else ''

def highlight_js(code):
    """Very light JS highlighter — replaces keywords/strings/comments with spans."""
    # Split into tokens carefully. Using regex on code safely.
    code = html.escape(code, quote=False)
    # Comments first (// to end of line)
    code = re.sub(r'(//[^\n]*)', r'<span class="hl-cmt">\1</span>', code)
    # Strings (double quotes, only within non-comment lines — naive but OK)
    code = re.sub(r'(&quot;[^&]*?&quot;)', r'<span class="hl-str">\1</span>', code)
    # Numbers
    code = re.sub(r'\b(\d+(?:\.\d+)?)\b', r'<span class="hl-num">\1</span>', code)
    # Keywords
    keywords = ['let','var','const','function','if','else','for','while','return','true','false']
    for kw in keywords:
        code = re.sub(r'\b(' + kw + r')\b', r'<span class="hl-kw">\1</span>', code)
    return code

def highlight_py(code):
    """Light Python highlighter."""
    code = html.escape(code, quote=False)
    # Comments (# to end of line)
    code = re.sub(r'(#[^\n]*)', r'<span class="hl-cmt">\1</span>', code)
    # Strings
    code = re.sub(r'(&quot;[^&]*?&quot;)', r'<span class="hl-str">\1</span>', code)
    # Numbers
    code = re.sub(r'\b(\d+(?:\.\d+)?)\b', r'<span class="hl-num">\1</span>', code)
    # Keywords
    keywords = ['def','if','elif','else','for','while','return','True','False','None','import','from','global','and','or','not','in','is','lambda','with']
    for kw in keywords:
        code = re.sub(r'\b(' + kw + r')\b', r'<span class="hl-kw">\1</span>', code)
    return code

# ═══════════════════════════════════════════════════════════════
#   FLOWCHART GENERATION
# ═══════════════════════════════════════════════════════════════

def gen_flowchart(steps, start_label='DÉBUT', end_label='FIN'):
    """Generate a simple flowchart from step descriptions.
    Heuristic: first step = start, steps with 'répéter'/'boucle' = loop,
    steps with 'si'/'if' = decision, last = end."""
    nodes = [('start', start_label)]
    for step in steps:
        s = step.lower()
        if 'répéter' in s or 'boucle' in s or 'en boucle' in s or 'repeat' in s or 'loop' in s or 'كرر' in s or 'حلقة' in s:
            nodes.append(('loop', step[:40]))
        elif s.startswith('si ') or 'si ' in s[:5] or s.startswith('if ') or s.startswith('إذا'):
            nodes.append(('decision', step[:40]))
        elif 'lire' in s[:8] or 'afficher' in s[:10] or 'read' in s[:8] or 'display' in s[:10] or 'show' in s[:6] or 'اقرأ' in s[:8] or 'اعرض' in s[:8]:
            nodes.append(('io', step[:40]))
        else:
            nodes.append(('process', step[:40]))
    nodes.append(('end', end_label))
    parts = []
    for i, (t, txt) in enumerate(nodes):
        parts.append(f'<div class="fc-node {t}">{escape(txt)}</div>')
        if i < len(nodes) - 1:
            parts.append('<div class="fc-arrow"></div>')
    return '<div class="flowchart">' + ''.join(parts) + '</div>'

def gen_pseudocode(steps, start_label='DÉBUT', end_label='FIN'):
    """Very simple pseudocode."""
    lines = [f'<span class="pk">{start_label}</span>']
    for s in steps:
        txt = escape(s)
        lines.append(f'  {txt}')
    lines.append(f'<span class="pk">{end_label}</span>')
    return '<div class="pseudo-box">' + '\n'.join(lines) + '</div>'

def gen_led_preview():
    """A small micro:bit LED preview, lighting the center + corners."""
    led_positions = [(1,1),(3,1),(0,2),(1,2),(2,2),(3,2),(4,2),(1,3),(2,3),(3,3),(2,4)]
    circles = []
    for y in range(5):
        for x in range(5):
            is_on = (x, y) in led_positions
            if is_on:
                circles.append(f'<circle cx="{12+x*18}" cy="{12+y*18}" r="7" fill="#ff1a1a" filter="url(#ledglow)"/>')
            else:
                circles.append(f'<circle cx="{12+x*18}" cy="{12+y*18}" r="7" fill="#1a1a2e" opacity="0.3"/>')
    return f'''<svg class="led-svg" width="96" height="96" viewBox="0 0 96 96" xmlns="http://www.w3.org/2000/svg">
<defs><filter id="ledglow"><feGaussianBlur stdDeviation="2" result="g"/><feMerge><feMergeNode in="g"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>
<rect width="96" height="96" rx="8" fill="#050510"/>
{''.join(circles)}
</svg>'''

# ═══════════════════════════════════════════════════════════════
#   ACTIVITY CARD RENDERER
# ═══════════════════════════════════════════════════════════════

# Pseudo-code and flowchart labels per language
PSEUDO_LABELS = {
    'fr': {'start': 'DÉBUT', 'end': 'FIN'},
    'en': {'start': 'START', 'end': 'END'},
    'ar': {'start': 'البداية', 'end': 'النهاية'},
}

# Difficulty labels per language
DIFF_LABELS = {
    'fr': {1:'Débutant', 2:'Intermédiaire', 3:'Avancé'},
    'en': {1:'Beginner', 2:'Intermediate', 3:'Advanced'},
    'ar': {1:'مبتدئ', 2:'متوسط', 3:'متقدم'},
}

def get_field(act, field, lang):
    """Get a translated field, falling back to FR if missing."""
    if lang == 'fr':
        return act.get(f'{field}_fr', act.get(field, ''))
    t = ALL_TRANSLATIONS.get(act['id'], {}).get(lang, {})
    return t.get(field, act.get(f'{field}_fr', act.get(field, '')))

def render_activity(act):
    cat = next(c for c in CATS if c['id'] == act['cat'])
    hdr_color = cat['color']

    # Stars
    stars_html = '<span class="tag-stars">' + '★' * act['stars'] + '☆' * (3 - act['stars']) + '</span>'
    diff_color = {1:'#40BF4A', 2:'#eab308', 3:'#DC143C'}[act['stars']]

    # Render difficulty labels per language
    diff_chips = ''.join(
        f'<span class="tag-chip diff" style="--dc:{diff_color}" lang="{lang}">{stars_html} {DIFF_LABELS[lang][act["stars"]]}</span>'
        for lang in ('fr', 'en', 'ar')
    )

    # Official badge
    official_badge = ''
    wiki_link = ''
    if act.get('official'):
        official_badge = '<span class="tag-chip official">📘 OFFICIEL</span>'
        if act.get('wiki'):
            wiki_link = f'<a class="act-wiki-link" href="{act["wiki"]}" target="_blank" rel="noopener" data-i18n="wiki_link">Voir sur le wiki DFRobot ↗</a>'

    # v2/ai chips
    v2_chip = '<span class="tag-chip v2">V2</span>' if act.get('v2') else ''
    ai_chip = '<span class="tag-chip ai">🧠 IA</span>' if act.get('ai') else ''

    # Titles per language (all 3)
    title_blocks = ''.join(
        f'<div class="act-title-text" lang="{lang}">{escape(act.get(f"title_{lang}", act.get("title_fr", "")))}</div>'
        for lang in ('fr', 'en', 'ar')
    )

    # Objectif per language
    objectif_blocks = ''.join(
        f'<div class="goal-text" lang="{lang}">{escape(get_field(act, "objectif", lang))}</div>'
        for lang in ('fr', 'en', 'ar')
    )

    # Materiel pills per language
    materiel_blocks_list = []
    for lang in ('fr', 'en', 'ar'):
        materiel = get_field(act, 'materiel', lang) if lang != 'fr' else act.get('materiel', [])
        if not materiel:  # fallback
            materiel = act.get('materiel', [])
        pills = ''.join(f'<span class="need-pill">{escape(m)}</span>' for m in materiel)
        materiel_blocks_list.append(f'<div class="needs-wrap" lang="{lang}">{pills}</div>')
    materiel_blocks = ''.join(materiel_blocks_list)

    # Etapes per language
    etapes_blocks_list = []
    for lang in ('fr', 'en', 'ar'):
        etapes = get_field(act, 'etapes', lang) if lang != 'fr' else act.get('etapes_fr', [])
        if not etapes:
            etapes = act.get('etapes_fr', [])
        items = ''.join(
            f'<li class="step-item"><span class="step-num">{i+1}</span><span class="step-text">{escape(s)}</span></li>'
            for i, s in enumerate(etapes)
        )
        etapes_blocks_list.append(f'<ol class="steps-list" lang="{lang}">{items}</ol>')
    etapes_blocks = ''.join(etapes_blocks_list)

    # Tip per language
    tip_blocks_list = []
    for lang in ('fr', 'en', 'ar'):
        tip = get_field(act, 'tip', lang) if lang != 'fr' else act.get('tip_fr', '')
        if not tip:
            tip = act.get('tip_fr', '')
        if tip:
            tip_blocks_list.append(f'<div class="tip-box" lang="{lang}"><span class="tip-icon">💡</span>{escape(tip)}</div>')
    tip_blocks = ''.join(tip_blocks_list)

    # Flowchart + pseudocode per language
    fc_pc_blocks_list = []
    for lang in ('fr', 'en', 'ar'):
        etapes = get_field(act, 'etapes', lang) if lang != 'fr' else act.get('etapes_fr', [])
        if not etapes:
            etapes = act.get('etapes_fr', [])
        fc = gen_flowchart(etapes, PSEUDO_LABELS[lang]['start'], PSEUDO_LABELS[lang]['end'])
        pc = gen_pseudocode(etapes, PSEUDO_LABELS[lang]['start'], PSEUDO_LABELS[lang]['end'])
        fc_pc_blocks_list.append(f'<div lang="{lang}">{fc}{pc}</div>')
    fc_pc_blocks = ''.join(fc_pc_blocks_list)

    # Code blocks (language-neutral — same for all)
    js_code = highlight_js(act['js'])
    py_code = highlight_py(act['py'])

    # Défis per language
    defis_blocks_list = []
    for lang in ('fr', 'en', 'ar'):
        defis = get_field(act, 'defis', lang) if lang != 'fr' else act.get('defis_fr', [])
        if not defis:
            defis = act.get('defis_fr', [])
        if defis:
            items = ''.join(
                f'<div class="chal-item"><span class="chal-dot {d["level"]}"></span><span>{escape(d["text"])}</span></div>'
                for d in defis
            )
            defis_blocks_list.append(f'<div class="chal-list" lang="{lang}">{items}</div>')
    defis_block_inner = ''.join(defis_blocks_list)
    defis_html = ''
    if defis_block_inner:
        defis_html = f'''
<div class="sec-label" data-i18n="sec_defis">Défis</div>
{defis_block_inner}'''

    # LED preview only for LED-related activities
    led_html = ''
    if act['cat'] == 'officiel' and 'LED' in act.get('title_fr', '').upper() or act['id'] == 3:
        led_html = f'<div class="led-col">{gen_led_preview()}</div>'

    return f'''
<section class="act-section" id="act-{act['id']}">
  <div class="act-header-bar" style="--hdr-color:{hdr_color}">
    <div class="act-num-badge" style="background:{hdr_color}">{act['id']}</div>
    <div class="act-title-area">
      {title_blocks}
      <div class="act-header-tags">
        {diff_chips}
        <span class="tag-chip time">⏱ {act['time']}</span>
        {official_badge}{v2_chip}{ai_chip}
        {wiki_link}
      </div>
    </div>
  </div>

  <div class="glass-card">
    <div class="sec-label" data-i18n="sec_objectif">Objectif</div>
    {objectif_blocks}
  </div>

  <div class="content-row">
    {led_html}
    <div class="info-col">
      <div class="sec-label" data-i18n="sec_materiel">Matériel</div>
      {materiel_blocks}
    </div>
  </div>

  <div class="sec-label" data-i18n="sec_etapes">Étapes</div>
  {etapes_blocks}

  {tip_blocks}

  <div class="sec-label" data-i18n="sec_algo">Algorithme</div>
  {fc_pc_blocks}

  <div class="sec-label" data-i18n="sec_code">Code</div>
  <div class="code-grid">
    <div class="code-panel">
      <div class="code-panel-header js-header">
        <span class="code-lang-dot js-dot"></span>JavaScript
        <div class="code-actions">
          <button class="code-btn copy-btn" data-i18n="copy_btn">Copier</button>
        </div>
      </div>
      <div class="code-block">{js_code}</div>
    </div>
    <div class="code-panel">
      <div class="code-panel-header py-header">
        <span class="code-lang-dot py-dot"></span>Python
        <div class="code-actions">
          <button class="code-btn copy-btn" data-i18n="copy_btn">Copier</button>
        </div>
      </div>
      <div class="code-block">{py_code}</div>
    </div>
  </div>

  {defis_html}

  <div class="act-done-bar">
    <div class="act-footer-meta">Activité #{act['id']} · {cat['icon']} {cat['name_fr']}</div>
    <button class="done-btn" data-id="{act['id']}" data-i18n="mark_done">Marquer comme fait</button>
  </div>
</section>
'''

# ═══════════════════════════════════════════════════════════════
#   SIDEBAR
# ═══════════════════════════════════════════════════════════════

def render_sidebar():
    sections = []
    for cat in CATS:
        cat_acts = [a for a in ACTIVITIES if a['cat'] == cat['id']]
        if not cat_acts:
            continue
        group_id = 'group-' + cat['id']
        # Activity links — trilingual title
        link_rows = []
        for a in cat_acts:
            title_blocks = ''.join(
                f'<span class="nav-link-title" lang="{lang}">{escape(a.get(f"title_{lang}", a.get("title_fr", "")))}</span>'
                for lang in ('fr', 'en', 'ar')
            )
            link_rows.append(
                f'<a class="nav-link" data-id="{a["id"]}" href="#act-{a["id"]}">'
                f'<span class="nav-link-num">{a["id"]}</span>'
                f'{title_blocks}'
                f'</a>'
            )
        links = ''.join(link_rows)
        # Category name trilingual
        cat_names = ''.join(
            f'<span lang="{lang}">{escape(cat[f"name_{lang}"])}</span>'
            for lang in ('fr', 'en', 'ar')
        )
        sections.append(f'''
<div class="nav-section open" data-target="{group_id}">
  <span class="nav-section-title">
    <span class="nav-section-icon">{cat['icon']}</span>
    {cat_names}
  </span>
  <span style="display:flex; align-items:center; gap:8px;">
    <span class="nav-section-count">{len(cat_acts)}</span>
    <span class="arrow">▶</span>
  </span>
</div>
<div class="nav-group open" id="{group_id}">{links}</div>''')
    return ''.join(sections)

# ═══════════════════════════════════════════════════════════════
#   THEME PANEL
# ═══════════════════════════════════════════════════════════════

def render_theme_swatches():
    themes = [
        ('mosque',  'Mosque',  '#d4af37'),
        ('zellige', 'Zellige', '#a855f7'),
        ('andalus', 'Andalus', '#10b981'),
        ('space',   'Space',   '#a855f7'),
        ('jungle',  'Jungle',  '#84cc16'),
        ('robot',   'Robot',   '#60a5fa'),
        ('riad',    'Riad',    '#c2783c'),
        ('medina',  'Medina',  '#0f766e'),
        ('retro',   '🕹️ Retro', '#00ff41'),
    ]
    return ''.join(
        f'<div class="theme-swatch" data-theme="{tid}"><span class="theme-dot" style="background:{dot}"></span>{name}</div>'
        for tid, name, dot in themes
    )

# ═══════════════════════════════════════════════════════════════
#   PARCOURS (learning paths) PANEL
# ═══════════════════════════════════════════════════════════════

def render_parcours_panel():
    cards = []
    for p in PARCOURS:
        # Find titles of activities in this path (show in all 3 langs with lang attr)
        path_acts = [a for a in ACTIVITIES if a['id'] in p['activity_ids']]

        act_list_fr = ''.join(
            f'<a href="#act-{a["id"]}" class="parcours-act" data-id="{a["id"]}">'
            f'<span class="parcours-act-num">{a["id"]}</span>'
            f'<span class="parcours-act-title">{escape(a.get("title_fr", ""))}</span>'
            f'<span class="parcours-act-stars">{"★" * a["stars"]}</span>'
            f'</a>'
            for a in path_acts
        )
        act_list_en = ''.join(
            f'<a href="#act-{a["id"]}" class="parcours-act" data-id="{a["id"]}">'
            f'<span class="parcours-act-num">{a["id"]}</span>'
            f'<span class="parcours-act-title">{escape(a.get("title_en", a.get("title_fr", "")))}</span>'
            f'<span class="parcours-act-stars">{"★" * a["stars"]}</span>'
            f'</a>'
            for a in path_acts
        )
        act_list_ar = ''.join(
            f'<a href="#act-{a["id"]}" class="parcours-act" data-id="{a["id"]}">'
            f'<span class="parcours-act-num">{a["id"]}</span>'
            f'<span class="parcours-act-title">{escape(a.get("title_ar", a.get("title_fr", "")))}</span>'
            f'<span class="parcours-act-stars">{"★" * a["stars"]}</span>'
            f'</a>'
            for a in path_acts
        )

        # Trilingual name, desc, meta
        names = ''.join(
            f'<div class="parcours-name" lang="{lang}">{escape(p[f"name_{lang}"])}</div>'
            for lang in ('fr', 'en', 'ar')
        )
        descs = ''.join(
            f'<div class="parcours-desc" lang="{lang}">{escape(p[f"desc_{lang}"])}</div>'
            for lang in ('fr', 'en', 'ar')
        )
        activities_label = {'fr': 'activités', 'en': 'activities', 'ar': 'نشاطاً'}
        metas = ''.join(
            f'<div class="parcours-meta" lang="{lang}">{escape(p[f"age_{lang}"])} · {escape(p[f"duration_{lang}"])} · {len(p["activity_ids"])} {activities_label[lang]}</div>'
            for lang in ('fr', 'en', 'ar')
        )

        cards.append(f'''
<div class="parcours-card">
  <div class="parcours-header">
    <span class="parcours-icon">{p['icon']}</span>
    <div class="parcours-info">
      {names}
      {metas}
    </div>
  </div>
  {descs}
  <div class="parcours-list" lang="fr">{act_list_fr}</div>
  <div class="parcours-list" lang="en">{act_list_en}</div>
  <div class="parcours-list" lang="ar">{act_list_ar}</div>
</div>''')
    return ''.join(cards)

# ═══════════════════════════════════════════════════════════════
#   RESOURCES PANEL
# ═══════════════════════════════════════════════════════════════

RESOURCES = [
    {
        'icon': '🔧',
        'title_fr': 'Outils en ligne', 'title_en': 'Online tools', 'title_ar': 'أدوات عبر الإنترنت',
        'items': [
            {'icon': '🟣', 'name': 'MakeCode micro:bit', 'url': 'https://makecode.microbit.org',
             'desc_fr': 'Éditeur officiel blocs + JavaScript',
             'desc_en': 'Official blocks + JavaScript editor',
             'desc_ar': 'المحرر الرسمي للمكعبات + JavaScript'},
            {'icon': '🐍', 'name': 'Python Editor', 'url': 'https://python.microbit.org',
             'desc_fr': 'Éditeur MicroPython pour micro:bit',
             'desc_en': 'MicroPython editor for micro:bit',
             'desc_ar': 'محرر MicroPython لـ micro:bit'},
            {'icon': '🧠', 'name': 'CreateAI', 'url': 'https://createai.microbit.org',
             'desc_fr': 'Entraîner des modèles IA qui tournent sur le micro:bit',
             'desc_en': 'Train AI models that run on the micro:bit',
             'desc_ar': 'تدريب نماذج الذكاء الاصطناعي التي تعمل على micro:bit'},
            {'icon': '📸', 'name': 'Teachable Machine', 'url': 'https://teachablemachine.withgoogle.com',
             'desc_fr': 'IA image / audio / pose dans le navigateur (Google)',
             'desc_en': 'Image / audio / pose AI in the browser (Google)',
             'desc_ar': 'ذكاء اصطناعي للصور/الصوت/الوضعية في المتصفح (Google)'},
            {'icon': '🎨', 'name': 'Mind+', 'url': 'https://mindplus.cc/en.html',
             'desc_fr': 'Alternative Scratch 3 graphique (DFRobot)',
             'desc_en': 'Scratch 3-style graphical alternative (DFRobot)',
             'desc_ar': 'بديل رسومي على نمط Scratch 3 (DFRobot)'},
        ],
    },
    {
        'icon': '🧩',
        'title_fr': 'Extensions MakeCode', 'title_en': 'MakeCode extensions', 'title_ar': 'إضافات MakeCode',
        'items': [
            {'icon': '🤖', 'name': 'pxt-maqueen (officiel)', 'url': 'https://github.com/DFRobot/pxt-maqueen',
             'desc_fr': 'Extension officielle DFRobot pour le Maqueen / Maqueen Lite',
             'desc_en': 'Official DFRobot extension for Maqueen / Maqueen Lite',
             'desc_ar': 'الامتداد الرسمي من DFRobot لـ Maqueen / Maqueen Lite'},
            {'icon': '🚗', 'name': 'pxt-DFRobot_MaqueenPlus_v20', 'url': 'https://github.com/DFRobot/pxt-DFRobot_MaqueenPlus_v20',
             'desc_fr': 'Extension pour Maqueen Plus V2 (modèle supérieur, HuskyLens, etc.)',
             'desc_en': 'Extension for Maqueen Plus V2 (premium model, HuskyLens, etc.)',
             'desc_ar': 'امتداد لـ Maqueen Plus V2 (الطراز المتقدم، HuskyLens، إلخ)'},
            {'icon': '💡', 'name': 'pxt-neopixel', 'url': 'https://github.com/microsoft/pxt-neopixel',
             'desc_fr': 'Bibliothèque officielle Microsoft pour LEDs RGB',
             'desc_en': 'Official Microsoft library for RGB LEDs',
             'desc_ar': 'مكتبة Microsoft الرسمية لمصابيح RGB'},
            {'icon': '🔧', 'name': 'pxt-maqueen (jhlucky fork)', 'url': 'https://github.com/jhlucky/maqueen',
             'desc_fr': 'Fork communautaire avec améliorations',
             'desc_en': 'Community fork with improvements',
             'desc_ar': 'نسخة مجتمعية مع تحسينات'},
            {'icon': '⚡', 'name': 'Arduino library', 'url': 'https://github.com/kd8bxp/micro-Maqueen-Arduino-Library',
             'desc_fr': 'Pour programmer le Maqueen via Arduino IDE',
             'desc_en': 'Program the Maqueen via Arduino IDE',
             'desc_ar': 'برمجة Maqueen عبر Arduino IDE'},
        ],
    },
    {
        'icon': '📘',
        'title_fr': 'Documentation officielle', 'title_en': 'Official documentation', 'title_ar': 'الوثائق الرسمية',
        'items': [
            {'icon': '📚', 'name': 'Wiki Maqueen Lite (ROB0148)', 'url': 'https://wiki.dfrobot.com/rob0148-en/',
             'desc_fr': 'Documentation officielle DFRobot — 15 exemples référence de ce guide',
             'desc_en': 'Official DFRobot docs — 15 reference examples of this guide',
             'desc_ar': 'الوثائق الرسمية من DFRobot — 15 مثالاً مرجعياً لهذا الدليل'},
            {'icon': '🛒', 'name': 'Page produit Maqueen Lite', 'url': 'https://www.dfrobot.com/product-1783.html',
             'desc_fr': 'Fiche produit, spécifications, commande',
             'desc_en': 'Product page, specifications, ordering',
             'desc_ar': 'صفحة المنتج، المواصفات، الطلب'},
            {'icon': '📖', 'name': 'Tutoriel Maqueen Plus (PDFs)', 'url': 'https://github.com/DFRobot/Maqueen_Plus_Getting_Started_Tutorial_MakeCode',
             'desc_fr': '14 chapitres PDF pour Maqueen Plus (applicable au Lite)',
             'desc_en': '14 PDF chapters for Maqueen Plus (applies to Lite too)',
             'desc_ar': '14 فصلاً PDF لـ Maqueen Plus (ينطبق على Lite)'},
            {'icon': '🟨', 'name': 'micro:bit foundation', 'url': 'https://microbit.org',
             'desc_fr': 'Site officiel du micro:bit — références et projets',
             'desc_en': 'Official micro:bit site — references and projects',
             'desc_ar': 'الموقع الرسمي لـ micro:bit — مراجع ومشاريع'},
            {'icon': '🎓', 'name': 'micro:bit classroom', 'url': 'https://classroom.microbit.org',
             'desc_fr': 'Plateforme enseignants : projeter le code, suivre les élèves',
             'desc_en': 'Teacher platform: project code, track students',
             'desc_ar': 'منصة للمعلمين: عرض الكود، متابعة الطلاب'},
            {'icon': '📑', 'name': "Guide d'utilisation micro:bit", 'url': 'https://microbit.org/get-started/user-guide/overview/',
             'desc_fr': 'Broches, capteurs, fonctions — référence technique',
             'desc_en': 'Pins, sensors, functions — technical reference',
             'desc_ar': 'الدبابيس، المستشعرات، الوظائف — المرجع التقني'},
        ],
    },
    {
        'icon': '💬',
        'title_fr': 'Communauté & support', 'title_en': 'Community & support', 'title_ar': 'المجتمع والدعم',
        'items': [
            {'icon': '🟣', 'name': 'Forum MakeCode', 'url': 'https://forum.makecode.com',
             'desc_fr': 'Poser une question sur MakeCode — réponses rapides',
             'desc_en': 'Ask MakeCode questions — quick answers',
             'desc_ar': 'طرح أسئلة حول MakeCode — إجابات سريعة'},
            {'icon': '🔶', 'name': 'Forum DFRobot', 'url': 'https://www.dfrobot.com/forum/',
             'desc_fr': 'Communauté DFRobot — projets, dépannage matériel',
             'desc_en': 'DFRobot community — projects, hardware troubleshooting',
             'desc_ar': 'مجتمع DFRobot — مشاريع، استكشاف أعطال الأجهزة'},
            {'icon': '🟨', 'name': 'Support micro:bit', 'url': 'https://support.microbit.org',
             'desc_fr': 'Aide officielle micro:bit — FAQ, tutoriels',
             'desc_en': 'Official micro:bit help — FAQ, tutorials',
             'desc_ar': 'الدعم الرسمي لـ micro:bit — الأسئلة الشائعة، الدروس'},
            {'icon': '🎯', 'name': 'Ce guide (bit-54)', 'url': 'https://abourdim.github.io/bit-54-activities/',
             'desc_fr': "58 activités micro:bit — grand cousin de ce guide",
             'desc_en': '58 micro:bit activities — big cousin of this guide',
             'desc_ar': '58 نشاطاً لـ micro:bit — ابن عم هذا الدليل الأكبر'},
            {'icon': '🛠️', 'name': 'Workshop-DIY Toolkit', 'url': 'https://abourdim.github.io/tools/',
             'desc_fr': 'Collection de guides pédagogiques maker',
             'desc_en': 'Collection of maker educational guides',
             'desc_ar': 'مجموعة من الأدلة التعليمية للمبدعين'},
        ],
    },
]

def render_resources_panel():
    sections = []
    for sec in RESOURCES:
        items_html = ''
        for item in sec['items']:
            desc_blocks = ''.join(
                f'<div class="resource-desc" lang="{lang}">{escape(item.get(f"desc_{lang}", item.get("desc_fr", "")))}</div>'
                for lang in ('fr', 'en', 'ar')
            )
            items_html += (
                f'<a href="{item["url"]}" class="resource-item" target="_blank" rel="noopener">'
                f'<span class="resource-icon">{item["icon"]}</span>'
                f'<div class="resource-info">'
                f'<div class="resource-name">{escape(item["name"])}</div>'
                f'{desc_blocks}'
                f'</div>'
                f'<span class="resource-arrow">↗</span>'
                f'</a>'
            )
        title_blocks = ''.join(
            f'<span class="resource-section-title" lang="{lang}">{escape(sec[f"title_{lang}"])}</span>'
            for lang in ('fr', 'en', 'ar')
        )
        sections.append(f'''
<div class="resource-section">
  <div class="resource-section-header">
    <span class="resource-section-icon">{sec['icon']}</span>
    {title_blocks}
    <span class="resource-section-count">{len(sec['items'])}</span>
  </div>
  <div class="resource-items">{items_html}</div>
</div>''')
    return ''.join(sections)


# ═══════════════════════════════════════════════════════════════
#   HELP PANEL (pinout + cheatsheet + FAQ)
# ═══════════════════════════════════════════════════════════════

def render_help_panel():
    from help_module import gen_pinout_svg
    # Cheatsheet — trilingual (pattern & note translate per lang; code is universal)
    cheat_by_lang = {}
    for lang in ('fr', 'en', 'ar'):
        sections_html = []
        for sec in CHEATSHEET_SECTIONS:
            items_html = ''
            for item in sec['items']:
                note = item.get(f'note_{lang}', '')
                note_html = f'<div class="cheat-note">{escape(note)}</div>' if note else ''
                items_html += (
                    f'<div class="cheat-item">'
                    f'<div class="cheat-pattern">{escape(item[f"pattern_{lang}"])}</div>'
                    f'<div class="cheat-code-row">'
                    f'<div class="cheat-code js"><span class="cheat-lang">JS</span><code>{escape(item["js"])}</code></div>'
                    f'<div class="cheat-code py"><span class="cheat-lang">PY</span><code>{escape(item["py"])}</code></div>'
                    f'</div>'
                    f'{note_html}'
                    f'</div>'
                )
            sections_html.append(f'''
<div class="cheat-section">
  <div class="cheat-section-header">
    <span class="cheat-section-icon">{sec['icon']}</span>
    <span>{escape(sec[f'title_{lang}'])}</span>
  </div>
  <div class="cheat-items">{items_html}</div>
</div>''')
        cheat_by_lang[lang] = ''.join(sections_html)

    # FAQ trilingual
    faq_by_lang = {}
    for lang in ('fr', 'en', 'ar'):
        items = []
        for faq in FAQ:
            bullets = ''.join(f'<li>{escape(a)}</li>' for a in faq[f'a_{lang}'])
            items.append(f'''
<details class="faq-item">
  <summary class="faq-question">{escape(faq[f'q_{lang}'])}</summary>
  <ul class="faq-answer">{bullets}</ul>
</details>''')
        faq_by_lang[lang] = ''.join(items)

    # Pinout: one SVG per language
    pinouts = ''.join(
        f'<div lang="{lang}">{gen_pinout_svg(lang)}</div>'
        for lang in ('fr', 'en', 'ar')
    )

    # Tab labels per language
    tab_labels = {
        'fr': ('📐 Matériel', '⚡ Antisèche', '🆘 FAQ'),
        'en': ('📐 Hardware', '⚡ Cheatsheet', '🆘 FAQ'),
        'ar': ('📐 العتاد', '⚡ ورقة الغش', '🆘 الأسئلة الشائعة'),
    }
    tabs_html_parts = []
    for lang in ('fr', 'en', 'ar'):
        pinout_lbl, cheat_lbl, faq_lbl = tab_labels[lang]
        tabs_html_parts.append(
            f'<div class="help-tabs" lang="{lang}">'
            f'<button class="help-tab active" data-tab="pinout">{pinout_lbl}</button>'
            f'<button class="help-tab" data-tab="cheat">{cheat_lbl}</button>'
            f'<button class="help-tab" data-tab="faq">{faq_lbl}</button>'
            f'</div>'
        )
    tabs_html = ''.join(tabs_html_parts)

    # Intros and specs per language
    intros = {
        'fr': {
            'pinout': '<strong>Maqueen Lite (ROB0148)</strong> — diagramme des ports et composants. Imprime cette page et colle-la à ton poste de travail : tu la consulteras des centaines de fois.',
            'cheat': 'Les patrons de code Maqueen les plus utilisés. Copie-colle directement dans MakeCode.',
            'faq': 'Les problèmes les plus fréquents en classe — et comment les résoudre en 30 secondes.',
        },
        'en': {
            'pinout': '<strong>Maqueen Lite (ROB0148)</strong> — ports and component diagram. Print this page and stick it near your workstation: you\'ll consult it hundreds of times.',
            'cheat': 'The most-used Maqueen code patterns. Copy-paste directly into MakeCode.',
            'faq': 'The most common classroom problems — and how to solve them in 30 seconds.',
        },
        'ar': {
            'pinout': '<strong>Maqueen Lite (ROB0148)</strong> — مخطط المنافذ والمكونات. اطبع هذه الصفحة والصقها بجانب مكان عملك: ستراجعها مئات المرات.',
            'cheat': 'أكثر أنماط كود Maqueen استخداماً. انسخ والصق مباشرة في MakeCode.',
            'faq': 'أكثر المشاكل شيوعاً في الفصل — وكيف تحلها في 30 ثانية.',
        },
    }

    specs_rows = {
        'fr': [
            ('Alimentation', '3,5–5V (3× AAA ou Li-ion 3,7V)'),
            ('Moteurs', '2× N20 métal, PWM 0-255'),
            ('LEDs avant', 'P8 (gauche), P12 (droite) · ON/OFF'),
            ('LEDs RGB ambiance', '4× NeoPixel sur P15 · 16M couleurs'),
            ('Capteurs ligne IR', 'P13 (G), P14 (D) · 0=noir, 1=blanc'),
            ('Ultrason', 'Port dédié SR04/SR04P · 3-400cm · 5V'),
            ('Servo', 'Ports S1 et S2 · AnalogPin P1/P2'),
            ('IR (télécommande)', 'Récepteur NEC sur P16'),
            ('I²C', '5V · pour module externe'),
            ('Broches Gravity', 'P0, P1, P2'),
            ('micro:bit', 'v1 ou v2 compatible (v2 pour IA, son, micro)'),
        ],
        'en': [
            ('Power', '3.5–5V (3× AAA or Li-ion 3.7V)'),
            ('Motors', '2× N20 metal, PWM 0-255'),
            ('Front LEDs', 'P8 (left), P12 (right) · ON/OFF'),
            ('Ambient RGB LEDs', '4× NeoPixel on P15 · 16M colors'),
            ('IR line sensors', 'P13 (L), P14 (R) · 0=black, 1=white'),
            ('Ultrasonic', 'Dedicated SR04/SR04P port · 3-400cm · 5V'),
            ('Servo', 'S1 and S2 ports · AnalogPin P1/P2'),
            ('IR (remote)', 'NEC receiver on P16'),
            ('I²C', '5V · for external module'),
            ('Gravity pins', 'P0, P1, P2'),
            ('micro:bit', 'v1 or v2 compatible (v2 for AI, sound, mic)'),
        ],
        'ar': [
            ('الطاقة', '3.5–5V (3× AAA أو Li-ion 3.7V)'),
            ('المحركات', '2× N20 معدني، PWM 0-255'),
            ('المصابيح الأمامية', 'P8 (يسار)، P12 (يمين) · تشغيل/إيقاف'),
            ('مصابيح RGB المحيطية', '4× NeoPixel على P15 · 16 مليون لون'),
            ('مستشعرات خط IR', 'P13 (يسار)، P14 (يمين) · 0=أسود، 1=أبيض'),
            ('الموجات فوق الصوتية', 'منفذ SR04/SR04P مخصص · 3-400سم · 5V'),
            ('سيرفو', 'منفذا S1 و S2 · AnalogPin P1/P2'),
            ('IR (جهاز التحكم)', 'مستقبل NEC على P16'),
            ('I²C', '5V · للوحدة الخارجية'),
            ('دبابيس Gravity', 'P0, P1, P2'),
            ('micro:bit', 'v1 أو v2 متوافق (v2 للذكاء الاصطناعي، الصوت، الميكروفون)'),
        ],
    }

    # Build the help-content pinout block per language
    pinout_blocks = []
    cheat_blocks = []
    faq_blocks = []
    for lang in ('fr', 'en', 'ar'):
        # Specs rows
        rows = ''.join(
            f'<div class="spec-row"><span class="spec-key">{escape(k)}</span><span class="spec-val">{escape(v)}</span></div>'
            for k, v in specs_rows[lang]
        )
        pinout_blocks.append(
            f'<div lang="{lang}" class="help-pinout-block">'
            f'<div class="help-intro">{intros[lang]["pinout"]}</div>'
            f'{gen_pinout_svg(lang)}'
            f'<div class="pinout-specs">{rows}</div>'
            f'</div>'
        )
        cheat_blocks.append(
            f'<div lang="{lang}">'
            f'<div class="help-intro">{escape(intros[lang]["cheat"])}</div>'
            f'{cheat_by_lang[lang]}'
            f'</div>'
        )
        faq_blocks.append(
            f'<div lang="{lang}">'
            f'<div class="help-intro">{escape(intros[lang]["faq"])}</div>'
            f'{faq_by_lang[lang]}'
            f'</div>'
        )

    return f'''
{tabs_html}

<div class="help-content help-pinout active">
  {''.join(pinout_blocks)}
</div>

<div class="help-content help-cheat">
  {''.join(cheat_blocks)}
</div>

<div class="help-content help-faq">
  {''.join(faq_blocks)}
</div>
'''

# ═══════════════════════════════════════════════════════════════
#   ASSEMBLE HTML
# ═══════════════════════════════════════════════════════════════

def build():
    sidebar_html = render_sidebar()
    activities_html = '\n'.join(render_activity(a) for a in ACTIVITIES)
    theme_swatches = render_theme_swatches()
    parcours_html = render_parcours_panel()
    resources_html = render_resources_panel()
    help_html = render_help_panel()

    # JS needs activities data (minimal, for ⌘K) + i18n
    js_activities = [{
        'id': a['id'],
        'cat': a['cat'],
        'stars': a['stars'],
        'time': a['time'],
        'official': bool(a.get('official')),
        'title_fr': a['title_fr'],
        'title_en': a['title_en'],
        'title_ar': a['title_ar'],
        'objectif_fr': a['objectif_fr'],
    } for a in ACTIVITIES]

    js_code = js_template(json.dumps(js_activities, ensure_ascii=False), json.dumps(I18N, ensure_ascii=False))
    js_code = js_code.replace('__ACTIVITIES__', json.dumps(js_activities, ensure_ascii=False))
    js_code = js_code.replace('__I18N__', json.dumps(I18N, ensure_ascii=False))

    html_out = f'''<!doctype html>
<html lang="fr" dir="ltr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=5">
<meta name="theme-color" content="#0a0f1e">
<title>Maqueen Lite · Guide Terrain · Workshop-DIY</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Tajawal:wght@400;500;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>

<!-- Splash -->
<div class="splash">
  <div class="splash-logo">🛠️</div>
  <div class="splash-title" data-i18n="splash_title">Maqueen · Guide Terrain</div>
  <div class="splash-sub" data-i18n="splash_sub">Workshop-DIY</div>
  <div class="splash-bismillah">بِسْمِ ٱللَّٰهِ ٱلرَّحْمَـٰنِ ٱلرَّحِيمِ</div>
</div>

<!-- Top bar -->
<nav class="topbar">
  <button class="mobile-toggle" id="mobile-toggle">☰</button>
  <a class="brand" id="btn-home" href="#">
    <span class="brand-logo">🛠️</span>
    <span class="brand-text">Maqueen · Guide</span>
  </a>
  <div class="bismillah-bar">بِسْمِ ٱللَّٰهِ ٱلرَّحْمَـٰنِ ٱلرَّحِيمِ</div>
  <div class="topbar-actions">
    <div class="progress-pill"><span>📊</span><span class="count">0/{len(ACTIVITIES)}</span></div>
    <img class="flag" data-lang="fr" src="{FLAGS['fr']}" alt="Français" title="Français">
    <img class="flag" data-lang="en" src="{FLAGS['en']}" alt="English" title="English">
    <img class="flag" data-lang="ar" src="{FLAGS['ar']}" alt="العربية" title="العربية">
    <button class="topbar-btn" id="btn-random" title="Activité au hasard">🎲</button>
    <button class="topbar-btn" id="btn-help" title="Aide / Matériel">📖<span data-i18n="nav_help">Aide</span></button>
    <button class="topbar-btn" id="btn-parcours" title="Parcours">🗺️<span data-i18n="nav_paths">Parcours</span></button>
    <button class="topbar-btn" id="btn-resources" title="Ressources">📚<span data-i18n="nav_resources">Ressources</span></button>
    <button class="topbar-btn" id="btn-cmdk" title="⌘K">🔍<span data-i18n="search">Rechercher</span></button>
    <button class="topbar-btn" id="btn-settings" title="Settings">⚙️</button>
  </div>
</nav>

<!-- Mobile overlay -->
<div class="mobile-overlay" id="mobile-overlay"></div>

<!-- Layout -->
<div class="layout">
  <!-- Sidebar -->
  <aside class="sidebar" id="sidebar">
    <div class="nav-search">
      <input type="text" id="sidebar-search" placeholder="Rechercher…" data-i18n-placeholder="cmdk_placeholder">
    </div>
    {sidebar_html}
  </aside>

  <!-- Main content -->
  <main class="main">
    <!-- Cover -->
    <section class="cover" id="cover">
      <div class="cover-board">
        <svg width="280" height="220" viewBox="0 0 280 220" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <filter id="coverglow"><feGaussianBlur stdDeviation="3" result="g"/><feMerge><feMergeNode in="g"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
          </defs>
          <!-- Maqueen body -->
          <rect x="40" y="60" width="200" height="110" rx="20" fill="#d4af37" opacity="0.15" stroke="#d4af37" stroke-width="1.5"/>
          <!-- micro:bit LED matrix -->
          <rect x="95" y="80" width="90" height="70" rx="4" fill="#050510"/>
          {''.join(f'<circle cx="{108+(i%5)*16}" cy="{92+(i//5)*13}" r="5" fill="#ff1a1a" filter="url(#coverglow)"/>' for i in range(25) if i in [0,2,4,5,7,9,10,12,14,16,18,22])}
          <!-- Wheels -->
          <circle cx="55" cy="140" r="22" fill="#333" stroke="#555" stroke-width="2"/>
          <circle cx="55" cy="140" r="8" fill="#666"/>
          <circle cx="225" cy="140" r="22" fill="#333" stroke="#555" stroke-width="2"/>
          <circle cx="225" cy="140" r="8" fill="#666"/>
          <!-- LEDs avant -->
          <circle cx="90" cy="185" r="8" fill="#ff0055" filter="url(#coverglow)"/>
          <circle cx="190" cy="185" r="8" fill="#ff0055" filter="url(#coverglow)"/>
          <!-- RGB LEDs (4) -->
          <circle cx="70" cy="45" r="5" fill="#a855f7" filter="url(#coverglow)"/>
          <circle cx="105" cy="40" r="5" fill="#22d3ee" filter="url(#coverglow)"/>
          <circle cx="175" cy="40" r="5" fill="#10b981" filter="url(#coverglow)"/>
          <circle cx="210" cy="45" r="5" fill="#eab308" filter="url(#coverglow)"/>
        </svg>
      </div>
      <h1 class="cover-hero" data-i18n="cover_hero">Maqueen Lite</h1>
      <div class="cover-sub" data-i18n="cover_sub">Guide terrain — Robotique micro:bit</div>
      <div class="cover-tagline" data-i18n="cover_tagline">Un guide complet et copy-paste pour apprendre la robotique avec le Maqueen Lite.</div>
      <div class="cover-cta">
        <a href="#act-1" class="cover-btn">🚀 <span data-i18n="cover_cta_start">Commencer</span></a>
        <a href="#act-2" class="cover-btn">📘 <span data-i18n="cover_cta_official">Exemples officiels</span></a>
        <button class="cover-btn" onclick="document.getElementById('btn-parcours').click()">🗺️ <span data-i18n="cover_cta_paths">Parcours</span></button>
        <button class="cover-btn" onclick="document.getElementById('btn-resources').click()">📚 <span data-i18n="cover_cta_resources">Ressources</span></button>
      </div>
      <div class="cover-stats">
        <div class="cover-stat">
          <div class="cover-stat-num">{len(ACTIVITIES)}</div>
          <div class="cover-stat-label" data-i18n="stat_activities">Activités</div>
        </div>
        <div class="cover-stat">
          <div class="cover-stat-num">3</div>
          <div class="cover-stat-label" data-i18n="stat_languages">Langues</div>
        </div>
        <div class="cover-stat">
          <div class="cover-stat-num">{len(CATS)}</div>
          <div class="cover-stat-label" data-i18n="stat_categories">Catégories</div>
        </div>
        <div class="cover-stat">
          <div class="cover-stat-num">{len([a for a in ACTIVITIES if a.get('official')])}</div>
          <div class="cover-stat-label" data-i18n="stat_official">Officiels</div>
        </div>
      </div>
    </section>

    {activities_html}
  </main>
</div>

<!-- Site footer -->
<footer class="site-footer">
  <span class="pet">🐱</span>
  <span class="hijri-date"></span>
  <span>·</span>
  <span data-i18n="footer_powered">Propulsé par</span>
  <a class="footer-link" href="https://abourdim.github.io/tools/" target="_blank" rel="noopener" data-i18n="footer_author">Workshop-DIY</a>
</footer>

<!-- Command palette -->
<div class="cmdk-overlay" id="cmdk-overlay">
  <div class="cmdk">
    <input class="cmdk-input" id="cmdk-input" type="text" placeholder="Rechercher une activité…" data-i18n-placeholder="cmdk_placeholder">
    <div class="cmdk-results" id="cmdk-results"></div>
    <div class="cmdk-hint">
      <span data-i18n="cmdk_hint_nav">↑↓ naviguer</span>
      <span data-i18n="cmdk_hint_open">↵ ouvrir</span>
      <span data-i18n="cmdk_hint_close">esc fermer</span>
    </div>
  </div>
</div>

<!-- Settings panel -->
<aside class="panel right" id="panel-settings">
  <div class="panel-header">
    <div class="panel-title">
      <span lang="fr">Paramètres</span>
      <span lang="en">Settings</span>
      <span lang="ar">الإعدادات</span>
    </div>
    <button class="panel-close">✕</button>
  </div>
  <div class="panel-section">
    <div class="panel-section-label">
      <span lang="fr">Thème</span>
      <span lang="en">Theme</span>
      <span lang="ar">السمة</span>
    </div>
    <div class="theme-grid">{theme_swatches}</div>
  </div>
  <div class="panel-section">
    <div class="panel-section-label">
      <span lang="fr">Son</span>
      <span lang="en">Sound</span>
      <span lang="ar">الصوت</span>
    </div>
    <div class="toggle-row">
      <span class="toggle-label">
        🔊
        <span lang="fr">Effets sonores</span>
        <span lang="en">Sound effects</span>
        <span lang="ar">المؤثرات الصوتية</span>
      </span>
      <div class="toggle-switch" id="sound-toggle"></div>
    </div>
  </div>
  <div class="panel-section">
    <div class="panel-section-label">
      <span lang="fr">Easter eggs</span>
      <span lang="en">Easter eggs</span>
      <span lang="ar">مفاجآت خفية</span>
    </div>
    <div style="font-size: 12px; color: var(--muted); line-height: 1.7;" lang="fr">
      🕹️ Konami code (↑↑↓↓←→←→BA) débloque le thème Retro<br>
      🐱 Clique 10 fois sur le chat en bas de page<br>
      ⌘K / Ctrl+K pour ouvrir la recherche
    </div>
    <div style="font-size: 12px; color: var(--muted); line-height: 1.7;" lang="en">
      🕹️ Konami code (↑↑↓↓←→←→BA) unlocks the Retro theme<br>
      🐱 Click the cat in the footer 10 times<br>
      ⌘K / Ctrl+K to open search
    </div>
    <div style="font-size: 12px; color: var(--muted); line-height: 1.7;" lang="ar">
      🕹️ شيفرة كونامي (↑↑↓↓←→←→BA) تفتح سمة Retro<br>
      🐱 انقر على القط في أسفل الصفحة 10 مرات<br>
      ⌘K / Ctrl+K لفتح البحث
    </div>
  </div>
</aside>

<!-- Parcours panel (learning paths) -->
<aside class="panel right" id="panel-parcours">
  <div class="panel-header">
    <div class="panel-title">
      <span style="margin-right:6px">🗺️</span>
      <span lang="fr">Parcours d'apprentissage</span>
      <span lang="en">Learning paths</span>
      <span lang="ar">مسارات التعلم</span>
    </div>
    <button class="panel-close">✕</button>
  </div>
  <div class="parcours-wrap">
    {parcours_html}
  </div>
</aside>

<!-- Resources panel (helpful links) -->
<aside class="panel right" id="panel-resources">
  <div class="panel-header">
    <div class="panel-title">
      <span style="margin-right:6px">📚</span>
      <span lang="fr">Ressources & liens utiles</span>
      <span lang="en">Resources & useful links</span>
      <span lang="ar">الموارد والروابط المفيدة</span>
    </div>
    <button class="panel-close">✕</button>
  </div>
  <div class="resources-wrap">
    <div class="resources-intro" lang="fr">
      Tous les liens essentiels pour aller plus loin avec ton Maqueen — extensions MakeCode, outils IA, documentation officielle, forums.
    </div>
    <div class="resources-intro" lang="en">
      All the essential links to go further with your Maqueen — MakeCode extensions, AI tools, official documentation, forums.
    </div>
    <div class="resources-intro" lang="ar">
      كل الروابط الأساسية للتعمق أكثر مع Maqueen — امتدادات MakeCode، أدوات الذكاء الاصطناعي، الوثائق الرسمية، المنتديات.
    </div>
    {resources_html}
  </div>
</aside>

<!-- Help panel (pinout + cheatsheet + FAQ) -->
<aside class="panel right panel-wide" id="panel-help">
  <div class="panel-header">
    <div class="panel-title">
      <span style="margin-right:6px">📖</span>
      <span lang="fr">Aide & référence</span>
      <span lang="en">Help & reference</span>
      <span lang="ar">المساعدة والمرجع</span>
    </div>
    <button class="panel-close">✕</button>
  </div>
  {help_html}
</aside>

<!-- Toast -->
<div class="toast" id="toast"></div>

<script>{js_code}</script>
</body>
</html>
'''
    return html_out


if __name__ == '__main__':
    out = build()
    pathlib.Path('maqueen-guide.html').write_text(out, encoding='utf-8')
    print(f'Written {len(out):,} bytes')
