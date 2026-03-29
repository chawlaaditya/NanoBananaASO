#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a simple review contact sheet from normalized App Store slides.")
    parser.add_argument("input_dir", type=Path, help="Directory containing normalized slide PNGs")
    parser.add_argument("output_file", type=Path, help="Output PNG path for the contact sheet")
    parser.add_argument("--columns", type=int, default=3, help="Number of columns")
    parser.add_argument("--thumb-width", type=int, default=220, help="Thumbnail width")
    parser.add_argument("--padding", type=int, default=24, help="Grid padding")
    parser.add_argument("--label-height", type=int, default=36, help="Space for the filename label")
    args = parser.parse_args()

    paths = sorted(args.input_dir.glob("*.png"))
    if not paths:
        raise SystemExit(f"No PNG files found in {args.input_dir}")

    with Image.open(paths[0]) as first:
        thumb_height = int(round(args.thumb_width * first.height / first.width))

    rows = (len(paths) + args.columns - 1) // args.columns
    sheet_w = args.columns * (args.thumb_width + args.padding) + args.padding
    sheet_h = rows * (thumb_height + args.label_height + args.padding) + args.padding

    sheet = Image.new("RGB", (sheet_w, sheet_h), "#111111")
    draw = ImageDraw.Draw(sheet)

    for i, path in enumerate(paths):
        with Image.open(path) as img:
            thumb = img.convert("RGB").resize((args.thumb_width, thumb_height), Image.Resampling.LANCZOS)
        x = args.padding + (i % args.columns) * (args.thumb_width + args.padding)
        y = args.padding + (i // args.columns) * (thumb_height + args.label_height + args.padding)
        sheet.paste(thumb, (x, y))
        draw.text((x, y + thumb_height + 8), path.stem, fill="white")

    args.output_file.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(args.output_file)
    print(args.output_file)


if __name__ == "__main__":
    main()
