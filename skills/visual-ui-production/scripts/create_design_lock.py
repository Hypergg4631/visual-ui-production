#!/usr/bin/env python3
"""Create and validate a machine-readable UI design lock."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "2.0"
VIEWPORT_RE = re.compile(r"^(?P<width>\d+)x(?P<height>\d+)$")


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Unable to read JSON {path}: {exc}") from exc


def write_json(path: Path, payload: dict[str, Any], force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing file: {path}. Pass --force only after explicit approval.")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def parse_viewport(value: str) -> dict[str, int]:
    match = VIEWPORT_RE.match(value)
    if not match:
        raise argparse.ArgumentTypeError("Viewport must use WIDTHxHEIGHT, for example 1920x1080.")
    width = int(match.group("width"))
    height = int(match.group("height"))
    if width < 320 or height < 240:
        raise argparse.ArgumentTypeError("Viewport is implausibly small.")
    return {"width": width, "height": height}


def parse_palette(values: list[str]) -> dict[str, str]:
    palette: dict[str, str] = {}
    for item in values:
        if "=" not in item:
            raise SystemExit(f"Palette entry must use role=value: {item}")
        role, value = item.split("=", 1)
        role = role.strip()
        value = value.strip()
        if not role or not value:
            raise SystemExit(f"Invalid palette entry: {item}")
        palette[role] = value
    return palette


def validate_lock(payload: dict[str, Any], require_approved: bool) -> list[str]:
    errors: list[str] = []
    required = ("schema_version", "status", "project", "screen", "framework", "selected_mock", "viewport")
    for field in required:
        if not payload.get(field):
            errors.append(f"Missing required field: {field}")

    viewport = payload.get("viewport")
    if not isinstance(viewport, dict) or not viewport.get("width") or not viewport.get("height"):
        errors.append("viewport must contain positive width and height")

    if payload.get("status") not in {"draft", "approved", "implemented", "frozen"}:
        errors.append("status must be draft, approved, implemented, or frozen")
    if require_approved and payload.get("status") not in {"approved", "implemented", "frozen"}:
        errors.append("design lock is not approved")

    for field in ("invariants", "components", "states"):
        value = payload.get(field)
        if value is not None and not isinstance(value, list):
            errors.append(f"{field} must be a list")

    style = payload.get("style")
    if style is not None and not isinstance(style, dict):
        errors.append("style must be an object")
    return errors


def command_init(args: argparse.Namespace) -> int:
    now = datetime.now(timezone.utc).isoformat()
    payload: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "status": args.status,
        "created_at": now,
        "updated_at": now,
        "project": str(Path(args.project).resolve()),
        "screen": args.screen,
        "framework": args.framework,
        "selected_mock": str(Path(args.mock).resolve()),
        "viewport": args.viewport,
        "task_type": args.task_type,
        "design_dials": {
            "variance": args.variance,
            "motion_intensity": args.motion,
            "visual_density": args.density,
            "skeuomorphism": args.skeuomorphism,
        },
        "style": {
            "mood": args.mood,
            "palette": parse_palette(args.palette),
            "typography": args.typography,
            "signature_materials": args.material,
            "avoid": args.avoid,
        },
        "layout": {
            "anchors": [],
            "safe_areas": [],
            "responsive_rules": [],
        },
        "invariants": args.invariant,
        "components": args.component,
        "states": args.state or ["idle", "hover", "pressed", "focus", "selected", "disabled"],
        "interaction": {
            "primary_path": args.primary_path,
            "motion_ms": {"hover": [100, 180], "screen": [150, 250]},
            "sound_policy": "Use short, non-blocking feedback only when the product already supports sound.",
        },
        "approval": {
            "approved_by": args.approved_by if args.status != "draft" else "",
            "approved_at": now if args.status != "draft" else "",
            "notes": args.approval_notes,
        },
    }
    errors = validate_lock(payload, require_approved=False)
    if errors:
        raise SystemExit("\n".join(errors))
    write_json(Path(args.output).resolve(), payload, args.force)
    print(f"Design lock: {Path(args.output).resolve()}")
    print(f"Status: {payload['status']}")
    print(f"Components: {len(payload['components'])}")
    return 0


def command_validate(args: argparse.Namespace) -> int:
    path = Path(args.path).resolve()
    errors = validate_lock(load_json(path), args.require_approved)
    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 2
    print(f"VALID: {path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Create or validate a UI design lock.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Create a design lock")
    init_parser.add_argument("--project", required=True)
    init_parser.add_argument("--screen", required=True)
    init_parser.add_argument("--framework", required=True)
    init_parser.add_argument("--mock", required=True)
    init_parser.add_argument("--viewport", type=parse_viewport, required=True)
    init_parser.add_argument("--output", required=True)
    init_parser.add_argument("--task-type", default="overhaul-redesign")
    init_parser.add_argument("--status", choices=("draft", "approved"), default="draft")
    init_parser.add_argument("--variance", type=int, choices=range(1, 11), default=6)
    init_parser.add_argument("--motion", type=int, choices=range(1, 11), default=4)
    init_parser.add_argument("--density", type=int, choices=range(1, 11), default=6)
    init_parser.add_argument("--skeuomorphism", type=int, choices=range(1, 11), default=3)
    init_parser.add_argument("--mood", default="")
    init_parser.add_argument("--typography", default="")
    init_parser.add_argument("--primary-path", default="")
    init_parser.add_argument("--palette", action="append", default=[], metavar="ROLE=VALUE")
    init_parser.add_argument("--material", action="append", default=[])
    init_parser.add_argument("--avoid", action="append", default=[])
    init_parser.add_argument("--invariant", action="append", default=[])
    init_parser.add_argument("--component", action="append", default=[])
    init_parser.add_argument("--state", action="append", default=[])
    init_parser.add_argument("--approved-by", default="")
    init_parser.add_argument("--approval-notes", default="")
    init_parser.add_argument("--force", action="store_true")
    init_parser.set_defaults(func=command_init)

    validate_parser = subparsers.add_parser("validate", help="Validate a design lock")
    validate_parser.add_argument("path")
    validate_parser.add_argument("--require-approved", action="store_true")
    validate_parser.set_defaults(func=command_validate)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
