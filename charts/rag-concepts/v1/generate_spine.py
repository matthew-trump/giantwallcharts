#!/usr/bin/env python3
"""
Giant Wall Charts — Pipeline Spine Scaffold Generator
------------------------------------------------------
Generates a vector SVG scaffold for a 36x24in landscape wall poster,
laid out around a left-to-right "pipeline spine" with weighted stage
widths (retrieval gets extra room for branching).

This is a STRUCTURE generator, not final art. Output is meant to be
imported into Affinity Designer as a starting layer, then hand-edited
freely — move nodes, resize boxes, add illustration, etc. Re-run this
script with different WEIGHTS/STAGES to produce a topology-matched
companion poster (e.g. "RAG on AWS") or a new major version.

Units: SVG uses points (1in = 72pt) so the file opens in Affinity at
the exact physical size when the document is set to inches.
"""

IN = 72  # points per inch

# ---------------------------------------------------------------------
# CONFIG — tweak these to iterate on the layout
# ---------------------------------------------------------------------

PAGE_W_IN = 36
PAGE_H_IN = 24
BLEED_IN = 0.125       # standard print bleed
SAFE_MARGIN_IN = 0.75  # inset from trim edge for live content

HEADER_H_IN = 2.25     # top zone: title / logo / version badge area
FOOTER_H_IN = 2.5      # bottom zone: failure-modes strip
STAGE_GAP_IN = 0.35    # horizontal gap between stage boxes

# Stage name -> relative width weight. Retrieval is widened for the
# dense/sparse/hybrid + reranking branching cluster.
STAGES = [
    ("INGESTION",  1.0),
    ("CHUNKING",   1.0),
    ("EMBEDDING",  1.0),
    ("INDEXING",   1.0),
    ("RETRIEVAL",  2.0),
    ("GENERATION", 1.0),
]

# Sub-branches drawn inside the retrieval stage box (topology hook for
# dense/sparse/hybrid + reranking + query rewriting)
RETRIEVAL_BRANCHES = ["DENSE", "SPARSE", "HYBRID", "RERANK"]

FAILURE_MODES = [
    "Stale index / doc drift",
    "Retrieval-generation mismatch",
    "Context overflow / lost-in-the-middle",
    "Chunk boundary cuts off answer",
    "Eval blind spots (recall@k != prod)",
]

VERSION_MAJOR = 1
VERSION_MINOR = 0

import os
OUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rag_concepts_spine_v1.svg")

# ---------------------------------------------------------------------
# Derived geometry (all in points)
# ---------------------------------------------------------------------

page_w = PAGE_W_IN * IN
page_h = PAGE_H_IN * IN
bleed = BLEED_IN * IN
safe = SAFE_MARGIN_IN * IN
header_h = HEADER_H_IN * IN
footer_h = FOOTER_H_IN * IN
gap = STAGE_GAP_IN * IN

canvas_w = page_w + 2 * bleed
canvas_h = page_h + 2 * bleed

# Trim box sits inset by `bleed` from the outer canvas edge
trim_x0, trim_y0 = bleed, bleed
trim_x1, trim_y1 = bleed + page_w, bleed + page_h

# Safe content box, inset further from trim
safe_x0, safe_y0 = trim_x0 + safe, trim_y0 + safe
safe_x1, safe_y1 = trim_x1 - safe, trim_y1 - safe
safe_w = safe_x1 - safe_x0

# Vertical zones within the safe area
spine_y0 = safe_y0 + header_h
spine_y1 = safe_y1 - footer_h
spine_h = spine_y1 - spine_y0

footer_y0 = spine_y1
footer_y1 = safe_y1

# Horizontal stage layout: divide safe_w among stages by weight, minus gaps
total_weight = sum(w for _, w in STAGES)
n_gaps = len(STAGES) - 1
usable_w = safe_w - n_gaps * gap

stage_boxes = []  # (name, x0, y0, x1, y1)
cursor_x = safe_x0
for name, weight in STAGES:
    w = usable_w * (weight / total_weight)
    x0 = cursor_x
    x1 = cursor_x + w
    stage_boxes.append((name, x0, spine_y0, x1, spine_y1))
    cursor_x = x1 + gap

# ---------------------------------------------------------------------
# SVG assembly
# ---------------------------------------------------------------------

