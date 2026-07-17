#!/usr/bin/env python3
"""Compare a reference UI mockup with a running-product screenshot."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Iterable

try:
    from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageStat
except ImportError as exc:  # pragma: no cover - dependency guidance
    raise SystemExit("Pillow is required: python -m pip install pillow") from exc


def parse_region(value: str) -> tuple[int, int, int, int]:
    try:
        x, y, width, height = (int(item) for item in value.split(","))
    except (TypeError, ValueError) as exc:
        raise argparse.ArgumentTypeError("Region must use x,y,width,height") from exc
    if width <= 0 or height <= 0:
        raise argparse.ArgumentTypeError("Region width and height must be positive")
    return x, y, width, height


def parse_byte(value: str) -> int:
    try:
        parsed = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Expected an integer from 0 to 255") from exc
    if not 0 <= parsed <= 255:
        raise argparse.ArgumentTypeError("Expected an integer from 0 to 255")
    return parsed


def parse_ratio(value: str) -> float:
    try:
        parsed = float(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Expected a ratio from 0.0 to 1.0") from exc
    if not 0.0 <= parsed <= 1.0:
        raise argparse.ArgumentTypeError("Expected a ratio from 0.0 to 1.0")
    return parsed


def parse_non_negative_float(value: str) -> float:
    try:
        parsed = float(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Expected a non-negative number") from exc
    if parsed < 0:
        raise argparse.ArgumentTypeError("Expected a non-negative number")
    return parsed


def validate_regions(regions: Iterable[tuple[int, int, int, int]], size: tuple[int, int]) -> None:
    image_width, image_height = size
    for x, y, width, height in regions:
        if x < 0 or y < 0 or x + width > image_width or y + height > image_height:
            raise SystemExit(f"Ignore region outside image bounds: {x},{y},{width},{height}")


def apply_ignore_regions(
    reference: Image.Image,
    actual: Image.Image,
    regions: Iterable[tuple[int, int, int, int]],
) -> None:
    for x, y, width, height in regions:
        box = (x, y, x + width, y + height)
        actual.paste(reference.crop(box), box)


def triptych(reference: Image.Image, actual: Image.Image, heatmap: Image.Image) -> Image.Image:
    width, height = reference.size
    canvas = Image.new("RGB", (width * 3, height), "#111111")
    canvas.paste(reference, (0, 0))
    canvas.paste(actual, (width, 0))
    canvas.paste(heatmap, (width * 2, 0))
    return canvas


def main() -> int:
    parser = argparse.ArgumentParser(description="Create deterministic UI screenshot difference artifacts.")
    parser.add_argument("reference", type=Path)
    parser.add_argument("actual", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--pixel-threshold", type=parse_byte, default=24, metavar="0..255")
    parser.add_argument("--max-changed-ratio", type=parse_ratio, default=0.12, metavar="0..1")
    parser.add_argument(
        "--max-mean-error",
        type=parse_non_negative_float,
        default=18.0,
        metavar="NUMBER",
    )
    parser.add_argument("--ignore-region", action="append", default=[], type=parse_region)
    parser.add_argument("--resize-actual", action="store_true")
    args = parser.parse_args()

    reference_path = args.reference.resolve()
    actual_path = args.actual.resolve()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    with Image.open(reference_path) as image:
        reference = image.convert("RGB")
    with Image.open(actual_path) as image:
        actual = image.convert("RGB")

    original_actual_size = actual.size
    if reference.size != actual.size:
        if not args.resize_actual:
            raise SystemExit(
                f"Image sizes differ: reference={reference.size}, actual={actual.size}. "
                "Use --resize-actual only when scaling is intentional."
            )
        actual = actual.resize(reference.size, Image.Resampling.LANCZOS)

    validate_regions(args.ignore_region, reference.size)
    apply_ignore_regions(reference, actual, args.ignore_region)

    difference = ImageChops.difference(reference, actual)
    stat = ImageStat.Stat(difference)
    mean_error = sum(stat.mean) / len(stat.mean)
    rms_error = math.sqrt(sum(value * value for value in stat.rms) / len(stat.rms))

    gray = difference.convert("L")
    mask = gray.point(lambda value: 255 if value > args.pixel_threshold else 0)
    histogram = mask.histogram()
    changed_pixels = histogram[255]
    total_pixels = reference.width * reference.height
    changed_ratio = changed_pixels / total_pixels if total_pixels else 0.0

    heat = Image.new("RGB", reference.size, "#080808")
    red = Image.new("RGB", reference.size, "#ff3045")
    amplified = ImageEnhance.Contrast(gray).enhance(2.2)
    heat.paste(red, mask=amplified)
    overlay = Image.blend(reference, actual, 0.5)

    difference.save(output_dir / "difference.png")
    mask.save(output_dir / "changed_mask.png")
    heat.save(output_dir / "heatmap.png")
    overlay.save(output_dir / "overlay.png")
    triptych(reference, actual, heat).save(output_dir / "comparison_triptych.png")

    passed = mean_error <= args.max_mean_error and changed_ratio <= args.max_changed_ratio
    report = {
        "reference": str(reference_path),
        "actual": str(actual_path),
        "reference_size": list(reference.size),
        "actual_original_size": list(original_actual_size),
        "pixel_threshold": args.pixel_threshold,
        "ignored_regions": [list(region) for region in args.ignore_region],
        "metrics": {
            "mean_absolute_error": round(mean_error, 4),
            "rms_error": round(rms_error, 4),
            "changed_pixels": changed_pixels,
            "changed_ratio": round(changed_ratio, 6),
        },
        "limits": {
            "max_mean_error": args.max_mean_error,
            "max_changed_ratio": args.max_changed_ratio,
        },
        "passed": passed,
        "note": "Pixel metrics are triage signals. Final acceptance still requires visual review.",
    }
    (output_dir / "comparison_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"Reference: {reference_path}")
    print(f"Actual:    {actual_path}")
    print(f"Mean error: {mean_error:.4f} / {args.max_mean_error:.4f}")
    print(f"Changed:    {changed_ratio:.4%} / {args.max_changed_ratio:.4%}")
    print(f"Result:     {'PASS' if passed else 'REVIEW'}")
    print(f"Artifacts:  {output_dir}")
    return 0 if passed else 2


if __name__ == "__main__":
    raise SystemExit(main())
