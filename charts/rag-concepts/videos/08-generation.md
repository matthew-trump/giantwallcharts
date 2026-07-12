# Video 8 — Stage 6: Generation

**Target:** 10–12 min · **Audience:** watched the series so far, or
arriving cold · **Job:** the viewer understands generation as "turning
retrieved chunks into a grounded, checkable answer" and can name why
having the right chunks in the prompt doesn't guarantee the model uses them.

## Hook (0:00–1:30)

- War story: retrieval does everything right — the exact chunk containing
  the answer is sitting in the prompt, verified, present. The model
  answers wrong anyway, or worse, contradicts the very text it was given.
  Someone debugging this assumes retrieval failed and spends a day
  re-tuning the retriever — the actual bug was generation ignoring
  correct context, a completely different failure with an identical
  symptom.
- This is why generation gets its own box instead of being an
  afterthought: "the model has the right information" and "the model
  used the right information" are two different claims.

## What generation actually does (1:30–3:00)

- Job in one sentence: **retrieved chunks + question in, a grounded
  answer out** — grounded meaning traceable back to the source text, not
  invented.
- The whole point of every stage before this one was to get the right
  text in front of the model. Generation is where that investment either
  pays off or gets squandered.

## The decision: context budget, citations, weak retrieval (3:00–7:00) — core segment

- **Context budget:** how much retrieved text actually fits, and where it
  sits in the prompt. Models don't weight all context equally —
  information can get lost in the middle of a long prompt even when it's
  technically present ("lost in the middle"). More context isn't
  automatically better context.
- **Citation strategy:** does the answer point back to *which* chunk
  supported *which* claim? This is what makes an answer checkable instead
  of just plausible-sounding — arguably RAG's biggest practical advantage
  over an ungrounded chatbot, and easy to skip if you're not deliberate
  about it.
- **What to do when retrieval came back weak:** if the retrieved chunks
  are marginal or contradictory, does the model say so — "I couldn't find
  a clear answer in the documents" — or does it paper over the gap with
  confident, fluent prose? This is a design decision, not an accident;
  it has to be prompted and tested for on purpose.
- DRAW THIS: two versions of the same generation step — one where the
  model silently ignores a contradicting chunk and states the wrong
  answer with full confidence, one where the model surfaces the
  contradiction and cites both sources, flagging the uncertainty.

## Grounding vs fluency — the hook, paid off (7:00–8:30)

- Language models are fluency machines first — they will produce a
  smooth, confident-sounding answer whether or not it's actually
  supported by the context they were given. Grounding is not the model's
  default behavior; it's a behavior you have to prompt for, test for, and
  sometimes fine-tune for.
- This is the throughline back to video 1's "confident guessing" — RAG
  reduces the *chances* of hallucination by giving the model real
  material to work from, but doesn't eliminate the model's tendency to
  sound sure of itself regardless.

## How to tell generation is broken (8:30–9:30)

- The tell: the correct chunk is verifiably present in what was sent to
  the model (check the actual prompt, not just the retrieval logs), and
  the answer still contradicts or ignores it. Distinct from every upstream
  failure — this is the one case where retrieval did its job perfectly
  and the failure happened anyway.

## Close (9:30–10:30)

- Recap: generation's job (chunks + question → grounded answer), its
  decisions (context budget, citations, handling weak retrieval), its
  signature failure (right chunks, ignored anyway).
- Chart beat: "sixth and final box — the pipeline's last stop, and the
  only one users actually see."
- Tease next: "we've now walked all six stages and all six failure
  points individually — last video pulls every failure mode together and
  asks: when RAG breaks in the wild, which of these is usually to blame?"

## Capture for the chart (fill in after recording)

- [ ] Did the "silently ignores vs. surfaces the contradiction" drawing
      land?
- [ ] Citation strategy — does it deserve its own poster line, given it's
      RAG's biggest practical selling point?
- [ ] "Lost in the middle" — fine print or full callout?
- [ ] Any explaining twice → candidate fine print.
