#!/usr/bin/env python3
"""
Maqueen Lite · Guide terrain — Main builder.
Emits a single index.html with the bit-48-activities look-and-feel,
populated with maqueen data.
"""
import json, pathlib, html, sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import ACTIVITIES as PHASE1_ACTIVITIES, CATS
from phase2 import PHASE2
from phase3 import PHASE3
from translations import TRANSLATIONS as T1
from translations_p2 import TRANSLATIONS_P2 as T2
from translations_p3 import TRANSLATIONS_P3 as T3
from css_module import CSS
from js_module import SCRIPT

ALL_TR = {**T1, **T2, **T3}
ACTIVITIES = PHASE1_ACTIVITIES + PHASE2 + PHASE3
EXPECTED = 85
assert len(ACTIVITIES) == EXPECTED, f"Parsed {len(ACTIVITIES)}; expected {EXPECTED}"
ids = [a['id'] for a in ACTIVITIES]
assert ids == list(range(1, EXPECTED + 1)), f"Non-sequential IDs: {ids}"
print(f"Loaded {len(ACTIVITIES)} activities")

# ═══════════════════════════════════════════════════════════════════
# DATA ADAPTERS — maqueen shape → bit-48 shape
# ═══════════════════════════════════════════════════════════════════

LEVEL_TO_DIFF = {'easy': 1, 'med': 2, 'hard': 3}

def part_of(act):
    # Stars 1–2 → simple, 3 → advanced.  Matches the two-group sidebar.
    return 'simple' if act['stars'] <= 2 else 'advanced'

def adapt_activity(a):
    """maqueen activity → bit-48 A[] entry."""
    return {
        'id': a['id'],
        'title': a['title_fr'],
        'part': part_of(a),
        'difficulty': a['stars'],
        'time': a.get('time', '—'),
        'v2': bool(a.get('v2')),
        'ia': bool(a.get('ai')),
        'goal': a['objectif_fr'],
        'needs': list(a.get('materiel', [])),
        'tip': a.get('tip_fr', ''),
        'blocks': list(a.get('etapes_fr', [])),
        'codeJS': a.get('js', ''),
        'codePY': a.get('py', ''),
        'challenges': [
            {'t': d['text'], 'd': LEVEL_TO_DIFF.get(d.get('level', 'easy'), 1)}
            for d in a.get('defis_fr', [])
        ],
    }

def adapt_tr(a, lang):
    """TR[lang][id] entry — per-activity translated fields."""
    tr = ALL_TR.get(a['id'], {}).get(lang, {}) or {}
    return {
        't': a.get(f'title_{lang}', a['title_fr']),
        'g': tr.get('objectif', a['objectif_fr']),
        'tip': tr.get('tip', a.get('tip_fr', '')),
        'n': tr.get('materiel', a.get('materiel', [])),
        'b': tr.get('etapes', a.get('etapes_fr', [])),
        'c': [
            {'t': d['text'], 'd': LEVEL_TO_DIFF.get(d.get('level', 'easy'), 1)}
            for d in tr.get('defis', a.get('defis_fr', []))
        ],
    }

A_LIST = [adapt_activity(a) for a in ACTIVITIES]
TR = {
    'en': {a['id']: adapt_tr(a, 'en') for a in ACTIVITIES},
    'ar': {a['id']: adapt_tr(a, 'ar') for a in ACTIVITIES},
}

# ═══════════════════════════════════════════════════════════════════
# TOPICS, BADGES, ROADMAP, UI
# ═══════════════════════════════════════════════════════════════════

SIMPLE_CATS = ['start', 'officiel', 'mouvement', 'leds']
ADVANCED_CATS = ['capteurs', 'interact', 'robot', 'defis', 'ia']
ALL_SIDEBAR_CATS = SIMPLE_CATS + ADVANCED_CATS

CAT_META = {c['id']: c for c in CATS}

TOPICS = {
    cid: {'ids': [a['id'] for a in ACTIVITIES if a['cat'] == cid]}
    for cid in ALL_SIDEBAR_CATS
}

