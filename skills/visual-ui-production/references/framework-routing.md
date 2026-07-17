# Framework Routing

Keep the visual workflow framework-independent. Select one implementation adapter only after the design lock and asset manifest exist.

## Detection Order

1. Read project metadata and existing source files.
2. Detect the active UI framework and build/runtime commands.
3. Detect resolution, scaling, localization, accessibility, state management, and asset conventions.
4. Prefer existing components and design tokens.
5. Load only the relevant adapter reference.

## Adapter Contract

Every framework adapter must define:

- project and entry-point detection;
- production asset directories and naming;
- semantic controls and dynamic text;
- scalable raster surface method;
- state, focus, accessibility, and localization handling;
- animation and sound integration;
- screenshot capture command;
- single-process runtime rule;
- visual comparison and acceptance states;
- rollback and file-hygiene behavior.

## Routing

| Project Evidence | Adapter |
|---|---|
| `.rpy`, Ren'Py SDK, `game/` | `adapters-renpy.md` |
| `package.json`, React/Vue/Svelte/Next/Vite | `adapters-web.md` |
| standalone HTML/CSS/JS | `adapters-web.md` |
| `project.godot` | `adapters-game-engines.md` |
| Unity or Unreal project folders | `adapters-game-engines.md` |
| `pubspec.yaml` | `adapters-apps.md` |
| Swift/Xcode project | `adapters-apps.md` |
| Android Gradle project | `adapters-apps.md` |
| Qt, WPF, WinUI, Electron, Tauri | `adapters-apps.md`; also use `adapters-web.md` for web renderers |

## Universal Implementation Rules

- Preserve behavior and information architecture before replacing visuals.
- Use raster assets only for image-native material.
- Keep text, values, inputs, focus, and actions semantic.
- Do not replace the project's framework for visual convenience.
- Implement all required states from the manifest.
- Capture the same viewport and state as the approved mock.
- Run at most one app, game, browser, simulator, or test process at a time.

## Web and App Baseline

For web and app projects:

- preserve responsive breakpoints or define them in the design lock;
- use stable component dimensions and test long/localized text;
- use CSS/native layout for structure, not coordinates baked into images;
- expose hover only where pointer input exists;
- test keyboard focus, touch targets, reduced motion, and contrast;
- capture desktop and mobile states with the established test framework.

## Game Engine Baseline

For Unity and Godot:

- preserve input maps, controller navigation, safe areas, and resolution policies;
- use nine-slice/sliced sprites for material frames;
- keep labels and values in engine text components;
- test controller focus, mouse hover, localization, and scene transitions;
- capture deterministic scenes without unrelated animation when comparing.

## Unsupported or Ambiguous Stacks

When no dedicated adapter exists:

1. infer the framework from source and build metadata;
2. apply the universal adapter contract above;
3. use the closest product-family adapter for interaction, scaling, and validation;
4. document the framework-specific mapping before production edits;
5. do not make the beginner choose implementation primitives.
