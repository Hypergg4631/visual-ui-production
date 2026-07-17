---
name: visual-ui-production
description: End-to-end visual UI production for non-designers and frontend beginners across websites, mobile apps, desktop software, and games. Use when Codex must inspect an existing project or product idea, generate visible UI directions before coding, obtain approval, lock the selected design, classify every element as image-native material or semantic code, produce implementation assets and states, integrate them through the detected framework, and validate the running result against the approved mockup. Also use when UI looks generic, code-only, line-based, templated, AI-made, misaligned, unreadable, inconsistent, or when a user wants visual assets faithfully recreated as maintainable product UI.
---

# Visual UI Production

Create UI through a visible, approval-driven, framework-independent pipeline. Let beginners make simple visual choices while the skill handles design reasoning, asset production, maintainable implementation, and running-product validation.

## Non-Negotiable Contract

1. Show visual work before implementation. Do not answer a request for visible UI options with text-only descriptions.
2. Treat generated mockups as north-star references, not runtime screenshots to paste wholesale into the product.
3. Keep exact copy, icons, values, focus states, and interactive controls deterministic in project code. Never trust image generation for final UI text.
4. Stop at every approval gate. Do not infer approval from silence, prior approval of another screen, or a vague positive comment.
5. After a direction is selected, preserve its composition. Iterate with one targeted change and repeat all invariants in the edit prompt. Never globally regenerate an approved screen to fix one local defect.
6. Preserve existing information architecture, behavior, save data, routes, labels, and accessibility unless the user explicitly approves changes.
7. Never overwrite an existing asset by default. Use versioned filenames and copy only selected final assets into the runtime project.
8. Keep drafts and test captures outside production asset folders. Leave the project with only selected, referenced deliverables.
9. Run at most one game, app, browser server, or test process at a time. Reuse or close the current process before starting another.
10. Never reduce approved image-native material to plain rectangles and thin borders. Use raster/vector assets for material and semantic controls for behavior.
11. Do not declare implementation complete without an approved design lock, a resolved asset manifest, running screenshots, and visual comparison evidence.

## Route the Task

Classify the request before generating:

- **Greenfield UI**: no established visual system. Define a direction and component vocabulary.
- **Preserve redesign**: modernize an existing UI without changing its identity or behavior. Audit and extract first.
- **Overhaul redesign**: replace the visual language while preserving content and interaction structure.
- **Targeted correction**: fix one approved element, such as a button, dialog, font, spacing, or state. Preserve everything else.
- **Image-to-project**: the user already selected a screenshot or mockup. Resolve that exact target before implementation.

If preserve versus overhaul changes the work materially and cannot be inferred, ask one concise question. Otherwise state a one-line design read and proceed.

## Beginner Mode

Use beginner mode by default unless the user demonstrates that they want direct control over implementation details.

- Ask no more than three questions before showing visual work.
- Infer framework, viewport, existing behavior, and visual language from the project.
- Present 2-3 visible directions and explain only what the user needs to compare.
- Accept simple feedback such as "less realistic", "more readable", or "keep this layout" and translate it into targeted design constraints.
- Recommend one option when the user does not want to choose.
- Hide implementation jargon until after visual approval.
- Never ask the user to decide whether an element should be CSS, PNG, a nine-slice, a widget, or an engine control. Resolve that through the asset manifest.
- At every gate, report: what is approved, what will change next, and whether production files will be edited.

## Completion Definition

A task is complete only when all applicable stages are done:

1. visible direction approved;
2. design lock approved and validated;
3. every visible component resolved in the asset manifest;
4. image-native assets produced and audited;
5. semantic controls implemented in the existing framework;
6. required states and interactions work;
7. running screenshots captured with one process;
8. visual comparison reviewed and blocking differences fixed;
9. production paths and residual limitations reported.

## Core Workflow

### 1. Inspect the Real Context

Read the project before designing. Identify:

- framework, engine, resolution, aspect ratios, scaling behavior, asset folders, and naming conventions;
- existing fonts, colors, textures, components, screens, interaction states, sounds, and motion;
- the screen's audience, purpose, primary action, information hierarchy, and repeated workflow;
- content and behavior that must remain exact;
- existing screenshots and approved visuals that must remain recognizable.

For redesigns, capture the current screen before editing. Record what to preserve and what to retire.

### 2. Declare the Design Read

