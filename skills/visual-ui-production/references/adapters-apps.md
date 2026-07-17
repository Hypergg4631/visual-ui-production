# Mobile and Desktop App Adapter

Use this adapter for Flutter, SwiftUI/UIKit, Jetpack Compose/Android Views, Qt, WPF, WinUI, Electron, Tauri, and similar application stacks.

## Project Detection

Identify:

- platform targets and active UI toolkit;
- application entry point, navigation, view model/state architecture, and theme system;
- DPI or density behavior, window-size policy, safe areas, text scaling, and localization;
- existing icons, fonts, accessibility labels, dialogs, and animation helpers;
- build, run, test, emulator, simulator, and screenshot commands.

Use the established toolkit. Do not replace native or project-standard controls only to imitate a screenshot.

## Universal Mapping

| Design ingredient | Preferred implementation |
|---|---|
| Layout and navigation | Existing native/widget layout system |
| Exact text and values | Runtime text with localization support |
| Forms and commands | Semantic native controls or project components |
| Material panels and frames | Raster/vector skin behind real controls |
| Scalable ornamental surface | Nine-slice, cap insets, stretch regions, or framework equivalent |
| Photography/illustration | Density-aware image resources |
| Window or modal behavior | Platform dialog/window primitives unless fiction requires custom UI |
| Motion and feedback | Toolkit animation APIs plus reduced-motion setting |

Separate visual skin from command behavior. A generated button face may decorate a real button, but must not replace focus, activation, accessibility, or disabled logic.

## Platform Requirements

### Mobile

- Respect safe areas, status/navigation bars, keyboard insets, rotation policy, and display cutouts.
- Test dynamic text size and the longest localized labels.
- Keep primary touch targets at least 44 by 44 points on iOS and 48 by 48 density-independent pixels on Android unless existing guidance is stricter.
- Do not rely on hover.
- Verify screen-reader labels and traversal order.

### Desktop

- Respect DPI scaling, resizable windows, minimum window size, keyboard shortcuts, and high-contrast settings.
- Keep familiar close, cancel, save, and destructive-action behavior.
- Verify tab order, focus visibility, mouse hit regions, and window restoration.
- For Electron/Tauri, keep web semantics and also test native window behavior.

## Toolkit Notes

- **Flutter**: use widgets, themes, `MediaQuery`, semantics, and golden tests; use `centerSlice` for nine-slice material.
- **SwiftUI/UIKit**: use dynamic type, safe-area APIs, accessibility labels, asset catalogs, and resizable images with cap insets.
- **Compose/Android Views**: use density-independent layout, content descriptions, state semantics, and scalable drawables or nine-patch assets.
- **Qt/WPF/WinUI**: use native layout containers, commands/bindings, DPI-aware assets, focus visuals, and framework screenshot tooling.
- **Electron/Tauri**: follow the web adapter for the renderer and validate native menus, dialogs, window sizing, and platform packaging.

## Asset Placement

Follow the platform resource system and generate required density variants only from an approved master. Record:

- logical dimensions and source pixel dimensions;
- density or scale variants;
- stretch/cap insets;
- light/dark theme applicability;
- localization or directionality constraints;
- consuming view/component.

Do not manually create near-identical assets when the platform can scale one verified source safely.

## Capture and Comparison

1. Use one emulator, simulator, app, or desktop process at a time.
2. Set deterministic test data, theme, locale, text scale, window size, and device profile.
3. Navigate to the exact approved state.
4. Capture through the toolkit's existing screenshot/golden mechanism.
5. Compare at the lock's logical viewport; use platform-specific masks only for nondeterministic system chrome.
6. Inspect the result at 100 percent and at normal device scale.

## Acceptance

The application UI is ready only when:

- the approved hierarchy and material language are preserved;
- platform behavior remains familiar and accessible;
- safe areas, DPI, text scaling, and localization do not break layout;
- all required states are real interactive states;
- generated material is implemented as maintainable resources, not a flattened screenshot;
- comparison artifacts and device/window profiles are recorded.
