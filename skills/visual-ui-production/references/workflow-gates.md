# Workflow Gates

Use these gates for every UI workflow. Read `approval-state-machine.md` first. A targeted correction may enter at Gate 4 only when a direct user message explicitly approves the exact source image and requested invariant set.

## Approval Evidence

Only the user can approve a gate. Record the direct user message and the exact artifact it approves.

Valid examples:

- `这套色板确认。`
- `选 B。`
- `就用 mockup_v3.png，按这张已批准稿继续。`
- `这份设计锁确认，可以开始实现。`

Invalid examples:

- an assistant says an image "will be the visual baseline";
- a screenshot appeared earlier in the task;
- the user says only `继续`, `再来一版`, or `重新设计一版`;
- a tool produced an image successfully;
- another screen or an earlier task was approved;
- the user did not object.

When evidence is missing, ask one approval question and stop. Never manufacture the missing approval in assistant prose.

## Gate 1: Direction

Deliver:

- one-line design read;
- audience, task, surface, and platform;
- preserve/overhaul classification;
- design variance, motion intensity, and visual density;
- 2-4 visual reference principles, not copied layouts.

Ask: `方向理解是否正确？确认后我只生成色板，不会直接生成完整界面。`

Do not generate mockups before confirmation when the direction is genuinely ambiguous.

## Gate 2: Palette

Deliver one image showing:

- background, surface, text, accent, and semantic colors;
- type direction and hierarchy;
- signature texture or motif;
- sample control at idle and hover.

Ask: `这套色板和材质是否锁定？确认后我再生成 2-3 个完整方向。`

Stop after presenting the palette. Do not generate full-screen directions against an unconfirmed palette.

## Gate 3: Full-Screen Directions

Deliver 2-3 separate images. Each image represents one coherent screen, not a mini mood board.

Directions must differ in structure:

- information hierarchy;
- navigation topology;
- density;
- focal point;
- component rhythm.

Keep palette and brand motif constant so the user compares design, not color preference.

Ask: `请选择一版，或明确要混合哪些元素。选定前不会生成设计锁或写入项目。`

Stop after presenting the directions. A request phrased in the singular does not reduce this gate to one image.

## Gate 4: Design Lock

Record:

- selected image path;
- target viewport and UI state;
- exact copy list;
- fixed layout anchors;
- visual materials;
- component states;
- motion and sound behavior;
- must-not-change list.

Ask: `我将按这份锁定清单拆素材并实现，是否确认？`

Stop after presenting the lock. Do not create production assets or edit code until the user explicitly confirms it.

## Gate 5: Asset Review

Present extracted/generated assets on a neutral inspection background. Include dimensions and state names.

Check:

- alpha edges;
- nine-slice safe center;
- consistent lighting and material;
- no text accidentally baked into reusable panels;
- complete state family;
- readable naming.

Ask: `素材是否确认进入项目？`

## Gate 6: Running Build

Show a capture from the actual running project at the same viewport and state as the approved mock.

Compare:

- hierarchy and proportions;
- text fidelity;
- material and image fidelity;
- interaction feedback;
- supported resolution behavior.

Do not claim completion from a successful build alone. A running visual comparison is required.

## Iteration Rule

For each revision:

1. name one target defect;
2. name the source-of-truth image;
3. list invariants;
4. change only that defect;
5. inspect before presenting;
6. reject the output yourself if it regresses clarity, identity, text, or composition.

If two consecutive generations drift, stop regenerating the full screen. Return to the last approved source and use deterministic composition or isolated assets.
