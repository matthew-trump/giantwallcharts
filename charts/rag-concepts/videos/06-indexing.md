# Video 6 — Stage 4: Indexing

**Target:** 10–12 min · **Audience:** watched the series so far, or
arriving cold · **Job:** the viewer understands indexing as "organizing
vectors so nearest-neighbor search is fast at scale" and can name the
exact/approximate tradeoff plus the silent-staleness failure.

## Hook (0:00–1:30)

- War story: a team ships RAG, it works great in the demo on 500
  documents, then someone loads the real corpus — five million chunks —
  and every query takes eight seconds. Or: the opposite trap — a team
  rebuilds their index nightly, someone edits a policy document at 9am,
  and the chatbot confidently quotes the *old* policy all day because the
  index doesn't know the document changed.
- Two failure shapes, same stage: indexing done wrong is either too slow
  to use, or too stale to trust.

## What indexing actually does (1:30–3:00)

- Job in one sentence: **store vectors so that "find the nearest ones to
  this query vector" is fast, even across millions of them.**
- Why this is genuinely hard: naive nearest-neighbor search means
  comparing the query to *every single vector* — fine at 500, useless at
  5 million. Indexing is the structure that avoids that brute-force scan.

## The decision: exact vs approximate (3:00–6:00) — core segment

- **Exact (flat) search:** compare against everything, guaranteed to find
  the true nearest neighbors. Correct, but doesn't scale — this is the
  brute-force scan.
- **Approximate (ANN) search — IVF, HNSW, and similar:** pre-organize
  vectors into a structure (clusters, graphs) that lets you skip most of
  the comparisons. Fast at scale, at the cost of occasionally missing the
  *true* nearest neighbor for a very close *near*-nearest one.
- DRAW THIS: brute-force as checking every house on every street vs. ANN
  as a filing system that jumps straight to the right neighborhood, with
  a small chance of a good-but-not-perfect match.
- The practical takeaway: at real-world scale almost everyone uses
  approximate search — the small accuracy cost is worth the speed. Exact
  search stays relevant for small corpora or as a correctness baseline
  when debugging.

## Metadata filtering, planned in from day one (6:00–7:30)

- Vector similarity alone often isn't enough — you also want "only
  documents from this department," "only after this date," "only public
  docs, not internal." That's metadata filtering, riding on the metadata
  ingestion captured back in stage one.
- Why "from day one" matters: bolting filtering onto an index built
  without it is a re-architecture, not a config change. This is a design
  decision, not a runtime option.

## The staleness failure (7:30–9:00) — the hook, paid off

- An index is a snapshot. The moment source documents change and the
  index doesn't get updated, every answer downstream is confidently wrong
  about something that's no longer true — and nothing in the pipeline
  will tell you, because retrieval and generation are both working
  perfectly on stale information.
- The fix isn't technical, it's operational: a defined re-indexing
  cadence (or trigger, for real-time-sensitive data) has to exist and be
  owned by someone. "We'll rebuild it eventually" is how policy documents
  from six months ago end up quoted as current.

## Close (9:00–10:00)

- Recap: indexing's job (fast search at scale), its central decision
  (exact vs approximate, plus filtering strategy), its signature failure
  (quietly stale vs. the real documents).
- Chart beat: "fourth box — the last stop in the offline lane before a
  real question ever arrives."
- Tease next: "everything so far ran ahead of time, off the clock. Next
  video: the stage that has to happen in the seconds a real user is
  waiting — retrieval."

## Capture for the chart (fill in after recording)

- [ ] Did the "brute-force vs filing system" drawing land?
- [ ] Metadata filtering — its own line on the poster, or a sub-note
      under the decision?
- [ ] Staleness — strong enough to be its own failure-strip entry
      (it already is on the current spine — confirm it still fits after
      teaching this)?
- [ ] Any explaining twice → candidate fine print.
