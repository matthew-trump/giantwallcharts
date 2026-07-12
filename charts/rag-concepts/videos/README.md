# RAG Concepts — Video Series (teaching-first content development)

A YouTube/Rumble series recorded BEFORE hand-finishing the poster design.
Purpose: teaching the material is how the chart's content gets discovered
and pressure-tested — what needs explaining, what diagram gets drawn on
the whiteboard, what tradeoff gets stated out loud is exactly what earns
space on the wall. The series also builds the audience the launch phase
(`docs/roadmap-to-first-sale.md`, Phase 4) will post to.

## Series map

| # | File | Title | Target length |
|---|------|-------|---------------|
| 1 | `01-what-is-rag.md` | What is RAG? | 10–12 min |
| 2 | `02-pipeline-overview.md` | The RAG Pipeline in Six Stages | 12–15 min |
| 3 | `03-ingestion.md` | Stage 1: Ingestion | 10–12 min |
| 4 | `04-chunking.md` | Stage 2: Chunking | 10–12 min |
| 5 | `05-embedding.md` | Stage 3: Embedding | 10–12 min |
| 6 | `06-indexing.md` | Stage 4: Indexing | 10–12 min |
| 7 | `07-retrieval.md` | Stage 5: Retrieval | 13–15 min |
| 8 | `08-generation.md` | Stage 6: Generation | 10–12 min |
| 9 | `09-failure-modes.md` | Why RAG Fails in Production (bonus) | 12–15 min |

Retrieval (#7) gets the longest runtime deliberately — it is double-width
on the poster for the same reason. #9 maps 1:1 onto the poster's
failure-modes strip and is likely the most clickable title in the series.

## Workflow per video

1. Record from the outline. The outlines are beat sheets, not scripts to
   read — timing marks are targets, not stage directions.
2. **Immediately after recording**, fill in the "Capture for the chart"
   section at the bottom of that video's outline file: what did you have
   to explain twice, what did you draw, which phrasing landed, what did
   you say that isn't in the chart outline yet?
3. Reconcile captures against the chart content outline in `../README.md`.
   Content that survived teaching earns wall space; content you skipped
   without missing it probably doesn't.

Note on the "locked" v1 outline: nothing has printed yet, so outline
revisions discovered through teaching are free — including topology
changes (a stage split/merged). Update `../README.md` and the generator
config together if the spine changes; the major/minor discipline in
`docs/versioning-scheme.md` only starts binding once v1 is on sale.

## Format conventions

- 10–15 minutes per video; one idea per segment; a drawn/visual moment in
  every video (these drawings are chart-content prototypes).
- Every video ends with the same beat: "this is one box on a wall chart
  I'm building" — plants the poster without selling it before it exists.
- Each stage video's hook is a concrete failure story that stage causes;
  the fix lands mid-video.
