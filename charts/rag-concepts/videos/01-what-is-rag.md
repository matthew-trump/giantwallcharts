# Video 1 — What is RAG?

**Target:** 10–12 min · **Audience:** technically curious; no ML background
assumed · **Job of this video:** someone who's used ChatGPT understands what
problem RAG solves and how, at the "explain it at dinner" level.

## Hook (0:00–1:00)

- Ask a chatbot about YOUR stuff — your company's vacation policy, your
  product's error codes. It either doesn't know, or worse: it answers
  anyway, confidently, wrong.
- Two structural problems, name them now: **frozen knowledge** and
  **confident guessing**. Today: the architecture that fixes both.

## Why the model can't just know (1:00–3:00)

- Training cutoff: the model is a snapshot; the world moved on.
- Private data: your docs were never in the training set, and you don't
  want them to be.
- Hallucination isn't a bug being fixed next release — next-token
  prediction *always* produces an answer-shaped thing.
- **Metaphor to land: a brilliant student taking a closed-book exam on
  material they never studied.** They write beautifully anyway.

## The obvious fixes, and why they fall short (3:00–5:00)

- Retrain the model on your data → costs a fortune, stale again tomorrow.
- Fine-tune → teaches *style and behavior*, unreliable for *facts*; still
  frozen at tuning time. (One line only — deeper compare later.)
- Paste all your docs into the prompt → context windows are finite, big
  contexts cost money, and models lose things in the middle of long
  context. Works right up until it doesn't.

## The RAG idea (5:00–7:30) — core segment

- Turn the closed-book exam into an **open-book exam**: don't make the
  model know it, let it *look it up*.
- Unpack the acronym in operating order: **Retrieve** the few most
  relevant passages from your documents → **Augment** the prompt with
  them → **Generate** an answer grounded in what was found.
- DRAW THIS: question → search box over a stack of docs → top 3 passages
  → stapled into the prompt → answer with citations.
- Walk one concrete example end to end (vacation-policy question against
  an HR handbook). Show the assembled prompt on screen — the moment
  people "get it" is seeing retrieved text sitting inside the prompt.

## What this buys you — and what it doesn't (7:30–9:30)

- Buys: fresh answers (update the docs, not the model), private
  knowledge, **citations you can check**, smaller/cheaper models doing
  better work.
- Doesn't buy: correctness for free. If retrieval brings back the wrong
  passage, generation dresses it in confidence. Garbage in, eloquent
  garbage out. (Plants the whole rest of the series.)

## When RAG / fine-tuning / long context (9:30–11:00)

- One rule of thumb each: RAG for *knowledge that changes or is private*;
  fine-tuning for *form, tone, and behavior*; long-context for *one-off
  questions over a small, static pile*.
- They compose — not rivals. Most real systems: RAG + a well-prompted
  base model.

## Close (11:00–11:30)

- "RAG in practice is a pipeline of six decisions — and each one has a
  way to quietly ruin your answers. Next video: the whole pipeline in
  fifteen minutes."
- Chart beat: this series is me designing a wall chart of this material
  in public. (No link yet — it doesn't exist. Plant only.)

## Capture for the chart (fill in after recording)

- [ ] Which metaphor landed — open-book exam or something better found live?
- [ ] Did the "buys / doesn't buy" list want to be on the poster (header
      zone? margin note?)
- [ ] The RAG-vs-fine-tune-vs-long-context rule of thumb: poster-worthy?
- [ ] Anything explained twice → candidate fine print.
