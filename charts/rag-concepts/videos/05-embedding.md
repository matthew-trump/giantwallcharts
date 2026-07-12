# Video 5 — Stage 3: Embedding

**Target:** 10–12 min · **Audience:** watched the series so far, or
arriving cold · **Job:** the viewer understands embedding as "turning text
into a point in meaning-space" well enough to see why a mismatched model
makes "similar" vectors that aren't actually similar.

## Hook (0:00–1:30)

- War story: a medical or legal team deploys RAG with a general-purpose,
  off-the-shelf embedding model. Ask it about "adverse events" and it
  retrieves chunks about "bad weather events" — the model was trained on
  everyday internet text, and in that world "adverse" clusters near
  "unfavorable/bad," not near the specific jargon meaning the domain
  intends. The retrieval math is working exactly as designed; it's just
  the wrong space.
- The lesson up front: embeddings don't fail loudly. They fail by quietly
  returning things that are "similar" by the wrong definition of similar.

## What embedding actually does (1:30–3:30)

- Job in one sentence: **chunks in, vectors out — numbers arranged so
  that similar meaning sits nearby in the vector space.**
- DRAW THIS: a simple 2D scatter — "dog" and "puppy" close together,
  "dog" and "car" far apart. This is the whole idea in one picture; the
  real vectors just have hundreds or thousands of dimensions instead of
  two.
- This is what makes semantic search possible at all: not matching exact
  keywords, but matching *meaning*. "How do I get my money back" finds a
  chunk that says "refund policy" even though no word overlaps.

## The decision: which embedding model (3:30–6:30) — core segment

- Three axes that actually matter in practice:
  - **Domain fit** — was it trained on text like yours (general web text
    vs. legal/medical/code-specific)? This is the axis that broke the
    hook's war story.
  - **Dimensionality** — more dimensions can capture more nuance, but
    cost more to store and search; not a free win.
  - **Cost and where it runs** — hosted API per-call cost vs. a
    self-hosted open model with upfront compute cost. Also: whatever you
    pick has to stay consistent, because...
- One rule that trips people up constantly: **you cannot mix embedding
  models within one index.** A vector from model A and a vector from
  model B are not comparable numbers, even if both are "embeddings" —
  switching models means re-embedding everything, not just the new
  documents.

## How to sanity-check a model choice (6:30–8:30)

- Don't trust the vibes — run a small, concrete test: take ten real
  questions your users would actually ask, embed them plus your actual
  documents, and look at what comes back nearest. Domain jargon is where
  general-purpose models most often quietly fail.
- Specialist/fine-tuned embedding models exist for exactly this reason —
  legal, medical, code. Worth a name-check, not a deep dive here.

## How to tell embedding is broken (8:30–9:30)

- The tell: retrieved chunks are topically *near* the question but not
  *about* the question — same general neighborhood, wrong house. Distinct
  from a chunking failure (where the right words are split or buried) —
  here the words themselves are being misjudged as similar or dissimilar.

## Close (9:30–10:30)

- Recap: embedding's job (meaning → geometry), its central decision
  (which model, on domain fit above all), its signature failure
  (confidently wrong notion of "similar").
- Chart beat: "third box — the one that turns 'search' from keyword
  matching into meaning matching, for better or worse."
- Tease next: "vectors are useless until you can search millions of them
  fast — next video, how they get stored and found."

## Capture for the chart (fill in after recording)

- [ ] Did the 2D scatter drawing land as the core visual, or find
      something better?
- [ ] "Can't mix embedding models" — surprising enough to earn poster
      space, or too in-the-weeds?
- [ ] Domain-fit sanity-check method — worth a fine-print callout?
- [ ] Any explaining twice → candidate fine print.
