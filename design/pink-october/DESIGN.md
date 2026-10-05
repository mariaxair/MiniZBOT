# Design System: ZAD — Pink October Campaign

Scope: social posts (4:5, 1080×1350) for ZAD AI's Breast Cancer Awareness Month campaign. Reference build: `pink-october.html` → `pink-october.png`.

## 1. Visual Theme & Atmosphere
A tactile, layered poster with real depth, like a satin ribbon resting on draped blush silk under soft studio light. Every layer has volume: an extruded title, a ribbon with selvedge edges and sheen, embossed rings, silk folds, and a fine grain over the whole canvas. Warm and hopeful, never clinical or sugary.

- **Density 6 — "Balanced, Filled":** no dead white zones. Every vertical band carries a ribbon, a ring, a drape or type. Margins are 56–72px, not airy gallery space.
- **Variance 3 — "Composed Symmetric":** a centered axis is intentional for a poster. Energy comes from offset title lines (Pink pushed left, October pushed right) and a −4° ribbon tilt, not from asymmetric layout.
- **Motion 0 — Static:** this is a print/social still. If animated for Reels or Stories, use only a slow shimmer across the ribbon's sheen band (transform/opacity, 4–6s loop).

## 2. Color Palette & Roles
- **ZAD Deep Green** (#044132) — Logo, identity line 1, tagline. The only cool color, and it anchors the composition.
- **ZAD Signal Pink** (#E2468A) — Identity line 2, ribbon mid-tone, tagline separator. The single accent.
- **Raspberry Ink** (#A3164F) — Title face. Its extrusion steps darken to #B42A62 → #921548.
- **Ribbon Satin Ramp** (#F9AFCB → #EF74A2 → #E2468A → #C42B6E) — Ribbon body gradient running along its length. Selvedge edge is #C12A69.
- **Blush Canvas** (#FFF8FA → #FBE4EB → #F3C2D2 → #E596B2) — Background, lightest at the top behind the logo and deepest at the bottom behind the card.
- **Frost Surface** (rgba(255,255,255,0.80 → 0.56)) — Identity card fill, with a 1px pure-white rim.
- **Shadow Wine** (#86103F / #6E0B35 at 0.35–0.50) — All shadows are tinted to the pink family, never grey or black.
- **Banned:** pure black (#000000), grey shadows, neon glows, mint/teal backgrounds (mint was the old flat base; green now lives only in type).

## 3. Typography Rules
- **Display — Fraunces Italic** (opsz 144, SOFT 100, WONK 1, weight 600), 162px, line-height 0.9, tracking −0.03em. Its soft, rounded curves replace the old thin script, which was illegible at feed size and had no weight. Volume comes from a 4-step 1px extrusion plus two soft drop shadows. Avoid gradient fills on the title.
- **Tagline — Fraunces Italic** (opsz 48, SOFT 100, weight 400), 35px, ZAD Deep Green. The separator is a pink middle dot.
- **Identity lines — Inter (brand identity, locked):** line 1 Inter 400, 35px, Deep Green; line 2 Inter 700, 32px, Signal Pink with a soft pink glow shadow. These are the only Inter usages. Do not restyle or swap them.
  - *Note:* the taste baseline bans Inter for premium contexts. ZAD's identity overrides that for these two lines only.
- **Logo:** the ZAD wordmark in Deep Green, 176px wide, centered, 72px from the top. `zad-logo.svg` is traced from a screenshot. Swap in the official vector logo for production.
- **Banned:** script/calligraphy fonts for the title, generic serifs (Times, Georgia, Garamond), all-caps body copy.

## 4. Component Stylings
- **Awareness Ribbon (hero object):** a flat satin strip (100u wide, rendered ~80px), not a tube. Layers from bottom to top: selvedge edge stroke → body gradient → offset wine shade (blurred, right side) → one soft sheen band (left side) → a hairline specular thread on each edge → a fine directional weave noise (soft-light). The front strand crosses on top with its own contact shadow. Tails end in V-notch (swallowtail) cuts, and the cast shadow follows the cut shape.
- **Identity Card:** a frosted glass slab, 40px radius, full width minus 56px margins, pinned 56px from the bottom. It has an inset top highlight, an inset bottom pink edge, and a two-layer pink-tinted drop shadow. Use this as the only card on the canvas.
- **Embossed Rings:** concentric circles (r 290–650, step 90) centered behind the ribbon. Each ring is a 2px white stroke shifted −1.5px plus a 2px wine stroke at 17% shifted +1.5px, so it reads as pressed into the paper.
- **Silk Drapes:** two overlapping wave bands in the lower third with gradient fills, a blurred wine under-shadow and white crest highlights. Lighter blurred wisps sit at the title's shoulders.
- **Light Orbs:** 8–10 white circles (6–56px), mostly blurred, on the flanks only. Keep them out of the type and ribbon zones.
- **Grain:** full-canvas fractal noise (baseFrequency 0.9, 3 octaves), wine-tinted, multiply blend, beneath the type.

## 5. Layout Principles
Vertical zones on a 1350px canvas, with no element overlapping another's zone:

| Zone | Y range | Content |
|---|---|---|
| Brand | 72–135 | ZAD logo |
| Title | 146–435 | Pink / October, offset −118px / +64px |
| Hero | 476–1020 | Ribbon, −4° tilt, centered on the ring origin (540, 740) |
| Tagline | 1046–1085 | Single line, centered |
| Identity | 1124–1294 | Frosted card with the two Inter lines |

- Side margins are 56px for the card and at least 64px for all type.
- The ribbon must not touch the title. Keep a minimum gap of 24px.
- Background layers (rings, drapes, orbs, grain) can run under everything. Foreground elements never overlap each other.
- Other formats: for Story (1080×1920), add 285px to both the Title and Hero zones and keep the card pinned to the bottom. For Square (1080×1080), drop the tagline and scale the ribbon to 0.62.

## 6. Motion & Interaction
Static by default. For an animated variant: a sheen band translating along the ribbon (opacity 0.35 → 0.6, 5s ease-in-out loop), orbs floating ±6px on staggered 7–11s loops, and grain held still. Animate only `transform` and `opacity`.

## 7. Anti-Patterns (Banned)
- Flat vector ribbons with a single gradient and no edge, shadow or texture
- Large empty white or mint fields. Every band must carry content or texture.
- Thin calligraphic scripts for the headline
- Text written along the ribbon (illegible at feed size)
- Grey or black drop shadows; neon or outer glows on pink
- More than one card or panel on the canvas
- Emojis, stock-photo hands holding ribbons, generic "hope" clip-art (doves, hearts)
- AI copy clichés ("Empower", "Elevate", "Unleash")
- Changing the ZAD logo, its color, or the Inter identity lines

---

## Variant B: Minimal Editorial (`pink-october-minimal.html`)
A quiet, editorial poster on warm paper. Built on negative space, one pastel shape and type contrast. There are no gradients, shadows or glass effects.

- **Palette:** Warm Bone canvas (#F7F5F2), Pale Pink disc (#FBE6EA), Rule Grey 1px lines (#E4DFD8), Off-Black ink (#1E2422), Muted meta (#7A7672). Accents are only ZAD Deep Green (#044132) and ZAD Signal Pink (#E2468A).
- **Type:**
  - Instrument Serif, 268px, line-height 0.86, tracking −0.035em: "Pink" in italic Signal Pink, "October" in roman Off-Black.
  - Tagline: Instrument Serif Italic, 50px.
  - Meta labels: Geist Mono, 18–20px, uppercase, +0.08em tracking.
  - Identity lines: Inter, unchanged and locked.
- **Grid:** 72px outer margins on every side. A header row (logo left, date right), then a 1px rule. The title sits left-aligned. Below it, the tagline is on the left and the ribbon on the right. A 1px rule sits above the left-aligned identity lines.
- **Ribbon:** one flat Signal Pink shape. The crossing is shown by a 16u knockout gap in the disc color, not by shading. The tails break out below the disc edge.
- **Texture:** only a 5% monochrome grain. Nothing else adds depth.
- **Banned in this variant:** gradients, drop shadows, glass cards, glows, more than one pastel shape, centered layouts.
