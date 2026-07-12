# Video 2 — The RAG Pipeline in Six Stages

**Target:** 12–15 min · **Audience:** watched #1, or developers who've done
a RAG tutorial · **Job:** the viewer can name the six stages, say what each
decides, and knows where systems break. *This video is the poster.*

## Hook (0:00–1:00)

- "RAG is ten lines of code." True — the demo takes an afternoon. Then
  it meets real documents and real users, and every one of those ten
  lines explodes into a decision. Production RAG is a **pipeline of six
  decisions**, and today we walk all of them.

## The two-lane secret (1:00–3:00) — the structural insight

- The pipeline isn't one assembly line, it's **two lanes meeting at an
  index**:
  - **Indexing lane (offline, ahead of time):** Ingestion → Chunking →
    Embedding → Indexing. Runs when documents change.
  - **Query lane (online, per question):** Retrieval → Generation. Runs
    in the user's latency budget, every single question.
- DRAW THIS: two lanes converging on a cylinder (the index). Offline lane
  can be slow and thorough; online lane has milliseconds and money on the
  line. Different economics, different failure styles.
- ⚑ CHART QUESTION: the current poster spine is one left-to-right line.
  Does the two-lane framing deserve to be visible in the topology (e.g.
  a subtle lane divider), or is it a caption? Decide after recording.

## Six stages, ~90 seconds each (3:00–12:00)

Format per stage — one job, one decision, one failure:

1. **INGESTION** — job: documents → clean text + metadata. Decision:
   layout-aware parsing vs plain extraction. Failure: a two-column PDF
   read in the wrong order poisons everything downstream.
2. **CHUNKING** — job: text → retrievable pieces. Decision: fixed size vs
   structure-aware vs semantic. Failure: the answer straddles a chunk
   boundary and neither half retrieves.
3. **EMBEDDING** — job: chunks → vectors that put similar meaning nearby.
   Decision: which model (dimensionality / cost / domain fit). Failure:
   generic model, specialist jargon — "similar" vectors that aren't.
4. **INDEXING** — job: store vectors so nearest-neighbor is fast.
   Decision: exact (flat) vs approximate (IVF, HNSW); metadata filtering
   planned in from day one. Failure: index quietly stale vs the docs.
5. **RETRIEVAL** (double time here — it's double width on the chart) —
   job: question → the right handful of chunks. Decisions stack up:
   dense vs sparse vs hybrid; rerank or not; rewrite the query or not;
   how many results (top-k). Failure: recall@k looks great, answers are
   still wrong.
6. **GENERATION** — job: chunks + question → grounded answer. Decision:
   context budget, citation strategy, and what to do when retrieval came
   back weak. Failure: right chunks in the prompt, model ignores them.

## Where it breaks: the seams (12:00–13:30)

- Failures mostly live **between** stages, not inside them. Preview the
  five (this is the poster's bottom strip verbatim): stale index / doc
  drift · retrieval-generation mismatch · context overflow /
  lost-in-the-middle · chunk boundary cuts the answer · eval blind spots.
- One sentence each; full video (#9) at the end of the series.

## Close (13:30–14:30)

- Series map: one video per stage, ten-ish minutes each, war story first.
- Chart beat: "this exact six-box layout is the wall chart — Retrieval
  double-wide, failure strip along the bottom. Teaching it is how I find
  out what belongs in the boxes."

## Capture for the chart (fill in after recording)

- [ ] Two-lane framing: topology, caption, or cut?
- [ ] Did the 1-job / 1-decision / 1-failure triple per stage feel like
      the right *box template* for the poster?
- [ ] Which stage ran long — more content living there than its box allows?
- [ ] Any stage that felt like it wanted to split/merge (topology signal).
