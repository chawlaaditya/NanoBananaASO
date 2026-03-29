---
name: nano-banana-app-store-campaign
description: "Build premium, consistent App Store screenshot campaigns with Nano Banana or Gemini image models. Use when Codex needs to analyze an app codebase for brand, style, and claims, decide which screens should be captured, direct the user to take specific screenshots, turn those screenshots into advertisement-first App Store slides, keep a consistent style anchor across the set, and normalize the final exports to App Store portrait sizes."
---

# Nano Banana App Store Campaign

Build App Store screenshots as ads, not tutorials.

Copy comes before layout. Narrative comes before decoration.
The overlay text is usually the argument. The UI is supporting evidence.

Use this skill when the user wants a screenshot campaign that:
- starts from the actual app codebase and real screenshots
- needs a consistent visual system across all slides
- uses Nano Banana or Gemini image generation for the ad treatment
- needs deterministic resizing and contact-sheet packaging

Prefer Nano Banana by default. If the user asked for Nano Banana, keep that explicit throughout the workflow instead of treating the image model as implied.

When using Gemini instead of Nano Banana, prefer the Pro Image Preview model path and do not silently drop to Flash for primary generation.

## Workflow

### 0. Confirm the image-generation path

Before planning prompts or generating any slides, confirm which image-generation path will be used.

Default behavior:
- prefer Nano Banana
- if the user already said “use Nano Banana,” treat that as locked
- if the user specified Gemini or provided a Gemini API key, use the Gemini path

For the Gemini path:
- prefer the Pro Image Preview model
- do not default to Flash for final campaign generation
- only use a Flash model if the user explicitly accepts lower-quality fallback behavior

If the path is unclear, ask one short question and resolve it before generation.

In plans, notes, and prompt logs, state the chosen path explicitly:
- `Nano Banana`
- `Gemini`
- or another specific model path

Do not leave the image-generation tool ambiguous.

### 1. Inspect the app before designing anything

Read the codebase and assets first. Derive:
- fonts and typography cues
- color palette and overall mood
- product claims that are actually supported
- differentiators worth selling
- the strongest user benefit
- the clearest user pain the app resolves
- the before-and-after shift the user should feel

Do not invent claims. Ground them in code, copy, settings, onboarding, pricing UI, or platform integrations.

Check for:
- fonts in asset or font folders
- color tokens in UI code
- onboarding / marketing copy
- pricing / purchase language
- offline, privacy, local AI, wearable, or platform integration claims

If the app is iOS-first, inspect the real iOS views or assets instead of guessing.

### 2. Decide the campaign story

Translate the app into an ad narrative that adapts to the user's requested slide count.

Do not force a fixed 5 to 7 slide story if the user asked for fewer or more. Use only the slots that help.

Use this screenshot framework as the default narrative arc:

| Slot | Purpose | Notes |
| --- | --- | --- |
| `#1` | Hero / Main Benefit | App icon + tagline + home screen when possible. This is the only slide many people will see. |
| `#2` | Differentiator | Show what makes the app meaningfully different from competitors. |
| `#3` | Ecosystem | Widgets, extensions, watch, desktop, or other beyond-the-core surfaces. Skip if not real. |
| `#4+` | Core Features | One feature per slide, ordered by importance. |
| `2nd to last` | Trust Signal | Identity, craft, or credibility. Example: “made for people who [X].” |
| `Last` | More Features | Pills or short modules for extras and coming soon. Skip if the app does not have enough honest depth. |

Also use this high-converting sequence logic when planning the slide order:
- screenshot 1 names the pain, desire, or tension
- screenshot 2 states the shift or outcome
- screenshot 3 shows proof with something concrete when available
- screenshots 4 and onward deliver the one or two features that make the promise believable

Blend this with the slot system instead of treating them as competing frameworks. For example:
- hero can name the pain or promise the outcome
- differentiator can serve as the shift
- an early core-feature or trust slide can serve as proof
- later feature slides explain delivery

Core story rules:
- each slide sells exactly one idea
- never put two features on one slide
- the first slide sells the strongest user benefit, not the broadest overview
- the sequence should feel intentional from slide to slide, not interchangeable
- use the requested slide count to choose the best-fitting slots instead of blindly filling every slot
- vary layouts across slides and do not repeat the same template structure
- adjacent slides must not reuse the same phone placement
- include 1 to 2 contrast slides with an inverted or clearly darker/lighter background for visual rhythm
- copy must be readable at thumbnail size
- decorative elements must support the message, never block the UI
- the screenshot should remain the main focal point on screenshot-based slides
- avoid billboard-only compositions that feel like text pasted over a screenshot
- integrate relevant supporting imagery such as people, places, objects, surfaces, or contextual scenes that are consistent with the app category
- make the set eye-catching and vibrant without becoming noisy or generic

