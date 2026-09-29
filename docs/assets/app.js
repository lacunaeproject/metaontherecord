(() => {
"use strict";
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const yearOf = d => +d.slice(0, 4);
const fmtDate = d => `${MONTHS[+d.slice(5, 7) - 1]} ${d.slice(0, 4)}`;

/* ---------- evidence glyphs: solidity encodes certainty ---------- */
function glyph(tier, cls = "glyph") {
  const a = `class="${cls}" viewBox="0 0 16 16" aria-hidden="true" focusable="false"`;
  switch (tier) {
    case "ruled":     return `<svg ${a}><rect x="1.5" y="1.5" width="13" height="13" fill="currentColor"/></svg>`;
    case "appeal":    return `<svg ${a}><path d="M1.5 1.5h8.5l4.5 4.5v8.5h-13z" fill="currentColor"/></svg>`;
    case "settled":   return `<svg ${a}><rect x="2.5" y="2.5" width="11" height="11" fill="none" stroke="currentColor" stroke-width="2"/><rect x="5.5" y="5.5" width="5" height="5" fill="currentColor"/></svg>`;
    case "admitted":  return `<svg ${a}><rect x="2.5" y="2.5" width="11" height="11" fill="none" stroke="currentColor" stroke-width="2"/><rect x="2.5" y="2.5" width="5.5" height="11" fill="currentColor"/></svg>`;
    case "reported":  return `<svg ${a}><rect x="2.5" y="2.5" width="11" height="11" fill="none" stroke="currentColor" stroke-width="2"/></svg>`;
    case "alleged":   return `<svg ${a}><rect x="2.5" y="2.5" width="11" height="11" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="2.4 2"/></svg>`;
    case "dismissed": return `<svg ${a}><rect x="2.5" y="2.5" width="11" height="11" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M3 13 13 3" stroke="currentColor" stroke-width="1.6"/></svg>`;
    case "credit":    return `<svg ${a}><circle cx="8" cy="8" r="6" fill="currentColor"/></svg>`;
  }
  return "";
}
const tierLabel = t => t === "credit" ? "Credit" : TIERS[t].label;

/* ---------- static fills ---------- */
$$(".tierline[data-tier]").forEach(el => { el.innerHTML = glyph(el.dataset.tier) + esc(tierLabel(el.dataset.tier)); });

const years = ENTRIES.map(e => yearOf(e.date));
const firstYear = Math.min(...years), lastYear = Math.max(...years);

const tierCount = k => ENTRIES.filter(e => e.tier === k).length;
$("#tierdefs").innerHTML = Object.entries(TIERS).map(([k, t]) =>
  `<div><dt>${glyph(k)}${esc(t.label)}</dt><dd>${esc(t.def)}</dd><a class="tier-go" href="#record" data-go-tier="${k}">${tierCount(k)} ${tierCount(k) === 1 ? "entry" : "entries"}</a></div>`).join("") +
  `<div><dt>${glyph("credit")}Credit</dt><dd>Something Meta did well, listed with the context it needs.</dd><a class="tier-go" href="#credits">${CREDITS.length} credits</a></div>`;

$("#notes").innerHTML = NOTES.map(([q, a]) => `<details><summary>${esc(q)}</summary><p>${esc(a)}</p></details>`).join("");

function sourcesHTML(list, check) {
  if (list && list.length) return `<ul class="src">${list.map(([l, u]) => `<li><a href="${esc(u)}" target="_blank" rel="noopener">${esc(l)}</a></li>`).join("")}</ul>`;
  return check ? `<p class="pending">Primary source link being added. Figures are drawn from public reporting and will be linked before this entry is final.</p>` : "";
}

$("#creditlist").innerHTML = CREDITS.map(c => `
  <li class="credit-row" id="${esc(c.id)}">
    <span class="when">${fmtDate(c.date)}</span>
    <div>${c.fig ? `<span class="big">${esc(c.fig)}</span>` : ""}<h3>${esc(c.title)}</h3><p>${esc(c.summary)}</p></div>
    <div><p class="ctx"><b>Context</b>${esc(c.ctx)}</p>${sourcesHTML(c.sources)}</div>
  </li>`).join("");

/* ---------- state ---------- */
const state = { themes: new Set(), tiers: new Set(), q: "", credits: false, newest: false };
const isFiltered = () => state.themes.size || state.tiers.size || state.q;

function matches(e) {
  if (e.kind === "credit") {
    if (!state.credits || state.themes.size || state.tiers.size) return false;
  } else {
    if (state.themes.size && !e.themes.some(t => state.themes.has(t))) return false;
    if (state.tiers.size && !state.tiers.has(e.tier)) return false;
  }
  if (state.q) {
    const hay = [e.title, e.summary, e.response, e.who, e.cap, e.status, e.ctx, ...(e.themes || []).map(t => THEMES[t])].join(" ").toLowerCase();
    if (!state.q.split(/\s+/).every(w => hay.includes(w))) return false;
  }
  return true;
}

/* ---------- filter dropdowns ---------- */
const topicChips = $("#topicchips"), tierChips = $("#tierchips");
const opt = (attrs, label, pressed) => `<button class="dd-opt" ${attrs} aria-pressed="${pressed}"><span class="dd-check" aria-hidden="true"></span>${label}</button>`;
topicChips.innerHTML = opt(`data-all="topic"`, "All topics", true) +
  Object.entries(THEMES).map(([k, v]) => opt(`data-theme="${k}"`, esc(v), false)).join("");
tierChips.innerHTML = opt(`data-all="tier"`, "All evidence", true) +
  Object.keys(TIERS).map(k => opt(`data-tier="${k}"`, `${glyph(k)}${esc(TIERS[k].label)}`, false)).join("");

const ddValue = (set, name) => set.size === 0 ? "All" : set.size === 1 ? name([...set][0]) : `${set.size} selected`;
function syncChips() {
  $$("[data-theme]", topicChips).forEach(b => b.setAttribute("aria-pressed", state.themes.has(b.dataset.theme)));
  $("[data-all=topic]", topicChips).setAttribute("aria-pressed", state.themes.size === 0);
  $$("[data-tier]", tierChips).forEach(b => b.setAttribute("aria-pressed", state.tiers.has(b.dataset.tier)));
  $("[data-all=tier]", tierChips).setAttribute("aria-pressed", state.tiers.size === 0);
  $("#topic-val").textContent = ddValue(state.themes, t => THEMES[t]);
  $("#tier-val").textContent = ddValue(state.tiers, t => TIERS[t].label);
  $("#topic-dd").classList.toggle("on", state.themes.size > 0);
  $("#tier-dd").classList.toggle("on", state.tiers.size > 0);
  $("#clear").hidden = !isFiltered();
}

function setDropdown(dd, open) {
  $(".dd-btn", dd).setAttribute("aria-expanded", open);
  $(".dd-menu", dd).hidden = !open;
}
const closeDropdowns = except => $$(".dd").forEach(dd => dd !== except && setDropdown(dd, false));
$$(".dd").forEach(dd => {
  const btn = $(".dd-btn", dd), opts = () => $$(".dd-opt", dd);
  btn.addEventListener("click", () => { const open = btn.getAttribute("aria-expanded") !== "true"; closeDropdowns(dd); setDropdown(dd, open); });
  btn.addEventListener("keydown", e => {
    if (e.key !== "ArrowDown") return;
    e.preventDefault(); closeDropdowns(dd); setDropdown(dd, true); opts()[0].focus();
  });
  $(".dd-menu", dd).addEventListener("keydown", e => {
    const list = opts(), i = list.indexOf(document.activeElement);
    if (e.key === "ArrowDown" || e.key === "ArrowUp") { e.preventDefault(); list[(i + (e.key === "ArrowDown" ? 1 : -1) + list.length) % list.length].focus(); }
    else if (e.key === "Home" || e.key === "End") { e.preventDefault(); list[e.key === "Home" ? 0 : list.length - 1].focus(); }
    else if (e.key === "Tab") setDropdown(dd, false);
  });
});
document.addEventListener("click", e => { if (!e.target.closest(".dd")) closeDropdowns(); });
document.addEventListener("keydown", e => {
  if (e.key !== "Escape") return;
  const dd = $$(".dd").find(d => $(".dd-btn", d).getAttribute("aria-expanded") === "true");
  if (dd) { setDropdown(dd, false); $(".dd-btn", dd).focus(); }
});
topicChips.addEventListener("click", e => {
  const b = e.target.closest("button"); if (!b) return;
  if (b.dataset.all) state.themes.clear();
  else state.themes.has(b.dataset.theme) ? state.themes.delete(b.dataset.theme) : state.themes.add(b.dataset.theme);
  update();
});
tierChips.addEventListener("click", e => {
  const b = e.target.closest("button"); if (!b) return;
  if (b.dataset.all) state.tiers.clear();
  else state.tiers.has(b.dataset.tier) ? state.tiers.delete(b.dataset.tier) : state.tiers.add(b.dataset.tier);
  update();
});
let qTimer;
$("#q").addEventListener("input", e => { clearTimeout(qTimer); qTimer = setTimeout(() => { state.q = e.target.value.trim().toLowerCase(); update(); }, 140); });
$("#showcredits").addEventListener("change", e => { state.credits = e.target.checked; update(); });
$("#clear").addEventListener("click", () => { clearFilters(); update(); $("#q").focus(); });
const sortBtn = $("#sort");
sortBtn.addEventListener("click", () => { state.newest = !state.newest; sortBtn.lastChild.textContent = state.newest ? "Newest first" : "Oldest first"; update(); });
$("#random").addEventListener("click", e => {
  const pick = ENTRIES[Math.floor(Math.random() * ENTRIES.length)];
  const btn = e.currentTarget; btn.classList.remove("spin"); void btn.offsetWidth; btn.classList.add("spin");
  if (location.hash === "#e-" + pick.id) openFromHash(); else location.hash = "e-" + pick.id;
});
document.addEventListener("keydown", e => {
  if (e.key !== "/" || e.metaKey || e.ctrlKey || e.altKey || e.target.closest("input, textarea, select, [contenteditable]")) return;
  e.preventDefault();
  $("#filters").scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "start" });
  $("#q").focus({ preventScroll: true });
});
function clearFilters() { state.themes.clear(); state.tiers.clear(); state.q = ""; $("#q").value = ""; }

