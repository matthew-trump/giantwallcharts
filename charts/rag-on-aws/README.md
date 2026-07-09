# RAG on AWS (planned)

Platform companion to `../rag-concepts/`. Not yet generated.

## Plan

Reuse `../rag-concepts/v1/generate_spine.py` as a base: same `STAGES` list
and weights (Retrieval stays double-width), so the two posters share
identical stage footprints and left-to-right order — per the "topology
close, not identical" rule in `docs/project-brief.md`.

What changes for this poster:
- `RETRIEVAL_BRANCHES` — swap generic dense/sparse/hybrid/rerank labels for
  actual AWS services (e.g. OpenSearch, Kendra, a vector DB on Bedrock,
  Bedrock's reranking support) — this is where the AWS-specific branching
  is expected to be heaviest, matching where Retrieval is already widened
  on the concept poster.
- Other stages (Ingestion, Chunking, Embedding, Indexing, Generation) get
  their own AWS service mappings inside the existing box footprint —
  branching allowed within a stage if a stage needs to fork into multiple
  services (e.g. Indexing forking into OpenSearch vs a Bedrock-native
  vector store), same pattern as Retrieval's sub-cluster.
- Title/output filename changes; house palette and grid stay identical to
  the concept poster (never adopt AWS's own brand colors — see
  `docs/brand-guidelines.md`).

## Status

Not started. Waiting on RAG Concepts v1 to reach a finished, hand-edited
state in Affinity before generating this companion, so any manual topology
tweaks made to the concept poster's spine can be carried over first.
