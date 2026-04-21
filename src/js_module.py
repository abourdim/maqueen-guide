#!/usr/bin/env python3
"""Bit-48 JS behavior, data placeholders for Maqueen build."""

SCRIPT = r'''
// ═══════════════════════════════════════════════════════════════════
// LOGO + UI i18n
// ═══════════════════════════════════════════════════════════════════
const LOGO_SVG = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 6.0 3.214096" preserveAspectRatio="xMidYMid meet" role="img"><g transform="translate(92.820084,-179.975632)" fill="currentColor" fill-rule="evenodd"><path d="M-90.269,180.707C-90.27,180.704,-90.281,180.555,-90.293,180.376C-90.305,180.197,-90.316,180.042,-90.317,180.032L-90.319,180.014L-90.296,180.014C-90.284,180.014,-90.259,180.012,-90.241,180.01C-90.222,180.008,-90.192,180.006,-90.173,180.005L-90.137,180.003L-90.129,180.131C-90.124,180.202,-90.119,180.27,-90.118,180.282L-90.116,180.304L-90.055,180.206C-90.022,180.153,-89.977,180.081,-89.957,180.048L-89.919,179.987L-89.883,179.985C-89.864,179.984,-89.825,179.981,-89.797,179.978C-89.769,179.976,-89.739,179.975,-89.73,179.976L-89.714,179.977L-89.826,180.146L-89.938,180.315L-89.797,180.491C-89.719,180.587,-89.656,180.668,-89.656,180.669C-89.656,180.671,-89.657,180.672,-89.659,180.672C-89.676,180.672,-89.857,180.684,-89.861,180.686C-89.866,180.687,-89.896,180.651,-89.971,180.554C-90.028,180.481,-90.076,180.421,-90.078,180.423C-90.08,180.424,-90.087,180.434,-90.093,180.446L-90.105,180.467L-90.097,180.582C-90.091,180.667,-90.09,180.697,-90.094,180.699C-90.099,180.703,-90.137,180.706,-90.21,180.709C-90.258,180.712,-90.268,180.711,-90.269,180.707z"/><path d="M-89.191,180.769C-89.268,180.753,-89.311,180.74,-89.36,180.717C-89.394,180.7,-89.472,180.651,-89.481,180.64C-89.485,180.635,-89.483,180.628,-89.446,180.493C-89.44,180.47,-89.428,180.473,-89.404,180.504C-89.35,180.572,-89.267,180.622,-89.189,180.636C-89.153,180.642,-89.15,180.642,-89.129,180.635C-89.093,180.624,-89.075,180.598,-89.082,180.566C-89.086,180.544,-89.122,180.514,-89.183,180.482C-89.255,180.445,-89.277,180.431,-89.31,180.4C-89.366,180.347,-89.383,180.292,-89.367,180.217C-89.35,180.135,-89.299,180.085,-89.207,180.06C-89.169,180.049,-89.099,180.048,-89.053,180.058C-88.98,180.074,-88.906,180.105,-88.844,180.146C-88.811,180.168,-88.807,180.171,-88.809,180.18C-88.811,180.186,-88.82,180.221,-88.83,180.258C-88.848,180.323,-88.849,180.326,-88.858,180.325C-88.863,180.324,-88.871,180.319,-88.875,180.313C-88.886,180.297,-88.933,180.252,-88.952,180.239C-89.003,180.204,-89.07,180.181,-89.113,180.185C-89.166,180.19,-89.196,180.228,-89.177,180.266C-89.168,180.285,-89.144,180.302,-89.079,180.337C-88.975,180.393,-88.925,180.435,-88.901,180.486C-88.888,180.514,-88.885,180.566,-88.894,180.603C-88.922,180.711,-89.011,180.774,-89.136,180.772C-89.157,180.772,-89.181,180.771,-89.191,180.769z"/><path d="M-91.104,180.904C-91.135,180.835,-91.199,180.692,-91.247,180.585C-91.294,180.479,-91.333,180.392,-91.332,180.391C-91.33,180.39,-91.249,180.353,-91.135,180.302C-91.081,180.278,-91.022,180.254,-91.004,180.248C-90.924,180.223,-90.849,180.234,-90.8,180.279C-90.776,180.3,-90.758,180.33,-90.743,180.373C-90.733,180.402,-90.731,180.413,-90.731,180.444C-90.731,180.474,-90.733,180.485,-90.742,180.507C-90.753,180.537,-90.772,180.572,-90.781,180.579C-90.784,180.582,-90.787,180.585,-90.787,180.587C-90.787,180.59,-90.751,180.61,-90.581,180.697C-90.521,180.729,-90.467,180.757,-90.462,180.76C-90.453,180.766,-90.457,180.768,-90.547,180.808C-90.599,180.831,-90.645,180.85,-90.65,180.85C-90.654,180.85,-90.72,180.816,-90.796,180.775L-90.934,180.7L-90.96,180.712C-90.974,180.718,-90.987,180.724,-90.987,180.724C-90.987,180.725,-90.965,180.775,-90.938,180.836C-90.91,180.898,-90.887,180.95,-90.887,180.953C-90.886,180.957,-90.91,180.97,-90.963,180.994C-91.005,181.013,-91.042,181.029,-91.044,181.029C-91.046,181.029,-91.073,180.972,-91.104,180.904z"/><path d="M-88.329,181.181C-88.367,181.155,-88.399,181.132,-88.4,181.131C-88.401,181.13,-88.362,181.073,-88.314,181.003C-88.266,180.933,-88.228,180.875,-88.229,180.874C-88.232,180.871,-88.365,180.779,-88.401,180.754L-88.419,180.742L-88.506,180.868C-88.554,180.937,-88.594,180.994,-88.596,180.994C-88.6,180.994,-88.742,180.897,-88.742,180.894C-88.742,180.893,-88.563,180.634,-88.382,180.374C-88.362,180.345,-88.345,180.321,-88.343,180.32C-88.34,180.32,-88.23,180.394,-88.196,180.419C-88.196,180.419,-88.227,180.465,-88.265,180.521C-88.304,180.576,-88.336,180.624,-88.337,180.626C-88.338,180.63,-88.305,180.655,-88.246,180.695C-88.195,180.73,-88.152,180.76,-88.15,180.76C-88.148,180.761,-88.114,180.715,-88.075,180.659C-88.036,180.602,-88.003,180.556,-88.001,180.556C-87.997,180.556,-87.857,180.653,-87.857,180.656C-87.857,180.662,-88.252,181.23,-88.256,181.23C-88.258,181.23,-88.291,181.208,-88.329,181.181z"/><path d="M-91.754,181.531C-91.889,181.512,-92.043,181.367,-92.083,181.222C-92.093,181.183,-92.092,181.109,-92.081,181.069C-92.049,180.958,-91.935,180.846,-91.825,180.817C-91.785,180.806,-91.704,180.807,-91.664,180.819C-91.604,180.836,-91.541,180.876,-91.484,180.932C-91.431,180.985,-91.395,181.04,-91.375,181.099C-91.365,181.129,-91.362,181.143,-91.361,181.18C-91.359,181.232,-91.363,181.26,-91.379,181.302C-91.403,181.365,-91.466,181.44,-91.53,181.482C-91.599,181.528,-91.67,181.544,-91.754,181.531z"/><path d="M-90.371,181.625C-90.383,181.62,-90.391,181.607,-90.417,181.549C-90.474,181.422,-90.475,181.421,-90.488,181.418C-90.495,181.417,-90.549,181.416,-90.608,181.416L-90.716,181.416L-90.724,181.431C-90.736,181.452,-90.772,181.484,-90.795,181.495C-90.86,181.525,-90.931,181.513,-90.977,181.463C-90.989,181.451,-91.003,181.43,-91.009,181.418C-91.02,181.397,-91.021,181.391,-91.021,181.36C-91.021,181.328,-91.02,181.322,-91.009,181.299C-90.993,181.265,-90.965,181.238,-90.931,181.222C-90.908,181.21,-90.901,181.209,-90.87,181.209C-90.808,181.208,-90.765,181.23,-90.732,181.277L-90.715,181.303L-90.576,181.304C-90.436,181.306,-90.436,181.306,-90.417,181.315C-90.398,181.324,-90.396,181.327,-90.375,181.369C-90.363,181.394,-90.335,181.456,-90.312,181.507C-90.289,181.558,-90.268,181.604,-90.265,181.608C-90.253,181.626,-90.259,181.629,-90.313,181.629C-90.34,181.628,-90.366,181.627,-90.371,181.625z"/><path d="M-87.689,181.815C-87.787,181.79,-87.87,181.716,-87.921,181.607C-87.961,181.522,-87.962,181.428,-87.925,181.347C-87.88,181.252,-87.77,181.161,-87.654,181.122C-87.641,181.117,-87.612,181.111,-87.59,181.107C-87.544,181.1,-87.501,181.104,-87.452,181.12C-87.349,181.153,-87.252,181.266,-87.222,181.386C-87.208,181.442,-87.216,181.523,-87.241,181.578C-87.277,181.657,-87.359,181.734,-87.458,181.782C-87.517,181.811,-87.551,181.819,-87.611,181.821C-87.649,181.822,-87.666,181.821,-87.689,181.815z"/><path d="M-91.18,182.039C-91.241,182.015,-91.284,181.955,-91.284,181.892C-91.285,181.847,-91.273,181.82,-91.236,181.783C-91.198,181.745,-91.182,181.739,-91.12,181.739C-91.078,181.739,-91.074,181.74,-91.05,181.751C-91.022,181.765,-90.989,181.795,-90.974,181.822L-90.964,181.838L-90.802,181.838L-90.64,181.838L-90.64,181.876C-90.64,181.897,-90.641,181.922,-90.642,181.932L-90.644,181.95L-90.804,181.95L-90.964,181.95L-90.981,181.974C-91,182.002,-91.037,182.034,-91.058,182.04C-91.065,182.042,-91.091,182.045,-91.116,182.046C-91.154,182.047,-91.163,182.046,-91.18,182.039z"/><path d="M-90.43,182.097C-90.443,182.092,-90.446,182.087,-90.446,182.064L-90.446,182.044L-90.474,182.031C-90.51,182.014,-90.523,182.002,-90.537,181.977C-90.553,181.948,-90.555,181.903,-90.543,181.874C-90.532,181.848,-90.495,181.813,-90.473,181.807C-90.455,181.802,-90.451,181.798,-90.448,181.778C-90.443,181.749,-90.442,181.746,-90.432,181.742C-90.426,181.739,-90.403,181.737,-90.376,181.737L-90.329,181.737L-90.326,181.748C-90.323,181.754,-90.322,181.818,-90.323,181.926C-90.324,182.07,-90.325,182.094,-90.33,182.098C-90.337,182.102,-90.418,182.102,-90.43,182.097z"/><path d="M-88.591,182.128L-88.591,181.999L-88.701,181.812C-88.762,181.709,-88.811,181.623,-88.811,181.621C-88.811,181.618,-88.783,181.617,-88.72,181.618L-88.628,181.619L-88.568,181.729C-88.535,181.789,-88.507,181.838,-88.505,181.838C-88.504,181.838,-88.477,181.789,-88.445,181.729L-88.387,181.619L-88.297,181.618C-88.248,181.618,-88.207,181.618,-88.207,181.619C-88.207,181.621,-88.414,181.971,-88.423,181.983C-88.427,181.989,-88.428,182.018,-88.428,182.124L-88.428,182.256L-88.509,182.256L-88.591,182.256L-88.591,182.128z"/><path d="M-89.308,182.253C-89.309,182.252,-89.31,182.227,-89.309,182.198L-89.309,182.146L-89.264,182.145L-89.218,182.144L-89.218,181.937L-89.218,181.73L-89.264,181.729L-89.309,181.728L-89.309,181.673L-89.309,181.619L-89.136,181.618L-88.962,181.617L-88.962,181.673L-88.962,181.73L-89.007,181.73L-89.052,181.73L-89.052,181.937L-89.052,182.144L-89.007,182.144L-88.962,182.144L-88.962,182.2L-88.962,182.256L-89.135,182.256C-89.229,182.256,-89.307,182.255,-89.308,182.253z"/><path d="M-89.906,182.262C-89.962,182.248,-89.99,182.234,-90.052,182.192C-90.115,182.15,-90.15,182.131,-90.192,182.113L-90.219,182.103L-90.219,182.053C-90.218,182.025,-90.218,181.942,-90.218,181.868L-90.217,181.733L-90.201,181.726C-90.162,181.711,-90.115,181.686,-90.064,181.652C-90.005,181.613,-89.953,181.586,-89.917,181.577C-89.823,181.553,-89.733,181.562,-89.646,181.605C-89.56,181.648,-89.498,181.721,-89.464,181.821C-89.453,181.85,-89.453,181.856,-89.453,181.919L-89.453,181.987L-89.467,182.025C-89.487,182.08,-89.51,182.117,-89.545,182.155C-89.598,182.21,-89.66,182.246,-89.739,182.264C-89.787,182.275,-89.858,182.274,-89.906,182.262z"/><path d="M-92.152,182.549C-92.178,182.546,-92.225,182.541,-92.257,182.537C-92.288,182.534,-92.338,182.529,-92.367,182.526C-92.396,182.522,-92.435,182.518,-92.454,182.516C-92.473,182.514,-92.513,182.509,-92.542,182.506C-92.571,182.503,-92.62,182.498,-92.651,182.494C-92.681,182.491,-92.729,182.486,-92.757,182.483C-92.786,182.48,-92.81,182.477,-92.811,182.476C-92.813,182.474,-92.8,182.436,-92.783,182.391C-92.754,182.314,-92.752,182.309,-92.742,182.307C-92.736,182.307,-92.705,182.311,-92.672,182.316C-92.64,182.321,-92.588,182.329,-92.559,182.334C-92.529,182.338,-92.495,182.343,-92.483,182.345C-92.471,182.347,-92.437,182.353,-92.408,182.357C-92.378,182.362,-92.339,182.368,-92.32,182.37C-92.302,182.373,-92.287,182.375,-92.287,182.375C-92.286,182.374,-92.373,182.314,-92.479,182.241C-92.586,182.168,-92.674,182.107,-92.675,182.106C-92.675,182.104,-92.663,182.068,-92.646,182.024L-92.616,181.945L-92.597,181.945C-92.587,181.945,-92.555,181.948,-92.528,181.951C-92.5,181.955,-92.455,181.961,-92.427,181.964C-92.399,181.967,-92.365,181.972,-92.351,181.974C-92.329,181.977,-92.302,181.98,-92.197,181.993C-92.178,181.995,-92.159,181.997,-92.154,181.997C-92.148,181.997,-92.215,181.952,-92.34,181.872C-92.448,181.804,-92.537,181.747,-92.538,181.745C-92.542,181.742,-92.481,181.576,-92.477,181.577C-92.471,181.578,-91.883,181.983,-91.883,181.986C-91.883,181.99,-91.945,182.161,-91.948,182.164C-91.951,182.167,-91.989,182.163,-92.237,182.138C-92.267,182.135,-92.31,182.131,-92.332,182.128C-92.354,182.126,-92.376,182.123,-92.38,182.122C-92.387,182.12,-92.388,182.121,-92.382,182.126C-92.379,182.129,-92.3,182.184,-92.206,182.249C-92.112,182.313,-92.034,182.368,-92.031,182.37C-92.024,182.377,-92.09,182.555,-92.099,182.554C-92.103,182.554,-92.126,182.551,-92.152,182.549z"/><path d="M-87.128,182.564C-87.143,182.559,-87.167,182.547,-87.182,182.537C-87.243,182.495,-87.275,182.442,-87.301,182.339C-87.31,182.305,-87.317,182.277,-87.318,182.277C-87.318,182.277,-87.335,182.28,-87.355,182.285C-87.475,182.316,-87.535,182.329,-87.537,182.328C-87.541,182.326,-87.582,182.16,-87.58,182.158C-87.579,182.158,-87.527,182.145,-87.466,182.129C-87.404,182.114,-87.299,182.089,-87.233,182.072C-87.167,182.056,-87.067,182.031,-87.011,182.018C-86.955,182.004,-86.907,181.993,-86.903,181.994C-86.898,181.995,-86.89,182.022,-86.867,182.117C-86.824,182.288,-86.82,182.309,-86.82,182.357C-86.82,182.467,-86.873,182.536,-86.98,182.566C-87.022,182.578,-87.092,182.577,-87.128,182.564z"/><path d="M-90.937,182.607C-90.969,182.591,-90.996,182.563,-91.011,182.532C-91.019,182.513,-91.021,182.505,-91.021,182.473C-91.021,182.439,-91.02,182.434,-91.008,182.41C-90.992,182.377,-90.966,182.351,-90.934,182.336C-90.911,182.325,-90.905,182.324,-90.864,182.324C-90.823,182.324,-90.818,182.325,-90.798,182.335C-90.769,182.35,-90.741,182.375,-90.725,182.4L-90.712,182.419L-90.597,182.418C-90.518,182.417,-90.48,182.416,-90.477,182.413C-90.474,182.41,-90.451,182.362,-90.425,182.304L-90.378,182.2L-90.329,182.199C-90.302,182.198,-90.276,182.2,-90.27,182.202C-90.26,182.206,-90.26,182.206,-90.266,182.22C-90.268,182.228,-90.285,182.266,-90.302,182.305C-90.32,182.343,-90.346,182.401,-90.36,182.432C-90.389,182.497,-90.407,182.52,-90.431,182.525C-90.438,182.527,-90.505,182.529,-90.581,182.53L-90.717,182.532L-90.73,182.552C-90.746,182.577,-90.771,182.599,-90.796,182.611C-90.813,182.619,-90.821,182.62,-90.863,182.62C-90.909,182.62,-90.91,182.62,-90.937,182.607z"/><path d="M-89.824,182.831C-89.825,182.829,-89.826,182.809,-89.826,182.786L-89.826,182.744L-88.327,182.744L-86.828,182.744L-86.828,182.789L-86.828,182.833L-88.325,182.833C-89.148,182.833,-89.822,182.832,-89.824,182.831z"/><path d="M-90.825,182.969L-90.825,182.926L-88.827,182.926L-86.828,182.926L-86.828,182.969L-86.828,183.012L-88.827,183.012L-90.825,183.012L-90.825,182.969z"/><path d="M-92.82,183.147L-92.82,183.105L-89.824,183.105L-86.828,183.105L-86.828,183.147L-86.828,183.19L-89.824,183.19L-92.82,183.19L-92.82,183.147z"/></g></svg>`;

const UI = __UI__;
function mk(id,title,part,meta,goal,needs,tip,blocks,codeJS,codePY,challenges){
  return {id,title,part,difficulty:meta.difficulty||1,time:meta.time||"—",v2:!!meta.v2,ia:!!meta.ia,goal,needs,tip,blocks,codeJS,codePY,challenges};
}

const A = __ACTIVITIES__;
// ═══════════════════════════════════════════════════════════════════
// VISUAL BLOCK TREES — MakeCode-style block data for each activity
// cat: basic|input|loops|logic|music|radio|variables|pins|math|game|bluetooth|neopixel|sonar|functions
// type: hat|stack|cblock|value
// ═══════════════════════════════════════════════════════════════════
const BT = __BT__;
// Assign blockTree to each activity
A.forEach(a => { if(BT[a.id]) a.blockTree = BT[a.id]; });

// Activity translations: {title, goal, tip, needs[], blocks[], challenges[].t}
// Code (JS/PY) is universal — not translated
const TR = __TR__;
// ═══════════════════════════════════════════════════════════════════
// STATE
// ═══════════════════════════════════════════════════════════════════
const STORAGE_KEY = "wdiy_microbit54_v3";
const defaultP = () => ({done:{},fav:{}});
function loadP(){try{const r=localStorage.getItem(STORAGE_KEY);if(!r)return defaultP();const o=JSON.parse(r);return{done:o.done||{},fav:o.fav||{}};}catch{return defaultP();}}
function saveP(p){localStorage.setItem(STORAGE_KEY,JSON.stringify(p));}
let progress = loadP();
let currentList = [];
let currentIndex = -1;
let lang = "fr";
let currentTopic = "all";

// ═══════════════════════════════════════════════════════════════════
// ACHIEVEMENT BADGES
// ═══════════════════════════════════════════════════════════════════
const BADGES = __BADGES__;
function checkBadges(){
  const earned = [];
  BADGES.forEach(b => {
    if(progress.badges && progress.badges[b.id]) return; // already earned
    let count = 0;
    if(b.topic === null){
      count = Object.keys(progress.done).length;
    } else if(TOPICS[b.topic]){
      count = TOPICS[b.topic].ids.filter(id => progress.done[id]).length;
    }
    if(count >= b.need){
      earned.push(b);
      if(!progress.badges) progress.badges = {};
      progress.badges[b.id] = Date.now();
      saveP(progress);
    }
  });
  return earned;
}

function getXP(){
  let xp = 0;
  Object.keys(progress.done).forEach(id => {
    const a = A.find(x => x.id === Number(id));
    if(a) xp += a.difficulty === 1 ? 10 : a.difficulty === 2 ? 20 : 30;
  });
  return xp;
}

function renderBadgeShelf(){
  const shelf = $("badgeShelf");
  if(!shelf) return;
  const xp = getXP();
  const xpLabel = lang==="ar"?"نقاط":lang==="en"?"XP":"XP";
  let h = `<div class="badge-xp">⚡ ${xp} ${xpLabel}</div><div class="badge-row">`;
  BADGES.forEach(b => {
    const earned = progress.badges && progress.badges[b.id];
    const name = b[lang] || b.fr;
    h += `<span class="badge-icon ${earned?'earned':'locked'}" title="${name}">${b.icon}</span>`;
  });
  h += `</div>`;
  shelf.innerHTML = h;
}

const TOPICS = __TOPICS__;
const $ = id => document.getElementById(id);
const grid = $("grid");
const overlay = $("overlay");

// ═══════════════════════════════════════════════════════════════════
// i18n HELPERS
// ═══════════════════════════════════════════════════════════════════
function t(key){ return UI[lang][key] || UI.fr[key] || key; }

// Get translated activity field, fallback to FR
function ta(a, field){
  if(lang === "fr") return a[field];
  const tr = TR[lang] && TR[lang][a.id];
  if(!tr) return a[field];
  const map = {title:"t",goal:"g",tip:"tip",needs:"n",blocks:"b"};
  const k = map[field];
  return k && tr[k] !== undefined ? tr[k] : a[field];
}

// Get translated challenges
function taChal(a){
  if(lang === "fr") return a.challenges;
  const tr = TR[lang] && TR[lang][a.id];
  if(!tr || !tr.c) return a.challenges;
  return a.challenges.map((ch, i) => ({t: tr.c[i] || ch.t, d: ch.d}));
}

function applyLang(){
  const isRTL = lang === "ar";
  document.documentElement.lang = lang;
  document.documentElement.dir = isRTL ? "rtl" : "ltr";

  $("mainTitle").textContent = t("title");
  $("mainSub").textContent = t("sub");
  $("lSearch").textContent = t("search");
  $("searchInput").placeholder = t("ph");
  $("lPart").textContent = t("part");
  $("lDiff").textContent = t("diff");
  $("lStatus").textContent = t("status");
  $("optAllParts").textContent = t("allParts");
  $("optSimple").textContent = t("simple");
  $("optAdv").textContent = t("advanced");
  $("optAllDiff").textContent = t("allDiff");
  $("optD1").textContent = t("d1");
  $("optD2").textContent = t("d2");
  $("optD3").textContent = t("d3");
  $("optAllStat").textContent = t("allStat");
  $("optTodo").textContent = t("todo");
  $("optDone").textContent = t("done");
  $("optFav").textContent = t("fav");
  $("lV2").textContent = t("v2only");
  $("lIA").textContent = t("iaonly");
  $("lReset").textContent = t("reset");
  $("lRandom").textContent = t("random");
  $("tabInfo").textContent = t("tabInfo");
  $("tabBlocks").textContent = t("tabBlocks");
  $("tabJS").innerHTML = '<span class="tab-lang-badge js-badge">JS</span> JavaScript';
  $("tabPY").innerHTML = '<span class="tab-lang-badge py-badge">PY</span> Python';
  $("tabChal").textContent = t("tabChal");
  if(typeof updateSimLabels==="function") updateSimLabels();
  $("mNeedsLabel").textContent = t("needsLabel");
  $("codeTip").innerHTML = t("codeTip");
  $("codeTipPY").innerHTML = t("codeTipPY") || t("codeTip");
  $("saveHint").textContent = t("saveHint");
  $("prevBtn").textContent = t("prev");
  $("nextBtn").textContent = t("next");

  // Sidebar labels
  $("sbSimple").textContent = t("sbSimple");
  $("sbAdvanced").textContent = t("sbAdvanced");
  document.querySelectorAll('#sidebar .sidebar-item[data-topic]').forEach(btn => {
    const topic = btn.dataset.topic;
    const key = topic === 'all' ? 'sbAll' : 'sb' + topic.charAt(0).toUpperCase() + topic.slice(1);
    const labelEl = btn.querySelector('.sidebar-label');
    if (labelEl) labelEl.textContent = t(key);
  });

  document.title = t("title") + " — Workshop DIY";
  render();
  // Re-render modal if open
  if(overlay.classList.contains("open") && currentList[currentIndex]) openModal();
}

// ═══════════════════════════════════════════════════════════════════
// HELPERS
// ═══════════════════════════════════════════════════════════════════
function esc(s){return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");}

// ═══════════════════════════════════════════════════════════════════
// VISUAL BLOCK RENDERER
// ═══════════════════════════════════════════════════════════════════
function renderArg(a){
  if(typeof a==="string") return `<span class="varg str">${esc(a)}</span>`;
  if(typeof a==="number") return `<span class="varg round">${a}</span>`;
  if(a && a.label) return renderOneBlock(a);
  return `<span class="varg round">${esc(String(a))}</span>`;
}
function renderOneBlock(b){
  const cat = "cat-"+(b.cat||"basic");
  const type = b.type||"stack";
  if(type==="cblock"){
    const elseLabel = lang==="ar"?"وإلا":lang==="en"?"else":"sinon";
    let h = `<div class="vblock cblock ${cat}"><div class="cblock-row">${esc(b.label)}`;
    if(b.arg!==undefined) h += " "+renderArg(b.arg);
    h += `</div><div class="cblock-body">`;
    if(b.children) b.children.forEach(c => { h += renderOneBlock(c); });
    if(!b.children || b.children.length===0) h += `<div style="height:24px"></div>`;
    h += `</div>`;
    if(b.else){
      h += `<div class="cblock-else">${elseLabel}</div><div class="cblock-body">`;
      b.else.forEach(c => { h += renderOneBlock(c); });
      h += `</div>`;
    }
    h += `<div class="cblock-cap"></div></div>`;
    return h;
  }
  if(type==="hat" && b.children && b.children.length > 0){
    // Hat block with children: label row + body
    let h = `<div class="vblock hat ${cat}"><div class="hat-label">${esc(b.label)}`;
    if(b.arg!==undefined) h += " "+renderArg(b.arg);
    if(b.args) b.args.forEach(a => { h += " "+renderArg(a); });
    h += `</div><div class="hat-body">`;
    b.children.forEach(c => { h += renderOneBlock(c); });
    h += `</div></div>`;
    return h;
  }
  // Simple stack/hat block (no children)
  let h = `<div class="vblock ${type} ${cat}">${esc(b.label)}`;
  if(b.arg!==undefined) h += " "+renderArg(b.arg);
  if(b.args) b.args.forEach(a => { h += " "+renderArg(a); });
  h += `</div>`;
  return h;
}
// ═══════════════════════════════════════════════════════════════════
// MAKECODE IFRAME BLOCK RENDERER
// Protocol: https://makecode.com/blocks-embed (gh-pages-embed.js)
// ═══════════════════════════════════════════════════════════════════
let mcRenderReady = false;
const mcRenderQueue = [];
const mcRenderCache = {};

window.addEventListener("message", function(ev){
  if(!ev.data || typeof ev.data !== "object") return;
  const msg = ev.data;
  if(msg.source === "makecode" || msg.type === "renderready"){
    mcRenderReady = true;
    // Process queued requests
    while(mcRenderQueue.length > 0){
      const req = mcRenderQueue.shift();
      sendMCRender(req.id, req.code);
    }
  }
  if(msg.type === "renderblocks" && msg.id){
    // Cache the result
    mcRenderCache[msg.id] = {uri:msg.uri, width:msg.width, height:msg.height, svg:msg.svg};
    // Update the DOM if this activity is still displayed
    const container = $("mBlocksMC");
    if(container && container.dataset.mcId === msg.id){
      container.innerHTML = "";
      const img = document.createElement("img");
      img.src = msg.uri;
      img.width = msg.width;
      img.height = msg.height;
      img.alt = "MakeCode blocks";
      img.style.maxWidth = "100%";
      img.style.height = "auto";
      container.appendChild(img);
      // Hide CSS fallback now that real blocks loaded
      const fb = $("mBlocksFallback");
      if(fb) fb.style.display = "none";
    }
  }
});

function sendMCRender(id, code){
  const frame = $("mcRenderFrame");
  if(!frame || !frame.contentWindow) return;
  frame.contentWindow.postMessage({
    type: "renderblocks",
    id: id,
    code: code
  }, "https://makecode.microbit.org");
}

function renderMakeCodeBlocks(a){
  const mcContainer = $("mBlocksMC");
  const fallback = $("mBlocksFallback");
  const mcId = "act-" + a.id;
  mcContainer.dataset.mcId = mcId;
  lastSyncedCode = a.codeJS;
  markCodeSynced();

  // Show CSS fallback immediately
  if(a.blockTree){
    fallback.innerHTML = renderBlocks(a.blockTree);
  } else {
    const blocks = ta(a,"blocks");
    fallback.innerHTML = (Array.isArray(blocks)?blocks:a.blocks).map((b,i) => `<div class="block-step"><span class="step-num">${i+1}</span>${esc(b)}</div>`).join("");
  }

  // Check cache first
  if(mcRenderCache[mcId]){
    const c = mcRenderCache[mcId];
    mcContainer.innerHTML = "";
    const img = document.createElement("img");
    img.src = c.uri;
    img.width = c.width;
    img.height = c.height;
    img.alt = "MakeCode blocks";
    img.style.maxWidth = "100%";
    img.style.height = "auto";
    mcContainer.appendChild(img);
    mcContainer.style.display = "";
    fallback.style.display = "none";
    return;
  }

  // Show loading + CSS fallback while waiting
  mcContainer.innerHTML = '<div class="mc-loading">' + (lang==="ar"?"جاري تحميل المكعبات من MakeCode":lang==="en"?"Loading blocks from MakeCode":"Chargement des blocs MakeCode") + '</div>';
  mcContainer.style.display = "";
  fallback.style.display = "";

  // Request rendering from iframe
  if(mcRenderReady){
    sendMCRender(mcId, a.codeJS);
  } else {
    mcRenderQueue.push({id: mcId, code: a.codeJS});
  }

  // Timeout: if no response in 5s, hide MC container and show fallback only
  setTimeout(() => {
    if(mcContainer.dataset.mcId === mcId && !mcRenderCache[mcId]){
      mcContainer.style.display = "none";
      fallback.style.display = "";
    }
  }, 5000);
}

// ═══════════════════════════════════════════════════════════════════
// LED ICON PATTERNS (5x5 boolean arrays)
// ═══════════════════════════════════════════════════════════════════
const LED_ICONS = {
  Heart:      [0,1,0,1,0, 1,1,1,1,1, 1,1,1,1,1, 0,1,1,1,0, 0,0,1,0,0],
  SmallHeart: [0,0,0,0,0, 0,1,0,1,0, 0,1,1,1,0, 0,0,1,0,0, 0,0,0,0,0],
  Happy:      [0,0,0,0,0, 0,1,0,1,0, 0,0,0,0,0, 1,0,0,0,1, 0,1,1,1,0],
  Sad:        [0,0,0,0,0, 0,1,0,1,0, 0,0,0,0,0, 0,1,1,1,0, 1,0,0,0,1],
  Meh:        [0,0,0,0,0, 0,1,0,1,0, 0,0,0,0,0, 0,0,0,0,0, 1,1,1,1,1],
  Yes:        [0,0,0,0,0, 0,0,0,0,1, 0,0,0,1,0, 1,0,1,0,0, 0,1,0,0,0],
  No:         [1,0,0,0,1, 0,1,0,1,0, 0,0,1,0,0, 0,1,0,1,0, 1,0,0,0,1],
  Flash:      [0,0,1,0,0, 0,1,1,0,0, 1,1,1,1,1, 0,0,1,1,0, 0,0,1,0,0],
  ArrowNorth: [0,0,1,0,0, 0,1,1,1,0, 1,0,1,0,1, 0,0,1,0,0, 0,0,1,0,0],
  ArrowSouth: [0,0,1,0,0, 0,0,1,0,0, 1,0,1,0,1, 0,1,1,1,0, 0,0,1,0,0],
  Skull:      [0,1,1,1,0, 1,0,1,0,1, 1,1,1,1,1, 0,1,1,1,0, 0,1,1,1,0],
  Asleep:     [0,0,0,0,0, 1,1,0,1,1, 0,0,0,0,0, 0,1,1,1,0, 0,0,0,0,0],
  Target:     [0,0,1,0,0, 0,1,1,1,0, 1,1,0,1,1, 0,1,1,1,0, 0,0,1,0,0],
  Square:     [1,1,1,1,1, 1,0,0,0,1, 1,0,0,0,1, 1,0,0,0,1, 1,1,1,1,1],
  SmallSquare:[0,0,0,0,0, 0,1,1,1,0, 0,1,1,1,0, 0,1,1,1,0, 0,0,0,0,0],
  Scissors:   [1,0,0,0,1, 0,1,0,1,0, 0,0,1,0,0, 0,1,0,1,0, 1,0,0,0,1],
  House:      [0,0,1,0,0, 0,1,1,1,0, 1,1,1,1,1, 0,1,1,1,0, 0,1,0,1,0],
  Duck:       [0,1,1,0,0, 1,1,1,0,0, 0,1,1,1,1, 0,1,1,1,0, 0,0,0,0,0]
};
// Digit patterns for showNumber
const LED_DIGITS = {
  0:[0,1,1,1,0, 1,0,0,1,1, 1,0,1,0,1, 1,1,0,0,1, 0,1,1,1,0],
  1:[0,0,1,0,0, 0,1,1,0,0, 0,0,1,0,0, 0,0,1,0,0, 0,1,1,1,0],
  2:[1,1,1,1,0, 0,0,0,0,1, 0,1,1,1,0, 1,0,0,0,0, 1,1,1,1,1],
  3:[1,1,1,1,0, 0,0,0,0,1, 0,1,1,1,0, 0,0,0,0,1, 1,1,1,1,0],
  4:[1,0,0,1,0, 1,0,0,1,0, 1,1,1,1,1, 0,0,0,1,0, 0,0,0,1,0],
  5:[1,1,1,1,1, 1,0,0,0,0, 1,1,1,1,0, 0,0,0,0,1, 1,1,1,1,0],
  6:[0,1,1,1,0, 1,0,0,0,0, 1,1,1,1,0, 1,0,0,0,1, 0,1,1,1,0],
  7:[1,1,1,1,1, 0,0,0,1,0, 0,0,1,0,0, 0,1,0,0,0, 0,1,0,0,0],
  8:[0,1,1,1,0, 1,0,0,0,1, 0,1,1,1,0, 1,0,0,0,1, 0,1,1,1,0],
  9:[0,1,1,1,0, 1,0,0,0,1, 0,1,1,1,1, 0,0,0,0,1, 0,1,1,1,0]
};

function renderLedGrid(pattern){
  let h = '<div class="led-sim"><div class="led-grid">';
  for(let i=0;i<25;i++){
    h += `<div class="led-cell${pattern&&pattern[i]?' on':''}"></div>`;
  }
  h += '</div></div>';
  return h;
}

function detectLedPattern(code){
  // showIcon(IconNames.XXX) → lookup pattern
  const iconMatch = code.match(/showIcon\(IconNames\.(\w+)\)/);
  if(iconMatch && LED_ICONS[iconMatch[1]]) return LED_ICONS[iconMatch[1]];
  // showLeds with # and . pattern
  const ledsMatch = code.match(/showLeds\s*\(\s*`([^`]+)`/);
  if(ledsMatch){
    const p = ledsMatch[1].replace(/[^#.]/g,'').split('').map(c=>c==='#'?1:0);
    if(p.length===25) return p;
  }
  // showNumber
  const numMatch = code.match(/showNumber\((\d)\)/);
  if(numMatch && LED_DIGITS[numMatch[1]]) return LED_DIGITS[numMatch[1]];
  return null;
}

// ═══════════════════════════════════════════════════════════════════
// LESSON GENERATOR — auto-generates concept, steps, diagram
// ═══════════════════════════════════════════════════════════════════
function generateLesson(a){
  const L = lang;
  const js = a.codeJS;
  const blocks = ta(a,"blocks");

  // ── CONCEPT: explain the key programming concept ──
  const concepts = [];
  if(js.includes("forever")) concepts.push({
    fr:"La <strong>boucle infinie</strong> (<code>forever</code>) répète le code sans fin. C'est le cœur de la plupart des programmes micro:bit : lire un capteur → réagir → recommencer.",
    en:"The <strong>infinite loop</strong> (<code>forever</code>) repeats code endlessly. It's the core of most micro:bit programs: read sensor → react → repeat.",
    ar:"<strong>الحلقة اللانهائية</strong> (<code>forever</code>) تكرر الكود بلا توقف. هي أساس معظم برامج المايكروبت: قراءة مستشعر ← تفاعل ← تكرار."
  });
  if(js.includes("onButtonPressed")) concepts.push({
    fr:"Un <strong>événement bouton</strong> déclenche du code quand tu appuies sur A, B ou A+B. C'est de la <strong>programmation événementielle</strong> : le programme attend une action.",
    en:"A <strong>button event</strong> triggers code when you press A, B, or A+B. This is <strong>event-driven programming</strong>: the program waits for an action.",
    ar:"<strong>حدث الزر</strong> يشغّل الكود عند الضغط على A أو B أو A+B. هذه <strong>برمجة بالأحداث</strong>: البرنامج ينتظر إجراءً."
  });
  if(js.includes("onGesture")||js.includes("Shake")) concepts.push({
    fr:"Le <strong>geste</strong> (secouer, incliner…) est détecté par l'<strong>accéléromètre</strong>, un capteur de mouvement intégré à la carte.",
    en:"A <strong>gesture</strong> (shake, tilt…) is detected by the <strong>accelerometer</strong>, a motion sensor built into the board.",
    ar:"<strong>الإيماءة</strong> (هزّ، ميل…) يكتشفها <strong>مقياس التسارع</strong>، وهو مستشعر حركة مدمج في البطاقة."
  });
  if(js.includes("if")) concepts.push({
    fr:"La <strong>condition</strong> (<code>if/else</code>) permet au programme de <strong>prendre des décisions</strong> : si une condition est vraie → faire A, sinon → faire B.",
    en:"A <strong>condition</strong> (<code>if/else</code>) lets the program <strong>make decisions</strong>: if something is true → do A, otherwise → do B.",
    ar:"<strong>الشرط</strong> (<code>if/else</code>) يسمح للبرنامج بـ<strong>اتخاذ قرارات</strong>: إذا تحقق الشرط ← نفّذ أ، وإلا ← نفّذ ب."
  });
  if(js.includes("randint")) concepts.push({
    fr:"<code>randint(min, max)</code> génère un <strong>nombre aléatoire</strong>. L'ordinateur choisit au hasard — comme lancer un dé !",
    en:"<code>randint(min, max)</code> generates a <strong>random number</strong>. The computer picks randomly — like rolling a dice!",
    ar:"<code>randint(min, max)</code> يولّد <strong>رقماً عشوائياً</strong>. الحاسوب يختار عشوائياً — مثل رمي النرد!"
  });
  if(js.includes("radio.")) concepts.push({
    fr:"Le <strong>radio</strong> permet à 2 micro:bits de communiquer sans fil. Les cartes sur le <strong>même groupe</strong> s'envoient des données.",
    en:"<strong>Radio</strong> lets 2 micro:bits communicate wirelessly. Boards on the <strong>same group</strong> send data to each other.",
    ar:"<strong>الراديو</strong> يتيح لبطاقتي مايكروبت التواصل لاسلكياً. البطاقات على <strong>نفس المجموعة</strong> ترسل بيانات لبعضها."
  });
  if(js.includes("pins.")) concepts.push({
    fr:"Les <strong>broches</strong> (P0, P1, P2) connectent des composants externes. On peut <strong>lire</strong> (capteur) ou <strong>écrire</strong> (LED, moteur) des valeurs.",
    en:"<strong>Pins</strong> (P0, P1, P2) connect external components. You can <strong>read</strong> (sensor) or <strong>write</strong> (LED, motor) values.",
    ar:"<strong>المنافذ</strong> (P0، P1، P2) تربط مكونات خارجية. يمكنك <strong>قراءة</strong> (مستشعر) أو <strong>كتابة</strong> (LED، محرك) القيم."
  });
  if(js.includes("let ")||js.includes("var ")) concepts.push({
    fr:"Une <strong>variable</strong> est une boîte mémoire avec un nom. On y stocke une valeur (nombre, texte) qu'on peut lire et modifier.",
    en:"A <strong>variable</strong> is a named memory box. You store a value (number, text) that you can read and change.",
    ar:"<strong>المتغير</strong> هو صندوق ذاكرة باسم. تخزّن فيه قيمة (رقم، نص) يمكنك قراءتها وتعديلها."
  });
  if(js.includes("music.")) concepts.push({
    fr:"Le micro:bit peut <strong>jouer des sons</strong>. Une note = une fréquence (Hz) + une durée (ms). Exemple: Do = 262 Hz.",
    en:"The micro:bit can <strong>play sounds</strong>. A note = a frequency (Hz) + duration (ms). Example: middle C = 262 Hz.",
    ar:"المايكروبت يمكنه <strong>تشغيل أصوات</strong>. النوتة = تردد (Hz) + مدة (ms). مثال: دو الوسطى = 262 Hz."
  });
  if(js.includes("function ")) concepts.push({
    fr:"Une <strong>fonction</strong> est un bloc de code réutilisable. Tu lui donnes un nom, et tu peux l'<strong>appeler</strong> plusieurs fois sans réécrire le code.",
    en:"A <strong>function</strong> is a reusable code block. You give it a name and <strong>call</strong> it multiple times without rewriting the code.",
    ar:"<strong>الدالة</strong> هي كتلة كود قابلة لإعادة الاستخدام. تسمّيها وتستدعيها عدة مرات دون إعادة كتابة الكود."
  });
  if(concepts.length===0) concepts.push({
    fr:"Cette activité utilise les <strong>blocs de base</strong> de MakeCode. Chaque bloc correspond à une action que la micro:bit exécute.",
    en:"This activity uses <strong>basic MakeCode blocks</strong>. Each block corresponds to an action the micro:bit executes.",
    ar:"هذا النشاط يستخدم <strong>المكعبات الأساسية</strong> لـ MakeCode. كل مكعب يقابل إجراءً ينفذه المايكروبت."
  });
  $("mConcept").innerHTML = concepts.map(c => c[L]||c.fr).join("<br><br>");

  // ── STEPS: guided walkthrough ──
  const stepsData = [];
  stepsData.push({fr:"Ouvre <strong>MakeCode</strong> (makecode.microbit.org) et crée un <strong>nouveau projet</strong>.",en:"Open <strong>MakeCode</strong> (makecode.microbit.org) and create a <strong>new project</strong>.",ar:"افتح <strong>MakeCode</strong> (makecode.microbit.org) وأنشئ <strong>مشروعاً جديداً</strong>."});

  const bArr = Array.isArray(blocks)?blocks:a.blocks;
  bArr.forEach(b => {
    stepsData.push({fr:"Ajoute le bloc : <strong>"+esc(b)+"</strong>",en:"Add the block: <strong>"+esc(b)+"</strong>",ar:"أضف المكعب: <strong>"+esc(b)+"</strong>"});
  });

  stepsData.push({fr:"Clique sur <strong>▶ Simuler</strong> pour tester dans le simulateur.",en:"Click <strong>▶ Simulate</strong> to test in the simulator.",ar:"اضغط <strong>▶ محاكاة</strong> للاختبار في المحاكي."});
  stepsData.push({fr:"<strong>Télécharge</strong> le fichier .hex sur ta micro:bit pour tester en vrai !",en:"<strong>Download</strong> the .hex file to your micro:bit to test for real!",ar:"<strong>حمّل</strong> ملف .hex على المايكروبت للاختبار الحقيقي!"});

  $("mSteps").innerHTML = stepsData.map((s,i) =>
    `<div class="info-step"><span class="step-n">${i+1}</span><span class="step-text">${s[L]||s.fr}</span></div>`
  ).join("");

  // ── DIAGRAM: LED simulator or wiring diagram ──
  const ledPattern = detectLedPattern(js);
  if(ledPattern){
    $("infoDiagramTitle").textContent = lang==="ar"?"📐 معاينة LED":lang==="en"?"📐 LED Preview":"📐 Aperçu LED";
    $("mDiagram").innerHTML = renderLedGrid(ledPattern);
  } else if(js.includes("pins.") && (js.includes("P0")||js.includes("P1")||js.includes("P2"))){
    $("mDiagram").innerHTML = `<pre style="margin:0;font-family:monospace;font-size:.7rem;color:var(--accent)">    ┌─────────────────┐
    │   micro:bit      │
    │  [A]       [B]   │
    │   ╔═══════════╗  │
    │   ║  5×5 LEDs  ║  │
    │   ╚═══════════╝  │
    └──┬──┬──┬──┬──┬──┘
       P0 P1 P2 3V GND
       │        │   │
       └─ composant ─┘</pre>`;
  } else if(js.includes("radio.")){
    $("mDiagram").innerHTML = `<pre style="margin:0;font-family:monospace;font-size:.7rem;color:var(--accent)">  micro:bit A        micro:bit B
  ┌────────┐  ~~~~>  ┌────────┐
  │ [A][B] │  radio  │ [A][B] │
  │ ╔════╗ │  <~~~~  │ ╔════╗ │
  │ ║LED ║ │ grp: 7  │ ║LED ║ │
  │ ╚════╝ │         │ ╚════╝ │
  └────────┘         └────────┘</pre>`;
  } else {
    // Default: empty LED grid (interactive)
    $("infoDiagramTitle").textContent = lang==="ar"?"📐 شاشة LED":lang==="en"?"📐 LED Screen":"📐 Écran LED";
    $("mDiagram").innerHTML = renderLedGrid(null);
  }
}

// ═══════════════════════════════════════════════════════════════════
// FLOWCHART + PSEUDOCODE GENERATOR
// ═══════════════════════════════════════════════════════════════════
function generateFlowAndPseudo(a){
  const js = a.codeJS;
  const L = lang;
  const kw = {
    start:{fr:"DÉBUT",en:"START",ar:"بداية"},
    end:{fr:"FIN",en:"END",ar:"نهاية"},
    forever:{fr:"RÉPÉTER indéfiniment",en:"REPEAT forever",ar:"تكرار دائم"},
    onBtn:{fr:"QUAND bouton pressé",en:"WHEN button pressed",ar:"عند ضغط الزر"},
    onShake:{fr:"QUAND secouer",en:"WHEN shake",ar:"عند الهزّ"},
    onLogo:{fr:"QUAND logo touché",en:"WHEN logo touched",ar:"عند لمس الشعار"},
    if:{fr:"SI",en:"IF",ar:"إذا"},
    then:{fr:"ALORS",en:"THEN",ar:"فعندها"},
    else:{fr:"SINON",en:"ELSE",ar:"وإلا"},
    show:{fr:"AFFICHER",en:"SHOW",ar:"اعرض"},
    set:{fr:"DÉFINIR",en:"SET",ar:"عرّف"},
    play:{fr:"JOUER",en:"PLAY",ar:"شغّل"},
    wait:{fr:"ATTENDRE",en:"WAIT",ar:"انتظر"},
    send:{fr:"ENVOYER",en:"SEND",ar:"أرسل"},
    read:{fr:"LIRE",en:"READ",ar:"اقرأ"}
  };
  const K = key => kw[key][L]||kw[key].fr;

  // ── FLOWCHART ──
  const nodes = [];
  const arrow = () => '<div class="flow-arrow"></div>';
  const node = (cls, text) => `<div class="flow-node ${cls}">${esc(text)}</div>`;

  nodes.push(node("start", K("start")));
  nodes.push(arrow());

  // Detect event handlers
  const events = [];
  if(js.includes("onButtonPressed(Button.A")) events.push({ev:K("onBtn")+" A"});
  if(js.includes("onButtonPressed(Button.B")) events.push({ev:K("onBtn")+" B"});
  if(js.includes("onButtonPressed(Button.AB")) events.push({ev:K("onBtn")+" A+B"});
  if(js.includes("onGesture(Gesture.Shake")) events.push({ev:K("onShake")});
  if(js.includes("onLogoEvent")) events.push({ev:K("onLogo")});
  if(js.includes("forever")) events.push({ev:K("forever")});

  if(events.length > 0){
    events.forEach(e => {
      nodes.push(node("io", "⚡ "+e.ev));
      nodes.push(arrow());
    });
  }

  // Detect key actions
  if(js.includes("showString")) nodes.push(node("process", K("show")+" texte"));
  else if(js.includes("showIcon")) nodes.push(node("process", K("show")+" icône"));
  else if(js.includes("showNumber")) nodes.push(node("process", K("show")+" nombre"));
  else if(js.includes("showLeds")) nodes.push(node("process", K("show")+" LEDs"));

  if(js.includes("if")) {
    nodes.push(arrow());
    const condMatch = js.match(/if\s*\(([^)]{1,40})\)/);
    const cond = condMatch ? condMatch[1].replace(/[{}]/g,'').trim() : "condition";
    nodes.push(node("decision", K("if")+" "+cond+" ?"));
    nodes.push(arrow());
  }

  if(js.includes("music.")) { nodes.push(node("process", K("play")+" 🎵")); nodes.push(arrow()); }
  if(js.includes("radio.send")) { nodes.push(node("process", K("send")+" 📻")); nodes.push(arrow()); }
  if(js.includes("pause(")) { nodes.push(node("process", K("wait")+" ⏱")); nodes.push(arrow()); }

  nodes.push(node("end", K("end")));

  $("mFlow").innerHTML = nodes.join("");

  // ── PSEUDOCODE ──
  const lines = [];
  const pk = t => `<span class="pk">${t}</span>`;
  const pv = t => `<span class="pv">${t}</span>`;
  const pf = t => `<span class="pf">${t}</span>`;
  const pc = t => `<span class="pc">${t}</span>`;

  lines.push(pk(K("start")));

  // Variables
  const vars = js.match(/let\s+(\w+)\s*=\s*([^;\n]+)/g);
  if(vars) vars.forEach(v => {
    const m = v.match(/let\s+(\w+)\s*=\s*(.+)/);
    if(m) lines.push("  "+pk(K("set"))+" "+pf(m[1])+" ← "+pv(m[2].trim()));
  });

  // Events
  if(js.includes("forever")){
    lines.push("");
    lines.push(pk(K("forever"))+" :");
  }
  if(js.includes("onButtonPressed(Button.A")) lines.push(pk(K("onBtn"))+" A :");
  if(js.includes("onButtonPressed(Button.B")) lines.push(pk(K("onBtn"))+" B :");
  if(js.includes("onGesture(Gesture.Shake")) lines.push(pk(K("onShake"))+" :");

  // Actions
  const showStr = js.match(/showString\("([^"]+)"\)/);
  if(showStr) lines.push("  "+pk(K("show"))+" "+pv('"'+showStr[1]+'"'));
  const showIcon = js.match(/showIcon\(IconNames\.(\w+)\)/);
  if(showIcon) lines.push("  "+pk(K("show"))+" icône "+pv(showIcon[1]));
  const showNum = js.match(/showNumber\((\w+)\)/);
  if(showNum) lines.push("  "+pk(K("show"))+" "+pv(showNum[1]));

  // Conditions
  const ifMatch = js.match(/if\s*\(([^)]{1,60})\)/);
  if(ifMatch){
    lines.push("  "+pk(K("if"))+" "+pv(ifMatch[1].trim())+" "+pk(K("then")));
    lines.push("    "+pc("// ...actions..."));
    if(js.includes("} else")) lines.push("  "+pk(K("else")));
    if(js.includes("} else")) lines.push("    "+pc("// ...actions..."));
  }

  if(js.includes("pause(")) lines.push("  "+pk(K("wait"))+" "+pv("ms"));
  if(js.includes("radio.send")) lines.push("  "+pk(K("send"))+" "+pv("radio"));

  lines.push("");
  lines.push(pk(K("end")));

  $("mPseudo").innerHTML = lines.join("\n");
}
// ═══════════════════════════════════════════════════════════════════
// SYNTAX HIGHLIGHTING (JS + Python)
// ═══════════════════════════════════════════════════════════════════
function highlightJS(code){
  return esc(code)
    .replace(/(\/\/[^\n]*)/g,'<span class="hl-comment">$1</span>')
    .replace(/\b(function|let|var|const|if|else|while|for|return|true|false|new|this)\b/g,'<span class="hl-keyword">$1</span>')
    .replace(/\b(\d+)\b/g,'<span class="hl-number">$1</span>')
    .replace(/(&quot;[^&]*?&quot;)/g,'<span class="hl-string">$1</span>');
}

function highlightPY(code){
  const e = esc(code);
  const tokens = [];
  let r = e;
  while(r.length > 0){
    let m;
    if((m=r.match(/^(#[^\n]*)/))){tokens.push('<span class="hl-comment">'+m[1]+'</span>');r=r.slice(m[0].length);continue;}
    if((m=r.match(/^(&quot;[^&]*?&quot;)/))){tokens.push('<span class="hl-string">'+m[1]+'</span>');r=r.slice(m[0].length);continue;}
    if((m=r.match(/^('[^']*?')/))){tokens.push('<span class="hl-string">'+m[1]+'</span>');r=r.slice(m[0].length);continue;}
    if((m=r.match(/^(def|if|elif|else|while|for|in|return|import|from|global|not|and|or|True|False|range|len|min|max|abs)\b/))){tokens.push('<span class="hl-keyword">'+m[1]+'</span>');r=r.slice(m[0].length);continue;}
    if((m=r.match(/^(\d+)/))){tokens.push('<span class="hl-number">'+m[1]+'</span>');r=r.slice(m[0].length);continue;}
    tokens.push(r[0]);r=r.slice(1);
  }
  return tokens.join('');
}

function renderBlocks(tree){
  if(!tree || !Array.isArray(tree)) return "";
  let h = `<div class="block-canvas">`;
  tree.forEach(b => { h += renderOneBlock(b); });
  h += `</div>`;
  return h;
}
function getStatus(a){if(progress.fav[a.id])return"fav";if(progress.done[a.id])return"done";return"todo";}

function tagHTML(a){
  let h = "";
  const sl = a.part==="simple" ? t("simpleTag") : t("advTag");
  h += `<span class="tag ${a.part==='simple'?'simple':'adv'}">${sl}</span>`;
  h += `<span class="tag d${a.difficulty}">${'⭐'.repeat(a.difficulty)}</span>`;
  h += `<span class="tag">⏱ ${esc(a.time)}</span>`;
  if(a.v2) h += `<span class="tag v2">V2</span>`;
  if(a.ia) h += `<span class="tag ia">${lang==="ar"?"ذ.إ.":"IA"}</span>`;
  return h;
}

// ═══════════════════════════════════════════════════════════════════
// RENDER
// ═══════════════════════════════════════════════════════════════════
function render(){
  const q = $("searchInput").value.trim().toLowerCase();
  const part = $("partSelect").value;
  const diff = $("diffSelect").value;
  const status = $("statusSelect").value;
  const v2 = $("onlyV2").checked;
  const ia = $("onlyIA").checked;

  let list = A.slice();
  if(currentTopic !== "all") {
    const topicIds = TOPICS[currentTopic] && TOPICS[currentTopic].ids;
    if(topicIds) list = list.filter(a => topicIds.includes(a.id));
  }
  if(q) list = list.filter(a => {
    const title = ta(a,"title");
    const goal = ta(a,"goal");
    const tip = ta(a,"tip");
    return [title,goal,tip,a.title,a.goal,...a.blocks,...a.challenges.map(c=>c.t),a.v2?"v2":"",a.ia?"ia":""].join(" ").toLowerCase().includes(q);
  });
  if(part!=="all") list = list.filter(a => a.part===part);
  if(diff!=="all") list = list.filter(a => a.difficulty===Number(diff));
  if(v2) list = list.filter(a => a.v2);
  if(ia) list = list.filter(a => a.ia);
  if(status!=="all") list = list.filter(a => getStatus(a)===status);

  currentList = list;

  const doneC = Object.keys(progress.done).length;
  const favC = Object.keys(progress.fav).length;
  $("statsRow").innerHTML = `<span>${t("results")} : <strong>${list.length}</strong> ${t("of")}</span><span>${t("doneL")} : <strong>${doneC}</strong></span><span>${t("favL")} : <strong>${favC}</strong></span>`;
  $("statsText").textContent = `${doneC} / ${A.length} (${Math.round(doneC/A.length*100)}%)`;

  if(list.length === 0){
    grid.innerHTML = `<div class="empty-state" style="grid-column:1/-1">${t("noResults")}</div>`;
    return;
  }

  grid.innerHTML = list.map((a,idx) => {
    const st = getStatus(a);
    const chip = st==="done"?`<span class="chip done">${t("chipDone")}</span>`:st==="fav"?`<span class="chip fav">${t("chipFav")}</span>`:`<span class="chip todo">${t("chipTodo")}</span>`;
    const goalText = ta(a,"goal");
    const preview = goalText.length>80 ? goalText.slice(0,80)+"…" : goalText;
    return `<article class="act-card" data-id="${a.id}" data-diff="${a.difficulty}" style="--i:${idx}">
      <div class="card-top"><div class="tags">${tagHTML(a)}</div><span class="card-id">#${a.id}</span></div>
      <h3>${esc(ta(a,"title"))}</h3>
      <p class="preview">${esc(preview)}</p>
      <div class="card-bottom">${chip}<button class="primary btn-sm" data-go="${a.id}">${t("go")}</button></div>
    </article>`;
  }).join("");
}

// ═══════════════════════════════════════════════════════════════════
// MODAL
// ═══════════════════════════════════════════════════════════════════
grid.addEventListener("click", e => {
  const goBtn = e.target.closest("[data-go]");
  const card = e.target.closest(".act-card");
  if(goBtn){openById(Number(goBtn.dataset.go));e.stopPropagation();}
  else if(card){openById(Number(card.dataset.id));}
});

function openById(id){
  const idx = currentList.findIndex(a => a.id===id);
  if(idx===-1){currentList=A.slice();currentIndex=A.findIndex(a=>a.id===id);}
  else currentIndex=idx;
  openModal();
}

function openModal(){
  const a = currentList[currentIndex];
  if(!a) return;
  stopSim(); simImported = false;

  $("mTitle").textContent = `#${a.id} — ${ta(a,"title")}`;
  $("mTags").innerHTML = tagHTML(a);

  // Info tab: meta chips
  const diffLabels = {1:lang==="ar"?"مبتدئ":lang==="en"?"Beginner":"Débutant", 2:lang==="ar"?"متوسط":lang==="en"?"Intermediate":"Intermédiaire", 3:lang==="ar"?"متقدم":lang==="en"?"Advanced":"Avancé"};
  let metaH = `<span class="meta-chip diff-${a.difficulty}">${'⭐'.repeat(a.difficulty)} ${diffLabels[a.difficulty]}</span>`;
  metaH += `<span class="meta-chip time-chip">⏱ ${esc(a.time)}</span>`;
  metaH += `<span class="meta-chip">${a.part==="simple"?(lang==="ar"?"بسيط":lang==="en"?"Simple":"Simple"):(lang==="ar"?"متقدم":lang==="en"?"Advanced":"Avancé")}</span>`;
  if(a.v2) metaH += `<span class="meta-chip v2-chip">V2</span>`;
  if(a.ia) metaH += `<span class="meta-chip ia-chip">${lang==="ar"?"🧠 ذكاء اصطناعي":lang==="en"?"🧠 AI":"🧠 IA"}</span>`;
  $("infoMeta").innerHTML = metaH;

  // Section titles
  $("infoGoalTitle").textContent = lang==="ar"?"🎯 الهدف":lang==="en"?"🎯 Goal":"🎯 Objectif";
  $("mNeedsLabel").textContent = lang==="ar"?"🧰 المواد":lang==="en"?"🧰 Materials":"🧰 Matériel";

  // Goal
  $("mGoal").textContent = ta(a,"goal");

  // Section titles + lesson content (concept, steps, diagram)
  $("infoConceptTitle").textContent = lang==="ar"?"💡 المفهوم":lang==="en"?"💡 Concept":"💡 Concept";
  $("infoStepsTitle").textContent = lang==="ar"?"📋 الخطوات":lang==="en"?"📋 Steps":"📋 Étapes";
  $("infoDiagramTitle").textContent = lang==="ar"?"📐 المخطط":lang==="en"?"📐 Diagram":"📐 Schéma";
  $("infoBlocksTitle").textContent = lang==="ar"?"🧩 المكعبات المستخدمة":lang==="en"?"🧩 Blocks used":"🧩 Blocs utilisés";
  $("infoCodeTitle").textContent = lang==="ar"?"💻 التعليمات":lang==="en"?"💻 Instructions":"💻 Instructions";

  // Flow + pseudo titles
  $("infoFlowTitle").textContent = lang==="ar"?"🔀 المخطط الانسيابي":lang==="en"?"🔀 Flowchart":"🔀 Algorithme";
  $("infoPseudoTitle").textContent = lang==="ar"?"📝 الكود الزائف":lang==="en"?"📝 Pseudocode":"📝 Pseudo-code";

  // Auto-generate lesson content
  generateLesson(a);

  // Auto-generate flowchart + pseudocode
  generateFlowAndPseudo(a);

  // Auto-detect blocks & instructions from JS code
  const blockMap = [
    {re:/basic\.showString/,cat:"basic",color:"#1E90FF",label:"afficher texte",js:"basic.showString()",py:"basic.show_string()"},
    {re:/basic\.showIcon/,cat:"basic",color:"#1E90FF",label:"montrer icône",js:"basic.showIcon()",py:"basic.show_icon()"},
    {re:/basic\.showNumber/,cat:"basic",color:"#1E90FF",label:"afficher nombre",js:"basic.showNumber()",py:"basic.show_number()"},
    {re:/basic\.showLeds/,cat:"basic",color:"#1E90FF",label:"montrer LEDs",js:"basic.showLeds()",py:"basic.show_leds()"},
    {re:/basic\.clearScreen/,cat:"basic",color:"#1E90FF",label:"effacer écran",js:"basic.clearScreen()",py:"basic.clear_screen()"},
    {re:/basic\.pause/,cat:"basic",color:"#1E90FF",label:"pause",js:"basic.pause(ms)",py:"basic.pause(ms)"},
    {re:/basic\.forever/,cat:"loops",color:"#00AA00",label:"répéter indéfiniment",js:"basic.forever()",py:"basic.forever()"},
    {re:/input\.onButtonPressed/,cat:"input",color:"#D400D4",label:"quand bouton pressé",js:"input.onButtonPressed()",py:"input.on_button_pressed()"},
    {re:/input\.onGesture/,cat:"input",color:"#D400D4",label:"quand geste",js:"input.onGesture()",py:"input.on_gesture()"},
    {re:/input\.onLogoEvent/,cat:"input",color:"#D400D4",label:"quand logo touché",js:"input.onLogoEvent()",py:"input.on_logo_event()"},
    {re:/input\.temperature/,cat:"input",color:"#D400D4",label:"température",js:"input.temperature()",py:"input.temperature()"},
    {re:/input\.lightLevel/,cat:"input",color:"#D400D4",label:"niveau lumière",js:"input.lightLevel()",py:"input.light_level()"},
    {re:/input\.soundLevel/,cat:"input",color:"#D400D4",label:"niveau sonore",js:"input.soundLevel()",py:"input.sound_level()"},
    {re:/input\.compassHeading/,cat:"input",color:"#D400D4",label:"direction boussole",js:"input.compassHeading()",py:"input.compass_heading()"},
    {re:/input\.acceleration/,cat:"input",color:"#D400D4",label:"accélération",js:"input.acceleration()",py:"input.acceleration()"},
    {re:/randint/,cat:"math",color:"#9400D3",label:"au hasard",js:"randint(min, max)",py:"randint(min, max)"},
    {re:/music\.playTone/,cat:"music",color:"#E63022",label:"jouer tonalité",js:"music.playTone()",py:"music.play_tone()"},
    {re:/music\.startMelody/,cat:"music",color:"#E63022",label:"jouer mélodie",js:"music.startMelody()",py:"music.start_melody()"},
    {re:/radio\.setGroup/,cat:"radio",color:"#E3008C",label:"radio groupe",js:"radio.setGroup()",py:"radio.set_group()"},
    {re:/radio\.sendNumber/,cat:"radio",color:"#E3008C",label:"radio envoyer",js:"radio.sendNumber()",py:"radio.send_number()"},
    {re:/radio\.onReceivedNumber/,cat:"radio",color:"#E3008C",label:"radio reçu",js:"radio.onReceivedNumber()",py:"radio.on_received_number()"},
    {re:/pins\.analogReadPin/,cat:"pins",color:"#3BDDD4",label:"lire analogique",js:"pins.analogReadPin()",py:"pins.analog_read_pin()"},
    {re:/pins\.digitalReadPin/,cat:"pins",color:"#3BDDD4",label:"lire numérique",js:"pins.digitalReadPin()",py:"pins.digital_read_pin()"},
    {re:/pins\.digitalWritePin/,cat:"pins",color:"#3BDDD4",label:"écriture numérique",js:"pins.digitalWritePin()",py:"pins.digital_write_pin()"},
    {re:/pins\.analogWritePin/,cat:"pins",color:"#3BDDD4",label:"écriture analogique",js:"pins.analogWritePin()",py:"pins.analog_write_pin()"},
    {re:/pins\.servoWritePin/,cat:"pins",color:"#3BDDD4",label:"servo écrire",js:"pins.servoWritePin()",py:"pins.servo_write_pin()"},
    {re:/led\.plot/,cat:"game",color:"#7600A8",label:"allumer LED",js:"led.plot(x,y)",py:"led.plot(x,y)"},
    {re:/led\.plotBarGraph/,cat:"game",color:"#7600A8",label:"graphique barres",js:"led.plotBarGraph()",py:"led.plot_bar_graph()"},
    {re:/game\.createSprite/,cat:"game",color:"#7600A8",label:"créer sprite",js:"game.createSprite()",py:"game.create_sprite()"},
    {re:/neopixel\.create/,cat:"neopixel",color:"#7600A8",label:"NeoPixel",js:"neopixel.create()",py:"neopixel.create()"},
    {re:/bluetooth\./,cat:"bluetooth",color:"#0082FB",label:"Bluetooth",js:"bluetooth.*",py:"bluetooth.*"},
    {re:/sonar\.ping/,cat:"sonar",color:"#00A4A6",label:"sonar distance",js:"sonar.ping()",py:"sonar.ping()"},
    {re:/huskylens\./,cat:"input",color:"#D400D4",label:"HuskyLens IA",js:"huskylens.*",py:"huskylens.*"},
    {re:/function\s+\w+/,cat:"functions",color:"#3455DB",label:"fonction",js:"function name()",py:"def name():"}
  ];

  const detected = blockMap.filter(b => b.re.test(a.codeJS));

  // Render block chips
  $("mBlocksUsed").innerHTML = detected.map(b =>
    `<span class="block-chip" style="background:${b.color}">${esc(b.label)}</span>`
  ).join("") || `<span style="font-size:.72rem;color:var(--text-muted)">${lang==="ar"?"(لا مكعبات مكتشفة)":lang==="en"?"(no blocks detected)":"(aucun bloc détecté)"}</span>`;

  // Render code key rows (JS + Python)
  $("mCodeKeys").innerHTML = detected.slice(0, 8).map(b =>
    `<div class="code-key-row"><span class="ck-block" style="background:${b.color}"></span><span class="ck-label">${esc(b.label)}</span><span class="ck-js">${esc(b.js)}</span><span class="ck-sep">│</span><span class="ck-py">${esc(b.py)}</span></div>`
  ).join("") || "";

  // Tip
  $("mTip").textContent = "💡 " + ta(a,"tip");

  // QR Code — links to this activity on GitHub Pages
  const appUrl = window.location.origin + window.location.pathname;
  const qrUrl = `${appUrl}?a=${a.id}`;
  const qrImg = `https://api.qrserver.com/v1/create-qr-code/?size=160x160&data=${encodeURIComponent(qrUrl)}`;
  const qrLabel = lang==="ar"?"امسح للفتح على الهاتف":lang==="en"?"Scan to open on phone":"Scanne pour ouvrir sur téléphone";
  const qrEbook = lang==="ar"?"للكتاب الإلكتروني":lang==="en"?"For ebook":"Pour l'ebook";
  $("qrSection").innerHTML = `<img src="${qrImg}" alt="QR #${a.id}" loading="lazy"><div class="qr-text"><strong>📱 ${qrLabel}</strong><br>${qrEbook}: Activity #${a.id}</div>`;

  // Needs
  const needs = ta(a,"needs");
  $("mNeeds").innerHTML = (Array.isArray(needs)?needs:a.needs).map(n => `<li>${esc(n)}</li>`).join("");

  // Render blocks: try MakeCode iframe first, CSS fallback
  renderMakeCodeBlocks(a);

  updateCode(a);

  const challenges = taChal(a);
  $("mChallenges").innerHTML = challenges.map((c,ci) => `<div class="challenge" style="--ci:${ci}"><span class="challenge-icon">${c.d===1?'🟢':c.d===2?'🟡':'🔴'}</span><div><div class="challenge-text">${c.t}</div><div class="diff-star">${'⭐'.repeat(c.d)}</div></div></div>`).join("");

  const done = !!progress.done[a.id];
  const fav = !!progress.fav[a.id];
  $("markDoneBtn").textContent = done ? t("unmarkDone") : t("markDone");
  $("markFavBtn").textContent = fav ? t("unmarkFav") : t("markFav");
  $("prevBtn").disabled = currentIndex<=0;
  $("nextBtn").disabled = currentIndex>=currentList.length-1;
  switchTab("info");
  overlay.classList.add("open");
  $("closeBtn").focus();
}

function updateCode(a){
  $("codeBlockJS").innerHTML = highlightJS(a.codeJS);
  $("codeBlockPY").innerHTML = highlightPY(a.codePY);
}

function closeModal(){
  stopSim();
  overlay.classList.remove("open");
  const card = document.querySelector(`.act-card[data-id="${currentList[currentIndex]?.id}"]`);
  if(card) card.focus();
}
// Focus trap: keep Tab inside modal
overlay.addEventListener("keydown", function(e){
  if(e.key!=="Tab"||!overlay.classList.contains("open")) return;
  const f = overlay.querySelectorAll("button:not(:disabled),[tabindex]:not([tabindex='-1']),a[href],input,select");
  if(!f.length) return;
  const first=f[0], last=f[f.length-1];
  if(e.shiftKey){if(document.activeElement===first){e.preventDefault();last.focus();}}
  else{if(document.activeElement===last){e.preventDefault();first.focus();}}
});
function switchTab(name){
  document.querySelectorAll(".tab-btn").forEach(b => b.classList.toggle("active", b.dataset.tab===name));
  document.querySelectorAll(".tab-panel").forEach(p => p.classList.toggle("active", p.id==="tab-"+name));
}

// ═══════════════════════════════════════════════════════════════════
// TOAST
// ═══════════════════════════════════════════════════════════════════
let toastTimer;
function showToast(msg){
  $("toastMsg").textContent = msg;
  $("toast").style.display = "block";
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => $("toast").style.display = "none", 1500);
}

// ═══════════════════════════════════════════════════════════════════
// EVENTS
// ═══════════════════════════════════════════════════════════════════
// Debounced render for search, instant for dropdowns/checkboxes
let renderTimer;
function debouncedRender(){ clearTimeout(renderTimer); renderTimer = setTimeout(render, 200); }
$("searchInput").addEventListener("input", debouncedRender);
["partSelect","diffSelect","statusSelect"].forEach(id => $(id).addEventListener("change", render));
["onlyV2","onlyIA"].forEach(id => $(id).addEventListener("change", render));

$("resetBtn").addEventListener("click", () => {
  if(confirm(t("resetConfirm"))){progress=defaultP();saveP(progress);render();showToast(t("resetDone"));}
});
$("randomBtn").addEventListener("click", () => {
  if(currentList.length>0){currentIndex=Math.floor(Math.random()*currentList.length);openModal();}
});

$("closeBtn").addEventListener("click", closeModal);
overlay.addEventListener("click", e => {if(e.target===overlay) closeModal();});
document.addEventListener("keydown", e => {
  if(!overlay.classList.contains("open")) return;
  if(e.key==="Escape") closeModal();
  if(e.key==="ArrowLeft" && currentIndex>0){currentIndex--;openModal();}
  if(e.key==="ArrowRight" && currentIndex<currentList.length-1){currentIndex++;openModal();}
});

$("markDoneBtn").addEventListener("click", () => {
  const a=currentList[currentIndex];if(!a)return;
  if(progress.done[a.id])delete progress.done[a.id];else progress.done[a.id]=true;
  saveP(progress);
  // Check for new badges
  const newBadges = checkBadges();
  newBadges.forEach(b => {
    const name = b[lang]||b.fr;
    showToast(`🏆 ${b.icon} ${name} !`);
  });
  renderBadgeShelf();
  render();openModal();
});
$("markFavBtn").addEventListener("click", () => {
  const a=currentList[currentIndex];if(!a)return;
  if(progress.fav[a.id])delete progress.fav[a.id];else progress.fav[a.id]=true;
  saveP(progress);render();openModal();
});
$("prevBtn").addEventListener("click", () => {if(currentIndex>0){currentIndex--;openModal();}});
$("nextBtn").addEventListener("click", () => {if(currentIndex<currentList.length-1){currentIndex++;openModal();}});
$("tabBar").addEventListener("click", e => {const btn=e.target.closest(".tab-btn");if(btn) switchTab(btn.dataset.tab);});
$("copyJSBtn").addEventListener("click", async () => {
  try{
    await navigator.clipboard.writeText($("codeBlockJS").textContent);
    $("copyJSBtn").textContent = "✅ Copié";
    showToast(t("copied"));
    setTimeout(() => $("copyJSBtn").textContent = "📋 Copier", 2000);
  }catch{showToast("Error");}
});
$("copyPYBtn").addEventListener("click", async () => {
  try{
    await navigator.clipboard.writeText($("codeBlockPY").textContent);
    $("copyPYBtn").textContent = "✅ Copié";
    showToast(t("copied"));
    setTimeout(() => $("copyPYBtn").textContent = "📋 Copier", 2000);
  }catch{showToast("Error");}
});
// Open in MakeCode — copy code to clipboard then open MakeCode
$("openMCJS").addEventListener("click", async () => {
  try{ await navigator.clipboard.writeText($("codeBlockJS").textContent); }catch(e){/* clipboard may fail silently */}
  showToast(lang==="ar"?"تم النسخ! الصق في MakeCode ← JavaScript":lang==="en"?"Copied! Paste in MakeCode → JavaScript":"Copié ! Colle dans MakeCode → JavaScript");
  window.open("https://makecode.microbit.org/#editor","_blank");
});
$("openMCPY").addEventListener("click", async () => {
  try{ await navigator.clipboard.writeText($("codeBlockPY").textContent); }catch(e){/* clipboard may fail silently */}
  showToast(lang==="ar"?"تم النسخ! الصق في MakeCode ← Python":lang==="en"?"Copied! Paste in MakeCode → Python":"Copié ! Colle dans MakeCode → Python");
  window.open("https://makecode.microbit.org/#editor","_blank");
});
// Restore saved theme on load; persist on change.
(function(){
  const sel = $("themeSelect");
  const valid = new Set([...sel.options].map(o => o.value));
  const saved = localStorage.getItem("theme");
  const theme = (saved && valid.has(saved)) ? saved : "robot";
  document.documentElement.dataset.theme = theme;
  sel.value = theme;
})();
$("themeSelect").addEventListener("change", e => {
  document.documentElement.dataset.theme = e.target.value;
  localStorage.setItem("theme", e.target.value);
});
$("langSelect").addEventListener("change", e => {lang=e.target.value;applyLang();});

// ═══════════════════════════════════════════════════════════════════
// CODE ↔ BLOCKS SYNC
// ═══════════════════════════════════════════════════════════════════
let syncTimer = null;
let lastSyncedCode = "";

function markCodeModified(){
  const ss = $("syncStatus");
  const sb = $("syncBlocksBtn");
  const modLabel = lang==="ar"?"⚠ تم التعديل":lang==="en"?"⚠ Modified":"⚠ Modifié";
  const reLabel = lang==="ar"?"🔄 تحديث المكعبات":lang==="en"?"🔄 Re-render blocks":"🔄 Actualiser les blocs";
  ss.textContent = modLabel;
  ss.className = "sync-status modified";
  sb.textContent = reLabel;
}

function markCodeSynced(){
  const ss = $("syncStatus");
  const syncLabel = lang==="ar"?"✅ متزامن":lang==="en"?"✅ Synced":"✅ Synchronisé";
  ss.textContent = syncLabel;
  ss.className = "sync-status synced";
}

function resyncBlocks(){
  const code = $("codeBlockJS").textContent;
  lastSyncedCode = code;
  const mcId = "edit-" + Date.now();
  const mcContainer = $("mBlocksMC");
  mcContainer.dataset.mcId = mcId;
  mcContainer.innerHTML = '<div class="mc-loading">' + (lang==="ar"?"جاري التحديث…":lang==="en"?"Updating blocks…":"Actualisation des blocs…") + '</div>';
  if(mcRenderReady){
    sendMCRender(mcId, code);
  } else {
    mcRenderQueue.push({id: mcId, code: code});
  }
  markCodeSynced();
}

// Listen for JS code edits
$("codeBlockJS").addEventListener("input", () => {
  const code = $("codeBlockJS").textContent;
  if(code !== lastSyncedCode){
    markCodeModified();
    // Auto-sync after 2s debounce
    clearTimeout(syncTimer);
    syncTimer = setTimeout(resyncBlocks, 2000);
  }
});

// Manual sync button
// LED grid click-to-toggle
document.addEventListener("click", e => {
  if(e.target.classList.contains("led-cell")) e.target.classList.toggle("on");
});

$("syncBlocksBtn").addEventListener("click", () => {
  clearTimeout(syncTimer);
  resyncBlocks();
});

// Edit blocks in MakeCode — copies JS code + opens editor
$("openMCBlocks").addEventListener("click", async () => {
  try{ await navigator.clipboard.writeText($("codeBlockJS").textContent); }catch(e){/* clipboard may fail silently */}
  showToast(lang==="ar"?"تم النسخ! الصق في MakeCode ← JavaScript ← ثم عدّل المكعبات":lang==="en"?"Copied! Paste in MakeCode → JavaScript → then edit blocks":"Copié ! Colle dans MakeCode → JavaScript → puis modifie les blocs");
  window.open("https://makecode.microbit.org/#editor","_blank");
});

// ═══════════════════════════════════════════════════════════════════
// SIDEBAR
// ═══════════════════════════════════════════════════════════════════
$("sidebar").addEventListener("click", e => {
  const item = e.target.closest(".sidebar-item");
  if(!item) return;
  currentTopic = item.dataset.topic;
  $("sidebar").querySelectorAll(".sidebar-item").forEach(el => el.classList.remove("active"));
  item.classList.add("active");
  render();
  // Close drawer on mobile
  $("sidebar").classList.remove("open");
  $("sidebarOverlay").classList.remove("open");
});

function updateSidebarCounts(){
  const countFor = key => {
    if(key==="all") return A.length;
    return TOPICS[key] ? TOPICS[key].ids.length : 0;
  };
  $("sbAllC").textContent = countFor("all");
  Object.keys(TOPICS).forEach(k => {
    const el = $("sb" + k.charAt(0).toUpperCase() + k.slice(1) + "C");
    if(el) el.textContent = countFor(k);
  });
}

// Mobile sidebar toggle
$("sidebarToggle").addEventListener("click", () => {
  $("sidebar").classList.toggle("open");
  $("sidebarOverlay").classList.toggle("open");
});
$("sidebarOverlay").addEventListener("click", () => {
  $("sidebar").classList.remove("open");
  $("sidebarOverlay").classList.remove("open");
});

// ═══════════════════════════════════════════════════════════════════
// INIT
// ═══════════════════════════════════════════════════════════════════
$("logoWrap").innerHTML = LOGO_SVG;
updateSidebarCounts();
renderBadgeShelf();
applyLang();

// ═══════════════════════════════════════════════════════════════════
// MAKECODE SIMULATOR (controller=1 API)
// ═══════════════════════════════════════════════════════════════════
let simReady = false;
let simPending = null;
let simImported = false;
const SIM_URL = "https://makecode.microbit.org?controller=1";

window.addEventListener("message", function(ev){
  const msg = ev.data;
  if(!msg) return;
  // MakeCode sends various message formats
  if(typeof msg === "string"){
    try{ const parsed = JSON.parse(msg); if(parsed.type === "pxteditor") handleSimMsg(parsed); }catch(e){/* not JSON */}
    return;
  }
  if(typeof msg === "object") handleSimMsg(msg);
});

function handleSimMsg(msg){
  const frame = $("simFrame");
  if(!frame || !frame.contentWindow) return;

  // Log all MakeCode messages for debugging
  if(msg.type === "pxteditor" || msg.type === "pxthost"){
    console.log("[SIM]", msg.type, msg.action, msg.id ? "id:"+msg.id : "");
  }

  // MakeCode asks for workspace — respond with empty project list
  if(msg.type === "pxthost" && msg.action === "workspacesync"){
    console.log("[SIM] Responding to workspacesync");
    frame.contentWindow.postMessage({
      type: "pxthost",
      id: msg.id,
      success: true,
      controllerId: "bit54activities",
      editor: {},
      projects: []
    }, "*");
    return;
  }

  // MakeCode wants to save workspace — acknowledge
  if(msg.type === "pxthost" && msg.action === "workspacesave"){
    console.log("[SIM] Acknowledging workspacesave");
    if(msg.response){
      frame.contentWindow.postMessage({
        type: "pxthost",
        id: msg.id,
        success: true
      }, "*");
    }
    return;
  }

  // MakeCode signals editor fully loaded — NOW we can import
  if(msg.type === "pxthost" && msg.action === "editorcontentloaded"){
    console.log("[SIM] Editor content loaded — ready to import");
    simReady = true;
    if(simPending){ setTimeout(()=>loadSimCode(simPending), 500); simPending = null; }
    return;
  }

  // pxteditor editorcontentloaded = editor fully ready, import once
  if(msg.type === "pxteditor" && msg.action === "editorcontentloaded"){
    simReady = true;
    if(!simImported){
      simImported = true;
      console.log("[SIM] Editor ready — importing code (once)");
      const a = currentList[currentIndex];
      if(a) setTimeout(()=>loadSimCode(a.codeJS), 500);
    }
    simPending = null;
  }
}

function loadSimCode(code){
  const frame = $("simFrame");
  if(!frame || !frame.contentWindow) return;
  if(!code){ console.log("[SIM] No code to import"); return; }
  console.log("[SIM] Importing code:", code.substring(0, 60) + "...");
  const project = {
    header: {
      name: "activity",
      meta: {},
      editor: "tsprj",
      pubId: "",
      pubCurrent: false,
      target: "microbit",
      id: "sim-" + Date.now(),
      recentUse: Date.now(),
      modificationTime: Date.now(),
      blobId: "",
      blobVersion: "",
      blobCurrent: false,
      isDeleted: false,
      saveId: null,
      cloudUserId: null,
      cloudCurrent: false,
      cloudVersion: null,
      cloudLastSyncTime: 0
    },
    text: {
      "main.ts": code,
      "main.blocks": "<xml xmlns=\"https://developers.google.com/blockly/xml\"></xml>",
      "pxt.json": JSON.stringify({
        name: "activity",
        description: "",
        dependencies: {"core":"*","radio":"*","microphone":"*","neopixel":"*","maqueen":"github:DFRobot/pxt-maqueen"},
        files: ["main.blocks","main.ts"]
      })
    }
  };
  frame.contentWindow.postMessage({
    type: "pxteditor",
    action: "importproject",
    project: project,
    response: false
  }, "*");
  setTimeout(() => {
    console.log("[SIM] Starting simulator...");
    frame.contentWindow.postMessage({type:"pxteditor",action:"startsimulator"}, "*");
  }, 3000);
}

function startSim(){
  const a = currentList[currentIndex];
  if(!a) return;
  const frame = $("simFrame");
  const hint = $("simHint");
  frame.classList.remove("hidden");
  hint.style.display = "none";
  simImported = false;
  if(!frame.src || frame.src === "about:blank"){
    simReady = false;
    simPending = a.codeJS;
    frame.src = SIM_URL;
  }
  // Always import twice: the first importproject is often dropped because the
  // MakeCode editor isn't yet listening for postMessage. A second import a few
  // seconds later reliably lands. Cheap and deterministic.
  const code = a.codeJS;
  setTimeout(() => loadSimCode(code), 3500);
  setTimeout(() => loadSimCode(code), 7000);
}

function stopSim(){
  const frame = $("simFrame");
  if(frame && frame.contentWindow){
    frame.contentWindow.postMessage({type:"pxteditor",action:"stopsimulator"}, "*");
  }
}

$("simRunBtn").addEventListener("click", startSim);
$("simStopBtn").addEventListener("click", stopSim);

function updateSimLabels(){
  $("simRunBtn").textContent = lang==="ar"?"▶ تشغيل":lang==="en"?"▶ Run":"▶ Lancer";
  $("simStopBtn").textContent = lang==="ar"?"⏹ إيقاف":lang==="en"?"⏹ Stop":"⏹ Arrêter";
  $("simHint").textContent = lang==="ar"?"اضغط ▶ لتشغيل محاكي المايكروبت":lang==="en"?"Click ▶ to run the micro:bit simulator":"Clique sur ▶ pour lancer le simulateur micro:bit";
  $("tabSim").textContent = "▶ "+(lang==="ar"?"المحاكي":lang==="en"?"Simulator":"Simulateur");
}

// ═══════════════════════════════════════════════════════════════════
// LEARNING ROADMAP
// ═══════════════════════════════════════════════════════════════════
const ROADMAP_ORDER = __ROADMAP_ORDER__;
const ROADMAP_ICONS = __ROADMAP_ICONS__;

function renderRoadmap(){
  $("roadmapTitle").textContent = lang==="ar"?"🗺 مسار التعلّم":lang==="en"?"🗺 Learning Path":"🗺 Parcours d'apprentissage";
  $("sbRoadmap").textContent = lang==="ar"?"المسار":lang==="en"?"Roadmap":"Parcours";
  let h = "";
  ROADMAP_ORDER.forEach((key, i) => {
    const t = TOPICS[key];
    if(!t) return;
    const total = t.ids.length;
    const done = t.ids.filter(id => progress.done[id]).length;
    const pct = Math.round(done/total*100);
    const completed = done >= total;
    const name = $("sb"+key.charAt(0).toUpperCase()+key.slice(1))?.textContent || key;
    h += `<div class="roadmap-node ${completed?'completed':''}" data-topic="${key}">`;
    h += `<div class="rn-icon">${ROADMAP_ICONS[key]}</div>`;
    h += `<div class="rn-info"><div class="rn-name">${name}</div>`;
    h += `<div class="rn-progress">${done} / ${total} ${completed?"✅":""}</div>`;
    h += `<div class="rn-bar"><div class="rn-bar-fill" style="width:${pct}%"></div></div>`;
    h += `</div></div>`;
    if(i < ROADMAP_ORDER.length - 1) h += `<div class="roadmap-connector"></div>`;
  });
  $("roadmapBody").innerHTML = h;
}

$("roadmapBtn").addEventListener("click", () => {
  renderRoadmap();
  $("roadmapOverlay").classList.add("open");
});
$("closeRoadmap").addEventListener("click", () => {
  $("roadmapOverlay").classList.remove("open");
});
$("roadmapBody").addEventListener("click", e => {
  const node = e.target.closest(".roadmap-node");
  if(!node) return;
  currentTopic = node.dataset.topic;
  document.querySelectorAll(".sidebar-item").forEach(el => el.classList.toggle("active", el.dataset.topic===currentTopic));
  render();
  $("roadmapOverlay").classList.remove("open");
});

// Auto-open activity from URL param ?a=ID (for QR codes)
const urlParams = new URLSearchParams(window.location.search);
const autoOpen = urlParams.get("a");
if(autoOpen){ const id=Number(autoOpen); if(id>=1&&id<=48) setTimeout(()=>openById(id),300); }

// ── PWA Service Worker Registration ──
if('serviceWorker' in navigator){
  const swCode = `
    const CACHE='microbit-v2';
    self.addEventListener('install',e=>e.waitUntil(caches.open(CACHE).then(c=>c.addAll(['./','/index.html'])).then(()=>self.skipWaiting())));
    self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim())));
    self.addEventListener('fetch',e=>{if(e.request.method!=='GET')return;e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request).then(res=>{const c=res.clone();caches.open(CACHE).then(cache=>cache.put(e.request,c));return res})))});
  `;
  const blob = new Blob([swCode],{type:'application/javascript'});
  navigator.serviceWorker.register(URL.createObjectURL(blob)).catch(()=>{});
}
'''