/* ---------- ledger ---------- */
const ledger = $("#ledger");
function entryHTML(e) {
  const credit = e.kind === "credit";
  const t = credit ? "credit" : e.tier;
  const themes = (e.themes || []).map(k => `<span class="tag">${esc(THEMES[k])}</span>`).join("");
  const resp = e.response ? `<blockquote class="response"><b>${credit ? "Context" : (e.who ? "In their words" : "Meta’s response")}</b>${esc(e.response)}${e.who ? ` <span>(${esc(e.who)})</span>` : ""}</blockquote>` : "";
  const ctx = credit ? `<blockquote class="response"><b>Context</b>${esc(e.ctx)}</blockquote>` : "";
  return `<li class="entry${credit ? " credit" : ""}" id="e-${esc(e.id)}">
    <button class="entry-head" aria-expanded="false" aria-controls="d-${esc(e.id)}">
      <span class="entry-date">${fmtDate(e.date)}</span>
      <span class="entry-title">${esc(e.title)}</span>
      <span class="entry-fig">${esc(e.fig || "")}</span>
      <span class="entry-tier">${glyph(t)}${esc(tierLabel(t))}</span>
      <span class="plus" aria-hidden="true"></span>
    </button>
    <div class="entry-body" id="d-${esc(e.id)}" role="region" aria-label="${esc(e.title)}">
      <div class="entry-inner"><div class="entry-content">
        <div class="main">
          ${e.status ? `<p class="status">${esc(e.status)}</p>` : ""}
          <p>${esc(e.summary)}</p>
          ${resp}${ctx}
          ${sourcesHTML(e.sources, e.check)}
          <div class="entry-meta">${themes}${e.url ? `<a class="linkbtn" href="${esc(e.url)}">Open the full entry</a>` : ""}<button class="linkbtn" data-copy="${esc(e.url || "#e-" + e.id)}">Copy link</button></div>
        </div>
        <div class="side">${e.fig ? `<div class="fact"><span class="fact-num">${esc(e.fig)}</span><span class="fact-cap">${esc(e.cap || "")}</span></div>` : ""}</div>
      </div></div>
    </div>
  </li>`;
}

