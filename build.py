#!/usr/bin/env python3
"""
Meta on the Record static site builder.

Edit the files in src/, then run:  python3 build.py && python3 og.py
The finished site is written to ./docs, which GitHub Pages publishes.
"""
import csv, html, json, os, re, shutil, unicodedata
from datetime import date

BASE = "https://metaontherecord.org"          # change if you launch on another domain
UPDATED = date(2026, 9, 27)
SITE = "Meta on the Record"
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "src")
DIST = os.path.join(HERE, "docs")

D = json.load(open(os.path.join(SRC, "data.json"), encoding="utf-8"))
TIERS, THEMES, ENTRIES, CREDITS, NOTES = D["TIERS"], D["THEMES"], D["ENTRIES"], D["CREDITS"], D["NOTES"]
MONTHS = ["January","February","March","April","May","June","July","August","September","October","November","December"]

TOPIC_SEO = {
  "privacy":  ("Meta privacy violations, fines and verdicts", "Fines, settlements and verdicts over how Facebook, Instagram and WhatsApp collected and shared people’s personal data."),
  "lgbtq":    ("Meta, Facebook and the safety of LGBTQ+ people", "How Meta’s products and policies have exposed, endangered or been used to target LGBTQ+ people."),
  "abroad":   ("Facebook and violence abroad: Myanmar, Sri Lanka, Ethiopia", "Places where violence followed hate and rumors spread on Meta’s platforms, and what courts and investigators found."),
  "kids":     ("Meta and child safety: research, lawsuits and verdicts", "Meta’s internal research, lawsuits, settlements and jury verdicts on the safety of children and teenagers."),
  "democracy":("Meta, elections and misinformation", "Election interference, misinformation, fact-checking and transparency on Facebook and Instagram."),
  "rights":   ("Discrimination in Facebook advertising", "How Facebook’s advertising system was used to discriminate, and what regulators required."),
  "labor":    ("Meta’s content moderators: lawsuits and working conditions", "The people who reviewed violent and abusive material for Meta, and the cases they brought."),
  "scams":    ("Scam ads on Facebook and Instagram", "Fraudulent advertising on Meta’s platforms and what internal documents show about it."),
  "market":   ("Meta antitrust and competition cases", "Competition cases against Meta around the world, including the ones Meta won."),
}

esc = lambda s: html.escape(str(s or ""), quote=True)

def slugify(s, n=64):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s[:n].rstrip("-")

def year(d): return int(d[:4])
def month_year(d): return f"{MONTHS[int(d[5:7])-1]} {d[:4]}"
def short_date(d): return f"{MONTHS[int(d[5:7])-1][:3]} {d[:4]}"

def company(e):
    """Name the company as it was called at the time, for search titles."""
    t = e["title"]
    if re.search(r"\b(Meta|Facebook|Instagram|WhatsApp|Messenger)\b", t) or e["date"] >= "2021-10": return t
    return f"Facebook: {t}"

def describe(text, n=158):
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= n: return text
    cut = text[:n].rsplit(" ", 1)[0].rstrip(",;:")
    return cut + "…"

# ---------- stable URLs ----------
seen = set()
for e in ENTRIES:
    s = f"{year(e['date'])}-{slugify(e['title'])}"
    while s in seen: s += "-2"
    seen.add(s)
    e["slug"] = s
    e["url"] = f"/record/{s}/"
ORDER = sorted(ENTRIES, key=lambda e: e["date"])

# ---------- shared markup ----------
def glyph(tier, cls="glyph"):
    a = f'class="{cls}" viewBox="0 0 16 16" aria-hidden="true" focusable="false"'
    return {
      "ruled":     f'<svg {a}><rect x="1.5" y="1.5" width="13" height="13" fill="currentColor"/></svg>',
      "appeal":    f'<svg {a}><path d="M1.5 1.5h8.5l4.5 4.5v8.5h-13z" fill="currentColor"/></svg>',
      "settled":   f'<svg {a}><rect x="2.5" y="2.5" width="11" height="11" fill="none" stroke="currentColor" stroke-width="2"/><rect x="5.5" y="5.5" width="5" height="5" fill="currentColor"/></svg>',
      "admitted":  f'<svg {a}><rect x="2.5" y="2.5" width="11" height="11" fill="none" stroke="currentColor" stroke-width="2"/><rect x="2.5" y="2.5" width="5.5" height="11" fill="currentColor"/></svg>',
      "reported":  f'<svg {a}><rect x="2.5" y="2.5" width="11" height="11" fill="none" stroke="currentColor" stroke-width="2"/></svg>',
      "alleged":   f'<svg {a}><rect x="2.5" y="2.5" width="11" height="11" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="2.4 2"/></svg>',
      "dismissed": f'<svg {a}><rect x="2.5" y="2.5" width="11" height="11" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M3 13 13 3" stroke="currentColor" stroke-width="1.6"/></svg>',
      "credit":    f'<svg {a}><circle cx="8" cy="8" r="6" fill="currentColor"/></svg>',
    }.get(tier, "")

def tier_label(t): return "Credit" if t == "credit" else TIERS[t]["label"]

def sources_html(e, heading=False):
    if e.get("sources"):
        items = "".join(f'<li><a href="{esc(u)}" rel="noopener">{esc(l)}</a></li>' for l, u in e["sources"])
        return (f'<h2 class="a-h">Sources</h2>' if heading else "") + f'<ul class="src">{items}</ul>'
    if e.get("check"):
        return (f'<h2 class="a-h">Sources</h2>' if heading else "") + '<p class="pending">Primary source link being added. Figures are drawn from public reporting and will be linked before this entry is final.</p>'
    return ""

