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

## Open questions

- **POD vendor** — Printful vs Printify vs other. Pull exact file specs
  before finalizing Publisher page setup; may require adjusting the
  scaffold generator's bleed/margin defaults.
- **Color profile** — CMYK conversion / profile target not yet specified;
  needs to be confirmed against vendor requirements before final export.
- **Spot color implementation** — the version badge is currently a flat
  placeholder fill (`#FF00A6`) in the generated SVG, explicitly named
  `VERSION_BADGE_spotcolor` so it's unmistakable which object to convert to
  a true spot-color swatch once the house palette (see
  `brand-guidelines.md`) is finalized.
