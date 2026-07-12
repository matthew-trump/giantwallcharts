# Video 7 — Stage 5: Retrieval

**Target:** 13–15 min (longest in the series, deliberately — this stage is
double-width on the poster) · **Audience:** watched the series so far, or
arriving cold · **Job:** the viewer can name the dense/sparse/hybrid
decision, what reranking and query rewriting add, and why a system can
have great recall metrics and still give wrong answers.

## Hook (0:00–1:30)

- War story: a team measures retrieval with recall@k and it looks
  excellent — the right document is in the top 5 results 95% of the time.
  Users still complain the bot is wrong constantly. The gap: recall@k
  asks "is the right chunk *somewhere* in the results," not "did the
  *most* relevant chunk rank high enough, and did generation actually use
  it." Retrieval can hit its metric and still be the reason the system
  fails.
- This is retrieval's whole double-width box on the poster in one
  sentence: it's not one decision, it's a stack of them, and each one has
  its own way of technically succeeding while practically failing.

## What retrieval actually does (1:30–3:00)

- Job in one sentence: **a question in, the right handful of chunks out**
  — the only stage that runs live, in the seconds a real user is waiting,
  against the index built by every stage before it.
- Everything upstream (ingestion, chunking, embedding, indexing) was
  preparation. Retrieval is where the pipeline meets an actual person
  with an actual question, under a real latency and cost budget.

## Decision 1: dense vs sparse vs hybrid (3:00–6:30) — core segment

- **Dense retrieval:** embedding-based, meaning-based — finds
  conceptually similar text even with zero word overlap. Weak on exact
  terms: product codes, part numbers, acronyms, names — things where the
  *literal string* matters more than the concept.
- **Sparse retrieval:** classic keyword search (think BM25/TF-IDF) —
  exact term matching, no notion of meaning. Finds "SKU-4471" perfectly;
  misses that "cost" and "price" are the same idea.
- **Hybrid:** run both, combine the results. Gets the best of each at the
  cost of more moving parts and a combination step that itself needs
  tuning.
- DRAW THIS: a query containing both a concept ("refund eligibility") and
  a literal code ("Form 1099-K") — dense nailing the concept and missing
  the code, sparse nailing the code and missing the concept, hybrid
  catching both.

## Decision 2: rerank or not (6:30–8:30)

- Initial retrieval (dense/sparse/hybrid) is built for speed across the
  whole index — it casts a wide, fast, somewhat approximate net.
- A reranker is a second, slower, more accurate pass applied only to
  those top candidates — reordering them by a finer-grained relevance
  judgment before they ever reach generation.
- The tradeoff is latency and cost for accuracy: worth it when precision
  at the very top matters (only the top 2-3 chunks actually make it into
  the prompt); less worth it when the initial retrieval is already clean.

## Decision 3: rewrite the query or not (8:30–10:00)

- Real user questions are often bad search queries: vague, conversational,
  missing the specific terms the documents actually use ("that thing with
  the refund" vs. the document's own phrase "return merchandise
  authorization").
- Query rewriting: use a model to expand, clarify, or reformulate the
  question before it hits retrieval — one more stage, one more place
  latency and errors can creep in.

## Decision 4: top-k (10:00–11:00)

- How many chunks come back. Too few: the answer's key fact isn't among
  them. Too many: noise dilutes the model's attention and inflates the
  context/cost downstream. Not a universal constant — tune per corpus and
  question type, same spirit as chunk size in video 4.

## The metric trap — the hook, paid off (11:00–12:30)

- Recall@k tells you the right chunk *exists* in the results. It says
  nothing about rank order, about whether the model actually used it, or
  about whether *other*, wrong-but-plausible chunks crowded it out of the
  model's attention. Good retrieval metrics are necessary, not sufficient
  — evaluation has to look at the final answer, not just the retrieval
  step in isolation. (Full treatment in video 9.)

## Close (12:30–13:30)

- Recap: retrieval's job (question → right chunks, live), its stack of
  decisions (dense/sparse/hybrid, rerank, rewrite, top-k), its signature
  trap (metrics that look great while answers stay wrong).
- Chart beat: "this is the double-wide box on the wall chart — one stage,
  four real decisions, because that's genuinely how much is packed in
  here."
- Tease next: "even perfect retrieval is wasted if the model ignores what
  it's given — next video, generation."

## Capture for the chart (fill in after recording)

- [ ] Did the dense/sparse/hybrid concept-vs-code example land, or find a
      cleaner one live?
- [ ] Four sub-decisions (dense/sparse/hybrid, rerank, rewrite, top-k) —
      does the double-wide box have room for all four, or does one get
      cut to fine print?
- [ ] Recall@k trap — poster-worthy as its own line, or purely video #9's
      territory?
- [ ] Which sub-decision ran longest live — signal for what needs the
      most poster real estate?
