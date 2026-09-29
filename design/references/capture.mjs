// Captures each reference piece for study: screenshots while scrolling, plus measured type, grid and color.
//   node design/references/capture.mjs [slug ...]
// Screenshots are third-party work and stay out of git (see .gitignore); measurements go in <slug>/measure.json.
import { chromium } from "playwright";
import { mkdir, readFile, writeFile } from "node:fs/promises";
import path from "node:path";

const here = path.dirname(new URL(import.meta.url).pathname);
const pieces = JSON.parse(await readFile(path.join(here, "pieces.json"), "utf8"));
const only = process.argv.slice(2);
const SIZES = [{ w: 1440, h: 900, mobile: false }, { w: 390, h: 844, mobile: true }];
const MAX_FRAMES = process.env.FRAMES ? { 1440: +process.env.FRAMES, 390: +process.env.FRAMES } : { 1440: 24, 390: 30 };
const MODE = { "visualrambling-dithering": "click", "straitstimes-indonesia-food": "wheel" };

function measure() {
  const vis = el => { const r = el.getBoundingClientRect(), s = getComputedStyle(el); return r.width > 0 && r.height > 0 && s.visibility !== "hidden" && s.display !== "none"; };
  const style = el => { const s = getComputedStyle(el); return { family: s.fontFamily.slice(0, 80), size: parseFloat(s.fontSize), weight: s.fontWeight, lineHeight: s.lineHeight, color: s.color, numerals: s.fontVariantNumeric, width: Math.round(el.getBoundingClientRect().width) }; };
  const h1 = [...document.querySelectorAll("h1")].find(vis);
  const paras = [...document.querySelectorAll("p")].filter(p => vis(p) && p.textContent.trim().length > 180);
  const body = paras[0];
  let cpl = null;
  if (body) {
    // characters per line: count characters in the first rendered line
    const range = document.createRange(), text = body.firstChild;
    if (text && text.nodeType === 3) {
      let top = null, n = 0;
      for (let i = 0; i < Math.min(text.length, 200); i++) {
        range.setStart(text, i); range.setEnd(text, i + 1);
        const t = range.getBoundingClientRect().top;
        if (top === null) top = t; else if (Math.abs(t - top) > 3) break;
        n++;
      }
      cpl = n;
    }
  }
  const svgText = [...document.querySelectorAll("svg text")].filter(vis).slice(0, 40);
  const fills = new Map();
  document.querySelectorAll("svg *").forEach(el => {
    if (!vis(el)) return;
    const s = getComputedStyle(el);
    for (const c of [s.fill, s.stroke]) if (c && c !== "none" && !c.startsWith("url")) fills.set(c, (fills.get(c) || 0) + 1);
  });
  const figs = [...document.querySelectorAll("figure, svg, canvas, video")].filter(el => vis(el) && el.getBoundingClientRect().width > 200).slice(0, 12).map(el => ({ tag: el.tagName.toLowerCase(), width: Math.round(el.getBoundingClientRect().width) }));
  const text = document.body.innerText;
  return {
    title: document.title,
    bodyBg: getComputedStyle(document.body).backgroundColor,
    h1: h1 ? { text: h1.textContent.trim().slice(0, 160), ...style(h1) } : null,
    body: body ? { sample: body.textContent.trim().slice(0, 120), ...style(body), charsPerLine: cpl } : null,
    chartLabels: svgText.length ? { count: document.querySelectorAll("svg text").length, samples: svgText.slice(0, 6).map(t => ({ text: t.textContent.trim().slice(0, 40), ...style(t) })) } : null,
    svgColors: [...fills.entries()].sort((a, b) => b[1] - a[1]).slice(0, 14),
    graphics: figs,
    counts: { svg: document.querySelectorAll("svg").length, canvas: document.querySelectorAll("canvas").length, video: document.querySelectorAll("video").length, img: document.querySelectorAll("img").length },
    blockedHint: /subscribe to continue|create a free account|access denied|are you a robot|verify you are human|captcha|enable javascript/i.test(text) ? text.match(/.{0,80}(subscribe to continue|create a free account|access denied|are you a robot|verify you are human|captcha|enable javascript).{0,80}/i)?.[0] : null,
    textLength: text.length,
    pageHeight: document.documentElement.scrollHeight,
  };
}

const browser = await chromium.launch();
const summary = [];
for (const [slug, url] of pieces) {
  if (only.length && !only.includes(slug)) continue;
  const dir = path.join(here, slug);
  await mkdir(dir, { recursive: true });
  const result = { slug, url, sizes: {} };
  for (const { w, h, mobile } of SIZES) {
    const ctx = await browser.newContext({ viewport: { width: w, height: h }, isMobile: mobile, hasTouch: mobile, userAgent: mobile
      ? "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1"
      : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36" });
    const page = await ctx.newPage();
    let status = null;
    try {
      const res = await page.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 });
      status = res?.status() ?? null;
      await page.waitForLoadState("networkidle", { timeout: 15000 }).catch(() => {});
      await page.evaluate(() => document.fonts.ready);
      await page.waitForTimeout(2500);
      // decline optional cookies so consent banners don't cover the frames (never accepts)
      for (const frame of page.frames()) {
        const btn = frame.getByRole("button", { name: /^(reject all|reject optional cookies|reject|i do not accept|necessary only|continue without accepting)$/i }).first();
        if (await btn.isVisible().catch(() => false)) { await btn.click().catch(() => {}); await page.waitForTimeout(1200); break; }
      }
      // banners with no reject option (e.g. US notices) only offer a close button; closing accepts nothing
      for (const frame of page.frames()) {
        const close = frame.getByRole("button", { name: /^(close|closer|dismiss|close banner|close this notice)$/i }).first();
        if (await close.isVisible().catch(() => false)) { await close.click().catch(() => {}); await page.waitForTimeout(1200); break; }
      }
      const frames = [];
      for (let i = 0; i < MAX_FRAMES[w]; i++) {
        const file = path.join(dir, `${w}-${String(i + 1).padStart(2, "0")}.png`);
        await page.screenshot({ path: file });
        frames.push(path.basename(file));
        if (MODE[slug] === "click") {
          // click-to-advance story: tap the right side of the screen
          await page.mouse.click(Math.round(w * 0.85), Math.round(h * 0.5));
        } else if (MODE[slug] === "wheel") {
          // the page scrolls inside its own container, so send real wheel input
          await page.mouse.move(Math.round(w / 2), Math.round(h / 2));
          await page.mouse.wheel(0, Math.round(h * 0.85));
        } else {
          const done = await page.evaluate(() => { const before = scrollY; scrollBy(0, Math.round(innerHeight * 0.85)); return scrollY === before; });
          if (done) break;
        }
        await page.waitForTimeout(900);
      }
      await page.evaluate(() => scrollTo(0, 0));
      await page.waitForTimeout(800);
      result.sizes[w] = { status, frames: frames.length, ...(await page.evaluate(measure)) };
    } catch (e) {
      result.sizes[w] = { status, error: e.message.split("\n")[0] };
    }
    await ctx.close();
  }
  await writeFile(path.join(dir, "measure.json"), JSON.stringify(result, null, 2));
  const d = result.sizes[1440] || {};
  summary.push(`${slug}: status ${d.status} frames ${d.frames ?? 0} text ${d.textLength ?? 0} ${d.error ? "ERROR " + d.error : ""}${d.blockedHint ? " BLOCKED? " + d.blockedHint.replace(/\s+/g, " ") : ""}`);
  console.log(summary.at(-1));
}
await browser.close();
