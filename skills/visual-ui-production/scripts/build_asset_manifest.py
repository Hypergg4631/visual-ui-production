#!/usr/bin/env python3
"""Create and validate the implementation manifest for an approved UI design."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


METHODS = {
    "semantic-control",
    "runtime-text",
    "native-shape",
    "raster-asset",
    "existing-asset",
    "icon-library",
    "animation",
    "sound",
    "intentional-omission",
    "unresolved",
}


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


def component_record(name: str) -> dict[str, Any]:
    return {
        "id": name.lower().replace(" ", "-"),
        "name": name,
        "method": "unresolved",
        "source": "",
        "output": "",
        "dimensions": None,
        "alpha": None,
        "nine_slice": None,
        "states": [],
        "dynamic_content": [],
        "consumer": "",
        "notes": "",
    }


def validate(payload: dict[str, Any], allow_unresolved: bool) -> list[str]:
    errors: list[str] = []
    for field in ("schema_version", "design_lock", "framework", "screen", "components"):
        if field not in payload:
            errors.append(f"Missing required field: {field}")

    components = payload.get("components")
    if not isinstance(components, list):
        errors.append("components must be a list")
        return errors

    ids: set[str] = set()
    for index, component in enumerate(components):
        prefix = f"components[{index}]"
        if not isinstance(component, dict):
            errors.append(f"{prefix} must be an object")
            continue
        component_id = component.get("id")
        if not component_id:
            errors.append(f"{prefix}.id is required")
        elif component_id in ids:
            errors.append(f"Duplicate component id: {component_id}")
        else:
            ids.add(component_id)

        method = component.get("method")
        if method not in METHODS:
            errors.append(f"{prefix}.method is invalid: {method}")
        if method == "unresolved" and not allow_unresolved:
            errors.append(f"{prefix}.method is unresolved")
        if method == "raster-asset" and not component.get("output"):
            errors.append(f"{prefix}.output is required for raster-asset")
        if method in {"semantic-control", "runtime-text"} and not component.get("consumer"):
            errors.append(f"{prefix}.consumer is required for {method}")
    return errors


def command_init(args: argparse.Namespace) -> int:
    lock_path = Path(args.design_lock).resolve()
    lock = load_json(lock_path)
    if lock.get("status") not in {"approved", "implemented", "frozen"} and not args.allow_draft:
        raise SystemExit("Design lock must be approved before creating a production manifest. Use --allow-draft only for planning.")

    components = [component_record(str(name)) for name in lock.get("components", [])]
    payload: dict[str, Any] = {
        "schema_version": "2.0",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "design_lock": str(lock_path),
        "framework": lock.get("framework", ""),
        "screen": lock.get("screen", ""),
        "viewport": lock.get("viewport", {}),
        "output_root": str(Path(args.output_root).resolve()) if args.output_root else "",
        "rules": {
            "runtime_text_is_semantic": True,
            "dynamic_content_is_semantic": True,
            "image_native_materials_use_raster_assets": True,
            "do_not_bake_full_mockup_as_interactive_ui": True,
            "version_assets_non_destructively": True,
        },
        "components": components,
        "state_matrix": [],
        "test_states": [],
    }
    write_json(Path(args.output).resolve(), payload, args.force)
    print(f"Asset manifest: {Path(args.output).resolve()}")
    print(f"Unresolved components: {len(components)}")
    return 0


def command_validate(args: argparse.Namespace) -> int:
    path = Path(args.path).resolve()
    errors = validate(load_json(path), args.allow_unresolved)
    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 2
    print(f"VALID: {path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Create or validate a UI asset implementation manifest.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init")
    init_parser.add_argument("--design-lock", required=True)
    init_parser.add_argument("--output", required=True)
    init_parser.add_argument("--output-root", default="")
    init_parser.add_argument("--allow-draft", action="store_true")
    init_parser.add_argument("--force", action="store_true")
    init_parser.set_defaults(func=command_init)

    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("path")
    validate_parser.add_argument("--allow-unresolved", action="store_true")
    validate_parser.set_defaults(func=command_validate)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
