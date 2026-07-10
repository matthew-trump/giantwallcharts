# Versioning Scheme

Fast-moving topics (RAG is the prototype case) need versioning that's honest
about being "current best understanding," not "eternal truth" — while still
letting the poster feel like a permanent, well-designed object rather than a
disposable printout.

## Major.minor, semver-style

- **Major version** — a structural / topological change to the poster's
  spine: a stage is added, split, merged, or reordered. Example: if
  "reranking" ever becomes significant enough to warrant its own numbered
  stage rather than living inside Retrieval, that's a major-version-defining
  change.
- **Minor version** — a content refresh inside an otherwise stable spine: a
  new technique or term added inside an existing stage box, an index type
  swapped for a newer one, a tradeoff note refined. These accumulate without
  moving or resizing anything structural.

This distinction is also a discipline for deciding whether a change is
version-worthy at all: real news in the field that doesn't touch the
topology is a minor content refresh; a change that does touch the topology
is worth a new major version and a badge update. This avoids both
over-versioning (badge churn with no real change) and under-versioning (a
real structural shift hiding as a footnote).

## On-poster signaling: the version badge

A fixed-position badge (bottom-right of the header zone in the current
scaffold) carries the version number in a **spot color**:

- The **spot color itself is tied to major version only** — this is the
  thing that should be legible from across a room. Two different major
  versions of the same poster should be visually distinguishable at a
  glance via badge color alone.
- The **minor version** is a smaller mark in the same color family
  (lighter tint or thinner weight), placed beside or inside the badge —
  legible on close inspection (exactly when a buyer deciding whether to
  upgrade would be looking), effectively invisible from normal viewing
  distance.
- Example: badge reads `v2` large, `.3` small and lighter beside it.

Keeping the spot color change confined to this one badge element (rather
than washing the whole design in a new color per version) means:
- The core Bauhaus palette and grid stay constant across every version of
  every chart — protecting the brand-recognition value of a consistent
  palette across the whole line (see `brand-guidelines.md`).
- Terminology note: "spot color" here means one designated solid accent
  color in the pre-digital sense, not a literal premixed-ink plate — POD
  and digital printing have no plates or separations, so there's no
  production-cost angle either way. The practical consequence instead:
  badge colors must be chosen to stay solid and punchy after CMYK/inkjet
  conversion, since no actual spot ink guarantees the hue.

## Two-tier signal, on purpose

The badge is the *explicit* version marker. The spine's structural stability
across minor (and even most major) versions is meant to function as an
*implicit* second signal for an experienced viewer — someone who knows the
field should be able to eyeball the topology itself and get a rough sense of
which era/version they're looking at, independent of reading the badge.

## Practical inventory/production implications

- **Major version bump** → new print file, effectively a new product
  listing/SKU on giantwallcharts.com.
- **Minor version bump** → does not necessarily require a new print run
  immediately. Can be tracked as a changelog note on the product listing
  ("current: v2.3") until enough minor changes accumulate to justify a
  reprint, at which point the physical badge is updated to match.

## Repo mechanics

- Each chart's directory (`charts/<slug>/`) contains one subdirectory per
  **major** version (`v1/`, `v2/`, ...).
- Minor versions live as commits/tags within a major version's directory —
  they do not get their own subdirectory.
- The structural scaffold generator script (see `production-pipeline.md`)
  is the source of truth for topology. When a major version changes the
  spine, update the generator's config (stage list/weights) and re-run it
  rather than hand-editing coordinates directly, so the topology change is
  visible and diffable in plain text (the script), not buried in a binary
  Affinity file.

## Upgrade purchase mechanic

Agreed v1 approach: **discount-on-repurchase** — a discount code tied to a
past order, offered when a new major version ships. Simple, no ongoing
commitment on either side, and it tests real demand for updates before
building anything more complex.

Deferred/later-stage ideas (not yet committed to):
- **Subscription** to a bundle/category (e.g. "AI infra" line), worth
  revisiting once the catalog has enough fast-moving titles to justify a
  recurring price.
- **Trade-in / upgrade credit** tied to proof of past purchase — adds
  support/verification overhead, hold until there's a clear reason to
  add it.
