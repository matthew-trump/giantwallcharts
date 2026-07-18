# RAG Pipeline Knowledge Check — Drill Log

A running log of a live Q&A drill (Claude quizzing Matthew, Socratic style)
working through the RAG pipeline stage by stage. Two purposes at once:

1. **Interview readiness** — surface and correct exactly the conflations
   that cause fumbles under pressure, with the tight one-breath phrasing
   that should come out instead.
2. **Chart content signal** — same principle as the video captures
   (`videos/README.md`): if a distinction was worth drilling here, it's
   worth asking whether it earns space on the poster. Entries below flag
   candidates with 🎯.

Format per stage: the conflation(s) actually made, the corrected
understanding, and the sharp phrasing to reuse.

## Two-lane structure (established first)

"The RAG pipeline" has two starting points, not one:

- **Offline/indexing lane** — starts with ingestion, runs ahead of time.
- **Online/query lane** — starts with the user's question, runs live.

🎯 Already an open chart question (see `videos/02-pipeline-overview.md`
⚑) — naming both lanes up front, unprompted, is itself the interview
signal of understanding the architecture vs. reciting a step list.

## Stage 1 — Ingestion

- **Conflation caught:** ingestion produces vectors. (It doesn't —
  vectorization is stage 3, embedding, and it acts on chunks, not raw
  documents. Naming vectors here silently skips chunking and embedding
  as if they don't exist.)
- **Corrected understanding:** ingestion's output is **clean text +
  metadata** (source, title, section, date) — a normalized text object,
  not a number.
- **The decision:** extraction fidelity — **plain extraction** (pull the
  raw text stream, ignore layout) vs **layout-aware extraction**
  (understand columns, tables, reading order as structure). Matthew's own
  phrasing, worth keeping verbatim: *"examine the format and make an
  intelligent guess as to the semantic arrangement of the text."*
- **The failure:** structure destroyed during extraction — e.g. a
  two-column PDF read naively left-to-right, splicing unrelated
  sentences together. Real words, scrambled meaning, invisible to a
  human skimming the source. Nothing downstream can recover from it.
- 🎯 "Examine the format, guess the semantic arrangement" is a strong
  compact box-copy candidate for the ingestion stage.

## Stage 2 — Chunking

- **Conflation caught (1st pass):** "how to split up the text" offered
  as *ingestion's* decision. (It's chunking's — at ingestion time there's
  no notion of "pieces" yet, only whole documents.)
- **Conflation caught (2nd pass):** chunk *size* (too big/too small)
  given as the headline failure. (Real and worth knowing, but not the
  sharp one — an interviewer wants the failure specific to chunking that
  nothing else causes.)
- **Corrected understanding / the failure:** boundary pathologies — sharp
  one-breath phrasing: **"the answer straddles a chunk boundary."**
  Example: "employees may carry over up to five vacation days" gets cut
  between "five" and "vacation days" by a naive fixed-size split; neither
  resulting chunk answers the question, regardless of how good retrieval
  or generation are downstream.
- **The decision — resolved:** fixed size vs structure-aware vs semantic.
  Matthew's default: fixed size, because it's simplest — correct as a
  default answer, worth pairing with *why* it's an acceptable default
  (works fine on simple, uniform documents; the other two cost more to
  build and reason about).
- **The mitigation:** overlap — repeat a little text between adjacent
  chunks. Sharp phrasing to reuse: **"reduces the boundary damage, it
  doesn't eliminate it"** — a big enough cut still slips past a small
  overlap, and overlap costs more chunks/storage/compute downstream. Not
  a fix, a patch.
- 🎯 "The answer straddles a chunk boundary" is strong enough to be the
  chunking box's failure line verbatim.

## Stage 3 — Embedding

- **Conflation caught:** "use an LLM to turn chunks into vectors...
  stored in a vector database" — folds two separate things into one
  answer. (1) It's an **embedding model**, a distinct class from an LLM
  — calling it "an LLM" muddies the one place generation-the-LLM actually
  belongs, stage 6. (2) "Stored in a vector database" is *indexing's* job
  (stage 4), not embedding's — same stage-collapsing pattern as before.
- **Corrected understanding:** embedding's job, precisely, stops at
  **chunks in, vectors out** — numbers arranged so semantic similarity
  maps to geometric closeness. Nothing about storage.
- **The decision — resolved:** domain fit is the answer. Sharp phrasing:
  *"was the model trained on text like yours, not general web text."*
  Failure if wrong: retrieval returns things that are topically near but
  not about the question — "adverse events" (medical) → "bad weather
  events," because a general model's notion of "adverse" was learned from
  everyday text.
- **Trap question — resolved:** no — you cannot mix embedding models
  within one index. Sharp phrasing: *"vectors from two different models
  aren't comparable numbers, even though both are 'embeddings' — they're
  points in two different, incompatible spaces."* Swapping models means
  re-embedding the **entire corpus**, not incrementally topping up new
  documents — a real infra cost, not a config change.
