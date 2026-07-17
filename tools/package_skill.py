#!/usr/bin/env python3
"""Create a deterministic, directly installable Skill archive."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "visual-ui-production"
VERSION_FILE = ROOT / "VERSION"
FORBIDDEN_PARTS = {"__pycache__", ".test-v2"}
FORBIDDEN_SUFFIXES = {".pyc", ".pyo", ".log", ".tmp"}


def archive_files() -> list[Path]:
    files: list[Path] = []
    for path in SKILL_ROOT.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(SKILL_ROOT)
        if FORBIDDEN_PARTS.intersection(relative.parts) or path.suffix.lower() in FORBIDDEN_SUFFIXES:
            continue
        files.append(path)
    return sorted(files, key=lambda item: item.as_posix())


def write_archive(destination: Path, force: bool) -> None:
    if destination.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing archive: {destination}. Pass --force after approval.")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(destination, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for path in archive_files():
            relative = Path("visual-ui-production") / path.relative_to(SKILL_ROOT)
            info = ZipInfo(relative.as_posix(), date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    version = VERSION_FILE.read_text(encoding="utf-8").strip()
    destination = args.output_dir.resolve() / f"visual-ui-production-v{version}.zip"
    write_archive(destination, args.force)

    digest = hashlib.sha256(destination.read_bytes()).hexdigest()
    checksum = destination.with_suffix(destination.suffix + ".sha256")
    if checksum.exists() and not args.force:
        raise SystemExit(f"Refusing to overwrite existing checksum: {checksum}. Pass --force after approval.")
    checksum.write_text(f"{digest}  {destination.name}\n", encoding="utf-8")

    print(f"Archive: {destination}")
    print(f"SHA-256: {digest}")
    print(f"Files: {len(archive_files())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
