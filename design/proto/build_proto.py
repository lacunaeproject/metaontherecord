#!/usr/bin/env python3
"""
Phase 3 prototypes: three directions for the hero and G1 ("What the record rests on").

    python3 build.py && python3 design/proto/build_proto.py

Writes docs/v1/, docs/v2/, docs/v3/ and docs/proto-assets/. Those paths are gitignored so the
prototypes are never published; view them with `npm run serve`.
"""
import os, re, shutil, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, ROOT)
import build as B  # noqa: E402  (reuses the site's data, glyphs, head and footer)

YEARS = list(range(2007, 2027))
STRENGTH = ["ruled", "appeal", "settled", "admitted", "reported", "alleged", "dismissed"]
RULING = {"ruled", "appeal"}
esc = B.esc


def glyph_inner(tier):
    g = B.glyph(tier)
    return g[g.index(">") + 1:g.rindex("</svg>")]


def month_year(d):
    return f"{B.MONTHS[int(d[5:7]) - 1]} {d[:4]}"


def columns(entries):
    cols = defaultdict(list)
    for e in entries:
        cols[int(e["date"][:4])].append(e)
    for y in cols:
        cols[y].sort(key=lambda e: (STRENGTH.index(e["tier"]), e["date"]))
    return cols


def square(e, x, y, size):
    t = e["tier"]
    cls = "sq rul" if t in RULING else "sq"
    era = "pre" if int(e["date"][:4]) < 2021 else "post"
    label = f'{e["title"]}, {month_year(e["date"])}. {B.TIERS[t]["label"]}.'
    return (f'<a class="{cls}" data-era="{era}" data-tier="{t}" href="{e["url"]}" aria-label="{esc(label)}">'
            f'<title>{esc(label)}</title>'
            f'<svg x="{x:.1f}" y="{y:.1f}" width="{size:.1f}" height="{size:.1f}" viewBox="0 0 16 16">{glyph_inner(t)}</svg></a>')


def unit_chart(entries, W, *, narrow=False, cell_max=30, ticks=None, brackets=True, direct=True, compact=False, stack=None):
    """Columns by year, one evidence-glyph square per entry, strongest at the bottom. Drawn at W px, not scaled."""
    cols = columns(entries)
    n = len(YEARS)
    colw = W / n
    cell = min(cell_max, colw * 0.74)
    gap = max(2.0, cell * 0.14)
    stack = stack or max((len(v) for v in cols.values()), default=1)
    band = 0 if not brackets else (30 if narrow else 58)
    dl = 20 if direct else 6
    plot = stack * (cell + gap)
    y0 = band + dl + plot
    H = y0 + (40 if not compact else 18)
    cx = lambda i: colw * i + colw / 2
    out = [f'<svg class="uc" width="{W}" height="{H:.0f}" viewBox="0 0 {W} {H:.0f}" role="img" aria-hidden="true">']
    # baseline and per-year zero ticks, so empty years read as zero rather than missing
    out.append(f'<line class="axis" x1="0" x2="{W}" y1="{y0 + 0.5:.1f}" y2="{y0 + 0.5:.1f}"/>')
    for i in range(n):
        out.append(f'<line class="tick" x1="{cx(i):.1f}" x2="{cx(i):.1f}" y1="{y0:.1f}" y2="{y0 + 4:.1f}"/>')
    ticks = ticks or ([2007, 2014, 2021, 2026] if narrow else [2007, 2010, 2015, 2021, 2026])
    for yr in ticks:
        i = YEARS.index(yr)
        anchor = "start" if i == 0 else "end" if i == n - 1 else "middle"
        x = 0 if i == 0 else W if i == n - 1 else cx(i)
        out.append(f'<text class="yr{" em" if yr == 2021 else ""}" x="{x:.1f}" y="{y0 + 17:.1f}" text-anchor="{anchor}">{yr}</text>')
        if yr == 2026 and not compact:
            out.append(f'<text class="yr" x="{x:.1f}" y="{y0 + 31:.1f}" text-anchor="end">so far</text>')
    # 2021 divider
    split = colw * YEARS.index(2021)
    if brackets:
        out.append(f'<line class="divider" x1="{split:.1f}" x2="{split:.1f}" y1="{band - 10:.1f}" y2="{y0:.1f}"/>')
    for i, yr in enumerate(YEARS):
        for k, e in enumerate(cols.get(yr, [])):
            out.append(square(e, cx(i) - cell / 2, y0 - (k + 1) * (cell + gap) + gap, cell))
    if direct:
        top = lambda yr: y0 - len(cols.get(yr, [])) * (cell + gap) - 6
        if cols.get(2025):
            out.append(f'<text class="dl" x="{cx(YEARS.index(2025)):.1f}" y="{top(2025):.1f}" text-anchor="middle">{len(cols[2025])}</text>')
        if cols.get(2026):
            out.append(f'<text class="dl" x="{cx(YEARS.index(2026)):.1f}" y="{top(2026):.1f}" text-anchor="middle">{len(cols[2026])}</text>')
    if brackets:
        pre = [e for e in entries if int(e["date"][:4]) < 2021]
        post = [e for e in entries if int(e["date"][:4]) >= 2021]
        spans = [("pre", 0, split, "2007 to 2020", pre), ("post", split, W, "Since 2021", post)]
        by = band - 10
        for key, x1, x2, head, group in spans:
            r = sum(1 for e in group if e["tier"] in RULING)
            out.append(f'<g class="br br-{key}"><path d="M{x1 + 3:.1f} {by + 6:.1f}V{by:.1f}H{x2 - 3:.1f}V{by + 6:.1f}"/>')
            if narrow:
                out.append(f'<circle cx="{x1 + 12:.1f}" cy="{by - 11:.1f}" r="8"/><text class="mk" x="{x1 + 12:.1f}" y="{by - 7:.1f}" text-anchor="middle">{1 if key == "pre" else 2}</text>')
            else:
                out.append(f'<text class="bh" x="{x1 + 3:.1f}" y="{by - 26:.1f}">{head}</text>'
                           f'<text class="bl" x="{x1 + 3:.1f}" y="{by - 9:.1f}">{len(group)} entries · {r} {"ruling" if r == 1 else "rulings"}</text>')
            out.append('</g>')
    out.append('</svg>')
    return "".join(out)


