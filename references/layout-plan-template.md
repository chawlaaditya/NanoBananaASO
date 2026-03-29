# Layout Plan Template

Use this file as the starting point for the campaign plan you write before image generation.

```md
# [App Name] Nano Banana Layout Plan

## Summary

Create a [N]-slide iPhone App Store campaign from the provided screenshots.

Generation path:
- [Nano Banana / Gemini / other]

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

## Consistency Spine

- typography DNA: [display feel + support feel]
- background language: [what all slides share]
- panel treatment: [glass / flat / carded / minimal]
- device treatment: [front-facing / angled / shadow style]
- accent behavior: [muted / bright / minimal / editorial]
- negative space philosophy: [dense / airy / centered / asymmetric]
- supporting imagery language: [people / places / objects / contextual scenes]
- follow-up anchor source: [normalized slide 1 export path]

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

### Layout rules
- one slide, one idea
- adjacent slides must not reuse the same placement
- headline readable in about one second
- every decorative element must reinforce the slide’s message
- all critical content must survive the final normalized crop

## Slide Specs

### Slide 1
- screenshot: `[file]`
- headline: `[headline]`
- support: `[support]`
- chips:
  - `[chip]`
  - `[chip]`
- purpose:
  - [what this slide sells]
- layout:
  - [composition notes]

### Slide 2
- screenshot: `[file]`
- headline: `[headline]`
- support: `[support]`
- purpose:
  - [what this slide sells]
- layout:
  - [composition notes]

[Repeat for all slides]

### Optional Value Slide
- screenshot: none
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
2. Review and revise slide 1 if needed.
3. Save the raw slide 1 output to `native/`.
4. Normalize slide 1 into `export-<width>x<height>/`.
5. Generate slides 2 to N using the normalized slide 1 export as the style reference.
6. State the chosen image tool in the prompt log or generation notes.
7. Normalize all exports.
8. Build a contact sheet.
```
