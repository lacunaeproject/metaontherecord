# Reference teardowns

Phase 1 of the redesign brief. Each piece below was opened in a real browser (Playwright, Chromium) at 1440×900 and 390×844, captured frame by frame while scrolling (or clicking, for click-through stories), and measured from the live page: computed font families, sizes, weights, line heights, colors and graphic widths (`<slug>/measure.json`). Every teardown was written from the captured frames, not from memory or the title. Values marked "estimated" were read off the frames; values marked "measured" came from the page.

The frames themselves are third-party work, so they stay on disk in `<slug>/` and out of git. `capture.mjs` regenerates them: `FRAMES=90 node design/references/capture.mjs [slug ...]`. The capture declines optional cookies (it clicks "reject" or closes the notice, never "accept") so banners don't hide content.

## Coverage

Read in full (10): Reuters, The Straits Times, iStories, The Guardian, visualrambling.space (Dithering), The Pudding (Onions), C.J. Robinson, The Pudding (30 Minutes with a Stranger), FlowingData, Our World in Data.

Known gaps within those:
- **FlowingData** runs a live random simulation; the capture caught only 1 to 5 simulated lives, so its histogram is sparse in the stills and the desktop and phone runs used different default ages.
- **30 Minutes with a Stranger**: the phone capture ends at 28m 20s; the last two minutes and the closing essay were read from desktop frames only.
- **Dithering**: the year isn't shown on the page. The brief lists it as a 2025 Pudding Cup winner.
- **The Guardian** phone frames carry a ~75px ad bar at the bottom.

Could not read (5). Each blocked automated browsers; I did not attempt to get around the blocks:
| Piece | What the page returned |
|---|---|
| NYT, Swept Away (Camp Mystic) | 403, "You have been blocked… we suspect that you're a robot" |
| NYT, Inside Sednaya Prison | 403, same robot block |
| Bloomberg Green, AI data center waste heat | 403, "Press & Hold" bot check |
| Bloomberg, OpenAI, Nvidia and the web of AI deals | 403, same bot check |
| Washington Post, Biggest donors of the 2026 cycle | connection dropped (HTTP/2 protocol error) before any page loaded |

Screenshots of these can go in `nyt-camp-mystic/`, `nyt-sednaya/`, `bloomberg-datacenter-heat/`, `bloomberg-ai-deals/` and `wapo-donors-2026/`, and they'll get teardowns in the same format.

---

## Eroding protections for public lands (Reuters, 2025)

- **Claim.** "Trump policies reshape the role of federally owned land, against the tide of U.S. public opinion." The dek states it first, in frame 1440-03 (published July 28, 2025). The scrolling hero sets it up in frames 1440-01 and 1440-02 ("the geographic landscape may be the one thing that unites the left and right"). The poll chart proves the "public opinion" half in frames 1440-18 and 1440-19: 89% of Harris voters and 64% of Trump voters oppose closing public lands.

- **Grid.** One text column. There are no sidebars.
  - Text column: 660px wide at x=390–1050 (measured). Body is 20.96px.
  - Measure: the 0.5em formula gives 660 / 10.48 = 63 chars. Counted lines in frame 03 run 72–76 chars, because FreightText is narrow. Phone: 360px at 18.17px gives 40 chars by formula and about 45 counted (390-04).
  - Graphics break out to four fixed widths:
    - 926px, 1.40x text (x=258–1184): both bar charts, the pull quote, the water chart (about 930px) and the poll chart (about 910px).
    - 1308px framed map, 1.98x text (x=66–1374).
    - 700px small-multiple strip, 1.06x text (x=375–1075).
    - About 1054px county-map spread, 1.6x text.
    - The topographic hero is full-bleed at 1440px, 2.18x text.
  - Notes and sources always return to the 660px text column, even under wide graphics (frames 04, 10, 13, 16).

- **Type.**
  - Headline: Baskerville 400 in all caps with letterspacing, #404040, stacked in three tiers. "PUBLIC LANDS" is 80.16px (measured). "ERODING PROTECTIONS" is about 32px and "FOR" about 20px (estimated).
  - Dek: italic serif, about 24px.
  - Byline: bold serif small caps, about 14px.
  - Body: FreightText 400, 20.96/31.44 (1.5 line-height), #404040.
  - Chart titles: letterspaced serif caps, about 18–20px.
  - Chart category labels: italic serif, about 16px ("American West", "Bureau of Land Management").
  - Values and map callouts: a rounded, hand-lettered-looking sans at about 13–14px ("56%", "87% of wildlife refuges…").
  - Notes and sources: sans, about 13px, grey.
  - Pull quote: bold italic serif at about 40px, in tan, spanning the 926px width (frame 17).
  - Ratio, headline to body to chart label: 80 : 21 : 14, about 5.7 : 1.5 : 1.
  - Weights: 400 for the headline and body, and bold for the byline, pull quote, map-legend headings and callout text.
  - Numerals: measured font-variant-numeric is normal. Body figures ("1860s", "59 million") render as lining.

- **Color.**
  - Page: bg #F4F3E4 (measured rgb 244,243,228), text #404040.
  - Five agency hues carry meaning, and each keeps its color across the bar chart and the map (frames 05–09): BLM #EABF4E, Forest Service #C7CC66, Fish & Wildlife #B5D4CE, National Park Service #EB7E5F, Other #E1DBCB.
  - Chart-specific hues:
    - Location bar: #CCBF92.
    - "Federal public land" in the small multiples: olive #A6B272.
    - Water chart: national forests #7DB0AB, other forests #B5D4CE.
    - Poll chart: Harris #00626B and Trump #A42401. The SVGs also carry #00767E and #982F00.
  - Context grey is #E1DBCB. It is used every time for the remainder category: "Rest of U.S.", "Other federal" and "Non-forest".
  - Tan #CEB87C marks poll respondents who did not oppose closure.
  - There is no single accent. Rust #D64000 is the most frequent SVG color (28 uses) and matches the Reuters logo. Meaning comes from the teal/rust pair: left and right, which converge.
  - Across the piece, about 9 hues carry meaning. Each chart uses 2–5 of them.

- **Annotation.**
  - Location and agency bars (frames 04–05): every bar is labeled directly. The value sits inside the bar at top-left and the italic name sits below it. There is no legend. The 5% "Other federal" sliver takes a dashed vertical leader to a label on the second line.
  - Land map (frames 06–10):
    - Five legend swatches in the left margin. Each has a bold italic name and a 2–5 line description, so the legend also explains what each agency does.
    - Five callouts. Three use angled leader lines ("87% of wildlife refuges…", "Tongass National Forest…", "Areas of Yosemite…"). "About 60% of BLM lands…" and "Only 8% of all federal land is in the East" are right-aligned text with no line.
    - About 7 place labels in small grey caps.
  - Small multiples (frame 11): a 3-key inline legend sits above the panels. Each of the 20 panels has a direct "↗945%" or "↘−51%" label below it. Four dashed leader lines drop from the 650%, 455%, 424% and 355% panels to their enlarged county maps.
  - County maps (frames 12–13): 2 icon keys and a 2–4 line blurb per map.
  - Water chart (frames 15–16): every value is labeled directly. One bracket callout reads "83% from forests".
  - Poll chart (frames 18–19): 2 direct percentages, 2 group headers and 1 endpoint label, "OPPOSE CLOSURE OF PUBLIC LANDS".

- **Density.**
  - Location bar: 3 marks. Agency bar: 5 marks.
  - Land map: raster relief with thousands of polygons, which cannot be counted from the stills.
  - Small multiples: 20 panels.
  - County maps: 4 maps with 8 icons in total.
  - Water chart: 5 cities × 3 bars = 15 marks.
  - Poll chart: 40 diamonds (20 per group, so each diamond = 5%; 18 teal and 13 rust) plus 31 curves.
  - Whitespace, measured from the frames:
    - About 90–135px from the last paragraph to a chart title (frame 04: 93px, frame 05: 114px, frame 06: 135px, frame 11: 101px).
    - About 55px from a chart to its note.
    - About 60–70px from the note to the next paragraph.

- **Motion and interaction.**
  - The only state change in the stills is the hero.
    - Frame 1440-01 shows only the topographic texture, two diamonds (teal at x=433, rust at x=1016) and the first phrase.
    - In 1440-02 two river-like lines have drawn from the diamonds and meet at the center, and two more phrases have appeared.
    - In 1440-03 the joined line ends at a grey diamond above the title.
  - Scroll triggers it, since the frames are sequential scroll positions. Duration is not observable in stills.
  - All charts below the hero are static. Nothing is hover-only: every value is printed on the page.
  - The story survives with no interaction.

- **Mobile.**
  - Text and title:
    - Text column: 360px with 15px gutters.
    - The headline tiers shrink, with "PUBLIC LANDS" at 39.6px (measured).
    - The pull quote goes from 3 lines to 6 (390-19).
  - Bar charts rotate from horizontal to vertical stacked columns (about 52px wide, labels to the right), as seen in 390-04, 390-05 and 390-07.
  - Land map:
    - The five-part margin legend moves above the map as a stacked list (390-08).
    - The map shrinks to a 344px frame showing the whole U.S. in one view (390-09).
    - It keeps 4 of the 5 callouts. "60% of BLM lands" and most grey place labels are cut.
  - Small multiples: the 10-panel rows wrap into 2 rows of 5 (390-11). The dashed leaders remain.
  - County maps stack in a single column (390-13).
  - Water chart: Phoenix stays full width, and the other 4 cities form a 2×2 grid (390-16, 390-17).
  - Poll chart: drops to about 10 diamonds per group, so each diamond is about 10% (390-20).

- **The steal.** The poll chart's "many marks converge on one labeled conclusion" form (frames 18–19). Each group is a row of 20 unit diamonds, and colored ones bend by thin curves into a single stem that ends at a black diamond with a caps label. Adapt it for **"One thread through the record"**, the 5-step teen-safety timeline:
  - Draw the five dated steps as cobalt diamonds in a row.
  - Drop a 1px cobalt curve from each step into one shared stem.
  - End the stem at a single ink diamond labeled with where the thread arrives, such as the latest ruling.
  - Print each step's evidence label under its diamond, the way "89%" sits under the curves.
  - Keep it static SVG with every label printed, as Reuters does. On phones, follow their move and tighten the row spacing rather than rotating it.

- **Frames cited.** 1440-01, 1440-02, 1440-03, 1440-04, 1440-05, 1440-06, 1440-07, 1440-08, 1440-09, 1440-10, 1440-11, 1440-12, 1440-13, 1440-15, 1440-16, 1440-17, 1440-18, 1440-19, 1440-21; 390-01, 390-03, 390-04, 390-05, 390-07, 390-08, 390-09, 390-11, 390-13, 390-16, 390-17, 390-19, 390-20; measure.json.

---

## Indonesia needs to grow more rice, corn and sugar. Can its forests survive? (The Straits Times, 2026)

- **Claim.** Indonesia's food self-sufficiency drive is clearing forest for estates that repeatedly fail, while higher yields on existing farmland, degraded land and crop diversification could raise output without deforestation. The dek states both halves first, in frame 1440-05 (published Sept 12, 2026): "Jakarta wants to boost crop production, risking the clearance of millions of hectares of forest. Yet, there are solutions that can increase production of rice and other staples without deforestation." The proof runs in this order:
  - **Kalumpang satellite sequence (frames 1440-07 to 1440-13).** 98.3ha cleared by June 2025 and 188.1ha by September 2025, still "unused" in July 2026.
  - **Scale-out maps.**
    - The national rice scheme covers 455,000ha (390-25).
    - South Papua estates have about 1m ha of forest cover (1440-23).
    - 20.6m ha of forest is reserved for food, energy and water, of which 8.8m ha is natural forest (1440-25).
  - **Permanent-deforestation map for 2001–2025 (1440-27, 1440-28).**
  - **Solutions half, starting at 1440-52.** It has no data graphics.

- **Grid.** One text column. There are no sidebars.
  - Text column: 700px at x=370–1070 (measured). This holds in every text frame (1440-13, 1440-31, 1440-56, 1440-61).
  - Body is about 19px on a 27px line pitch (estimated from 1440-13). The 0.5em formula gives 700 / 9.5 = 74 chars. Counted lines run 80–87 chars (1440-13: "many of the roughly 500 households in the village – even though they held no title" = 83).
  - Phone: 358px at about 19px gives 38 chars by formula. Counted lines run 38–44 (390-16, 390-67).
  - Graphics use five widths:
    - **Sticky satellite stage:** 1302px (x=69–1371), 1.86x text, inset 16px top and bottom in the 900px viewport (1440-07 to 1440-11, 1440-21).
    - **Sticky national and regional maps:** 1408px (x=16–1424), 2.01x text (1440-23, 1440-25, 1440-33, 1440-35, 1440-36, 1440-37).
    - **Static permanent-deforestation map:** full-bleed 1440px, 2.06x text. Its title sits at text width, x=370 (1440-27, 1440-28).
    - **Static South Papua concessions map:** 700px, 1.0x text. This is the measured 700px figure in measure.json (1440-44, 1440-45).
    - **Photos and videos:** inline photos at 700px (1440-17, 1440-39, 1440-41, 1440-49, 1440-53, 1440-57). Full-bleed videos and photos at 1440px (1440-01 to 1440-05, 1440-15, 1440-21, 1440-29, 1440-43, 1440-48, 1440-51, 1440-55).
  - Section icons are about 155px wide and centered (1440-44, 1440-52, 1440-59).

- **Type.**
  - Headline: "Selane Twenty" serif, 400, 50/52, white (measured).
  - Dek: Selane Text, 23/30 (measured).
  - Body: Selane Text, about 19/27, white.
  - Section heads: serif, about 26px, centered, above each chapter. Seen: "South Papua's troubled rice and sugar estates" (1440-44), "Supercharging rice fields" (1440-52), "Degraded land" (1440-59), "Safeguarding the forest" (390-34), "Cetak Sawah Rakyat – national rice programme" (390-43).
  - Map text:
    - Place labels: CuratorRegular 14–16px, rgba(255,255,255,0.9) (measured).
    - Country labels: CuratorBold 18px (measured), sometimes letterspaced about 0.5em ("I N D O N E S I A", 1440-25, 1440-33).
  - Static-map titles: a sans sentence, about 18px, at x=370 (1440-27, 1440-44).
  - Sticky stage:
    - Date stamps: sans caps, about 22px ("APRIL 2025").
    - Area labels: bold sans, about 32px, yellow ("188.1ha").
    - Caption cards: serif, about 19/31.
  - Captions and credits: sans, about 13px, grey, with the credit in about 10px caps. Source lines: about 13px sans (1440-28).
  - Ratio, headline to body to chart label: 50 : 19 : 14, about 3.6 : 1.4 : 1.
  - Weights: 400 for all running text. Bold appears only in chips, area labels, country labels and "Produced by:" (1440-61).
  - Numerals: measured font-variant-numeric is normal. Figures render as lining ("433,751ha", 1440-26).