function renderLedger() {
  const all = ENTRIES.concat(CREDITS.map(c => ({ ...c, kind: "credit", themes: [] })));
  const shown = all.filter(matches).sort((a, b) => state.newest ? b.date.localeCompare(a.date) : a.date.localeCompare(b.date));
  const harmShown = shown.filter(e => e.kind !== "credit").length;
  $("#count").textContent = `Showing ${harmShown} of ${ENTRIES.length} entries` + (state.credits ? ` and ${shown.length - harmShown} credits` : "");
  if (!shown.length) {
    ledger.innerHTML = `<p class="empty">No entries match these filters. <button class="linkbtn" id="empty-clear">Clear filters</button> to see the full record.</p>`;
    $("#empty-clear").onclick = () => { clearFilters(); update(); };
    return;
  }
  const groups = new Map();
  shown.forEach(e => { const y = yearOf(e.date); if (!groups.has(y)) groups.set(y, []); groups.get(y).push(e); });
  ledger.innerHTML = Array.from(groups, ([y, list]) =>
    `<section class="year" id="y${y}" aria-label="${y}"><h3 class="year-num">${y}</h3><ol class="entries">${list.map(entryHTML).join("")}</ol></section>`).join("");
}

ledger.addEventListener("click", e => {
  const copy = e.target.closest("[data-copy]");
  if (copy) {
    const target = copy.dataset.copy;
    const url = new URL(target, location.href).href;
    const done = ok => { copy.textContent = ok ? "Link copied" : "Copy failed: " + url; setTimeout(() => copy.textContent = "Copy link", 2600); };
    if (target.startsWith("#")) { try { history.replaceState(null, "", target); } catch (_) {} }
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(url).then(() => done(true), () => done(false));
    else done(false);
    return;
  }
  const head = e.target.closest(".entry-head");
  if (head) toggleEntry(head.closest(".entry"));
});
function toggleEntry(li, force) {
  const open = force ?? !li.classList.contains("open");
  li.classList.toggle("open", open);
  $(".entry-head", li).setAttribute("aria-expanded", open);
}

