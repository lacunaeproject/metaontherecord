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
