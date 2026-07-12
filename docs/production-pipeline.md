# Production Pipeline

## Tooling

- **Affinity Designer 2** — illustration/diagram work: the pipeline spine,
  stage boxes, branching sub-elements, any custom iconography.
- **Affinity Publisher 2** — page layout: places Designer artwork as a
  linked resource, handles the multi-tier typography hierarchy, bleed,
  margins, and final print/PDF export.
- Chosen over Adobe InDesign/Illustrator after direct experience: Adobe's
  interaction model didn't transfer well from years of prior QuarkXPress
  (v3-v5) experience and felt effectively unusable for complex work despite
  effort invested. Affinity 2 (one-time purchase) was adopted as a working
  replacement; proficiency is solid in Publisher 2 and Designer 2, not
  expert-level.

## Structure-first workflow

Because charts in this line have hard topology constraints (see
`versioning-scheme.md` and the "concept + platform" matched-pair rule in
`project-brief.md`), layouts are **generated programmatically before any
manual design work begins**:

1. A small Python script (see `charts/rag-concepts/v1/generate_spine.py` for
   the reference implementation) defines stage positions, weights, spine
   coordinates, and grid units as plain variables/config.
2. Running it produces an exact, reproducible SVG scaffold at true print
   dimensions (points, where 1in = 72pt), including bleed/trim/safe-margin
   guides on clearly labeled layers.
3. That SVG is imported into Affinity Designer as a starting layer. From
   here on, everything is normal hand-editable vector work — move nodes,
   resize boxes, add illustration, adjust curves. The script is a precise
   starting position, not a constraint on subsequent manual editing.
4. To produce a topology-matched companion poster (e.g. the AWS platform
   poster to a concept poster), or a new major version, re-run the same
   generator with updated config (e.g. swapped branch labels, adjusted
   stage list) rather than rebuilding the grid by hand — this is what
   guarantees the topology-matching constraint holds exactly, rather than
   approximately by eye.

Why this matters: the topology-matching and slow-structural-change
constraints are exactly the kind of precision requirement that's error-prone
to maintain by hand across multiple binary Affinity files, but trivial to
guarantee in a script whose diffs are plain text and reviewable in git.

## Letter proofs (draft printing at any stage)

`shared/scripts/letter_proof.py` turns any draft artifact — the generated
SVG scaffold, or a PNG/JPEG exported from Affinity — into an 11x8.5in
landscape PDF, scaled to fit, with a header noting source file, date, and
reduction scale (~29% of full poster size):

```
python3 shared/scripts/letter_proof.py charts/<slug>/v1/<draft>.svg
```

Writes `<draft>_letterproof.pdf` next to the input and opens it in
Preview for printing. Layout/proportion check only — fine print will be
tiny at this reduction and desktop printer color is not calibrated.
Requires Google Chrome (used headlessly for PDF rendering). Proof PDFs
are derived artifacts and gitignored.

## Print specifications (current defaults)

- Canvas: 36in x 24in, landscape orientation.
- Bleed: 0.125in on all sides.
- Safe margin: 0.75in inset from trim edge for live content.
- Header zone: ~2.25in (title, logo, version badge).
- Footer zone: ~2.5in (failure-modes / at-a-glance strip, where applicable).

These are the scaffold generator's current defaults
(`charts/rag-concepts/v1/generate_spine.py`) and should be re-validated
against whichever specific POD vendor is chosen — vendor template
requirements (bleed, DPI, color profile, sometimes vendor-specific
templates) are not yet locked in this repo.

## Export target for POD posters (researched July 2026)

Current Printful and Printify guidelines both want the same artifact, so
the vendor decision does not block design or export work:

- **Flat raster file, not a press-ready PDF.** PNG preferred (JPEG
  acceptable). Printify caps PNG/JPEG uploads at 100 MB — a flat-color
  poster PNG compresses comfortably under that.
- **Color: sRGB IEC61966-2.1, not CMYK.** Vendors convert to their
  printers' space themselves and explicitly ask for sRGB submissions.
  Set up the Affinity Designer/Publisher documents as RGB/8 with the
  sRGB IEC61966-2.1 profile from the start — do not design in CMYK.
- **Resolution: 300 DPI at full physical size.** 36x24in trim =
  10800x7200 px; 10875x7275 px if the bleed is included in the upload.
  (300 is the recommended/ideal; Printful accepts down to 75 for paper
  products, but there's no reason to go below 300 here.)
- **Bleed: 0.125in**, matching the scaffold generator's default. Check
  the chosen product's "File guidelines" tab at upload time for whether
  the uploaded file should include the bleed area or be trim-size with
  full-bleed artwork — Affinity Publisher can export either from the
  same document.
- **Candidate product**: Printful "Enhanced Matte Paper Poster" carries
  24x36in (printed landscape for this line) and is printed in-house with
  consistent quality; Printify is cheaper but routes to third-party print
  providers with more variable output. Same file works for both.

## Open questions

- **POD vendor** — Printful vs Printify vs other. Non-blocking for design
  work (see export target above); decide at listing time based on
  price/quality of an ordered proof.
- **Spot color implementation** — the version badge is currently a flat
  placeholder fill (`#FF00A6`) in the generated SVG, explicitly named
  `VERSION_BADGE_spotcolor` so it's unmistakable which object to convert to
  a true spot-color swatch once the house palette (see
  `brand-guidelines.md`) is finalized.