def response_html(e, credit=False):
    if credit:
        return f'<blockquote class="response"><b>Context</b>{esc(e["ctx"])}</blockquote>'
    if not e.get("response"): return ""
    label = "In their words" if e.get("who") else "Meta’s response"
    who = f' <span>({esc(e["who"])})</span>' if e.get("who") else ""
    return f'<blockquote class="response"><b>{label}</b>{esc(e["response"])}{who}</blockquote>'

def ledger_entry(e, credit=False):
    t = "credit" if credit else e["tier"]
    themes = "".join(f'<span class="tag">{esc(THEMES[k])}</span>' for k in e.get("themes", []))
    link = f'<a class="linkbtn" href="{e["url"]}">Open the full entry</a>' if e.get("url") else ""
    copy = e.get("url") or f'#e-{e["id"]}'
    fact = f'<div class="fact"><span class="fact-num">{esc(e["fig"])}</span><span class="fact-cap">{esc(e.get("cap",""))}</span></div>' if e.get("fig") else ""
    return f'''<li class="entry{' credit' if credit else ''}" id="e-{esc(e['id'])}">
    <button class="entry-head" aria-expanded="false" aria-controls="d-{esc(e['id'])}">
      <span class="entry-date">{short_date(e['date'])}</span>
      <span class="entry-title">{esc(e['title'])}</span>
      <span class="entry-fig">{esc(e.get('fig',''))}</span>
      <span class="entry-tier">{glyph(t)}{esc(tier_label(t))}</span>
      <span class="plus" aria-hidden="true"></span>
    </button>
    <div class="entry-body" id="d-{esc(e['id'])}" role="region" aria-label="{esc(e['title'])}">
      <div class="entry-inner"><div class="entry-content">
        <div class="main">
          {f'<p class="status">{esc(e["status"])}</p>' if e.get("status") else ""}
          <p>{esc(e['summary'])}</p>
          {response_html(e, credit)}
          {sources_html(e)}
          <div class="entry-meta">{themes}{link}<button class="linkbtn" data-copy="{esc(copy)}">Copy link</button></div>
        </div>
        <div class="side">{fact}</div>
      </div></div>
    </div>
  </li>'''

# ---------- G1: the record by year, one evidence glyph per entry (design/DESIGN.md §1) ----------
G1_YEARS = list(range(2007, UPDATED.year + 1))
STRENGTH = ["ruled", "appeal", "settled", "admitted", "reported", "alleged", "dismissed"]
RULING = {"ruled", "appeal"}

def _glyph_inner(tier):
    g = glyph(tier)
    return g[g.index(">") + 1:g.rindex("</svg>")]

