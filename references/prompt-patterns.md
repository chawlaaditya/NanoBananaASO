# Prompt Patterns

Use these as prompt shapes, not rigid copy.

If Nano Banana is the chosen path, write that explicitly in the working notes or prompt log so the workflow is reproducible and the style-anchor step is unambiguous.

In the prompt log, write `Nano Banana` explicitly and note whether credentials came from `GEMINI_API_KEY`, `GOOGLE_API_KEY`, or the user.

## 1. Style Anchor Prompt

```text
Create a premium iPhone App Store advertisement for [APP NAME].

Use the attached layout plan as the visual source of truth.
Use the attached app screenshot faithfully.
If a category-specific lifestyle or product image is attached, use it only as subtle background atmosphere.

Slide archetype:
[Typography-led hero / Hybrid ad / Product proof / Contextual-lifestyle / Brand-value]

Required copy:
Headline ([N] lines):
[LINE 1]
[LINE 2]
[Optional line 3]
Support: [SUPPORT]

Core message:
[MESSAGE]

Compact chips or side claims:
- [CHIP]
- [CHIP]

Layout direction:
[LAYOUT]

Lock these family traits in the anchor:
- typography scale and weight
- background language
- panel and chip treatment
- device treatment and shadows
- accent behavior
- supporting imagery language

Hard rules:
- preserve the supplied screenshot faithfully
- do not redesign the app UI
- let the visual concept explain the slide before the text does
- keep typography readable at thumbnail size
- keep the result portrait
- compose for a later center-crop to the final App Store size
- keep all critical text and focal visuals well inside safe margins
- keep headline and support copy comfortably inside the center-safe zone, not hugging the side edges
- leave sacrificial background space near the edges
- assume the first-pass portrait source may lose about 10 to 16 percent of width on each side during center-crop
- keep all must-read content inside the central 58 to 70 percent of the source width, not the full canvas
- keep the screenshot or core product visual as the hero
- avoid text-only billboard compositions
- use relevant supporting people, places, or objects only when they strengthen the app story
- make the slide feel art-directed, not templated
- make it feel like an ad, not a tutorial
- no fake ratings, no fake testimonials, no invented features
- do not render literal `<br />` characters in the final image
```

## 2. Follow-up Slide Prompt

```text
Create another App Store advertisement using the first attached image as the locked campaign style reference.

The first attached image should be the normalized export of slide 1, not a random raw render.

The result must clearly belong to the same visual family:
- same overall mood
- same typography quality
- same premium product-ad feel
- same restrained use of decorative elements
- same typography scale logic
- same panel and chip treatment
- same background language
- same device lighting and shadow treatment
- same supporting imagery language
- same proven crop-safe spacing and text-density decisions learned from the anchor
- same chip / CTA / badge sizing rules that survived normalization in the anchor

Use the attached layout plan as the ruleset.
Use the supplied screenshot faithfully.

Slide archetype:
[Hybrid ad / Product proof / Contextual-lifestyle]

Required copy:
Headline ([N] lines):
[LINE 1]
[LINE 2]
[Optional line 3]
Support: [SUPPORT]

Core message:
[MESSAGE]

Compact chips or side claims:
- [CHIP]
- [CHIP]

Layout direction:
[LAYOUT]

Hard rules:
- preserve the screenshot faithfully
- do not redesign the app UI
- prefer a stronger visual explanation over adding more text
- vary the layout from adjacent slides
- vary the archetype weight from adjacent slides when helpful
- use the same headline font family or type style as the anchor
- do not drift into serif headlines or a different typography voice unless the anchor already does that
- keep decorative elements behind or around the product
- make the background and motifs reinforce the slide message
- compose for a later center-crop to the final App Store size
- keep all critical text and focal visuals well inside safe margins
- keep headline, support, and chips inside the center-safe zone, especially on text-heavy slides
- leave sacrificial background space near the edges
- assume the first-pass portrait source may lose about 10 to 16 percent of width on each side during center-crop
- keep phones, copy, and proof fragments inside the central safe box rather than near the original edges
- keep the screenshot or product visual as the main focus
- avoid flat billboard layouts
- avoid oversized white text cards or giant copy panels unless they are part of the anchor's visual language
- use supporting imagery only when it clearly matches the product category and message
- no fabricated claims
- do not render literal `<br />` characters in the final image
```

## 3. Typography-Led Hero or Brand Slide Prompt

Use this when the campaign needs a punchier ad slide with little or no screenshot emphasis.

```text
Create a premium App Store campaign slide using the first attached image as the campaign style reference.

This should feel like a bold advertisement, not a tutorial panel.

Slide archetype:
Typography-led hero or brand-value

Required copy:
Headline ([N] lines):
[LINE 1]
[LINE 2]
[Optional line 3]
Support: [SUPPORT]

Core message:
[MESSAGE]

Visual motifs:
- [ICON / OBJECT / BADGE / SCENE]
- [ICON / OBJECT / BADGE / SCENE]

Layout direction:
[LAYOUT]

Hard rules:
- use oversized, highly readable typography, but do not let text completely replace the visual idea
- use oversized, highly readable typography
- do not fabricate a fake screenshot
- if you include the app icon, object, mascot, or lifestyle cutout, make it feel premium and category-specific
- use only 1 to 3 strong motifs, not a pile of filler
- keep the slide in the same campaign family as the style reference
- avoid generic AI imagery, robots, and cloud clichés
- keep the composition energetic but controlled
- compose for a later center-crop to the final App Store size
- keep all critical text and focal visuals well inside safe margins
- keep the copy block comfortably inside the center-safe zone
- leave sacrificial background space near the edges
- assume the first-pass portrait source may lose about 10 to 16 percent of width on each side during center-crop
- keep the full headline block well inside the central safe box instead of stretching it toward the edges
- do not render literal `<br />` characters in the final image
```

## 4. Value Slide Prompt

Use this when there is no screenshot.

```text
Create a premium App Store value slide using the first attached image as the campaign style reference.

This slide has no app screenshot. Build a typography-led brand/value composition in the same campaign family.

Slide archetype:
Brand-value

Required copy:
Headline ([N] lines):
[LINE 1]
[LINE 2]
[Optional line 3]
Support: [SUPPORT]

Core message:
[MESSAGE]

Layout direction:
[LAYOUT]

Hard rules:
- do not fabricate a fake app screen
- use 2 to 3 meaningful premium panels or motifs to sell the claims
- let the motifs and composition communicate most of the meaning before the copy does
- avoid generic AI imagery, robots, and cloud clichés
- prefer concrete category symbols such as rewards, certificates, routes, coins, objects, scenes, or brand characters when relevant
- keep typography readable at thumbnail size
- keep the composition advertisement-first
- make the visual motifs directly reinforce the claims instead of acting as filler
- compose for a later center-crop to the final App Store size
- keep all critical text and focal visuals well inside safe margins
- keep the copy block comfortably inside the center-safe zone
- leave sacrificial background space near the edges
- assume the first-pass portrait source may lose about 10 to 16 percent of width on each side during center-crop
- keep value panels, symbols, and copy inside the central safe box
- avoid empty, lifeless backgrounds
- do not render literal `<br />` characters in the final image
```