/* ---------- density strip ---------- */
const dbars = $("#dbars"), daxis = $("#daxis");
const span = []; for (let y = firstYear; y <= lastYear; y++) span.push(y);
document.documentElement.style.setProperty("--years", span.length);
const totals = Object.fromEntries(span.map(y => [y, ENTRIES.filter(e => yearOf(e.date) === y).length]));
const maxTotal = Math.max(...Object.values(totals));
const labelYears = new Set([firstYear, 2010, 2014, 2018, 2022, lastYear]);
dbars.innerHTML = span.map((y, i) => `<button class="dbar${i < 3 ? " tip-l" : i > span.length - 4 ? " tip-r" : ""}" style="--i:${i}" data-year="${y}" data-tip="${y} · ${totals[y]} ${totals[y] === 1 ? "entry" : "entries"}" ${totals[y] ? "" : "disabled"} aria-label="${y}: ${totals[y]} ${totals[y] === 1 ? "entry" : "entries"}"><span class="tot" style="height:${totals[y] ? Math.max(6, totals[y] / maxTotal * 100) : 2}%"><span class="hit"></span></span></button>`).join("");
daxis.innerHTML = span.map(y => `<span class="${labelYears.has(y) ? "show" : ""}">${labelYears.has(y) ? y : ""}</span>`).join("");
const recent = ENTRIES.filter(e => yearOf(e.date) >= 2021).length;
function renderDensity() {
  span.forEach(y => {
    const hits = ENTRIES.filter(e => yearOf(e.date) === y && matches(e)).length;
    const bar = $(`.dbar[data-year="${y}"] .hit`, dbars);
    bar.style.height = totals[y] ? `${hits / totals[y] * 100}%` : "0";
  });
  $("#dnote").textContent = isFiltered()
    ? "Entries per year. Blue shows entries matching your filters."
    : `Entries per year. ${recent} of the ${ENTRIES.length} entries date from 2021 or later.`;
}
dbars.addEventListener("click", e => {
  const b = e.target.closest(".dbar"); if (!b || b.disabled) return;
  const y = b.dataset.year;
  if (!$(`#y${y}`)) { clearFilters(); update(); }
  const target = $(`#y${y}`); if (target) target.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "start" });
});