When compressing the story into fewer slides:
- keep `#1` hero
- prefer one differentiator before additional feature slides
- drop ecosystem or “more features” before dropping the main differentiator

When expanding the story into more slides:
- add more core-feature slides before adding filler
- keep the trust-signal slide near the end
- use the final “more features” slide only if it adds honest breadth without weakening the set

### 2.5. Write copy first

Do not build layouts before the headlines are strong enough.

Get headline approval before final layout generation. Bad copy ruins good design.

Assume screenshot performance is driven more by the text overlay than the UI arrangement. Treat copy as the highest-leverage design variable.

For each planned slide:
- write 3 headline options before layout work
- use one option from each of these approaches:
  - paint a moment
  - state an outcome
  - kill a pain
- present the options to the user with one short reason each when approval is part of the workflow
- if user interaction is not possible, choose the strongest option internally and state why in the plan or notes

Iron rules for screenshot copy:
- one idea per headline
- never join two claims with “and”
- use short, common words whenever possible
- keep copy readable at thumbnail size
- if you cannot state the core change in 8 words or fewer, simplify until you can
- aim for 3 to 5 words per line
- use intentional line breaks with `<br />`
- avoid jargon unless the domain truly requires it
- avoid feature-list headlines
- avoid compound clauses
- avoid vague aspirational lines that say little
- avoid marketing buzzwords unless the claim is concrete and real

Use these headline modes:

| Type | What it does | Example |
| --- | --- | --- |
| Paint a moment | Helps the viewer imagine using the app | `Check your coffee<br />without opening the app.` |
| State an outcome | Sells the end state | `A home for every<br />coffee you buy.` |
| Kill a pain | Names and destroys the problem | `Never waste<br />a great bag.` |

Rewrite weak copy before layout generation. Prefer the user's benefit, not the UI inventory.
Do not describe features first. Lead with the life change, then let the feature support it.

Bad-to-better rewrite patterns:

| Weak | Better | Why it wins |
| --- | --- | --- |
| `Track habits and stay motivated` | `Keep your streak alive` | one idea, faster to parse |
| `Organize tasks with AI summaries and smart sorting` | `Turn notes into next steps` | outcome-first, less jargon |
| `Save recipes with tags, filters, and favorites` | `Find dinner fast` | sells the benefit, not the feature list |
| `Manage budgets and never miss payments` | `See where money goes` | cleaner promise, no dual claim |
| `AI-powered wellness support` | `Feel calmer tonight` | concrete emotional outcome |

Copy process:
1. Write 3 options per slide.
2. Read each at arm's length. If it cannot be parsed in about 1 second, rewrite it.
3. Check line length. If a line is too dense, add or change `<br />`.
4. Cover the UI with your hand and read only the text. If the sequence reads like a feature catalog instead of a story, rewrite it.
5. Confirm each slide still sells only one idea.
6. Lock the approved headline set before building final layouts.

### 3. Tell the user exactly which screenshots to capture

If screenshots are not already provided, create a concrete capture list based on the approved story slots and headlines.

Write a short ordered list with:
- filename
- exact screen to capture
- what should be visible on the screen
- which slide idea it supports

Keep it one raw screenshot per screenshot-based slide.

Do not request screenshots for slides that should be typography-led value slides.

Example capture list shape:
- `01-main-value-screen.png`: the screen that best shows the app’s primary benefit, with one clear hero section
- `02-structure-screen.png`: a screen that shows organization, workflow, or the next step clearly
- `03-action-screen.png`: a screen that shows the user about to do the core action, with the main CTA visible

### 4. Lock the layout plan before generation

Before generating any final slide, write a layout-plan markdown file in the project or output directory.

Use [references/layout-plan-template.md](references/layout-plan-template.md) as the starting structure.
If the user needs a strong default starting point, also read [references/visual-recipe.md](references/visual-recipe.md).

The layout plan is the source of truth for:
- generation path
- campaign positioning
- story spine
- story slots used and which ones were intentionally skipped
- the pain -> shift -> proof -> delivery logic used across the sequence
- consistency spine
- crop-safe composition rules
- slide order
- approved headline/support copy
- the three headline options considered for each slide when useful
- phone placement variety
- layout variation strategy
- contrast-slide plan
- background treatment
- differentiator treatment
- export target

Do not skip this step. The plan is what prevents style drift.

### 5. Generate a style anchor first

Do not batch-generate the whole set immediately.

