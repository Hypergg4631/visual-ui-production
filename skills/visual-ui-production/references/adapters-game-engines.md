# Game Engine UI Adapter

Use this adapter for Unity, Godot, Unreal, and other game engines. For Ren'Py, use the dedicated `adapters-renpy.md` instead.

## Project Detection

Identify:

- engine and version;
- active UI system and scene/prefab ownership;
- reference resolution, stretch/scaling mode, safe areas, and aspect-ratio policy;
- input maps, mouse/controller/touch support, focus navigation, and localization;
- theme/style resources, atlases, fonts, audio buses, tween/animation helpers, and test scenes;
- run and screenshot commands.

Preserve the project's active UI technology. In Unity, do not switch between UI Toolkit and Canvas without approval. In Godot, use the established `Control`/theme structure.

## Implementation Mapping

| Design ingredient | Preferred implementation |
|---|---|
| Layout | Engine UI containers, anchors, constraints, and safe-area helpers |
| Exact text and values | Engine text components with localization |
| Material frame | Nine-slice/sliced sprite or theme box |
| Button visual | Stateful sprite/style resource on a real button control |
| Icon | Existing atlas/vector support or approved asset |
| Screen illustration | Texture/image resource with explicit scaling policy |
| Focus/selection | Input-aware focus state and navigation graph |
| Motion | Engine tween/animation system |
| Sound | Existing UI audio bus and event hooks |

Do not render a full menu as one texture with coordinate hotspots. Keep focus, text, values, actions, and accessibility/modality logic in engine controls.

## Engine Notes

### Unity

- Reuse the existing Canvas or UI Toolkit architecture.
- For Canvas, use anchors, layout groups, `Image.Type = Sliced`, TextMeshPro, selectable navigation, and event-system input.
- For UI Toolkit, use visual elements, USS variables/classes, focus behavior, and nine-slice style properties.
- Store reusable surfaces as prefabs or style resources rather than duplicating scene markup.
- Test gamepad, keyboard, pointer, and supported touch paths.

### Godot

- Use `Control` nodes, containers, anchors, theme resources, `StyleBoxTexture`, and localized `Label`/`Button` controls.
- Keep focus neighbors and input actions explicit.
- Use theme overrides only when a reusable theme resource is not appropriate.
- Test stretch mode, viewport scaling, and project input actions.

### Unreal and Others

- Use the established widget system, layout panels, style assets, navigation, localization, and input abstraction.
- Use nine-slice or box-draw resources for material frames.
- Keep reusable widgets separate from level-specific presentation.

## Resolution and Safe Area

Record the reference resolution and scaling mode in the design lock. Test:

- approved reference resolution;
- one wider aspect ratio;
- one narrower or handheld aspect ratio when supported;
- platform safe areas;
- text expansion and localization;
- controller focus with no pointer present.

Character art, scene art, and full-screen material may crop intentionally, but command controls and critical values must remain inside safe areas.

## Motion and Sound

- Common hover/focus feedback should normally settle within 100-200 ms.
- Selection and confirm sounds must fire once per state change or activation.
- Reduced-motion and reduced-flash settings must disable or soften relevant effects.
- Motion must not resize layout tracks or move the hit target unexpectedly.

## Capture and Comparison

1. Open one editor or standalone game process only.
2. Use a deterministic UI test scene or stable save state.
3. Freeze unrelated animation, particles, clock values, and random background events when possible.
4. Capture the exact target resolution and input modality.
5. Capture idle, focus/hover, selected, and modal states separately where applicable.
6. Compare against the approved mock with documented masks for intentionally dynamic scene areas.
7. Confirm no editor or game process remains after the test.

## Acceptance

The game UI is ready only when:

- mouse, keyboard, controller, and touch paths work as applicable;
- focus cannot become trapped or disappear;
- material assets preserve the approved identity at supported resolutions;
- exact text and values remain runtime-rendered;
- scene transitions, sound timing, and feedback states behave correctly;
- comparison artifacts and tested resolutions/input modes are recorded.