- 🎯 The re-embed-everything cost is a strong fine-print callout — it's
  the kind of operational detail that separates "read about RAG" from
  "ran one," and might belong as a small note near the embedding box.

## Stage 4 — Indexing

- **Why indexing exists:** comparing a query vector against every stored
  vector (brute-force linear scan) is fine at hundreds of vectors, seconds
  per query at millions — and indexing feeds the *online* lane, where a
  real user is waiting inside a latency budget. Correct instinct
  ("computationally expensive"), sharpened: it's specifically the
  linear-scan-doesn't-scale problem.
- **The decision — needed a direct answer, not fully recalled live:**
  **exact (flat) search** vs **approximate (ANN) search** — ANN names to
  drop: **IVF**, **HNSW**. Exact checks everything, guaranteed correct,
  doesn't scale. Approximate pre-organizes vectors (clusters / graph) so
  a query jumps to a promising neighborhood instead of scanning
  everything — fast at scale, trades a small chance of missing the *true*
  nearest neighbor for a very close one.
  Sharp phrasing: *"exact guarantees correctness and doesn't scale;
  approximate scales and trades a small, tunable amount of accuracy for
  it — in production, almost everyone takes that trade."*
- **Metadata filtering — resolved:** why day-one, not bolt-on: some
  index structures (ANN especially — IVF, HNSW) bake filtering into their
  internal organization. Retrofitting it later often means rebuilding the
  index from scratch, not flipping a setting — same "everything, not
  incrementally" cost pattern as the embedding-model-swap trap. Good
  transfer of that pattern once prompted.
