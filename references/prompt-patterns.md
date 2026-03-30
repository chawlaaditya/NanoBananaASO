# Prompt Patterns

Use these as prompt shapes, not rigid copy.

If Nano Banana is the chosen path, write that explicitly in the working notes or prompt log so the workflow is reproducible and the style-anchor step is unambiguous.

If Nano Banana is implemented through Gemini, write that explicitly as `Nano Banana via Gemini Pro Image Preview`.

## 1. Style Anchor Prompt

```text
Create a premium iPhone App Store advertisement for [APP NAME].

Use the attached layout plan as the visual source of truth.
Use the attached app screenshot faithfully.
If a category-specific lifestyle or product image is attached, use it only as subtle background atmosphere.

Required copy:
Headline: [HEADLINE]
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
- keep typography readable at thumbnail size
- keep the result portrait
- compose for a later center-crop to the final App Store size
- keep all critical text and focal visuals well inside safe margins
- leave sacrificial background space near the edges
- keep the screenshot or core product visual as the hero
- avoid text-only billboard compositions
- use relevant supporting people, places, or objects only when they strengthen the app story
- make it feel like an ad, not a tutorial
- no fake ratings, no fake testimonials, no invented features
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

Use the attached layout plan as the ruleset.
Use the supplied screenshot faithfully.

Required copy:
Headline: [HEADLINE]
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
- vary the layout from adjacent slides
- keep decorative elements behind or around the product
- make the background and motifs reinforce the slide message
- compose for a later center-crop to the final App Store size
- keep all critical text and focal visuals well inside safe margins
- leave sacrificial background space near the edges
- keep the screenshot or product visual as the main focus
- avoid flat billboard layouts
- use supporting imagery only when it clearly matches the product category and message
- no fabricated claims
```

## 3. Value Slide Prompt

Use this when there is no screenshot.

```text
Create a premium App Store value slide using the first attached image as the campaign style reference.

This slide has no app screenshot. Build a typography-led brand/value composition in the same campaign family.

Required copy:
Headline: [HEADLINE]
Support: [SUPPORT]

Core message:
[MESSAGE]

Layout direction:
[LAYOUT]

Hard rules:
- do not fabricate a fake app screen
- use 2 to 3 meaningful premium panels or motifs to sell the claims
- avoid generic AI imagery, robots, and cloud clichés
- keep typography readable at thumbnail size
- keep the composition advertisement-first
- make the visual motifs directly reinforce the claims instead of acting as filler
- compose for a later center-crop to the final App Store size
- keep all critical text and focal visuals well inside safe margins
- leave sacrificial background space near the edges
- avoid empty, lifeless backgrounds
```
