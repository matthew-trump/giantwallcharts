# Video 4 — Stage 2: Chunking

**Target:** 10–12 min · **Audience:** watched the series so far, or
arriving cold · **Job:** the viewer understands chunking as "deciding the
unit of retrieval" and can name why the obvious approach (fixed-size
slices) quietly breaks answers.

## Hook (0:00–1:30)

- War story: a policy answer lives in one sentence — "employees may carry
  over up to five vacation days" — but a fixed-size chunker cut the
  document every 500 characters without looking at sentence boundaries.
  The number "five" ends up in one chunk, the words "vacation days" in
  the next. Neither chunk, alone, answers the question. Retrieval finds
  one or the other, never both — the system answers confidently and
  wrong, or refuses to answer at all.
- This is chunking's whole problem in one image: **the answer straddled
  a boundary, and the boundary won.**

## What chunking actually does (1:30–3:00)

- Job in one sentence: **clean text in, retrievable pieces out.**
- Why not retrieve whole documents? Because relevance and context length
  both push toward small units — you want the *few sentences* that
  answer the question, not the fifty-page manual they're buried in.
- The chunk is the atomic unit for everything downstream: it's what gets
  embedded, what gets retrieved, what gets shown to the model. Get the
  unit wrong and every later stage inherits the mistake.

## The decision: fixed size vs structure-aware vs semantic (3:00–7:00) — core segment

- **Fixed size:** slice every N characters/tokens, maybe with overlap.
  Dead simple, fast, and blind — it will cut mid-sentence, mid-table,
  mid-thought, exactly as often as it happens to.
- **Structure-aware:** cut on the document's own boundaries — headings,
  paragraphs, list items, table rows. Respects what the author already
  told you about where ideas begin and end.
- **Semantic:** measure meaning as you go (via embeddings) and cut where
  the topic actually shifts, not where a heading happens to be. Most
  adaptive, most expensive, hardest to reason about when it goes wrong.
- DRAW THIS: the same paragraph sliced three ways — fixed-size cutting
  the vacation-days sentence in half, structure-aware keeping the whole
  policy bullet intact, semantic drawing the boundary at the actual topic
  change.
- Overlap as a partial patch: repeating a little text between chunks
  reduces boundary casualties but doesn't eliminate them, and it inflates
  index size. A mitigation, not a fix.

## Chunk size as its own tradeoff (7:00–9:00)

- Too small: fragments lose context — a chunk with just "five days" and
  no subject is useless alone.
- Too large: dilutes relevance — the right sentence is buried in four
  paragraphs of unrelated policy, and embedding similarity gets muddier
  the more topics one chunk covers.
- No universal right answer — it depends on document type (a legal
  contract chunks differently than a chat log) and what questions users
  actually ask. Name this as an experiment you run, not a constant you
  look up.

## How to tell chunking is broken (9:00–10:00)

- The tell: retrieval returns chunks that are *almost* right — the answer
  is clearly nearby, split across two results that never both make the
  cut, or crammed alongside enough noise that the model can't isolate it.
- Practical habit: when an answer is wrong, read the actual chunk that
  was retrieved. If the right words are present but incomplete or
  swamped, that's a chunking problem wearing a retrieval costume.

## Close (10:00–11:00)

- Recap: chunking's job (define the retrievable unit), its central
  decision (fixed vs structure-aware vs semantic), its signature failure
  (the answer straddles a boundary).
- Chart beat: "second box on the wall chart — right after ingestion,
  because you can't chunk what you haven't cleanly extracted yet."
- Tease next: "chunks are just text. Next video: turning them into
  something a computer can search by meaning, not by keyword."

## Capture for the chart (fill in after recording)

- [ ] Did the three-way slice drawing land, or find a cleaner way to show it?
- [ ] Chunk-size tradeoff — poster-worthy as its own line, or folds into
      the "decision" box?
- [ ] Overlap — mention on the poster at all, or pure fine print?
- [ ] Any explaining twice → candidate fine print.