GUIDE_STROKE = "#00AEEF"      # bright cyan — clearly a non-final guide color
GUIDE_DASH = "6,6"
TRIM_STROKE = "#FF00FF"       # magenta trim/bleed guide (never a real ink color)
SPOT_PLACEHOLDER = "#FF00A6"  # placeholder fill flagged for spot-color swap

svg_parts = []
svg_parts.append(
    f'<svg xmlns="http://www.w3.org/2000/svg" '
    f'width="{PAGE_W_IN}in" height="{PAGE_H_IN}in" '
    f'viewBox="0 0 {canvas_w:.2f} {canvas_h:.2f}">'
)

# --- Layer: bleed / trim / safe guides ---
svg_parts.append('<g id="GUIDES_bleed_trim_safe">')
svg_parts.append(
    f'<rect id="bleed_box" x="0" y="0" width="{canvas_w:.2f}" height="{canvas_h:.2f}" '
    f'fill="none" stroke="{TRIM_STROKE}" stroke-width="0.75" stroke-dasharray="{GUIDE_DASH}"/>'
)
svg_parts.append(
    f'<rect id="trim_box" x="{trim_x0:.2f}" y="{trim_y0:.2f}" '
    f'width="{page_w:.2f}" height="{page_h:.2f}" '
    f'fill="none" stroke="{TRIM_STROKE}" stroke-width="1.25"/>'
)
svg_parts.append(
    f'<rect id="safe_margin_box" x="{safe_x0:.2f}" y="{safe_y0:.2f}" '
    f'width="{safe_w:.2f}" height="{safe_y1 - safe_y0:.2f}" '
    f'fill="none" stroke="{GUIDE_STROKE}" stroke-width="0.75" stroke-dasharray="{GUIDE_DASH}"/>'
)
svg_parts.append('</g>')

# --- Layer: header zone (title / logo / version badge) ---
svg_parts.append('<g id="HEADER_zone">')
svg_parts.append(
    f'<rect id="header_placeholder" x="{safe_x0:.2f}" y="{safe_y0:.2f}" '
    f'width="{safe_w:.2f}" height="{header_h:.2f}" '
    f'fill="none" stroke="{GUIDE_STROKE}" stroke-width="0.75" stroke-dasharray="{GUIDE_DASH}"/>'
)
svg_parts.append(
    f'<text id="title_placeholder" x="{safe_x0 + 12:.2f}" y="{safe_y0 + 48:.2f}" '
    f'font-family="Helvetica, Arial, sans-serif" font-size="42" font-weight="700" '
    f'fill="#111111">RAG PIPELINE — QUICK REVIEW</text>'
)

# Version badge — bottom-right corner of header zone, on its own id
# so the spot color swatch can be assigned directly to this fill in Affinity.
badge_w, badge_h = 1.6 * IN, 0.6 * IN
badge_x = safe_x1 - badge_w
badge_y = safe_y0 + header_h - badge_h
svg_parts.append(
    f'<g id="VERSION_BADGE_spotcolor">'
    f'<rect x="{badge_x:.2f}" y="{badge_y:.2f}" width="{badge_w:.2f}" height="{badge_h:.2f}" '
    f'fill="{SPOT_PLACEHOLDER}"/>'
    f'<text x="{badge_x + 14:.2f}" y="{badge_y + badge_h/2 + 10:.2f}" '
    f'font-family="Helvetica, Arial, sans-serif" font-size="26" font-weight="700" '
    f'fill="#FFFFFF">v{VERSION_MAJOR}<tspan font-size="14" dx="2" dy="1">.{VERSION_MINOR}</tspan></text>'
    f'</g>'
)
svg_parts.append('</g>')  # end HEADER_zone

# --- Layer: spine baseline ---
spine_mid_y = (spine_y0 + spine_y1) / 2
svg_parts.append('<g id="SPINE_baseline">')
svg_parts.append(
    f'<line x1="{safe_x0:.2f}" y1="{spine_mid_y:.2f}" x2="{safe_x1:.2f}" y2="{spine_mid_y:.2f}" '
    f'stroke="#111111" stroke-width="2"/>'
)
svg_parts.append('</g>')

