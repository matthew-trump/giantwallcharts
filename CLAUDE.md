# Giant Wall Charts — Project Context for Claude Code

This is a monorepo for **Giant Wall Charts** (domain: giantwallcharts.com), a
publishing venture producing large-format (typically 36"x24") educational
wall posters — initially in STEM, philosophy, and humanities topics — sold
print-on-demand (POD) initially, with successful designs moved to bulk print
runs once demand is proven.

Read this file first in any session. Then read `docs/project-brief.md` for
full background, `docs/versioning-scheme.md` before touching any version
badge or spine topology, and `docs/production-pipeline.md` before generating
or editing print artifacts.

## Repo shape (monorepo)

```
giantwallcharts/
  docs/                        # project-wide direction, brand, versioning, production docs
  charts/                      # one directory per poster title
    <chart-slug>/
      v1/, v2/, ...            # one directory per MAJOR version
        generate_spine.py      # parametric structure generator (if applicable)
        <slug>_spine_v#.svg    # generated scaffold, imported into Affinity
        <slug>.afdesign        # (added later) hand-finished Affinity Designer art
        <slug>.afpub           # (added later) Affinity Publisher page/print file
        README.md              # per-chart content outline, stage notes, status
  shared/
    scripts/                   # reusable generator logic shared across charts
    templates/                 # shared brand assets: palette, type scale, etc. (to be added)
  site/                        # giantwallcharts.com shopping cart site (not yet started)
```

Each chart gets its own directory under `charts/`, and each **major version**
of a chart gets its own subdirectory. Minor versions do not get new
directories — they're tracked as commits/tags within a major version
directory, per `docs/versioning-scheme.md`.

## Status as of repo creation

- **RAG Concepts (v1)** — content outline locked (six-stage spine +
  failure-modes strip), structural scaffold generated
  (`charts/rag-concepts/v1/generate_spine.py` +
  `rag_concepts_spine_v1.svg`). Not yet opened in Affinity for hand-finishing.
- **RAG on AWS** — planned as a topology-matched companion to RAG Concepts
  (same spine, AWS-specific branching inside the Retrieval stage). Not yet
  generated. Directory scaffolded and empty.
- **Quantum Gravity History poster** — the original/first product concept
  (dual-lineage canonical + covariant thesis through Bryce DeWitt). Predates
  this repo; content and brief exist outside it. Placeholder directory only —
  bring existing materials in when ready.
- **Site (shopping cart)** — not started. Domain giantwallcharts.com is
  owned and reserved for this. Placeholder directory only.

## Working conventions

- **Design tools**: Affinity Designer 2 (illustration/diagram work) and
  Affinity Publisher 2 (page layout, typography hierarchy, print/PDF export).
  Structural layouts are generated programmatically first (Python -> SVG)
  to guarantee exact, reproducible topology, then imported into Designer as
  a starting layer and hand-finished. See `docs/production-pipeline.md`.
- **Brand consistency**: one constant color palette and grid system across
  the entire chart line, regardless of topic (RAG, AWS, quantum gravity,
  Latin declensions, etc.) — this is what makes the line read as a coherent
  brand rather than one-off posters. Never use a vendor's own brand colors
  (e.g. AWS orange) for vendor-specific companion charts — use the house
  palette plus generic shapes/labels to avoid any trademark question.
- **Versioning**: major.minor, signaled on-poster via a fixed-position spot
  color badge (major version drives the badge's spot color; minor version
  is a smaller same-family mark beside it). Major = structural/topology
  change (a stage added, split, merged, reordered). Minor = content refresh
  within a stable spine (new technique/term added inside an existing box).
  Full rationale in `docs/versioning-scheme.md`.
- **Print specs**: default canvas 36"x24" landscape, 0.125" bleed, 0.75"
  safe margin inset from trim. Confirm against the specific POD vendor's
  template before final export — vendor specifics are not yet locked in
  this repo (see `docs/production-pipeline.md` open questions).

## Open questions / next decisions

- Which POD vendor (Printful, Printify, or other) — pull exact file specs
  before finalizing page setup in Publisher.
- Typography hierarchy tier count and sizes (stage title -> key term ->
  tradeoff line -> fine print) — not yet formalized as a shared style.
- Whether `shared/templates/` should hold a literal Affinity palette/swatch
  file once the house palette is finalized, so every chart inherits it
  rather than redefining it per-project.
- Business mechanic for version upgrades (discount-on-repurchase is the
  agreed v1 approach; subscription bundling is a later-stage idea once the
  catalog is large enough).
