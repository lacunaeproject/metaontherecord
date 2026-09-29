#!/usr/bin/env python3
"""Builds docs/preview/: the current home page with design/preview/preview.css layered on top.
Run after build.py. docs/preview/ is gitignored, so it is never published."""
import os, re, shutil
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
src = open(os.path.join(ROOT, "docs", "index.html"), encoding="utf-8").read()
src = re.sub(r"<!-- Google tag.*?</script>\s*<script>.*?</script>", "", src, flags=re.S)
src = src.replace('<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">')
src = src.replace('<link rel="stylesheet" href="/assets/site.css">',
                  '<link rel="stylesheet" href="/assets/site.css">\n<link rel="stylesheet" href="/preview/preview.css">')
# people: each story becomes one card; the camp photo moves inside the Rohingya card, and the evidence label joins the name
m = re.search(r'(\s*<figure class="photo story-photo">.*?</figure>)(\s*<article class="story">\s*<h3 class="story-name">The Rohingya)', src, re.S)
if m:
    src = src.replace(m.group(0), m.group(2), 1)
    photo = m.group(1).strip()
    i = src.index('<h3 class="story-name">The Rohingya'); j = src.index('</article>', i)
    src = src[:j] + photo + src[j:]
def move_tier(mm):
    art = mm.group(0)
    t = re.search(r'\s*(<span class="tierline"[^>]*>.*?</span></span>|<span class="tierline"[^>]*>.*?</span>)(?=\s*</div>)', art, re.S)
    if not t: return art
    art = art.replace(t.group(0), "", 1)
    return re.sub(r'(<span class="story-where">.*?</span>)(</h3>)', lambda k: k.group(1) + k.group(2) + t.group(1), art, count=1, flags=re.S)
src = re.sub(r'<article class="story">.*?</article>', move_tier, src, flags=re.S)
out = os.path.join(ROOT, "docs", "preview"); os.makedirs(out, exist_ok=True)
open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(src)
shutil.copy(os.path.join(ROOT, "design", "preview", "preview.css"), os.path.join(out, "preview.css"))
print("Built /preview/")
