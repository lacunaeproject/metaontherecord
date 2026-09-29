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
