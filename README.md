# Giant Wall Charts

Large-format (36"x24") educational wall posters — STEM, philosophy, and
humanities topics — designed with a Swiss/Bauhaus aesthetic, sold print-on-
demand initially via giantwallcharts.com, with proven sellers moved to bulk
print runs.

This is a monorepo: it will eventually hold every chart title, shared brand
assets, and the shopping cart site itself.

**Start here:** [`CLAUDE.md`](./CLAUDE.md) for project conventions and
current status, then [`docs/`](./docs) for full background.

## Layout

- `docs/` — project brief, brand guidelines, versioning scheme, production
  pipeline
- `charts/` — one directory per poster title, one subdirectory per major
  version
- `shared/` — reusable generator scripts and (eventually) shared brand
  templates/swatches
- `site/` — giantwallcharts.com shopping cart site (not yet started)

## Current chart titles

| Chart | Status |
|---|---|
| RAG Concepts | Outline locked, structural scaffold generated (v1) |
| RAG on AWS | Planned companion to RAG Concepts, not yet generated |
| Quantum Gravity History | Original product concept, predates this repo |
