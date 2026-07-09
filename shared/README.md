# shared/

Reusable assets across all charts.

- `scripts/` — generalized version of the spine-scaffold generator, once
  it's proven out across two or more charts (currently, the only
  implementation lives in `charts/rag-concepts/v1/generate_spine.py`; not
  yet extracted into a shared library — do that once RAG on AWS is built
  and the common pattern is clear).
- `templates/` — house color palette (Affinity swatch file) and
  typography scale, once finalized. See `docs/brand-guidelines.md` for
  what's still open here.
