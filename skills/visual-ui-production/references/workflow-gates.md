# Workflow Gates

Use these gates for full UI creation and major redesigns. Targeted corrections may enter at Gate 4, but must still preserve an explicitly named source of truth.

## Gate 1: Direction

Deliver:

- one-line design read;
- audience, task, surface, and platform;
- preserve/overhaul classification;
- design variance, motion intensity, and visual density;
- 2-4 visual reference principles, not copied layouts.

Ask: `方向理解是否正确？确认后我再生成色板。`

Do not generate mockups before confirmation when the direction is genuinely ambiguous.

## Gate 2: Palette

Deliver one image showing:

- background, surface, text, accent, and semantic colors;
- type direction and hierarchy;
- signature texture or motif;
- sample control at idle and hover.

Ask: `这套色板和材质是否锁定？需要调整哪一项？`

Do not generate multiple screen directions against an unconfirmed palette.

## Gate 3: Full-Screen Directions

Deliver 2-3 separate images. Each image represents one coherent screen, not a mini mood board.

Directions must differ in structure:

- information hierarchy;
- navigation topology;
- density;
- focal point;
- component rhythm.

Keep palette and brand motif constant so the user compares design, not color preference.

Ask: `请选择一版，或明确要混合哪些元素。选定前不会写入项目。`

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
