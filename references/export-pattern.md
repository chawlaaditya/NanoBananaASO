# Export Pattern

Use this exact output pattern. It is based on the working `campaign-v3` run that produced the good, properly sized App Store set.

## Folder structure

```text
output/
  nano-banana-layout-plan.md
  prompt-log.md
  native/
    slide-01-...
    slide-02-...
    ...
  export-1320x2868/
    slide-01-...
    slide-02-...
    ...
  contact-sheet.png
```

## Required decisions

- Save raw model outputs to `native/` first.
- Normalize every slide into `export-<width>x<height>/`.
- Keep a `prompt-log.md`.
- Build a `contact-sheet.png` from the normalized exports.
- Use the normalized export of slide 1 as the follow-up style reference.
- Use the fixes learned from slide 1 as follow-up generation rules, not just the image itself.
- Generate source slides with crop-safe margins so normalization does not remove key content.
- Run at least one anchor crop-verification pass and one final full-set crop-verification pass.
- During each crop-verification pass, visually inspect the normalized images themselves and keep regenerating until the crop works.

## Why this matters

This pattern fixes two common failure modes:

1. Weird output sizes
   - Image models often return inconsistent portrait dimensions.
   - The final App Store set must be normalized after generation.

2. Style drift
   - If later slides reference a raw or differently sized image, composition and spacing can drift.
   - Using the normalized slide 1 export as the family reference makes the campaign more stable.
   - Reusing the anchor findings for fonts, spacing, chips, and CTA scale makes the campaign more stable too.

3. Cropped-off copy or focal visuals
   - If the source image uses the full canvas too aggressively, normalization can clip the layout.
   - Design the source image with sacrificial edge space and safe margins from the start.
   - Then inspect the normalized output visually and loop until the export is clean.

4. Flat billboard compositions
   - If the slide relies on text plus a screenshot with no richer visual language, it will feel cheap.
   - Keep the screenshot or product visual as the hero and use category-relevant supporting imagery to add life and energy.

## Recommended target

Default iPhone portrait:
- `1320x2868`

If the user requests another App Store slot, keep the same pattern and change only the target size.

## Minimum deliverables

- `nano-banana-layout-plan.md`
- `prompt-log.md`
- `native/`
- `export-<target-size>/`
- `contact-sheet.png`
