#!/usr/bin/env python3
"""Render 1200x630 share images for every page. Run after build.py (needs Playwright + Chromium)."""
import asyncio, json, os, sys
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "docs", "og")
CHROME = os.environ.get("CHROME_PATH")

TEMPLATE = r"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,300..900&family=Newsreader:opsz,wght@6..72,400..600&display=block" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0}
body{width:1200px;height:630px;overflow:hidden;background:#1F2FC8;color:#fff;font-family:Archivo,Arial,sans-serif}
.card{position:relative;width:1200px;height:630px;padding:56px 64px;display:flex;flex-direction:column;isolation:isolate}
.card::before{content:"";position:absolute;inset:0;z-index:-1;opacity:.13;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 .55 0'/%3E%3C/filter%3E%3Crect width='160' height='160' filter='url(%23n)'/%3E%3C/svg%3E")}
.brand{display:flex;align-items:center;gap:12px;font-weight:850;font-variation-settings:"wdth" 118;font-size:30px;letter-spacing:-.01em}
.brand svg{width:30px;height:30px}
.meta{margin-left:auto;font-weight:550;font-size:24px;opacity:.8}
.title{margin-top:auto;font-weight:850;font-variation-settings:"wdth" 108;line-height:1.02;letter-spacing:-.02em;max-width:1040px}
.foot{display:flex;align-items:flex-end;gap:40px;margin-top:40px;padding-top:26px;border-top:3px solid #fff}
.fig{font-weight:900;font-variation-settings:"wdth" 70;font-size:72px;line-height:.9;letter-spacing:-.02em}
.cap{font-size:22px;opacity:.82;max-width:520px;line-height:1.3;padding-bottom:6px}
.tier{margin-left:auto;display:flex;align-items:center;gap:12px;font-size:26px;font-weight:650;padding-bottom:6px;white-space:nowrap}
.tier svg{width:26px;height:26px}
.quake{position:relative;margin-top:auto}
.motto{font-weight:850;line-height:.86;letter-spacing:-.035em}
.m1{display:block;white-space:nowrap;font-variation-settings:"wdth" 125;font-size:200px}
.m2{display:block;white-space:nowrap;font-variation-settings:"wdth" 62;font-weight:900;font-size:228px}
.s1{clip-path:polygon(0 0,100% 0,100% 64%,88% 71%,74% 61%,61% 78%,47% 67%,34% 82%,20% 70%,8% 79%,0 73%)}
.s2{position:absolute;inset:0;clip-path:polygon(0 73%,8% 79%,20% 70%,34% 82%,47% 67%,61% 78%,74% 61%,88% 71%,100% 64%,100% 100%,0 100%);transform:translate(16px,9px) rotate(1.1deg);transform-origin:12% 70%}
.tag{font-size:28px;font-weight:550;opacity:.9;margin-top:34px}
</style></head><body><div class="card" id="card"></div>
<script>
const MARK='<svg viewBox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd" d="M3 3h18v18H3z M7 7.5h10v2H7z M7 11.5h10v2H7z M7 15.5h6v2H7z"/></svg>';
const G={ruled:'<rect x="1.5" y="1.5" width="13" height="13" fill="currentColor"/>',appeal:'<path d="M1.5 1.5h8.5l4.5 4.5v8.5h-13z" fill="currentColor"/>',settled:'<rect x="2.5" y="2.5" width="11" height="11" fill="none" stroke="currentColor" stroke-width="2"/><rect x="5.5" y="5.5" width="5" height="5" fill="currentColor"/>',admitted:'<rect x="2.5" y="2.5" width="11" height="11" fill="none" stroke="currentColor" stroke-width="2"/><rect x="2.5" y="2.5" width="5.5" height="11" fill="currentColor"/>',reported:'<rect x="2.5" y="2.5" width="11" height="11" fill="none" stroke="currentColor" stroke-width="2"/>',alleged:'<rect x="2.5" y="2.5" width="11" height="11" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="2.4 2"/>',dismissed:'<rect x="2.5" y="2.5" width="11" height="11" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M3 13 13 3" stroke="currentColor" stroke-width="1.6"/>'};
const esc=s=>String(s||"").replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c]));
window.render=d=>{
  const c=document.getElementById('card');
  const brand=`<div class="brand">${MARK}Meta on the Record${d.meta?`<span class="meta">${esc(d.meta)}</span>`:''}</div>`;
  if(d.kind==='index'){c.innerHTML=brand+`<div class="quake"><div class="s1"><p class="motto"><span class="m1">Move fast</span><span class="m2">and break things.</span></p></div><div class="s2"><p class="motto"><span class="m1">Move fast</span><span class="m2">and break things.</span></p></div></div><p class="tag">Meta’s rulings, findings and reported events, 2007 to 2026, labeled by strength of evidence.</p>`;
    const max=1072;
    c.querySelectorAll('.m1,.m2').forEach(el=>{let s=parseFloat(getComputedStyle(el).fontSize);el.style.display='inline-block';while(el.scrollWidth>max&&s>60){s-=4;el.style.fontSize=s+'px';}el.style.display='block';});
    return;}
  const n=d.title.length, size=n<34?92:n<52?78:n<70?66:56;
  const tier=d.tier?`<span class="tier"><svg viewBox="0 0 16 16">${G[d.tier]}</svg>${esc(d.tierLabel)}</span>`:'';
  const fig=d.fig?`<span class="fig">${esc(d.fig)}</span><span class="cap">${esc(d.cap)}</span>`:`<span class="cap">${esc(d.cap||'')}</span>`;
  c.innerHTML=brand+`<h1 class="title" style="font-size:${size}px">${esc(d.title)}</h1><div class="foot">${fig}${tier}</div>`;
};
</script></body></html>"""

async def main():
    m = json.load(open(os.path.join(HERE, "og-manifest.json"), encoding="utf-8"))
    os.makedirs(OUT, exist_ok=True)
    jobs = [("index", {"kind": "index"})]
    jobs += [(e["slug"], {"title": e["title"], "meta": e["date"], "fig": e["fig"], "cap": e["cap"], "tier": e["tier"], "tierLabel": e["tierLabel"]}) for e in m["entries"]]
    jobs += [(f"topic-{t['key']}", {"title": t["title"], "meta": "Topic", "cap": f"{t['count']} entries in the record, each labeled by strength of evidence"}) for t in m["topics"]]
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CHROME) if CHROME else await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1200, "height": 630})
        await pg.set_content(TEMPLATE)
        await pg.evaluate("document.fonts.ready")
        await pg.wait_for_timeout(2500)
        for name, data in jobs:
            await pg.evaluate("d => window.render(d)", data)
            await pg.evaluate("document.fonts.ready")
            await pg.screenshot(path=os.path.join(OUT, f"{name}.png"), type="png")
        await b.close()
    print(f"Rendered {len(jobs)} share images into {OUT}")

asyncio.run(main())