def g1_chart(W, narrow=False):
    """Drawn at W px for its breakpoint, never scaled. Strongest evidence sits at the bottom of each year."""
    cols = {y: sorted([e for e in ENTRIES if year(e["date"]) == y], key=lambda e: (STRENGTH.index(e["tier"]), e["date"])) for y in G1_YEARS}
    n = len(G1_YEARS); colw = W / n
    cell = min(16 if narrow else 30, colw * 0.74); gap = max(2.0, cell * 0.14)
    stack = max(len(v) for v in cols.values())
    band = 34 if narrow else 58
    y0 = band + 22 + stack * (cell + gap)
    H = y0 + 40
    cx = lambda i: colw * i + colw / 2
    split = colw * G1_YEARS.index(2021)
    o = [f'<svg class="uc" width="{W}" height="{H:.0f}" viewBox="0 0 {W} {H:.0f}" aria-hidden="true">',
         f'<line class="axis" x1="0" x2="{W}" y1="{y0 + .5:.1f}" y2="{y0 + .5:.1f}"/>']
    o += [f'<line class="tick" x1="{cx(i):.1f}" x2="{cx(i):.1f}" y1="{y0:.1f}" y2="{y0 + 4:.1f}"/>' for i in range(n)]
    for yr in ([2007, 2014, 2021, G1_YEARS[-1]] if narrow else [2007, 2010, 2015, 2021, G1_YEARS[-1]]):
        i = G1_YEARS.index(yr); x = 0 if i == 0 else W if i == n - 1 else cx(i)
        anchor = "start" if i == 0 else "end" if i == n - 1 else "middle"
        o.append(f'<text class="yr{" em" if yr == 2021 else ""}" x="{x:.1f}" y="{y0 + 17:.1f}" text-anchor="{anchor}">{yr}</text>')
    o.append(f'<text class="yr" x="{W:.1f}" y="{y0 + 31:.1f}" text-anchor="end">so far</text>')
    o.append(f'<line class="divider" x1="{split:.1f}" x2="{split:.1f}" y1="{band - 10:.1f}" y2="{y0:.1f}"/>')
    for i, yr in enumerate(G1_YEARS):
        for k, e in enumerate(cols[yr]):
            t = e["tier"]; label = f'{e["title"]}, {month_year(e["date"])}. {TIERS[t]["label"]}.'
            o.append(f'<a class="sq{" rul" if t in RULING else ""}" data-id="{esc(e["id"])}" href="#e-{esc(e["id"])}" aria-label="{esc(label)}"><title>{esc(label)}</title>'
                     f'<svg x="{cx(i) - cell / 2:.1f}" y="{y0 - (k + 1) * (cell + gap) + gap:.1f}" width="{cell:.1f}" height="{cell:.1f}" viewBox="0 0 16 16">{_glyph_inner(t)}</svg></a>')
    top = lambda yr: y0 - len(cols[yr]) * (cell + gap) - 6
    peak = max(G1_YEARS, key=lambda y: len(cols[y]))
    o.append(f'<text class="dl" x="{cx(G1_YEARS.index(peak)):.1f}" y="{top(peak):.1f}" text-anchor="middle">{len(cols[peak])}</text>')
    if peak != G1_YEARS[-1] and not narrow:
        o.append(f'<text class="dl" x="{cx(n - 1):.1f}" y="{top(G1_YEARS[-1]):.1f}" text-anchor="middle">{len(cols[G1_YEARS[-1]])}</text>')
    by = band - 10
    for key, x1, x2, group in (("pre", 0, split, [e for e in ENTRIES if year(e["date"]) < 2021]),
                               ("post", split, W, [e for e in ENTRIES if year(e["date"]) >= 2021])):
        r = sum(1 for e in group if e["tier"] in RULING)
        o.append(f'<g class="br"><path d="M{x1 + 3:.1f} {by + 6:.1f}V{by:.1f}H{x2 - 3:.1f}V{by + 6:.1f}"/>')
        if narrow:
            short = "2007–20" if key == "pre" else "2021–"
            tail = f" · {r} of {len(group)} on a ruling" if key == "pre" else f" · {r} of {len(group)}"
            o.append(f'<text class="bl" x="{x1 + 3:.1f}" y="{by - 8:.1f}"><tspan class="bh">{short}</tspan>{tail}</text>')
        else:
            head = "2007 to 2020" if key == "pre" else "Since 2021"
            o.append(f'<text class="bh" x="{x1 + 3:.1f}" y="{by - 26:.1f}">{head}</text>'
                     f'<text class="bl" x="{x1 + 3:.1f}" y="{by - 9:.1f}">{len(group)} entries · {r} on a ruling</text>')
        o.append('</g>')
    # the one pre-2021 ruling is the exception that makes the headline true: label it where it sits
    early = [(i, k) for i, yr in enumerate(G1_YEARS) if yr < 2021 for k, e in enumerate(cols[yr]) if e["tier"] in RULING]
    if len(early) == 1 and not narrow:
        i, k = early[0]; e = cols[G1_YEARS[i]][k]
        sy = y0 - (k + 1) * (cell + gap) + gap + cell / 2; lx = colw * i; ny = y0 - (stack - 2) * (cell + gap)
        o.append(f'<g class="note"><text x="{lx - 8:.1f}" y="{ny:.1f}" text-anchor="end">The one earlier ruling:</text>'
                 f'<text x="{lx - 8:.1f}" y="{ny + 17:.1f}" text-anchor="end">{esc(e["title"].split(" exposes")[0])}, {year(e["date"])}</text>'
                 f'<path d="M{lx - 4:.1f} {ny + 12:.1f}H{lx:.1f}V{sy:.1f}H{cx(i) - cell / 2 - 3:.1f}"/>'
                 f'<circle cx="{cx(i) - cell / 2 - 3:.1f}" cy="{sy:.1f}" r="2"/></g>')
    o.append('</svg>')
    return "".join(o)

def g1_html():
    rulings = [e for e in ENTRIES if e["tier"] in RULING]
    recent = [e for e in rulings if year(e["date"]) >= 2021]
    key = ", ".join(f'<span class="k{" rul" if t in RULING else ""}">{glyph(t)}{esc(TIERS[t]["label"].lower())}</span>' for t in STRENGTH)
    rows = "".join(f'<tr><th scope="row">{y}</th><td>{sum(1 for e in ENTRIES if year(e["date"]) == y)}</td>'
                   f'<td>{sum(1 for e in rulings if year(e["date"]) == y)}</td></tr>' for y in G1_YEARS)
    return (f'<figure class="g1" id="g1" data-shot="g1"><figcaption>'
            f'<p class="g-head">Of the <span class="kchip">{len(rulings)}</span> entries resting on a ruling against Meta, {len(recent)} are events from 2021 or later.</p>'
            f'<p class="g-method">Each square is one entry, stacked in the year the event happened and drawn as its evidence label: {key}. '
            f'It counts entries in this record, not incidents, and coverage before 2017 is thinner.</p></figcaption>'
            f'<div class="uc-w">{g1_chart(832)}</div><div class="uc-m">{g1_chart(700)}</div><div class="uc-n">{g1_chart(350, narrow=True)}</div>'
            f'<p class="g-source">Source: Meta on the Record entries, dated by the year of the event; {UPDATED.year} runs through {MONTHS[UPDATED.month - 1]}. '
            f'<a href="/data/record.csv">Download the data</a></p>'
            f'<details class="g-table"><summary>Show the numbers as a table</summary><table><thead><tr><th scope="col">Year</th>'
            f'<th scope="col">Entries</th><th scope="col">On a ruling</th></tr></thead><tbody>{rows}</tbody></table></details></figure>')

