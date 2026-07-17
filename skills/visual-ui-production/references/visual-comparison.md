# Visual Comparison

Visual comparison closes the gap between an approved mockup and the running product.

## Capture Contract

Capture the same:

- viewport and scale;
- screen and content state;
- selected, hover, focus, and pressed state;
- background/scene;
- dynamic-data fixtures;
- animation time or paused frame.

Mask only genuinely dynamic regions such as clocks, live video, random avatars, or changing network data. Never mask a layout defect.

## Compare

```powershell
python scripts/compare_ui_screenshots.py `
  "approved-mock.png" `
  "running-screen.png" `
  --output-dir ".ui-production\comparison\load-screen-v1" `
  --pixel-threshold 24 `
  --max-changed-ratio 0.12 `
  --max-mean-error 18
```

Ignore a controlled dynamic region:

```powershell
--ignore-region 120,80,300,40
```

The script produces:

- `difference.png`;
- `changed_mask.png`;
- `heatmap.png`;
- `overlay.png`;
- `comparison_triptych.png`;
- `comparison_report.json`.

Exit code `0` means metrics passed. Exit code `2` means review is required.

## Interpretation

Pixel metrics are triage signals, not design judgment. Generated mockups and runtime rendering may differ in anti-aliasing, fonts, and background imagery.

Always visually review:

- hierarchy and composition;
- layout anchors and safe areas;
- material fidelity;
- typography, wrapping, and baseline alignment;
- contrast and readability;
- interactive states;
- unintended clipping, overlap, or layout shift.

## Acceptance Matrix

Capture at minimum:

- default/idle;
- hover;
- keyboard or controller focus;
- pressed or active;
- selected;
- disabled or empty;
- longest localized text;
- smallest supported viewport;
- return/navigation result.

Fix blocking discrepancies, capture a new versioned run, and repeat. Do not overwrite prior failed evidence.
