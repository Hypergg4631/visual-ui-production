#!/usr/bin/env python3
"""Read-only metadata audit for UI raster assets."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

try:
    from PIL import Image
except ImportError as exc:  # pragma: no cover - dependency guidance
    raise SystemExit("Pillow is required: python -m pip install pillow") from exc


SUPPORTED = {".png", ".webp", ".jpg", ".jpeg", ".bmp", ".gif"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def alpha_summary(image: Image.Image) -> dict[str, Any]:
    if "A" not in image.getbands():
        return {"has_alpha": False, "transparent_pixels": 0, "opaque_pixels": image.width * image.height}

    alpha = image.getchannel("A")
    histogram = alpha.histogram()
    return {
        "has_alpha": True,
        "transparent_pixels": histogram[0],
        "opaque_pixels": histogram[255],
        "partial_alpha_pixels": sum(histogram[1:255]),
        "transparent_corners": sum(alpha.getpixel(point) == 0 for point in (
            (0, 0),
            (image.width - 1, 0),
            (0, image.height - 1),
            (image.width - 1, image.height - 1),
        )),
    }


def inspect(path: Path, root: Path) -> dict[str, Any]:
    with Image.open(path) as image:
        report: dict[str, Any] = {
            "path": str(path.relative_to(root)),
            "bytes": path.stat().st_size,
            "format": image.format,
            "mode": image.mode,
            "width": image.width,
            "height": image.height,
            "aspect_ratio": round(image.width / image.height, 6) if image.height else None,
            "sha256": sha256(path),
        }
        report.update(alpha_summary(image))
        return report


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit UI image dimensions, alpha, and duplicate content without modifying files.")
    parser.add_argument("directory", type=Path, help="Asset directory to inspect")
    parser.add_argument("--json", dest="json_path", type=Path, help="Optional JSON report path")
    args = parser.parse_args()

    root = args.directory.resolve()
    if not root.is_dir():
        parser.error(f"Not a directory: {root}")

    paths = sorted(path for path in root.rglob("*") if path.is_file() and path.suffix.lower() in SUPPORTED)
    records = [inspect(path, root) for path in paths]

    hashes: dict[str, list[str]] = {}
    for record in records:
        hashes.setdefault(record["sha256"], []).append(record["path"])
    duplicates = [items for items in hashes.values() if len(items) > 1]

    payload = {
        "root": str(root),
        "asset_count": len(records),
        "duplicate_groups": duplicates,
        "assets": records,
    }

    print(f"Root: {root}")
    print(f"Assets: {len(records)}")
    for record in records:
        alpha = "alpha" if record["has_alpha"] else "opaque"
        print(f"{record['width']:>5}x{record['height']:<5} {alpha:<6} {record['format'] or '?':<5} {record['path']}")
    if duplicates:
        print("Duplicate content:")
        for group in duplicates:
            print("  - " + " | ".join(group))

    if args.json_path:
        output = args.json_path.resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"JSON: {output}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