- **Staleness — resolved, term correct, mechanism needed a fix:** right
  term recalled close to verbatim — this project's own materials call it
  **"stale index / doc drift."** Wrong mechanism first pass though:
  staleness is not a retrieval *miss* (that's approximate search's
  tradeoff, a different stage's concept). Staleness is the index finding
  something and handing it over *confidently* — just a version of the
  document that's no longer true. Sharp phrasing: *"nothing errors,
  nothing looks broken — retrieval and generation both execute flawlessly
  on outdated ground truth."*
- 🎯 Why staleness > chunking mistake in danger: a chunking failure tends
  to look visibly incomplete/garbled — inviting suspicion. A stale index
  produces a complete, confident, well-formed answer about something that
  changed last week. Nothing about the output signals "check this." This
  contrast is a strong failure-strip callout candidate — could be the
  poster's implicit argument for *why* staleness gets its own strip entry
  even though it "sounds boring" next to the others.

## Stage 5 — Retrieval

- **Decision 1 — dense vs sparse vs hybrid: correct on first pass.**
  Matthew's terms (lexical/semantic) map to the field's other common
  naming (sparse/dense) — worth knowing both, interviewers use either.
  - **Dense/semantic:** embedding-based, meaning-based. Weak on exact
    strings — codes, part numbers, acronyms.
  - **Lexical/sparse:** keyword search (BM25/TF-IDF). Exact-match
    precise, zero notion of meaning — misses synonyms/paraphrase entirely.
  - **Hybrid:** run both, combine results — best of each, at the cost of
    an extra combination/scoring step that itself needs tuning.
  Correctly named hybrid as the production standard, and correctly
  reasoned *why* (real queries mix both needs) once prompted.
- **Decision 2 — reranking: strong on first pass, without the term.**
  Described the cross-encoder mechanism unprompted ("pays attention
  across the document and candidate text") before knowing its name.
  - **Bi-encoder** (initial retrieval): query and chunk embedded
    *independently*, compared cheaply via cosine similarity/dot product.
    Fast — nothing interacts directly, just comparing precomputed points.
  - **Cross-encoder** (reranking): query + candidate fed through the
    model *together*, attention runs across both — more accurate, and
    exactly why it's slow: can't be precomputed, runs fresh per
    candidate per query.
  - **Why accept the cost:** only the top 2–3 results actually reach
    generation, so precision at the very top matters more than broad
    recall across fifty decent candidates.
  🎯 Bi-encoder/cross-encoder is exactly the kind of precise vocabulary
  that could sit as a fine-print pair inside the retrieval box.
- **Decision 3 — query rewriting: correct and complete.** Named it
  correctly, cost correctly identified as latency from the extra model
  call. Added nuance: also a small correctness risk — the rewrite is
  itself a model call, so it can drift from the user's actual intent
  (over-clarify a vague question into the *wrong* specific one).
- **Decision 4 — top-k: right instinct, mechanism needed a fix.**
  Too small → correct, unprompted: the right chunk is simply absent from
  the results. Too large → instinct right (something breaks), mechanism
  off: it's not search cost that suffers (that's the indexing decision's
  territory), it's the **downstream generation prompt** — extra chunks
  are extra tokens, extra cost/latency, and diluted attention, i.e. the
  needle isn't lost *searching*, it's buried *in the prompt* the model
  has to read (ties directly to stage 6's "lost in the middle"). Correct
  closing instinct: k is a tuned parameter, same spirit as chunk size
  in stage 2 — no universal right answer, depends on corpus/question type.
- **The metric trap — resolved, correct and complete on first pass.**
  recall@k is retrieval-only: measures whether the right chunk made the
  top-k, nothing about rank/salience within those results or whether
  generation actually used it. Correctly separated two distinct bugs
  behind the same symptom: generation *ignoring* the right chunk for a
  worse one, vs. generation *hallucinating* despite having it.
  Sharp phrasing: *"good retrieval metrics are necessary but not
  sufficient — you have to evaluate the final answer, not just the
  retrieval step in isolation."*
  🎯 Directly the reason this project's Video 9 exists and the reason
  "eval blind spots" earns its own line on the failure strip — confirms
  that failure mode as real and load-bearing, not padding.

Retrieval stage — done. All four decisions (dense/sparse/hybrid, rerank,
query rewrite, top-k) plus the metric trap, drilled.

## Stage 6 — Generation

- **Strong on first pass, unprompted:** named contradictory retrieved
  context and lost-in-the-middle-style information loss as causes; named
  both real mitigations — citation strategy (make the model point at its
  source) and explicit permission to answer "I don't know" rather than
  paper over a gap.
- **The "why" underneath, added:** models are **fluency machines first**
  — producing smooth, confident text is the default; grounding strictly
  in provided context is not automatic, it has to be deliberately
  prompted and tested for. Given the right chunk, a model *often* uses it
  correctly, not *always* — nothing in training specifically rewards "I
  don't know" over sounding sure. Direct throughline back to video 1's
  "confident guessing."
- 🎯 **What makes this failure a different class, not just another item:**
  every other failure in the pipeline is a failure of *getting the right
  information to the model* (bad extraction, severed chunk, wrong
  embedding model, stale index, weak retrieval). Generation's failure is
  the only one that happens with the right information already,
  verifiably, in hand — a failure of *use*, not *delivery*. Practical
  consequence: debugging it means checking the actual prompt sent to the
  model, not retrieval logs. Strong candidate for a poster callout that
  distinguishes the generation box from the other five.

**All six pipeline stages now drilled.** See "Pattern noticed" below for
the throughline across the whole drill.

## Adjacent topic — Observability (interview tangent, off the six-stage pipeline)

Not a pipeline stage — surfaced from a real interview question ("which
observability stack are you using") that has two distinct halves.

- **Traditional observability** — already known reasonably well (logs,
  general infra monitoring). Vocabulary worth having ready: the three
  pillars are **metrics, logs, traces**; tool names — Datadog,
  Grafana+Prometheus, CloudWatch, ELK stack.
- **LLM/RAG observability — new territory, taught from scratch.** One-line
  frame to lead an answer with: *"traditional observability tells you if
  the system is running correctly; LLM observability tells you if it's
  reasoning correctly."* Uptime/latency say nothing about whether
  retrieval found the right chunks or generation used them.
  - **Four things this tooling does:** (1) trace a request through the
    whole chain — question → retrieved chunks + scores → assembled
    prompt → answer; (2) evaluation/scoring — faithfulness/groundedness,
    relevance, correctness, sometimes LLM-as-judge; (3) prompt/version
    tracking, so a quality regression traces back to what changed;
    (4) cost/latency broken down *per stage*, not one end-to-end number.
  - 🎯 Point (2) is directly the fix for **eval blind spots** — the fifth
    failure mode already on the poster's failure strip
    (`videos/09-failure-modes.md`). Worth knowing this tooling category
    exists specifically because recall@k-style metrics aren't enough —
    reinforces that failure mode is a real, named industry problem, not
    an invented one for the chart.
  - **Three tools, differentiated** (not memorized before this):
    **LangSmith** (LangChain-team, best if already in LangChain/LangGraph)
    · **Langfuse** (open-source, self-hostable, framework-agnostic)
    · **Arize Phoenix** (open-source, strongest at embedding/retrieval
    visualization — clustering, drift detection — plus RAG eval templates).
  - Answer-ready line: *"depends on the framework and whether self-hosting
    matters — LangSmith if already in LangChain, Langfuse for open-source
    self-hosted, Phoenix if embedding-space drift visualization is the
    specific need."*

## Pattern noticed

Both fumbles so far were the same shape: collapsing two or three adjacent
stages into one blurred stage ("ingestion" absorbing chunking's job,
"ingestion" absorbing embedding's job). The fix in both cases wasn't new
information — it was insisting each stage have its own distinct verb
(extract / split / vectorize / index / retrieve / generate) and its own
distinct failure that the others can't cause. That distinction-per-stage
habit is worth carrying into the rest of the drill.
