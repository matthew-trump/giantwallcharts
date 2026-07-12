# Video 9 — Why RAG Fails in Production (bonus)

**Target:** 12–15 min · **Audience:** watched the series, or arriving cold
via the most clickable title in the lineup · **Job:** the viewer gets a
standalone diagnostic tour of the five failure modes that live at the
seams *between* stages — this video maps 1:1 onto the poster's bottom
failure-modes strip.

## Hook (0:00–1:30)

- Across the last six videos, every stage got its own "how to tell it's
  broken" moment — and nearly every one of those failures didn't live
  *inside* a stage, it lived in the handoff *between* two stages. RAG
  rarely fails because one component is bad in isolation. It fails at the
  seams.
- Today: all five seam failures in one place, as a diagnostic checklist —
  "my RAG system is wrong, where do I even start looking."

## Why seams, not stages (1:30–2:30)

- DRAW THIS: the six-stage pipeline as boxes with arrows between them —
  circle the *arrows*, not the boxes. Each stage can individually pass
  its own tests and the connection between two passing stages can still
  be broken (mismatched assumptions, stale handoffs, lost metadata).
- This reframes debugging: don't just ask "is retrieval good" and "is
  generation good" — ask "does what retrieval hands off match what
  generation expects, right now, today."

## The five failures (2:30–10:30) — core segment, ~90 seconds each

1. **Stale index / doc drift** (seam: indexing → retrieval) — the index
   is a snapshot; source documents changed and the index didn't. Every
   downstream stage runs perfectly on outdated ground truth. Fix: a real,
   owned re-indexing cadence — not "eventually."
2. **Retrieval-generation mismatch** (seam: retrieval → generation) — the
   right chunk is IN the prompt, model uses it wrong or not at all
   (video 8's whole hook). Fix: verify the actual prompt sent, not just
   retrieval logs; test grounding behavior deliberately.
3. **Context overflow / lost-in-the-middle** (seam: retrieval → generation)
   — too much retrieved text, or the right piece buried mid-prompt where
   attention is weakest. Fix: tighter top-k, better chunk ranking,
   position-aware prompt construction.
4. **Chunk boundary cuts the answer** (seam: chunking → embedding →
   retrieval) — the answer was split across two chunks at ingestion/
   chunking time, and no later stage can stitch it back together
   (video 4's whole hook). Fix: structure-aware chunking, overlap, or
   testing chunk boundaries against real Q&A pairs.
5. **Eval blind spots** — not a seam between two pipeline stages but a
   seam between *the system and how you're judging it*: metrics like
   recall@k measure something real but not the thing that matters
   (final answer correctness) — video 7's whole hook. Fix: evaluate
   end-to-end answers against ground truth, not just retrieval in
   isolation.
- For each: one sentence on what it looks like from the outside (the
  symptom a user or developer actually sees) paired with one sentence on
  where to look first.

## The diagnostic order (10:30–12:00)

- When an answer is wrong, work backward in a fixed order rather than
  guessing: (1) is the source document itself correct and current? (2)
  is the index current with that document? (3) was the right chunk
  actually retrieved — check retrieval logs directly? (4) was that chunk
  actually in the final prompt sent to the model? (5) only now suspect
  the model's reasoning itself.
- The point: four of these five checks are cheaper and faster than
  assuming "the model is just bad" and reaching for a bigger model or a
  reranker as a first move.

## Close (12:00–13:30)

- Recap: five failures, five seams, one diagnostic order — this video is
  effectively the operator's manual for everything the series covered.
- Chart beat: "this bottom strip is the last piece of the wall chart —
  six boxes above it for the stages, five failure points below it for
  where they actually break in the real world. That's the whole poster."
- Series close: point back to video 1 for anyone arriving here first;
  no hard sell, just "the chart itself is up next" once design starts.

## Capture for the chart (fill in after recording)

- [ ] Did the "circle the arrows, not the boxes" framing land as the
      chart's visual logic for the failure strip?
- [ ] Are all five failure modes still the right five after teaching all
      six stages, or did a sixth candidate surface?
- [ ] Diagnostic order (5 steps) — worth compressing onto the poster
      itself (e.g. as a numbered path through the failure strip), or stays
      video-only content?
- [ ] Which failure mode got the strongest reaction/most questions —
      signal for which deserves the most poster weight.
