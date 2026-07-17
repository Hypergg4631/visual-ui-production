# Design Lock

Use a design lock after the user selects a visual direction and before producing runtime assets or code.

## Purpose

The design lock prevents visual drift. It records the approved source of truth, the elements that may not change, and the states that implementation must reproduce.

Create it with:

```powershell
python scripts/create_design_lock.py init `
  --project "D:\path\to\project" `
  --screen "account-settings" `
  --framework "react-vite" `
  --mock "D:\path\selected-settings-mock.png" `
  --viewport 1440x960 `
  --status approved `
  --mood "quiet professional workspace" `
  --palette "canvas=#101214" `
  --palette "text=#f1f2f3" `
  --palette "accent=#cc594c" `
  --material "brushed dark header surface" `
  --invariant "account fields and save behavior remain unchanged" `
  --component "settings navigation" `
  --component "account form" `
  --component "save action" `
  --output ".ui-production\account-settings.design-lock.json"
```

Never pass `--status approved` without explicit user approval of the selected mockup.

## Required Contents

- selected mock path and viewport;
- product/framework and target screen;
- design variance, motion, density, and skeuomorphism dials;
- palette roles and typography direction;
- signature materials and forbidden motifs;
- layout anchors and safe areas;
- visible components and required states;
- preserved information architecture and behavior;
- approval identity, time, and notes.

## Lifecycle

`draft -> approved -> implemented -> frozen`

- `draft`: visual exploration only; no production implementation.
- `approved`: exact mock selected; create the asset manifest.
- `implemented`: running screen exists and is under visual comparison.
- `frozen`: acceptance complete; future work must preserve the system.

Validate before implementation:

```powershell
python scripts/create_design_lock.py validate ".ui-production\account-settings.design-lock.json" --require-approved
```

## Targeted Revision Rule

For local corrections, update only the affected lock fields and preserve:

- selected source mock;
- layout anchors;
- unaffected typography and palette;
- component registration and dimensions;
- all previously approved states.

Do not replace the source of truth with a failed or globally regenerated variant.