# --- Layer: stage boxes ---
svg_parts.append('<g id="STAGES">')
for i, (name, x0, y0, x1, y1) in enumerate(stage_boxes, start=1):
    w = x1 - x0
    h = y1 - y0
    is_retrieval = name == "RETRIEVAL"
    svg_parts.append(f'<g id="STAGE_{i:02d}_{name}">')
    svg_parts.append(
        f'<rect x="{x0:.2f}" y="{y0:.2f}" width="{w:.2f}" height="{h:.2f}" '
        f'fill="none" stroke="#111111" stroke-width="1.5"/>'
    )
    svg_parts.append(
        f'<text x="{x0 + 10:.2f}" y="{y0 + 34:.2f}" '
        f'font-family="Helvetica, Arial, sans-serif" font-size="24" font-weight="700" '
        f'fill="#111111">{i}. {name}</text>'
    )
    # Retrieval gets its branching sub-cluster drawn inside, as a topology hook
    if is_retrieval:
        n = len(RETRIEVAL_BRANCHES)
        sub_pad = 16
        sub_top = y0 + 56
        sub_h = (h - (sub_top - y0) - sub_pad * (n + 1)) / n
        for j, branch in enumerate(RETRIEVAL_BRANCHES):
            by0 = sub_top + sub_pad + j * (sub_h + sub_pad)
            svg_parts.append(
                f'<rect id="BRANCH_{branch}" x="{x0 + 14:.2f}" y="{by0:.2f}" '
                f'width="{w - 28:.2f}" height="{sub_h:.2f}" '
                f'fill="none" stroke="#111111" stroke-width="1" stroke-dasharray="4,3"/>'
            )
            svg_parts.append(
                f'<text x="{x0 + 24:.2f}" y="{by0 + sub_h/2 + 6:.2f}" '
                f'font-family="Helvetica, Arial, sans-serif" font-size="15" '
                f'fill="#333333">{branch}</text>'
            )
    svg_parts.append('</g>')
svg_parts.append('</g>')  # end STAGES

# --- Layer: footer strip (failure modes) ---
svg_parts.append('<g id="FOOTER_failure_modes_strip">')
svg_parts.append(
    f'<rect x="{safe_x0:.2f}" y="{footer_y0:.2f}" width="{safe_w:.2f}" height="{footer_y1 - footer_y0:.2f}" '
    f'fill="none" stroke="#111111" stroke-width="1.5"/>'
)
svg_parts.append(
    f'<text x="{safe_x0 + 10:.2f}" y="{footer_y0 + 28:.2f}" '
    f'font-family="Helvetica, Arial, sans-serif" font-size="20" font-weight="700" '
    f'fill="#111111">FAILURE MODES AT A GLANCE</text>'
)
n_fm = len(FAILURE_MODES)
fm_col_w = safe_w / n_fm
for i, fm in enumerate(FAILURE_MODES):
    fx = safe_x0 + i * fm_col_w
    svg_parts.append(
        f'<line x1="{fx:.2f}" y1="{footer_y0 + 36:.2f}" x2="{fx:.2f}" y2="{footer_y1:.2f}" '
        f'stroke="#CCCCCC" stroke-width="0.75"/>'
    )
    # simple word-wrap: split into two lines on the middle space
    words = fm.split(" ")
    mid = len(words) // 2 or 1
    line1 = " ".join(words[:mid])
    line2 = " ".join(words[mid:])
    svg_parts.append(
        f'<text x="{fx + 10:.2f}" y="{footer_y0 + 60:.2f}" '
        f'font-family="Helvetica, Arial, sans-serif" font-size="14" fill="#111111">{line1}</text>'
    )
    svg_parts.append(
        f'<text x="{fx + 10:.2f}" y="{footer_y0 + 78:.2f}" '
        f'font-family="Helvetica, Arial, sans-serif" font-size="14" fill="#111111">{line2}</text>'
    )
svg_parts.append('</g>')

svg_parts.append('</svg>')

with open(OUT_PATH, "w") as f:
    f.write("\n".join(svg_parts))

print(f"Wrote {OUT_PATH}")
print(f"Canvas: {canvas_w/IN:.3f}in x {canvas_h/IN:.3f}in (incl. {BLEED_IN}in bleed)")
print(f"Trim:   {PAGE_W_IN}in x {PAGE_H_IN}in")
print("Stage widths (in):")
for name, x0, y0, x1, y1 in stage_boxes:
    print(f"  {name:12s} {((x1-x0)/IN):.2f}in")
