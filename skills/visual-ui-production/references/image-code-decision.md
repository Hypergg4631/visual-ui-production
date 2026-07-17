# Image Versus Code Decision Rules

Apply this decision before producing assets or implementation.

## Hard Rule

If a visual element depends on material, lighting, wear, grain, irregular edges, film, wood, paper fibers, embossing, painted metal, illustrated scenery, or complex ornamental shape, do not reduce it to a plain rectangle and thin border. Produce or reuse an image-native asset.

If an element carries behavior, exact text, localization, dynamic values, accessibility semantics, focus, or user input, keep it as a real runtime control.

Most polished UI components are hybrids: raster material behind a semantic control.

## Decision Table

| Element | Default Method |
|---|---|
| background scene or atmospheric plate | raster asset |
| textured panel or irregular frame | raster asset, usually nine-slice |
| complex button material | raster state family behind semantic button |
| simple separator or flat fill | native shape |
| text, date, price, score, page number | runtime text |
| button, checkbox, slider, tab, field | semantic control |
| standard icon | existing icon library |
| unique story or brand symbol | approved vector or raster asset |
| screenshot/save thumbnail/avatar | dynamic runtime image |
| glow, fog, grain, vignette | shader/native effect when stable; raster overlay otherwise |

## Reject as Pure-Code Slop

Reject an implementation when the approved mock relies on rich material but runtime replaces it with:

- uniform 1 px outlines;
- plain translucent rectangles;
- repeated identical cards;
- untextured gradients;
- CSS/Ren'Py borders pretending to be wood, film, paper, or metal;
- decorative lines that do not correspond to hierarchy or behavior.

## Reject as Baked Screenshot UI

Do not paste the entire approved mockup as a screen background while placing invisible hit areas over it. This breaks localization, accessibility, dynamic content, scaling, and maintainability.

## Hybrid Construction

Use this order:

1. atmospheric background or scene plate;
2. scalable material surfaces;
3. semantic layout and controls;
4. runtime text and values;
5. state overlays, focus, motion, and sound;
6. final texture/grain overlay only when it does not reduce readability.

## Raster Asset Requirements

- clean registration and documented dimensions;
- transparent background when the silhouette requires it;
- quiet safe center for text;
- corners and ornaments outside stretch regions;
- no baked labels, dates, values, screenshots, or focus indicators;
- versioned file name;
- complete visual state family when texture changes by state.
