# Roadmap to First Sale — RAG Concepts v1

The critical path from the current state (structural scaffold generated,
export target locked — see `production-pipeline.md`) to the first sale of
a physical poster. Roughly 15–20 working hours; 2–4 weeks calendar time,
dominated by proof shipping waits, not work.

Scope discipline: everything in "Explicitly not on this path" (bottom) is
a detour until the first sale happens.

## Phase 0 — Teach it first (video series, before design details)

Content development, not busywork: teaching the material live is how the
chart's boxes get pressure-tested before a single hour of Affinity work is
spent finishing them. Also builds the audience Phase 4's launch posts go
out to. Full workflow and outlines: `charts/rag-concepts/videos/`.

- [x] Outlines written for all 9 videos (`01-what-is-rag.md` through
      `09-failure-modes.md`).
- [ ] Record the series (self-produced, no help needed here).
- [ ] After each recording, fill in that video's "Capture for the chart"
      checklist.
- [ ] Reconcile captures against `charts/rag-concepts/README.md` — content
      that survived teaching earns wall space; topology changes are free
      until v1 prints (see `versioning-scheme.md`).

## Phase 1 — Unblock the design (one evening)

The only open decisions that gate the Affinity work. Per the "start
sparse" principle (`brand-guidelines.md`), these need to be *committed*,
not perfect.

- [ ] **Lock a v1 house palette** — one near-black ink, one paper/off-white,
      one or two accents, plus the version-badge color family (v1's badge
      color chosen to stay solid and punchy through CMYK/inkjet conversion).
      Save as an Affinity swatch file in `shared/templates/` so every later
      chart inherits it.
- [ ] **Placeholder wordmark** — "GIANT WALL CHARTS" typeset in a confident
      slab serif is enough for v1; the real logotype is a v1.x refinement,
      not a launch gate. Confirm the font license covers commercial print.
- [ ] **Fix the four typography tiers** (stage title → key term → tradeoff
      line → fine print) as reusable text styles: sizes and weights decided
      once.

## Phase 2 — Make the object (~8 hours design work)

- [ ] **Set up the Affinity document**: 36in × 24in landscape, 0.125in
      bleed, **RGB/8, sRGB IEC61966-2.1** (not CMYK — see the export
      target in `production-pipeline.md`).
- [ ] **Import `charts/rag-concepts/v1/rag_concepts_spine_v1.svg` as a
      locked bottom layer**; do all hand work on layers above it, so a
      regenerated scaffold can be swapped underneath without losing
      finishing work.
- [ ] **Hand-finish RAG Concepts v1** per the locked content outline
      (`charts/rag-concepts/README.md`). Resist scope growth — density
      grows in minor versions.
- [ ] **Export the print PNG**: 300 DPI, full size, sRGB.
      (36×24in trim = 10800×7200 px; 10875×7275 px if bleed included —
      the vendor's template overlay at upload settles which.)

## Phase 3 — Proof (~1 week, mostly waiting)

- [ ] **Create Printful account, upload, order one proof** to home
      (~$30 delivered; sample-order discounts may apply). Optionally order
      a Printify proof from the same file (~$25) as a vendor bake-off.
- [ ] **While the proof ships** (dead time — use it):
  - [ ] Draft listing copy.
  - [ ] Decide price (~$45–60 is the going range for large-format matte
        posters).
  - [ ] Put a one-page landing at giantwallcharts.com: headline, poster
        image, **email signup** (the upgrade-mechanic infrastructure —
        see `versioning-scheme.md`), link-to-listing placeholder.
- [ ] **Evaluate the proof on a wall**: color shift vs screen, fine-print
      legibility at arm's length, structure legibility across the room,
      paper feel. Cosmetic fixes → proceed; structural fixes → one more
      proof cycle (+1 week, +$30). Budget for one respin — first proofs
      usually surprise somewhere, typically color or small type.

## Phase 4 — List and launch (a weekend)

- [ ] **Photograph the proof hanging on a real wall.** This photo is the
      launch asset; it outsells any digital mockup and makes launch posts
      credible.
- [ ] **Open the storefront**: Etsy connected to Printful (built-in
      discovery, sales tax handled, auto-fulfillment) is the fastest path
      to a first sale. Shopify — which shares customer emails — is the
      better long-term home; add it second.
- [ ] **Launch posts**, staggered over a few days, each with the wall
      photo, one honest paragraph on the interview-prep origin story, and
      the listing link:
  - [ ] Show HN
  - [ ] LinkedIn
  - [ ] X/Twitter
  - [ ] Relevant subreddits (r/LangChain, r/Rag, etc.)
- [ ] **First sale** — Printful fulfills; nothing to do.

## Explicitly not on this path

- RAG on AWS companion (gated on v1 being hand-finished anyway)
- Quantum Gravity History poster
- The custom shopping-cart site (`site/`)
- Subscription / upgrade-credit mechanics beyond collecting emails
- Any further repo tooling or generator work
