# Prompt Recipes

Use these as structures, not mandatory verbosity. Keep prompts focused and label every input image by role.

## Palette Artifact

```text
Use case: ui-mockup
Asset type: UI palette and material board
Primary request: Define the visual contract for <screen/product>.
Context: <audience, repeated task, platform>
Palette: show canvas, two surfaces, primary/secondary text, accent, focus, danger, disabled
Typography: <display direction if applicable>; compact UI family; Chinese legibility
Signature motif: one material or ornament tied to <domain>
Interaction sample: one control in idle and hover states
Composition: one clean reference image, not a collage of screenshots
Exact text: use only short labels supplied below
Avoid: generic templates, unreadable text, excessive cards, pills, gradients, decorative telemetry
```

## Full-Screen Direction

```text
Use case: ui-mockup
Asset type: high-fidelity north-star UI mockup
Primary request: Create direction <A/B/C> for <screen>.
Input images:
- Image 1: approved palette and material reference
- Image 2: current screen to preserve <if redesign>
- Image 3: product/background/character identity reference <if needed>
Viewport: <width x height, aspect ratio>
Task: <primary user action>
Hierarchy: <primary, secondary, tertiary>
Controls: <list visible controls and required states>
Composition: <structural direction that makes this variant distinct>
Text: use the supplied labels verbatim for visual placement; final text will be rendered by the project
Constraints: preserve <IA, brand, content, identity, safe areas>
Avoid: <project-specific issues and anti-template list>
```

## Targeted Mock Edit

```text
Use case: precise-object-edit
Asset type: approved UI mockup correction
Edit target: Image 1 is the last approved clear source of truth
Primary request: Change only <one defect>.
Invariants: keep layout, copy, typography, palette, imagery, component positions, and all other states unchanged
Reference inputs: Image 2 defines <identity/material/state>
Validation: reject any result that changes an invariant or reduces clarity
Avoid: global redraw, reflow, new decorations, text mutation, blur, identity drift
```

If exact preservation is genuinely required, do not promise that ImageGen will keep every pixel. Use it only for the affected image-native layer, then compose deterministic text and controls in the project.

## Isolated Panel or Frame

```text
Use case: ui-mockup
Asset type: scalable UI frame asset
Primary request: Produce only the empty <panel/button/dialog> material from the approved mock
Background: flat removable chroma key with no shadow or gradient
Dimensions: <target dimensions>
Safe center: clean, low-detail content area with <insets>
Corners: preserve ornament detail; suitable for nine-slice scaling
Text: none
Icons: none
Avoid: baked labels, uneven lighting across the stretch center, cropped edges, watermark
```

## State Family

Generate each state separately while keeping dimensions and registration identical.

```text
Asset type: <control> state <idle/hover/pressed/selected/disabled/focus>
Edit target: approved idle asset
Change only: <edge light, material compression, accent, indicator>
Keep unchanged: exact dimensions, silhouette, corners, safe center, texture registration
No text, icon, or shadow outside bounds
```

## Background or Texture

```text
Use case: stylized-concept or photorealistic-natural
Asset type: runtime UI background/texture
Primary request: <scene/material>
Intended overlay: UI text and controls occupy <safe region>
Contrast: keep the safe region quiet enough for <text color>
Loop/scale needs: <tileable or fixed>
Text: none
Avoid: focal details under controls, baked UI, watermarks, illegible micro-patterns
```
