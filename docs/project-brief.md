# Project Brief — Giant Wall Charts

## What this is

A publishing venture producing premium, large-format (36"x24") educational
wall posters — laminated tri-folds and rigid prints — in STEM, philosophy,
and humanities subjects. Designed with a Swiss/Bauhaus visual language:
disciplined grid, restrained palette, tasteful white space, clear typographic
hierarchy. Brand home: **giantwallcharts.com**.

Branding inspiration note: the confident, oversized, friendly-slab-serif
energy of the "Giant Hamburger" fast food chain (California) is a useful mood
reference — big, unapologetic, a little playful, without losing precision.

## Business model

- **Print-on-demand (POD) first.** Every new title launches via POD
  (Printful/Printify-style) to test real demand with near-zero upfront
  inventory risk.
- **Scale winners, break-even on prestige projects.** Some titles (e.g. the
  Quantum Gravity History poster) are pursued for their intellectual/prestige
  value even if they're not big sellers. Titles that do sell get moved to
  bulk print runs (e.g. Amazon FBA) once demand is proven, where per-unit
  economics improve substantially over POD.
- **"If I can make any money at all in initial POD sales, I'm not bothered."**
  The bar for shipping v1 of a new title is low. The point of POD is
  learning what sells, not maximizing margin on day one.

## Product philosophy: cultivate many ideas, then bear down

The founder's working style is to follow inspiration across many interests
at once early on (physics, philosophy, RAG/AI infrastructure, classical
languages, cinema, etc.), then focus hard on whichever idea is actually
moving toward completion. The poster line is structured to match this: each
new topic is a cheap, contained bet (design time + one print run), and the
line as a whole only needs a few genuine winners to fund the more niche or
prestige titles.

## The "concept + platform" format

RAG Concepts / RAG on AWS establishes a repeatable two-poster format for any
technical topic that has both a vendor-neutral conceptual core and a
dominant-platform implementation:

1. **Concept poster** — the vendor-neutral pipeline/spine, evergreen,
   doesn't age with any one vendor's product names.
2. **Platform poster** — the same spine/topology, with stages mapped to a
   specific vendor's actual services (e.g. AWS Bedrock/Kendra/OpenSearch for
   RAG). Sold as a matched companion to the concept poster.

This format is designed to be repeated: e.g. "Kubernetes Concepts" +
"Kubernetes on AWS/EKS," or eventually "...on GCP" / "...on Azure" variants
of any topic once it's proven to sell. Owning the concept-to-implementation
pairing, consistently, across topics is a real content moat once there are
several of these.

**Topology rule:** the platform poster's stage order and rough footprint
must stay closely aligned with the concept poster's — an expert should be
able to find "Retrieval" in the same place on both posters without
re-orienting — while individual stages are allowed to internally branch or
reshape to fit what the platform actually offers (e.g. Retrieval forking
into OpenSearch / Kendra / a vector DB on Bedrock). "Topology close, not
identical." See `versioning-scheme.md` for how this interacts with major/minor
versioning.

## Design as signal, not just decoration

For fast-moving topics (RAG is the prototype case), the poster's structural
spine is deliberately built to be relatively slow-moving across versions,
even as specific terms/techniques inside it get refreshed. The goal: an
experienced practitioner should be able to glance at the macro-structure of
the poster and immediately know roughly which version/era they're looking
at — similar to how a physicist can date a Feynman diagram's era by its
notation conventions, without checking a publication date. This is a
deliberate design constraint, not an accident of not-yet-having-decided
structure. See `versioning-scheme.md`.

## Interview-prep framing (origin of RAG Concepts specifically)

The RAG Concepts poster originated from a personal need: technical interview
screens sometimes require recalling architectural details cold, over the
phone, without notes — and it's easy to fumble broad-glance recall even when
the underlying knowledge is solid. The poster is designed as a "quick review"
artifact for exactly that moment: dense enough to be a genuine reference,
structured enough (via the pipeline spine) to be scannable in well under a
minute.

## Current titles

- **RAG Concepts** — see `charts/rag-concepts/`
- **RAG on AWS** — planned, see `charts/rag-on-aws/`
- **Quantum Gravity History** — the original product concept (dual-lineage
  canonical + covariant thesis through Bryce DeWitt); predates this repo,
  bring existing brief/materials in when ready