def rotated_chart(entries, W):
    """Phone layout for the monument: years as rows, squares running right."""
    cols = columns(entries)
    labw = 44
    cell = min(30, (W - labw - 8) / 9 - 4)
    gap = 4
    rowh = cell + 6
    H = len(YEARS) * rowh + 8
    out = [f'<svg class="uc rot" width="{W}" height="{H:.0f}" viewBox="0 0 {W} {H:.0f}" aria-hidden="true">']
    for i, yr in enumerate(YEARS):
        y = i * rowh + 4
        if yr == 2021:
            out.append(f'<line class="divider" x1="0" x2="{W}" y1="{y - 3:.1f}" y2="{y - 3:.1f}"/>')
        out.append(f'<text class="yr{" em" if yr == 2021 else ""}" x="0" y="{y + cell * 0.72:.1f}">{yr}</text>')
        row = cols.get(yr, [])
        for k, e in enumerate(row):
            out.append(square(e, labw + k * (cell + gap), y, cell))
        if yr == 2026 and row:
            out.append(f'<text class="dl" x="{labw + len(row) * (cell + gap) + 2:.1f}" y="{y + cell * 0.72:.1f}">so far</text>')
    out.append('</svg>')
    return "".join(out)


def data_table(entries):
    cols = columns(entries)
    rows = "".join(f'<tr><th scope="row">{y}</th><td>{len(cols.get(y, []))}</td><td>{sum(1 for e in cols.get(y, []) if e["tier"] in RULING)}</td></tr>' for y in YEARS)
    return (f'<details class="g-table"><summary>Show the numbers as a table</summary><table><thead><tr><th scope="col">Year of event</th>'
            f'<th scope="col">Entries</th><th scope="col">Resting on a ruling</th></tr></thead><tbody>{rows}</tbody></table></details>')


HEAD_SENTENCE = '<span class="kchip">15 of the 16</span> entries that rest on a ruling against Meta are events from 2021 or later'
METHOD = ("Each square is one entry, stacked in the year the event happened and drawn as its evidence label. "
          "Rulings against Meta, final or under appeal, are in blue. This counts entries in the record, not incidents; "
          "coverage before 2017 is thinner, and 2026 runs through September.")
