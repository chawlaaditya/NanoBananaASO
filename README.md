# Nano Banana ASO

A Codex skill for building premium, consistent App Store screenshot campaigns with Nano Banana or Gemini image generation.

This skill helps Codex:
- analyze an app codebase for brand, claims, and differentiators
- decide which app screens should be captured
- write a layout plan before image generation
- lock a style anchor for consistency across the set
- generate advertisement-first App Store slides
- normalize exports to App Store-safe sizes
- build a contact sheet for review

## Included

- `SKILL.md`
- `agents/openai.yaml`
- `references/`
- `scripts/normalize_app_store_exports.py`
- `scripts/build_contact_sheet.py`

## What It Optimizes For

- screenshots as ads, not tutorials
- consistent campaign-wide visual language
- screenshot-led compositions with relevant supporting imagery
- crop-safe layouts that survive final App Store normalization
- a `native/` plus `export-<size>/` workflow

## Default Export Pattern

```text
output/
  nano-banana-layout-plan.md
  prompt-log.md
  native/
  export-1320x2868/
  contact-sheet.png
```

## Model Guidance

- Prefer `Nano Banana` when available.
- For Gemini, prefer the `Pro Image Preview` model path for final campaign generation.
- Do not silently fall back to Flash for the main set.

## Install

Copy this repo into your Codex skills directory, or clone it there directly:

```bash
git clone https://github.com/chawlaaditya/NanoBananaASO.git "${CODEX_HOME:-$HOME/.codex}/skills/nano-banana-app-store-campaign"
```

## Use

Example prompt:

```text
Use $nano-banana-app-store-campaign to analyze this app, tell me which screenshots to capture, lock a Nano Banana style anchor, and generate a consistent App Store screenshot campaign.
```
