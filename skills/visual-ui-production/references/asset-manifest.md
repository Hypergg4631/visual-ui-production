# Asset and Implementation Manifest

The manifest is the bridge from an approved visual to maintainable product code.

Create a manifest only from an approved design lock:

```powershell
python scripts/build_asset_manifest.py init `
  --design-lock ".ui-production\load-screen.design-lock.json" `
  --output ".ui-production\load-screen.asset-manifest.json" `
  --output-root "assets\ui\load-screen"
```

The initial manifest intentionally marks components as `unresolved`. Resolve every component before editing production code.

## Allowed Implementation Methods

- `semantic-control`: button, input, slider, switch, tab, menu, list, focus target.
- `runtime-text`: labels, timestamps, counters, localized copy, dynamic values.
- `native-shape`: simple solid fills, spacing, masks, separators, focus rings.
- `raster-asset`: texture, atmospheric image, ornate frame, illustrated surface, irregular silhouette.
- `existing-asset`: approved project asset reused without duplication.
- `icon-library`: standard semantic icon from the existing product library.
- `animation`: state or transition behavior.
- `sound`: hover, confirm, cancel, warning, or error feedback.
- `intentional-omission`: approved element intentionally excluded from runtime.

## Component Record

Every visible component must include:

- stable `id` and human-readable `name`;
- implementation `method`;
- source mock or existing source asset;
- versioned output path;
- dimensions, alpha, and optional nine-slice insets;
- required states;
- dynamic content rendered at runtime;
- consuming file, screen, scene, or component;
- implementation notes.

## Production Gate

The manifest is not production-ready while any component remains `unresolved`.

```powershell
python scripts/build_asset_manifest.py validate ".ui-production\load-screen.asset-manifest.json"
```

Use `--allow-unresolved` only while planning.

## State Matrix

For each interactive component, record applicable states:

| State | Visual Requirement | Behavioral Requirement |
|---|---|---|
| idle | clear default affordance | accepts focus and pointer |
| hover | visible without layout shift | 100-180 ms, rate-limited sound |
| pressed | material compression or tonal change | command is not delayed |
| focus | keyboard/controller-visible | meets contrast requirements |
| selected | persistent state | survives screen refresh |
| disabled | visibly unavailable | cannot activate |
| loading/error | only when applicable | announced and recoverable |

Text, screenshots, dates, usernames, prices, scores, and localization must remain dynamic even when surrounded by raster material.