# ---------- G2: penalties as days of 2025 revenue (design/DESIGN.md §1) ----------
REVENUE_2025 = 201  # $ billions, as reported by PBS NewsHour
# (label, detail, shown amount, value in $ billions; euros counted one to one, as in the total, short name for the chart)
TALLY = [
    ("State attorneys general, child safety", "2026, paid over ten years", "$12.1B", 12.1, "State attorneys general"),
    ("Federal Trade Commission, privacy", "2019", "$5B", 5, "FTC"),
    ("European regulators", "2017 to 2025, some under appeal", "€4.0B", 4.0, "European regulators"),
    ("Texas, facial recognition", "2024", "$1.4B", 1.4, "Texas"),
    ("Texas, child safety", "2026", "$1B", 1, "Texas"),
    ("Cambridge Analytica class action", "final in 2025", "$725M", 0.725, "Cambridge Analytica"),
    ("Illinois, facial recognition", "2021", "$650M", 0.65, "Illinois"),
    ("Other US and international cases", "SEC, moderators, Nigeria, India and more", "~$0.6B", 0.6, "Other cases"),
]
MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def g2_segments():
    """Days each payer fills, rounded cumulatively so the segments always add up to the total."""
    per_day = REVENUE_2025 / 365
    out, cum, prev = [], 0.0, 0
    for row in TALLY:
        cum += row[3]
        end = round(cum / per_day)
        out.append((prev, end))
        prev = end
    return out

def g2_calendar(W, narrow=False, uid="w"):
    segs = g2_segments(); total = segs[-1][1]
    lab = 30 if narrow else 40
    gap = 2 if narrow else 3
    cell = (W - lab - 30 * gap) / 31
    rowh = cell + gap
    top = 30 if narrow else 34          # room for the January brackets
    feb_extra = 30                       # room under February for its brackets
    H = top + rowh * 12 + feb_extra
    y_of = lambda m: top + m * rowh + (feb_extra if m >= 2 else 0)
    x_of = lambda d: lab + d * (cell + gap)
    seg_of = {}
    for i, (a, b) in enumerate(segs):
        for d in range(a, b): seg_of[d] = i
    o = [f'<svg class="cal" width="{W}" height="{H:.0f}" viewBox="0 0 {W} {H:.0f}" aria-hidden="true">',
         f'<defs><pattern id="owed-{uid}" width="4" height="4" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
         '<rect width="4" height="4" class="owed-bg"/><rect width="1.4" height="4" class="owed-line"/></pattern></defs>']
    day = 0
    for m, n in enumerate(MONTH_DAYS):
        y = y_of(m)
        if not narrow or m in (0, 6, 11):
            o.append(f'<text class="mo" x="0" y="{y + cell * .8:.1f}">{MONTHS[m][:3]}</text>')
        for d in range(n):
            s = seg_of.get(day)
            if s is None:
                o.append(f'<rect class="rev" x="{x_of(d):.1f}" y="{y:.1f}" width="{cell:.1f}" height="{cell:.1f}"/>')
            else:
                owed = f' owed" style="fill:url(#owed-{uid})' if s == 0 else ''
                o.append(f'<rect class="pen{owed}" data-seg="{s}" x="{x_of(d):.1f}" y="{y:.1f}" width="{cell:.1f}" height="{cell:.1f}"/>')
            day += 1
    # brackets: January above, February below, one per payer group
    def bracket(m, d0, d1, text, above):
        x1, x2 = x_of(d0) + .5, x_of(d1 - 1) + cell - .5
        if above:
            y = y_of(m) - 5
            return (f'<path class="bk" d="M{x1:.1f} {y + 3:.1f}V{y:.1f}H{x2:.1f}V{y + 3:.1f}"/>'
                    f'<text class="bt" x="{x1:.1f}" y="{y - 5:.1f}">{text}</text>')
        y = y_of(m) + cell + 5
        return (f'<path class="bk" d="M{x1:.1f} {y - 3:.1f}V{y:.1f}H{x2:.1f}V{y - 3:.1f}"/>'
                f'<text class="bt" x="{x1:.1f}" y="{y + 14:.1f}">{text}</text>')
    jan_ag, jan_ftc = segs[0], segs[1]
    feb0 = MONTH_DAYS[0]
    ag_len, ftc_len = jan_ag[1] - jan_ag[0], jan_ftc[1] - jan_ftc[0]
    eu = segs[2]; rest = (segs[3][0], segs[-1][1])
    o.append(bracket(0, jan_ag[0], jan_ag[1], f'State attorneys general · {ag_len} days' if not narrow else f'State AGs · {ag_len} days', True))
    o.append(bracket(0, jan_ftc[0], jan_ftc[1], f'FTC · {ftc_len}', True))
    o.append(bracket(1, eu[0] - feb0, eu[1] - feb0, f'EU · {eu[1] - eu[0]}', False))
    o.append(bracket(1, rest[0] - feb0, rest[1] - feb0, f'Others · {rest[1] - rest[0]}', False))
    o.append('</svg>')
    return "".join(o), total

def g2_html():
    segs = g2_segments()
    total_days = segs[-1][1]
    import datetime as _dt
    last = _dt.date(2025, 1, 1) + _dt.timedelta(days=total_days - 1)
    wide, _ = g2_calendar(640, uid="w"); mid, _ = g2_calendar(560, uid="m"); narrow, _ = g2_calendar(350, narrow=True, uid="n")
    rows = "".join(f'<li data-seg="{i}"><span>{esc(label)}<small>{esc(detail)}</small></span><b>{esc(shown)}</b></li>'
                   for i, (label, detail, shown, _v, _s) in enumerate(TALLY))
    total = sum(r[3] for r in TALLY)
    return f'''<div class="money-grid" data-shot="money">
      <figure class="g2">
        <figcaption>
          <p class="g-head">Meta took in enough revenue in 2025 to cover every fine and settlement in this record by <span class="kchip">{MONTHS[last.month - 1]} {last.day}</span>.</p>
          <p class="g-method">Each square is one day of Meta’s 2025 revenue: ${REVENUE_2025} billion ÷ 365, about ${REVENUE_2025 / 365 * 1000:.0f} million a day. Penalties fill days from January 1 at their announced value, with euros counted one to one. The hatched days are the state settlement, which is paid over ten years.</p>
        </figcaption>
        <div class="uc-w">{wide}</div><div class="uc-m">{mid}</div><div class="uc-n">{narrow}</div>
        <p class="g-source">Sources: revenue as reported by PBS NewsHour; penalties as linked in each entry.</p>
      </figure>
      <div>
        <ul class="tally">{rows}<li class="sum"><span>Total</span><b>${total:.0f}B+</b></li></ul>
        <p class="money-notes">The total is a minimum. It leaves out New Mexico’s $942 million judgment and other verdicts under appeal, damages still to be set in the Flo case, and more than 200,000 pending individual claims.</p>
      </div>
    </div>'''

