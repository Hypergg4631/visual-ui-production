from __future__ import annotations

import json
import re
import subprocess
import sys
import unittest
import uuid
from pathlib import Path
from zipfile import ZipFile

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "visual-ui-production"
SCRIPTS = SKILL / "scripts"


class RepositoryTests(unittest.TestCase):
    def scratch_dir(self, label: str) -> Path:
        path = ROOT / "output" / "test-runs" / f"{label}-{uuid.uuid4().hex}"
        path.mkdir(parents=True)
        return path

    def publishable_files(self) -> list[Path]:
        result = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
            cwd=ROOT,
            check=True,
            text=True,
            capture_output=True,
        )
        return [ROOT / line for line in result.stdout.splitlines() if line]

    def run_python(self, *args: object) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, *(str(arg) for arg in args)],
            cwd=ROOT,
            check=True,
            text=True,
            capture_output=True,
        )

    def test_skill_metadata_and_resources(self) -> None:
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        frontmatter = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        self.assertIsNotNone(frontmatter)
        metadata = frontmatter.group(1)
        self.assertRegex(metadata, r"(?m)^name:\s*visual-ui-production\s*$")
        self.assertRegex(metadata, r"(?m)^description:\s*\S")

        references = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
        self.assertTrue(references)
        for reference in references:
            self.assertTrue((SKILL / reference).is_file(), reference)

        script_references = set(re.findall(r"scripts/[A-Za-z0-9_.-]+", text))
        self.assertEqual(
            script_references,
            {
                "scripts/build_asset_manifest.py",
                "scripts/compare_ui_screenshots.py",
                "scripts/create_design_lock.py",
                "scripts/inspect_ui_assets.py",
            },
        )

        interface = (SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn('display_name:', interface)
        self.assertIn('$visual-ui-production', interface)

    def test_repository_contains_no_publish_forbidden_files(self) -> None:
        forbidden_parts = {"__pycache__", ".test-v2", ".env", "creative_drafts", "generated_images"}
        forbidden_suffixes = {".pyc", ".pyo", ".log", ".tmp"}
        violations: list[str] = []
        for path in self.publishable_files():
            relative = path.relative_to(ROOT)
            if forbidden_parts.intersection(relative.parts) or path.suffix.lower() in forbidden_suffixes:
                violations.append(relative.as_posix())
        self.assertEqual(violations, [])

    def test_text_files_do_not_expose_local_identity(self) -> None:
        patterns = [
            re.compile(r"C:" + r"\\Users\\", re.IGNORECASE),
            re.compile(r"D:" + r"\\Workspace", re.IGNORECASE),
            re.compile("27" + "977"),
            re.compile("雾里" + "第三夜"),
            re.compile(r"BEGIN (?:RSA|OPENSSH|EC) PRIVATE KEY"),
        ]
        violations: list[str] = []
        text_suffixes = {".md", ".txt", ".py", ".yaml", ".yml", ".json", ".html", ".css", ".js", ".rpy", ".svg"}
        for path in self.publishable_files():
            if path.suffix.lower() not in text_suffixes:
                continue
            text = path.read_text(encoding="utf-8")
            if any(pattern.search(text) for pattern in patterns):
                violations.append(path.relative_to(ROOT).as_posix())
        self.assertEqual(violations, [])

    def test_anonymous_examples_validate(self) -> None:
        examples = ROOT / "examples"
        for name in ("web-dashboard", "desktop-settings", "game-save-menu"):
            directory = examples / name
            lock = directory / "design-lock.json"
            manifest = directory / "asset-manifest.json"
            summary = json.loads((directory / "comparison-summary.json").read_text(encoding="utf-8"))
            self.assertTrue((directory / "mockup.svg").is_file())
            self.assertTrue(summary["passed"])
            self.run_python(SCRIPTS / "create_design_lock.py", "validate", lock, "--require-approved")
            self.run_python(SCRIPTS / "build_asset_manifest.py", "validate", manifest)

    def test_image_tools_end_to_end(self) -> None:
        root = self.scratch_dir("image-tools")
        assets = root / "assets"
        assets.mkdir()
        reference = assets / "reference.png"
        actual = assets / "actual.png"
        Image.new("RGBA", (96, 64), "#176b5bff").save(reference)
        Image.new("RGBA", (96, 64), "#176b5bff").save(actual)

        audit_report = root / "audit.json"
        self.run_python(SCRIPTS / "inspect_ui_assets.py", assets, "--json", audit_report)
        self.assertEqual(json.loads(audit_report.read_text(encoding="utf-8"))["asset_count"], 2)

        comparison = root / "comparison"
        self.run_python(
            SCRIPTS / "compare_ui_screenshots.py",
            reference,
            actual,
            "--output-dir",
            comparison,
        )
        report = json.loads((comparison / "comparison_report.json").read_text(encoding="utf-8"))
        self.assertTrue(report["passed"])
        self.assertTrue((comparison / "comparison_triptych.png").is_file())

    def test_release_package_is_installable(self) -> None:
        output = self.scratch_dir("package")
        self.run_python(ROOT / "tools" / "package_skill.py", "--output-dir", output)
        archives = list(output.glob("*.zip"))
        self.assertEqual(len(archives), 1)
        with ZipFile(archives[0]) as archive:
            names = set(archive.namelist())
        self.assertIn("visual-ui-production/SKILL.md", names)
        self.assertIn("visual-ui-production/agents/openai.yaml", names)
        self.assertIn("visual-ui-production/scripts/compare_ui_screenshots.py", names)
        self.assertFalse(any("__pycache__" in name or name.endswith(".pyc") for name in names))


if __name__ == "__main__":
    unittest.main()