/* ---------- sticky offsets ---------- */
function measureFilters() {
  const parts = [...state.themes].map(t => THEMES[t]).concat([...state.tiers].map(t => TIERS[t].label));
  if (state.q) parts.push(`“${state.q}”`);
  const shown = ENTRIES.filter(matches).length;
  $("#fbarsum").innerHTML = `<b>${shown} of ${ENTRIES.length} entries</b>${parts.length ? ": " + esc(parts.join(", ")) : ", all topics and evidence"}`;
}

function update() { syncChips(); renderLedger(); renderDensity(); measureFilters(); }
update();

/* deep links */
function openFromHash() {
  const id = decodeURIComponent(location.hash.slice(1));
  if (!id.startsWith("e-")) return;
  let li = document.getElementById(id);
  if (!li) { clearFilters(); if (id.startsWith("e-c-")) { state.credits = true; $("#showcredits").checked = true; } update(); li = document.getElementById(id); }
  if (li) {
    toggleEntry(li, true);
    setTimeout(() => { li.scrollIntoView({ block: "start" }); li.classList.remove("flash"); void li.offsetWidth; li.classList.add("flash"); }, 60);
  }
}
openFromHash();
window.addEventListener("hashchange", openFromHash);
window.addEventListener("resize", () => { clearTimeout(window.__rz); window.__rz = setTimeout(measureFilters, 150); });

/* ---------- navigation ---------- */
const topnav = $("#topnav");
new IntersectionObserver(([en]) => topnav.classList.toggle("show", !en.isIntersecting), { rootMargin: "-40px 0px 0px 0px" }).observe($("#top"));
const navLinks = $$(".navlinks a");
const secObs = new IntersectionObserver(ens => {
  ens.forEach(en => {
    if (!en.isIntersecting) return;
    navLinks.forEach(a => a.setAttribute("aria-current", a.getAttribute("href") === "#" + en.target.id ? "true" : "false"));
  });
}, { rootMargin: "-45% 0px -50% 0px" });
["pattern","record","people","money","credits","method"].forEach(id => secObs.observe(document.getElementById(id)));

/* ---------- compact filter bar ---------- */
const fbar = $("#fbar"), fbarBtn = $("#fbarbtn");
let filtersAbove = false, inRecord = false;
function syncFbar() {
  const show = filtersAbove && inRecord;
  fbar.classList.toggle("show", show);
  fbar.setAttribute("aria-hidden", !show);
  fbarBtn.tabIndex = show ? 0 : -1;
}
new IntersectionObserver(([en]) => { filtersAbove = !en.isIntersecting && en.boundingClientRect.top < 0; syncFbar(); },
  { rootMargin: "-56px 0px 0px 0px" }).observe($("#filters"));