def g1_mini(this, W=272):
    """The whole record as a small strip, with this entry as the only accent (entry pages)."""
    cols = {y: sorted([e for e in ENTRIES if year(e["date"]) == y], key=lambda e: (STRENGTH.index(e["tier"]), e["date"])) for y in G1_YEARS}
    n = len(G1_YEARS); colw = W / n
    cell = min(11, colw * 0.78); gap = 1.6
    stack = max(len(v) for v in cols.values())
    y0 = stack * (cell + gap) + 2
    H = y0 + 18
    cx = lambda i: colw * i + colw / 2
    o = [f'<svg class="mini" width="{W}" height="{H:.0f}" viewBox="0 0 {W} {H:.0f}" aria-hidden="true">',
         f'<line class="axis" x1="0" x2="{W}" y1="{y0 + .5:.1f}" y2="{y0 + .5:.1f}"/>']
    for yr in (2007, 2021, G1_YEARS[-1]):
        i = G1_YEARS.index(yr); x = 0 if i == 0 else W if i == n - 1 else cx(i)
        anchor = "start" if i == 0 else "end" if i == n - 1 else "middle"
        o.append(f'<text class="yr" x="{x:.1f}" y="{y0 + 14:.1f}" text-anchor="{anchor}">{yr}</text>')
    for i, yr in enumerate(G1_YEARS):
        for k, e in enumerate(cols[yr]):
            cls = "sq this" if e is this else "sq"
            if e is this:
                o.append(f'<rect class="ring" x="{cx(i) - cell / 2 - 3:.1f}" y="{y0 - (k + 1) * (cell + gap) + gap - 3:.1f}" width="{cell + 6:.1f}" height="{cell + 6:.1f}"/>')
            o.append(f'<a class="{cls}" href="{e["url"]}" aria-label="{esc(e["title"])}"><title>{esc(e["title"])}, {month_year(e["date"])}</title>'
                     f'<svg x="{cx(i) - cell / 2:.1f}" y="{y0 - (k + 1) * (cell + gap) + gap:.1f}" width="{cell:.1f}" height="{cell:.1f}" viewBox="0 0 16 16">{_glyph_inner(e["tier"])}</svg></a>')
    o.append('</svg>')
    same = len(cols[year(this["date"])])
    lab = TIERS[this["tier"]]["label"].lower()
    peers = sum(1 for e in ENTRIES if e["tier"] == this["tier"])
    cap = (f'One of {same} {"entry" if same == 1 else "entries"} from {year(this["date"])}, and one of {peers} labeled {lab}. '
           f'Each square is an entry in the record; this one is in blue.')
    return f'<figure class="mini-fig"><figcaption>{esc(cap)}</figcaption>{"".join(o)}<p class="g-source"><a href="/#g1">See the whole record</a></p></figure>'

def ledger_html():
    groups = {}
    for e in ORDER: groups.setdefault(year(e["date"]), []).append(e)
    return "".join(f'<section class="year" id="y{y}" aria-label="{y}"><h3 class="year-num">{y}</h3><ol class="entries">{"".join(ledger_entry(e) for e in lst)}</ol></section>' for y, lst in groups.items())

def credits_html():
    rows = []
    for c in CREDITS:
        big = f'<span class="big">{esc(c["fig"])}</span>' if c.get("fig") else ""
        rows.append(f'''<li class="credit-row" id="{esc(c['id'])}"><span class="when">{short_date(c['date'])}</span><div>{big}<h3>{esc(c['title'])}</h3><p>{esc(c['summary'])}</p></div><div><p class="ctx"><b>Context</b>{esc(c['ctx'])}</p>{sources_html(c)}</div></li>''')
    return "".join(rows)

WORDMARK = '<svg aria-hidden="true"><use href="#mark"/></svg>'
SYMBOL = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true"><symbol id="mark" viewBox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd" d="M3 3h18v18H3z M7 7.5h10v2H7z M7 11.5h10v2H7z M7 15.5h6v2H7z"/></symbol></svg>'''

FONTS = '''<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,300..900&family=Newsreader:ital,opsz,wght@0,6..72,300..700;1,6..72,300..700&display=swap" rel="stylesheet">'''

GTAG = '''<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-3WWWFXQHPM"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-3WWWFXQHPM');
</script>'''

def head(title, desc, path, image, jsonld, extra=""):
    url = BASE + path
    ld = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in jsonld)
    return f'''<!doctype html>
<html lang="en">
<head>
{GTAG}
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#1F2FC8">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate" type="application/json" href="/data/record.json" title="Meta on the Record data (JSON)">
<meta property="og:site_name" content="{SITE}">
<meta property="og:type" content="{'website' if path == '/' else 'article'}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}{image}">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{BASE}{image}">
{FONTS}
<link rel="stylesheet" href="/assets/site.css">
{extra}
{ld}
</head>'''

