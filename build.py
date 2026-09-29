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
    body = body.replace('<div class="ledger" id="ledger"></div>', f'<div class="ledger" id="ledger">{ledger_html()}</div>')
    body = body.replace('<ol class="credit-list" id="creditlist"></ol>', f'<ol class="credit-list" id="creditlist">{credits_html()}</ol>')
    tierdefs = "".join(f'<div><dt>{glyph(k)}{esc(t["label"])}</dt><dd>{esc(t["def"])}</dd></div>' for k, t in TIERS.items())
    tierdefs += f'<div><dt>{glyph("credit")}Credit</dt><dd>Something Meta did well, listed with the context it needs.</dd></div>'
    body = body.replace('<dl class="tiers" id="tierdefs"></dl>', f'<dl class="tiers" id="tierdefs">{tierdefs}</dl>')
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
        fact = f'<aside class="a-side"><div class="fact"><span class="fact-num">{esc(e["fig"])}</span><span class="fact-cap">{esc(e.get("cap",""))}</span></div></aside>' if e.get("fig") else '<aside class="a-side"></aside>'
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
        tally = ", ".join(f"{n} {TIERS[t]['label'].lower()}" for t, n in tallies.items())
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
<body class="page">{masthead()}<main id="main" class="article wrap"><h1 class="a-title">This page doesn’t exist.</h1><p class="a-lede">The link may be old or mistyped. <a href="/#record">Go to the full record</a> or search it from there.</p></main>{footer()}</body></html>''')

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
