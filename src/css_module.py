#!/usr/bin/env python3
"""CSS for Maqueen guide — ported verbatim from bit-48-activities."""

CSS = r"""
/* ═══════════════════════════════════════════════════════════════════ */
[data-theme="mosque-gold"]{--bg:#08091a;--panel:#0b0d24;--accent:#d4a03c;--accent2:#0ea5e9;--glow:rgba(212,160,60,.15);--glow2:rgba(14,165,233,.1);--text:#e4ddd0;--text-muted:#8a7e6e;--border:rgba(212,160,60,.18);--band1:#d4a03c;--band2:#c08c2e;--band3:#f0c96e;--font-h:'Righteous','Tajawal',sans-serif;--font-b:'Tajawal',system-ui,sans-serif;--card-ornament:"✦";--summary-marker:"◆";--bism-color:#d4a03c}
[data-theme="zellige"]{--bg:#041c2c;--panel:#06253a;--accent:#38bdf8;--accent2:#f0abfc;--glow:rgba(56,189,248,.12);--glow2:rgba(240,171,252,.08);--text:#d6eaf8;--text-muted:#6b9cc0;--border:rgba(56,189,248,.18);--band1:#38bdf8;--band2:#0284c7;--band3:#7dd3fc;--font-h:'Righteous','Tajawal',sans-serif;--font-b:'Tajawal',system-ui,sans-serif;--card-ornament:"✧";--summary-marker:"◇";--bism-color:#7dd3fc}
[data-theme="andalus"]{--bg:#0a1a0a;--panel:#0d200e;--accent:#4ade80;--accent2:#fbbf24;--glow:rgba(74,222,128,.12);--glow2:rgba(251,191,36,.08);--text:#d5eed5;--text-muted:#6b9e6b;--border:rgba(74,222,128,.18);--band1:#4ade80;--band2:#16a34a;--band3:#fbbf24;--font-h:'Righteous','Tajawal',sans-serif;--font-b:'Tajawal',system-ui,sans-serif;--card-ornament:"❋";--summary-marker:"✿";--bism-color:#86efac}
[data-theme="space"]{--bg:#0c0020;--panel:#110030;--accent:#c084fc;--accent2:#22d3ee;--glow:rgba(192,132,252,.15);--glow2:rgba(34,211,238,.1);--text:#e8dff8;--text-muted:#8b7aad;--border:rgba(192,132,252,.2);--band1:#c084fc;--band2:#7c3aed;--band3:#22d3ee;--font-h:'Orbitron','Righteous',sans-serif;--font-b:'Tajawal',system-ui,sans-serif;--card-ornament:"⚡";--summary-marker:"▸";--bism-color:#c084fc}
[data-theme="jungle"]{--bg:#071407;--panel:#0c1f0a;--accent:#a3e635;--accent2:#fb923c;--glow:rgba(163,230,53,.12);--glow2:rgba(251,146,60,.08);--text:#e2f0d0;--text-muted:#7a9e5c;--border:rgba(163,230,53,.2);--band1:#a3e635;--band2:#65a30d;--band3:#fb923c;--font-h:'Bangers','Righteous',sans-serif;--font-b:'Tajawal',system-ui,sans-serif;--card-ornament:"🌿";--summary-marker:"▸";--bism-color:#a3e635}
[data-theme="robot"]{--bg:#0a0f1e;--panel:#0e1529;--accent:#3b82f6;--accent2:#f97316;--glow:rgba(59,130,246,.12);--glow2:rgba(249,115,22,.08);--text:#d0ddf0;--text-muted:#5e7499;--border:rgba(59,130,246,.2);--band1:#3b82f6;--band2:#1d4ed8;--band3:#f97316;--font-h:'Orbitron','Righteous',sans-serif;--font-b:'Tajawal',system-ui,sans-serif;--card-ornament:"⚙";--summary-marker:"▹";--bism-color:#60a5fa}

/* ── ANIMATED BG PARTICLES ── */
@keyframes floatDot{0%{transform:translateY(0) scale(1);opacity:.3}50%{transform:translateY(-40px) scale(1.2);opacity:.15}100%{transform:translateY(0) scale(1);opacity:.3}}
@keyframes floatDot2{0%{transform:translateY(0) translateX(0);opacity:.2}50%{transform:translateY(-25px) translateX(15px);opacity:.1}100%{transform:translateY(0) translateX(0);opacity:.2}}
@keyframes pulseGlow{0%,100%{opacity:.4;transform:scale(1)}50%{opacity:.8;transform:scale(1.05)}}
@keyframes cardEnter{from{opacity:0;transform:translateY(18px) scale(.97)}to{opacity:1;transform:translateY(0) scale(1)}}
@keyframes slideUnderline{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@keyframes statusPulse{0%,100%{box-shadow:0 0 4px rgba(59,130,246,.4)}50%{box-shadow:0 0 12px rgba(59,130,246,.8)}}
@keyframes ripple{from{transform:scale(0);opacity:.5}to{transform:scale(2.5);opacity:0}}
@keyframes challengeEnter{from{opacity:0;transform:translateX(-10px)}to{opacity:1;transform:translateX(0)}}
@keyframes glowStripe{0%{background-position:0% 0%}100%{background-position:0% 200%}}

*{box-sizing:border-box;margin:0;padding:0}
body{min-height:100vh;background:var(--bg);color:var(--text);font-family:var(--font-b);display:flex;align-items:stretch;justify-content:center;padding:16px;overflow-x:hidden;transition:background .4s ease}
[dir="rtl"]{font-family:'Tajawal','Amiri',sans-serif}
[dir="rtl"] h1,[dir="rtl"] .card-title,[dir="rtl"] .tab-btn{font-family:'Tajawal',sans-serif!important;letter-spacing:0!important}

.app{display:flex;flex-direction:column;max-width:1100px;width:100%;background:radial-gradient(ellipse at top,var(--glow),transparent 55%),radial-gradient(ellipse at bottom right,var(--glow2),transparent 55%),var(--panel);border-radius:18px;box-shadow:0 0 0 1px var(--border),0 30px 60px rgba(0,0,0,.5),inset 0 1px 0 rgba(255,255,255,.04);position:relative;z-index:1;overflow:hidden;transition:background .4s ease,box-shadow .4s ease}
.app::before{content:"";position:absolute;inset:0;pointer-events:none;z-index:0;background:radial-gradient(circle 120px at 15% 20%,var(--glow),transparent),radial-gradient(circle 80px at 85% 30%,var(--glow2),transparent),radial-gradient(circle 60px at 50% 70%,var(--glow),transparent),radial-gradient(circle 100px at 70% 90%,var(--glow2),transparent);animation:floatDot 8s ease-in-out infinite}
.app::after{content:"";position:absolute;inset:0;pointer-events:none;z-index:0;background:radial-gradient(circle 50px at 30% 60%,var(--glow2),transparent),radial-gradient(circle 70px at 80% 15%,var(--glow),transparent),radial-gradient(circle 40px at 60% 45%,var(--glow2),transparent);animation:floatDot2 12s ease-in-out infinite}
.rows-container{position:relative;z-index:1;padding:0 4px}
.deco-band{height:2px;background:linear-gradient(90deg,transparent,var(--accent),var(--accent2),var(--accent),transparent);opacity:.6;box-shadow:0 0 12px var(--glow),0 0 4px var(--glow2)}
.bottom-band{margin-top:auto}

.header{position:relative;padding:14px 16px 6px;display:flex;align-items:center;justify-content:space-between;gap:10px}
.header-right{display:flex;flex-direction:column;align-items:flex-end;gap:6px}
[dir="rtl"] .header-right{align-items:flex-start}
.title-block{display:flex;align-items:center;gap:14px}
.logo-wrap{width:68px;height:68px;flex-shrink:0}.logo-wrap svg{width:100%;height:100%}
.title-block h1{font-family:var(--font-h);font-size:1.3rem;letter-spacing:.06em;text-transform:uppercase;background:linear-gradient(135deg,var(--accent),var(--accent2),var(--accent));background-size:200% 200%;-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;animation:gradShift 5s ease infinite;filter:drop-shadow(0 0 12px var(--glow))}
@keyframes gradShift{0%,100%{background-position:0% 50%}50%{background-position:100% 50%}}
.title-block .subtitle{font-size:.78rem;color:var(--text-muted);margin-top:2px;letter-spacing:.04em;animation:subtitlePulse 4s ease infinite}
@keyframes subtitlePulse{0%,100%{opacity:.7}50%{opacity:1}}
.bismillah{position:absolute;top:3px;inset-inline:0;display:flex;justify-content:center;align-items:center;gap:6px;font-family:'Amiri',serif;font-size:.72rem;color:var(--bism-color);opacity:.5;pointer-events:none}
.bism-ornament{font-size:.55rem;opacity:.6}
.header-dropdowns{display:flex;gap:5px}
.mini-select{padding:2px 4px;border-radius:6px;font-size:.65rem;font-weight:600;font-family:var(--font-b);background:rgba(0,0,0,.4);color:var(--text-muted);border:1px solid var(--border);cursor:pointer;transition:all .2s;outline:none;-webkit-appearance:none;appearance:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='8' height='5'%3E%3Cpath d='M0 0l4 5 4-5z' fill='%23888'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 4px center;padding-right:14px}
[dir="rtl"] .mini-select{background-position:left 4px center;padding-right:4px;padding-left:14px}
.mini-select:hover{border-color:var(--accent)}
.mini-select option{background:var(--panel);color:var(--text)}
.status-pill{display:inline-flex;align-items:center;gap:5px;padding:3px 8px;border-radius:999px;font-size:.68rem;letter-spacing:.07em;text-transform:uppercase;border:1px solid rgba(255,255,255,.12);color:var(--text);background:rgba(0,0,0,.4);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}
.status-dot{width:7px;height:7px;border-radius:999px;background:var(--accent);animation:statusPulse 2s ease-in-out infinite}

.controls-bar{display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr;gap:8px;padding:10px 12px;margin:0 4px 8px;background:rgba(0,0,0,.2);border:1px solid var(--border);border-radius:14px;backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);box-shadow:inset 0 1px 0 rgba(255,255,255,.04),0 4px 24px rgba(0,0,0,.2)}
@media(max-width:780px){.controls-bar{grid-template-columns:1fr 1fr}}
@media(max-width:480px){.controls-bar{grid-template-columns:1fr}}
.ctrl-group{display:flex;flex-direction:column;gap:4px}
.ctrl-group label{font-size:.7rem;color:var(--text-muted);text-transform:uppercase;letter-spacing:.05em}
.ctrl-group select,.ctrl-group input[type="search"]{width:100%;padding:7px 10px;border-radius:10px;font-size:.78rem;border:1px solid var(--border);background:rgba(0,0,0,.4);color:var(--text);font-family:var(--font-b);outline:none;transition:border-color .2s}
.ctrl-group select:focus,.ctrl-group input:focus{border-color:var(--accent)}
.options-row{display:flex;gap:8px;align-items:center;flex-wrap:wrap;padding:0 12px 8px;margin:0 4px}
.pill-opt{display:inline-flex;align-items:center;gap:6px;padding:5px 10px;border-radius:999px;border:1px solid var(--border);background:rgba(0,0,0,.2);color:var(--text-muted);cursor:pointer;font-size:.72rem;user-select:none;transition:all .25s;backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px)}
.pill-opt:hover{border-color:var(--accent);box-shadow:0 0 10px var(--glow);transform:translateY(-1px)}
.pill-opt input{accent-color:var(--accent2);width:14px;height:14px}
.stats-row{display:flex;gap:8px;flex-wrap:wrap;padding:0 8px 8px;font-size:.72rem;color:var(--text-muted)}
.stats-row span{padding:4px 12px;border-radius:10px;background:rgba(0,0,0,.2);border:1px solid rgba(255,255,255,.05);backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px)}
.stats-row strong{color:var(--accent)}

button{border:none;border-radius:999px;padding:6px 11px;font-size:.75rem;font-family:var(--font-b);cursor:pointer;display:inline-flex;align-items:center;justify-content:center;gap:5px;background:rgba(0,0,0,.4);color:var(--text);border:1px solid rgba(255,255,255,.1);transition:all .25s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden}
button::after{content:"";position:absolute;inset:0;background:radial-gradient(circle,rgba(255,255,255,.25) 0%,transparent 60%);transform:scale(0);opacity:0;border-radius:inherit;pointer-events:none}
button:active::after{animation:ripple .5s ease-out}
button:hover:not(:disabled){border-color:var(--accent);box-shadow:0 0 16px var(--glow),0 4px 12px rgba(0,0,0,.2);transform:translateY(-2px)}
button:disabled{opacity:.4;cursor:default}
button.primary{background:linear-gradient(135deg,var(--accent),var(--band2));color:var(--bg);font-weight:700;border-color:var(--accent);box-shadow:0 6px 20px var(--glow)}
button.primary:hover:not(:disabled){box-shadow:0 8px 28px var(--glow),0 0 0 2px rgba(255,255,255,.1);transform:translateY(-2px) scale(1.04)}
.btn-sm{padding:4px 9px;font-size:.7rem}

.activity-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;padding:0 4px 10px}
@media(max-width:860px){.activity-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:540px){.activity-grid{grid-template-columns:1fr}}
.act-card{border-radius:14px;border:1px solid var(--border);background:rgba(255,255,255,.02);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);padding:12px;position:relative;overflow:hidden;cursor:pointer;display:flex;flex-direction:column;gap:8px;min-height:140px;transition:all .3s cubic-bezier(.4,0,.2,1);animation:cardEnter .4s cubic-bezier(.4,0,.2,1) both;animation-delay:calc(var(--i,0) * 40ms);box-shadow:inset 0 1px 0 rgba(255,255,255,.04),0 2px 8px rgba(0,0,0,.15)}
.act-card::before{content:var(--card-ornament);position:absolute;top:6px;inset-inline-end:10px;font-size:14px;color:var(--accent);opacity:.12;pointer-events:none;transition:all .3s}
.act-card::after{content:"";position:absolute;inset:0;border-radius:14px;opacity:0;transition:opacity .3s;background:radial-gradient(circle at 50% 0%,var(--glow),transparent 70%);pointer-events:none}
.act-card:hover{border-color:var(--accent);box-shadow:0 0 24px var(--glow),0 8px 32px rgba(0,0,0,.3),inset 0 1px 0 rgba(255,255,255,.08);transform:translateY(-4px) scale(1.02)}
.act-card:hover::before{opacity:.35;transform:scale(1.3)}
.act-card:hover::after{opacity:1}
.act-card .card-top{display:flex;justify-content:space-between;align-items:flex-start;gap:6px;position:relative;z-index:1}
.act-card .tags{display:flex;gap:4px;flex-wrap:wrap}
.act-card .card-id{font-size:.62rem;color:var(--bg);white-space:nowrap;background:var(--accent);padding:1px 7px;border-radius:999px;font-weight:700;letter-spacing:.03em;opacity:.85}
.act-card h3{font-size:.88rem;line-height:1.25;font-weight:600;position:relative;z-index:1}
.act-card .preview{font-size:.74rem;color:var(--text-muted);line-height:1.3;position:relative;z-index:1}
.act-card .card-bottom{margin-top:auto;display:flex;justify-content:space-between;align-items:center;gap:8px;position:relative;z-index:1}
.tag{padding:2px 7px;border-radius:999px;font-size:.62rem;font-weight:600;border:1px solid rgba(255,255,255,.1);background:rgba(0,0,0,.18);white-space:nowrap;letter-spacing:.03em;backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);transition:all .2s}
.tag:hover{transform:translateY(-1px);box-shadow:0 2px 8px rgba(0,0,0,.2)}
.tag.v2{border-color:rgba(74,222,128,.4);color:rgba(74,222,128,.95)}
.tag.ia{border-color:rgba(255,214,107,.4);color:rgba(255,214,107,.95)}
.tag.adv{border-color:rgba(122,167,255,.4);color:rgba(122,167,255,.95)}
.tag.simple{border-color:rgba(255,255,255,.12);color:var(--text-muted)}
.tag.d1{border-color:rgba(74,222,128,.3);color:rgba(74,222,128,.9)}
.tag.d2{border-color:rgba(251,191,36,.3);color:rgba(251,191,36,.9)}
.tag.d3{border-color:rgba(255,107,138,.3);color:rgba(255,107,138,.9)}
.chip{padding:3px 8px;border-radius:999px;font-size:.66rem;font-weight:600;border:1px solid rgba(255,255,255,.1);background:rgba(0,0,0,.1)}
.chip.done{border-color:rgba(107,255,149,.35);color:rgba(107,255,149,.95);box-shadow:0 0 6px rgba(107,255,149,.15)}
.chip.todo{border-color:rgba(255,255,255,.12);color:var(--text-muted)}
.chip.fav{border-color:rgba(255,214,107,.35);color:rgba(255,214,107,.95);box-shadow:0 0 6px rgba(255,214,107,.15)}
.act-card[data-diff="1"]{border-inline-start:3px solid transparent;border-image:linear-gradient(180deg,rgba(74,222,128,.7),rgba(74,222,128,.15)) 1}
.act-card[data-diff="2"]{border-inline-start:3px solid transparent;border-image:linear-gradient(180deg,rgba(251,191,36,.7),rgba(251,191,36,.15)) 1}
.act-card[data-diff="3"]{border-inline-start:3px solid transparent;border-image:linear-gradient(180deg,rgba(255,107,138,.7),rgba(255,107,138,.15)) 1}

.modal-overlay{position:fixed;inset:0;background:rgba(0,0,0,.82);display:none;z-index:100;padding:16px;overflow-y:auto;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);animation:fadeIn .25s ease}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
.modal-overlay.open{display:flex;align-items:flex-start;justify-content:center}
.modal{max-width:720px;width:100%;margin:20px auto;background:radial-gradient(ellipse at top left,var(--glow),transparent 50%),radial-gradient(ellipse at bottom right,var(--glow2),transparent 50%),rgba(14,21,41,.92);border:1px solid var(--border);border-radius:18px;box-shadow:0 30px 80px rgba(0,0,0,.6),0 0 0 1px rgba(255,255,255,.04),inset 0 1px 0 rgba(255,255,255,.06);overflow:hidden;animation:modalSlide .35s cubic-bezier(.4,0,.2,1);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
@keyframes modalSlide{from{opacity:0;transform:translateY(24px) scale(.97)}to{opacity:1;transform:translateY(0) scale(1)}}
.modal-head{padding:14px 16px 10px;display:flex;justify-content:space-between;align-items:flex-start;gap:10px;border-bottom:1px solid rgba(255,255,255,.08)}
.modal-head h2{font-size:1rem;font-family:var(--font-h);letter-spacing:.04em}
.modal-head .tags{display:flex;gap:4px;flex-wrap:wrap;margin-top:4px}
.close-btn{background:rgba(0,0,0,.4);border:1px solid rgba(255,255,255,.1);color:var(--text);border-radius:10px;padding:6px 10px;cursor:pointer;font-weight:700;font-size:.85rem;flex-shrink:0}
.tab-bar{display:flex;border-bottom:1px solid rgba(255,255,255,.08);overflow-x:auto;-webkit-overflow-scrolling:touch;scrollbar-width:none}
.tab-bar::-webkit-scrollbar{display:none}
.tab-btn{flex:1;padding:10px 8px;text-align:center;font-size:.74rem;font-weight:600;color:var(--text-muted);background:transparent;border:none;border-bottom:2px solid transparent;cursor:pointer;transition:all .25s;white-space:nowrap;border-radius:0;font-family:var(--font-b);position:relative}
.tab-btn:hover{color:var(--text);background:rgba(255,255,255,.04)}
.tab-btn.active{color:var(--accent);border-bottom-color:var(--accent);background:linear-gradient(180deg,transparent,rgba(255,255,255,.03))}
.tab-btn.active::after{content:"";position:absolute;bottom:0;left:10%;right:10%;height:2px;background:var(--accent);border-radius:2px;box-shadow:0 0 8px var(--glow);animation:slideUnderline .3s ease}
.tab-panel{display:none;padding:14px 16px;opacity:0;transition:opacity .15s}.tab-panel.active{display:block;opacity:1}
/* ── ENRICHED INFO TAB ── */
.info-meta{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px;align-items:center}
.info-meta .meta-chip{display:inline-flex;align-items:center;gap:4px;padding:4px 12px;border-radius:999px;font-size:.72rem;font-weight:600;border:1px solid rgba(255,255,255,.1);background:rgba(0,0,0,.2)}
.info-meta .meta-chip.diff-1{border-color:rgba(74,222,128,.3);color:rgba(74,222,128,.9)}
.info-meta .meta-chip.diff-2{border-color:rgba(251,191,36,.3);color:rgba(251,191,36,.9)}
.info-meta .meta-chip.diff-3{border-color:rgba(255,107,138,.3);color:rgba(255,107,138,.9)}
.info-meta .meta-chip.time-chip{color:var(--text-muted)}
.info-meta .meta-chip.v2-chip{border-color:rgba(74,222,128,.4);color:rgba(74,222,128,.95)}
.info-meta .meta-chip.ia-chip{border-color:rgba(255,214,107,.4);color:rgba(255,214,107,.95)}
.info-section{margin-bottom:12px}
.info-section-title{font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--accent);margin-bottom:6px;display:flex;align-items:center;gap:4px}
.info-learn{font-size:.8rem;line-height:1.5;color:var(--text-muted);padding:8px 12px;border-radius:10px;background:rgba(0,0,0,.1);border:1px solid rgba(255,255,255,.05)}
.info-learn ul{margin:4px 0 0 16px;padding:0}
.info-learn li{margin-bottom:3px}
.goal-text{font-size:.85rem;line-height:1.5;margin-bottom:0}
/* Concept explanation box */
.info-concept{font-size:.8rem;line-height:1.6;color:var(--text);padding:10px 14px;border-radius:10px;background:rgba(59,130,246,.06);border:1px solid rgba(59,130,246,.15);border-inline-start:3px solid var(--accent)}
.info-concept strong{color:var(--accent)}
.info-concept code{padding:1px 5px;border-radius:4px;font-size:.72rem;background:rgba(0,0,0,.2);border:1px solid rgba(255,255,255,.08);color:var(--accent);font-family:"SF Mono",monospace}
/* Step-by-step guide */
.info-steps{display:flex;flex-direction:column;gap:6px}
.info-step{display:flex;gap:10px;align-items:flex-start;padding:8px 10px;border-radius:8px;background:rgba(0,0,0,.08);border:1px solid rgba(255,255,255,.04);font-size:.78rem;line-height:1.4;transition:background .2s}
.info-step:hover{background:rgba(0,0,0,.14)}
.info-step .step-n{width:24px;height:24px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.65rem;font-weight:700;background:var(--accent);color:var(--bg);flex-shrink:0}
.info-step .step-text{color:var(--text-muted)}
.info-step .step-text strong{color:var(--text)}
.info-step .step-text code{padding:1px 5px;border-radius:4px;font-size:.7rem;background:rgba(0,0,0,.2);border:1px solid rgba(255,255,255,.08);color:var(--accent);font-family:"SF Mono",monospace}
/* ── FLOWCHART (draw.io style) ── */
.info-flow{display:flex;flex-direction:column;align-items:center;gap:0;padding:12px 8px;background:rgba(0,0,0,.08);border-radius:10px;border:1px solid rgba(255,255,255,.05);overflow-x:auto}
.flow-node{padding:6px 16px;border-radius:20px;font-size:.72rem;font-weight:600;text-align:center;max-width:260px;color:#fff;position:relative}
.flow-node.start{background:#40BF4A;border-radius:20px}
.flow-node.end{background:#DC143C;border-radius:20px}
.flow-node.process{background:#1E90FF;border-radius:6px}
.flow-node.decision{background:#9400D3;border-radius:4px;transform:none;padding:6px 14px;border:2px solid rgba(255,255,255,.2)}
.flow-node.decision::before{content:"◇";position:absolute;inset-inline-start:-14px;top:50%;transform:translateY(-50%);font-size:.7rem;color:#9400D3}
.flow-node.io{background:#E63022;border-radius:6px 20px 6px 20px}
.flow-node.loop{background:#00AA00;border-radius:6px;border-inline-start:4px solid rgba(255,255,255,.3)}
.flow-arrow{width:2px;height:14px;background:var(--accent);position:relative}
.flow-arrow::after{content:"▼";position:absolute;bottom:-7px;left:50%;transform:translateX(-50%);font-size:.5rem;color:var(--accent);line-height:1}
.flow-branch{display:flex;gap:12px;align-items:flex-start;margin:4px 0}
.flow-branch-label{font-size:.58rem;color:var(--text-muted);text-transform:uppercase;letter-spacing:.04em;padding:2px 6px}
.flow-branch-yes{color:rgba(74,222,128,.9)}
.flow-branch-no{color:rgba(255,107,138,.9)}

/* ── PSEUDOCODE ── */
.info-pseudo{font-family:"SF Mono",ui-monospace,Menlo,monospace;font-size:.72rem;line-height:1.6;color:var(--text);padding:10px 14px;border-radius:10px;background:rgba(0,0,0,.15);border:1px solid rgba(255,255,255,.06);white-space:pre;overflow-x:auto;direction:ltr;text-align:left;margin:0}
.info-pseudo .pk{color:#569CD6;font-weight:700}
.info-pseudo .pv{color:#CE9178}
.info-pseudo .pc{color:#6A9955;font-style:italic}
.info-pseudo .pf{color:#DCDCAA}

/* QR Code section */
.qr-section{display:flex;align-items:center;gap:12px;margin-top:12px;padding:10px 14px;border-radius:10px;background:rgba(0,0,0,.1);border:1px solid rgba(255,255,255,.05)}
.qr-section img{width:80px;height:80px;border-radius:6px;background:#fff;padding:4px}
.qr-section .qr-text{font-size:.72rem;color:var(--text-muted);line-height:1.4}
.qr-section .qr-text strong{color:var(--text)}

/* LED Simulator */
.led-sim{display:flex;flex-direction:column;align-items:center;gap:8px}
.led-sim-label{font-size:.68rem;color:var(--text-muted);text-transform:uppercase;letter-spacing:.05em}
.led-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:4px;padding:12px;background:#111;border-radius:12px;border:2px solid #333;width:fit-content}
.led-cell{width:28px;height:28px;border-radius:50%;background:#1a1a1a;border:1px solid #222;transition:all .15s;cursor:pointer}
.led-cell.on{background:#ff1a1a;box-shadow:0 0 8px #ff1a1a,0 0 16px rgba(255,26,26,.4);border-color:#ff4444}
.led-cell:hover{border-color:#555}
/* Wiring diagram (for pin activities) */
.info-diagram{font-family:"SF Mono",monospace;font-size:.7rem;line-height:1.4;color:var(--accent);padding:10px 14px;border-radius:10px;background:rgba(0,0,0,.2);border:1px solid rgba(255,255,255,.06);white-space:pre;overflow-x:auto;direction:ltr;text-align:left}
/* Block chips (mini MakeCode blocks in Info tab) */
.info-blocks-used{display:flex;flex-wrap:wrap;gap:6px}
.block-chip{display:inline-flex;align-items:center;gap:4px;padding:4px 10px;border-radius:6px;font-size:.72rem;font-weight:600;color:#fff;border-bottom:2px solid rgba(0,0,0,.2);font-family:system-ui,-apple-system,sans-serif}
.block-chip .bc-icon{font-size:.8rem}
/* Code keys (JS + Python side by side) */
.info-code-keys{display:flex;flex-direction:column;gap:4px}
.code-key-row{display:flex;gap:6px;align-items:center;font-size:.72rem;padding:4px 8px;border-radius:8px;background:rgba(0,0,0,.1);border:1px solid rgba(255,255,255,.05)}
.code-key-row .ck-block{width:8px;height:8px;border-radius:2px;flex-shrink:0}
.code-key-row .ck-label{color:var(--text-muted);min-width:100px}
.code-key-row .ck-js{font-family:"SF Mono",ui-monospace,Menlo,monospace;color:#F7DF1E;font-size:.68rem}
.code-key-row .ck-py{font-family:"SF Mono",ui-monospace,Menlo,monospace;color:#4B8BBE;font-size:.68rem}
.code-key-row .ck-sep{color:var(--text-muted);opacity:.4}
.needs-list{list-style:none;padding:0;display:flex;gap:6px;flex-wrap:wrap}
.needs-list li{padding:4px 10px;border-radius:999px;font-size:.72rem;border:1px solid var(--border);background:rgba(0,0,0,.25);color:var(--text-muted)}
.tip-box{margin-top:10px;padding:10px 12px;border-radius:12px;border:1px dashed rgba(255,214,107,.3);background:linear-gradient(135deg,rgba(255,214,107,.06),rgba(255,214,107,.02));font-size:.78rem;color:rgba(255,214,107,.9);line-height:1.4;backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);box-shadow:inset 0 0 20px rgba(255,214,107,.03)}
/* block-step styles moved to bottom */
.code-toggle{display:flex;gap:6px;margin-bottom:10px}
.code-toggle button{padding:5px 14px;border-radius:999px;font-size:.72rem;font-weight:700;border:1px solid var(--border);background:rgba(0,0,0,.3);color:var(--text-muted);cursor:pointer;transition:all .2s}
.code-toggle button.active{border-color:var(--accent);color:var(--accent);background:rgba(0,0,0,.5)}
.code-block{position:relative;border-radius:12px;border:1px solid var(--border);background:rgba(0,0,0,.5);padding:12px 14px;overflow-x:auto;font-family:"SF Mono",ui-monospace,Menlo,Consolas,monospace;font-size:.76rem;line-height:1.5;color:var(--text);white-space:pre;max-height:280px;overflow-y:auto;direction:ltr;text-align:left;box-shadow:inset 0 2px 8px rgba(0,0,0,.3),0 1px 0 rgba(255,255,255,.03)}
.copy-btn{position:absolute;top:8px;right:8px;padding:4px 10px;border-radius:8px;font-size:.66rem;font-weight:700;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.12);color:var(--text-muted);cursor:pointer;transition:all .2s;z-index:2}
.copy-btn:hover{border-color:var(--accent);color:var(--accent)}
.copy-btn.copied{border-color:rgba(74,222,128,.5);color:rgba(74,222,128,.9)}
.challenge{padding:10px 12px;border-radius:12px;margin-bottom:8px;border:1px solid rgba(255,255,255,.08);background:rgba(0,0,0,.12);display:flex;gap:10px;align-items:flex-start;border-inline-start:3px solid var(--accent);animation:challengeEnter .3s ease both;animation-delay:calc(var(--ci,0) * 80ms);transition:all .2s}
.challenge:hover{background:rgba(0,0,0,.2);border-inline-start-color:var(--accent2);transform:translateX(3px)}
.challenge-icon{font-size:1.1rem;flex-shrink:0;margin-top:1px}
.challenge-text{font-size:.78rem;line-height:1.4;color:var(--text-muted)}
.challenge-text code{padding:1px 5px;border-radius:4px;font-size:.72rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);color:var(--accent);font-family:"SF Mono",ui-monospace,Menlo,Consolas,monospace;direction:ltr;display:inline-block}
.challenge .diff-star{font-size:.65rem;color:rgba(255,214,107,.7)}
.modal-actions{display:flex;gap:8px;flex-wrap:wrap;padding:10px 16px 14px;border-top:1px solid rgba(255,255,255,.08);justify-content:space-between;align-items:center}
.modal-actions .left,.modal-actions .right{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.hint-text{font-size:.66rem;color:var(--text-muted)}
.badge{font-size:.68rem;padding:1px 6px;border-radius:999px;border:1px solid var(--border);color:var(--text-muted)}.badge strong{color:var(--accent)}
.empty-state{text-align:center;padding:40px 16px;color:var(--text-muted);font-size:.85rem;background:radial-gradient(ellipse,var(--glow),transparent 70%);border-radius:14px}
.toast-indicator{display:none;position:fixed;bottom:20px;inset-inline-end:20px;background:linear-gradient(135deg,var(--accent),var(--band2));padding:10px 18px;border-radius:50px;box-shadow:0 4px 24px var(--glow),0 0 0 1px rgba(255,255,255,.1);z-index:9999;animation:slideIn .4s cubic-bezier(.4,0,.2,1);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}
.toast-inner{display:flex;align-items:center;gap:8px}
.toast-text{color:var(--bg);font-weight:700;font-size:.85rem}
@keyframes slideIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
::-webkit-scrollbar{width:5px;height:5px}::-webkit-scrollbar-track{background:transparent}::-webkit-scrollbar-thumb{background:var(--border);border-radius:3px}::-webkit-scrollbar-thumb:hover{background:var(--accent)}
@media(max-width:600px){.header{flex-wrap:wrap;gap:6px}.logo-wrap{width:52px;height:52px}.title-block h1{font-size:1rem}.modal{border-radius:14px}.tab-btn{font-size:.68rem;padding:8px 6px}}

/* ── FOCUS INDICATORS ── */
button:focus-visible,.mini-select:focus-visible,.sidebar-item:focus-visible,.tab-btn:focus-visible,.pill-opt:focus-visible,.act-card:focus-visible{outline:2px solid var(--accent);outline-offset:2px;box-shadow:0 0 0 4px var(--glow)}
input:focus-visible,select:focus-visible{outline:2px solid var(--accent);outline-offset:1px}
.close-btn:focus-visible{outline:2px solid var(--accent);outline-offset:2px}

/* ── PRINT STYLES ── */
@media print{
  body{background:#fff;color:#000;padding:0}
  .app{box-shadow:none;border:none;max-width:100%}
  .app::before,.app::after,.deco-band,.sidebar,.sidebar-overlay,.header-dropdowns,.status-pill,.options-row,.controls-bar,.sidebar-toggle,.toast-indicator,.modal-overlay{display:none!important}
  .act-card{break-inside:avoid;border:1px solid #ccc;box-shadow:none;background:#fff;color:#000;animation:none!important}
  .act-card .card-id{background:#333;color:#fff}
  .activity-grid{grid-template-columns:repeat(2,1fr)!important;gap:8px}
  .tag{border-color:#999;color:#333}
  .chip{border-color:#999;color:#333}
}

/* ── REDUCED MOTION ── */
@media(prefers-reduced-motion:reduce){
  *,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}
}

/* ── ENHANCED HEADER ── */
.logo-wrap{filter:drop-shadow(0 0 8px var(--glow));transition:filter .3s}
.logo-wrap:hover{filter:drop-shadow(0 0 16px var(--accent))}

/* ── BLOCK STEPS ── */
.block-step{padding:8px 10px;border-radius:10px;font-size:.78rem;line-height:1.4;border:1px solid rgba(255,255,255,.08);background:rgba(0,0,0,.12);color:var(--text-muted);margin-bottom:6px;transition:all .2s}
.block-step:hover{background:rgba(0,0,0,.2);border-color:rgba(255,255,255,.12);transform:translateX(2px)}
.block-step .step-num{display:inline-flex;align-items:center;justify-content:center;width:20px;height:20px;border-radius:50%;font-size:.62rem;font-weight:700;background:linear-gradient(135deg,var(--accent),var(--band2));color:var(--bg);margin-inline-end:8px;flex-shrink:0;box-shadow:0 2px 8px var(--glow)}

/* ── VISUAL BLOCKS (MakeCode Zelos renderer) ── */
/* Based on Blockly Zelos constants: GRID_UNIT=4, CORNER_RADIUS=4, NOTCH_WIDTH=36, NOTCH_HEIGHT=8 */
.block-canvas{display:flex;flex-direction:column;gap:4px;padding:8px 4px;background:rgba(255,255,255,.03);border-radius:8px}

/* ── Base block ── */
.vblock{position:relative;border-radius:4px;padding:0 8px;min-height:40px;font-size:12px;font-weight:500;color:#fff;display:flex;flex-wrap:wrap;align-items:center;gap:4px;line-height:40px;cursor:default;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif}
.vblock::before,.vblock::after{display:none}
/* Dark bottom edge — Zelos style 3D */
.vblock{box-shadow:0 2px 0 0 rgba(0,0,0,.2)}

/* ── Notch connector (top of non-hat blocks) ── */
.vblock:not(.hat):not(.cblock)::before{content:"";display:block;position:absolute;top:-4px;left:12px;width:36px;height:4px;background:inherit;border-radius:2px 2px 0 0;filter:brightness(.85)}
[dir="rtl"] .vblock:not(.hat):not(.cblock)::before{left:auto;right:12px}

/* ── Hat block (event trigger) ── */
.vblock.hat{border-radius:22px 22px 4px 4px;min-height:44px;padding:0 12px;line-height:44px;flex-direction:column;align-items:stretch;box-shadow:0 2px 0 0 rgba(0,0,0,.2)}
.vblock.hat>.hat-label{display:flex;align-items:center;gap:4px;min-height:44px}
.vblock .hat-body{display:flex;flex-direction:column;gap:1px;padding-bottom:4px}

/* ── C-block (if, forever, while, repeat) ── */
.vblock.cblock{padding:0;flex-direction:column;align-items:stretch;line-height:normal;box-shadow:none}
.vblock .cblock-row{display:flex;flex-wrap:wrap;align-items:center;gap:4px;min-height:40px;padding:0 8px;line-height:40px;border-radius:4px 4px 0 0;box-shadow:0 0 0 0}
.vblock .cblock-body{margin:0;padding:4px 4px 4px 16px;background:rgba(0,0,0,.15);min-height:40px;display:flex;flex-direction:column;gap:1px}
[dir="rtl"] .vblock .cblock-body{padding:4px 16px 4px 4px}
/* C-block bottom cap — same color, with notch */
.vblock.cblock>.cblock-cap{min-height:12px;border-radius:0 0 4px 4px;background:inherit;box-shadow:0 2px 0 0 rgba(0,0,0,.2)}
/* Else separator */
.vblock .cblock-else{padding:0 8px;min-height:32px;line-height:32px;color:rgba(255,255,255,.9);font-weight:500;background:inherit;filter:brightness(.95)}

/* ── Argument fields (Zelos: FIELD_BORDER_RECT_HEIGHT=32, RADIUS=4) ── */
.vblock .varg{display:inline-flex;align-items:center;height:24px;padding:0 8px;border-radius:12px;background:rgba(255,255,255,.95);color:#333;font-size:11px;font-weight:600;white-space:nowrap;line-height:24px;vertical-align:middle}
/* Round reporter (number/variable) — pill shape */
.vblock .varg.round{border-radius:999px;background:rgba(255,255,255,.95);color:#333}
/* String field — darker colored pill */
.vblock .varg.str{background:rgba(0,0,0,.18);color:#fff;border-radius:12px}
.vblock .varg.str::before{content:"\" ";opacity:.5;font-size:10px}.vblock .varg.str::after{content:" \"";opacity:.5;font-size:10px}
/* Nested value block (reporter inside field) */
.vblock .varg .vblock{display:inline-flex;height:22px;padding:0 8px;margin:0 -4px;font-size:11px;font-weight:500;border-radius:999px;line-height:22px;min-height:auto;box-shadow:0 1px 0 rgba(0,0,0,.15);gap:3px}
.vblock .varg .vblock::before,.vblock .varg .vblock::after{display:none}
.vblock .varg .vblock .varg{height:18px;padding:0 6px;font-size:10px;line-height:18px}
/* MakeCode official category colors (from pxt-microbit GitHub source) */
.vblock.cat-basic{background:#1E90FF}       /* Basic: DodgerBlue */
.vblock.cat-input{background:#D400D4}       /* Input: Magenta */
.vblock.cat-loops{background:#00AA00}       /* Loops: Green */
.vblock.cat-logic{background:#00A4A6}       /* Logic: Teal */
.vblock.cat-music{background:#E63022}       /* Music: Red-Orange */
.vblock.cat-radio{background:#E3008C}       /* Radio: Pink-Magenta */
.vblock.cat-variables{background:#DC143C}   /* Variables: Crimson */
.vblock.cat-pins{background:#3BDDD4}        /* Pins: Turquoise */
.vblock.cat-math{background:#9400D3}        /* Math: DarkViolet */
.vblock.cat-game{background:#7600A8}        /* Game/LED: Purple */
.vblock.cat-bluetooth{background:#0082FB}   /* Bluetooth: Blue */
.vblock.cat-neopixel{background:#7600A8}    /* NeoPixel: Purple */
.vblock.cat-sonar{background:#00A4A6}       /* Sonar: Teal */
.vblock.cat-functions{background:#3455DB}   /* Functions: RoyalBlue */

/* ── MAKECODE RENDERED BLOCKS ── */
.makecode-blocks{min-height:60px;display:flex;flex-direction:column;align-items:center;gap:8px;padding:8px 0}
.makecode-blocks img{max-width:100%;height:auto;border-radius:6px}
.makecode-blocks .mc-loading{font-size:.75rem;color:var(--text-muted);padding:16px;text-align:center}
.makecode-blocks .mc-loading::after{content:"";display:inline-block;width:14px;height:14px;border:2px solid var(--accent);border-top-color:transparent;border-radius:50%;animation:spin .6s linear infinite;margin-inline-start:8px;vertical-align:middle}
@keyframes spin{to{transform:rotate(360deg)}}

/* ── SIMULATOR ── */
.sim-container{display:flex;flex-direction:column;align-items:center;gap:8px}
.sim-actions{display:flex;gap:8px}
.sim-run-btn{background:linear-gradient(135deg,#40BF4A,#2d8f34)!important;color:#fff!important;font-weight:700;border:none!important;padding:6px 16px;font-size:.78rem}
.sim-stop-btn{background:linear-gradient(135deg,#DC143C,#a31020)!important;color:#fff!important;font-weight:700;border:none!important;padding:6px 16px;font-size:.78rem}
.sim-iframe{width:100%;max-width:100%;height:clamp(300px,60vh,600px);border:1px solid var(--border);border-radius:12px;background:#fff}
.sim-iframe.hidden{display:none}
.sim-hint{font-size:.76rem;color:var(--text-muted);text-align:center;padding:12px}

/* ── LEARNING ROADMAP ── */
.roadmap-overlay{position:fixed;inset:0;background:rgba(0,0,0,.82);display:none;z-index:200;padding:20px;overflow-y:auto;backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px)}
.roadmap-overlay.open{display:flex;align-items:flex-start;justify-content:center}
.roadmap-panel{max-width:800px;width:100%;margin:20px auto;background:var(--panel);border:1px solid var(--border);border-radius:18px;box-shadow:0 30px 60px rgba(0,0,0,.5);overflow:hidden}
.roadmap-header{display:flex;justify-content:space-between;align-items:center;padding:14px 16px;border-bottom:1px solid rgba(255,255,255,.08)}
.roadmap-header h2{font-size:1rem;font-family:var(--font-h)}
.roadmap-body{padding:16px;display:flex;flex-direction:column;gap:8px}
.roadmap-node{display:flex;align-items:center;gap:12px;padding:10px 14px;border-radius:12px;border:1px solid rgba(255,255,255,.06);background:rgba(0,0,0,.1);cursor:pointer;transition:all .2s}
.roadmap-node:hover{background:rgba(0,0,0,.2);border-color:var(--accent)}
.roadmap-node .rn-icon{font-size:1.4rem;width:36px;height:36px;display:flex;align-items:center;justify-content:center;border-radius:50%;background:rgba(0,0,0,.2);flex-shrink:0}
.roadmap-node .rn-info{flex:1}
.roadmap-node .rn-name{font-size:.82rem;font-weight:600;color:var(--text)}
.roadmap-node .rn-progress{font-size:.68rem;color:var(--text-muted);margin-top:2px}
.roadmap-node .rn-bar{width:100%;height:6px;background:rgba(255,255,255,.08);border-radius:3px;margin-top:4px;overflow:hidden}
.roadmap-node .rn-bar-fill{height:100%;border-radius:3px;background:var(--accent);transition:width .3s}
.roadmap-node.completed{border-color:rgba(74,222,128,.3);background:rgba(74,222,128,.06)}
.roadmap-node.completed .rn-icon{background:rgba(74,222,128,.2)}
.roadmap-connector{width:2px;height:16px;background:rgba(255,255,255,.1);margin-inline-start:28px}

/* ── BADGE SHELF (sidebar bottom) ── */
.badge-shelf{margin-top:auto;padding:8px;border-top:1px solid rgba(255,255,255,.06)}
.badge-xp{font-size:.68rem;font-weight:700;color:var(--accent);text-align:center;margin-bottom:4px}
.badge-row{display:flex;flex-wrap:wrap;gap:4px;justify-content:center}
.badge-icon{font-size:1.1rem;width:28px;height:28px;display:flex;align-items:center;justify-content:center;border-radius:8px;transition:all .2s;cursor:default}
.badge-icon.earned{background:rgba(255,214,107,.15);border:1px solid rgba(255,214,107,.3);animation:badgePop .4s ease}
.badge-icon.locked{opacity:.25;filter:grayscale(1)}
@keyframes badgePop{0%{transform:scale(0)}50%{transform:scale(1.3)}100%{transform:scale(1)}}

/* ── BLOCKS SYNC BAR ── */
.blocks-sync-bar{display:flex;align-items:center;gap:8px;padding:4px 0 8px;font-size:.72rem}
.sync-status{padding:2px 10px;border-radius:999px;font-weight:600}
.sync-status.synced{background:rgba(74,222,128,.12);color:rgba(74,222,128,.9);border:1px solid rgba(74,222,128,.25)}
.sync-status.modified{background:rgba(251,191,36,.12);color:rgba(251,191,36,.9);border:1px solid rgba(251,191,36,.25)}
.sync-btn{background:linear-gradient(135deg,var(--accent),var(--band2))!important;color:var(--bg)!important;font-weight:700;font-size:.7rem;padding:4px 12px;border-radius:999px;border:none!important;cursor:pointer}

/* ── CODE EDITOR (editable textarea) ── */
.code-editor{width:100%;min-height:160px;max-height:300px;resize:vertical;border-radius:10px;border:1px solid var(--border);background:rgba(0,0,0,.5);padding:12px 14px;font-family:"SF Mono",ui-monospace,Menlo,Consolas,monospace;font-size:.76rem;line-height:1.5;color:var(--text);white-space:pre;overflow:auto;direction:ltr;text-align:left;box-shadow:inset 0 2px 6px rgba(0,0,0,.25);outline:none;tab-size:4}
.code-editor:focus{border-color:var(--accent);box-shadow:inset 0 2px 6px rgba(0,0,0,.25),0 0 0 2px var(--glow)}
.code-actions{display:flex;gap:6px;margin-bottom:8px;flex-wrap:wrap}
.code-actions button{font-size:.72rem;padding:5px 12px}
.open-makecode-btn{background:linear-gradient(135deg,#6C3FC5,#9B59B6)!important;color:#fff!important;border:1px solid rgba(108,63,197,.5)!important;font-weight:700}
.open-makecode-btn:hover{box-shadow:0 0 16px rgba(108,63,197,.4);transform:translateY(-1px)}

/* ── SYNTAX HIGHLIGHTING ── */
.hl-keyword{color:#569CD6;font-weight:700}
.hl-string{color:#CE9178}
.hl-comment{color:#6A9955;font-style:italic}
.hl-number{color:#B5CEA8}

/* ── LANGUAGE TAB BADGES ── */
.tab-lang-badge{display:inline-block;font-size:.55rem;font-weight:800;padding:1px 5px;border-radius:3px;vertical-align:middle;margin-inline-end:3px;letter-spacing:.03em}
.js-badge{background:#F7DF1E;color:#000}
.py-badge{background:#306998;color:#FFD43B}

/* ── PYTHON CODE UNDER BLOCKS ── */
.blocks-python{margin-top:14px;border-top:1px solid rgba(255,255,255,.08);padding-top:12px}
.blocks-python-label{font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--text-muted);margin-bottom:6px;display:flex;align-items:center;gap:6px}
.blocks-python-label .py-icon{background:#306998;color:#FFD43B;font-size:.6rem;font-weight:800;padding:2px 6px;border-radius:4px}
.blocks-python pre{border-radius:10px;border:1px solid var(--border);background:rgba(0,0,0,.45);padding:12px 14px;overflow-x:auto;font-family:"SF Mono",ui-monospace,Menlo,Consolas,monospace;font-size:.74rem;line-height:1.5;color:var(--text);white-space:pre;max-height:220px;overflow-y:auto;direction:ltr;text-align:left;box-shadow:inset 0 2px 6px rgba(0,0,0,.25)}
.blocks-python .py-comment{color:#6A9955;font-style:italic}
.blocks-python .py-keyword{color:#569CD6}
.blocks-python .py-string{color:#CE9178}
.blocks-python .py-number{color:#B5CEA8}

/* ── SIDEBAR LAYOUT ── */
.app-body{display:flex;position:relative;z-index:1;min-height:0;flex:1}
.sidebar{width:200px;flex-shrink:0;padding:10px 8px;display:flex;flex-direction:column;gap:3px;border-inline-end:1px solid var(--border);background:rgba(0,0,0,.15);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);overflow-y:auto;position:sticky;top:0;max-height:calc(100vh - 120px);scrollbar-width:thin}
.sidebar-title{font-size:.62rem;text-transform:uppercase;letter-spacing:.08em;color:var(--text-muted);padding:4px 10px 2px;margin-top:4px}
.sidebar-item{display:flex;align-items:center;gap:8px;padding:7px 10px;border-radius:10px;border:1px solid transparent;background:transparent;color:var(--text-muted);cursor:pointer;font-size:.74rem;font-weight:500;font-family:var(--font-b);transition:all .2s;width:100%;text-align:start;position:relative;overflow:hidden}
.sidebar-item::after{content:"";position:absolute;inset:0;background:radial-gradient(circle at 50% 0%,var(--glow),transparent 70%);opacity:0;transition:opacity .2s;pointer-events:none;border-radius:inherit}
.sidebar-item:hover{background:rgba(255,255,255,.04);border-color:rgba(255,255,255,.06);color:var(--text)}
.sidebar-item:hover::after{opacity:.5}
.sidebar-item.active{background:rgba(255,255,255,.06);border-color:var(--accent);color:var(--accent);border-inline-start:3px solid var(--accent);box-shadow:0 0 12px var(--glow)}
.sidebar-item.active::after{opacity:1}
.sidebar-icon{font-size:1rem;flex-shrink:0;width:22px;text-align:center}
.sidebar-label{flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sidebar-count{font-size:.6rem;padding:1px 6px;border-radius:999px;background:rgba(0,0,0,.3);color:var(--text-muted);font-weight:700;min-width:18px;text-align:center}
.sidebar-item.active .sidebar-count{background:var(--accent);color:var(--bg)}
.main-area{flex:1;min-width:0;padding:0 4px}

/* Hamburger toggle */
.sidebar-toggle{display:none;background:rgba(0,0,0,.4);border:1px solid var(--border);color:var(--text);padding:6px 8px;border-radius:8px;font-size:1rem;cursor:pointer;transition:all .2s;line-height:1}
.sidebar-toggle:hover{border-color:var(--accent)}

/* Grid with sidebar: 2 columns */
.app-body .activity-grid{grid-template-columns:repeat(2,1fr)}

/* Tablet: icon-only sidebar */
@media(max-width:860px){
  .sidebar{width:52px;padding:8px 4px;align-items:center}
  .sidebar-label,.sidebar-count,.sidebar-title{display:none}
  .sidebar-item{justify-content:center;padding:8px}
  .sidebar-icon{width:auto}
  .app-body .activity-grid{grid-template-columns:repeat(2,1fr)}
}
/* Mobile: sidebar as drawer */
@media(max-width:540px){
  .sidebar-toggle{display:inline-flex}
  .sidebar{position:fixed;inset-block:0;inset-inline-start:0;z-index:90;width:240px;max-height:100vh;border-radius:0 14px 14px 0;box-shadow:4px 0 30px rgba(0,0,0,.5);background:var(--panel);transform:translateX(-100%);transition:transform .3s cubic-bezier(.4,0,.2,1)}
  [dir="rtl"] .sidebar{inset-inline-start:auto;inset-inline-end:0;transform:translateX(100%);border-radius:14px 0 0 14px;box-shadow:-4px 0 30px rgba(0,0,0,.5)}
  .sidebar.open{transform:translateX(0)}
  .sidebar-label,.sidebar-count,.sidebar-title{display:block}
  .sidebar-item{justify-content:flex-start}
  .sidebar-overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:89;backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px)}
  .sidebar-overlay.open{display:block}
  .app-body .activity-grid{grid-template-columns:1fr}
}
  """