State one line in the user's language:

`Reading this as: <surface> for <audience>, with <mood/domain language>, preserving <critical invariant>.`

Set and briefly justify three dials from 1 to 10:

- `DESIGN_VARIANCE`: structural originality versus conventional familiarity.
- `MOTION_INTENSITY`: static versus expressive feedback.
- `VISUAL_DENSITY`: airy versus information-dense.

Use the product's domain, not personal taste, to choose the values.

### 3. Lock Direction Inputs

Ask at most three targeted questions only when the answers are missing and materially affect the visual result: target screen, atmosphere/reference lane, and must-preserve content. Reuse answers already supplied in the same task.

When Creative Production is available, use its board as the visual workspace. Open one board once and reuse its `boardId`. Use ImageGen for raster mockups, textures, scene-led UI, and image-native visual ingredients.

Read [workflow-gates.md](references/workflow-gates.md) before starting a full greenfield or overhaul flow.

### 4. Confirm a Palette Artifact

Generate one focused palette artifact containing:

- background and surface colors;
- primary, accent, semantic, and text colors;
- typography direction;
- one signature material or motif;
- a short note about intended density and motion.

Show it and stop. Continue only after explicit palette confirmation. Skip this gate only when an existing approved design system already defines these choices.

### 5. Generate Visible UI Directions

Generate 2-3 full-screen, single-image mockups against the confirmed palette. Each direction must differ structurally in hierarchy, composition, density, or topology, not merely in color.

For each direction, label:

- what the user should compare;
- the primary interaction path;
- the distinctive visual motif;
- the main implementation risk.

Do not create a collage unless the user explicitly requests one. Do not begin code. Stop until the user selects one direction or delegates the choice.

Read [aesthetic-system.md](references/aesthetic-system.md) before prompting visual variants and [prompt-recipes.md](references/prompt-recipes.md) when using ImageGen.

### 6. Freeze the Selected Direction

Record a compact design lock:

- selected mock path or attachment;
- viewport and state shown;
- layout anchors and safe areas;
- palette and type choices;
- signature motif and material treatment;
- controls and interaction states;
- elements that must not change.

If the user requests a local correction, edit the selected mock with the selected image as the edit target. State `change only X; keep Y unchanged`. Do not use the latest failed variant as the new source of truth.

Read [design-lock.md](references/design-lock.md), then create and validate a machine-readable lock with `scripts/create_design_lock.py`. Do not start production implementation from a draft lock.

### 7. Build a Fidelity Inventory

Inventory every visible ingredient and assign one implementation method:

- semantic layout/code;
- real text rendered by the engine or app;
- icon library or existing project icon;
- scalable vector/native shape;
- generated raster asset;
- sourced photo or existing project asset;
- animation or sound behavior;
- intentional omission.

Rasterize only image-native material: textures, atmospheric backplates, ornate frames, illustrated scenes, masks, and unique decorative surfaces. Keep labels, numbers, buttons, toggles, sliders, keyboard focus, and exact copy semantic.

Read [image-code-decision.md](references/image-code-decision.md), [asset-manifest.md](references/asset-manifest.md), and [asset-implementation.md](references/asset-implementation.md). Create the initial manifest with `scripts/build_asset_manifest.py`, resolve every `unresolved` component, and validate it before editing production code.

Apply the hard hybrid rule:

- material, lighting, wear, irregular silhouettes, illustration, photography, film, wood, metal, paper, and atmospheric texture use image-native assets;
- text, values, localization, inputs, focus, actions, accessibility, and dynamic content use semantic runtime controls;
- polished components normally combine both.

### 8. Produce Final Assets Non-Destructively

Use ImageGen's built-in path by default. Keep drafts under the generator's default storage until the user selects them. For project-bound assets:

- generate or extract one asset per call;
- use a flat removable key background for simple transparency, then validate alpha;
- create complete state families when the visual itself changes: idle, hover, pressed, selected, disabled, and focus;
- use stable, descriptive, versioned filenames;
- record dimensions, format, alpha, safe insets, and consuming screen;
- copy only selected finals into the project.

Run `scripts/inspect_ui_assets.py <asset-directory>` after production.

### 9. Implement in the Existing Stack

Use the project's established framework, engine helpers, design system, and naming patterns. Do not replace working architecture for visual convenience.

