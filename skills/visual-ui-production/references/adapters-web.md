# Web Product Adapter

Use this adapter for websites and browser products built with React, Vue, Svelte, Next.js, Nuxt, Vite, or standalone HTML/CSS/JS.

## Project Detection

Inspect:

- `package.json`, lockfiles, framework config, and scripts;
- routes, page entry points, component folders, design tokens, and CSS strategy;
- existing icon, animation, form, and accessibility libraries;
- supported browsers, viewport breakpoints, themes, and localization;
- the established local start, test, and build commands.

Do not introduce a new UI framework or styling system unless the project has no usable one and the user approves the dependency.

## Implementation Mapping

| Design ingredient | Preferred implementation |
|---|---|
| Page structure | Semantic HTML and framework layout components |
| Responsive geometry | CSS Grid, Flexbox, container queries, and stable constraints |
| Exact copy and values | Runtime text and data binding |
| Standard icons | Existing icon library or accessible inline vector |
| Material skin | Layered raster asset, `border-image`, mask, or pseudo-element |
| Ornate scalable frame | Nine-slice equivalent using `border-image` or sliced layers |
| Illustration or photography | Responsive image asset with explicit dimensions |
| Hover/focus/pressed | Real component states, never baked into a screenshot |
| Motion | Existing motion library or CSS transitions with reduced-motion fallback |

Never use one full-screen mockup image with invisible hotspots. The approved image defines composition; the product remains semantic and responsive.

## Component Requirements

- Preserve native links, buttons, labels, inputs, dialogs, menus, and landmarks.
- Keep exact text out of generated images.
- Keep hit areas stable when visuals animate.
- Implement visible keyboard focus and logical tab order.
- Use `aria-*` only when native semantics are insufficient.
- Define loading, empty, error, disabled, and long-content states where relevant.
- Use stable image dimensions and aspect ratios to prevent layout shift.
- Keep touch targets at least 44 by 44 CSS pixels unless the established system is stricter.

## Responsive Contract

Record named viewports in the design lock. At minimum test:

- the selected desktop reference viewport;
- one narrow mobile viewport;
- one intermediate or tablet viewport when layout topology changes.

Do not scale font size directly with viewport width. Reflow layout at deliberate breakpoints. Confirm that the longest localized string fits without clipping.

## Asset Placement

Follow the existing public/static/import convention. Prefer:

- WebP or AVIF for opaque photographic material when supported;
- PNG for alpha-heavy UI skins;
- SVG only for genuine vector geometry;
- versioned filenames until the selected asset is approved.

Record each asset import and consuming component in the manifest.

## Capture and Comparison

Use the existing browser test setup. If none exists, use Playwright:

1. start one development server;
2. wait for the page readiness signal, not a fixed arbitrary delay;
3. set viewport, color scheme, reduced-motion preference, and test data;
4. navigate to the exact state;
5. hide only approved nondeterministic regions;
6. capture a versioned screenshot;
7. run `compare_ui_screenshots.py`;
8. stop the server after validation.

Capture hover and keyboard focus separately when those states materially alter the visual.

## Acceptance

The web implementation is ready only when:

- semantic controls and keyboard navigation work;
- selected desktop composition matches the approved lock;
- mobile layout is intentionally adapted rather than merely shrunk;
- image-native material retains its approved texture and depth;
- no text, focus ring, menu, or dynamic value is baked into a bitmap;
- comparison artifacts and tested viewport names are recorded.