SOURCE = 'Source: Meta on the Record entries. <a href="/data/record.csv">Download the CSV</a>'
NARROW_NOTES = ('<ol class="g-notes"><li><b>2007 to 2020:</b> 14 entries, 1 resting on a ruling.</li>'
                '<li><b>Since 2021:</b> 37 entries, 15 resting on a ruling. 2026 runs through September.</li></ol>')


def g1_figure(shot="g1", extra_cls="", head=HEAD_SENTENCE, variants=None, steps=None):
    variants = variants or [("w", 832, {}), ("m", 700, {}), ("n", 350, {"narrow": True, "cell_max": 16})]
    svgs = "".join(f'<div class="uc-{k}">{unit_chart(B.ORDER, w, **kw)}</div>' for k, w, kw in variants)
    chart = f'<div class="uc-wrap">{svgs}</div>'
    if steps:
        # the headline is pinned with the chart; the figcaption with method, notes and source closes the figure
        return (f'<figure class="g1 {extra_cls}" data-shot="{shot}" aria-labelledby="{shot}-head">'
                f'<div class="scrolly"><div class="scrolly-fig" data-state="rulings"><p class="g-head" id="{shot}-head">{head}.</p>{chart}</div>'
                f'<ol class="scrolly-steps" data-step-trigger="0.5">{steps}</ol></div>'
                f'<figcaption><p class="g-method">{METHOD}</p>{NARROW_NOTES}<p class="g-source">{SOURCE}</p>{data_table(B.ORDER)}</figcaption></figure>')
    return (f'<figure class="g1 {extra_cls}" data-shot="{shot}">'
            f'<figcaption><p class="g-head">{head}.</p><p class="g-method">{METHOD}</p></figcaption>'
            f'{chart}{NARROW_NOTES}'
            f'<p class="g-source">{SOURCE}</p>{data_table(B.ORDER)}</figure>')


def hero(variant=""):
    html = open(os.path.join(B.SRC, "home.html"), encoding="utf-8").read()
    h = html[html.index('<header class="hero"'):html.index("</header>") + 9]
    h = re.sub(r'href="#(?!top)', 'href="/#', h)
    h = h.replace('<p class="hero-meta" id="herometa">Updated September 27, 2026</p>',
                  f'<p class="hero-meta">{len(B.ENTRIES)} entries from 2007 to 2026. Updated September 27, 2026.</p>')
    if variant:
        h = h.replace('<header class="hero"', f'<header class="hero {variant}"', 1)
    return h


def symbols():
    html = open(os.path.join(B.SRC, "home.html"), encoding="utf-8").read()
    return html[html.index("<svg width=\"0\""):html.index("</svg>", html.index("<svg width=\"0\"")) + 6]


def page(slug, title, body, note):
    motion = '<script>if(!window.matchMedia("(prefers-reduced-motion: reduce)").matches)document.documentElement.classList.add("motion");</script>'
    extra = motion + '<link rel="stylesheet" href="/proto-assets/proto.css"><meta name="robots" content="noindex">'
    head = B.head(f"{title} | prototype", "Design prototype, not published.", f"/{slug}/", "/og/index.png", [], extra)
    head = head.replace(B.GTAG, "")  # keep prototypes out of analytics
    return (f'{head}\n<body class="proto {slug}">\n{symbols()}\n'
            f'<div class="proto-flag" role="note"><b>{slug.upper()}</b> {esc(note)} <a href="/v1/">V1</a> <a href="/v2/">V2</a> <a href="/v3/">V3</a></div>\n'
            f'{body}\n'
            '<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.13.0/gsap.min.js"></script>\n'
            '<script src="/proto-assets/proto.js"></script>\n</body></html>')


# ---------- V1: the argument, built step by step ----------
def v1():
    steps = [
        ("plain", "Each square is one entry in this record: 51 of them, from 2007 to 2026, stacked in the year the event happened."),
        ("recent", "Most are recent. <b>37 of the 51</b> are events from 2021 or later."),
        ("rulings", "Sixteen rest on a ruling against Meta, final or under appeal. <b>Fifteen of those</b> are events from 2021 or later. Before 2021 there is one: the 2018 “View As” breach, now under appeal."),
    ]
    step_html = "".join(f'<li class="sstep" data-step="{i + 1}" data-state="{k}"><p>{t}</p></li>' for i, (k, t) in enumerate(steps))
    body = hero() + f'''
<main id="main">
<section class="build" aria-labelledby="build-h">
  <div class="wrap">
    <h2 class="h-section" id="build-h">What the record rests on</h2>
    {g1_figure(steps=step_html)}
  </div>
</section>
</main>'''
    return page("v1", "V1: the argument, built", body, "Scroll-driven annotated build: a sticky graphic, three steps, each owning one state.")


