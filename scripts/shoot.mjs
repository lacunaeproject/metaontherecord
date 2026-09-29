#!/usr/bin/env node
/*
  Screenshot harness for design review.

    npm run serve                      # in another terminal: serves docs/ on :8765
    npm run shoot -- <label> [url] [--paths=/,/record/2018-cambridge-analytica/]

  Writes design/shots/<label>/<pass>/ for three passes: motion (default), reduced-motion and dark.
  For each page and width (1440, 834, 390) it captures:
    <page>-<w>-full.png           the whole page
    <page>-<w>-full-NN.png        the same page in readable slices
    <page>-<w>-shot-<name>.png    every [data-shot="name"] element on its own
    <page>-<w>-step-<n>.png       the viewport with each [data-step] at its trigger line
*/
import { chromium } from "playwright";
import { mkdir, rm } from "node:fs/promises";
import path from "node:path";

const args = process.argv.slice(2);
const flags = Object.fromEntries(args.filter(a => a.startsWith("--")).map(a => a.slice(2).split("=")));
const [label, baseArg] = args.filter(a => !a.startsWith("--"));
if (!label) {
  console.error("Usage: npm run shoot -- <label> [url] [--paths=/,/topics/kids/]");
  process.exit(1);
}
const base = (baseArg || "http://localhost:8765").replace(/\/$/, "");
const paths = (flags.paths || "/").split(",");
const outRoot = path.join("design", "shots", label);

const WIDTHS = [
  { w: 1440, h: 900, mobile: false },
  { w: 834, h: 1112, mobile: true },
  { w: 390, h: 844, mobile: true },
];
const SLICE = { 1440: 1800, 834: 2200, 390: 2000 };
const STEP_TRIGGER = 0.6; // matches the timeline fill line in src/app.js
const HERO_INTRO_MS = 3200; // the motto animation runs about 2.8s

const written = [];
const pageName = p => (p === "/" ? "home" : p.replace(/^\/|\/$/g, "").replace(/[/.]+/g, "-"));

async function settle(page, maxMs = 2500) {
  await page.evaluate(async maxMs => {
    const t0 = performance.now();
    while (performance.now() - t0 < maxMs) {
      const running = document.getAnimations().filter(a => a.playState === "running" && a.effect?.getTiming().iterations !== Infinity);
      if (!running.length) break;
      await new Promise(r => setTimeout(r, 100));
    }
    await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
  }, maxMs);
}

async function walk(page) {
  // scroll the whole page once so scroll-triggered reveals and lazy images resolve
  await page.evaluate(async () => {
    const step = Math.round(innerHeight * 0.6);
    for (let y = 0; y < document.documentElement.scrollHeight; y += step) {
      scrollTo(0, y);
      await new Promise(r => setTimeout(r, 90));
    }
    scrollTo(0, 0);
  });
  await page.waitForLoadState("networkidle").catch(() => {});
  await settle(page);
}

async function shootPage(browser, pass, route, { w, h, mobile }) {
  const context = await browser.newContext({
    viewport: { width: w, height: h },
    deviceScaleFactor: 1,
    isMobile: mobile,
    hasTouch: mobile,
    reducedMotion: pass === "reduced-motion" ? "reduce" : "no-preference",
    colorScheme: pass === "dark" ? "dark" : "light",
  });
  // keep test captures out of the site's analytics
  await context.route(/google-analytics\.com|googletagmanager\.com/, r => r.abort());
  const page = await context.newPage();
  const errors = [];
  page.on("pageerror", e => errors.push(e.message));

  await page.goto(base + route, { waitUntil: "networkidle" });
  await page.evaluate(() => document.fonts.ready);
  if (pass !== "reduced-motion") await page.waitForTimeout(HERO_INTRO_MS);
  await walk(page);

  const dir = path.join(outRoot, pass);
  const stem = `${pageName(route)}-${w}`;
  const save = async (name, opts, target = page) => {
    const file = path.join(dir, `${stem}-${name}.png`);
    await target.screenshot({ path: file, ...opts });
    written.push(file);
  };

  await save("full", { fullPage: true });
  const height = await page.evaluate(() => document.documentElement.scrollHeight);
  const slice = SLICE[w];
  for (let y = 0, i = 1; y < height; y += slice, i++) {
    await save(`full-${String(i).padStart(2, "0")}`, { fullPage: true, clip: { x: 0, y, width: w, height: Math.min(slice, height - y) } });
  }

  // fixed bars would be stamped over any element taller than the viewport
  const hideChrome = await page.addStyleTag({ content: ".topnav,.fbar{visibility:hidden!important}" });
  for (const el of await page.$$("[data-shot]")) {
    const name = await el.getAttribute("data-shot");
    await el.scrollIntoViewIfNeeded();
    await settle(page, 1500);
    await save(`shot-${name}`, {}, el);
  }
  await hideChrome.evaluate(node => node.remove());

  const steps = await page.$$("[data-step]");
  for (const [i, el] of steps.entries()) {
    const id = (await el.getAttribute("data-step")) || i + 1;
    await el.evaluate((node, fallback) => {
      // a page can declare its own trigger line with data-step-trigger on a step or an ancestor
      const trigger = parseFloat(node.closest("[data-step-trigger]")?.dataset.stepTrigger ?? fallback);
      const top = node.getBoundingClientRect().top + scrollY;
      scrollTo(0, top - innerHeight * trigger + 24);
    }, STEP_TRIGGER);
    await page.waitForTimeout(150);
    await settle(page, 1500);
    await save(`step-${id}`, {});
  }

  if (errors.length) console.warn(`  ! ${pass} ${route} @${w}: ${errors.join(" | ")}`);
  await context.close();
}

async function main() {
  try {
    const res = await fetch(base + paths[0]);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
  } catch (e) {
    console.error(`Can't reach ${base}${paths[0]} (${e.message}). Start the site with: npm run serve`);
    process.exit(1);
  }

  const browser = await chromium.launch();
  const probe = await browser.newPage();
  await probe.goto(base + paths[0], { waitUntil: "networkidle" });
  const hasDark = await probe.evaluate(() => [...document.styleSheets].some(s => {
    try { return [...s.cssRules].some(r => r.media && /prefers-color-scheme:\s*dark/.test(r.media.mediaText)); } catch { return false; }
  }));
  await probe.close();

  const passes = ["motion", "reduced-motion", ...(hasDark ? ["dark"] : [])];
  await rm(outRoot, { recursive: true, force: true });
  for (const pass of passes) {
    await mkdir(path.join(outRoot, pass), { recursive: true });
    for (const route of paths) for (const size of WIDTHS) {
      process.stdout.write(`${pass} ${route} @${size.w}\n`);
      await shootPage(browser, pass, route, size);
    }
  }
  await browser.close();

  console.log(`\nWrote ${written.length} files to ${outRoot}/`);
  for (const f of written) console.log("  " + f);
}

main().catch(e => { console.error(e); process.exit(1); });
