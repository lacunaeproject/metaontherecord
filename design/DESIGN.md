# Meta on the Record: design spec

Status: **approved by the editor on September 29, 2026, and binding for Phases 3 and 4.** Decisions 1–4 and 7 are accepted as proposed. Decision 6 is accepted but blocked on two sourced values (§9). Decision 5 is still open, so G3 is not built until it is chosen.

Sources for this spec: `design/references/TEARDOWNS.md` (ten measured teardowns and the five-pattern synthesis), `design/critiques/baseline.md` (the critic's review of the current site, verified), and the entry data in `src/data.json`. Every number below was computed from those files or measured, not estimated from memory.

---

## 0. Decisions for the editor

1. **Page ground.** The brief bans cream or off-white page grounds. The current ground is `#F1F3F9`, a cool blue-white. It is not cream, but it is off-white. **Proposed:** pure white `#FFFFFF` for reading surfaces, keeping the cobalt hero and the deep navy people/footer bands. Alternative: keep `#F1F3F9` and record it as an approved exception.
2. **Hero motion.** The brief bans motion that doesn't encode a change in the data. The hero's motto build and crack don't encode data. You like the hero. **Proposed:** keep it as the one declared exception, limited to the hero, with the existing reduced-motion path (static cracked motto).
3. **Decorative motion added on September 29.** The scroll reveals (headings rising word by word, blocks fading in), the timeline's scroll fill and the reading-progress bar encode no data. **Proposed:** remove all three. The baseline critique also found that the timeline fill never reaches its end state with reduced motion and borrows the evidence glyphs' filled-means-stronger vocabulary.
4. **Cobalt's meaning.** Cobalt currently means hero ground, credits ground, data marks, links, dates and figures. **Proposed:** cobalt stays the hero's brand field, and inside the page it means exactly one thing in data: *the marks the graphic's headline names* (§5). Links, dates and figures move to ink. The "What Meta got right" section moves off the cobalt field to the deep navy band, so credits never share the penalty color.
5. **Timeline thesis.** The site's stance is "draw your own conclusion". A graphic still has to prove one sentence. Two options for the teen-safety thread (§1, G3); pick one.
6. **Currency and revenue source for the money graphic.** The €4.0B from European regulators is currently summed as dollars. **Proposed:** convert at the ECB's 2025 average EUR/USD reference rate, stated in the method line. Cite Meta's FY2025 Form 10-K for the $201B revenue rather than PBS NewsHour. Both need a sourced value added to the data before G2 ships.
7. **D3 at build time.** The brief says to use D3 for scales and joins. The site is built by Python. **Proposed:** render every graphic's default state as static SVG at build time in `build.py` (so it works with no JavaScript and causes no layout shift), and use D3 v7 in the browser only for interactive states (filter transitions, highlight joins). If you'd rather have D3 do the initial render, the build gains a Node step.

---

## 1. Graphics: thesis and encoding

Each graphic gets one sentence it proves, the reader question it answers, an encoding chosen by the relationship in the data (FT Visual Vocabulary category), and at least two rejected alternatives. A graphic without a thesis doesn't get built. The story must be complete with every graphic in its default, non-interactive state.

### G1. What the record rests on (replaces the entries-per-year strip in "The record")

- **Thesis.** "Most of this record is recent, and so is nearly every ruling in it: 37 of the 51 entries, and 15 of the 16 that rest on a ruling against Meta, are events from 2021 or later."
- **Reader question.** Is this a list of old scandals, and how much of it is actually proven?
- **Data** (computed from `src/data.json`, by year of the event):

  | Years | Entries | Resting on a ruling (ruled or under appeal) |
  |---|---|---|
  | 2007–2020 | 14 | 1 (the 2018 "View As" breach, under appeal) |
  | 2021–2026 | 37 | 15 |

  Per-year totals run from 0 (2008, 2010, 2011, 2013, 2015, 2016) to 9 (2025); 2026 has 8 through September.
- **Relationship.** Change over time plus part-to-whole: a count per year, split by evidence strength.
- **Encoding.** A unit chart. Each of the 51 entries is one square, stacked in its year's column on a true year axis from 2007 to 2026, with empty years kept as gaps. Each square is drawn *as its evidence glyph* (filled for ruled, cut corner for under appeal, and so on), so strength is encoded by shape and fill pattern, not color alone. The 16 ruling squares take the accent; the rest are ink glyphs. Within each column, squares stack strongest evidence at the bottom. 2026 gets a "through September" note on its column.
  - Headline chip: "**15 of the 16**" on an accent chip, matching the accent squares.
  - Direct labels: the 2025 peak ("9") and the 2026 partial column ("8 so far"). No legend box: the evidence glyphs are already defined in "How we know", and the headline names the accent set.
  - Method line: "Counts entries in this record by the year of the event, not incidents. Coverage before 2017 is thinner. 2026 through September."
  - Source line: "Source: Meta on the Record entries (CSV)" linking to the download.
  - Filters: when a topic or evidence filter is active, matching squares stay at full strength and others drop to the context grey outline. This replaces today's second bar layer.
- **Rejected.**
  1. *Bars per year (the current strip).* Shows volume but hides evidence strength, and its rising shape reads as a rate of wrongdoing (baseline critique finding 2).
  2. *Stacked bars colored by the seven evidence labels.* Needs seven hues, which breaks the one-accent rule and fails color-vision checks at seven categories.
  3. *A line of entries per year.* 51 items across 20 years is too sparse for a line, and a line implies a continuous rate.

### G2. Penalties against revenue (replaces the $1B square grid in "The money")

- **Thesis.** "Meta took in enough revenue to cover every fine and settlement in this record since 2009 by mid-February 2025."
  - Arithmetic: $201B of 2025 revenue is about $0.55B a day. The tally sums to about $25.5B with euros counted as dollars (46 days, February 15), or about $26.0B with euros converted at roughly 1.13 (47 days, February 16). "Mid-February" is true under both; the exact date ships only after Decision 6.
- **Reader question.** Are these penalties large for Meta?
- **Relationship.** Magnitude, framed as time: a sum of penalties expressed in days of revenue.
- **Encoding.** A 2025 calendar: 365 day cells in 12 month rows (Jan–Dec, 28–31 cells each), separated by 2px gaps. Revenue days are context-grey cells. The penalty days fill from January 1 in the accent, **segmented by payer** in tally order, with a 2px gap between segments:
  - State attorneys general, 22 days
  - FTC, 9 days
  - European regulators, about 7–8 days
  - Texas facial recognition, 3 days
  - Texas child safety, 2 days
  - Cambridge Analytica, 1 day
  - Illinois, 1 day
  - Other, 1 day

  Rounding is cumulative, so the segments always sum to the total. The State AG segment is hatched and labeled "paid over ten years", because it is committed, not paid. The three largest segments are labeled directly with leader lines. The tally list stays beside the calendar as the table view, and the headline's "mid-February" sits on an accent chip.
  - Method line: "One cell is one day of Meta's 2025 revenue ($201B ÷ 365). Penalties are counted at announced value; euros converted at [rate]."
  - Source line: "Sources: Meta Form 10-K (FY2025); penalty sources linked in each entry."
  - The existing note "The total is a minimum…" stays.
- **Rejected.**
  1. *The current $1B square grid.* It compares 17 years of penalties with one year of revenue without saying so, and its breakdown lives only on hover (baseline critique findings 1 and 4).
  2. *Two bars, $25B against $201B.* Accurate but inert: a 1:8 bar ratio doesn't give a reader a unit they feel, and it hides the composition.
  3. *Cumulative penalties against cumulative revenue, 2009–2025.* The most like-for-like comparison, but it needs a sourced annual revenue series that isn't in the data yet. Revisit if one is added.
  4. *Pie or donut.* Banned for more than three slices, and it hides the time framing.

### G3. One thread through the record (the teen-safety timeline)

- **Thesis. Decision 5: pick one.**
  - **A (claim-bearing):** "Twice, Meta changed course on teenagers after journalists obtained its internal documents." Both halves are already stated in the entries: Instagram Kids was paused in September 2021 after the research was published, and the chatbot passages were removed after Reuters asked about them.
  - **B (neutral):** "Seven years separate Meta's internal research on teenagers and its $12.1 billion settlement with the states."
- **Reader question.** What happened, in what order, and how far apart?
- **Relationship.** Change over time: five dated events with uneven gaps.
- **Encoding.** A vertical timeline on a true time scale (2019 to 2026). Vertical spacing is proportional to elapsed time, with a floor so short gaps stay readable. The long quiet stretch between September 2021 and August 2025 is labeled on the rail ("3 years, 11 months"). Each node is that entry's own evidence glyph, not a generic dot, so the node shows how well established the event is.
  - Under option A, the two "changed course" events take the accent on their node and on the phrase naming the change, and the headline names them on an accent chip.
  - Each step shows its key sentence as a highlighted quotation from the reporting or document, set in the text (the Robinson steal, done typographically; no facsimile images of third-party documents).
  - The Haugen photo moves out of the rail into a figure-width breakout beside step 3 at 1440, and stacks under step 3 at 390.
  - Every step keeps "Read the entry" and its source.
- **Rejected.**
  1. *Evenly spaced list (current).* Hides the nearly four-year gap, which is part of the story (baseline critique finding 7).
  2. *Click or scroll stepper with a fixed stage (Dithering pattern).* Hides four of five events at any moment. Kept only if it enhances a plain ordered list, and even then it adds interaction without new information.
  3. *Converging curves into one endpoint (Reuters poll chart).* Implies the events cause or lead to the endpoint, which the site can't prove.
  4. *Horizontal timeline.* Five multi-sentence steps don't fit a horizontal row at 390px without truncation.

### G4. The evidence labels ("How we know")

- **Thesis.** "Fewer than a third of the entries rest on a ruling against Meta; the largest single group is reported events." (16 of 51 ruled or under appeal; reported is 12, the largest single label.)
- **Relationship.** Ranking and part-to-whole across seven labels.
- **Encoding.** The existing definitions list, each label with its glyph, its definition and its count as a direct label ("11 entries"), in the site's evidence order (strongest to weakest), plus a single 51-unit row of glyphs grouped by label above the list, matching G1's squares. No accent here except the ruling groups, which match G1.
- **Rejected.** *A bar chart of counts* (duplicates the numbers the list already prints). *A donut* (banned).

### Not graphics

- **Hero.** Typographic. No data claim; no chart. See Decision 2.
- **The record ledger.** A table, not a chart. Entries keep date, title, figure and evidence label visible by default. At 390px the figure moves inline after the evidence label (baseline critique finding 11) instead of being dropped.
- **The people.** Four stories and two public-domain photos. No data graphic.
- **What Meta got right.** A list. The large figures stay as typographic figures, not charts.

---

## 2. Grid

- **Container.** Max 78rem (1248px), side gutter clamp(1.25rem, 4vw, 3.5rem). The content box is 1136px at 1440.
- **Alignment.** Left-aligned editorial column, not centered. Graphics break out to the right; notes and source lines snap back to the text column's left edge (pattern 4).
- **Named widths.**

  | Name | Width | Use |
  |---|---|---|
  | `text` | 36rem (576px) | body, intros, notes, sources |
  | `figure` | 52rem (832px), 1.44× text | G1, G2, G3 photo breakout |
  | `wide` | full content box (up to 1136px) | section headings, the record ledger |
  | `bleed` | 100vw | hero, colored bands only |

  At 834px wide, `figure` and `wide` both become the full content box (about 768px). At 390px everything is the content box (350px), with graphics redrawn for that width, never scaled.
- **Measure.** Newsreader at 18px in 36rem sets about 65–72 characters per line (to be measured in the layout pass; target 60–75). At 390px the body sets about 40–45.
- **Spacing scale** (px, 8-based): 4, 8, 12, 16, 24, 32, 48, 64, 96, 128.
  - Text to graphic headline: 48.
  - Headline to graphic: 16.
  - Graphic to method and source lines: 12.
  - Source line to next text: 48.
  - Section padding: clamp(80px, 12vh, 144px) top and bottom.

## 3. Type system

- **Families.** Two, both open-licensed (SIL OFL) and to be self-hosted:
  - **Archivo** (variable: width 62–125, weight 100–900). Display, UI and all data text. Verified: contains `tnum` and `pnum`; default figures are lining (digit height 687–698 against cap height 686).
  - **Newsreader** (variable: optical size 6–72, weight 200–800). Headlines where the editor wants a serif, body and running prose only. Verified: lining figures by default.
- **Data text rule.** Axis labels, direct labels, tables and figures use Archivo at width 100 (no condensed or expanded widths for data), weight 450–600, with `font-variant-numeric: lining-nums tabular-nums`. Minimum 12px.
- **Display rule.** The wide (width 110–125) and condensed (62–80) Archivo cuts are for display only: the hero motto, section headings and large typographic figures. The condensed year numerals in the ledger move to width 100, weight 700, 32px, so years stop outranking entry titles (baseline critique finding 12).
- **Scale.** Ratio 1.25 from an 18px body (rem at 16px root):

  | Step | Size | Role |
  |---|---|---|
  | −2 | 12px | chart ticks, source lines |
  | −1 | 14.4px | direct labels, method notes, captions |
  | 0 | 18px | body |
  | 1 | 22.5px | graphic headlines, lead paragraphs |
  | 2 | 28px | entry titles in articles |
  | 3 | 35px | subsection heads |
  | 4 | 44px | section heads at 390 |
  | 5–7 | 55 / 69 / 86px | section heads (fluid between steps 4 and 7) |

  The hero motto keeps its own fluid sizes.
- **Weights.** 400 body; 450–500 labels; 600 graphic headlines and entry titles; 800–900 display only. Bold inside annotations only for emphasis of the finding.
- **Line heights.** Body 1.6; lead 1.45; graphic headlines 1.2; display 0.9–1.0; labels 1.3.
- **Typesetting.** `text-wrap: balance` on all headings and graphic headlines; `text-wrap: pretty` on body; `hanging-punctuation: first` where supported; curly quotes, en dashes in ranges and true apostrophes are already in the data and stay.
- **Loading.** Self-host subsets (Latin plus punctuation) as woff2, preload the two faces used above the fold, `font-display: swap`, and set metric-matched fallbacks with `size-adjust` and `ascent-override`.
  - Archivo has 1000 units per em, ascent 878, descent 210, x-height 526. Fallback: Arial.
  - Newsreader has 2000 units per em, ascent 1470, descent 530, x-height 852. Fallback: Georgia.
  - The size-adjust values are computed in the detail pass.

## 4. Color system

Defined in OKLCH. Hue 268–275 throughout, so greys carry a faint cool cast that matches the cobalt.

| Token | Light (OKLCH → hex) | Dark (OKLCH → hex) | Use |
|---|---|---|---|
| `ground` | `oklch(1 0 0)` → #FFFFFF (Decision 1) | `oklch(0.164 0.052 274)` → #080B24 | page |
| `ink` | `oklch(0.182 0.06 273)` → #0A0E2C | `oklch(0.938 0.016 275)` → #E7EAF6 | text, ink glyphs |
| `ink-2` | `oklch(0.443 0.057 275)` → #4A5173 | `oklch(0.722 0.053 275)` → #9BA3C7 | secondary text, method and source lines |
| `context` | `oklch(0.64 0.03 272)` → #858B9F | `oklch(0.52 0.04 274)` → #616880 | context marks (revenue days, filtered-out entries) |
| `hairline` | `oklch(0.90 0.012 272)` → #DBDEE6 | `oklch(0.30 0.05 274)` → #262C47 | rules and gridlines (never meaningful on their own) |
| `accent` | `oklch(0.423 0.23 268)` → #202FC8 | `oklch(0.715 0.15 277)` → #8C98FF | the marks the headline names |
| `field` | cobalt #1F2FC8 | cobalt #1F2FC8 | hero ground only |
| `deep` | #0A0E2C | #11164A | people, credits and footer bands |

- **One accent, one meaning.** In any graphic, `accent` marks exactly the set named by that graphic's headline, which shows the same set on an accent chip (white text on accent in light mode, `ground` text on accent in dark mode). Nothing else in a graphic is accent colored. Links are `ink` with an underline; dates and figures are `ink` or `ink-2`.
- **No sequential or diverging ramp.** None of the four graphics encodes a continuous quantity by color, so none is defined. If one is added later, it gets a single-hue OKLCH lightness ramp (sequential) or two hues around a `context` midpoint (diverging), validated the same way.
- **Never color alone.** Evidence strength is encoded by glyph shape and fill pattern. The accent set is also named in the headline and, where it fits, labeled directly. The hatched "committed" pattern is a texture, not a color.
- **Gaps are mandatory.** Accent and context marks must be separated by at least 2px of `ground`. The measurement below shows why: no grey reaches 3:1 against both the ground and the accent.

**Verification** (computed September 29, 2026; WCAG 2 contrast; color-vision simulation with Machado 2009 matrices at full severity; ΔE in OKLab ×100; cross-checked with the dataviz skill's `validate_palette.js` against the real grounds):

| Check | Light | Dark | Requirement |
|---|---|---|---|
| ink on ground | 18.88 | 16.15 | 4.5 text |
| ink-2 on ground | 7.73 | 7.80 | 4.5 text |
| accent on ground | 9.12 | 7.43 | 3.0 marks, 4.5 if text |
| context on ground | 3.39 | 3.51 | 3.0 marks |
| chip text on accent | 9.12 (white) | 7.43 (ground) | 4.5 text |
| accent vs context, touching | 2.69 | 2.12 | 3.0, **not met, so the 2px gap rule applies** |
| accent vs context ΔE, normal vision | 29.3 | 22.4 | ≥15 |
| accent vs context ΔE, worst color-vision case | 23.9 (protan); tritan 20.2 | 21.5 (deutan); tritan 19.6 | ≥8 |
| hairline on ground | 1.35 | 1.42 | decorative only; never the only cue |

The validator's "lightness band" and "chroma floor" checks report FAIL for this pair. Both are rules for categorical palettes, where every slot must be a distinct saturated hue. Here the grey is intentionally grey (the context color), so they don't apply. The checks that do apply (color-vision separation, normal-vision floor, contrast against the surface) pass in both modes.

## 5. Annotation system

Annotation is its own layer: its own markup, its own collision handling, and its own rules at each width.

| Element | Spec |
|---|---|
| Graphic headline | The finding, with its number, as a sentence. Archivo 600, step 1 (22.5px), `ink`, max 32ch, balanced. The accent set is named on an accent chip. Required on every graphic. |
| Method line | One line on how to read the graphic. Archivo 400, step −1, `ink-2`. |
| Direct label | Names or values placed on or beside a mark. Archivo 500, step −1, tabular figures, `ink`. |
| Mark note | A short interpretation tied to a mark: at most 3 per graphic, at most 12 words each. Archivo 450, step −1, `ink`; the key phrase may be 600. Joined by a 1px `ink` leader with a 3px dot at the mark end. The most important note is placed first in reading order, top-left. |
| Leader lines | 1px `ink`, straight or one elbow, never curved. Minimum 12px long. |
| Numbered markers | At 390px, mark notes that don't fit become 18px circled numbers on the mark, with the note text listed in order under the graphic. |
| Source line | "Source:" plus sources, Archivo 400, step −2, `ink-2`, aligned to the text column, 12px under the method line. Links to the data. |
| Chip | Accent fill, 2px radius, 0.1em × 0.35em padding, text in chip-text color, same size as the surrounding text. Only for naming the accent set. |
| Legends | None, unless a graphic has more than one colored set and direct labels can't fit. None of G1–G4 needs one. |

Every graphic is a `<figure>` whose `<figcaption>` states the takeaway in full. Each figure also has a text alternative describing the finding and the visual, and a table view or CSV link.

## 6. Motion principles

- **Allowed to move:**
  1. Filter state changes in G1 (squares change between accent, ink and context).
  2. Entry expand and collapse in the ledger.
  3. The hero, as the declared exception (Decision 2).

  Nothing else moves.
- **Removed** (Decision 3): scroll reveals, the timeline scroll fill and the progress bar.
- **Durations.**
  - State changes: 240ms, `cubic-bezier(0.4, 0, 0.2, 1)` (ease-in-out).
  - Entrances: 320ms, `cubic-bezier(0.2, 0.7, 0.2, 1)` (ease-out).
  - Staged transitions keep each stage under 600ms, with axes, then marks, then labels.
  - No bounce, elastic or spring.
- **Object constancy.** Each entry square in G1 is keyed by entry id and keeps its position across filter states. Only its fill changes.
- **Reduced motion.** All transitions resolve instantly to the end state. The hero shows the static cracked motto. Nothing depends on motion to be understood.
- **No scroll-jacking.** No sticky scrollytelling is planned. G3 is stacked, not scrolly: its transitions wouldn't carry meaning.

## 7. Interaction budget

| Interaction | What it reveals beyond the default | Required for the story? |
|---|---|---|
| Record filters (topic, evidence, search, credits toggle, sort) | Subsets of the ledger, reflected in G1 | No |
| Expand an entry | Summary, Meta's response, status, sources | No: date, title, figure and label are visible by default, and every entry has its own page |
| Hover or focus a G1 square | That entry's title and date; click opens it in the ledger | No |
| Hover or focus a G2 tally row or segment | Highlights the matching calendar segment | No: segments are labeled and the tally is printed |
| Random entry, the `/` search shortcut | Convenience | No |

**Confirmation.** With zero interaction the reader gets every thesis, every number and every source: headlines and labels carry G1–G4, the ledger shows each entry's essentials, and each entry has its own page. Tooltips hold nothing the story depends on. All controls are keyboard-operable, have visible focus states, and meet a 44px touch target on touch devices.

## 8. Bans

Everything in the brief's ban list applies. Applied to this site specifically:

- No off-white page ground (Decision 1). No orange or burgundy anywhere.
- No kicker labels above headings. The "Page not found" label I added to the 404 page on September 29 is one, even without uppercase, and should go. The date line above entry titles ("March 2018") is content, not a kicker, and stays.
- No legends where direct labels fit. No full-contrast gridlines. No pies. No 3D.
- No gradients with more than three stops, no glassmorphism, no glow. The hero's noise texture is a grain, not a gradient; it stays.
- No bounce or spring easing, and no motion that doesn't encode data, apart from the hero exception.
- No centered-everything layouts, no uniform card grids standing in for hierarchy, no emoji icons, no stock illustration.
- AI disclosures stay where they are in every version.

## 9. Data dependencies before building

1. **Sourced 2025 revenue.** Meta's FY2025 10-K figure and link, for G2's method line (Decision 6).
2. **Euro conversion.** The ECB 2025 average EUR/USD rate and link, for G2 (Decision 6).
3. **Key sentences for G3.** One exact sentence per step, drawn from each step's existing sources, with the source named. Each needs checking against the linked source before it ships.