Read [framework-routing.md](references/framework-routing.md) and load only the detected product adapter: [adapters-web.md](references/adapters-web.md), [adapters-apps.md](references/adapters-apps.md), [adapters-game-engines.md](references/adapters-game-engines.md), or [adapters-renpy.md](references/adapters-renpy.md). Treat adapters as implementation contracts, not visual style presets.

Recreate the approved hierarchy and material language while keeping runtime text and controls editable. Implement all states a user naturally expects. Add restrained motion and sound only when they communicate feedback or state.

Do not silently alter unrelated screens. For shared components, check every consumer before changing behavior.

### 10. Validate the Running UI

Start one process only. Capture the same viewport and state as the approved mock, then compare them side by side.

Verify:

- visual hierarchy, alignment, spacing, type size, contrast, and safe areas;
- long text, two-line text, localization, and dynamic values;
- hover, focus, pressed, selected, disabled, loading, and error states as applicable;
- mouse, keyboard, controller, and touch paths as applicable;
- sound timing and 100-200 ms feedback timing for common product/game controls;
- multiple supported resolutions without overlap, clipping, or layout shift;
- no extra test process remains running.

Read [visual-comparison.md](references/visual-comparison.md) and [qa-checklist.md](references/qa-checklist.md). Run `scripts/compare_ui_screenshots.py` against versioned captures, inspect the generated overlay/heatmap/triptych, fix blocking issues, and recapture until the comparison passes. Pixel metrics are triage signals; visual review remains mandatory.

### 11. Handoff and Freeze

Report:

- selected direction and implemented screen;
- final asset paths and consuming project files;
- test command and verified resolutions/states;
- any residual limitation;
- the single most useful next task.

After the user freezes a screen, treat it as locked. Future work may reuse its tokens and components but must not redesign it without explicit approval.

## Tool Rules

### Creative Production

- Use one board per workflow when the plugin is available.
- Keep every board tile to one clean visual reference.
- Use the board for comparison, selection, and iteration, not as a substitute for project implementation.
- Preserve supplied identities, logos, materials, proportions, and approved content.

### ImageGen

- Inspect local edit targets before editing.
- Label every input image as edit target, identity reference, style reference, or supporting asset.
- Repeat invariants on every edit.
- Do not promise pixel-locked local edits when the model will regenerate the whole image. If exact preservation is required, reconstruct text and controls deterministically after using ImageGen for image-native layers.
- Avoid repeated full-image generations. Return to the last approved clear source when an iteration degrades.
- Save project-bound selected assets inside the workspace; do not leave runtime dependencies only under generated-image storage.

## Resource Map

- [workflow-gates.md](references/workflow-gates.md): stage deliverables and approval language.
- [aesthetic-system.md](references/aesthetic-system.md): anti-template visual reasoning and component taste rules.
- [prompt-recipes.md](references/prompt-recipes.md): prompts for palettes, mockups, targeted edits, and production assets.
- [asset-implementation.md](references/asset-implementation.md): semantic-versus-raster decisions and production asset rules.
- [design-lock.md](references/design-lock.md): approved visual source of truth and lifecycle.
- [asset-manifest.md](references/asset-manifest.md): component-to-implementation mapping and state matrix.
- [image-code-decision.md](references/image-code-decision.md): hard rules for image-native material versus semantic code.
- [framework-routing.md](references/framework-routing.md): product/framework detection and adapter contract.
- [adapters-web.md](references/adapters-web.md): responsive websites and browser-product implementation.
- [adapters-apps.md](references/adapters-apps.md): mobile and desktop application implementation.
- [adapters-game-engines.md](references/adapters-game-engines.md): Unity, Godot, Unreal, and general game UI implementation.
- [adapters-renpy.md](references/adapters-renpy.md): complete Ren'Py implementation and test adapter.
- [visual-comparison.md](references/visual-comparison.md): deterministic screenshot comparison and acceptance matrix.
- [qa-checklist.md](references/qa-checklist.md): visual, interaction, accessibility, performance, and file-hygiene checks.
- `scripts/inspect_ui_assets.py`: read-only metadata audit for generated UI assets.
- `scripts/create_design_lock.py`: create and validate the selected visual contract.
- `scripts/build_asset_manifest.py`: create and validate the implementation inventory.
- `scripts/compare_ui_screenshots.py`: produce diff, mask, heatmap, overlay, triptych, and pass/review metrics.