PUBLISHER = {"@type": "Organization", "name": SITE, "url": BASE + "/"}
META_ORG = {"@type": "Organization", "name": "Meta Platforms", "sameAs": ["https://en.wikipedia.org/wiki/Meta_Platforms", "https://www.wikidata.org/wiki/Q380"]}

def footer():
    topics = "".join(f'<li><a href="/topics/{k}/">{esc(v)}</a></li>' for k, v in THEMES.items())
    return f'''<footer class="foot">
  <div class="wrap">
    <p class="foot-big" aria-hidden="true">Meta on the Record</p>
    <nav class="foot-topics" aria-label="Browse by topic"><h2>Browse by topic</h2><ul>{topics}</ul></nav>
    <div class="foot-cols">
      <p>An independent record. Not affiliated with Meta Platforms, Facebook, Instagram or WhatsApp. Researched, written and organized with AI (Anthropic’s Claude). <a href="/#made">How this was made</a></p>
      <p>Last updated {MONTHS[UPDATED.month-1]} {UPDATED.day}, {UPDATED.year}. The data is free to reuse with credit: <a href="/data/record.csv">CSV</a>, <a href="/data/record.json">JSON</a>.</p>
      <p>Found an error? Send a correction with a source. Corrections are dated and published. <span id="contact">Contact address coming soon.</span></p>
    </div>
  </div>
</footer>'''

def masthead():
    return f'''{SYMBOL}
<a class="skip" href="#main">Skip to content</a>
<header class="masthead"><div class="wrap">
  <a class="wordmark" href="/">{WORDMARK}Meta on the Record</a>
  <span class="mast-tag">Sourced and labeled by strength of evidence</span>
  <a class="mast-link" href="/#record">The full record</a>
</div></header>'''

# ---------- write helpers ----------
def write(path, text):
    full = os.path.join(DIST, path.lstrip("/"))
    if full.endswith("/"): full += "index.html"
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f: f.write(text)