new IntersectionObserver(([en]) => { inRecord = en.isIntersecting; syncFbar(); },
  { rootMargin: "-120px 0px -40% 0px" }).observe($("#ledger"));
fbarBtn.addEventListener("click", () => {
  $("#filters").scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "start" });
  setTimeout(() => $("#q").focus({ preventScroll: true }), reduceMotion ? 0 : 450);
});

/* ---------- money grid ---------- */
const cells = $("#cells");
const REVENUE = 201, PENALTIES = 25;
cells.innerHTML = Array.from({ length: REVENUE }, (_, i) =>
  `<span class="cell${i < PENALTIES ? " fill" : ""}"${i < PENALTIES && !reduceMotion ? ` style="transition-delay:${i * 45}ms"` : ""}></span>`).join("");
if (reduceMotion) cells.classList.add("on");
else new IntersectionObserver(([en], o) => { if (en.isIntersecting) { cells.classList.add("on"); o.disconnect(); } }, { threshold: .45 }).observe(cells);

/* each tally line lights up its share of the squares (euros counted one to one, as in the total) */
const SHARES = [12.1, 5, 4.0, 1.4, 1, 0.725, 0.65, 0.6];
const rows = $$(".tally li:not(.sum)"), cellEls = $$(".cell.fill", cells), hint = $("#cellshint");
const defaultHint = matchMedia("(hover: hover)").matches ? "Point to a line in the tally to see its share." : "Tap a line in the tally to see its share.";
hint.textContent = defaultHint;
let cum = 0;
const ranges = SHARES.map(v => { const a = Math.round(cum); cum += v; return [a, Math.min(PENALTIES, Math.round(cum))]; });
function lightRow(i) {
  rows.forEach((r, j) => r.classList.toggle("hl", j === i));
  cells.classList.toggle("focus", i >= 0);
  cellEls.forEach((c, j) => c.classList.toggle("hl", i >= 0 && j >= ranges[i][0] && j < ranges[i][1]));
  if (i < 0) { hint.textContent = defaultHint; return; }
  const [label] = rows[i].querySelector("span").childNodes;
  const n = ranges[i][1] - ranges[i][0];
  hint.innerHTML = `<b>${esc(rows[i].querySelector("b").textContent)}</b> · ${esc(label.textContent.trim())}: ${n ? `about ${n} ${n === 1 ? "square" : "squares"}` : "less than one square"}`;
}
rows.forEach((r, i) => {
  r.tabIndex = 0;
  r.addEventListener("mouseenter", () => lightRow(i));
  r.addEventListener("focus", () => lightRow(i));
  r.addEventListener("mouseleave", () => lightRow(-1));
  r.addEventListener("blur", () => lightRow(-1));
});
cellEls.forEach((c, j) => {
  const i = ranges.findIndex(([a, b]) => j >= a && j < b);
  c.addEventListener("mouseenter", () => lightRow(i));
  c.addEventListener("mouseleave", () => lightRow(-1));
});

/* ---------- tier definitions filter the record ---------- */
$("#tierdefs").addEventListener("click", e => {
  const a = e.target.closest("[data-go-tier]"); if (!a) return;
  e.preventDefault();
  clearFilters(); state.tiers.add(a.dataset.goTier); update();
  $("#filters").scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "start" });
});

