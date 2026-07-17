# Changelog

All notable changes are documented here.

## 1.0.1 — 2026-07-17

- Added an authoritative approval state machine for all visual workflows.
- Restricted approval evidence to direct user messages.
- Prevented assistant-authored baselines, historical screenshots, generic continuation language, and singular redesign requests from skipping gates.
- Required a stop after palette, direction, and design-lock delivery.
- Added a regression test for approval-gate behavior.

## 1.0.0 — 2026-07-17

- Added the complete approval-driven visual UI production workflow.
- Added Web, desktop application, game-engine, and Ren'Py adapters.
- Added design-lock, asset-manifest, asset-audit, and screenshot-comparison tools.
- Added three anonymous synthetic examples.
- Added repository validation, packaging, CI, and tag-based release automation.
