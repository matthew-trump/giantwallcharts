# Brand Guidelines

## Domain / storefront

**giantwallcharts.com** — reserved, intended as the eventual shopping cart
site for the whole product line (see `site/`, not yet built).

## Visual language

Swiss/Bauhaus: disciplined grid, restrained palette, tasteful white space,
clear typographic hierarchy. Posters should read as designed objects, not
dense infographics — density is earned by content maturity over versions,
not present from day one (see "start sparse, fill in" principle below).

Mood reference: the "Giant Hamburger" fast food chain (California) — big,
unapologetic, confident scale, friendly slab-serif energy, without losing
precision. Useful north star for the wordmark/logo direction.

## One palette and grid across the entire line

The single most important brand rule: **the same color palette and grid
system is used across every chart title, regardless of topic** — RAG,
AWS, quantum gravity, Latin declensions, whatever comes next. This is what
makes the catalog read as one coherent brand rather than a series of
one-off posters, and it's what will make future "on GCP" / "on Azure" /
other-topic entries feel like a series rather than reskins.

Consequence: **never adopt a third-party vendor's own brand colors** for a
platform-specific companion poster (e.g. do not use AWS's orange/black for
"RAG on AWS"). Reasons:
1. Brand consistency — the house palette must remain constant.
2. Trademark/licensing safety — using another company's specific brand
   colors and iconography on a commercial product invites licensing
   questions that using generic shapes/labels avoids entirely. Notably,
   AWS itself is inconsistent about color-to-service mapping in its own
   materials, so there's no strong user expectation being violated by using
   the house system instead.

## Start sparse, fill in ("Moore's Law in print, tastefully")

New posters — and new versions of existing posters — should launch with a
lean, sparse layout and let a typography hierarchy (stage title -> key term
-> one-line tradeoff -> fine print) grow into the design over subsequent
minor versions, informed by what buyers actually reference or ask for. This
keeps early print runs cheap to be wrong about, and keeps the design from
ever reading as crammed just because it's information-dense.

## Format conventions

- Landscape orientation for pipeline/process posters (left-to-right flow
  matches how a spine/pipeline is naturally read).
- 36"x24" is the default premium size; smaller formats may be produced later
  once a title is validated at full size.
- See `production-pipeline.md` for concrete print specs (bleed, margins).

## Open / not yet finalized

- Exact house color palette (swatch values) — not yet locked. Once decided,
  should live as a literal Affinity swatch file in `shared/templates/` so
  every chart inherits it rather than redefining it per project.
- Wordmark / logotype for Giant Wall Charts.
- Typography tier sizes/weights as a formal, reusable style (currently only
  loosely defined per the scaffold generator's defaults).
