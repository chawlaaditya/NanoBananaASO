#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def normalize(image: Image.Image, width: int, height: int) -> Image.Image:
    target_ratio = width / height
    image = image.convert("RGB")
    src_w, src_h = image.size
    src_ratio = src_w / src_h

    if src_ratio > target_ratio:
        new_w = int(round(src_h * target_ratio))
        left = max(0, (src_w - new_w) // 2)
        image = image.crop((left, 0, left + new_w, src_h))
    elif src_ratio < target_ratio:
        new_h = int(round(src_w / target_ratio))
        top = max(0, (src_h - new_h) // 2)
        image = image.crop((0, top, src_w, top + new_h))

    return image.resize((width, height), Image.Resampling.LANCZOS)


def main() -> None:
    parser = argparse.ArgumentParser(description="Normalize generated App Store slides to a fixed portrait size.")
    parser.add_argument("input_dir", type=Path, help="Directory containing generated slide PNGs")
    parser.add_argument("output_dir", type=Path, help="Directory for normalized slide PNGs")
    parser.add_argument("--width", type=int, default=1320, help="Target width")
    parser.add_argument("--height", type=int, default=2868, help="Target height")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    files = sorted(args.input_dir.glob("*.png"))
    if not files:
        raise SystemExit(f"No PNG files found in {args.input_dir}")

    for path in files:
        out_path = args.output_dir / path.name
        with Image.open(path) as img:
            normalize(img, args.width, args.height).save(out_path)
        print(out_path)


if __name__ == "__main__":
    main()