Generate slide 1 first as the style anchor:
- use the real screenshot faithfully
- use the locked layout plan
- create a premium ad treatment around the screenshot
- keep the app UI recognizable
- make the hero slide sell one clear main benefit
- make the text do the selling and the UI do the proving
- define the family’s typography, panel treatment, device lighting, accent behavior, and negative-space philosophy
- define the supporting imagery language for the whole set: people, places, objects, or contextual scenes that match the app
- keep the screenshot as the hero while the supporting imagery makes the slide feel richer and more alive

If there is no stronger app-specific direction, use the proven portrait recipe from [references/visual-recipe.md](references/visual-recipe.md) as the default composition system.

Do not continue to slides 2 to N until the anchor is either:
- explicitly approved by the user, or
- clearly strong enough on internal review to serve as the campaign family reference

Then use the approved slide 1 as the primary style reference for the rest of the campaign.

This is the key consistency trick:
- scaffold with the image model
- then use that scaffolded slide as the family reference for the remaining slides
- use the normalized export of slide 1 as the follow-up style reference, not an arbitrary raw output

If Nano Banana is the chosen path, state that explicitly in the layout plan and prompt log.

### 6. Generate the rest of the campaign

Use the style anchor plus each target screenshot to generate slides 2 to N.

Follow these rules:
- preserve the real app UI
- do not redesign the product
- use enlarged UI fragments only from the same screenshot
- keep the campaign in the same family
- vary phone placement across adjacent slides
- vary the overall composition rhythm across the set
- keep typography large and strong
- keep claims short and specific
- keep each slide focused on a single approved idea
- let the text lead and the interface support the claim
- make each background or decorative motif support the slide’s message
- keep the screenshot or core product visual as the main focus
- add supporting imagery only when it strengthens the message and the app category
- avoid dead empty backgrounds and avoid text-only billboard compositions

For every follow-up prompt, explicitly restate the style DNA from the anchor:
- typography scale
- background language
- panel treatment
- device treatment
- accent behavior

Follow this output pattern exactly:
- save raw model outputs to `native/`
- normalize every slide into `export-<width>x<height>/`
- keep a `prompt-log.md`
- build a `contact-sheet.png` from the normalized exports

This is the reference working pattern from the good `campaign-v3` run. Reuse it instead of inventing a looser export flow.

Use [references/prompt-patterns.md](references/prompt-patterns.md) for prompt structure.

### 6.5. Design for the final crop, not the raw output

The generated source image must already anticipate the final App Store crop.

Do not place critical content flush to the edges and hope normalization keeps it safe.

Treat normalization as a final packaging step, not as a layout step.

Keep all critical elements inside a crop-safe zone:
- headline and support copy
- chips and value panels
- phone or primary focal object
- any must-read iconography or callouts

Use these default crop-safe rules for portrait slides:
- side safe margin: at least 8 percent of canvas width
- top safe margin: at least 6 percent of canvas height
- bottom safe margin: at least 8 percent of canvas height
- never let key copy or focal objects touch the outer frame

When writing prompts, explicitly tell Nano Banana or Gemini:
- compose for a later center-crop to the final App Store size
- keep all critical text and key visuals well within safe margins
- leave sacrificial background space near the edges for normalization

If a slide looks good only before cropping, it is not done.

### 6.6. Run a crop-verification pass before final signoff

After generating the anchor and after generating the full set:
- normalize the current outputs
- inspect the normalized exports, not just the native renders
- check that no headline, support line, screenshot edge, chip, or visual panel has been cropped awkwardly

If the normalized export reveals any crop problem:
- revise the source prompt
- create more edge breathing room
- regenerate that slide

Treat this as a required second pass, not an optional polish step.

### 7. Handle brand-value slides separately

If the set needs a slide for pricing, offline use, privacy, on-device AI, or ownership:
- do not fake an app screen
- do not use random abstract imagery with no message
- build a typography-led value slide
- use 2 to 3 meaningful premium panels or motifs that communicate the claims

Good examples:
- ownership card or purchase metaphor for one-time payment
- signal-off or local-mode motif for offline use
- private-device / local model motif for on-device AI

Avoid:
- robots
- glowing brains
- cloud clichés
- dense spec-sheet copy

### 8. Normalize exports

Always normalize final exports to a target App Store size after generation.

Default iPhone portrait target:
- `1320x2868`

If the user requests another Apple slot, use that exact target instead.

Use the bundled scripts:
- `scripts/normalize_app_store_exports.py`
- `scripts/build_contact_sheet.py`

