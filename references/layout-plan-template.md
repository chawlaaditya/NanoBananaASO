# Layout Plan Template

Use this file as the starting point for the campaign plan you write before image generation.

```md
# [App Name] Nano Banana Layout Plan

## Summary

Create a [N]-slide iPhone App Store campaign from the provided screenshots.

Generation path:
- `Nano Banana`
- credential source: [`GEMINI_API_KEY` / `GOOGLE_API_KEY` / ask user]

Campaign positioning:
- [primary product story]
- [secondary story]
- weave in differentiators:
  - [claim 1]
  - [claim 2]
  - [claim 3]

## Story Spine

- slide 1 sells: [strongest outcome]
- slide 2 sells: [next narrative beat]
- slide 3 sells: [next narrative beat]
- slide 4 sells: [next narrative beat]
- slide 5 sells: [next narrative beat]
- slide 6 sells: [next narrative beat]
- optional slide 7 sells: [value / pricing / privacy / ownership]

## Visual Rhythm Plan

- slide 1 archetype: [Typography-led hero / Hybrid ad / Product proof / Contextual-lifestyle / Brand-value]
- slide 2 archetype: [archetype]
- slide 3 archetype: [archetype]
- slide 4 archetype: [archetype]
- slide 5 archetype: [archetype]
- slide 6 archetype: [archetype]
- optional slide 7 archetype: [archetype]
- boldest slide: [which slide and why]
- cleanest proof slide: [which slide and why]
- richest supporting-imagery slide: [which slide and why]
- contrast-slide plan: [where the set deliberately shifts tone]

## Consistency Spine

- typography DNA: [display feel + support feel]
- background language: [what all slides share]
- panel treatment: [glass / flat / carded / minimal]
- device treatment: [front-facing / angled / shadow style]
- accent behavior: [muted / bright / minimal / editorial]
- negative space philosophy: [dense / airy / centered / asymmetric]
- supporting imagery language: [people / places / objects / contextual scenes]
- follow-up anchor source: [normalized slide 1 export path]

## Anchor Findings

- crop-safe spacing that survived normalization: [notes]
- headline font treatment that held up best: [notes]
- support-line density that still read clearly: [notes]
- chip / badge / CTA sizing that worked: [notes]
- motifs or panels removed for being too busy: [notes]
- reusable rules for slides 2 to N: [notes]

## Export Standard

- final export size: `1320x2868`
- portrait only
- normalize all final slides to the same target

## Crop-Safe Rules

- compose the source image for later normalization
- keep all must-read text and focal visuals inside a safe zone
- side safe margin: at least 8 percent of width
- top safe margin: at least 6 percent of height
- bottom safe margin: at least 8 percent of height
- leave sacrificial background space near the edges
- do not rely on normalization to save an edge-heavy composition
- write down the expected first-pass crop math for the source size when known
- if the source is wider than the target ratio, calculate:
  - surviving width = `src_h * 0.4603`
  - trim per side = `(src_w - surviving width) / 2`
  - safer left edge = `trim + 0.08 * surviving width`
  - safer right edge = `src_w - safer left edge`
- if source size is unknown, assume the first pass may lose `10 to 16 percent` of width on each side and compose inside the central safe box

## Shared Visual System

### Mood
- [dark editorial / light premium / bold colorful / etc.]
- [eye-catching but still coherent]

### Typography
- display feel: [font cue]
- support feel: [font cue]
- strong contrast
- large readable type

### Product treatment
- preserve the app UI
- use tasteful UI fragments from the same screenshot
- do not let decorative elements block key UI
- keep the screenshot or product visual as the main focus
- use relevant supporting imagery to enrich the ad instead of relying on text alone
- prefer visual explanation over extra explanatory copy

### Layout rules
- one slide, one idea
- adjacent slides must not reuse the same placement
- mix at least 3 slide archetypes across the set when the count allows
- headline readable in about one second
- the visual should communicate most of the idea before the text does
- every decorative element must reinforce the slide’s message
- all critical content must survive the final normalized crop

## Slide Specs

### Slide 1
- screenshot: `[file]`
- archetype: `[archetype]`
- headline: `[headline]`
- support: `[support]`
- chips:
  - `[chip]`
  - `[chip]`
- purpose:
  - [what this slide sells]
- layout:
  - [composition notes]
  - [supporting imagery / motifs]

### Slide 2
- screenshot: `[file]`
- archetype: `[archetype]`
- headline: `[headline]`
- support: `[support]`
- purpose:
  - [what this slide sells]
- layout:
  - [composition notes]
  - [supporting imagery / motifs]

[Repeat for all slides]

### Optional Value Slide
- screenshot: none
- archetype: `Brand-value`
- headline: `[headline]`
- support: `[support]`
- purpose:
  - [ownership / privacy / no subscription / offline]
- layout:
  - no fake app screen
  - typography-led composition
  - use 2 to 3 visual value panels if needed

## Prompt Rules

- preserve screenshots faithfully
- do not redesign the app UI
- keep typography large and readable
- keep the set in the same campaign family
- no fabricated claims

## Workflow

1. Generate slide 1 first as the style anchor.
2. Stress-test slide 1 for crop, font, CTA, chip, and panel behavior.
3. Review and revise slide 1 until it works as a reliable system.
4. Save the raw slide 1 output to `native/`.
5. Normalize slide 1 into `export-<width>x<height>/`.
6. Write the anchor findings into the plan or prompt log.
7. Generate slides 2 to N using the normalized slide 1 export plus the anchor findings as the style reference.
8. State the chosen image tool in the prompt log or generation notes.
8.5. Record whether the Nano Banana credential came from `GEMINI_API_KEY`, `GOOGLE_API_KEY`, or the user.
9. Normalize all exports.
10. Build a contact sheet.
```
