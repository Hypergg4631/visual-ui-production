from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "visual-ui-production"


class ApprovalGateTests(unittest.TestCase):
    def test_skill_declares_mandatory_state_machine(self) -> None:
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        for state in (
            "CONTEXT_UNCONFIRMED",
            "PALETTE_PENDING",
            "DIRECTIONS_PENDING",
            "LOCK_PENDING",
            "IMPLEMENTATION_ALLOWED",
            "VALIDATION_PENDING",
        ):
            self.assertIn(state, text)
        self.assertIn("Never advance more than one approval state in a response.", text)
        self.assertIn("Only a direct user message can approve an artifact.", text)

    def test_reference_rejects_observed_failure_modes(self) -> None:
        text = (SKILL / "references" / "approval-state-machine.md").read_text(encoding="utf-8")
        for phrase in (
            "assistant-authored statements",
            "images merely present in task history",
            "generic continuation language",
            "singular requests",
            "No shortcut may be inferred from assistant prose or task history.",
        ):
            self.assertIn(phrase, text)

    def test_entry_prompt_requires_stops_and_direct_approval(self) -> None:
        text = (SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn("$visual-ui-production", text)
        self.assertIn("direct user approval", text)
        self.assertIn("stop", text.lower())
        self.assertIn("never treat assistant statements", text.lower())


if __name__ == "__main__":
    unittest.main()