def main():
    if os.path.exists(DIST): shutil.rmtree(DIST)
    os.makedirs(DIST)
    urls = []

    # assets
    os.makedirs(os.path.join(DIST, "assets"))
    shutil.copy(os.path.join(SRC, "styles.css"), os.path.join(DIST, "assets", "site.css"))
    shutil.copytree(os.path.join(SRC, "img"), os.path.join(DIST, "img"))
    data_js = "const TIERS=%s;\nconst THEMES=%s;\nconst ENTRIES=%s;\nconst CREDITS=%s;\nconst NOTES=%s;\n" % tuple(
        json.dumps(x, ensure_ascii=False) for x in (TIERS, THEMES, ENTRIES, CREDITS, NOTES))
    write("/assets/data.js", data_js)
    write("/assets/app.js", "(() => {" + open(os.path.join(SRC, "app.js"), encoding="utf-8").read() + "})();\n")
    write("/favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><rect width="24" height="24" rx="4" fill="#1F2FC8"/><path fill="#fff" d="M7 7.5h10v2H7zM7 11.5h10v2H7zM7 15.5h6v2H7z"/></svg>')

    # ---- index ----
    body = open(os.path.join(SRC, "home.html"), encoding="utf-8").read()
    body = body.replace('<div class="g1-slot"></div>', g1_html())
    body = body.replace('<div class="g2-slot"></div>', g2_html())
    body = re.sub(r'<span class="node" data-tier="(\w+)"></span>', lambda m: f'<span class="node" aria-hidden="true">{glyph(m.group(1))}</span>', body)
    body = body.replace('<div class="ledger" id="ledger"></div>', f'<div class="ledger" id="ledger">{ledger_html()}</div>')
    body = body.replace('<ol class="credit-list" id="creditlist"></ol>', f'<ol class="credit-list" id="creditlist">{credits_html()}</ol>')
    tierdefs = "".join(f'<div><dt>{glyph(k)}{esc(t["label"])}</dt><dd>{esc(t["def"])}</dd></div>' for k, t in TIERS.items())
    tierdefs += f'<div><dt>{glyph("credit")}Credit</dt><dd>Something Meta did well, listed with the context it needs.</dd></div>'
    body = body.replace('<dl class="tiers" id="tierdefs" data-shot="labels"></dl>', f'<dl class="tiers" id="tierdefs" data-shot="labels">{tierdefs}</dl>')
    notes = "".join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in NOTES)
    body = body.replace('<div class="notes" id="notes"></div>', f'<div class="notes" id="notes">{notes}</div>')
    body = re.sub(r'<span class="tierline" data-tier="(\w+)"></span>',
                  lambda m: f'<span class="tierline" data-tier="{m.group(1)}">{glyph(m.group(1))}{esc(tier_label(m.group(1)))}</span>', body)
    body = body.replace(f'<p class="hero-meta" id="herometa">Updated September 27, 2026</p>',
                        f'<p class="hero-meta" id="herometa">{len(ENTRIES)} entries from {year(ORDER[0]["date"])} to {year(ORDER[-1]["date"])}. Updated September 27, 2026.</p>')
    # swap the page footer for the shared one with topic links and data downloads
    body = re.sub(r'<footer class="foot">.*?</footer>', footer(), body, flags=re.S)
    body = body.replace('<a class="btn btn-ghost" href="#method">How evidence is labeled</a>',
                        '<a class="btn btn-ghost" href="#method">How evidence is labeled</a>')
    idx_title = "Meta on the Record: court rulings, findings and reported events, 2007 to 2026"
    idx_desc = "Court rulings, regulatory findings and reported events involving Meta, Facebook, Instagram and WhatsApp, from Cambridge Analytica to the 2026 verdicts. Each entry is labeled by evidence strength and linked to its sources."
    ld_site = {"@context": "https://schema.org", "@type": "WebSite", "name": SITE, "url": BASE + "/", "description": idx_desc, "publisher": PUBLISHER, "about": META_ORG}
    ld_data = {"@context": "https://schema.org", "@type": "Dataset", "name": "Meta on the Record: rulings, findings and reported events involving Meta Platforms",
               "description": "Each record lists a date, a description, an evidence label (ruled, under appeal, settled, admitted, reported, alleged or dismissed), key figures, Meta’s response and source links. Covers " + str(year(ORDER[0]['date'])) + " to " + str(year(ORDER[-1]['date'])) + ".",
               "url": BASE + "/", "creator": PUBLISHER, "measurementTechnique": "Researched, written and organized with AI (Anthropic’s Claude) and checked against linked public sources.", "dateModified": UPDATED.isoformat(),
               "license": "https://creativecommons.org/licenses/by/4.0/", "isAccessibleForFree": True, "about": META_ORG,
               "temporalCoverage": f"{ORDER[0]['date']}/{ORDER[-1]['date']}",
               "distribution": [{"@type": "DataDownload", "encodingFormat": "text/csv", "contentUrl": BASE + "/data/record.csv"},
                                {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": BASE + "/data/record.json"}]}
    motion = '<script>if(!window.matchMedia("(prefers-reduced-motion: reduce)").matches)document.documentElement.classList.add("motion");</script>'
    scripts = '''<script src="/assets/data.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.13.0/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.13.0/ScrollTrigger.min.js"></script>
<script src="/assets/app.js"></script>
</body>
</html>'''
    write("/", head(idx_title, idx_desc, "/", "/og/index.png", [ld_site, ld_data], motion) + "\n" + body + scripts)
    urls.append(("/", "1.0"))

    # ---- entry pages ----
    for i, e in enumerate(ORDER):
        prev_e = ORDER[i-1] if i > 0 else None
        next_e = ORDER[i+1] if i < len(ORDER)-1 else None
        title = f"{company(e)} ({short_date(e['date'])}) | {SITE}"
        desc = describe(e["summary"])
        t = TIERS[e["tier"]]
        topics = "".join(f'<a class="tag" href="/topics/{k}/">{esc(THEMES[k])}</a>' for k in e["themes"])
        figblock = f'<div class="fact"><span class="fact-num">{esc(e["fig"])}</span><span class="fact-cap">{esc(e.get("cap",""))}</span></div>' if e.get("fig") else ''
        fact = f'<aside class="a-side">{figblock}{g1_mini(e)}</aside>'
        pager = '<nav class="pager" aria-label="More entries">'
        pager += (f'<a class="pg prev" href="{prev_e["url"]}"><span class="label">Earlier</span>{esc(prev_e["title"])}</a>' if prev_e else '<span></span>')
        pager += (f'<a class="pg next" href="{next_e["url"]}"><span class="label">Later</span>{esc(next_e["title"])}</a>' if next_e else '<span></span>')
        pager += '</nav>'
        ld_article = {"@context": "https://schema.org", "@type": "Article", "headline": company(e)[:110], "description": desc,
                      "datePublished": UPDATED.isoformat(), "dateModified": UPDATED.isoformat(),
                      "mainEntityOfPage": BASE + e["url"], "image": BASE + f"/og/{e['slug']}.png",
                      "author": PUBLISHER, "publisher": PUBLISHER, "about": META_ORG,
                      "keywords": ", ".join(THEMES[k] for k in e["themes"]),
                      "citation": [u for _, u in e.get("sources", [])]}
        ld_crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "The record", "item": BASE + "/#record"},
            {"@type": "ListItem", "position": 2, "name": THEMES[e["themes"][0]], "item": BASE + f"/topics/{e['themes'][0]}/"},
            {"@type": "ListItem", "position": 3, "name": e["title"], "item": BASE + e["url"]}]}
        page = head(title, desc, e["url"], f"/og/{e['slug']}.png", [ld_article, ld_crumbs]) + f'''
<body class="page">
{masthead()}
<main id="main" class="article wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/#record">The record</a><span aria-hidden="true">/</span><a href="/topics/{e['themes'][0]}/">{esc(THEMES[e['themes'][0]])}</a></nav>
  <p class="a-date"><time datetime="{e['date']}">{month_year(e['date'])}</time></p>
  <h1 class="a-title">{esc(e['title'])}</h1>
  <p class="a-tier">{glyph(e['tier'])}<b>{esc(t['label'])}.</b> {esc(t['def'])} <a href="/#method">How evidence is labeled</a></p>
  <div class="a-grid">
    <div class="a-main">
      {f'<p class="status">{esc(e["status"])}</p>' if e.get("status") else ""}
      <p class="a-lede">{esc(e['summary'])}</p>
      {response_html(e)}
      <p class="ai-note">This entry was researched and written with AI (Anthropic’s Claude) from the sources below. <a href="/#made">How this was made</a></p>
      {sources_html(e, heading=True)}
      <h2 class="a-h">Topics</h2><div class="a-topics">{topics}</div>
    </div>
    {fact}
  </div>
  {pager}
</main>
{footer()}
</body>
</html>'''
        write(e["url"], page)
        urls.append((e["url"], "0.8"))

    # ---- topic pages ----
    for k, name in THEMES.items():
        items = [e for e in ORDER if k in e["themes"]]
        seo_title, intro = TOPIC_SEO[k]
        rows = "".join(f'''<li><a class="row" href="{e['url']}"><span class="entry-date">{short_date(e['date'])}</span><span class="entry-title">{esc(e['title'])}</span><span class="entry-fig">{esc(e.get('fig',''))}</span><span class="entry-tier">{glyph(e['tier'])}{esc(TIERS[e['tier']]['label'])}</span></a></li>''' for e in items)
        tallies = {}
        for e in items: tallies[e["tier"]] = tallies.get(e["tier"], 0) + 1
        short = {"appeal": "under appeal"}
        tally = ", ".join(f"{tallies[t]} {short.get(t, TIERS[t]['label'].lower())}" for t in TIERS if t in tallies)
        ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": seo_title, "description": intro, "url": BASE + f"/topics/{k}/",
              "isPartOf": {"@type": "WebSite", "name": SITE, "url": BASE + "/"}, "about": META_ORG,
              "hasPart": [{"@type": "Article", "headline": e["title"], "url": BASE + e["url"]} for e in items]}
        page = head(f"{seo_title} | {SITE}", intro, f"/topics/{k}/", f"/og/topic-{k}.png", [ld]) + f'''
<body class="page">
{masthead()}
<main id="main" class="article wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/#record">The record</a><span aria-hidden="true">/</span><span>{esc(name)}</span></nav>
  <h1 class="a-title">{esc(seo_title)}</h1>
  <p class="a-lede topic-intro">{esc(intro)}</p>
  <p class="topic-count">{len(items)} {'entry' if len(items)==1 else 'entries'}: {esc(tally)}.</p>
  <ol class="topic-list">{rows}</ol>
</main>
{footer()}
</body>
</html>'''
        write(f"/topics/{k}/", page)
        urls.append((f"/topics/{k}/", "0.7"))

    # ---- 404 ----
    write("/404.html", head(f"Page not found | {SITE}", "This page does not exist.", "/404.html", "/og/index.png", []) .replace('content="index, follow, max-image-preview:large"', 'content="noindex"') + f'''
<body class="page">{masthead()}<main id="main" class="article wrap notfound"><h1 class="a-title">This page doesn’t exist.</h1><p class="a-lede">The link may be old or mistyped. The full record has every entry, with search and filters, and the topics below group them by subject.</p><p class="nf-actions"><a class="btn btn-ink" href="/#record">Go to the full record</a></p></main>{footer()}</body></html>''')

    # ---- data downloads ----
    os.makedirs(os.path.join(DIST, "data"), exist_ok=True)
    public = [{"id": e["id"], "date": e["date"], "title": e["title"], "evidence": e["tier"], "evidence_label": TIERS[e["tier"]]["label"],
               "topics": e["themes"], "summary": e["summary"], "figure": e.get("fig", ""), "figure_caption": e.get("cap", ""),
               "status": e.get("status", ""), "meta_response": e.get("response", ""), "response_attribution": e.get("who", ""),
               "sources": [{"label": l, "url": u} for l, u in e.get("sources", [])], "needs_source": bool(e.get("check")),
               "url": BASE + e["url"]} for e in ORDER]
    json.dump({"name": "Meta on the Record", "updated": UPDATED.isoformat(), "license": "CC BY 4.0", "method": "Researched, written and organized with AI (Anthropic’s Claude) and checked against the linked public sources. AI can make mistakes; verify against the sources.", "entries": public},
              open(os.path.join(DIST, "data", "record.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    with open(os.path.join(DIST, "data", "record.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id","date","title","evidence","topics","summary","figure","figure_caption","status","meta_response","sources","needs_source","url"])
        for p in public:
            w.writerow([p["id"], p["date"], p["title"], p["evidence_label"], "; ".join(THEMES[t] for t in p["topics"]), p["summary"], p["figure"],
                        p["figure_caption"], p["status"], p["meta_response"], " | ".join(s["url"] for s in p["sources"]), p["needs_source"], p["url"]])

    # ---- sitemap + robots ----
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path, pr in urls:
        sm.append(f"<url><loc>{BASE}{path}</loc><lastmod>{UPDATED.isoformat()}</lastmod><priority>{pr}</priority></url>")
    sm.append("</urlset>")
    write("/sitemap.xml", "\n".join(sm))
    write("/robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    # GitHub Pages: keep the custom domain and skip Jekyll processing
    write("/CNAME", BASE.split("://", 1)[1] + "\n")
    write("/.nojekyll", "")

    # manifest of pages for the social-image step
    json.dump({"index": {"title": "Meta on the Record", "kicker": ""},
               "entries": [{"slug": e["slug"], "title": e["title"], "date": month_year(e["date"]), "fig": e.get("fig", ""), "cap": e.get("cap", ""), "tier": e["tier"], "tierLabel": TIERS[e["tier"]]["label"]} for e in ORDER],
               "topics": [{"key": k, "title": TOPIC_SEO[k][0], "count": sum(1 for e in ORDER if k in e["themes"])} for k in THEMES]},
              open(os.path.join(HERE, "og-manifest.json"), "w", encoding="utf-8"), ensure_ascii=False)
    print(f"Built {len(urls)} pages into {DIST}")

if __name__ == "__main__":
    main()
