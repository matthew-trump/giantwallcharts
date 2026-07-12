#!/usr/bin/env python3
"""
Giant Wall Charts — Letter-Size Proof Generator
------------------------------------------------
Takes any draft artifact (SVG scaffold, or a PNG/JPEG exported from
Affinity) and produces an 11x8.5in landscape PDF proof, scaled to fit,
with a header line noting the source file, date, and reduction scale.

Intended use: at any stage of design work, print the latest draft on a
regular letter printer to check layout/proportions on paper. This is a
LAYOUT proof — at ~29% of full poster size, fine print will be tiny;
color is whatever your desktop printer does (not calibrated).

Usage:
    python3 shared/scripts/letter_proof.py <draft.svg|draft.png|draft.jpg>

Writes <draft>_letterproof.pdf next to the input and opens it in
Preview (Cmd+P from there, orientation is already landscape).
Pass --no-open to skip opening.

Requires Google Chrome (used headlessly to render the PDF).
Python 3 standard library only otherwise.
"""

import base64
import datetime
import os
import re
import subprocess
import sys
import tempfile

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

MIME = {
    ".svg": "image/svg+xml",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
}

# Letter landscape, with a margin most desktop printers can honor
PAGE_W_IN = 11.0
PAGE_H_IN = 8.5
MARGIN_IN = 0.25
HEADER_H_IN = 0.3


def source_width_inches(path, ext):
    """Best-effort physical width of the source, for the scale note."""
    if ext == ".svg":
        head = open(path, "r", errors="ignore").read(2000)
        m = re.search(r'<svg[^>]*\bwidth="([\d.]+)in"', head)
        if m:
            return float(m.group(1))
    return None


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    no_open = "--no-open" in sys.argv
    if len(args) != 1:
        sys.exit(__doc__)

    src = os.path.abspath(args[0])
    ext = os.path.splitext(src)[1].lower()
    if ext not in MIME:
        sys.exit(f"Unsupported input type {ext!r} — expected .svg, .png, or .jpg")
    if not os.path.exists(src):
        sys.exit(f"No such file: {src}")
    if not os.path.exists(CHROME):
        sys.exit("Google Chrome not found at the expected path — needed to render the PDF.")

    data = base64.b64encode(open(src, "rb").read()).decode("ascii")
    uri = f"data:{MIME[ext]};base64,{data}"

    src_w = source_width_inches(src, ext)
    usable_w = PAGE_W_IN - 2 * MARGIN_IN
    scale_note = (
        f" · printed at ~{usable_w / src_w * 100:.0f}% of full size"
        if src_w else ""
    )
    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    header = f"LETTER PROOF · {os.path.basename(src)} · {stamp}{scale_note}"

    img_h = PAGE_H_IN - 2 * MARGIN_IN - HEADER_H_IN
    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>
  @page {{ size: {PAGE_W_IN}in {PAGE_H_IN}in; margin: 0; }}
  html, body {{ margin: 0; padding: 0; }}
  body {{ width: {PAGE_W_IN}in; height: {PAGE_H_IN}in; box-sizing: border-box;
         padding: {MARGIN_IN}in; font-family: Helvetica, Arial, sans-serif; }}
  .hdr {{ height: {HEADER_H_IN}in; font-size: 8pt; color: #555;
          letter-spacing: 0.03em; }}
  .art {{ width: {usable_w}in; height: {img_h}in;
          display: flex; align-items: center; justify-content: center; }}
  .art img {{ max-width: 100%; max-height: 100%; }}
</style></head><body>
  <div class="hdr">{header}</div>
  <div class="art"><img src="{uri}"></div>
</body></html>"""

    out_pdf = os.path.splitext(src)[0] + "_letterproof.pdf"
    with tempfile.NamedTemporaryFile(
        "w", suffix=".html", delete=False, dir=os.path.dirname(src)
    ) as f:
        f.write(html)
        tmp_html = f.name
    try:
        subprocess.run(
            [
                CHROME,
                "--headless",
                "--disable-gpu",
                "--no-pdf-header-footer",
                f"--print-to-pdf={out_pdf}",
                "file://" + tmp_html,
            ],
            check=True,
            capture_output=True,
            timeout=120,
        )
    finally:
        os.unlink(tmp_html)

    print(f"Wrote {out_pdf}")
    if not no_open:
        subprocess.run(["open", out_pdf])


if __name__ == "__main__":
    main()
