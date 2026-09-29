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
