#!/usr/bin/env python3
"""Build a compact review sheet from exported carousel PNG files."""

from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a carousel contact sheet")
    parser.add_argument("--input-dir", required=True, help="Directory with slide-*.png")
    parser.add_argument("--output", required=True, help="Output JPG or PNG")
    parser.add_argument("--columns", type=int, default=3, help="Number of columns")
    parser.add_argument("--thumb-width", type=int, default=340, help="Thumbnail width")
    parser.add_argument("--gap", type=int, default=18, help="Gap and outer margin")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_dir = Path(args.input_dir).expanduser().resolve()
    output = Path(args.output).expanduser().resolve()
    slides = sorted(input_dir.glob("slide-*.png"))

    if not slides:
        raise RuntimeError(f"No slide-*.png files found in {input_dir}")
    if args.columns < 1:
        raise ValueError("--columns must be at least 1")

    with Image.open(slides[0]) as first:
        ratio = first.height / first.width

    thumb_height = round(args.thumb_width * ratio)
    rows = math.ceil(len(slides) / args.columns)
    width = args.columns * args.thumb_width + (args.columns + 1) * args.gap
    height = rows * thumb_height + (rows + 1) * args.gap
    sheet = Image.new("RGB", (width, height), "#171416")

    for index, path in enumerate(slides):
        with Image.open(path) as slide:
            thumb = slide.convert("RGB").resize(
                (args.thumb_width, thumb_height), Image.Resampling.LANCZOS
            )
        column = index % args.columns
        row = index // args.columns
        x = args.gap + column * (args.thumb_width + args.gap)
        y = args.gap + row * (thumb_height + args.gap)
        sheet.paste(thumb, (x, y))

    output.parent.mkdir(parents=True, exist_ok=True)
    save_kwargs = {"quality": 90, "optimize": True} if output.suffix.lower() in {".jpg", ".jpeg"} else {}
    sheet.save(output, **save_kwargs)
    print(f"[OK] Wrote {output} from {len(slides)} slides ({width}x{height})")


if __name__ == "__main__":
    main()
