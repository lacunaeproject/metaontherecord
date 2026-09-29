"use strict";
(() => {
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));

/* V1: each step owns one state of the sticky chart. Without JS, or before any step is reached, the chart shows its final state. */
const fig = $(".scrolly-fig");
if (fig && "IntersectionObserver" in window) {
  const steps = $$(".scrolly-steps .sstep");
  const setState = s => { fig.dataset.state = s; steps.forEach(st => st.classList.toggle("on", st.dataset.state === s)); };
  const io = new IntersectionObserver(ens => ens.forEach(en => { if (en.isIntersecting) setState(en.target.dataset.state); }),
    { rootMargin: "-50% 0px -50% 0px" });
  steps.forEach(st => io.observe(st));
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
