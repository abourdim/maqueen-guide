#!/usr/bin/env python3
"""JavaScript runtime for Maqueen guide."""

def js_template(activities_json, i18n_json):
    return r"""
// ═══════════════════════════════════════════════════════════════
//   DATA
// ═══════════════════════════════════════════════════════════════
const ACTIVITIES = __ACTIVITIES__;
const I18N = __I18N__;

// ═══════════════════════════════════════════════════════════════
//   STATE
// ═══════════════════════════════════════════════════════════════
const STATE = {
  lang: localStorage.getItem('mq-lang') || 'fr',
  theme: localStorage.getItem('mq-theme') || 'mosque',
  sound: localStorage.getItem('mq-sound') !== '0',
  done: new Set(JSON.parse(localStorage.getItem('mq-done') || '[]')),
  currentId: null,
  konami: [],
};
const KONAMI_SEQ = ['ArrowUp','ArrowUp','ArrowDown','ArrowDown','ArrowLeft','ArrowRight','ArrowLeft','ArrowRight','b','a'];

// ═══════════════════════════════════════════════════════════════
//   I18N
// ═══════════════════════════════════════════════════════════════
function t(key) {
  return (I18N[STATE.lang] && I18N[STATE.lang][key]) || I18N.fr[key] || key;
}

function applyLang() {
  document.documentElement.lang = STATE.lang;
  document.documentElement.dir = STATE.lang === 'ar' ? 'rtl' : 'ltr';
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    el.textContent = t(key);
  });
  document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
    el.placeholder = t(el.getAttribute('data-i18n-placeholder'));
  });
  document.querySelectorAll('.flag').forEach(f => f.classList.toggle('active', f.dataset.lang === STATE.lang));
  renderActivityTitles();
  localStorage.setItem('mq-lang', STATE.lang);
}

function renderActivityTitles() {
  // Titles are now rendered in all 3 languages via [lang] attributes.
  // CSS handles visibility — no-op here.
}

// ═══════════════════════════════════════════════════════════════
//   THEME
// ═══════════════════════════════════════════════════════════════
const THEMES = [
  { id:'mosque',  name:'Mosque',  dot:'#d4af37', hidden:false },
  { id:'zellige', name:'Zellige', dot:'#a855f7', hidden:false },
  { id:'andalus', name:'Andalus', dot:'#10b981', hidden:false },
  { id:'space',   name:'Space',   dot:'#a855f7', hidden:false },
  { id:'jungle',  name:'Jungle',  dot:'#84cc16', hidden:false },
  { id:'robot',   name:'Robot',   dot:'#60a5fa', hidden:false },
  { id:'riad',    name:'Riad',    dot:'#c2783c', hidden:false },
  { id:'medina',  name:'Medina',  dot:'#0f766e', hidden:false },
  { id:'retro',   name:'Retro',   dot:'#00ff41', hidden:true  },
];
const THEME_MELODIES = {
  mosque: [329.63, 392.00, 523.25],
  zellige: [440.00, 523.25, 659.25],
  andalus: [293.66, 369.99, 440.00],
  space: [523.25, 659.25, 783.99],
  jungle: [261.63, 329.63, 392.00],
  robot: [440.00, 554.37, 659.25],
  riad: [349.23, 440.00, 523.25],
  medina: [293.66, 349.23, 440.00],
  retro: [523.25, 261.63, 523.25],
};
function applyTheme() {
  document.documentElement.setAttribute('data-theme', STATE.theme);
  document.querySelectorAll('.theme-swatch').forEach(s => {
    s.classList.toggle('active', s.dataset.theme === STATE.theme);
  });
  localStorage.setItem('mq-theme', STATE.theme);
}

function unlockRetro() {
  const swatch = document.querySelector('[data-theme="retro"]');
  if (swatch) swatch.style.display = '';
  STATE.theme = 'retro';
  applyTheme();
  playMelody('retro');
  toast('🕹️ Retro theme unlocked!');
}

// ═══════════════════════════════════════════════════════════════
//   SOUND (Web Audio)
// ═══════════════════════════════════════════════════════════════
let audioCtx = null;
function getAudio() {
  if (!audioCtx) {
    try { audioCtx = new (window.AudioContext || window.webkitAudioContext)(); }
    catch(e) { return null; }
  }
  return audioCtx;
}
function beep(freq=800, dur=100, vol=0.08) {
  if (!STATE.sound) return;
  const ctx = getAudio(); if (!ctx) return;
  const osc = ctx.createOscillator();
  const gain = ctx.createGain();
  osc.frequency.value = freq;
  osc.type = 'sine';
  gain.gain.setValueAtTime(vol, ctx.currentTime);
  gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + dur/1000);
  osc.connect(gain); gain.connect(ctx.destination);
  osc.start(); osc.stop(ctx.currentTime + dur/1000);
}
function playMelody(themeId) {
  const notes = THEME_MELODIES[themeId] || THEME_MELODIES.mosque;
  notes.forEach((f, i) => setTimeout(() => beep(f, 150, 0.06), i * 140));
}
function successChime() { beep(523.25, 120, 0.06); setTimeout(()=>beep(659.25, 180, 0.06), 100); }

// ═══════════════════════════════════════════════════════════════
//   ROUTING
// ═══════════════════════════════════════════════════════════════
function gotoActivity(id, scroll = true) {
  STATE.currentId = id;
  document.querySelectorAll('.nav-link').forEach(l => {
    l.classList.toggle('active', parseInt(l.dataset.id) === id);
  });
  if (scroll) {
    const el = document.getElementById('act-' + id);
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
  history.replaceState(null, '', '#act-' + id);
  closeMobileSidebar();
}

function gotoCover() {
  STATE.currentId = null;
  document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
  const el = document.getElementById('cover');
  if (el) el.scrollIntoView({ behavior: 'smooth' });
  history.replaceState(null, '', '#');
}

// ═══════════════════════════════════════════════════════════════
//   PROGRESS
// ═══════════════════════════════════════════════════════════════
function toggleDone(id) {
  if (STATE.done.has(id)) STATE.done.delete(id);
  else { STATE.done.add(id); successChime(); glowBismillah(); petBounce(); }
  localStorage.setItem('mq-done', JSON.stringify([...STATE.done]));
  updateProgress();
}
function updateProgress() {
  const done = STATE.done.size;
  const total = ACTIVITIES.length;
  const el = document.querySelector('.progress-pill .count');
  if (el) el.textContent = done + '/' + total;
  document.querySelectorAll('.nav-link').forEach(l => {
    const id = parseInt(l.dataset.id);
    l.classList.toggle('done', STATE.done.has(id));
  });
  ACTIVITIES.forEach(a => {
    const btn = document.querySelector('#act-' + a.id + ' .done-btn');
    if (!btn) return;
    const isDone = STATE.done.has(a.id);
    btn.classList.toggle('done', isDone);
    btn.textContent = isDone ? '✓ ' + t('done_label') : t('mark_done');
  });
}

// ═══════════════════════════════════════════════════════════════
//   COMMAND PALETTE (⌘K)
// ═══════════════════════════════════════════════════════════════
function openCmdK() {
  const overlay = document.getElementById('cmdk-overlay');
  const input = document.getElementById('cmdk-input');
  overlay.classList.add('open');
  input.value = '';
  input.focus();
  renderCmdKResults('');
}
function closeCmdK() {
  document.getElementById('cmdk-overlay').classList.remove('open');
}
function renderCmdKResults(q) {
  const results = document.getElementById('cmdk-results');
  const query = q.toLowerCase().trim();
  const matches = ACTIVITIES.filter(a => {
    if (!query) return true;
    const title = (a['title_' + STATE.lang] || a.title_fr).toLowerCase();
    const obj = (a.objectif_fr || '').toLowerCase();
    return title.includes(query) || obj.includes(query) || ('' + a.id).includes(query);
  }).slice(0, 20);
  if (!matches.length) {
    results.innerHTML = `<div class="cmdk-empty">${t('no_results')}</div>`;
    return;
  }
  results.innerHTML = matches.map((a, i) => `
    <div class="cmdk-item ${i===0?'sel':''}" data-id="${a.id}">
      <span class="cmdk-item-icon">${a.official ? '📘' : '✨'}</span>
      <span class="cmdk-item-title">${a.id}. ${a['title_' + STATE.lang] || a.title_fr}</span>
      <span class="cmdk-item-meta">${a.time} · ${'★'.repeat(a.stars)}</span>
    </div>
  `).join('');
  results.querySelectorAll('.cmdk-item').forEach(el => {
    el.onclick = () => { gotoActivity(parseInt(el.dataset.id)); closeCmdK(); };
  });
}

// ═══════════════════════════════════════════════════════════════
//   PANELS (settings)
// ═══════════════════════════════════════════════════════════════
function togglePanel(id) {
  const p = document.getElementById(id);
  if (!p) return;
  const wasOpen = p.classList.contains('open');
  document.querySelectorAll('.panel').forEach(x => x.classList.remove('open'));
  if (!wasOpen) p.classList.add('open');
}
function closeAllPanels() {
  document.querySelectorAll('.panel').forEach(p => p.classList.remove('open'));
}

// ═══════════════════════════════════════════════════════════════
//   MOBILE
// ═══════════════════════════════════════════════════════════════
function toggleMobileSidebar() {
  document.getElementById('sidebar').classList.toggle('open');
  document.getElementById('mobile-overlay').classList.toggle('show');
}
function closeMobileSidebar() {
  document.getElementById('sidebar').classList.remove('open');
  document.getElementById('mobile-overlay').classList.remove('show');
}

// ═══════════════════════════════════════════════════════════════
//   UI HELPERS
// ═══════════════════════════════════════════════════════════════
function toast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg; t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2400);
}
function glowBismillah() {
  const b = document.querySelector('.bismillah-bar');
  if (!b) return;
  b.classList.add('glow');
  setTimeout(() => b.classList.remove('glow'), 1500);
}
function petBounce() {
  const pet = document.querySelector('.pet');
  if (!pet) return;
  pet.classList.add('happy');
  setTimeout(() => pet.classList.remove('happy'), 700);
}
function copyCode(btn) {
  const code = btn.closest('.code-panel').querySelector('.code-block');
  const text = code.textContent;
  navigator.clipboard.writeText(text).then(() => {
    const orig = btn.innerHTML;
    btn.innerHTML = '✓ ' + t('copied');
    beep(880, 80, 0.05);
    setTimeout(() => btn.innerHTML = orig, 1500);
  });
}
function openMakeCode(lang) {
  window.open('https://makecode.microbit.org/?search=maqueen', '_blank');
}

// ═══════════════════════════════════════════════════════════════
//   HIJRI DATE (approx)
// ═══════════════════════════════════════════════════════════════
function hijriDate() {
  const gregorian = new Date();
  // Umm al-Qura-ish approximation: Hijri = (Gregorian - 622) * 1.0307
  const diffYears = gregorian.getFullYear() - 622;
  const hYear = Math.floor(diffYears * 33 / 32) + 1;
  const months = ['محرم','صفر','ربيع الأول','ربيع الآخر','جمادى الأولى','جمادى الآخرة','رجب','شعبان','رمضان','شوال','ذو القعدة','ذو الحجة'];
  const hMonth = months[(gregorian.getMonth() + 10) % 12];
  return hMonth + ' ' + hYear;
}

// ═══════════════════════════════════════════════════════════════
//   INIT
// ═══════════════════════════════════════════════════════════════
function init() {
  applyTheme();
  applyLang();
  updateProgress();

  // Hijri date
  const hd = document.querySelector('.hijri-date');
  if (hd) hd.textContent = hijriDate();

  // Hide retro theme by default
  const retroSwatch = document.querySelector('[data-theme="retro"]');
  if (retroSwatch && STATE.theme !== 'retro') retroSwatch.style.display = 'none';

  // Nav section collapse
  document.querySelectorAll('.nav-section').forEach(sec => {
    sec.onclick = () => {
      const targetId = sec.dataset.target;
      const group = document.getElementById(targetId);
      sec.classList.toggle('open');
      group.classList.toggle('open');
    };
  });

  // Nav links
  document.querySelectorAll('.nav-link').forEach(l => {
    l.onclick = e => {
      e.preventDefault();
      gotoActivity(parseInt(l.dataset.id));
      beep(800, 40, 0.03);
    };
  });

  // Flag click
  document.querySelectorAll('.flag').forEach(f => {
    f.onclick = () => {
      STATE.lang = f.dataset.lang;
      applyLang();
      beep(660, 80, 0.04);
    };
  });

  // Theme swatch click
  document.querySelectorAll('.theme-swatch').forEach(s => {
    s.onclick = () => {
      STATE.theme = s.dataset.theme;
      applyTheme();
      playMelody(STATE.theme);
    };
  });

  // Sound toggle
  const soundToggle = document.getElementById('sound-toggle');
  if (soundToggle) {
    soundToggle.classList.toggle('on', STATE.sound);
    soundToggle.onclick = () => {
      STATE.sound = !STATE.sound;
      soundToggle.classList.toggle('on', STATE.sound);
      localStorage.setItem('mq-sound', STATE.sound ? '1' : '0');
      if (STATE.sound) beep(800, 100);
    };
  }

  // Topbar buttons
  document.getElementById('btn-cmdk').onclick = () => { openCmdK(); beep(700, 50, 0.04); };
  document.getElementById('btn-settings').onclick = () => togglePanel('panel-settings');
  const btnParcours = document.getElementById('btn-parcours');
  if (btnParcours) btnParcours.onclick = () => togglePanel('panel-parcours');
  const btnResources = document.getElementById('btn-resources');
  if (btnResources) btnResources.onclick = () => togglePanel('panel-resources');
  const btnHelp = document.getElementById('btn-help');
  if (btnHelp) btnHelp.onclick = () => togglePanel('panel-help');
  const btnRandom = document.getElementById('btn-random');
  if (btnRandom) btnRandom.onclick = () => {
    const a = ACTIVITIES[Math.floor(Math.random() * ACTIVITIES.length)];
    gotoActivity(a.id);
    toast('🎲 ' + a['title_' + STATE.lang]);
    beep(800, 80, 0.04);
  };
  document.getElementById('btn-home').onclick = () => gotoCover();

  // Help panel tabs
  document.querySelectorAll('.help-tab').forEach(tab => {
    tab.onclick = () => {
      const target = tab.dataset.tab;
      document.querySelectorAll('.help-tab').forEach(t => t.classList.toggle('active', t === tab));
      document.querySelectorAll('.help-content').forEach(c => {
        c.classList.toggle('active', c.classList.contains('help-' + target));
      });
    };
  });

  // Mobile toggle
  const mt = document.getElementById('mobile-toggle');
  if (mt) mt.onclick = toggleMobileSidebar;
  const mo = document.getElementById('mobile-overlay');
  if (mo) mo.onclick = closeMobileSidebar;

  // Panel close buttons
  document.querySelectorAll('.panel-close').forEach(b => {
    b.onclick = () => closeAllPanels();
  });

  // Done buttons
  document.querySelectorAll('.done-btn').forEach(b => {
    b.onclick = () => {
      const id = parseInt(b.dataset.id);
      toggleDone(id);
    };
  });

  // Copy buttons
  document.querySelectorAll('.copy-btn').forEach(b => {
    b.onclick = () => copyCode(b);
  });

  // Cmd-K input
  const cmdkInput = document.getElementById('cmdk-input');
  cmdkInput.oninput = () => renderCmdKResults(cmdkInput.value);
  cmdkInput.onkeydown = e => {
    const items = document.querySelectorAll('.cmdk-item');
    const sel = document.querySelector('.cmdk-item.sel');
    let idx = [...items].indexOf(sel);
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      if (sel) sel.classList.remove('sel');
      idx = (idx + 1) % items.length;
      items[idx]?.classList.add('sel');
      items[idx]?.scrollIntoView({ block: 'nearest' });
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      if (sel) sel.classList.remove('sel');
      idx = idx <= 0 ? items.length - 1 : idx - 1;
      items[idx]?.classList.add('sel');
      items[idx]?.scrollIntoView({ block: 'nearest' });
    } else if (e.key === 'Enter') {
      e.preventDefault();
      if (sel) {
        gotoActivity(parseInt(sel.dataset.id));
        closeCmdK();
      }
    } else if (e.key === 'Escape') {
      closeCmdK();
    }
  };
  document.getElementById('cmdk-overlay').onclick = e => {
    if (e.target === document.getElementById('cmdk-overlay')) closeCmdK();
  };

  // Global keyboard
  document.addEventListener('keydown', e => {
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
      e.preventDefault();
      openCmdK();
    } else if (e.key === 'Escape') {
      closeCmdK(); closeAllPanels();
    }

    // Konami code
    STATE.konami.push(e.key.toLowerCase() === 'b' || e.key.toLowerCase() === 'a' ? e.key.toLowerCase() : e.key);
    if (STATE.konami.length > KONAMI_SEQ.length) STATE.konami.shift();
    if (STATE.konami.length === KONAMI_SEQ.length
        && STATE.konami.every((k, i) => k === KONAMI_SEQ[i])) {
      unlockRetro();
      STATE.konami = [];
    }
  });

  // Scroll spy
  const obsr = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        const id = e.target.id;
        if (id && id.startsWith('act-')) {
          const actId = parseInt(id.slice(4));
          document.querySelectorAll('.nav-link').forEach(l => {
            l.classList.toggle('active', parseInt(l.dataset.id) === actId);
          });
          STATE.currentId = actId;
        }
      }
    });
  }, { rootMargin: '-30% 0px -60% 0px', threshold: 0 });
  document.querySelectorAll('.act-section').forEach(s => obsr.observe(s));

  // Hash on load
  if (location.hash.startsWith('#act-')) {
    const id = parseInt(location.hash.slice(5));
    if (!isNaN(id)) setTimeout(() => gotoActivity(id), 100);
  }

  // Pet click easter egg
  const pet = document.querySelector('.pet');
  if (pet) {
    let clicks = 0;
    pet.onclick = () => {
      clicks++;
      petBounce();
      beep(500 + clicks * 100, 80, 0.04);
      if (clicks === 10) toast('🎉 ' + t('pet_loves_you'));
    };
  }

  // Splash hide
  setTimeout(() => {
    document.querySelector('.splash')?.classList.add('hide');
  }, 2500);
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}
"""
