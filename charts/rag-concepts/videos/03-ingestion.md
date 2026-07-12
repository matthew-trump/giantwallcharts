# Video 3 — Stage 1: Ingestion

**Target:** 10–12 min · **Audience:** watched #1/#2, or arriving cold off
the title · **Job:** the viewer understands ingestion as "turning real-world
documents into clean, structured text" and can name the two or three ways
this quietly goes wrong before anything downstream even runs.

## Hook (0:00–1:30)

- War story: a two-column PDF — say, a policy document laid out like a
  newspaper — gets read by a naive extractor left-to-right across the full
  page width instead of down each column. Sentences from column A splice
  into sentences from column B. The document looks fine to a human, reads
  as nonsense to the pipeline.
- The twist: nothing downstream — not chunking, not embedding, not the
  fanciest reranker — can recover from this. Ingestion is the pipeline's
  foundation. Garbage laid in the foundation stays garbage no matter how
  good the building above it is.

## What ingestion actually does (1:30–3:30)

- Job in one sentence: **raw documents in, clean text + metadata out.**
- "Documents" is doing a lot of work: PDFs, Word docs, HTML pages, Slack
  exports, scanned images, spreadsheets — each with its own way of
  encoding structure (or hiding it).
- Metadata isn't optional extra credit — source, title, section, date,
  author travel with the text from here on and are what later stages use
  for filtering and citations. Lose it here, it's gone for good.

## The decision: layout-aware vs plain extraction (3:30–6:30) — core segment

- Plain extraction: pull the text stream, ignore visual layout. Fast,
  cheap, works great on simple single-column text.
- Layout-aware extraction: understand columns, tables, headers, reading
  order — treat the page as a structure, not a string.
- DRAW THIS: the two-column PDF example from the hook, side by side — naive
  left-to-right extraction producing spliced nonsense vs layout-aware
  extraction producing the correct sentence order.
- The tradeoff is real, not a solved problem: layout-aware tools cost more
  (compute, sometimes literal API fees) and still fail on weird documents.
  Plain extraction is a legitimate choice when your source documents are
  genuinely simple and uniform.
- Tables deserve their own beat: a table flattened to plain text loses its
  grid — rows and columns collapse into a run-on sentence that means
  something different. Show one example if time allows.

## Other ingestion failure modes, briefly (6:30–8:30)

- Scanned/image documents: no text layer at all, needs OCR — a whole
  additional error surface (misread characters, especially in tables and
  handwriting).
- Boilerplate noise: headers, footers, page numbers, nav menus from
  scraped HTML — junk that survives extraction and pollutes every chunk
  it touches.
- Encoding/language issues: mixed encodings, non-English text, special
  characters — silent corruption that's invisible until someone searches
  for the exact phrase that got mangled.
- One line each; this is a "know these exist" pass, not deep dives.

## How to tell ingestion is broken (8:30–10:00)

- The tell: answers are wrong in a way that traces back to *garbled
  source text*, not to retrieval or generation. If you paste the actual
  retrieved chunk into a doc and a human squints and can't parse it
  either — that's an ingestion problem, not a model problem.
- Practical habit: spot-check extracted text against the source document
  before building anything on top of it. Five minutes here saves days of
  debugging retrieval "failures" that were never retrieval's fault.

## Close (10:00–11:00)

- Recap: ingestion's job (clean text + metadata), its central decision
  (layout-aware vs plain), and its signature failure (structure lost,
  silently).
- Chart beat: "this is the first box on the wall chart — first because
  everything else stands on it."
- Tease next: "clean text still isn't retrievable text — next video, how
  we cut it into pieces without cutting through the answer."

## Capture for the chart (fill in after recording)

- [ ] Did the two-column PDF example land, or did a better failure story
      surface live?
- [ ] Table-flattening — worth its own line in the box, or fine print?
- [ ] Which "other failure modes" got cut for time — signal they're
      lower priority for the poster too?
- [ ] Any explaining twice → candidate fine print or margin note.