# ---------- V2: the atlas ----------
def v2():
    panels = []
    themes = sorted(B.THEMES.items(), key=lambda kv: -sum(1 for e in B.ENTRIES if kv[0] in e["themes"]))
    shared = max(len(v) for k, _ in themes for v in columns([e for e in B.ORDER if k in e["themes"]]).values())
    for k, name in themes:
        L = [e for e in B.ORDER if k in e["themes"]]
        r = sum(1 for e in L if e["tier"] in RULING)
        svgs = "".join(f'<div class="uc-{v}">{unit_chart(L, w, narrow=(v == "n"), cell_max=cm, brackets=False, direct=False, compact=True, ticks=[2007, 2021, 2026], stack=shared)}</div>'
                       for v, w, cm in (("w", 352, 13), ("m", 352, 13), ("n", 350, 13)))
        panels.append(f'<article class="panel"><h3><a href="/topics/{k}/">{esc(name)}</a></h3>'
                      f'<p class="panel-n"><b>{len(L)}</b> {"entry" if len(L) == 1 else "entries"} · <b>{r}</b> {"ruling" if r == 1 else "rulings"}</p>{svgs}</article>')
    body = hero("hero-compact") + f'''
<main id="main">
<section class="atlas" aria-labelledby="atlas-h">
  <div class="wrap">
    <h2 class="h-section" id="atlas-h">The record at a glance</h2>
    {g1_figure()}
    <figure class="atlas-grid-fig" data-shot="atlas">
      <figcaption><p class="g-head"><span class="kchip">12 of the 16</span> entries resting on a ruling involve privacy; none of the 7 entries on violence abroad has reached one.</p>
      <p class="g-method">The same chart for each topic, on the same scale. An entry can belong to more than one topic, so panels add up to more than 51.</p></figcaption>
      <div class="atlas-grid">{"".join(panels)}</div>
      <p class="g-source">{SOURCE}</p>
    </figure>
  </div>
</section>
</main>'''
    return page("v2", "V2: the atlas", body, "Dense small multiples that reward scanning: the whole record, then every topic on one scale.")


# ---------- V3: the monument ----------
def v3():
    variants = [("w", 1136, {"cell_max": 40}), ("m", 768, {"cell_max": 30})]
    svgs = "".join(f'<div class="uc-{k}">{unit_chart(B.ORDER, w, **kw)}</div>' for k, w, kw in variants)
    svgs += f'<div class="uc-n">{rotated_chart(B.ORDER, 350)}</div>'
    body = hero() + f'''
<main id="main">
<section class="monument dark-band" aria-labelledby="mon-h">
  <div class="wrap">
    <figure class="g1 mono" data-shot="g1">
      <figcaption>
        <h2 class="mon-num" id="mon-h"><span class="mon-a">15</span><span class="mon-of">of</span><span class="mon-b">16</span></h2>
        <p class="g-head mon-head">entries that rest on a ruling against Meta are events from 2021 or later. Before 2021, there is one.</p>
        <p class="g-method">{METHOD}</p>
      </figcaption>
      <div class="uc-wrap">{svgs}</div>
      <p class="g-source">{SOURCE}</p>
      {data_table(B.ORDER)}
    </figure>
  </div>
</section>
</main>'''
    return page("v3", "V3: the monument", body, "One monumental graphic in a strong typographic frame.")


def main():
    for slug, fn in (("v1", v1), ("v2", v2), ("v3", v3)):
        B.write(f"/{slug}/", fn())
    dst = os.path.join(B.DIST, "proto-assets")
    os.makedirs(dst, exist_ok=True)
    for f in ("proto.css", "proto.js"):
        shutil.copy(os.path.join(HERE, f), os.path.join(dst, f))
    print("Built /v1/, /v2/, /v3/")


if __name__ == "__main__":
    main()
