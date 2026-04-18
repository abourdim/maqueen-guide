#!/usr/bin/env python3
"""CSS for Maqueen guide — bit-58 + Workshop-DIY hybrid."""

CSS = r"""
/* ═══════════════════════════════════════════════════════════════ */
/*   MULTILANG — hide non-active language content                    */
/* ═══════════════════════════════════════════════════════════════ */
html[lang="fr"] [lang]:not([lang="fr"]) { display: none !important; }
html[lang="en"] [lang]:not([lang="en"]) { display: none !important; }
html[lang="ar"] [lang]:not([lang="ar"]) { display: none !important; }

/* ═══════════════════════════════════════════════════════════════ */
/*   RESET & BASE                                                    */
/* ═══════════════════════════════════════════════════════════════ */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; scroll-padding-top: 20px; }
body {
  font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
  background: var(--bg);
  color: var(--fg);
  line-height: 1.65;
  font-size: 15px;
  overflow-x: hidden;
  transition: background 0.3s, color 0.3s;
}
[dir="rtl"] { font-family: 'Amiri', system-ui, serif; }
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--track); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: var(--accent); }

/* ═══════════════════════════════════════════════════════════════ */
/*   THEMES — 9                                                      */
/* ═══════════════════════════════════════════════════════════════ */
:root,
[data-theme="mosque"] {
  --bg: #0a0f1e; --fg: #d0ddf0;
  --panel: rgba(8, 12, 28, 0.95); --panel-border: rgba(59, 130, 246, 0.15);
  --card: rgba(255, 255, 255, 0.03); --card-border: rgba(255, 255, 255, 0.06);
  --accent: #d4af37; --accent-soft: rgba(212, 175, 55, 0.12);
  --accent2: #3b82f6; --accent2-soft: rgba(59, 130, 246, 0.08);
  --muted: #7a8aaa; --faint: #3a4a6a; --track: #1e2a4a;
  --code-bg: rgba(0, 0, 0, 0.35); --code-border: rgba(255, 255, 255, 0.05);
  --success: #40BF4A; --warn: #eab308; --danger: #DC143C;
}
[data-theme="zellige"] {
  --bg: #0d0a20; --fg: #ddd0ef;
  --panel: rgba(10, 8, 25, 0.95); --panel-border: rgba(147, 51, 234, 0.18);
  --card: rgba(255, 255, 255, 0.03); --card-border: rgba(255, 255, 255, 0.06);
  --accent: #a855f7; --accent-soft: rgba(168, 85, 247, 0.12);
  --accent2: #60a5fa; --accent2-soft: rgba(96, 165, 250, 0.08);
  --muted: #8a7aaa; --faint: #4a3a6a; --track: #2a1e4a;
  --code-bg: rgba(0, 0, 0, 0.35); --code-border: rgba(255, 255, 255, 0.05);
  --success: #40BF4A; --warn: #eab308; --danger: #DC143C;
}
[data-theme="andalus"] {
  --bg: #0a1a14; --fg: #d0f0dd;
  --panel: rgba(8, 20, 16, 0.95); --panel-border: rgba(52, 211, 153, 0.18);
  --card: rgba(255, 255, 255, 0.03); --card-border: rgba(255, 255, 255, 0.06);
  --accent: #10b981; --accent-soft: rgba(16, 185, 129, 0.12);
  --accent2: #d4af37; --accent2-soft: rgba(212, 175, 55, 0.08);
  --muted: #7aaa8a; --faint: #3a6a4a; --track: #1e4a2a;
  --code-bg: rgba(0, 0, 0, 0.35); --code-border: rgba(255, 255, 255, 0.05);
  --success: #40BF4A; --warn: #eab308; --danger: #DC143C;
}
[data-theme="space"] {
  --bg: #050014; --fg: #e0d0f0;
  --panel: rgba(5, 0, 20, 0.95); --panel-border: rgba(168, 85, 247, 0.2);
  --card: rgba(255, 255, 255, 0.03); --card-border: rgba(255, 255, 255, 0.06);
  --accent: #a855f7; --accent-soft: rgba(168, 85, 247, 0.12);
  --accent2: #22d3ee; --accent2-soft: rgba(34, 211, 238, 0.08);
  --muted: #7a7aaa; --faint: #3a3a6a; --track: #1e1e4a;
  --code-bg: rgba(0, 0, 0, 0.4); --code-border: rgba(255, 255, 255, 0.05);
  --success: #40BF4A; --warn: #eab308; --danger: #DC143C;
}
[data-theme="jungle"] {
  --bg: #0a1a0a; --fg: #d0f0c0;
  --panel: rgba(8, 25, 8, 0.95); --panel-border: rgba(132, 204, 22, 0.2);
  --card: rgba(255, 255, 255, 0.03); --card-border: rgba(255, 255, 255, 0.06);
  --accent: #84cc16; --accent-soft: rgba(132, 204, 22, 0.12);
  --accent2: #fb923c; --accent2-soft: rgba(251, 146, 60, 0.08);
  --muted: #7aaa6a; --faint: #3a6a2a; --track: #1e4a1e;
  --code-bg: rgba(0, 0, 0, 0.35); --code-border: rgba(255, 255, 255, 0.05);
  --success: #40BF4A; --warn: #eab308; --danger: #DC143C;
}
[data-theme="robot"] {
  --bg: #050a18; --fg: #c0d0e0;
  --panel: rgba(5, 10, 24, 0.95); --panel-border: rgba(59, 130, 246, 0.2);
  --card: rgba(255, 255, 255, 0.03); --card-border: rgba(255, 255, 255, 0.06);
  --accent: #60a5fa; --accent-soft: rgba(96, 165, 250, 0.12);
  --accent2: #fb923c; --accent2-soft: rgba(251, 146, 60, 0.08);
  --muted: #6a7a8a; --faint: #2a3a4a; --track: #1e2a3a;
  --code-bg: rgba(0, 0, 0, 0.4); --code-border: rgba(255, 255, 255, 0.05);
  --success: #40BF4A; --warn: #eab308; --danger: #DC143C;
}
[data-theme="riad"] {
  --bg: #fdf6e8; --fg: #3a2a1a;
  --panel: rgba(255, 250, 240, 0.95); --panel-border: rgba(194, 120, 60, 0.2);
  --card: rgba(255, 255, 255, 0.6); --card-border: rgba(194, 120, 60, 0.15);
  --accent: #c2783c; --accent-soft: rgba(194, 120, 60, 0.08);
  --accent2: #8b5a2b; --accent2-soft: rgba(139, 90, 43, 0.08);
  --muted: #8a6a4a; --faint: #ba9a7a; --track: #eadab0;
  --code-bg: rgba(0, 0, 0, 0.04); --code-border: rgba(0, 0, 0, 0.08);
  --success: #16a34a; --warn: #b45309; --danger: #b91c1c;
}
[data-theme="medina"] {
  --bg: #f0f9f6; --fg: #1a3a2a;
  --panel: rgba(240, 250, 245, 0.95); --panel-border: rgba(20, 184, 166, 0.2);
  --card: rgba(255, 255, 255, 0.6); --card-border: rgba(20, 184, 166, 0.12);
  --accent: #0f766e; --accent-soft: rgba(15, 118, 110, 0.06);
  --accent2: #0891b2; --accent2-soft: rgba(8, 145, 178, 0.06);
  --muted: #4a7a6a; --faint: #8abab0; --track: #cae0da;
  --code-bg: rgba(0, 0, 0, 0.04); --code-border: rgba(0, 0, 0, 0.08);
  --success: #16a34a; --warn: #b45309; --danger: #b91c1c;
}
[data-theme="retro"] {
  --bg: #000000; --fg: #00ff41;
  --panel: rgba(0, 20, 5, 0.95); --panel-border: rgba(0, 255, 65, 0.25);
  --card: rgba(0, 255, 65, 0.04); --card-border: rgba(0, 255, 65, 0.15);
  --accent: #00ff41; --accent-soft: rgba(0, 255, 65, 0.12);
  --accent2: #00ff41; --accent2-soft: rgba(0, 255, 65, 0.08);
  --muted: #00aa2a; --faint: #004410; --track: #002010;
  --code-bg: rgba(0, 0, 0, 0.6); --code-border: rgba(0, 255, 65, 0.15);
  --success: #00ff41; --warn: #eab308; --danger: #ff003c;
  font-family: 'Courier New', monospace !important;
}
[data-theme="retro"] body,
[data-theme="retro"] * {
  font-family: 'Courier New', monospace !important;
  text-shadow: 0 0 2px currentColor;
}
[data-theme="retro"]::before {
  content: ''; position: fixed; inset: 0;
  background: linear-gradient(rgba(0,0,0,0) 50%, rgba(0,40,10,0.1) 50%);
  background-size: 100% 3px; pointer-events: none; z-index: 9999;
}

/* ═══════════════════════════════════════════════════════════════ */
/*   SPLASH                                                          */
/* ═══════════════════════════════════════════════════════════════ */
.splash {
  position: fixed; inset: 0; z-index: 10000;
  background: var(--bg);
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  gap: 20px; transition: opacity 0.5s;
}
.splash.hide { opacity: 0; pointer-events: none; }
.splash-logo { font-size: 64px; animation: splashPulse 1.5s ease-in-out infinite; }
@keyframes splashPulse {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.1); opacity: 0.85; }
}
.splash-title {
  font-size: 22px; font-weight: 700; color: var(--accent);
  letter-spacing: 0.5px;
}
.splash-sub {
  font-size: 12px; color: var(--muted); text-transform: uppercase; letter-spacing: 2px;
}
.splash-bismillah {
  font-family: 'Amiri', serif; font-size: 20px; color: var(--accent);
  margin-top: 40px; opacity: 0.85;
}

/* ═══════════════════════════════════════════════════════════════ */
/*   TOP BAR                                                         */
/* ═══════════════════════════════════════════════════════════════ */
.topbar {
  position: fixed; top: 0; left: 0; right: 0; z-index: 100;
  height: 52px;
  background: var(--panel);
  backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--panel-border);
  display: flex; align-items: center; padding: 0 16px;
  gap: 12px;
}
.brand {
  display: flex; align-items: center; gap: 8px;
  text-decoration: none; color: var(--fg);
  font-weight: 700; font-size: 15px;
}
.brand-logo { font-size: 22px; }
.brand-text { letter-spacing: -0.3px; }
.bismillah-bar {
  flex: 1; text-align: center;
  font-family: 'Amiri', serif;
  font-size: 16px; color: var(--accent);
  opacity: 0.7; white-space: nowrap; overflow: hidden;
  transition: opacity 0.3s, text-shadow 0.3s;
}
.bismillah-bar.glow { opacity: 1; text-shadow: 0 0 8px var(--accent); }
.topbar-actions { display: flex; align-items: center; gap: 6px; }
.topbar-btn {
  background: transparent; border: 1px solid transparent;
  color: var(--muted); cursor: pointer;
  padding: 6px 10px; border-radius: 8px;
  font-size: 13px; font-weight: 500;
  display: flex; align-items: center; gap: 6px;
  transition: all 0.15s;
}
.topbar-btn:hover { background: var(--accent-soft); color: var(--accent); border-color: var(--panel-border); }
.topbar-btn.active { background: var(--accent-soft); color: var(--accent); }
.flag {
  width: 22px; height: 16px; border-radius: 3px;
  object-fit: cover; cursor: pointer;
  opacity: 0.5; transition: opacity 0.2s, transform 0.2s;
  border: 1px solid transparent;
}
.flag:hover { opacity: 0.9; transform: scale(1.1); }
.flag.active { opacity: 1; border-color: var(--accent); box-shadow: 0 0 0 2px var(--accent-soft); }
.progress-pill {
  display: inline-flex; align-items: center; gap: 5px;
  padding: 4px 10px; border-radius: 12px;
  background: var(--accent-soft); color: var(--accent);
  font-size: 12px; font-weight: 600;
  border: 1px solid var(--panel-border);
}
.progress-pill .count { font-variant-numeric: tabular-nums; }

/* ═══════════════════════════════════════════════════════════════ */
/*   LAYOUT (sidebar + main)                                         */
/* ═══════════════════════════════════════════════════════════════ */
.layout { padding-top: 52px; min-height: 100vh; }
.sidebar {
  position: fixed; top: 52px; left: 0; bottom: 0;
  width: 272px;
  background: var(--panel);
  backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
  border-right: 1px solid var(--panel-border);
  overflow-y: auto; overflow-x: hidden;
  padding: 16px 0;
  transition: transform 0.3s ease;
  z-index: 50;
}
.sidebar::-webkit-scrollbar { width: 5px; }
[dir="rtl"] .sidebar { left: auto; right: 0; border-right: none; border-left: 1px solid var(--panel-border); }
.nav-search {
  margin: 0 16px 16px; position: relative;
}
.nav-search input {
  width: 100%; padding: 8px 12px 8px 32px;
  background: var(--card); border: 1px solid var(--card-border);
  border-radius: 8px; color: var(--fg);
  font-size: 13px; outline: none;
  transition: border-color 0.15s;
}
.nav-search input:focus { border-color: var(--accent); }
.nav-search::before {
  content: '🔍'; position: absolute; left: 10px; top: 50%; transform: translateY(-50%);
  font-size: 12px; opacity: 0.6; pointer-events: none;
}
[dir="rtl"] .nav-search input { padding: 8px 32px 8px 12px; }
[dir="rtl"] .nav-search::before { left: auto; right: 10px; }
.nav-section {
  display: flex; align-items: center; justify-content: space-between;
  padding: 10px 20px; cursor: pointer; user-select: none;
  font-size: 11px; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.8px;
  color: var(--muted); transition: color 0.15s;
}
.nav-section:hover { color: var(--fg); }
.nav-section-title { display: flex; align-items: center; gap: 8px; }
.nav-section-icon { font-size: 14px; }
.nav-section-count {
  font-size: 10px; font-weight: 500;
  padding: 1px 6px; border-radius: 8px;
  background: var(--card); color: var(--muted);
  font-variant-numeric: tabular-nums;
}
.nav-section .arrow {
  font-size: 10px; transition: transform 0.25s;
}
.nav-section.open .arrow { transform: rotate(90deg); }
[dir="rtl"] .nav-section.open .arrow { transform: rotate(-90deg); }
.nav-group { overflow: hidden; max-height: 0; transition: max-height 0.4s ease; }
.nav-group.open { max-height: 2400px; }
.nav-link {
  display: flex; align-items: center; gap: 8px;
  padding: 6px 20px 6px 32px;
  font-size: 13px; color: var(--muted);
  text-decoration: none;
  border-left: 2px solid transparent;
  transition: all 0.15s;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  cursor: pointer;
}
[dir="rtl"] .nav-link {
  padding: 6px 32px 6px 20px;
  border-left: none; border-right: 2px solid transparent;
}
.nav-link:hover { color: var(--fg); background: var(--accent-soft); }
.nav-link.active {
  color: var(--accent); border-left-color: var(--accent);
  background: var(--accent-soft); font-weight: 600;
}
[dir="rtl"] .nav-link.active { border-right-color: var(--accent); }
.nav-link-num {
  font-size: 10px; font-variant-numeric: tabular-nums;
  color: var(--faint); width: 20px;
}
.nav-link-title { flex: 1; overflow: hidden; text-overflow: ellipsis; }
.nav-link.done::after {
  content: '✓'; color: var(--success); font-weight: 700; font-size: 11px;
}
.main {
  margin-left: 272px;
  min-height: calc(100vh - 52px);
  padding: 20px 0 40px;
}
[dir="rtl"] .main { margin-left: 0; margin-right: 272px; }
.mobile-toggle {
  display: none; background: transparent; border: none;
  color: var(--fg); font-size: 22px; cursor: pointer;
  padding: 4px 8px;
}
.mobile-overlay {
  display: none; position: fixed; inset: 0;
  background: rgba(0, 0, 0, 0.5); z-index: 40;
  opacity: 0; transition: opacity 0.3s;
}
.mobile-overlay.show { display: block; opacity: 1; }

/* ═══════════════════════════════════════════════════════════════ */
/*   COVER                                                           */
/* ═══════════════════════════════════════════════════════════════ */
.cover {
  padding: 40px 32px 60px;
  max-width: 960px; margin: 0 auto;
  text-align: center; position: relative;
}
.cover::before {
  content: ''; position: absolute; inset: 0;
  background:
    radial-gradient(ellipse 600px 300px at 30% 40%, var(--accent-soft), transparent),
    radial-gradient(ellipse 500px 300px at 70% 60%, var(--accent2-soft), transparent);
  pointer-events: none; z-index: -1;
}
.cover-hero {
  font-size: 48px; font-weight: 800; letter-spacing: -1.5px;
  background: linear-gradient(135deg, var(--accent), var(--accent2), var(--accent));
  background-size: 200% auto;
  -webkit-background-clip: text; background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gradShift 4s ease infinite;
  margin-bottom: 8px;
}
@keyframes gradShift {
  0%, 100% { background-position: 0% center; }
  50% { background-position: 200% center; }
}
.cover-sub {
  font-size: 18px; color: var(--muted); margin-bottom: 4px;
  font-weight: 400;
}
.cover-tagline {
  font-size: 14px; color: var(--faint); margin-top: 24px;
  max-width: 640px; margin-left: auto; margin-right: auto;
  line-height: 1.7;
}
.cover-cta {
  margin-top: 32px; display: flex; gap: 10px; justify-content: center;
  flex-wrap: wrap;
}
.cover-btn {
  padding: 10px 20px; border-radius: 10px;
  background: var(--accent-soft); color: var(--accent);
  border: 1px solid var(--accent); font-weight: 600; font-size: 14px;
  cursor: pointer; text-decoration: none;
  display: inline-flex; align-items: center; gap: 8px;
  transition: all 0.2s;
}
.cover-btn:hover {
  background: var(--accent); color: var(--bg);
  transform: translateY(-2px);
}
.cover-board {
  margin: 40px auto 20px; max-width: 300px;
}
.cover-stats {
  display: grid; grid-template-columns: repeat(4, 1fr);
  gap: 12px; margin-top: 40px; max-width: 720px;
  margin-left: auto; margin-right: auto;
}
.cover-stat {
  padding: 16px; border-radius: 12px;
  background: var(--card); border: 1px solid var(--card-border);
}
.cover-stat-num {
  font-size: 28px; font-weight: 800; color: var(--accent);
  font-variant-numeric: tabular-nums;
}
.cover-stat-label {
  font-size: 11px; text-transform: uppercase; letter-spacing: 1px;
  color: var(--muted); margin-top: 4px;
}

/* ═══════════════════════════════════════════════════════════════ */
/*   ACTIVITY SECTION                                                */
/* ═══════════════════════════════════════════════════════════════ */
.act-section {
  padding: 40px 32px;
  border-bottom: 1px solid var(--card-border);
  max-width: 960px; margin: 0 auto;
}
.act-header-bar {
  display: flex; align-items: center; gap: 14px;
  padding: 14px 20px; border-radius: 12px;
  margin-bottom: 24px; position: relative; overflow: hidden;
  border: 1px solid var(--hdr-color, var(--accent));
}
.act-header-bar::before {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(135deg, var(--hdr-color, var(--accent)) 0%, transparent 100%);
  opacity: 0.12; pointer-events: none;
}
.act-num-badge {
  position: relative; z-index: 1;
  width: 42px; height: 42px; border-radius: 10px;
  background: var(--hdr-color, var(--accent)); color: #fff;
  display: flex; align-items: center; justify-content: center;
  font-size: 17px; font-weight: 800; flex-shrink: 0;
  font-variant-numeric: tabular-nums;
}
.act-title-area { position: relative; z-index: 1; flex: 1; min-width: 0; }
.act-title-text {
  font-size: 20px; font-weight: 700; color: var(--fg);
  overflow: hidden; text-overflow: ellipsis;
}
.act-header-tags {
  display: flex; gap: 6px; margin-top: 4px; flex-wrap: wrap; align-items: center;
}
.tag-chip {
  display: inline-flex; align-items: center; gap: 3px;
  padding: 2px 8px; border-radius: 6px;
  font-size: 11px; font-weight: 600;
  background: var(--card);
  border: 1px solid var(--card-border);
  color: var(--muted);
}
.tag-chip.diff { color: var(--dc, var(--accent)); }
.tag-chip.v2 { color: #40BF4A; border-color: #40BF4A55; }
.tag-chip.ai { color: #eab308; border-color: #eab30855; }
.tag-chip.official { color: var(--accent2); border-color: var(--accent2); }
.tag-stars { letter-spacing: 1px; }
.act-wiki-link {
  margin-left: auto; font-size: 11px; color: var(--muted);
  text-decoration: none; padding: 3px 8px; border-radius: 6px;
  border: 1px solid var(--card-border);
  transition: all 0.15s;
}
.act-wiki-link:hover { color: var(--accent); border-color: var(--accent); }

/* Glass card */
.glass-card {
  background: var(--card);
  backdrop-filter: blur(6px); -webkit-backdrop-filter: blur(6px);
  border: 1px solid var(--card-border);
  border-radius: 12px; padding: 14px 18px; margin-bottom: 18px;
}
.sec-label {
  font-size: 11px; font-weight: 700; text-transform: uppercase;
  letter-spacing: 1.2px; color: var(--accent); margin-bottom: 8px;
  display: flex; align-items: center; gap: 8px;
}
.sec-label::after {
  content: ''; flex: 1; height: 1px;
  background: linear-gradient(to right, var(--accent-soft), transparent);
}
[dir="rtl"] .sec-label::after {
  background: linear-gradient(to left, var(--accent-soft), transparent);
}
.goal-text { font-size: 15px; line-height: 1.7; color: var(--fg); }

/* Content row — LED preview + info side by side */
.content-row {
  display: flex; gap: 20px; align-items: flex-start; margin-bottom: 18px;
}
.content-row .led-col { flex-shrink: 0; }
.content-row .info-col { flex: 1; min-width: 0; }
.led-svg { display: block; }

/* Materials pills */
.needs-wrap { display: flex; flex-wrap: wrap; gap: 6px; }
.need-pill {
  padding: 4px 12px; border-radius: 20px;
  font-size: 12px; font-weight: 500;
  background: var(--card); border: 1px solid var(--card-border);
  color: var(--muted);
}

/* Flowchart */
.flowchart {
  display: flex; flex-direction: column; align-items: center;
  gap: 0; padding: 16px; background: var(--code-bg);
  border-radius: 10px; border: 1px solid var(--code-border);
  margin-bottom: 16px;
}
.fc-node {
  padding: 6px 18px; font-size: 11px; font-weight: 600;
  color: #fff; text-align: center; max-width: 240px;
  font-variant-numeric: tabular-nums;
}
.fc-node.start { background: #40BF4A; border-radius: 20px; }
.fc-node.end   { background: #DC143C; border-radius: 20px; }
.fc-node.process { background: #1E90FF; border-radius: 5px; }
.fc-node.decision { background: #9400D3; border-radius: 4px; border: 1.5px solid rgba(255,255,255,0.2); padding: 5px 14px; }
.fc-node.io { background: #D400D4; border-radius: 5px 16px 5px 16px; }
.fc-node.loop { background: #00AA00; border-radius: 5px; border-left: 3px solid rgba(255,255,255,0.3); }
.fc-arrow { width: 2px; height: 14px; background: var(--accent); position: relative; }
.fc-arrow::after {
  content: '▼'; position: absolute; bottom: -6px; left: 50%;
  transform: translateX(-50%); font-size: 8px; color: var(--accent);
}

/* Pseudo-code */
.pseudo-box {
  font-family: 'SF Mono', 'Fira Code', Consolas, monospace;
  font-size: 11.5px; line-height: 1.7;
  padding: 14px 16px;
  background: var(--code-bg);
  border-radius: 10px; border: 1px solid var(--code-border);
  white-space: pre; overflow-x: auto; margin-bottom: 16px;
  color: var(--fg);
}
.pk { color: #569CD6; font-weight: 700; }
.pv { color: #CE9178; }
.pc { color: #6A9955; font-style: italic; }

/* Steps */
.steps-list { list-style: none; margin-bottom: 18px; }
.step-item {
  display: flex; gap: 12px; align-items: flex-start;
  padding: 6px 0;
}
.step-num {
  width: 24px; height: 24px; border-radius: 50%;
  background: var(--accent-soft); color: var(--accent);
  font-size: 12px; font-weight: 700;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0; margin-top: 1px;
  border: 1px solid var(--accent);
}
.step-text { font-size: 14px; color: var(--fg); line-height: 1.6; flex: 1; }

/* Tip box */
.tip-box {
  padding: 12px 16px; border-radius: 10px;
  background: rgba(234, 179, 8, 0.08);
  border: 1px solid rgba(234, 179, 8, 0.25);
  color: #eab308; font-size: 13px; line-height: 1.6;
  margin-bottom: 18px;
}
.tip-box .tip-icon { margin-right: 6px; }
[dir="rtl"] .tip-box .tip-icon { margin-right: 0; margin-left: 6px; }

/* Code area */
.code-grid {
  display: flex; flex-direction: column; gap: 12px;
  margin-bottom: 18px;
}
.code-panel {
  border-radius: 10px; overflow: hidden; position: relative;
  border: 1px solid var(--code-border);
}
.code-panel-header {
  padding: 8px 14px; display: flex; align-items: center; gap: 8px;
  font-size: 12px; font-weight: 700;
}
.code-panel-header.js-header { background: rgba(247, 223, 30, 0.12); color: #f7df1e; }
.code-panel-header.py-header { background: rgba(48, 105, 152, 0.2); color: #60a5fa; }
.code-lang-dot { width: 8px; height: 8px; border-radius: 50%; }
.code-lang-dot.js-dot { background: #f7df1e; }
.code-lang-dot.py-dot { background: #306998; }
.code-actions {
  margin-left: auto; display: flex; gap: 4px;
}
.code-btn {
  padding: 3px 10px; border-radius: 6px;
  font-size: 11px; font-weight: 600;
  background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1);
  color: var(--muted); cursor: pointer;
  transition: all 0.15s;
  display: inline-flex; align-items: center; gap: 4px;
  text-decoration: none;
}
.code-btn:hover { background: rgba(255,255,255,0.1); color: var(--fg); }
.code-block {
  padding: 14px 16px;
  font-family: 'SF Mono', 'Fira Code', Consolas, monospace;
  font-size: 12.5px; line-height: 1.65;
  overflow-x: auto; white-space: pre;
  background: var(--code-bg);
  color: var(--fg);
}
.hl-kw { color: #c084fc; font-weight: 600; }
.hl-str { color: #34d399; }
.hl-cmt { color: #6A9955; font-style: italic; }
.hl-num { color: #f59e0b; }
.hl-fn { color: #60a5fa; }

/* Challenges */
.chal-list { margin-bottom: 16px; }
.chal-item {
  display: flex; gap: 10px; align-items: flex-start;
  padding: 5px 0; font-size: 13px; color: var(--fg);
}
.chal-dot {
  width: 10px; height: 10px; border-radius: 50%;
  flex-shrink: 0; margin-top: 5px;
}
.chal-dot.easy { background: #40BF4A; }
.chal-dot.med  { background: #f59e0b; }
.chal-dot.hard { background: #DC143C; }

/* Done button */
.act-done-bar {
  margin-top: 24px; padding-top: 16px;
  border-top: 1px solid var(--card-border);
  display: flex; justify-content: space-between; align-items: center;
  gap: 12px; flex-wrap: wrap;
}
.done-btn {
  padding: 8px 16px; border-radius: 8px;
  background: var(--success); color: #fff; border: none;
  font-weight: 600; font-size: 13px; cursor: pointer;
  transition: all 0.2s;
  display: inline-flex; align-items: center; gap: 6px;
}
.done-btn:hover { transform: translateY(-1px); opacity: 0.9; }
.done-btn.done { background: var(--accent); }
.act-footer-meta {
  font-size: 11px; color: var(--faint); letter-spacing: 0.5px;
}

/* ═══════════════════════════════════════════════════════════════ */
/*   COMMAND PALETTE                                                 */
/* ═══════════════════════════════════════════════════════════════ */
.cmdk-overlay {
  position: fixed; inset: 0; z-index: 200;
  background: rgba(0, 0, 0, 0.5); backdrop-filter: blur(4px);
  display: none; align-items: flex-start; justify-content: center;
  padding-top: 10vh;
}
.cmdk-overlay.open { display: flex; }
.cmdk {
  width: 90%; max-width: 600px;
  background: var(--panel); border: 1px solid var(--panel-border);
  border-radius: 14px; overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
}
.cmdk-input {
  width: 100%; padding: 16px 20px;
  background: transparent; border: none; outline: none;
  color: var(--fg); font-size: 16px;
  border-bottom: 1px solid var(--card-border);
}
.cmdk-results { max-height: 50vh; overflow-y: auto; }
.cmdk-item {
  display: flex; align-items: center; gap: 12px;
  padding: 10px 20px; cursor: pointer;
  border-left: 3px solid transparent;
  color: var(--fg);
  transition: background 0.1s;
}
.cmdk-item:hover, .cmdk-item.sel {
  background: var(--accent-soft);
  border-left-color: var(--accent);
}
[dir="rtl"] .cmdk-item { border-left: none; border-right: 3px solid transparent; }
[dir="rtl"] .cmdk-item:hover, [dir="rtl"] .cmdk-item.sel { border-right-color: var(--accent); }
.cmdk-item-icon { font-size: 16px; width: 20px; text-align: center; }
.cmdk-item-title { flex: 1; font-size: 14px; }
.cmdk-item-meta { font-size: 11px; color: var(--muted); }
.cmdk-hint {
  padding: 8px 20px; border-top: 1px solid var(--card-border);
  font-size: 11px; color: var(--faint);
  display: flex; gap: 12px; justify-content: center;
}
.cmdk-empty { padding: 30px; text-align: center; color: var(--muted); font-size: 13px; }

/* ═══════════════════════════════════════════════════════════════ */
/*   SETTINGS PANEL                                                  */
/* ═══════════════════════════════════════════════════════════════ */
.panel {
  position: fixed; top: 52px; bottom: 0; width: 340px;
  background: var(--panel); border-left: 1px solid var(--panel-border);
  z-index: 80; padding: 20px; overflow-y: auto;
  transform: translateX(100%); transition: transform 0.3s;
}
.panel.right { right: 0; }
.panel.left { left: 0; border-left: none; border-right: 1px solid var(--panel-border); transform: translateX(-100%); }
.panel.open { transform: translateX(0); }
[dir="rtl"] .panel.right { right: auto; left: 0; border-left: none; border-right: 1px solid var(--panel-border); transform: translateX(-100%); }
[dir="rtl"] .panel.right.open { transform: translateX(0); }
[dir="rtl"] .panel.left { left: auto; right: 0; border-right: none; border-left: 1px solid var(--panel-border); transform: translateX(100%); }
[dir="rtl"] .panel.left.open { transform: translateX(0); }
.panel-header {
  display: flex; justify-content: space-between; align-items: center;
  padding-bottom: 16px; border-bottom: 1px solid var(--card-border);
  margin-bottom: 20px;
}
.panel-title { font-size: 16px; font-weight: 700; }
.panel-close {
  background: transparent; border: none; color: var(--muted);
  font-size: 22px; cursor: pointer; line-height: 1;
}
.panel-close:hover { color: var(--fg); }
.panel-section { margin-bottom: 24px; }
.panel-section-label {
  font-size: 11px; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.8px; color: var(--muted); margin-bottom: 10px;
}
.theme-grid {
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px;
}
.theme-swatch {
  padding: 10px 8px; border-radius: 8px; cursor: pointer;
  border: 1px solid var(--card-border);
  font-size: 11px; font-weight: 600; text-align: center;
  transition: all 0.15s; color: var(--fg);
  background: var(--card);
}
.theme-swatch:hover { border-color: var(--accent); }
.theme-swatch.active { border-color: var(--accent); background: var(--accent-soft); color: var(--accent); }
.theme-dot {
  display: block; width: 22px; height: 22px; border-radius: 50%;
  margin: 0 auto 4px; border: 1px solid rgba(255,255,255,0.1);
}
.toggle-row {
  display: flex; align-items: center; justify-content: space-between;
  padding: 8px 0;
}
.toggle-label { font-size: 13px; color: var(--fg); }
.toggle-switch {
  position: relative; width: 40px; height: 22px;
  background: var(--card); border: 1px solid var(--card-border);
  border-radius: 12px; cursor: pointer;
  transition: all 0.2s;
}
.toggle-switch::after {
  content: ''; position: absolute; left: 2px; top: 2px;
  width: 16px; height: 16px; border-radius: 50%;
  background: var(--muted); transition: all 0.2s;
}
.toggle-switch.on { background: var(--accent-soft); border-color: var(--accent); }
.toggle-switch.on::after { left: calc(100% - 18px); background: var(--accent); }

/* ═══════════════════════════════════════════════════════════════ */
/*   HELP PANEL (pinout + cheatsheet + FAQ)                          */
/* ═══════════════════════════════════════════════════════════════ */
.panel-wide { width: 480px; }
@media (max-width: 900px) { .panel-wide { width: 100%; } }

.help-tabs {
  display: flex; gap: 4px;
  margin-bottom: 16px;
  border-bottom: 1px solid var(--card-border);
  padding-bottom: 0;
}
.help-tab {
  flex: 1; padding: 8px 10px;
  background: transparent; border: none;
  color: var(--muted); cursor: pointer;
  font-size: 12px; font-weight: 600;
  border-bottom: 2px solid transparent;
  transition: all 0.15s;
}
.help-tab:hover { color: var(--fg); }
.help-tab.active {
  color: var(--accent); border-bottom-color: var(--accent);
}
.help-content { display: none; }
.help-content.active { display: block; }
.help-intro {
  font-size: 12px; color: var(--muted); line-height: 1.6;
  padding: 12px 14px; border-radius: 8px;
  background: var(--card); border: 1px solid var(--card-border);
  margin-bottom: 14px;
}

/* Pinout specs */
.pinout-specs {
  margin-top: 16px; padding: 12px;
  background: var(--card); border: 1px solid var(--card-border);
  border-radius: 10px;
}
.spec-row {
  display: flex; justify-content: space-between; gap: 10px;
  padding: 6px 0; font-size: 12px;
  border-bottom: 1px solid var(--card-border);
}
.spec-row:last-child { border-bottom: none; }
.spec-key { color: var(--muted); font-weight: 600; flex-shrink: 0; }
.spec-val { color: var(--fg); text-align: right; }
[dir="rtl"] .spec-val { text-align: left; }

/* Cheatsheet */
.cheat-section {
  border: 1px solid var(--card-border);
  border-radius: 10px; margin-bottom: 12px;
  overflow: hidden;
}
.cheat-section-header {
  display: flex; align-items: center; gap: 8px;
  padding: 8px 12px;
  background: var(--card);
  font-size: 12px; font-weight: 700;
  color: var(--accent);
  border-bottom: 1px solid var(--card-border);
}
.cheat-section-icon { font-size: 14px; }
.cheat-items { padding: 8px; display: flex; flex-direction: column; gap: 10px; }
.cheat-item {
  padding: 8px 10px; border-radius: 8px;
  background: rgba(255,255,255,0.02);
  border: 1px solid var(--card-border);
}
.cheat-pattern {
  font-size: 12px; font-weight: 600; color: var(--fg);
  margin-bottom: 6px;
}
.cheat-code-row { display: flex; flex-direction: column; gap: 4px; }
.cheat-code {
  font-family: 'SF Mono', 'Fira Code', Consolas, monospace;
  font-size: 10.5px; line-height: 1.5;
  padding: 6px 8px; border-radius: 6px;
  background: var(--code-bg);
  color: var(--fg);
  display: flex; gap: 8px; align-items: flex-start;
  overflow-x: auto;
}
.cheat-code code { white-space: pre; flex: 1; }
.cheat-lang {
  font-size: 9px; font-weight: 700;
  padding: 1px 5px; border-radius: 3px;
  flex-shrink: 0; margin-top: 2px;
}
.cheat-code.js .cheat-lang { background: rgba(247,223,30,0.2); color: #f7df1e; }
.cheat-code.py .cheat-lang { background: rgba(48,105,152,0.3); color: #60a5fa; }
.cheat-note {
  font-size: 10.5px; color: var(--muted);
  margin-top: 6px; font-style: italic;
  padding-left: 4px; border-left: 2px solid var(--card-border);
}

/* FAQ */
.faq-item {
  margin-bottom: 10px;
  border: 1px solid var(--card-border);
  border-radius: 10px; overflow: hidden;
  background: var(--card);
}
.faq-question {
  padding: 10px 14px;
  font-size: 13px; font-weight: 600; color: var(--fg);
  cursor: pointer; user-select: none;
  list-style: none;
  position: relative;
  padding-right: 32px;
}
[dir="rtl"] .faq-question { padding-right: 14px; padding-left: 32px; }
.faq-question::-webkit-details-marker { display: none; }
.faq-question::after {
  content: '▸'; position: absolute;
  right: 14px; top: 50%; transform: translateY(-50%);
  color: var(--accent); font-size: 11px;
  transition: transform 0.2s;
}
[dir="rtl"] .faq-question::after { right: auto; left: 14px; }
.faq-item[open] .faq-question::after { transform: translateY(-50%) rotate(90deg); }
.faq-item:hover { border-color: var(--accent); }
.faq-answer {
  list-style: none; padding: 0 14px 12px 14px;
  margin: 0;
}
.faq-answer li {
  font-size: 12px; color: var(--muted); line-height: 1.7;
  padding: 3px 0;
}

/* ═══════════════════════════════════════════════════════════════ */
/*   RESOURCES PANEL                                                 */
/* ═══════════════════════════════════════════════════════════════ */
.resources-wrap { display: flex; flex-direction: column; gap: 18px; }
.resources-intro {
  font-size: 12px; color: var(--muted); line-height: 1.6;
  padding: 12px 14px; border-radius: 8px;
  background: var(--card); border: 1px solid var(--card-border);
  margin-bottom: 4px;
}
.resource-section {
  border: 1px solid var(--card-border);
  border-radius: 10px;
  overflow: hidden;
}
.resource-section-header {
  display: flex; align-items: center; gap: 8px;
  padding: 10px 14px;
  background: var(--card);
  font-size: 13px; font-weight: 700;
  color: var(--accent);
  border-bottom: 1px solid var(--card-border);
}
.resource-section-icon { font-size: 16px; }
.resource-section-title { flex: 1; }
.resource-section-count {
  font-size: 11px; font-weight: 500;
  padding: 2px 8px; border-radius: 10px;
  background: var(--accent-soft); color: var(--accent);
  font-variant-numeric: tabular-nums;
}
.resource-items { display: flex; flex-direction: column; }
.resource-item {
  display: flex; align-items: center; gap: 10px;
  padding: 10px 14px; text-decoration: none;
  color: var(--fg);
  border-bottom: 1px solid var(--card-border);
  transition: background 0.15s;
}
.resource-item:last-child { border-bottom: none; }
.resource-item:hover { background: var(--accent-soft); }
.resource-icon { font-size: 16px; flex-shrink: 0; width: 22px; text-align: center; }
.resource-info { flex: 1; min-width: 0; }
.resource-name {
  font-size: 13px; font-weight: 600; color: var(--fg);
  margin-bottom: 2px;
}
.resource-item:hover .resource-name { color: var(--accent); }
.resource-desc {
  font-size: 11px; color: var(--muted); line-height: 1.5;
}
.resource-arrow {
  font-size: 14px; color: var(--muted); flex-shrink: 0;
  opacity: 0.5; transition: opacity 0.15s, transform 0.15s;
}
.resource-item:hover .resource-arrow {
  opacity: 1; color: var(--accent); transform: translate(2px, -2px);
}

/* ═══════════════════════════════════════════════════════════════ */
/*   PARCOURS (learning paths)                                       */
/* ═══════════════════════════════════════════════════════════════ */
.parcours-wrap { display: flex; flex-direction: column; gap: 16px; }
.parcours-card {
  border: 1px solid var(--card-border);
  background: var(--card);
  border-radius: 12px; padding: 14px;
}
.parcours-header {
  display: flex; gap: 12px; align-items: center; margin-bottom: 8px;
}
.parcours-icon { font-size: 32px; flex-shrink: 0; }
.parcours-info { flex: 1; min-width: 0; }
.parcours-name { font-size: 14px; font-weight: 700; color: var(--fg); }
.parcours-meta { font-size: 11px; color: var(--muted); margin-top: 2px; }
.parcours-desc {
  font-size: 12px; color: var(--muted); line-height: 1.6;
  margin-bottom: 10px;
}
.parcours-list {
  display: flex; flex-direction: column; gap: 4px;
  max-height: 220px; overflow-y: auto;
}
.parcours-act {
  display: flex; align-items: center; gap: 8px;
  padding: 6px 10px; border-radius: 6px;
  font-size: 12px; color: var(--fg);
  text-decoration: none;
  background: rgba(255,255,255,0.02);
  border: 1px solid transparent;
  transition: all 0.15s;
}
.parcours-act:hover {
  background: var(--accent-soft);
  border-color: var(--accent);
  color: var(--accent);
}
.parcours-act-num {
  font-size: 10px; font-variant-numeric: tabular-nums;
  color: var(--muted); width: 20px; flex-shrink: 0;
}
.parcours-act-title {
  flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
}
.parcours-act-stars {
  font-size: 10px; color: var(--warn);
  flex-shrink: 0;
}

/* ═══════════════════════════════════════════════════════════════ */
/*   FOOTER                                                          */
/* ═══════════════════════════════════════════════════════════════ */
.site-footer {
  margin-left: 272px; padding: 32px;
  border-top: 1px solid var(--card-border);
  display: flex; align-items: center; justify-content: center;
  gap: 12px; flex-wrap: wrap;
  font-size: 12px; color: var(--faint);
}
[dir="rtl"] .site-footer { margin-left: 0; margin-right: 272px; }
.pet {
  font-size: 20px; cursor: pointer;
  transition: transform 0.2s;
  display: inline-block;
}
.pet:hover { transform: scale(1.3) rotate(-10deg); }
.pet.happy { animation: petBounce 0.6s ease; }
@keyframes petBounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-8px) scale(1.2); }
}
.hijri-date { font-family: 'Amiri', serif; color: var(--muted); }
.footer-link {
  color: var(--muted); text-decoration: none;
  padding: 2px 6px; border-radius: 4px;
  transition: color 0.15s;
}
.footer-link:hover { color: var(--accent); }

/* ═══════════════════════════════════════════════════════════════ */
/*   TOAST                                                           */
/* ═══════════════════════════════════════════════════════════════ */
.toast {
  position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%) translateY(120%);
  background: var(--panel); border: 1px solid var(--accent);
  border-radius: 10px; padding: 10px 18px;
  font-size: 13px; color: var(--fg); z-index: 300;
  transition: transform 0.3s ease;
  box-shadow: 0 10px 30px rgba(0,0,0,0.3);
  display: flex; align-items: center; gap: 8px;
}
.toast.show { transform: translateX(-50%) translateY(0); }

/* ═══════════════════════════════════════════════════════════════ */
/*   RESPONSIVE                                                      */
/* ═══════════════════════════════════════════════════════════════ */
@media (max-width: 900px) {
  .sidebar { transform: translateX(-100%); }
  .sidebar.open { transform: translateX(0); }
  [dir="rtl"] .sidebar { transform: translateX(100%); }
  [dir="rtl"] .sidebar.open { transform: translateX(0); }
  .mobile-toggle { display: block; }
  .main { margin-left: 0 !important; margin-right: 0 !important; }
  .site-footer { margin-left: 0 !important; margin-right: 0 !important; }
  .mobile-overlay { z-index: 45; }
  .act-section { padding: 28px 20px; }
  .content-row { flex-direction: column; }
  .cover-hero { font-size: 32px; }
  .cover-stats { grid-template-columns: repeat(2, 1fr); }
  .bismillah-bar { display: none; }
  .topbar-btn span { display: none; }
  .panel { width: 100%; }
}
@media (max-width: 500px) {
  .cover-hero { font-size: 26px; }
  .act-title-text { font-size: 17px; }
}

/* ═══════════════════════════════════════════════════════════════ */
/*   PRINT                                                           */
/* ═══════════════════════════════════════════════════════════════ */
@media print {
  @page { size: A4; margin: 1.5cm 1.8cm; }
  body { background: #fff; color: #1a1a2e; font-size: 10pt; }
  .topbar, .sidebar, .mobile-toggle, .mobile-overlay,
  .cmdk-overlay, .panel, .site-footer, .cover-cta,
  .code-actions, .code-btn, .mobile-overlay, .toast { display: none !important; }
  .layout { padding-top: 0; }
  .main { margin: 0 !important; }
  .cover { padding: 1cm 0; page-break-after: always; }
  .cover-hero { -webkit-text-fill-color: #1E90FF !important; color: #1E90FF !important; background: none !important; animation: none; }
  .act-section { padding: 0.8cm 0; page-break-inside: avoid; border-bottom: 1px solid #eee; }
  .act-header-bar { background: none !important; }
  .act-header-bar::before { display: none; }
  .glass-card, .code-block, .flowchart, .pseudo-box {
    background: #f9f9f9 !important; border: 1px solid #ddd !important; backdrop-filter: none;
  }
  .goal-text, .step-text { color: #333; }
  .tip-box { background: #fffde7 !important; border: 1px dashed #daa520 !important; color: #8b6914 !important; }
  .hl-kw { color: #0000ff; }
  .hl-str { color: #a31515; }
  .hl-cmt { color: #008000; }
  .hl-num { color: #098658; }
  .fc-node, .act-num-badge, .chal-dot, .need-pill { print-color-adjust: exact; -webkit-print-color-adjust: exact; }
  .act-title-text, .step-text { color: #1a1a2e; }
  .sec-label { color: #1E90FF; }
  .sec-label::after { background: #eee; }
  .act-done-bar { display: none; }
}
"""