Normalize every slide to the same target size. Do not stretch images. Crop to the target aspect ratio first, then resize.
Never trust the image model to return the final App Store size directly.

But also:
- do not let normalization remove essential content
- review at least one normalized export before batch signoff
- if the crop harms readability or layout, revise the source generation prompt and regenerate
- run a second crop-verification pass on the full normalized set before marking it final

Preferred folder structure:

```text
output/
  nano-banana-layout-plan.md
  prompt-log.md
  native/
    slide-01-...
    slide-02-...
  export-1320x2868/
    slide-01-...
    slide-02-...
  contact-sheet.png
```

### 9. Package review outputs

At the end, provide:
- the layout plan file
- the final export folder
- the prompt log if one was used
- a contact sheet for review

### 10. Run a consistency QA pass

Before declaring the set done, review it against [references/quality-gates.md](references/quality-gates.md).

If any of these failures show up, revise before presenting the work as complete:
- random backgrounds that do not reinforce the message
- plain screenshot-in-a-mockup compositions
- tiny or overly verbose copy
- adjacent slides with the same placement rhythm
- value slides that feel like generic AI art instead of product claims
- slides that do not feel like one coherent campaign
- screenshot text that reads like patch notes or feature labels
- a sequence that works in any order because it tells no real story

## Prompting Guidelines

Use imperative prompt language with hard rules.

If Nano Banana is the chosen path:
- say “Nano Banana” explicitly in the plan or prompt log
- describe slide 1 as the Nano Banana style anchor
- describe later slides as consistent variants derived from that anchor

If Gemini is the chosen path:
- use the Pro Image Preview model path
- state the model explicitly in the prompt log or generation notes
- do not silently substitute Flash for the main campaign

Always include:
- preserve the screenshot faithfully
- do not redesign the app UI
- keep typography readable at thumbnail size
- keep headline line breaks intentional with `<br />` when needed
- keep the slide advertisement-first
- keep each slide focused on one idea only
- make the copy the argument and the UI the visual proof
- keep the slide in the same family as the style anchor
- make the visual language reinforce the slide’s message

When generating a value slide with no screenshot, say so explicitly.

## Failure Modes

Actively avoid these common bad outcomes:
- leaving the image-generation tool ambiguous when the user asked for Nano Banana
- using a Flash image model as the default Gemini path
- skipping the copy-first phase or generating layouts before headlines are locked
- writing screenshot text like feature documentation instead of an ad argument
- saving only one set of outputs and skipping the native/export split
- using a raw or differently sized anchor image as the follow-up family reference
- trusting the model’s returned size instead of normalizing
- placing text or focal visuals too close to the edges so normalization crops them out
- treating the slide like a text billboard instead of a rich product advertisement
- adding random imagery that is not clearly connected to the app category or message
- using the same vague background treatment on multiple slides
- generating all slides before the style anchor is locked
- treating the layout plan as optional
- reusing the same slide template structure across the set
- repeating the same phone placement on adjacent slides
- stuffing the slide with feature copy instead of one message
- writing headlines that join two ideas with “and”
- using feature lists as headlines
- using vague or buzzword-heavy headlines that do not sell a concrete user benefit
- building a set whose screenshots can be shuffled into any order without changing meaning
- letting decorative panels repeat the same text with no added meaning
- creating “AI” slides with cliché imagery rather than product-grounded value panels

## Resources

### references/

Read these only when needed:
- [references/layout-plan-template.md](references/layout-plan-template.md): template for the campaign plan file
- [references/prompt-patterns.md](references/prompt-patterns.md): reusable prompt structures for anchor slides, follow-up slides, and value slides
- [references/quality-gates.md](references/quality-gates.md): review checklist for story and visual consistency
- [references/export-pattern.md](references/export-pattern.md): exact folder and normalization pattern from the working v3 campaign
- [references/visual-recipe.md](references/visual-recipe.md): the specific visual decisions that worked well in the strong v3 set
- [references/gemini-image-api.md](references/gemini-image-api.md): Gemini Pro Image Preview guidance and calling pattern

### scripts/

Use these deterministic helpers after generation:
- `scripts/normalize_app_store_exports.py`: crop and resize generated slides to a consistent App Store size
- `scripts/build_contact_sheet.py`: assemble a review sheet from the normalized exports

## Output Checklist

Before finishing, confirm:
- the campaign is ad-first, not tutorial-first
- every slide sells one idea
- headlines were written and locked before final layouts
- the text alone tells a coherent story when the UI is covered
- adjacent slides vary in placement
- the set includes visual rhythm instead of one repeated template
- claims are grounded in the app
- the set feels visually consistent
- exports are normalized to one App Store size
