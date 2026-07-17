# Aesthetic System

## Read the Domain

Design for the product's repeated task and audience.

- Operational tools should feel quiet, efficient, familiar, and scan-friendly.
- Games may be expressive, but controls still need immediate affordance and readable state.
- Horror and mystery should earn atmosphere through composition, texture, pacing, and sound, not by making every control dark and unreadable.
- Consumer and campaign surfaces may use stronger imagery and type, but the action path must remain obvious.

Avoid applying a favorite visual style without evidence from the brief.

## Preserve Before Inventing

For redesigns, inventory:

- brand colors and type;
- signature materials, motifs, and sounds;
- navigation and information architecture;
- repeated component vocabulary;
- labels, shortcuts, save behavior, and analytics-sensitive identifiers;
- accessibility wins;
- patterns the user explicitly approved.

Modernize in this order: typography, spacing/rhythm, color calibration, state feedback, key composition, then full component replacement.

## Anti-Template Rules

Reject these defaults unless the brief explicitly calls for them:

- purple-blue gradients, glowing blobs, generic glassmorphism, and neon-on-black;
- beige paper plus brass as automatic "premium" styling;
- three equal cards, card-inside-card layouts, and pills for every label;
- centered hero/title over an abstract background when the product has real imagery;
- arbitrary tiny uppercase labels, decorative version numbers, fake telemetry, and meaningless dots;
- identical rounded rectangles for every action;
- display fonts inside compact buttons, settings, tables, or dense menus;
- texture pasted uniformly across every surface;
- motion applied to every element with the same timing;
- ornamental metal frames that ignore actual hit areas and scalable content.

If a viewer can identify the design as an AI template before understanding the product, redesign it.

## Hierarchy

Create one primary focal point per screen. Use size, contrast, spacing, position, and motion in that order. Do not make every section equally loud.

Match typography to container scale:

- hero or title screens may use display type;
- dialogs, settings, save slots, and toolbars need compact, stable type;
- labels and values need a tighter ratio than marketing headings;
- long Chinese labels require tested line-height and width, not viewport-scaled type.

Keep body text readable and avoid low-contrast secondary text that disappears against atmospheric imagery.

## Color

Use a small role-based palette:

- canvas/background;
- primary surface;
- secondary surface;
- primary text;
- secondary text;
- accent/selection;
- focus;
- danger, warning, success, and disabled.

Use accent color for action and state, not decoration. Test contrast in the actual scene, not only on a swatch.

## Shape and Material

Use one shape system and one material logic. A wet-metal button, paper save slot, and glass dialog can coexist only if the fiction explains the relationship.

For image-led materials:

- preserve a quiet center for text;
- keep corners and ornaments outside the content-safe region;
- use nine-slice construction for scalable frames;
- avoid random scratches crossing text or focus indicators;
- ensure hover and pressed states change affordance without shifting layout.

## Interaction and Motion

Every interactive component needs the applicable states: default, hover, focus, pressed, selected, disabled, loading, and error.

Use 100-200 ms for common game/menu feedback and roughly 150-250 ms for product UI transitions. Motion must communicate hierarchy, state, or feedback. Provide reduced-motion behavior when the platform supports it.

Use sound sparingly:

- hover: quiet and rate-limited;
- confirm: distinct but short;
- cancel/back: softer and lower;
- error: recognizable without being punishing.

Never let sound or animation delay the command.

## Reference Use

Study references for principles: hierarchy, density, materials, typography, motion, and interaction. Do not clone branded layouts or proprietary assets.

When the user asks to "learn from good work," browse current official or primary visual sources when possible, summarize the principles, then generate an original direction grounded in the user's product.
