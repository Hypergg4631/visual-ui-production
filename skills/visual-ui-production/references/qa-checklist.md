# UI Production QA Checklist

## Source and Scope

- [ ] The selected mock is unambiguous and locally viewable.
- [ ] The latest failed or blurry variant is not being used as source of truth.
- [ ] Preserve/overhaul mode is explicit.
- [ ] Exact copy and behavior are listed separately from image-native visuals.
- [ ] No unrelated screen or component changed.

## Visual Fidelity

- [ ] The running capture and approved mock use the same viewport and UI state.
- [ ] Primary focal point and information hierarchy match.
- [ ] Major anchors, panel bounds, spacing rhythm, and safe areas match.
- [ ] Typography size, line height, weight, and alignment are coherent.
- [ ] Chinese text is crisp, correctly encoded, and not baked into generated assets unless truly image-native.
- [ ] Long labels, two-line text, dynamic values, and localization do not overlap.
- [ ] Text contrast remains readable over every supported background.
- [ ] Materials share one lighting and texture logic.
- [ ] No obvious AI template tells, random decorations, or fake telemetry remain.
- [ ] Raster assets are sharp at intended scale and do not reveal extraction fringes.

## Interaction

- [ ] Primary actions work end to end.
- [ ] Hover, focus, pressed, selected, disabled, loading, empty, success, and error states exist where applicable.
- [ ] Focus order is logical and visible.
- [ ] Mouse, keyboard, controller, and touch work as applicable.
- [ ] Hover feedback does not shift layout.
- [ ] Motion communicates state and respects reduced-motion preferences where supported.
- [ ] Sound is short, rate-limited, and synchronized with the visual response.
- [ ] Exit, back, cancel, and confirmation actions remain reachable.

## Responsive and Scaling

- [ ] Base resolution passes.
- [ ] Smallest supported resolution passes.
- [ ] Largest/wide supported resolution passes.
- [ ] Windowed and fullscreen scaling pass when applicable.
- [ ] No clipping, horizontal scroll, incoherent overlap, or off-screen primary action.
- [ ] Nine-slice corners remain stable at minimum and maximum sizes.

## Accessibility

- [ ] Body and control text reaches reasonable contrast, targeting WCAG AA when platform-appropriate.
- [ ] Interactive targets have adequate size.
- [ ] Meaning is not conveyed by color alone.
- [ ] Images and icons have labels/alt text where the platform supports them.
- [ ] Text scaling does not break the core flow.

## Runtime Safety

- [ ] No more than one app/game/server/test process was started.
- [ ] Existing process was reused or stopped before relaunch.
- [ ] CPU usage returned to normal after testing.
- [ ] No test process was left running at handoff.
- [ ] Test screenshots and logs were written outside production asset folders.

## File Hygiene

- [ ] No existing asset was overwritten without explicit approval.
- [ ] Final assets use versioned, descriptive names.
- [ ] Rejected variants are not referenced by project code.
- [ ] Every project-referenced asset exists inside the workspace.
- [ ] No runtime path points into temporary or generated-image storage.
- [ ] Asset inspection reports expected dimensions, alpha, and format.
- [ ] Only selected final assets were copied into production folders.

## Completion Gate

Do not report the UI complete unless:

1. the project runs;
2. the primary interaction works;
3. the same-state visual comparison passes;
4. no blocking overlap, text, contrast, or scaling issue remains;
5. no extra test process remains running.
