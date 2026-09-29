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
