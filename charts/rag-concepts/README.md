# RAG Concepts

Vendor-neutral "quick review" poster for the RAG (Retrieval-Augmented
Generation) pipeline. Origin: a personal need to recall architectural
details cold during phone technical screens — designed to be scannable at
a glance, not just a reference to read slowly.

Companion poster: **RAG on AWS** (`../rag-on-aws/`) — same spine topology,
stages mapped to specific AWS services. See `docs/project-brief.md` for the
"concept + platform" format this pair establishes.

## Content outline (locked, v1)

Six-stage pipeline spine, left to right:

1. **Ingestion** — source formats (PDF, HTML, structured JSON, API pulls),
   the parsing decision (layout-aware vs plain text extraction)
2. **Chunking** — fixed-size vs recursive vs semantic, one-line tradeoff
   each solves (cost/speed vs coherence)
3. **Embedding** — model choice tradeoffs (dimensionality vs cost vs domain
   fit), single-vector vs multi-vector (e.g. ColBERT-style)
4. **Indexing** — vector index types at a glance (HNSW vs IVF vs flat),
   metadata filtering as a first-class concern, not an afterthought
5. **Retrieval** (widened — gets the branching treatment, double width of
   other stages) — dense vs sparse vs hybrid, reranking as a distinct
   sub-stage, query rewriting/expansion, top-k tuning
6. **Generation** — context window budget, citation/grounding strategy,
   handling "no good context found" gracefully

**Bottom strip — failure modes at a glance:**
- Stale index / doc drift
- Retrieval-generation mismatch (right chunks, model ignores them)
- Context overflow / lost-in-the-middle
- Chunk boundary cutting off the answer
- Eval blind spots (looks good on recall@k, fails in production)

## Design decisions specific to this title

- Retrieval stage is exactly double the width of the other five stages
  (weight 2 vs weight 1 each in the generator config) — this is the stage
  people most often fumble recalling under interview pressure, so it gets
  the visual and content weight to match.
- Failure-modes strip runs full width along the bottom, separate register
  from the clean pipeline diagram above it — reads like field notes, not
  part of the spine itself.
- This spine's topology (six stages, Retrieval widened with four
  sub-branches: dense/sparse/hybrid/rerank) is the reference topology that
  `rag-on-aws` must stay closely aligned to.

## Status

- v1 content outline: locked
- v1 structural scaffold: generated (`v1/generate_spine.py` ->
  `v1/rag_concepts_spine_v1.svg`)
- Not yet opened in Affinity Designer for hand-finishing (illustration,
  final typography, house palette application)
- Version badge in the scaffold is a placeholder fill, not yet a real spot
  color swatch (house palette not finalized — see
  `docs/brand-guidelines.md`)

## Regenerating / iterating the scaffold

`v1/generate_spine.py` is self-contained (Python 3 standard library only).
Edit the `STAGES`, `RETRIEVAL_BRANCHES`, `FAILURE_MODES`, or geometry
constants at the top of the file, then run:

```
python3 generate_spine.py
```

This regenerates `rag_concepts_spine_v1.svg` in place. Any manual edits
already made in Affinity to a previously-imported scaffold are NOT
preserved by re-running the script — treat the script as the source of
truth for structure only, and re-apply hand-finishing after a structural
regeneration.
