# Ren'Py Adapter

Load this adapter only for Ren'Py projects.

## Audit

Inspect:

- `game/gui.rpy`, `game/screens.rpy`, `game/options.rpy`, theme files, and custom screens;
- configured virtual resolution and `gui.scale` behavior;
- existing fonts, transitions, sounds, transforms, save compatibility, and navigation;
- image and test directories;
- every consumer of shared styles before editing them.

Do not change labels, routes, save semantics, rollback behavior, or preferences without explicit approval.

## Mapping

| Visual Ingredient | Ren'Py Method |
|---|---|
| textured scalable frame | `Frame("asset.png", left, top, right, bottom)` |
| material button states | semantic `button` with idle/hover/selected backgrounds |
| exact runtime text | `text` or `textbutton`, never baked into assets |
| save thumbnail | `FileScreenshot(slot)` |
| save metadata | `FileTime`, `FileSaveName`, `FileSlotName` |
| checkbox/preference | semantic button/toggle using preference actions |
| slider | `bar` with preference value |
| focus/controller state | style focus/selected state and key navigation |
| hover/press motion | transform, usually 100-180 ms |
| UI sound | `hover_sound`/`activate_sound`, short and non-blocking |

## Coordinate and Scaling Rules

- Treat `config.screen_width` and `config.screen_height` as the virtual canvas.
- Verify whether project helpers already scale values before calling `gui.scale`.
- Do not double-scale absolute coordinates.
- Prefer `xalign`, `yalign`, stable containers, grids, and fixed dimensions over scattered coordinates.
- Test at the configured virtual resolution and at least one windowed scale.
- Keep text inside stable width/height containers to prevent layout shifts.

## Asset Rules

- Store selected runtime assets in the established project UI asset directory.
- Keep generated drafts and screenshots outside production assets.
- Use versioned names until the screen is frozen.
- Use PNG/WebP for raster material; validate alpha.
- Use `Frame`/nine-slice for scalable material and keep the center low-detail.
- Do not rasterize Chinese labels, dates, slot names, page numbers, or preference values.

## Implementation Sequence

1. Validate the approved design lock.
2. Resolve every asset manifest component.
3. Generate or extract empty material assets without text.
4. Inspect dimensions, alpha, and duplicates.
5. Implement a new screen or narrowly update the existing screen.
6. Add idle, hover, pressed, focus, selected, and disabled states.
7. Add restrained motion and sound.
8. Run Ren'Py lint.
9. Run one targeted test process and capture exact states.
10. Compare captures against the approved mock.
11. Stop the process and verify no Python/Ren'Py process remains.

## Save/Load Screen Requirements

Test:

- empty slot and occupied slot;
- selected, hovered, and disabled slot;
- quick-save and auto-save pages;
- page numbers beyond page one;
- correct absolute slot numbering;
- delete action and confirmation;
- dynamic thumbnail, timestamp, and save name;
- mouse, keyboard, and controller navigation;
- return to previous screen and main menu;
- no save-data format change.

## Test Isolation

Use unique directories for screenshots, logs, and Ren'Py app data. Never overwrite a previous failed capture by default. Keep at most one process active.

Typical sequence:

```powershell
$env:APPDATA = "D:\project\tests\appdata\ui-test-v1"
$env:LOCALAPPDATA = $env:APPDATA
python renpy.py "D:\project\game-project" lint
python renpy.py "D:\project\game-project" test ui_screen_test_v1 --report-detailed
```

Run lint and test sequentially, never concurrently.