/* ---------- scroll: progress bar and the pattern timeline ---------- */
const progress = $("#progress"), steps = $$(".step");
document.documentElement.classList.add("tl");
function onScroll() {
  const max = document.documentElement.scrollHeight - innerHeight;
  progress.style.setProperty("--p", max > 0 ? scrollY / max : 0);
  const line = innerHeight * .6;
  const nodes = steps.map(st => { const r = st.getBoundingClientRect(); return r.top + parseFloat(getComputedStyle(st).paddingTop) + 12; });
  steps.forEach((st, i) => {
    st.classList.toggle("lit", nodes[i] < line);
    if (i < steps.length - 1) st.style.setProperty("--seg", `${Math.max(0, Math.min(1, (line - nodes[i]) / (nodes[i + 1] - nodes[i]))) * 100}%`);
  });
}
let scrollQueued = false;
addEventListener("scroll", () => { if (!scrollQueued) { scrollQueued = true; requestAnimationFrame(() => { scrollQueued = false; onScroll(); }); } }, { passive: true });
addEventListener("resize", onScroll);
onScroll();

/* ---------- reveals ---------- */
if (!reduceMotion && "IntersectionObserver" in window) {
  document.documentElement.classList.add("reveal");
  $$("main .h-section").forEach(h => {
    let wi = 0;
    h.innerHTML = h.textContent.trim().split(/\s+/).map(w => `<span class="w"><span style="--wi:${wi++}">${esc(w)}</span></span>`).join(" ");
  });
  const groups = [".h-section", "main .intro", ".coda", ".story-photo", ".story", ".tally", ".money-grid figure", ".credit-row", ".stance", ".tiers > div", ".method-cols > div", ".density"];
  const rvObs = new IntersectionObserver(ens => ens.forEach(en => { if (en.isIntersecting) { en.target.classList.add("in"); rvObs.unobserve(en.target); } }), { rootMargin: "0px 0px -8% 0px" });
  groups.forEach(sel => $$(sel).forEach((el, i) => {
    el.classList.add("rv");
    if (/credit-row|tiers/.test(sel)) el.style.setProperty("--d", `${(i % 4) * 90}ms`);
    rvObs.observe(el);
  }));
}

/* ---------- hero: the one kinetic moment ---------- */
const root = document.documentElement;
let heroStarted = false;
const release = () => root.classList.remove("motion");
setTimeout(() => { if (!heroStarted) release(); }, 3000);

async function hero() {
  if (!root.classList.contains("motion") || !window.gsap) { release(); return; }
  try { await document.fonts.ready; } catch (_) {}
  heroStarted = true;
  const g = window.gsap;
  if (window.ScrollTrigger) g.registerPlugin(ScrollTrigger);
  const top = $(".shard-top"), bot = $(".shard-bot"), quake = $("#quake"), foot = $("#herofoot");
  g.set([".m1 > span", ".m2 > span"], { yPercent: 145 });
  g.set(foot, { autoAlpha: 0 });
  g.set(bot, { x: 0, y: 0, rotation: 0 });
  release();
  g.timeline({ delay: .2, onComplete: driftOnScroll })
    .to(".m1 > span", { yPercent: 0, duration: 1.1, ease: "power4.out" })
    .to(".m2 > span", { yPercent: 0, duration: 1.1, ease: "power4.out" }, "-=0.8")
    .to(quake, { x: 4, duration: .045, repeat: 5, yoyo: true, ease: "none" }, "+=0.35")
    .set(quake, { x: 0 })
    .to(bot, { x: "1.4vw", y: "0.8vw", rotation: 1.1, duration: .6, ease: "expo.out" })
    .to(top, { x: "-0.3vw", rotation: -.2, duration: .6, ease: "expo.out" }, "<")
    .to(foot, { autoAlpha: 1, duration: .9, ease: "power2.out" }, "-=0.25");


  function driftOnScroll() {
    if (!window.ScrollTrigger) return;
    const st = { trigger: "#top", start: "top top", end: "bottom top", scrub: 1 };
    g.to(bot, { y: "+=16vh", rotation: "+=4", ease: "none", scrollTrigger: st });
    g.to(top, { y: "-=4vh", ease: "none", scrollTrigger: { ...st } });
  }
}
hero();
})();