- **Color.**
  - Page bg: #1E202E (measured rgb 30,32,46).
  - About 7 hues carry meaning:
    - **Yellow: cleared or deforested land.** The Kalumpang polygon stroke is #EEBD12, with fill at about 40% alpha. On the national permanent-deforestation map, fill and chip are both #FBC80E (sampled).
    - **Cyan #0AD5CB:** the Cetak Sawah Rakyat rice scheme.
    - **Green #9DD171 / #6FA946:** forest area reserved for food, energy and water (1440-25).
    - **Blue: rice.** Crop dots #46A3DD, chip #49B0EE, concession fill #0D7BAE.
    - **Violet: sugarcane.** Chip #9A63D4, concession fill #673BC2.
    - **Olive #B4AC5E: maize.** Used for the chip and dots (1440-35).
    - **Coral #F2715A (measured):** the viewport box on the globe locator, which moves with each map state (1440-25, 1440-33, 1440-35, 1440-37).
  - Context colors:
    - Land is slate #304055 (measured rgb 48,63,84), and sea is #1D202F, about equal to the page bg.
    - Hillshade relief appears on the zoomed maps (1440-35, 1440-37).
  - The single accent is yellow, and it means "cleared". The same yellow marks the 188.1ha Kalumpang clearance and the national 2001–2025 permanent deforestation, and the drop cap and byline links reuse it (#FBC80E).
  - The solutions half (1440-52 to 1440-61) uses no data color. Only the green section icons appear (#72A21E, sampled from an icon in the earlier capture).

- **Annotation.**
  - No legend box appears anywhere. The key is written into a sentence, with a filled chip whose color matches the marks:
    - Caption cards: "national rice scheme" (1440-11), "rice" / "sugar" (1440-23), "forest area" (1440-25), "rice" (1440-33), "maize" (1440-35), "Sugarcane" (1440-36).
    - Static-map titles: "permanent deforestation" (1440-27); "rice" and "sugarcane" (1440-44).
  - Each sticky state has:
    - 1 caption card, 400px wide, with a 1px light border.
    - 0–1 date stamp.
    - 0–1 direct area label centered in the polygon (1440-09, 1440-11).
    - 1 scale bar and 1 globe locator of about 120px.
    - 3–15 place labels.
  - The crop-dot map explains its size encoding in prose: "the circles are sized based on the land used for each crop" (1440-33). There is no size key.
  - Static maps put the title sentence above, and the source line 20px below the map. Example: "Source: WRI/Google DeepMind Global Drivers Of Forest Loss 2001-2025" (1440-28).
  - There are 0 leader lines in the whole piece.

- **Density.**
  - Kalumpang states: 1 yellow polygon. July 2026 adds 5 cyan polygons.
  - Scheme map: 30+ cyan fragments (390-25). South Papua estates: about 60 fragments (1440-23).
  - Forest-area and permanent-deforestation maps: raster fills with thousands of patches, which cannot be counted.
  - Crop-dot maps:
    - Rice: about 900–1,200 blue dots, estimated from the hex-packed fill of Sumatra, Kalimantan, Sulawesi and Papua (1440-33, 1440-34).
    - Maize: about 90 dots in the Sumatra view (1440-35).
    - Sugarcane: about 200 violet dots (1440-37).
  - Concessions map: 2 filled regions and 5 labels (1440-45).
  - Solutions half: 0 data graphics; 7 photos or videos and 2 section icons (1440-51 to 1440-61).
  - Whitespace:
    - Paragraph to static-map title: about 85px. Title to map: about 40px (1440-27). Map to source: 20px. Source to text: about 50px (1440-28).
    - Photo caption to text: about 60px (1440-41, 1440-53).
    - Text to section icon: about 70px. Icon to head: about 40px (1440-52).

- **Motion and interaction.**
  - Hero (1440-01 to 1440-05): a full-screen drone video with "SCROLL DOWN". Caption cards pass over it (1440-03), and the headline card rises over the video (1440-05).
  - Three sticky, scroll-stepped map sequences:
    1. **Kalumpang (1440-07 to 1440-11).** APRIL 2025 with no polygon, then JUNE 2025 at 98.3ha, then SEPTEMBER 2025 at 188.1ha, then JULY 2026 with cyan scheme overlays.
    2. **Zoom-out (1440-21 to 1440-25).** It re-enters on the same July 2026 view, then goes to the 455,000ha scheme (2 km scale bar on phone, 390-25), then South Papua rice and sugar estates (50 km), then the national forest-area map (300 km).
    3. **Crop dots (1440-33 to 1440-37).** National rice (300 km), then Sumatra maize (200 km), then Papua sugarcane (200 km), then the same view at 100 km with the card gone.
  - In each sequence the coral globe box re-frames to the current extent.
  - Trigger: scrolling only. No hover, tooltip, toggle or control appears in any frame.
  - Duration and easing are not observable in stills.
  - The two static maps (1440-27, 1440-44) and the whole solutions half need no interaction.
  - The story survives without interaction apart from the exact 98.3ha and 188.1ha figures, which appear only inside the sticky graphic; the prose says "nearly 200ha".

- **Mobile.**
  - Text: headline 32/35, body at 16px gutters (358px, measured).
  - Kalumpang stage: a 390×520px box vertically centered in the 844px viewport, with about 162px dark bands (390-10, 390-13). Caption cards move below or over the image. The scale bar changes from 200 m to 300 m.
  - Regional and crop maps go full-screen at 390×844, with cards at 358px (390-25, 390-28, 390-40, 390-41).
  - Scale bars coarsen: national 300 km becomes 500 km (390-28, 390-31), and the concessions map goes from 50 km to 100 km (390-52).
  - Static maps go full-width at 390px. The chip title wraps to 3 lines (390-31, 390-52).
  - The globe locator shrinks from about 120px to about 60px.
  - Recirculation goes from a 4-across row (1440-62) to a single stacked column (390-70, 390-73).
  - Nothing is rotated or cut from the story.

- **The steal.** Put the legend inside the sentence: a word or phrase in a filled chip whose color matches the marks it names. ST uses it in both places: in scrolly caption cards (1440-11, 1440-23, 1440-25, 1440-33, 1440-35, 1440-36) and as the title of a static chart (1440-27, 1440-44). Adapt it for **"The record"** ledger's entries-per-year strip, which also covers the evidence-label key used in **"How we know"**:
  - Replace the separate key with one title sentence above the strip, such as "Of 51 entries, 19 are court rulings and 32 are reported events."
  - Set "court rulings" and "reported events" as chips filled with the exact colors of those segments.
  - Reuse the same chips as the topic and evidence filter buttons, so the sentence, the strip and the filter share one token.
  - Keep one accent the way ST keeps yellow for "cleared": cobalt should mean only one evidence class. On phones, let the title wrap (ST's goes to 3 lines at 358px) and leave the chips inline.

- **Frames cited.** 1440-01, 1440-03, 1440-05, 1440-07, 1440-09, 1440-11, 1440-13, 1440-15, 1440-17, 1440-19, 1440-21, 1440-23, 1440-25, 1440-26, 1440-27, 1440-28, 1440-29, 1440-31, 1440-32, 1440-33, 1440-34, 1440-35, 1440-36, 1440-37, 1440-39, 1440-41, 1440-43, 1440-44, 1440-45, 1440-47, 1440-48, 1440-49, 1440-50, 1440-51, 1440-52, 1440-53, 1440-55, 1440-57, 1440-59, 1440-61, 1440-62; 390-01, 390-07, 390-10, 390-13, 390-16, 390-25, 390-28, 390-31, 390-34, 390-40, 390-41, 390-43, 390-52, 390-61, 390-67, 390-70, 390-73; measure.json.

- **Capture notes (not a template heading, recorded for accuracy).**
  - The recapture covers the full page: desktop is 47,277px and phone is 53,063px.
  - The story ends and the credits ("Produced by:") appear at 1440-61. The recirculation and footer are at 1440-62. Frames 1440-63 to 1440-90 are byte-identical copies of 1440-62 (checked by md5).
  - On phone, the footer is at 390-74, and 390-75 to 390-90 are identical copies of it.
  - No cookie banner or paywall appears. Only the ST masthead and "LOG IN" overlay the hero (1440-01, 390-01).
  - The earlier notes about black map tiles (old 1440-24) and a mid-transition frame (old 1440-08) do not recur in the frames checked here.

---

## About 60% of Paper Votes for United Russia Might be Fabricated (iStories / Important Stories, 2026)

- **Claim.** Roughly 18.4 million of the ~30 million paper ballots counted for United Russia may be fabricated, which would put the party's real share near 35% rather than the declared 58%. It is first stated in the h1 and standfirst on frame 1440-01 ("18 of 30 millions", "around 35% instead of the declared 58%"). The body restates it as a section head on 1440-03 ("United Russia got no more than 35% of the real vote share") and as a chart title on 1440-06 ("More than 18 million paper ballot votes ... may have been fabricated").

- **Grid.**
  - Structure: one text column. A white page card spans x=24–1416 (1392px) and sits on a dark page background, `rgb(37,39,41)` #252729.
  - Measure: the text column runs x=288–1152, so it is 864px wide. Body type is about 17px (estimated from frames; line pitch 24px, measured on 1440-03 at y=83/107/131). At 864 / (17 × 0.5) that gives ~100 characters per line, and a counted line on 1440-03 has 104. That is a long measure.
  - Chart widths:
    - The seven inline charts are the same width as the text: each pink card is 864px (x=288–1152) with ~20px inner padding, so plot areas are ~825px. None breaks out.
    - The small-multiples card (1440-09) uses two columns of about 390px each inside that 864px.
    - The only breakout is the hero. `measure.json` records the figure as 1296px wide; in the frame it fills the 1392px page card edge to edge. Relative to the 864px text column, that is 1.5–1.6×.
  - Chrome: a sticky cream section bar, 36px tall, stays pinned at the top of every scrolled frame.

- **Type.**
  - Families:
    - Sans (Proto Grotesk): headline, section heads, chart titles. Chart axes and legends use a lighter grotesk.
    - Serif (IBM Plex Serif): standfirst, body, and related-story titles.
  - Measured sizes:
    - h1: Proto Grotesk 52px/54px, weight 700, #252729. At 390: 28px/30px.
    - Standfirst: IBM Plex Serif 28px/30px, weight 400. At 390: 22.5px/24px. `measure.json` "body" sampled this element.
  - Estimated from frames:
    - Body: ~17px/24px serif.
    - Section h2: ~32px sans, weight ~500.
    - Chart title: ~28px sans, weight 800–900 in most cards. Two cards (1440-05 and 1440-11) use a narrower ~26px bold semi-condensed face, so the chart title style is not consistent.
    - Chart subtitle: ~22px regular.
    - Axis ticks and legend: ~16–18px. Axis titles: ~16px, rotated 90° on the y axis.
    - Bar value labels: ~18px heavy.
  - Ratio (headline : body : chart label): 52 : 17 : 16, or about 3.1 : 1 : 0.95. Chart labels are nearly body size.
  - Weights: 400 (body), ~500 (section heads), 700 (h1), ~800–900 (chart titles and bar values).
  - Numerals: `measure.json` reports `font-variant-numeric` "normal" (default lining and proportional). Axes use decimal commas ("0,5", "1,5"), carried over from the Russian edition. Turnout ticks are irregular ("0 3 6 9 13 17 21 25 30..." on 1440-06/07 and "0.0 11.1 22.1 35.1..." on 1440-09).

- **Color.**
  - Brand accent: `rgb(153,65,70)` #994146, the most frequent SVG fill (403 uses in `measure.json`). It is used on the logo, links, the donate band and the per-chart logo stamp, never on data.
  - Data hues:
    - Scatter (1440-05) and Dagestan dots (1440-11/12): one hue, blue ~#1F66B3 (estimated).
    - Stacked area (1440-06): two hues. Blue means "real votes" and red ~#C9454A (estimated) means "anomalous votes".
    - Tongs (1440-13/14): the same pair. Blue is United Russia and red is "any other party".
    - Multi-line (1440-07): five categorical hues (red, olive, teal, grey, lavender), one per election.
    - Small multiples (1440-09): one hue per day (red, purple, blue).
    - Bars (1440-15/16): one teal ~#169A9A (estimated).
  - Context colors:
    - Chart cards have a pale pink ground, ~#FDF3F3 (estimated).
    - Shaded "zones" are warm grey, ~#E9E4E4 (estimated): the "Votes transferred" band on 1440-13/14 and the commission bands on 1440-11/12.
    - Gridlines are very light grey.
    - Source text and axis titles are mid grey, ~#6E6E6E (estimated). `measure.json` lists `rgb(104,104,104)` and `rgb(141,134,134)` as low-count SVG greys.
  - Meaning: blue versus red is the argument. Red in the area chart is the fabricated excess. A navy `rgb(28,39,76)` appears 8 times in SVGs. The four Google-logo colors in `measure.json` (#EA4335, #4285F4, #FBBC05, #34A853) belong to an "Add on Google" button, not to the data.

- **Annotation.**
  - Every chart card carries the same furniture: a declarative title that states the finding, a one- or two-line method subtitle, a source line with a year, and a logo stamp at top right, 108×30px (estimated).
  - Per chart:
    - Scatter: 0 annotations on marks. The subtitle does the reading ("One dot equals one polling station...").
    - Stacked area: a 2-swatch legend above the plot, 0 direct labels.
    - Multi-line: a 5-swatch legend above the plot plus a "Votes for" select field, 0 direct labels.
    - Small multiples: 8 dashed vertical reference lines per panel, labeled directly with rotated percentages (30%, 40%, 50%, 60%, 65%, 70%, 85%, 95%), so 24 labels in total. The panel titles are colored to match each series, so they act as the legend.
    - Dagestan strip: 12 grey bands, each labeled directly with a rotated commission name (Bezhta, Gunib, Derbent...).
    - Tongs: 1 shaded zone labeled directly "Votes transferred" (rotated), plus a 2-swatch legend.
    - Bars: 11 direct value labels at bar ends, plus category labels on the left. No legend.
  - None of the charts uses leader lines or callout boxes.
  - Some charts put series identity in a legend (area, multi-line, tongs). Others label directly (bars, small multiples, bands). Reference thresholds are always labeled directly.

- **Density.**
  - Marks per graphic (estimated):
    - Scatter: ~40,000–60,000 dots, one per polling station, heavily overplotted.
    - Stacked area: 2 series × ~100 turnout bins.
    - Multi-line: 5 lines × ~100 points.
    - Small multiples: 3 panels × ~1,000 bins, plus 24 reference lines.
    - Dagestan strip: ~1,500 dots plus 12 bands.
    - Tongs: 2 lines × ~80 points plus 1 band.
    - Bars: 11.
  - Whitespace: ~50–60px between a text block and a chart card, above and below (1440-05: text ends y≈823, card starts y≈883; 1440-06: text ends y≈57, card starts y≈118). Inner card padding is ~20px on the left and right and ~30–40px on top. Section h2s have ~90px above and ~40px below.

- **Motion and interaction.**
  - Scroll-driven line draw on the tongs chart:
    - 1440-13: the blue line stops at turnout ≈83% partway through the plot.
    - 1440-14: both lines are complete to 100%.
    - 390-18: both lines stop near turnout ≈72% while the chart is fully in view.
    - Trigger: scroll position. Duration: not observable in stills.
  - The multi-line chart has a "Votes for" select or search field (1440-07, 390-09). Its behavior is not observable in stills.
  - An info icon (ⓘ) sits inline after "New Moscow" (1440-10 and 390-13). It is probably a footnote popover; behavior is not observable in stills.
  - The hero composites the tongs chart (axes, blue and red lines, "Votes transferred" label) over a photo of the election commission chair (1440-02, 390-02). It is static.
  - The story survives without interaction. Every chart is readable in its end state, and titles state the conclusion.

- **Mobile.**
  - Text and type at 390: the column is 354px (18px gutters). h1 is 28px/30px, standfirst 22.5px/24px, body ~17px. That gives ~41 characters per line (354 / 8.5), down from ~100 on desktop.
  - Charts:
    - Cards shrink to 354px, the column width, and do not scroll horizontally.
    - Turnout ticks thin from 26 to 13 (390-09: "0 6 13 21 30 38 47 56 65 74 83 91 99").
    - Legends wrap to 2–3 lines. The stacked-area legend stacks swatches vertically (390-07).
    - Small multiples go from 2 columns to 1, and turnout ticks become "0.0 9.1 18.1 29.1..." (390-11).
  - Defects:
    - Dagestan band labels collide: "Kayakent" and "Kizilyurt" overprint (390-15).
    - Bar value labels clip at the card's right edge: "61%" is cut off (390-21).
  - Other changes:
    - The metadata row (date, authors, editor) stacks vertically (390-02).
    - The hero chart-photo stays at 390 × ~236px.
    - "Read also" becomes a horizontal card carousel with arrows (390-25).
  - Nothing is rotated. No chart is cut.

- **The steal.** Treat each chart as a self-contained evidence card. The title is a declarative finding with the number in it ("More than 18 million paper ballot votes ... may have been fabricated"). Under it goes a one-line method subtitle, and at the foot a source line with its year, all inside one tinted card with a small wordmark, so a screenshot of the card alone keeps the claim, method and source together.
  - Where: the **"Penalties and revenue"** square grid and tally.
  - Title: replace any neutral label with the finding, e.g. "Every fine to date equals N days of Meta revenue".
  - Subtitle: one line on the method ("1 square = $X; revenue from 10-K filings").
  - Footer: source and year, in the site's grey.
  - Card: a 1px ink rule or a very light cobalt tint rather than iStories' pink.
  - Wordmark: "metaontherecord.org" set in Archivo at ~11px, top right.

- **Frames cited.**
  - 1440 claim and hero: 1440-01, 1440-02, 1440-03
  - 1440 charts: 1440-05, 1440-06, 1440-07, 1440-09, 1440-11, 1440-12, 1440-13, 1440-14, 1440-15, 1440-16
  - 1440 other: 1440-10 (inline info icon), 1440-17/18 (donation band and end of article)
  - 390: 390-01, 390-02, 390-07, 390-09, 390-11, 390-13, 390-15, 390-18, 390-21, 390-25

---

## Bird migration is changing. What does this reveal about our planet? – visualised (The Guardian, 2025)

- **Claim.** GPS tracking shows migration routes and wintering grounds shifting as the climate warms. The evidence is three tracked birds; the plainest proof is Bewick's swans wintering further north each year as temperatures rise (2016 3.02C to 2019 5.53C, frame 1440-21).
  - First stated in the h1 on frame 1440-01 ("Bird migration is changing."), which is fully visible in this capture.
  - The page is dated "Thu 16 Oct 2025 04.00 EDT" (1440-01).
  - Sharpened in the standfirst on 1440-08 ("new threats that are reshaping them").

- **Grid.**
  - Structure: a 3-column editorial grid framed by thin vertical rules at x=70, 320 and 1370.
    - Left rail: x=70–320 (250px), for captions, the species fact blocks and small illustrations.
    - Main text column: x=331–951 (620px).
    - Right: x=951–1370 (~420px), empty.
  - Measure: body 17px/24px (measured). 620 / 8.5 gives ~73 characters per line, and a counted line on 1440-11 has 73. `measure.json` reports 56 characters per line for a 458px element, the scrollytelling narration box (x=480–960).
  - Graphic widths, from `measure.json` and the frames:
    - Hero and scrollytelling world map: 1440–1442px (canvas plus SVG), full bleed (1440-01 to 1440-08). That is 2.3× the text column.
    - Species illustrations: 1260px (x≈90–1350), 2.0× the text column (1440-08/09, 1440-14, 1440-18).
    - Route maps ("Marlo's journey", "A nightingale's journey", "Mary's journey", the swan wintering map, the wind map): 620px, exactly the text column.
    - Inline photos in the left rail: 380px (x=91–471). They overhang the text column by 150px, and the text wraps around them (1440-11, 1440-16, 1440-20).
    - West Africa habitat map (1440-16/17): ~964px (x≈171–1135), a partial breakout of 1.55× the text column. It is introduced by a 1px rule spanning x=91–1350.

- **Type.**
  - Families: all serif Egyptian for text; the charts use a sans.
    - Headline: GH Guardian Headline.
    - Body: Guardian Text Egyptian.
    - Chart labels and captions: Guardian Text Sans (estimated from letterforms).
  - Measured sizes:
    - h1: 50px/70px, weight 500, white. It is set 4 lines deep on per-line black highlight boxes (line pitch 70px at y≈340/410/480/550, left edge x=241, 1440-01). At 390: 30px/42px, also 4 lines (390-01).
    - Body: 17px/24px, weight 400, `rgb(18,18,18)`.
  - Estimated from frames:
    - Hero furniture above and below the h1 (1440-01):
      - Kicker: a plum box with "The age of extinction" in bold serif ~20px over "Birds" ~16px.
      - Age badge: yellow, "This article is more than 11 months old", ~16px sans.
      - Byline: bold plum serif ~24px over 2 lines (4 authors).
      - Dateline: ~12px sans.
      - Share: a pill button with a plum outline.
    - Species headers: Latin name in italic serif ~42px over the common name in bold serif ~42px (1440-08, 1440-14, 1440-18).
    - Fact rows (DIET / LENGTH / MIGRATION): ~16px sans, with labels in caps.
    - Chart titles ("Marlo's journey"): ~20px bold serif, above a 1px rule.
    - Chart annotations: bold date ~13px plus regular description ~13px sans.
    - Place names: italic grey ~13px.
    - Graphic credits ("Guardian graphic."): ~11px grey.
    - Scrollytelling: narration boxes ~18px serif; month label ~24px sans caps (e.g. "JANUARY").
  - Ratio (headline : body : chart label): 50 : 17 : 13, or about 3.8 : 1 : 0.76.
  - Weights: 400, 500 (h1) and 700 (byline, dates in labels, chart titles).
  - Numerals: `measure.json` reports "normal". Dates are written out ("Nov 2019", "Winter 2016-17"). Temperatures carry both units ("4.32C (39.8F)").

- **Color.**
  - Page ground: `rgb(248,243,240)` #F8F3F0.
  - Context grey: `rgb(95,94,91)` #5F5E5B, the dominant SVG color (119 uses). It is used for coastlines, borders, place labels and arrows. The base map land in the route maps is a paler fill of about #F3EEEA (estimated).
  - Single accent: plum or magenta, `rgb(88,25,64)` #581940 and `rgb(92,12,74)` #5C0C4A. It always means "a tracked bird": flight tracks, GPS dots, start and end glyphs, the play-progress ring, and the bold keyword "British nightingales" in 1440-17. The same plum colors the kicker box and byline (1440-01), so the section brand and the data accent are one color.
  - Ramps: the swan map varies the accent from light pink to dark plum to encode year (2016 to 2019, 4 steps, 1440-21).
  - Other meaning-carrying ramps appear only in the scrollytelling base layer and the habitat map:
    - Vegetation: white to green, "Sparser–Denser" (1440-04).
    - Temperature: blue to red, "Cooler–Warmer" (1440-05).
    - Habitat suitability: yellow to green, "Less suitable–More suitable" (1440-17).
    - Wind speed: pale to dark slate blue, 0–90 km/h (1440-12).
  - Count: 1 categorical accent plus 4 continuous ramps.
  - Other colors: the navy #052962 and the yellow badge are Guardian page chrome. `rgb(0,119,182)` #0077B6 appears 5 times; its role is not observable in stills.

- **Annotation.**
  - "Marlo's journey" (1440-10): 6 text callouts, each a bold date plus 1–3 lines ("Nov 2019 / Leaves the colony in Bugio Island..."). One of them is a pure reading note ("Marlo also makes long foraging trips, shown here as squiggly lines"). Also 5 curved direction arrows, 1 italic place label ("Atlantic Ocean"), a flag glyph at the start and a checkered flag at the end. Callouts attach by adjacency or a short straight leader to a dot.
  - "A nightingale's journey" (1440-15):
    - 4 date callouts (Jul, Apr, Oct, Mar), each with a horizontal leader line ~20–50px long to the route.
    - 2 italic grey method labels, "GPS signal" (the dots) and "Approximate route" (the dashed line), also on leaders. These replace a legend for solid versus dashed line.
    - 3 arrows.
  - "Mary's journey" (1440-19):
    - 5 date callouts (May 2017, Sep 2017, Feb 2017, Winter 2017-18, Winter 2016-17), each attached by a vertical leader ~30–50px long.
    - 2 arrows, plus an inset locator globe ~120px across with a plum box.
    - One callout carries the claim in miniature: "In Germany, 3 degrees north of her 2016 wintering site".
  - Wind map (1440-12/13):
    - A dated header ("Monday 2 September"), a labeled gradient scale (0/30/60/90 km/h), and a locator globe.
    - 1 place label, the petrel track as a plum line with a dot head, and a play button.
    - The caption sits below with a camera icon.
  - West Africa map (1440-16/17):
    - A legend strip at top: a dot for "British birds" and a gradient bar for "Less suitable / More suitable".
    - 1 curved-leader callout whose keyword is set in the accent color.
    - ~14 country labels in grey, a scale bar in km and miles, and a 2-line method note under the map.
  - Swan wintering map (1440-21): 4 year labels, each colored to match its dot cluster, with an italic temperature line beneath. There is no legend; everything is labeled directly.
  - Scrollytelling map (1440-03 to 1440-07): the ramp legends sit inside the narration box, under the sentence that explains them. A petrel-track glyph is set inline in a sentence as a word-sized legend ("~ Desertas petrel", 1440-06).

- **Density.**
  - Marks per graphic (estimated):
    - World map: 45 species' paths drawn as ~150–200 dots and short comet-tail dashes per frame (1440-03, 1440-04).
    - Marlo's track: 1 polyline of ~500+ vertices in a 620 × ~720px map (y≈80–800, 1440-10).
    - Nightingale: 2 routes, 5 GPS dots and 3 arrows.
    - Mary: 2 routes and ~30 clustered dots.
    - Swan wintering: ~60 dots in 4 clusters.
    - West Africa: ~35 dots over a raster.
  - Whitespace, measured on 1440-10:
    - Rule to chart title: ~20px. Title to map top: ~35px.
    - Map bottom to "Guardian graphic." credit: ~27px. Credit to next text: ~32px.
  - Whitespace, measured on 1440-21: last text line to the 1px rule ~25px, then ~20px to the chart title.
  - Scrollytelling to article: ~100px of empty ground between the controls (y≈308) and the standfirst (y≈465) on 1440-08.
  - Species illustrations run edge to edge with ~0px padding. The audio button sits ~20px below the art, and text starts ~40px below that.

- **Motion and interaction.**
  - Hero: the h1, kicker and byline sit on a full-bleed illustrated world map. Small bird illustrations (petrel, nightingale, 2 swans) float over the map. At 1440-02 the map is still in its illustrated state as the page scrolls.
  - Scrollytelling: a sticky full-bleed world map with narration boxes 480px wide (x=480–960) scrolling over it. Each box swaps the base layer, and all states are triggered by scroll:
    - 1440-03: shaded relief, "45 species".
    - 1440-04: vegetation.
    - 1440-05: temperature.
    - 1440-06: relief, with all tracks except the petrel removed.
    - 1440-07: "three birds".
  - Time animation: the tracks animate through the months. A control row at x≈205–440, y≈767 has prev, pause with a circular plum progress ring, next, and the month label. The month advances between frames (JANUARY 1440-03, FEBRUARY 1440-04, MARCH 1440-05/06, APRIL 1440-07/08), so it autoplays while scrolling. Loop duration: not observable in stills.
  - Audio: three "Listen to a …" play buttons, one per species (1440-09, 1440-14, 1440-18).
  - Wind-field map: animated wind streaks with a play button (1440-13). The storm-chase animation duration is not observable in stills.
  - Without interaction: the story survives. The three route maps, the habitat map and the swan wintering map are static and fully annotated, and they carry the claim. The motion is atmosphere, not evidence.

- **Mobile.**
  - Hero (390-01): the h1 wraps to 4 boxed lines at 30px/42px. The byline wraps to 3 lines of plum bold. The kicker drops "Birds". The dateline, Share pill and guardian.org logo stack at left over the map.
  - Text: body stays 17px/24px, in a 350px column at 44 characters per line (measured).
  - Scrollytelling map: it is cropped and panned, not scaled down.
    - 390-03 shows Africa and Europe, 390-05 the Americas, and 390-07 the North Atlantic, so the full-globe view is cut.
    - Narration boxes go full width, ~370px with 10px margins, and the ramp legends stay inside them (390-05).
    - The month control sits at y≈765 and is partly hidden behind the ad bar (390-03 to 390-07).
  - Route maps: they go to the full 370–390px width. Annotations are kept and repositioned, with callouts still on leaders (390-11, 390-17, 390-23).
  - Habitat map (390-20):
    - The map is cropped to its western third, so Mali, Ghana, Nigeria and most country labels are cut; only "Senegal" and "The Gambia" remain.
    - The legend stacks into 2 rows ("British birds", then the gradient).
    - The scale bar moves to top right and becomes 300 km.
    - The callout moves below the dots on a vertical leader ~70px long.
  - Swan wintering map (390-25): temperature labels break onto 2 lines ("4.32C / (39.8F)").
  - Left-rail photos and captions drop inline at full width, ~370px (390-11, 390-17).
  - Illustrations are cropped to the viewport height (390-09, 390-15, 390-21).
  - Species headers stack as Latin name, common name, then fact rows (390-15, 390-21).
  - Nothing is rotated.

- **The steal.** Use Marlo's, the nightingale's and Mary's annotated route pattern: each waypoint is a bold short date over one plain-language line, attached to its mark by a short straight leader. The start gets a small flag glyph, the end a checkered flag, and method labels (e.g. "Approximate route") sit in italic grey on the line itself instead of in a legend.
  - Where: the **"One thread through the record"** 5-step teen-safety timeline.
  - Dates: each step becomes a bold Archivo date ("Mar 2019") over a one-line Newsreader description, joined to its node by a 24–40px ink leader.
  - Ends: step 1 gets a flag glyph and step 5 an end marker.
  - Evidence: carry the grade on the connecting segment in italic grey ("court finding", "reported"), matching the "How we know" labels, so no separate legend is needed.
  - Accent: cobalt stays the single accent for the "thread".

- **Capture notes.**
  - This recapture has no privacy banner.
  - At 390, frames 390-03 onward carry a sticky ad bar ~75px tall (y≈770–844, "Advertisement" plus a banner), which hides the bottom ~9% of each of those frames. 390-01 has no ad.
  - The folder holds 390-01..34, not 37 as briefed.
  - 1440-24 to 1440-28 and 390-29 to 390-34 are the support ask, related-story carousels, "Most viewed" and the footer, not the article.

- **Frames cited.**
  - 1440 hero and scrollytelling map: 1440-01, 1440-02, 1440-03, 1440-04, 1440-05, 1440-06, 1440-07, 1440-08
  - 1440 petrel: 1440-09 (audio), 1440-10 (Marlo's route), 1440-11 (left-rail photo), 1440-12, 1440-13 (wind map)
  - 1440 nightingale: 1440-14 (species header), 1440-15 (route), 1440-16, 1440-17 (habitat map)
  - 1440 swan: 1440-18 (species header), 1440-19 (Mary's route), 1440-20, 1440-21 (wintering map)
  - 1440 end matter: 1440-22 (methodology), 1440-23 (citations), 1440-24 to 1440-28 (support ask and page chrome)
  - 390 (odd frames): 390-01, 390-03, 390-05, 390-07, 390-09, 390-11, 390-13, 390-15, 390-17, 390-19, 390-21, 390-23, 390-25, 390-27, 390-29, 390-31, 390-33
  - 390 (extra): 390-20

---

## Dithering - Part 1 (visualrambling.space, year not visible in frames)

- **Claim.** "And that's how dithering works in a nutshell: it replicates shades with fewer colors, which are strategically placed to maintain the original look." That sentence is the recap in 1440-38 (step 38 of 47).
  - It first appears as "That's what dithering does: it simulates more color variations than what are actually used" in 1440-06 (step 6).
  - The mechanism is proven in two passes:
    - Naive thresholding fails in 1440-16 to 1440-19.
    - The threshold map works, in 1440-27 to 1440-37. 1440-37 reads "The variations in shades are now replaced by variations in black/white pixel density", and 390-36 reads "The image now uses only two colors, but its overall appearance is preserved."

- **Grid.** There is no text grid. The page is one full-viewport canvas (measured canvas width 1440 at desktop and 390 at phone, page height 900 / 844, so it never scrolls), with a single caption layer on top.
  - Caption measure at desktop: the box spans about 730px (x 355 to 1085) at about 24px sans. The longest observed line is 68 characters ("I've always been fascinated by the dithering effect. It has a unique", 1440-02). Estimate at 0.5em is about 61 chars, observed 60 to 68.
  - Caption measure at phone: about 326px wide at about 15px. Observed lines run 36 to 42 chars ("I was even more amazed when I learned", 390-03).
  - The graphic is always wider than the text:
    - Main dither square: 810x810px (x 315 to 1125, y 45 to 855), 1.11x the caption width. It is used for the intro (1440-07 to -11) and again for the whole closing run (1440-38 to -47 and the end card).
    - Statue photo: 540x540px, 0.74x.
    - Thresholded or dithered statue: 720x720px (x 360 to 1080).
    - Threshold map: 8x8 grid about 345px wide in perspective (x 548 to 892, 1440-27).
    - Zoom states (1440-04, -05, -22, -23, -25) run full bleed at 1440x900, about 1.97x the caption width.
  - Fixed chrome: masthead "visualrambling.space" at x 32 and "about" at x 1346, y about 40. Progress rail of 47 ticks from x 440 to 1000 at y 884 (tick count measured from pixels). The final tick is reached at 1440-47.

- **Type.** This is a sans-and-mono piece with no serif in view. The measured h1 is "Dithering - Part 1", Times 32px, 700, rgb(0,0,0). The visible title is not live type: it is drawn in the canvas as a skewed monospace graphic, "DITHERING" at about 110px cap height, over a "Part 1 - Introduction" label at about 26px (1440-01).
  - Roles:
    - Geometric sans (DM Sans-like) for captions: about 24px desktop, 400, line-height about 34px. Italic is used for emphasis ("(spoiler: there are many ways!)" in 1440-41, "error diffusion" in 390-42).
    - Monospace for UI hints (about 20px), for in-graphic labels ("Brightness Level: 0.25", about 22px, 1440-31 and -33) and for the end card (about 22px desktop, about 13px phone, 1440-48 and 390-48).
    - Sans for the masthead (about 24px).
  - Ratios (estimated): title graphic : caption : chart label is about 110 : 24 : 22, or 4.6 : 1 : 0.92. The measured h1 : caption is 32 : 24, or 1.33 : 1.
  - Weights: 400 for captions, about 500 to 700 for the mono title and labels, and bold italic mono for "visualrambling.space" on the end card.
  - Numerals: measured "normal". The values seen ("0", "1", "0.25", "2") are all lining; "0.25" is in monospace.
  - measure.json has body = null and chartLabels = null, so all text is either canvas or overlay spans.

- **Color.**
  - Ground: sampled #F9C939 (yellow). The measured body bg rgb(34,34,34) (#222222) sits under the canvas and never shows.
  - Hues carrying meaning: 0. The data is pure black #000000 versus white #FFFFFF, the "two available colors".
  - Mid-greys appear only where grey value is the data: the source photo (1440-12, -13), the point clouds (1440-14, -15), the threshold-map cells (8 grey levels plus black and white, 1440-27) and the extruded pixel columns (1440-29, -31).
  - The context color is the yellow ground #F9C939, not a grey. It works as "empty / not a pixel": in 1440-17, -21 and -22 yellow shows through where pixels have been lifted out of the plane.
  - Captions are white on #000000 knock-out boxes. Other yellow-on-image uses:
    - Sparse yellow "+" sparkles mark pixels being flipped (1440-22, -23).
    - Thin yellow scan lines mark the sweep line in 1440-35 and -37, as the photo is converted row by row.

- **Annotation.**
  - Each state has one caption of 1 to 3 lines, and that caption is the only annotation in 40 of 47 states.
  - Direct in-graphic labels appear in only 4 states, none with leader lines:
    - 1440-16: two boxed mono callouts with arrow glyphs, "lighter pixels <- become white" (white box) and "darker pixels -> become black" (black box).
    - 1440-27: one perspective title, "THRESHOLD MAP", set on the plane of the grid.
    - 1440-31 and -33: one perspective label, "Brightness Level: 0.25", sitting on the grey input block and then on the resulting black-and-white 4x4 pattern.
  - There is no legend anywhere. Black and white and the 0-to-1 scale are defined in the captions ("from 0 (darkest) to 1 (brightest)", 1440-27).

- **Density.**
  - Intro and closing dither squares: 810px at about 5 to 6px per cell, so about 135x135, roughly 18,000 cells.
  - Point cloud (1440-14): estimated 20,000 to 40,000 points.
  - Threshold map: 8x8, 64 cells (1440-27). The output pattern at brightness 0.25 is a 4x4 block of cubes plus about 12 black columns, about 16 to 28 marks (1440-33).
  - End card: black text panel about 720x540px (x 360 to 1080, y 180 to 720) over the 810px dither square, leaving about 45px of pattern visible on each side (1440-48).
  - Whitespace, desktop: statue photo has 180px above, 360px left and right, and a 25px gap to the caption. The main square has a 45px top and bottom margin to the viewport. The threshold map has about 150px of yellow above and a 50px gap to the caption (1440-27).
  - Whitespace, phone: the square has a 20px side gutter (x 20 to 370) and about 250px of yellow above and below.

- **Motion and interaction.**
  - Trigger: click or tap the right half to advance and the left half to go back; arrow keys also work (hints in 1440-01 to -03). There is no scroll. There are 47 discrete states, 1 per tick, followed by an end card.
  - Sequence of states (camera moves in 3D throughout):
    - 1-11: skewed plane, zoom into the pixels (1440-04, -05), then pull back to a flat square.
    - 12-13: switch to the photo.
    - 14-16: pixels explode into a 3D point cloud sorted by brightness, then split in two.
    - 17-19: collapse into a black/white plane.
    - 20-26: re-dither, with a zoom in at 1440-25.
    - 27-33: 3D threshold-map demo, with a grey pixel column compared against 8x8 cells and extruded into a cube pattern.
    - 35-37: the photo plane is converted by a sweeping fold, with the dithered upper half and the greyscale lower half visible at the same time.
    - 38-47: a flat 810px square cycles through new dithered photos (statue, then a church in 1440-40 and -47, a landscape in 1440-41 and -43, crowd and trees in 1440-45).
    - After step 47 comes the end card.
  - The end card's background keeps cycling on its own. Frames 1440-48 to -54 show 5 distinct backgrounds behind an unchanged text panel, and clicks after step 47 do not advance, so frames 48 to 90 repeat those 5 states.
  - The intro dither pattern also animates by itself (1440-07 vs -11).
  - Durations are not observable in stills. Two captures caught transitions midway, which suggests tweens of non-trivial length plus a caption fade:
    - 390-19: the caption says "fully black or white" while the image is still greyscale.
    - 1440-39 and 390-39: the caption is ghosted at about 20% opacity during a crossfade.
  - Without interaction the story does not survive: only state 1 renders, and the text exists only as per-state captions.

- **Mobile.**
  - Same canvas at 390x844. The main square shrinks to 350x350 (x 20 to 370).
  - Caption width drops to about 326px at about 15px, so captions wrap to 2 to 4 lines instead of 1 to 3.
  - Caption position shifts:
    - It stays centered over the square wherever the square is flat (390-03 to -11, -42, -45).
    - It drops below the graphic (y about 700 to 750) in the photo, point-cloud and threshold sections (390-13 to -36), leaving about 120 to 150px of yellow between graphic and caption.
  - The nav hint wraps to 2 lines (390-01).
  - Some graphics are cropped rather than scaled:
    - The skewed statue plane bleeds off the left edge (390-19, -25).
    - The 3D threshold columns bleed off the right and bottom (390-29).
    - The folded conversion plane fills about 330px (390-36).
  - End card: the text panel grows to 328x416px (x 31 to 359, y 214 to 630), wider than the 350px square behind it, which is hidden except for 10px slivers at each side. Text drops to about 13px mono, and the links wrap to 2 lines (390-48, -54).
  - No text is cut. 47 ticks show on both widths, and the end card is reached at 390-48.

- **The steal.** A persistent graphic stays in place while one knock-out caption (white on solid ink, one sentence) changes per step. Steps are driven by click-right, click-left or arrow keys, a tick rail shows position, and the story ends with a one-sentence recap step before the credits ("And that's how dithering works in a nutshell ...", 1440-38).
  - Where: "One thread through the record", the 5-step teen-safety timeline.
  - How:
    - Keep one stage (the timeline strip) fixed.
    - Each step highlights one event and swaps a single-sentence caption in a cobalt or ink knock-out box.
    - Add a 6th recap step that restates the thread in one sentence before handing off to "The record".
    - Use a 6-tick rail directly under the stage.
  - Guard: unlike visualrambling, render all captions as an ordered list in HTML, and upgrade to the stepper only with JS, so the thread still reads with scripts off and in print.

- **Frames cited.**
  - Desktop: 1440-01 to 1440-25 (all), 1440-27, 1440-29, 1440-31, 1440-33, 1440-35, 1440-37, 1440-38, 1440-39, 1440-40, 1440-41, 1440-43, 1440-45, 1440-47, 1440-48, 1440-49, 1440-50, 1440-53, 1440-54.
  - Phone: 390-01, -03, -05, -07, -09, -11, -13, -15, -17, -19, -21, -23, -25, -27, -29, -30, -33, -36, -39, -42, -45, -48, -54.
  - Frames 49 to 90 at both widths are checksum duplicates of the end-card states in frames 48 to 54 and were not reviewed beyond 54.

---

## Dicing an Onion, the Mathematically Optimal Way (The Pudding, 2025)

- **Claim.** "When making 10 cuts into a 10-layer onion, the smallest standard deviation (29.5%) occurs when making radial cuts aimed 96% of the onion's radius below the cutting surface!" It is stated as a bold standalone paragraph in 1440-10 (390-09 on phone).
  - The setup comes earlier: the question "what's the best way to dice it?" in 1440-02, and Kenji's "~60% below" claim in 1440-07.
  - The results table in 1440-13 generalizes the answer across 19,320 combinations.

- **Grid.** One centered column, measured at 576px (x 432 to 1008).
  - Body is 22px Tiempos Text, so the estimate at 0.5em is about 52 chars per line. Observed lines run 49 to 53 chars ("Why? Because tens of millions of people are curious" = 51, 1440-01).
  - Every chart and figure is exactly column width: 6 svgs and 6 figures all measured 576px, a 1.00x ratio to the text. The same is true for the control panels, the results table (1440-13) and the embedded slide (1440-09).
  - Only the onion-letter word images break out:
    - "ONION" is about 793px (x 325 to 1118), 1.38x.
    - "VERTICAL" is about 738px, 1.28x.
    - "TECHNIQUE" is about 892px (x 275 to 1167), 1.55x.
    - "RADIAL" is about 548px, 0.95x.
  - A Kenji avatar (about 85px) hangs in the left margin at x 320 to 405, outside the column (1440-01, 1440-15).
  - The page frame is an about 18px inset border with a magenta-to-yellow gradient (edge sample #E2A2C5) on all four sides.

- **Type.**
  - Families:
    - Serif body: Tiempos Text, 22px, 400, line-height 30.8px (1.4).
    - Sans display: Atlas Grotesk, h1 54px, 700 italic, line-height 60.75px.
    - Sans chart and table labels: Atlas Grotesk, 10px, 400.
  - Ratios:
    - Headline : body : chart label is 54 : 22 : 10, or 5.4 : 2.2 : 1.
    - Section heads ("Optimal techniques", "Insights") are about 30px bold sans, a 1.36 ratio to body.
    - Control labels (EXPLODE, CUTS (VERTICAL), STD DEV) are about 12px, 700, all caps sans.
    - Table body is about 14px sans.
  - Weights: 400 and 700. Sans bold is also used inline inside serif paragraphs for key phrases ("vertical cuts", "a higher standard deviation means more piece size variation.").
  - Numerals: measured "normal". Figures look lining in both families. Table values are right-aligned (29.5% to 43.5%, 1440-13), but tabular figures are not confirmed from stills.

- **Color.**
  - Ground: #FFF8EF (measured rgb(255,248,239)). Text and hairlines are plum #4B0C2F (measured rgb(75,12,47), 139 svg uses).
  - Hues carrying meaning: 2 in the diagrams, plus 1 on a badge.
    - Teal #2B7679 (31 svg uses) marks the focal piece set.
    - Magenta #891555 (19 uses) marks the contrasting piece set.
    - The badge purple is #723A80 (sampled) and appears only on the "FAIR UNIFORMITY" badge (1440-06).
  - The context color is not grey. The onion layers and cut lines are 1px plum #4B0C2F hairlines, with the cut lines dotted.
  - Highlight yellow #FDE9A8 (sampled) is used for slider tracks, toggle backgrounds, the collapsible note boxes and the table icon chips. Link underlines are a saturated yellow (about #F5C400, estimated).
  - The accent teal means "the pieces the sentence is talking about" and also "Excellent uniformity" (badge, 1440-04, -08, -10). Magenta is the second group ("along the bottom", "near the center").

- **Annotation.**
  - The diagrams carry 0 text labels. Annotation is done by color-keyed prose: the paragraph below each diagram uses bold phrases colored to match the marks. "near the center line" is teal and "along the bottom" is magenta (1440-04), then "near the outside" teal and "near the center" magenta (1440-06). That is 1 to 2 keyed phrases per chart.
  - The interactive panels add 3 to 7 direct readouts above each chart, all labeled directly with no legend:
    - A rating badge.
    - "STD DEV: 37.3%".
    - Slider values ("10", "~96%").
    - A cut-type segmented control.
  - The results table (1440-13) has 10 rows, each with a 36px yellow icon chip showing the cut geometry and its depth label (10px, "96%") inside the chip.

- **Density.**
  - Base diagram: 10 concentric half-rings, 1 baseline and 10 dotted cut lines, so 21 marks. The highlighted states add about 10 teal and 9 magenta piece outlines (about 40 marks, 1440-03). The radial-below state has about 21 marks plus 8 teal pieces and 1 origin dot (1440-08).
  - Results table: 10 rows x 4 columns = 40 cells.
  - Whitespace around the diagrams at desktop:
    - About 100px from the end of the text to the top ring (y 434 to 538, 1440-02).
    - About 80px from the baseline to the next text line (y 768 to 848).
    - About 60px from a control panel to the diagram (1440-05).
    - About 70px between the text and a letter image (1440-03).

- **Motion and interaction.**
  - Controls change the stills: sliders for cuts, layers and horizontal cuts (0 to 10), target height (about -96%), a vertical/radial toggle, and an "explode" toggle. The badge text and color switch between EXCELLENT (teal) and FAIR (#723A80), and STD DEV updates (37.3%, 57.7%, 34.5%, 29.5% across 1440-05, -06, -08, -10).
  - The number-of-layers dropdown re-sorts the table, and the column headers show sort arrows (1440-13).
  - Two collapsible yellow notes ("A note on the standard deviation", "How do you find the size of an onion piece?") are closed by default.
  - Scrolling alone triggers nothing that is visible in stills. Transition durations are not observable in stills.
  - The story survives without interaction: every key number is repeated in the prose (57.7% vs 37.3% in 1440-07; 34.5% in 1440-09; 29.5% in 1440-10), and every diagram renders a meaningful default state.

- **Mobile.**
  - The column narrows to 326px with body text at 18px (line-height 25.2px), about 36 chars estimated and 31 to 36 observed. The h1 is 38px.
  - Diagrams scale to 326px, still 1.00x the text.
  - Letter images shrink and stop breaking out: "ONION" about 230px, "VERTICAL" about 286px, "TECHNIQUE" about 343px, which is nearly full bleed.
  - Control panels restack into rows (390-09, -11):
    - "EXPLODE" on its own row.
    - Badge and STD DEV on the next row.
    - Sliders full width.
    - CUT TYPE moves below the sliders.
  - In the table, the method text wraps to 2 lines ("radial, / 69% depth", 390-13).
  - The footer goes from 3 columns to 2 (390-15).
  - Nothing is cut, and the gradient border frame is kept at about 16px.

- **The steal.** Color-keyed prose instead of a legend: the bold phrase in the sentence is set in exactly the fill color of the marks it describes, and the chart itself carries no labels.
  - Where: "Penalties and revenue", the square grid plus tally.
  - How: the sentence under the grid reads, for example, "**penalties paid** fill N squares; **revenue** fills the rest". The "penalties paid" phrase is bold Archivo in the same cobalt as the penalty squares, and "revenue" is in the ink or grey used for revenue squares.
  - Result: the legend is removed and the reader's eye links sentence to marks.
  - Secondary use: the same device can key the entries-per-year strip in "The record" to the active topic filter's color.

- **Frames cited.**
  - Desktop: 1440-01, 1440-02, 1440-03, 1440-04, 1440-05, 1440-06, 1440-07, 1440-08, 1440-09, 1440-10, 1440-11, 1440-12, 1440-13, 1440-14, 1440-15, 1440-16.
  - Phone: 390-01, 390-03, 390-05, 390-07, 390-09, 390-11, 390-13, 390-15.

---

## The Legislative Network Behind State Trans Laws (C.J. Robinson, 2025)

Capture note: this is a full-length recapture.
- Desktop: 35 frames × about 777px covers the whole 27,200px page, ending on the methodology and credits (1440-35).
- Phone: 39 frames covers the whole 33,423px page, ending in the credits (390-39).
- The phone frames were re-spaced in the recapture, so every 390 citation below refers to the new set.
- The year "2025" comes from the body text ("By August 2025", 1440-11; "In January 2025", 1440-29). No dateline was visible.
- The credits identify it as a master's project from Columbia Journalism School (1440-35).

- **Claim.** State anti-trans bills reuse text written by lobbying groups and spread through networks of state legislators.
  - First stated in text at 1440-08: "A new data-driven analysis reveals how state transgender policies utilize language sourced from lobbying groups and disseminated throughout state legislator networks".
  - The images show it first: at 1440-05, the Montana HB 112 page has green highlights where it matches Idaho HB 500.
  - Restated as the conclusion at 1440-34: "With the same language showing up across states, these efforts have become part of a political playbook reshaping the debate over civil rights and states' power."
  - The method is given at 1440-34/35: over 10,000 Legiscan bills, compared as 5-word phrases, with bills under 10% similarity filtered out.

- **Grid.**
  - 1 centred column. The body column is 700px wide (x 370–1070). At 19.2px Georgia that is 78 characters per line measured (700 / (19.2 × 0.5) ≈ 73 estimated).
  - Scrolly caption cards are 518px wide (x 461–979), with about 19px padding and about 16px text, so about 60 characters per line.
  - Graphics mostly stay at or inside the text width:
    - Datawrapper bar chart: 700px (1440-11).
    - Choropleth pair: two maps of about 310px each side by side inside the 700px column (x ≈ 390–690 and 740–1055, 1440-32/33).
    - Bill pages: 328px wide at rest (0.47× text width, 1440-01), zooming to 600px (0.86×, 1440-03).
    - Two-page comparison: 672px (x 384–1056, 1440-25).
    - Thumbnail wall: 8 per row, each thumbnail 79×104px with a 10px gap, so 702px per row (x 369–1071, 1440-08, 1440-27).
  - The only breakout wider than the text is the two-document spread at x 212–1056 = 844px (1440-24) to 994px (1440-21). That is 1.2–1.42× the text width.

- **Type.**
  - Serif body: Georgia 19.2px, weight 400, 28.8px line height (1.5). Italic is used only in the credits (1440-35).
  - Grotesque sans for display:
    - Headline: about 60px bold, 2 lines (1440-09/10).
    - Section heads: about 30px bold ("SAFE Act", 1440-14; "Fairness in Women's Sports Act", 1440-29; "Representative Republications", 1440-32; "Methodology", 1440-34).
    - Year tags on documents: about 20px bold grey.
  - Courier New monospace inside the facsimile bills: 12px, weight 200 measured, about 8–9px in the thumbnail state.
  - Charts use Datawrapper's sans. Bar chart title about 18px bold, subtitle about 16px, ticks 12px grey (1440-11). The map chart title is about 18px bold over 2 lines, with a 16px subtitle and about 13px bold map labels (1440-32).
  - Ratio headline : body : chart label ≈ 60 : 19.2 : 12 = 5 : 1.6 : 1.
  - Weights: 200 (facsimile), 400 body, 700 display.
  - Numerals: Georgia's old-style figures in body text ("533", "2025", "10,000" drop below the baseline, 1440-11, 1440-34). Chart axes use lining figures.

- **Color.**
  - Two hues carry meaning.
    - Green, about #228B22 (estimated), means "shares language with the model bill". It is used for matched-text highlights, thumbnail fill density, caption key-word chips ("Repeated phrases", "same language"), the bar fills, and the map fill for states that introduced a copy (1440-32/33). Body links use the same green (1440-29 to 1440-35), so links and data share one colour.
    - Yellow, about #FFFF00 (estimated), highlights only the bill's short title (1440-03).
  - Context colours:
    - scrolly stage: about #F0F0F0
    - facsimile paper: about #F8F7F5
    - text sections: #FFFFFF
    - unmatched bill text: dimmed to about #BBBBBB (1440-04)
    - non-adopting states on the maps: about #F0F0F0 with white borders (1440-33)
    - year and state tags: about #999–#AAA
    - section divider: 1px rule, about #999, 700px wide (1440-34/35)
  - Single accent: green = "copied or adopted". The captions use it as the legend.
  - Body text is rgb(0,0,0) (measured).

- **Annotation.**
  - Bar chart (1440-11):
    - 1 annotation: a 4-line note joined by a hand-drawn curved arrow to the 2023 bar.
    - No value labels, 3 gridlines, no legend (single series).
    - Source line underneath.
  - Maps (1440-32/33):
    - 0 annotations and no legend.
    - Each map is titled directly with the bill name in quotes. Green equals "introduced", explained only by the subtitle "Legislation introduced in the United States utilizing language found in model bills".
  - Documents:
    - 0 leader lines. The labelling is colour on the marks themselves: green highlight on matched spans, yellow on the title.
    - Each thumbnail carries a 2-letter state code (about 30px grey) and a year (about 16px bold grey).
    - The caption's green chip does the legend's job (1440-05, 1440-18).

- **Density.**
  - Bar chart: 6 bars, 3 gridlines, 1 note.
  - Maps: 2 × about 50 states. About 16 states green on the Fairness map and about 22 on the SAFE map (1440-33, counted by eye).
  - Two-page comparison: about 12–15 highlighted spans (1440-05). Missouri lines 96–117 show 4 green blocks (1440-24/25).
  - Walls:
    - Fairness wall: 15 thumbnails (8 + 7, 1440-08).
    - SAFE wall: 8 + 8 + 8 + 7 = 31 thumbnails in view (1440-27), then a trailing row of 5 dated 2024–2025 (OK, RI, RI, RI, DE, 1440-28). The caption says "18 other states" (1440-26).
  - Whitespace:
    - about 60px between the last paragraph and the chart title (1440-11)
    - about 68px after the source line (1440-12)
    - about 40px between the maps and the next paragraph (1440-33)
    - about 112px between the document and the caption card on the stage (1440-01)
    - about 250px of empty stage above the walls (1440-06, 1440-27)
    - about 100px above and below the rule before "Methodology" (1440-34)

- **Motion and interaction.**
  - Scroll-driven, with no clicks. White caption cards scroll over a sticky document stage. The sequence:
    - 1440-01→03: Idaho zooms from 328 to 600px and the title turns yellow.
    - 1440-04→05: Montana fades in and its matches turn green.
    - 1440-06→08: pages shrink and 15 later bills fan in from the right, opacity ramping from about 20% to 100%.
    - 1440-16→25: SAFE Act. Arkansas 2021 is paired with Missouri 2023, then South Carolina 2024. The Missouri or South Carolina page scrolls internally and its matches light green in passes. At 1440-25 a new bolded "aids or abets" clause appears next to the caption "This iteration added a section incriminating anyone who 'aids or abets'".
    - 1440-26→28: the SAFE wall, 31 or more thumbnails staggered in with fading.
    - 1440-28: the stage hands off to the text section at a hard edge (grey stage ends at y 185).
  - Everything after 1440-28 is static prose, plus 1 static map pair.
  - Transition durations: not observable in stills.
  - Near-empty transition frames: 1440-15, 390-18.
  - Survival without interaction: the argument, the adoption count and the maps survive as prose and static graphics. The phrase-level evidence exists only as scroll states.

- **Mobile.**
  - Body column 371px at 19.2px Georgia, 43 characters per line measured.
  - Caption cards 348px wide (x 21–369).
  - Bill pages stay 328px wide. The zoomed state is wider than the viewport and clips both edges (390-03).
  - The first comparison is a staggered overlap, with Idaho top-left and Montana lower-right and both partly off-screen (390-05). Later comparisons stack vertically, 2021 above 2023 or 2024, each about 328px wide (390-21, 390-24).
  - Walls drop from 8 to 4 per row at the same 79px thumbnail size (390-08, 390-09, 390-27).
  - The headline wraps to 3+ lines at about 52px ("The / Legislative / Network", 390-09).
  - Bar chart: the desktop's curved-arrow note becomes a circled numeral "1" with a short arrow at the 2023 bar, and the note text moves to a numbered footnote under the axis (390-12). This is the one annotation adaptation in the piece.
  - The two maps stack vertically at about 340px each (390-35/36).
  - Nothing is cut and nothing is rotated.

- **The steal.** Put the primary document on screen and highlight the one matched phrase in the accent. Set the caption's key word on a chip of the same colour so the caption doubles as the legend (1440-05, 1440-18, 390-21 "same language").
  - Where: **"One thread through the record"**, the 5-step teen-safety timeline. Each step gets a cropped source page (internal document, filing or ruling) at about 328px, with its load-bearing sentence highlighted in cobalt and the same phrase on a cobalt chip in the caption.
  - On phone, stack the source crop above the caption, as 390-21/24 do.
  - Secondary: the phone bar-chart treatment (circled numeral at the mark, note moved to a footnote, 390-12) suits the **"The record"** entries-per-year strip. A single numbered marker on a peak year avoids a long label colliding with narrow bars at 390px.

- **Frames cited.** 1440-01, 1440-02, 1440-03, 1440-04, 1440-05, 1440-06, 1440-07, 1440-08, 1440-09, 1440-10, 1440-11, 1440-12, 1440-13, 1440-14, 1440-15, 1440-16, 1440-17, 1440-18, 1440-19, 1440-20, 1440-21, 1440-22, 1440-23, 1440-24, 1440-25, 1440-26, 1440-27, 1440-28, 1440-29, 1440-30, 1440-31, 1440-32, 1440-33, 1440-34, 1440-35; 390-03, 390-05, 390-06, 390-08, 390-09, 390-12, 390-15, 390-18, 390-21, 390-24, 390-27, 390-30, 390-33, 390-35, 390-36, 390-39.

---

## 30 minutes with a stranger (The Pudding, 2025)

Capture note: this is a full-length recapture.
- Desktop: 90 frames cover the whole 69,151px page. The timestamp ruler, set at 30px per conversation-second (1440-02), runs from 0m 0s to 30m 0s (1440-89). After it come the closing essay and the site footer (1440-90).
- Phone: 90 frames of the 70,596px page end at 28m 20s (390-90). The phone set does not include the last ~2 minutes of the ruler or the closing essay; the desktop frames cover those.
- The year comes from the URL (/2025/06/); no dateline was visible.

- **Claim.** People expect a conversation with a stranger to go badly, but by the end of a 30-minute call most feel better. Across all 1,700 conversations, average positive feeling rose from 6.1 before the call to 7.4 at the end, on a 0–10 scale. The rise held regardless of the partners' age gap, race or politics.
  - The expectation is set up by the essay: trust fell from 47% to 34% (1440-25), and commuters predicted a "negative experience" (390-28).
  - Start of the call: many felt "the same or worse" (1440-23).
  - Middle: "a huge portion" felt "better" (1440-41).
  - The conclusion is first stated at 1440-69: "By the end of the call, the large majority of people said they felt [better] than when the conversation began."
  - Quantified at 1440-71 (bars 6.1 / 6.2 / 6.9 / 7.4 for Before / Begin / Middle / End).
  - Broken down by subgroup at 1440-73 (age gap), 1440-75 (race) and 1440-77 (politics).
  - The earlier essay has the research precedent: the 2014 follow-up found "almost no rejections, pleasant conversations, and an overall positive experience" (1440-56).
  - The closing essay ends on the author's subway anecdote and "I want people to do the same for me—regardless of whether I'm a stranger or not" (1440-89/90).

- **Grid.**
  - 1 centred column for text.
    - Captions sit in black boxes 400px wide (x 520–920) with about 21px padding.
    - Caption body text: 17px Tiempos, 358px wide measured, 34 characters per line measured (≈ 42 estimated).
    - Essay text runs about 575px wide (x 430–1006, 1440-25, 1440-56), which is about 60–68 characters per line at 17px (≈ 68 estimated).
  - Charts sit inside the 400px caption box, with a plot about 350px wide (1440-71 to 1440-77). The line chart runs in the essay column at about 575px (1440-25).
  - The tile layouts break far out of the column:
    - sorted grid: 18 columns × about 68px on a 76px pitch = 1361px, 3.4× the caption width (1440-16)
    - paired grid: 9 pairs = 1339px (1440-24, 1440-69)
    - zoomed paired grid: tiles about 90px, 7 pairs visible, overflowing both edges (1440-39, 1440-66, 1440-87)
    - clusters: about 1340px (1440-73 to 1440-77)
  - The 60px ruler is pinned to the right edge (x 1380–1440) throughout. The two-shot is 2 × 110px = 222px, centred.

- **Type.**
  - Serif: Tiempos Text.
    - title: 18px, weight 500, 25.2px line height
    - body and captions: 17px, weight 400, 25px line height
    - legend heads: about 18px bold
  - Monospace for everything data-like:
    - timestamps: about 12px; the active one bold white at about 14px
    - speech bubbles: about 14px
    - chart titles: about 18–20px bold ("To what extent do you feel positive feelings or negative feelings?", 1440-71)
    - axis labels: about 11–12px
    - tile labels: about 11px bold white ("Age: 28", "White", "Very Con", 1440-73/75/77)
    - value labels: about 14px (1440-71)
  - Ratio headline : body : chart label ≈ 18 : 17 : 11 = 1.6 : 1.5 : 1. The headline is almost body size.
  - Weights: 400, 500, 700.
  - Numerals: lining in Tiempos. Monospace is fixed-width, so the timestamps and value labels align.

- **Color.**
  - Page background: #201126. Body text: #CEBCD4. Captions sit on #000000.
  - The same ~200 tiles are re-encoded by one variable at a time. Hues carrying meaning per state:
    - age: 6
    - race: 5
    - education: 5
    - politics: 5, diverging
    - mood: 3 (Worse / Same / Better)
  - Maximum simultaneous hues: 6.
  - Mood palette (1440-69):
    - Worse: pink, about #FF6FB5
    - Same: grey-mauve, about #7A6A72. This is the context colour.
    - Better: yellow, about #E8E27A
  - The resolution is carried by colour alone. The paired grid goes from mostly grey and pink (1440-23/24), to mixed (1440-41), to mostly yellow (1440-69: estimated 60–70% of visible tiles).
  - The Kate/Dawn two-shot tiles turn from lilac (1440-61) to yellow (1440-79 onward), so the recurring pair visibly "ends better".
  - Before/Begin/Middle/End bars use a 4-step pink → salmon → orange → yellow ramp that matches the mood palette (1440-71).
  - Beginning-vs-end paired bars use violet, about #B57BDB, against yellow (1440-73 to 1440-77).
  - Single accent: bright violet, about #C45CE6. It marks the speaking-avatar border (4px), links, and the "47%" endpoint.

- **Annotation.**
  - Legends sit inside the caption box: 3–6 swatches of about 14px with monospace labels.
  - Captions double as legends: key words sit on chips filled with the swatch colour ("the [same] or [worse]", 1440-23; "feeling [better]", 1440-41, 1440-69).
  - The sort direction of the clusters is keyed in the sentence with boxed arrow glyphs: "[↑] smaller age gaps at the top, [↓] bigger age gaps at the bottom" (1440-73, 1440-75, 1440-77).
  - Tiles in the clusters carry direct white monospace labels for the sort variable (1440-73/75/77), so no legend is needed for the categories.
  - Bar charts:
    - 1440-71: direct value labels above each bar, coloured to match the bar (6.1, 6.2, 6.9, 7.4).
    - Subgroup charts: 2-item inline legend (Beginning / End), no value labels, 4–5 gridlines labelled 0–8, source line in monospace.
    - 1440-77: an arrow axis label ("Same politics → Very different politics").
  - Line chart (1440-25, 390-27/28): endpoint labels only (47%, 34%).
  - Two-shot: names are labelled directly on the tiles. Bubbles attach to the speaking tile with a 10px pointer.

- **Density.**
  - Tile layouts:
    - sorted grid: 18 × 11 = 198 tiles (1440-16)
    - paired grid: 9 × 11 pairs = 198 tiles (1440-24, 1440-69, 1440-88)
    - zoomed paired grid: about 7 × 9 pairs visible (1440-39)
    - clusters: about 200 tiles with about 150 direct labels (1440-73/75/77)
  - Bar charts: 4 bars (1440-71), 10 bars in 5 pairs (1440-73), 4 bars in 2 pairs (1440-75), 12 bars in 6 pairs (1440-77).
  - Line chart: about 35 vertices.
  - Two-shot: 2 tiles plus 1 bubble in about 390px of empty background above and below.
  - Whitespace:
    - essay blocks start about 100–140px below the last tile row (1440-25, 1440-89)
    - about 60px between the essay and the line-chart title
    - caption boxes overlay the tiles with 0px separation

- **Motion and interaction.**
  - The ruler advances 30px per conversation-second as you scroll, from 0m 0s (1440-02) to 30m 0s (1440-89). The 1,800 seconds take about 54,000px of the 69,151px page.
  - Two-shot:
    - The speaker border toggles with each turn and the bubble text is replaced.
    - Four pairs recur: Kate/Dawn, Paige/Raúl, Eve/Dave, Hank/Faith. Their scenes are interleaved as the ruler advances (1440-29 to 1440-61, 1440-65, 1440-79 to 1440-86).
    - At 1440-55/57 the two-shot stays fixed while an essay section scrolls under the ruler, which pauses at 19m 30s (1440-56).
  - Wall states cycle for the full ~200 tiles: scatter → sorted → clusters by demographic → mood grid at the start (1440-23/24) → zoomed mood grid at 13m (1440-39) → "better" at the middle (1440-41) → "nearing the end" (1440-66) → the end (1440-69) → bar chart (1440-71) → clusters sorted by age gap, race and politics with the paired-bar charts (1440-73/75/77) → final two-shot goodbyes (1440-79 to 1440-86) → the grid fades out at 30m 0s (1440-88/89).
  - Tile recolouring between states is what shows the result.
  - Triggers: scroll position. "Click on a person to explore" (1440-10) was not exercised.
  - Transition durations: not observable in stills.
  - Survival without interaction: yes. Every finding is stated in caption text and the bar charts are static inside the captions.

- **Mobile.**
  - Caption boxes span 371px (x 10–381). Body text stays 17px, 34 characters per line.
  - Charts inside captions widen to about 320px (390-81).
  - Layout changes:
    - the ruler stays pinned right (x 335–385)
    - sorted grid: 9 columns
    - paired grid: 4 pairs per row at about 28px tiles (390-75, 390-84)
    - clusters: compressed into one column, about 260px wide (390-78)
    - two-shot tiles: about 85px, with bubbles 250px wide (390-54, 390-57, 390-66)
  - Nothing is rotated.
  - Transition frames on phone show collisions that desktop does not:
    - a tile clipped at x < 0 (390-36)
    - Kate's tile half off the right edge on top of the ruler (390-51)
    - the Paige/Raúl two-shot and its bubble cut off at the left edge, with the bubble text truncated (390-69)
    - timestamps overprinting the zoomed grid tiles (390-42, 390-72)
    - a mid-zoom two-shot with about 55px tiles and about 9px bubble text (390-45)

- **The steal.** Let colour state carry the conclusion. Keep one fixed set of marks and recolour it between states, naming the state in the sentence on a matching chip ("felt [better]", 1440-69). Here the same 198 tiles move from grey and pink to mostly yellow. Pair it with a caption-sized chart that uses the same palette and labels its values directly in the bar colour (1440-71).
  - Where: **"The record"** ledger. Draw the 51 entries as 51 squares in the entries-per-year strip.
    - Step 1: all ink-grey, sorted by year.
    - Step 2: recolour only the entries backed by a court finding in cobalt. The sentence above names the count on a cobalt chip, e.g. "[N] rest on a court finding", matching the **"How we know"** labels.
    - A 3–4 bar caption chart per evidence label, with values in bar colour, replaces the separate filter legend.

- **Frames cited.** 1440-01 to 1440-25 (all), 1440-27, 1440-29, 1440-31, 1440-33, 1440-35, 1440-37, 1440-39, 1440-41, 1440-43, 1440-45, 1440-47, 1440-49, 1440-51, 1440-53, 1440-55, 1440-56, 1440-57, 1440-59, 1440-61, 1440-63, 1440-65, 1440-66, 1440-67, 1440-69, 1440-71, 1440-73, 1440-75, 1440-77, 1440-79, 1440-81, 1440-83, 1440-84, 1440-85, 1440-86, 1440-87, 1440-88, 1440-89, 1440-90; 390-01, 390-03, 390-05, 390-07, 390-09, 390-11, 390-13, 390-15, 390-17, 390-19, 390-21, 390-23, 390-25, 390-26, 390-27, 390-28, 390-29, 390-30, 390-33, 390-36, 390-39, 390-42, 390-45, 390-48, 390-51, 390-54, 390-57, 390-60, 390-63, 390-66, 390-69, 390-72, 390-75, 390-78, 390-81, 390-84, 390-87, 390-90.

---

## When You Will Die (FlowingData, 2025)

- **Claim.** Running the yearly survival odds as a simulation gives a more useful answer than average life expectancy: the simulated ages of death settle on a median and a mode (in the desktop capture, "Ready? You will die at 94" for a 2-year-old female). The method is stated first in the dek on 1440-01 ("run simulations to get a more accurate and more meaningful answer than average life expectancy"). The number itself arrives on 1440-08 (desktop) and 390-11 (phone, which gives 74 for a 31-year-old).

- **Grid.** The container is 1090px wide (x = 175 to 1265 at 1440; measured h1/graphic width 1090). Prose sits in a 670px left column (measured). At 18px serif and about 9px per character that is about 74 characters per line; the measured value is 79, and a counted line on 1440-01 has about 75. There are three ways graphics leave the text column:
  1. Full container width. The "Time of Death" chart is 1090px (1.63x the text width) on 1440-01. It then turns into a sticky condensed bar about 114px tall and 1120px wide (x = 160 to 1280, drop shadow) that holds the controls and a mini curve. It is pinned on every frame from 1440-02 to 1440-10.
  2. Right-hand second column. There are two 530px SVGs (0.79x the text width) at x = 735 to 1265, with a 40px gutter. On 1440-04 the "Female Mortality" chart sits beside a 520px text block. On 1440-05 the histogram sits at x = 209 to 685 (about 476px) in the left column and the annotation text sits in the right column.
  3. Staggered one-line typography. On 1440-09, "You only... / ...get... / ...one life. / You are here." steps diagonally from x = 255 to x = 1140 across the full 1090px.
  - A grey sidebar box (390px, x = 875 to 1265) on 1440-10 is the only other right-column element.
  - Layout is effectively 2 columns (670 + 40 gutter + 380/530).

- **Type.**
  - Families:
    - Mercury SSm (serif): h1, section heads, body.
    - Inconsolata (monospace): all chart labels, axis titles in caps ("PROBABILITY OF LIVING ANOTHER YEAR", "YEARS OLD"), the speed buttons ("Live Fast / Live Slow / Sloth Mode") and inline formula text ("100% - chances of dying in a year", 1440-02).
  - No sans-serif.
  - Sizes (measured): h1 40px/52px, weight 700. Body 18px/28.8px, weight 400, #111111. Chart labels 14px/26px, weight 400, #111111.
  - Ratios: headline:body:chart label = 40:18:14 = 2.22:1:0.78.
  - Section heads (h2, for example "Where the Data Comes From") are an estimated 32px, weight 700, #333333. Chart titles (for example "Female Mortality, Pushing Down") are an estimated 26px, weight 700.
  - The control sentence "I am female / male and 2 years old" is an estimated 26px, weight 700. The unselected option ("male") is light grey, about #CCCCCC.
  - Weights: 400 and 700, plus italic 400 for defined terms ("period life expectancy", "median", "mode").
  - Numerals: font-variant-numeric is "normal" (measured). The serif shows old-style-looking proportional figures in body text, and chart numerals are monospaced (Inconsolata).

- **Color.**
  - One hue carries meaning: teal rgb(101,192,186) = #65C0BA. It is the survival curve, the histogram bars and the live-number highlight.
  - A 10-step ramp runs from grey to teal for time: rgb(224,224,224) #E0E0E0 through rgb(213,221,221), (202,218,217) ... to rgb(123,198,193), then the full #65C0BA. It encodes 1910 (grey) through 2025 (full teal) on the 1440-04 mortality chart.
  - Context greys: #E8E8E8 (the "YOU ARE HERE" band, the shaded past-age region on the curve) and #E0E0E0. Ink is #000000 for the balls, axes and dropped-ball ticks, and #111111 for text.
  - Live, simulation-driven numbers in prose (99.98%, 102, 94, 92) get a pale teal background, estimated #CFE9E6. Numbers taken from user input ("female", "2024", "3") get a pale grey background, estimated #E8E8E8. So the tint shows whether a number was computed or chosen.
  - Links are dark red (estimated #7A1020, 1440-10).
  - The single accent (teal) means a simulated life or its outcome.

- **Annotation.**
  - Time of Death curve (1440-01): 2 annotations. The y-axis title is set in caps mono. A grey shaded band plus a vertical rule marks the user's current age. No legend.
  - Female Mortality chart (1440-04): 3 annotations. The curves are labelled directly at their ends ("In 2025" at the top right, "In 1910" at mid-right, both in 14px mono). A vertical line with a teal dot marker shows the user's age. No legend; the grey-to-teal ramp is explained in the adjacent prose.
  - Histogram (1440-05 to 1440-07): 3 annotations.
    - A "YOU ARE HERE" band across the top at the current age.
    - A dashed horizontal rule labelled "Median age of death, 94 years", right-aligned above the rule.
    - An x-axis title that carries the running N: "PROBABILITY OF DYING (3 SIMS.)".
  - A side note in the right column ("While death is unlikely at earlier ages, the chances are not zero.", 1440-05) is placed next to the part of the chart it describes, with a 1px rule above it.
  - Everything is labelled directly. The table on 1440-07 fills only the cell with the largest share (100%) in teal.

- **Density.**
  - Main curve: 1 path plus 1 to 3 balls visible at a time, plus dropped-ball ticks on the baseline (0 on 1440-02, 3 by 1440-08).
  - Mortality chart: 13 curves (1910 to 2020 by decade plus 2025) over 0 to 119 years. That is about 1,500 vertices, 8 gridlines and 12 x ticks.
  - Histogram: one bar per simulated age. In the capture that is 2 bars (1440-06) to 5 bars (390-09), because only 1 to 5 simulations had run. The y axis runs 0 to 120 with minor ticks every year (121 ticks).
  - Table: 6 rows by 2 columns.
  - Whitespace:
    - Control row to chart title: 1440-01 has a rule at y ≈ 671, 30px above the title.
    - Chart bottom to next paragraph: 1440-04, axis label at y ≈ 632, next paragraph at y ≈ 705, a gap of about 73px.
    - Paragraph to h2: about 80px.
    - Histogram axis to "After 3 simulations..." h2: 1440-07, about 85px.
    - Paragraph spacing: about 22px (a 28.8px line height with about 22px between paragraphs).

- **Motion and interaction.**
  - Balls roll along the survival curve continuously. The ball x-position differs in every frame: about 425 (1440-01), 670 (-02), 922 (-03), 366 and 1031 (-04), 618 (-05). When a life ends the ball drops to the baseline and leaves a permanent tick (ticks at x ≈ 807, 1031, 1103 accumulate from 1440-04 to 1440-08).
  - Each finished life updates:
    - the simulation counter in prose (1 on -02, 2 on -05, 3 on -07);
    - the histogram bars and median line;
    - the median/mode numbers in text;
    - the table.
  - Triggers are a timer, which runs automatically with no scroll trigger, plus user controls: female/male toggle, age slider, and a speed toggle "Live Fast / Live Slow / Sloth Mode" ("Live Slow" active in every frame).
  - The controls and mini chart stay pinned in a sticky header from 1440-02 onward.
  - Animation speed and duration per simulated life are not observable in stills.
  - Does the story survive without interaction? Partly. The prose explains the method fully. But the headline answer ("You will die at 94") is a live value that depends on how many simulations have run: the capture shows 94 on desktop and 74 on phone after 3 to 5 sims. The histogram is nearly empty in the stills (1440-05 has 0 bars, 1440-06 has 2), so a static or no-JS reader gets a thin chart.

- **Mobile.**
  - Single column 367px wide (measured) with 12px gutters. Body stays 18px/28.8px at about 39 characters per line (measured). h1 stays 40px and wraps to 2 lines ("When You Will / Die", 390-01).
  - The sticky bar grows to about 128px. The speed buttons wrap to a second row under "I am female male and 31 years old", and the mini curve runs full width (390-03).
  - The two 530px side-column charts become 367px full-width blocks stacked after their prose (390-06, Female Mortality). The histogram becomes full width with the x axis rescaled to 0 to 20% (390-09).
  - The right-column side note and the membership box stack inline (390-15).
  - Nothing is cut or rotated. The staggered "You only... get... one life" line survives in narrower form (390-13).
  - The phone capture defaulted to age 31 and the desktop capture to age 2, so the numbers differ between sizes.

- **The steal.** Take the sticky condensed control bar, which carries a live mini chart and the reader's current filter state while the prose scrolls under it (1440-02 to 1440-10, 390-03 to 390-15). Put it on "The record" ledger of 51 entries: when the reader scrolls past the ledger header, collapse the entries-per-year strip and the topic/evidence filter chips into one pinned bar about 96px tall at 1440 (two rows at 390). Add a running count set in the Archivo tabular numerals ("Showing 14 of 51") and a cobalt tick on the strip that marks the year of the entry currently in view, the way the dropped-ball ticks accumulate on FlowingData's baseline. A second, smaller steal is the tint coding for numbers in prose: computed/record counts get a pale cobalt background and reader-chosen filter values get a grey one. It could apply to the "Penalties and revenue" tally sentence.

- **Frames cited.** 1440-01, 1440-02, 1440-03, 1440-04, 1440-05, 1440-06, 1440-07, 1440-08, 1440-09, 1440-10; 390-01, 390-03, 390-05, 390-06, 390-07, 390-09, 390-11, 390-13, 390-15.

---

## Measles vaccines save millions of lives each year (Our World in Data, 2025)

- **Claim.** Measles vaccination is the most life-saving childhood vaccine in use: about 93.7 million lives saved from 1974 to 2024, compared with 27.9 million for the next vaccine (tetanus). The h1 states it on 1440-01 ("Measles vaccines save millions of lives each year"), with the dek "Measles once killed millions every year. Vaccines changed this...". It is quantified in the prose on 1440-02 ("prevented over ninety million deaths... likely the most life-saving ones currently in use") and proved by the first chart on the same frame (Measles bar at 93.7 million). It is restated twice near the end: in the prose after the cumulative chart ("94 million lives have been saved", 1440-10), and in an unheaded 4-paragraph recap set off by a 1px rule, 628px wide ("preventing an estimated 90 million deaths in the last fifty years — more than any other childhood vaccine used today", 1440-11).

- **Grid.**
  - One centred text column 628px wide (measured; x = 406 to 1034 at 1440). Body is Lato 18px sans-serif; at about 9px per character that is about 70 characters per line, and a counted line on 1440-01 has 74.
  - Chart figures break out to 845px (measured figure width; SVG 841px), x = 298 to 1143. That is 1.35x the text width, extending about 108px past the text on each side, inside a 1px light-grey frame (estimated #E7E7E7).
  - The heatmap figure (1440-04, 1440-05) is the same 845px, followed by a full-width 845px "Download image or data" bar (1440-05).
  - The header card (title, dek, byline) is 845px wide and sits on a gold band (estimated #F7C020) that is 200px tall (1440-01).
  - Sidenotes use a right margin column about 300px wide (x = 1058 to 1360), set in italic 14px with a 1px left rule (1440-03, "Measles immune globulin...").
  - The bar chart and the coverage chart frames are each about 573px tall at 1440 (bar chart y = 284 to 857 on 1440-02; coverage chart y = 315 to 888 on 1440-08). The deaths area chart spans 2 frames (1440-06 top at y = 465, 1440-07 bottom at y = 273).
  - Two fixed 40x40px navy squares (newsletter, feedback; x = 1336 to 1424, y = 844 to 884) sit in the bottom-right corner of every desktop frame, outside the 845px column.
  - So there are 3 widths: 628 text, 845 figure, and about 300 margin.
  - Endnotes (1440-13) switch to 2 columns of about 400px each inside the 845px width, on an off-white background (estimated #F9F8F4).

- **Type.**
  - Families:
    - Playfair Display (serif display): h1, h2, chart titles.
    - Lato (sans-serif): body, dek, chart labels, UI.
    - A monospace face for the citation blocks (1440-14).
  - Desktop sizes (measured): h1 Playfair 40px/48px, weight 600, rgb(29,61,99) = #1D3D63. Body Lato 18px/27.9px, weight 400, #1D3D63. Chart labels Lato 12px/16px, weight 400, rgb(91,91,91) = #5B5B5B.
  - Ratio headline:body:chart label = 40:18:12 = 3.33:1:0.67.
  - Other desktop sizes (estimated): h2 about 34px Playfair, weight 600 (1440-03). Chart titles about 20px Playfair, weight 400 (1440-02). Dek about 24px Lato, weight 400, in a muted blue estimated #5B7A9E (1440-01).
  - Phone sizes (measured): h1 20px, weight 700; body 16px/24px; labels 10.5px. The phone ratio is 20:16:10.5 = 1.25:1:0.66, so the headline shrinks to half while body drops only 2px.
  - Weights: 400, 600 and 700, plus italic 400 for sidenotes and the chart credit line (1440-05).
  - Numerals: font-variant-numeric is "normal" (measured). Lato's default lining proportional figures in both text and axes. Values are written out with units ("93.7 million", "554,000").

- **Color.**
  - Text is navy #1D3D63 everywhere, not black. Footnote markers are red (estimated #D42B21).
  - Single accent: rgb(151,0,70) = #970046 (measured, used 49 to 50 times). It always means measles.
    - Bar chart (1440-02): the Measles bar is #970046 (it renders about #A8336B), and the other 13 bars are a muted blue, rgb(76,106,156) #4C6A9C, estimated to render about #6D87B3.
    - Coverage chart (1440-08): the "Measles, first dose (MCV1)" line and its label are #970046. The other 9 vaccine lines are grey.
  - Context grey: rgb(221,221,221) #DDDDDD (the most common SVG colour, 284 uses) for gridlines and the de-emphasised lines on the coverage chart. Other greys: #A8A8A8/#999999 for the grey lines as rendered, #5B5B5B for labels, #767676 for secondary labels.
  - Heatmap (1440-04/05): a sequential yellow-green-blue ramp on a log scale (0 to 1,000 cases per 100,000), from pale yellow (estimated #FFFFCC) to navy (estimated #08306B). Event rules are a separate hot magenta (estimated #E0147A).
  - Stacked area charts (1440-06/07, 1440-10) use a 6-colour categorical palette for WHO regions (magenta, ochre, rust, green, blue, purple). So the accent is not reserved on those charts: the African Region area is also a magenta.
  - Hues carrying meaning per chart: 2 on the bar chart (measles vs other), 2 on the coverage line (measles vs grey), 6 on the areas, 1 ramp plus 1 event colour on the heatmap.

- **Annotation.**
  - Bar chart (1440-02): 14 bars. Every bar has a direct category label on the left (right-aligned, 12px) and a direct value label at the bar end ("93.7 million" ... "2,000"). No legend, 0 callouts.
  - Heatmap (1440-04/05): 4 dated event callouts:
    - "1963: The first measles vaccine is developed by John Enders"
    - "1971: ... MMR vaccine ..."
    - "1980: It becomes mandatory ..."
    - "1989: Widespread outbreaks lead officials to recommend a second dose ..."
    - Each is attached by a full-height 2px vertical magenta rule at its year, with an elbow leader from the text to the rule.
    - Callout text is about 11px, with the year in bold magenta.
    - The colour scale sits in a vertical legend bar on the right ("Reported cases of measles per 100,000 (log scale)", ticks 0, 1, 3, 10, 30, 100, 300, 1,000; the bar is about 26px wide and about 440px tall, spanning 1440-04 to 1440-05).
    - Rows carry 51 state labels (Alabama to Wyoming, about 7px), and the x axis runs 1929 to 2022.
  - Deaths by region area (1440-06/07): 6 direct region labels at the right end with elbow leader lines, colour-matched text plus "(WHO)" and an info icon. No legend box.
  - Coverage line (1440-08): 10 direct series labels at the right with elbow leaders. Only the measles label is in the accent colour; the other 9 are grey, estimated #AAAAAA.
  - Cumulative area (1440-10): 6 direct labels at the right, stacked in the same order as the bands.
  - Every chart ends with the same 3-line footer at about 12 to 13px: a bold "Data source:" plus the citation (for example "Shattock et al. (2024)...", "IHME, Global Burden of Disease (2025)", "WHO & UNICEF (2024)"), an underlined "Learn more about this data" link, and "OurWorldInData.org/vaccination | CC BY". Action buttons sit right-aligned on the same baseline (1440-02, 1440-07, 1440-08, 1440-10). Interactive charts also carry Table/Chart tabs at the top left and an "Our World in Data" logo tag, about 65x36px, at the top right.
  - The heatmap footer instead has 2 lines: "Data source: Project Tycho (2018); Centers for Disease Control and Prevention (1959–2022)", and "Licensed under CC-BY by the author Fiona Spooner", right-aligned. Under the frame are a full-width download bar and a centred italic 14px credit ("inspired by Tynan DeBold and Dov Friedman's data visualizations in the Wall Street Journal... Scripts... on GitHub", 1440-05).

- **Density.**
  - Mark counts per chart:
    - Bar chart: 14 bars plus 28 labels.
    - Heatmap: 51 rows x 94 years, about 4,800 cells (each about 7x8px at 1440, plot width about 690px). Some cells are hatched for missing data (Alaska, Hawaii, Mississippi, Nevada, Kansas).
    - Deaths area: 6 bands x 44 years (1980 to 2023).
    - Coverage: 10 lines, with about 44 dot markers on the measles line and about 300 dots in total.
    - Cumulative area: 6 bands x 51 years.
  - Whitespace:
    - Paragraph end to figure frame: about 40px (1440-02, text ends y ≈ 245, figure top y ≈ 284; 1440-06, 418 to 465 ≈ 47px).
    - Figure frame end to next paragraph: about 60px (1440-07, 273 to 335; 1440-09, 123 to 185; 1440-10, 611 to 673).
    - Newsletter box (628px wide, grey #F2F2F2 estimated, 1440-07) to the next h2: about 50px.
    - Inside the figure frame: 16px padding.
    - Before an h2: about 45px (1440-05, credit text ends y ≈ 455, h2 top y ≈ 510).

- **Motion and interaction.**
  - No scroll-driven changes. Every frame is a static scroll position, and chart states are identical at each size.
  - Interactive affordances visible:
    - Table / Bar / Area / Line tabs.
    - A play button plus a range slider from 1980 to 2023 (1440-07, 1440-08, 1440-09) or 1974 to 2024 (1440-10). The slider has 2 visible states. On 1440-08 the thumbs are filled slate blue (estimated #5B7A9E) and the years sit in bordered boxes. On 1440-07 and 1440-09 the thumbs are grey (estimated #A0A0A0) and the years are unboxed. The capture seems to have caught a hover or active state on 1440-08; what triggers it is not observable in stills.
    - "Edit countries and regions" / "Change country or region".
    - Download, Share, Enter full-screen, "Explore the data" (1440-03, 1440-07, 1440-09).
  - The heatmap is a static image with a download button (1440-05).
  - Hover, tooltip and play-animation behaviour and their durations are not observable in stills.
  - The story survives fully without interaction: every default view carries the point, and the prose restates each chart's number.
  - The 2 fixed corner buttons (newsletter, feedback) stay on screen on every desktop frame (1440-01 to 1440-16); they are absent on the phone.

- **Mobile.**
  - Text column 358px (measured; 16px gutters), about 45 characters per line (counted 47 on 390-01).
  - Figures widen to 374px (8px gutters) or 390px full-bleed (measured). So graphics break out further than text on the phone, by 8 to 16px per side.
  - The h1 drops from 40px to 20px (measured) and wraps to 2 lines (390-01). The byline and cite/reuse links stack vertically instead of sitting in 2 columns.
  - Chart titles wrap to 3 lines (390-02). The deaths chart's "1980 to 2023" drops to its own line under the title (390-07).
  - Bar labels wrap to 2 lines ("Whooping cough / (Pertussis)"). All 14 bars are kept, and the bar chart runs about 470px tall (390-02 to 390-03).
  - Button text is shortened ("Edit countries and regions" becomes "Edit countries"; "Change country or region" becomes "Change country"). The Table/Chart tabs and the Download/Share/Full-screen buttons become icon-only, about 32px squares; only "Explore the data" keeps its label (390-03, 390-07, 390-09, 390-11).
  - X-axis ticks are thinned: 1980, 2000, 2010, 2023 (1990 is dropped) on the deaths and coverage charts (390-07, 390-09), and 1974, 1990, 2024 on the cumulative chart (390-11). The slider's end years move into bordered boxes (390-07).
  - Source footers wrap to 3 or 4 lines, with "CC BY" on its own line beside the icon buttons (390-03, 390-09).
  - On the coverage chart the label column takes about 45% of the width, squeezing the plot to about 150px (x ≈ 58 to 207), and the labels wrap to 2 lines (390-09). The cumulative area chart is squeezed the same way, with a plot about 150px wide and 6 labels in the right half (390-11).
  - The heatmap is not re-laid out. The static image is scaled to about 358px, so state labels and callouts render at about 3px and are unreadable (390-05). This is the one place the layout fails. The download bar (358px) and the centred italic credit, now 4 lines, follow below it (390-05).
  - The margin sidenote folds inline, directly under its paragraph, with an "Aside:" prefix in italic, estimated at 13px (390-04). There is no left rule.
  - The newsletter box stacks its red Subscribe button under the text (390-08). The endnotes collapse to 1 column (390-15, 390-17). The footer link columns go from 4 to 2, and the social icons spread across the full width (390-21, 390-22).

- **The steal.** Take the heatmap's dated event rules: full-height accent rules at specific years, each with a short "Year: what happened" callout (bold year in the accent, about 11px text, elbow leader) laid over a dense per-year grid of marks (1440-04). Put it on the entries-per-year strip in "The record". Overlay the 5 steps of "One thread through the record" (the teen-safety timeline) as thin cobalt vertical rules, each with a two-line callout above the strip in Archivo 11 to 12px ("2021: ..."). The ledger's volume and the teen-safety thread then share one axis, and the timeline stops being a separate island. Keep the per-year bars in ink or grey so cobalt means only "a step in the thread", the way OWID reserves #970046 for measles across charts. On the phone, do not scale the strip as an image (OWID's failure on 390-05). Drop the callout text to numbered markers 1 to 5 above the rules and key them to the timeline cards below.

- **Frames cited.** From the recapture with optional cookies rejected: 1440-01, 1440-02, 1440-03, 1440-04, 1440-05, 1440-06, 1440-07, 1440-08, 1440-09, 1440-10, 1440-11, 1440-12, 1440-13, 1440-14, 1440-15, 1440-16; 390-01, 390-02, 390-03, 390-04, 390-05, 390-07, 390-08, 390-09, 390-11, 390-12, 390-13, 390-15, 390-17, 390-19, 390-21, 390-22. Capture note: no cookie banner and no blank frames. The only overlays are the 2 fixed 40x40px desktop corner buttons (x = 1336 to 1424, y = 844 to 884), which cover no chart content. 1440-08 shows a slider hover/active state that the other slider frames do not.

---


---

# Synthesis: five patterns that recur in the strongest pieces

These are the patterns that show up across most of the ten pieces and are absent or broken in the weakest moments of the others. Each is stated as a rule this site can follow, with the evidence and the counter-examples.

## 1. The title states the finding, with its number, and every graphic carries its own method and source

- **Evidence.** iStories titles each chart card with the claim and the number ("More than 18 million paper ballot votes … may have been fabricated") and puts a method subtitle and a dated source line inside the same card. OWID's h1 is the finding ("Measles vaccines save millions of lives each year"), and every chart ends in the same three-line footer: data source, "learn more", licence. The Straits Times ends each static map with a source line 20px below it. Onions states its answer as one bold standalone sentence with the number (29.5%). The Stranger piece names its result in the caption ("felt [better]") and then quantifies it (6.1 to 7.4).
- **Counter-examples.** Robinson's maps are titled with bill names, not findings. FlowingData's headline answer is a live number that changes per visit.
- **Rule here.** Every graphic gets a headline sentence that states what it shows, with the number in it, plus a one-line method note and a source line, so a screenshot of the graphic alone keeps its claim, method and source together.

## 2. The legend lives in the sentence or on the marks, not in a box

- **Evidence.** Seven of ten pieces key their colors in the text or label marks directly:
  - The Straits Times sets "rice", "sugar" and "permanent deforestation" on filled chips matching the map colors, in caption cards and chart titles alike.
  - Onions colors the bold phrase in the paragraph to match the marks and puts no labels on the diagram.
  - Robinson and the Stranger piece put the key word on a chip of the data color ("same language", "[worse]", "[better]").
  - The Guardian sets a track glyph inline as a word ("~ Desertas petrel") and labels the swan clusters by year directly.
  - Reuters and OWID label every bar and line end directly, with no legend.
- **Counter-examples.** iStories falls back to swatch legends on three charts; they are its hardest charts to read.
- **Rule here.** Direct-label marks wherever they fit. Where color carries a category, name it in the adjacent sentence on a chip or colored phrase that uses exactly the mark color. No separate legend boxes.

## 3. One accent means one thing, everywhere; everything else is context

- **Evidence.**
  - OWID reserves #970046 for measles across every chart and greys the other nine vaccines.
  - The Straits Times keeps yellow for "cleared" from one satellite polygon up to the national deforestation map.
  - Robinson's green means "copied from the model bill" in highlights, chips, bars and maps.
  - FlowingData's teal means "a simulated life".
  - The Guardian's plum means "a tracked bird".
- **Counter-examples.** Reuters spreads meaning across about nine hues and has no single accent. iStories keeps its brand red off the data, which works, but its multi-line chart uses five unrelated hues. Both are harder to read than the single-accent pieces.
- **Rule here.** Give each accent exactly one meaning across the whole site; the baseline critique found this site's cobalt currently means hero ground, credits ground, data marks, links, dates and figures at once. Everything else is ink or a context grey that clears 3:1 for graphical marks.

## 4. A 60 to 78 character text column, graphics at a few fixed breakout widths, notes snapped back to the column

- **Measured text columns** (character counts counted from lines, estimates in brackets):

  | Piece | Column | Characters per line |
  |---|---|---|
  | Reuters | 660px | 72 to 76 |
  | The Straits Times | 700px | 80 to 87 |
  | Robinson | 700px | 78 |
  | The Guardian | 620px | 73 |
  | OWID | 628px | 74 |
  | FlowingData | 670px | about 75 |
  | Onions | 576px | 49 to 53 |
- **Breakout widths.** Each piece uses a small set of them, repeated:
  - Reuters: 926, 1308 and 1440px.
  - OWID: 845px everywhere.
  - The Straits Times: 700, 1302 and 1408px, plus full bleed.
  - The Guardian: 620px maps with partial and full breakouts.
- **Notes and sources snap back.** Reuters and The Straits Times always return notes and sources to the text column, even under a full-bleed graphic.
- **Counter-example.** iStories runs body text at about 100 characters per line in an 864px column and never breaks out; it reads as a report, not a story.
- **Rule here.** A single text measure of about 60 to 75 characters, two or three named breakout widths used consistently, and source lines aligned to the text column.

## 5. The default state carries the story; motion re-encodes the same marks; phones get a re-layout, not a shrink

- **Survives without interaction.** Reuters, The Straits Times, OWID, Onions, the Stranger piece and The Guardian all hold up with no interaction: every number the argument needs is printed or restated in prose, and controls add depth.
  - Onions repeats every key standard deviation in the text.
  - OWID restates each chart's number in the following paragraph.
- **Motion moves or recolors the same marks.** When motion is used it keeps object constancy: the Stranger piece recolors the same ~198 tiles from grey and pink to yellow, and The Straits Times reframes one map through three scales with a moving locator box. Robinson zooms and highlights the same documents.
- **Counter-examples.** Dithering fails without clicks: only its first state renders. FlowingData's headline number depends on how many simulations ran before you looked.
- **Phones.** The strongest pieces re-lay out instead of scaling:
  - Reuters rotates bars into columns and keeps 4 of 5 map callouts.
  - Robinson turns a long annotation into a numbered marker plus footnote at 390px.
  - The Straits Times coarsens scale bars.
  - OWID's one failure is the heatmap scaled as an image to 358px, with 3px labels.
- **Rule here.** Every graphic is complete in its static end state, which is also what reduced motion shows. Motion is allowed only to show a change in the data on marks that keep their identity. At 390px, graphics are redrawn for the width, with annotations turned into numbered markers where needed.

---

## Where the steals compete

The teardowns proposed more than one steal for the same section. These choices belong in DESIGN.md:

- **"One thread through the record" (teen-safety timeline).** Four proposals:
  - Reuters: converging diamonds into one labeled endpoint.
  - The Guardian: annotated waypoints with the evidence grade on each segment.
  - Robinson: a cropped source document with the key sentence highlighted.
  - Dithering: a fixed stage with a one-sentence stepper.

  Robinson's is the only one that shows evidence rather than describing it, which fits a site whose product is sourcing. The Guardian's segment labels fit the evidence-label system. The Dithering stepper conflicts with pattern 5 unless it enhances a plain list.
- **"The record" entries-per-year strip.** Four proposals:
  - OWID: dated event rules marking the five thread steps on the strip.
  - The Straits Times: legend chips that double as filter buttons.
  - The Stranger piece: 51 squares recolored by evidence label.
  - FlowingData: a sticky condensed filter bar with a live mini strip.

  OWID's event rules and the Stranger recolor are compatible, and both answer the baseline critique's point that the strip currently has no finding.
- **"Penalties and revenue."** iStories' self-contained evidence card and Onions' color-keyed sentence are compatible and together address the baseline critique's top finding (the grid states no claim and hides its breakdown behind hover).

## Conflicts with the brief's bans

- **Warm grounds.** Reuters (#F4F3E4), Onions (#FFF8EF) and The Guardian (#F8F3F0) all use cream or off-white grounds, which the brief bans. Their techniques transfer; their grounds don't.
- **Eyebrow kickers.** The Guardian's hero has a kicker box above the h1 ("The age of extinction"). The brief bans eyebrow kickers.
- **Burgundy accents.** OWID's measles accent (#970046) and Robinson's links sharing the data green both show "one accent, one meaning". On this site the accent is cobalt, and burgundy is banned.
