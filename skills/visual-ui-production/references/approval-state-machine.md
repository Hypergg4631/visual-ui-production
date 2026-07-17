# Approval State Machine

This file is the authoritative transition contract for visual work. When another instruction appears to permit skipping a gate, follow this file.

## Approval truth source

Only a direct user message can approve an artifact. Approval must identify the artifact or the immediately preceding artifact unambiguously.

Never count any of the following as approval:

- assistant-authored statements, summaries, recommendations, or plans;
- images merely present in task history;
- approval from another task, screen, state, or revision;
- successful tool output;
- silence or lack of objection;
- generic continuation language such as `继续`;
- singular requests such as `重新设计一版` or `再做一版`.

If a task contains a candidate reference image but no direct user approval, ask:

`你是否确认将这张具体图片作为本屏幕的视觉基准？确认前我不会继续生成或实现。`

Then stop.

## States and transitions

### `CONTEXT_UNCONFIRMED`

Allowed:

- inspect project files and the running screen;
- classify the task;
- state the design read and three design dials;
- ask at most three material questions.

Next state: `PALETTE_PENDING`.

Forbidden: full-screen mockups, production assets, code edits.

### `PALETTE_PENDING`

Allowed:

- generate exactly one palette/material artifact;
- explain what the user should evaluate;
- ask for explicit palette approval.

Stop after the artifact. Advance only after a direct user approval.

Forbidden: full-screen directions, design lock, production edits.

### `DIRECTIONS_PENDING`

Allowed only after palette approval:

- generate 2-3 separate full-screen directions;
- keep palette and must-preserve content constant;
- label comparison points and implementation risk;
- ask the user to select one direction.

Stop after the directions. Advance only after a direct user selection or explicit delegation.

Forbidden: selecting a direction on the user's behalf unless explicitly delegated, creating final assets, production edits.

### `LOCK_PENDING`

Allowed only after direction selection:

- create and validate the machine-readable design lock;
- show viewport, anchors, invariants, states, and must-not-change items;
- ask for explicit implementation approval.

Stop after the lock. Advance only after a direct user approval of that lock.

Forbidden: production assets, code edits, treating direction selection as automatic implementation approval.

### `IMPLEMENTATION_ALLOWED`

Allowed only after design-lock approval:

- create and resolve the asset manifest;
- produce selected assets non-destructively;
- edit production code in the existing stack;
- implement required states and interactions.

Next state: `VALIDATION_PENDING`.

### `VALIDATION_PENDING`

Allowed:

- run one product/test process;
- capture the approved viewport and state;
- compare screenshots and inspect interaction states;
- fix blocking differences without redesigning the locked screen;
- report evidence and limitations.

## Entry shortcuts

Shortcuts require direct user evidence:

- An existing approved design system may satisfy the palette gate only when the user explicitly says it is approved for this screen.
- An image-to-project task may satisfy the direction gate only when the user explicitly identifies the exact image as selected.
- A targeted correction may begin at `LOCK_PENDING` only when the user explicitly names the approved source and the one defect to change.
- A request to "implement this approved design" may begin at `LOCK_PENDING`; still show and confirm the design lock before production edits.

No shortcut may be inferred from assistant prose or task history.