def badge_need(cid):
    n = len(TOPICS[cid]['ids'])
    return max(1, n // 2)

BADGES = []
for cid in ALL_SIDEBAR_CATS:
    m = CAT_META[cid]
    BADGES.append({
        'id': cid, 'icon': m['icon'],
        'fr': m['name_fr'], 'en': m['name_en'], 'ar': m['name_ar'],
        'topic': cid, 'need': badge_need(cid),
    })
BADGES.append({
    'id': 'master', 'icon': '🏆',
    'fr': 'Grand Maître', 'en': 'Grand Master', 'ar': 'الأستاذ الكبير',
    'topic': None, 'need': EXPECTED,
})

ROADMAP_ORDER = ALL_SIDEBAR_CATS
ROADMAP_ICONS = {c: CAT_META[c]['icon'] for c in ALL_SIDEBAR_CATS}

# UI labels (bit-48 keys), customized for maqueen.
UI = {
    'fr': {
        'title': 'Maqueen · 85 activités', 'sub': '🧩 blocs · 💻 code · 🚀 défis',
        'search': '🔍 Recherche', 'ph': 'robot, capteur, ligne, IA…',
        'part': '📂 Partie', 'diff': '⭐ Difficulté', 'status': '📊 Statut',
        'allParts': 'Toutes', 'simple': 'Simple', 'advanced': 'Avancée',
        'allDiff': 'Toutes', 'd1': '⭐ Débutant', 'd2': '⭐⭐ Inter.', 'd3': '⭐⭐⭐ Avancé',
        'allStat': 'Tous', 'todo': 'À faire', 'done': 'Fait ✅', 'fav': 'Favoris ⭐',
        'v2only': 'V2 uniquement', 'iaonly': 'IA uniquement',
        'reset': '🔄 Réinit.', 'random': '🎲 Au hasard',
        'results': 'Résultats', 'of': '/ 85', 'doneL': 'Fait', 'favL': 'Favoris',
        'tabInfo': '🎯 Info', 'tabBlocks': '🧩 Blocs', 'tabChal': '🚀 Défis',
        'needsLabel': 'Tu as besoin de :',
        'codeTip': "💡 Ouvre <strong>MakeCode</strong> → ajoute l'extension <strong>maqueen-lite</strong> → passe en <strong>JavaScript</strong>/<strong>Python</strong> → colle le code.",
        'markDone': 'Marquer Fait ✅', 'unmarkDone': 'Annuler Fait ✅',
        'markFav': 'Favori ⭐', 'unmarkFav': 'Retirer ⭐',
        'saveHint': 'Sauvegardé sur cet appareil', 'prev': '◀ Préc.', 'next': 'Suiv. ▶',
        'copied': 'Copié !', 'copyBtn': '📋 Copier',
        'resetConfirm': 'Réinitialiser la progression ?', 'resetDone': 'Progression réinitialisée',
        'noResults': 'Aucune activité trouvée.', 'simpleTag': 'Simple', 'advTag': 'Avancée',
        'chipDone': 'Fait ✅', 'chipFav': 'Favori ⭐', 'chipTodo': 'À faire', 'go': 'GO ▶',
        'sbAll': 'Tout', 'sbSimple': 'Simple', 'sbAdvanced': 'Avancé',
    },
    'en': {
        'title': 'Maqueen · 85 Activities', 'sub': '🧩 blocks · 💻 code · 🚀 challenges',
        'search': '🔍 Search', 'ph': 'robot, sensor, line, AI…',
        'part': '📂 Part', 'diff': '⭐ Difficulty', 'status': '📊 Status',
        'allParts': 'All', 'simple': 'Simple', 'advanced': 'Advanced',
        'allDiff': 'All', 'd1': '⭐ Beginner', 'd2': '⭐⭐ Inter.', 'd3': '⭐⭐⭐ Advanced',
        'allStat': 'All', 'todo': 'To do', 'done': 'Done ✅', 'fav': 'Favorites ⭐',
        'v2only': 'V2 only', 'iaonly': 'AI only',
        'reset': '🔄 Reset', 'random': '🎲 Random',
        'results': 'Results', 'of': '/ 85', 'doneL': 'Done', 'favL': 'Favorites',
        'tabInfo': '🎯 Info', 'tabBlocks': '🧩 Blocks', 'tabChal': '🚀 Challenges',
        'needsLabel': 'You need:',
        'codeTip': '💡 Open <strong>MakeCode</strong> → add the <strong>maqueen-lite</strong> extension → switch to <strong>JavaScript</strong>/<strong>Python</strong> → paste the code.',
        'markDone': 'Mark Done ✅', 'unmarkDone': 'Undo Done ✅',
        'markFav': 'Favorite ⭐', 'unmarkFav': 'Remove ⭐',
        'saveHint': 'Saved on this device', 'prev': '◀ Prev', 'next': 'Next ▶',
        'copied': 'Copied!', 'copyBtn': '📋 Copy',
        'resetConfirm': 'Reset progress?', 'resetDone': 'Progress reset',
        'noResults': 'No activity found.', 'simpleTag': 'Simple', 'advTag': 'Advanced',
        'chipDone': 'Done ✅', 'chipFav': 'Favorite ⭐', 'chipTodo': 'To do', 'go': 'GO ▶',
        'sbAll': 'All', 'sbSimple': 'Simple', 'sbAdvanced': 'Advanced',
    },
    'ar': {
        'title': 'Maqueen · 85 نشاطاً', 'sub': '🧩 مكعبات · 💻 كود · 🚀 تحديات',
        'search': '🔍 بحث', 'ph': 'روبوت، مستشعر، خط، ذكاء اصطناعي…',
        'part': '📂 القسم', 'diff': '⭐ الصعوبة', 'status': '📊 الحالة',
        'allParts': 'الكل', 'simple': 'بسيط', 'advanced': 'متقدم',
        'allDiff': 'الكل', 'd1': '⭐ مبتدئ', 'd2': '⭐⭐ متوسط', 'd3': '⭐⭐⭐ متقدم',
        'allStat': 'الكل', 'todo': 'للعمل', 'done': 'تم ✅', 'fav': 'مفضل ⭐',
        'v2only': 'V2 فقط', 'iaonly': 'ذ.إ. فقط',
        'reset': '🔄 إعادة', 'random': '🎲 عشوائي',
        'results': 'النتائج', 'of': '/ 85', 'doneL': 'تم', 'favL': 'مفضل',
        'tabInfo': '🎯 معلومات', 'tabBlocks': '🧩 المكعبات', 'tabChal': '🚀 التحديات',
        'needsLabel': 'تحتاج إلى:',
        'codeTip': '💡 افتح <strong>MakeCode</strong> ← أضف إضافة <strong>maqueen-lite</strong> ← انتقل إلى وضع <strong>JavaScript</strong>/<strong>Python</strong> ← الصق الكود.',
        'markDone': 'تم الإنجاز ✅', 'unmarkDone': 'إلغاء الإنجاز ✅',
        'markFav': 'مفضل ⭐', 'unmarkFav': 'إزالة ⭐',
        'saveHint': 'محفوظ على هذا الجهاز', 'prev': 'السابق ◀', 'next': '▶ التالي',
        'copied': 'تم النسخ!', 'copyBtn': '📋 نسخ',
        'resetConfirm': 'إعادة تعيين التقدم؟', 'resetDone': 'تمت إعادة التعيين',
        'noResults': 'لم يُعثر على نشاط.', 'simpleTag': 'بسيط', 'advTag': 'متقدم',
        'chipDone': 'تم ✅', 'chipFav': 'مفضل ⭐', 'chipTodo': 'للعمل', 'go': '▶ ابدأ',
        'sbAll': 'الكل', 'sbSimple': 'بسيط', 'sbAdvanced': 'متقدم',
    },
}
for lang in ('fr', 'en', 'ar'):
    for cid in ALL_SIDEBAR_CATS:
        UI[lang][f'sb{cid.capitalize()}'] = CAT_META[cid][f'name_{lang}']

# ═══════════════════════════════════════════════════════════════════
# HTML BODY
# ═══════════════════════════════════════════════════════════════════

def sidebar_buttons():
    out = ['        <button class="sidebar-item active" data-topic="all"><span class="sidebar-icon">📋</span><span class="sidebar-label" id="sbAll">Tout</span><span class="sidebar-count" id="sbAllC">0</span></button>']
    out.append('        <div class="sidebar-title" id="sbSimple">Simple</div>')
    for cid in SIMPLE_CATS:
        m = CAT_META[cid]
        key = f'sb{cid.capitalize()}'
        out.append(f'        <button class="sidebar-item" data-topic="{cid}"><span class="sidebar-icon">{m["icon"]}</span><span class="sidebar-label" id="{key}">{html.escape(m["name_fr"])}</span><span class="sidebar-count" id="{key}C">0</span></button>')
    out.append('        <div class="sidebar-title" id="sbAdvanced">Avancé</div>')
    for cid in ADVANCED_CATS:
        m = CAT_META[cid]
        key = f'sb{cid.capitalize()}'
        out.append(f'        <button class="sidebar-item" data-topic="{cid}"><span class="sidebar-icon">{m["icon"]}</span><span class="sidebar-label" id="{key}">{html.escape(m["name_fr"])}</span><span class="sidebar-count" id="{key}C">0</span></button>')
    out.append('        <div class="badge-shelf" id="badgeShelf"></div>')
    out.append('        <button class="sidebar-item roadmap-btn" id="roadmapBtn"><span class="sidebar-icon">🗺</span><span class="sidebar-label" id="sbRoadmap">Parcours</span></button>')
    return '\n'.join(out)

BODY = f'''
  <div class="app">
    <div class="deco-band top-band" aria-hidden="true"></div>
    <div class="rows-container">
      <div class="header">
        <div class="bismillah" aria-hidden="true"><span class="bism-ornament">&#x2726;</span>بِسْمِ ٱللَّٰهِ ٱلرَّحْمَـٰنِ ٱلرَّحِيمِ<span class="bism-ornament">&#x2726;</span></div>
        <div class="title-block">
          <div class="logo-wrap" id="logoWrap"></div>
          <div>
            <h1 id="mainTitle">Maqueen · 85 activités</h1>
            <div class="subtitle" id="mainSub">🧩 blocs · 💻 code · 🚀 défis</div>
          </div>
        </div>
        <div class="header-right">
          <div class="header-dropdowns">
            <select id="langSelect" class="mini-select" aria-label="Language">
              <option value="fr" selected>FR</option>
              <option value="en">EN</option>
              <option value="ar">عربي</option>
            </select>
            <select id="themeSelect" class="mini-select" aria-label="Theme">
              <option value="robot" selected>Robot</option><option value="space">Space</option><option value="jungle">Jungle</option>
              <option value="mosque-gold">Mosque</option><option value="zellige">Zellige</option><option value="andalus">Andalus</option>
            </select>
          </div>
          <div class="status-pill"><span class="status-dot"></span><span id="statsText">0 / {EXPECTED}</span></div>
          <button onclick="window.print()" aria-label="Export / Print" style="font-size:.7rem;padding:4px 10px">&#128214; Export</button>
          <button class="sidebar-toggle" id="sidebarToggle" aria-label="Menu">☰</button>
        </div>
      </div>

    </div><!-- /rows-container (header only) -->
    <div class="sidebar-overlay" id="sidebarOverlay"></div>
    <div class="app-body">
      <nav class="sidebar" id="sidebar">
{sidebar_buttons()}
      </nav>
      <div class="main-area">
      <div class="controls-bar">
        <div class="ctrl-group"><label for="searchInput" id="lSearch">🔍 Recherche</label><input id="searchInput" type="search" placeholder="" /></div>
        <div class="ctrl-group"><label for="partSelect" id="lPart">📂 Partie</label><select id="partSelect"><option value="all" id="optAllParts"></option><option value="simple" id="optSimple"></option><option value="advanced" id="optAdv"></option></select></div>
        <div class="ctrl-group"><label for="diffSelect" id="lDiff">⭐ Difficulté</label><select id="diffSelect"><option value="all" id="optAllDiff"></option><option value="1" id="optD1"></option><option value="2" id="optD2"></option><option value="3" id="optD3"></option></select></div>
        <div class="ctrl-group"><label for="statusSelect" id="lStatus">📊 Statut</label><select id="statusSelect"><option value="all" id="optAllStat"></option><option value="todo" id="optTodo"></option><option value="done" id="optDone"></option><option value="fav" id="optFav"></option></select></div>
      </div>

      <div class="options-row">
        <label class="pill-opt"><input id="onlyV2" type="checkbox" /> <span id="lV2">V2 uniquement</span></label>
        <label class="pill-opt"><input id="onlyIA" type="checkbox" /> <span id="lIA">IA uniquement</span></label>
        <button class="btn-sm" id="resetBtn"><span id="lReset">🔄 Réinit.</span></button>
        <button class="btn-sm" id="randomBtn"><span id="lRandom">🎲 Au hasard</span></button>
      </div>

      <div class="stats-row" id="statsRow"></div>
      <div class="activity-grid" id="grid"></div>
      </div><!-- /main-area -->
    </div><!-- /app-body -->
    <div class="deco-band bottom-band" aria-hidden="true"></div>
  </div>

  <!-- MODAL -->
  <div class="modal-overlay" id="overlay">
    <div class="modal" id="modal" role="dialog" aria-modal="true" aria-labelledby="mTitle">
      <div class="modal-head"><div><h2 id="mTitle"></h2><div class="tags" id="mTags"></div></div><button class="close-btn" id="closeBtn">✕</button></div>
      <div class="tab-bar" id="tabBar">
        <button class="tab-btn active" data-tab="info" id="tabInfo">🎯 Info</button>
        <button class="tab-btn" data-tab="sim" id="tabSim">▶ Simulateur</button>
        <button class="tab-btn" data-tab="blocks" id="tabBlocks">🧩 Blocs</button>
        <button class="tab-btn" data-tab="js" id="tabJS"><span class="tab-lang-badge js-badge">JS</span> JavaScript</button>
        <button class="tab-btn" data-tab="py" id="tabPY"><span class="tab-lang-badge py-badge">PY</span> Python</button>
        <button class="tab-btn" data-tab="challenges" id="tabChal">🚀 Défis</button>
      </div>
      <div class="tab-panel active" id="tab-info">
        <div class="info-meta" id="infoMeta"></div>
        <div class="info-section"><div class="info-section-title" id="infoGoalTitle">🎯 Objectif</div><div class="goal-text" id="mGoal"></div></div>
        <div class="info-section"><div class="info-section-title" id="infoConceptTitle">💡 Concept</div><div class="info-concept" id="mConcept"></div></div>
        <div class="info-section"><div class="info-section-title" id="infoStepsTitle">📋 Étapes</div><div class="info-steps" id="mSteps"></div></div>
        <div class="info-section"><div class="info-section-title" id="infoDiagramTitle">📐 Schéma</div><div class="info-diagram" id="mDiagram"></div></div>
        <div class="info-section"><div class="info-section-title" id="infoFlowTitle">🔀 Algorithme</div><div class="info-flow" id="mFlow"></div></div>
        <div class="info-section"><div class="info-section-title" id="infoPseudoTitle">📝 Pseudo-code</div><pre class="info-pseudo" id="mPseudo"></pre></div>
        <div class="info-section"><div class="info-section-title" id="infoBlocksTitle">🧩 Blocs utilisés</div><div class="info-blocks-used" id="mBlocksUsed"></div></div>
        <div class="info-section"><div class="info-section-title" id="infoCodeTitle">💻 Instructions</div><div class="info-code-keys" id="mCodeKeys"></div></div>
        <div class="info-section"><div class="info-section-title" id="mNeedsLabel">🧰 Matériel</div><ul class="needs-list" id="mNeeds"></ul></div>
        <div class="tip-box" id="mTip"></div>
        <div class="qr-section" id="qrSection"></div>
      </div>
      <div class="tab-panel" id="tab-sim">
        <div class="sim-container">
          <div class="sim-actions"><button class="sim-run-btn" id="simRunBtn">▶ Lancer</button><button class="sim-stop-btn" id="simStopBtn">⏹ Arrêter</button></div>
          <iframe id="simFrame" class="sim-iframe hidden" allow="usb; autoplay; camera; microphone"></iframe>
          <div class="sim-hint" id="simHint">Clique sur ▶ pour lancer le simulateur micro:bit</div>
        </div>
      </div>
      <div class="tab-panel" id="tab-blocks">
        <div class="blocks-sync-bar" id="blocksSyncBar"><span class="sync-status synced" id="syncStatus">✅ Synced</span><button class="sync-btn" id="syncBlocksBtn">🔄 Actualiser</button><button class="open-makecode-btn" id="openMCBlocks">🧩 Modifier dans MakeCode</button></div>
        <div id="mBlocksMC" class="makecode-blocks"></div>
        <div id="mBlocksFallback" style="display:none"></div>
      </div>
      <div class="tab-panel" id="tab-js">
        <div class="code-actions"><button class="copy-btn" id="copyJSBtn">📋 Copier</button><button class="open-makecode-btn" id="openMCJS">🚀 Ouvrir MakeCode</button></div>
        <pre class="code-editor" id="codeBlockJS" contenteditable="true" spellcheck="false"></pre>
        <div class="tip-box" style="margin-top:10px;border-color:rgba(122,167,255,.3);color:rgba(122,167,255,.9);background:rgba(122,167,255,.05)" id="codeTip"></div>
      </div>
      <div class="tab-panel" id="tab-py">
        <div class="code-actions"><button class="copy-btn" id="copyPYBtn">📋 Copier</button><button class="open-makecode-btn" id="openMCPY">🐍 Ouvrir MakeCode</button></div>
        <pre class="code-editor" id="codeBlockPY" contenteditable="true" spellcheck="false"></pre>
        <div class="tip-box" style="margin-top:10px;border-color:rgba(48,105,152,.4);color:rgba(255,212,59,.9);background:rgba(48,105,152,.08)" id="codeTipPY"></div>
      </div>
      <div class="tab-panel" id="tab-challenges"><div id="mChallenges"></div></div>
      <div class="modal-actions">
        <div class="left"><button id="markDoneBtn"></button><button id="markFavBtn"></button><span class="hint-text" id="saveHint"></span></div>
        <div class="right"><button id="prevBtn"></button><button id="nextBtn"></button></div>
      </div>
    </div>
  </div>

  <!-- ROADMAP OVERLAY -->
  <div class="roadmap-overlay" id="roadmapOverlay">
    <div class="roadmap-panel">
      <div class="roadmap-header"><h2 id="roadmapTitle">🗺 Parcours d'apprentissage</h2><button class="close-btn" id="closeRoadmap">✕</button></div>
      <div class="roadmap-body" id="roadmapBody"></div>
    </div>
  </div>

  <!-- MakeCode block rendering iframe (hidden) -->
  <iframe id="mcRenderFrame" src="https://makecode.microbit.org/--docs?render=1" style="position:absolute;width:1px;height:1px;border:0;opacity:0;pointer-events:none" sandbox="allow-scripts allow-same-origin"></iframe>

  <div id="toast" class="toast-indicator"><div class="toast-inner"><div class="toast-text" id="toastMsg"></div></div></div>
'''

HEAD = '''
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Maqueen · 85 activités — Workshop DIY</title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect x='4' y='8' width='24' height='16' rx='3' fill='%239400D3'/><circle cx='11' cy='16' r='2.5' fill='%23fff'/><circle cx='21' cy='16' r='2.5' fill='%23fff'/><rect x='14' y='14' width='4' height='4' rx='1' fill='%23fff' opacity='.6'/></svg>" type="image/svg+xml" />
  <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Righteous&family=Tajawal:wght@400;500;700&family=Bangers&family=Orbitron:wght@500;700&display=swap" rel="stylesheet" />
'''

# ═══════════════════════════════════════════════════════════════════
# SCRIPT SUBSTITUTION
# ═══════════════════════════════════════════════════════════════════

def jsd(v):
    return json.dumps(v, ensure_ascii=False)

script = SCRIPT
script = script.replace('__UI__', jsd(UI))
script = script.replace('__ACTIVITIES__', jsd(A_LIST))
script = script.replace('__BT__', '{}')
script = script.replace('__TR__', jsd(TR))
script = script.replace('__BADGES__', jsd(BADGES))
script = script.replace('__TOPICS__', jsd(TOPICS))
script = script.replace('__ROADMAP_ORDER__', jsd(ROADMAP_ORDER))
script = script.replace('__ROADMAP_ICONS__', jsd(ROADMAP_ICONS))

for p in ('__UI__','__ACTIVITIES__','__BT__','__TR__','__BADGES__','__TOPICS__','__ROADMAP_ORDER__','__ROADMAP_ICONS__'):
    assert p not in script, f"Unfilled placeholder: {p}"

# ═══════════════════════════════════════════════════════════════════
# ASSEMBLE
# ═══════════════════════════════════════════════════════════════════

HTML = f'''<!doctype html>
<html lang="fr" dir="ltr" data-theme="robot">
<head>{HEAD}<style>{CSS}</style></head>
<body>{BODY}
<script>{script}</script>
</body>
</html>
'''

out = pathlib.Path(__file__).resolve().parent.parent / 'index.html'
out.write_text(HTML, encoding='utf-8')
print(f"Wrote {out} ({len(HTML):,} chars, {len(HTML)/1024:.1f} KB)")
