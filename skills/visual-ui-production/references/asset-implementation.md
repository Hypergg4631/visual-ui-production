# Asset and Implementation Guide

## Decide What Becomes Raster

Keep semantic/native:

- all exact text, numbers, dates, labels, shortcuts, and dynamic values;
- standard icons when a project icon family exists;
- hit areas, focus logic, sliders, toggles, checkboxes, scrollbars, and progress behavior;
- layout spacing and responsive behavior;
- hover, pressed, selected, disabled, and loading logic;
- accessibility names and keyboard/controller navigation.

Use raster for:

- photographic or illustrated backplates;
- unique materials and textures that code cannot reproduce credibly;
- ornate borders and corner treatments;
- atmospheric overlays, masks, and scene-led decoration;
- character, product, or environment art.
- approved control skins whose identity depends on wood, film, metal, fabric, paper, glass, wear, lighting, or irregular silhouette.

Use vector/native shapes for simple dividers, icons, focus outlines, and geometry. Do not generate a bitmap for a line or standard symbol. Read [image-code-decision.md](image-code-decision.md) before final classification.

## File Staging

Keep previews and rejected variants outside production folders. Preferred order:

1. leave Creative Production/ImageGen drafts in their managed storage;
2. place selected extraction work in a dedicated external or sibling production-work folder;
3. copy only approved final assets into the runtime project;
4. use versioned names instead of overwriting.

Suggested names:

```text
ui_<surface>_<element>_<state>_v01.png
ui_<surface>_<texture>_v01.webp
ui_<surface>_<background>_v01.png
ui_<surface>_mock_<direction>_v01.png
```

Record each asset's width, height, alpha, safe insets, state, and consumer.

## Transparency

For simple opaque assets, generate on a flat chroma-key background and remove it locally. Validate:

- alpha channel exists;
- corners are transparent;
- no key-color fringe remains;
- reflective/highlight areas were not erased;
- subject bounds include padding;
- no cast shadow remains unless intentionally separated.

Complex hair, glass, smoke, translucent materials, or soft shadows may need true model-native transparency. Do not silently downgrade models or promise clean alpha without validation.

## Nine-Slice Frames

Create frames with:

- fixed corners;
- fixed ornamental edges where needed;
- a quiet, repeatable or stretchable center;
- safe text insets;
- no directional highlight across the stretch region;
- matching state assets registered to identical bounds.

Test the smallest and largest expected content sizes.

## Framework Adapters

Read [framework-routing.md](framework-routing.md) and load only the detected framework adapter. For Ren'Py, use the full contract in [adapters-renpy.md](adapters-renpy.md).

## Web Adapter

- Use the existing framework and design system.
- Keep controls semantic HTML and preserve keyboard focus.
- Use CSS layout for responsiveness; do not bake an entire screen into a background image.
- Use `border-image`, layered backgrounds, masks, or pseudo-elements only for image-native materials.
- Provide reduced-motion alternatives.
- Verify desktop and mobile captures at named viewports.

## Desktop and Mobile Adapter

- Use the platform's established component and layout system.
- Respect DPI, safe areas, touch target sizes, text scaling, and localization.
- Keep platform-standard dialogs and controls familiar unless the fiction genuinely requires a custom treatment.
- Separate decorative skins from command behavior.

## Fidelity Inventory Template

| Ingredient | Source | Implementation | Exact? | States | Final path |
|---|---|---|---|---|---|
| Background | Approved mock | Raster | No | static | pending |
| Dialog frame | Generated asset | Nine-slice | Shape yes | idle | pending |
| Dialog title | Project copy | Native text | Yes | dynamic | code |
| Confirm button | Component | Native + raster skin | Label yes | all | pending |
| Icon | Existing library | Vector | Yes | all | code |

Do not start implementation until every major ingredient has an assigned method.
