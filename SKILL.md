---
name: nano-banana-app-store-campaign
description: "Build premium, consistent App Store screenshot campaigns with Nano Banana. Use when Codex needs to analyze an app codebase for brand, style, and claims, decide which screens should be captured, direct the user to take specific screenshots, turn those screenshots into advertisement-first App Store slides, keep a consistent style anchor across the set, and normalize the final exports to App Store portrait sizes."
---

# Nano Banana App Store Campaign

Build App Store screenshots as ads, not tutorials.

Copy comes before layout. Narrative comes before decoration.
The slide should explain itself visually first.
The text should sharpen the message, not do all the work.

Use this skill when the user wants a screenshot campaign that:
- starts from the actual app codebase and real screenshots
- needs a consistent visual system across all slides
- uses Nano Banana for the ad treatment
- needs deterministic resizing and contact-sheet packaging

Use Nano Banana only in this skill.
Do not switch to other image models.
Do not silently fall back to Flash or any lower-quality image path.

## Workflow

### 0. Confirm Nano Banana credentials

Before planning prompts or generating any slides, confirm that Nano Banana can actually run in the current environment.

Default behavior:
- use `Nano Banana`
- first check whether `GEMINI_API_KEY` is set
- if not, check whether `GOOGLE_API_KEY` is set
- if neither key is available, stop and ask the user for the Gemini API key before generation

Do not treat a missing key as permission to use another image model.

In plans, notes, and prompt logs, state the chosen path explicitly:
- `Nano Banana`

When credential discovery matters, record it like this:
- `Nano Banana credential source: GEMINI_API_KEY`
- or `Nano Banana credential source: GOOGLE_API_KEY`

Do not leave the tool or credential source ambiguous.

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
- plan the set as a mix of slide archetypes, not one repeated template
- use the requested slide count to choose the best-fitting slots instead of blindly filling every slot
- vary layouts across slides and do not repeat the same template structure
- adjacent slides must not reuse the same phone placement
- include 1 to 2 contrast slides with an inverted or clearly darker/lighter background for visual rhythm
- copy must be readable at thumbnail size
- decorative elements must support the message, never block the UI
- the screenshot should remain the main focal point on screenshot-based slides
- prioritize visual explanation over textual explanation
- aim for a clean balance of text and visual, but when forced to choose, strengthen the visual before adding more copy
- avoid billboard-only compositions that feel like text pasted over a screenshot
- allow 1 to 2 deliberately ad-led slides where typography or contextual imagery carries more of the weight than the screenshot
- integrate relevant supporting imagery such as people, places, objects, surfaces, or contextual scenes that are consistent with the app category
- make the set eye-catching and vibrant without becoming noisy or generic

Use these slide archetypes intentionally. Most good sets mix at least 3 of them:

| Archetype | What it is for | Typical use |
| --- | --- | --- |
| `Typography-led hero` | Large bold type with minimal product framing | slide 1, trust slide, or a value slide |
| `Hybrid ad` | Screenshot plus strong contextual imagery, stickers, badges, paths, or objects | differentiator and outcome slides |
| `Product proof` | Screenshot-forward slide with restrained supporting fragments | core feature and proof slides |
| `Contextual/lifestyle` | Real-world scene, person, mascot, place, or object that makes the benefit feel alive | emotional differentiator or category fit |
| `Brand/value` | No fake screenshot; typography, iconography, objects, or value panels only | ownership, privacy, rewards, pricing, trust |

Archetype rules:
- do not make every slide a product-proof slide
- do not make every slide a text billboard either
- at least one slide should feel like a bold ad first, not just a dressed-up screenshot
- if the app category supports it, include at least one slide with contextual imagery that sells the lifestyle or setting around the app
- when using contextual imagery, tie it directly to the message: travel places, routes, food, trainers, coins, certificates, characters, rooms, desks, or objects that the user immediately understands
- allow one slide to minimize or even omit the phone when the message is stronger as a pure value ad

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

Treat copy as a precision tool, not as the whole slide.
The visual should communicate the feature, mood, or outcome first.
The text should make that meaning faster and clearer, not replace the visual explanation.

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

Render-safe copy rule:
- use `<br />` only in planning documents, layout plans, and review notes
- when writing the actual image-generation prompt, convert planned line breaks into explicit multi-line copy blocks such as:
  - `Headline (2 lines):`
  - `Line 1`
  - `Line 2`
- explicitly tell the image model not to render literal `<br />` characters in the final image
- do not assume Nano Banana will interpret HTML-style line break tokens correctly

Use these headline modes:

| Type | What it does | Example |
| --- | --- | --- |
| Paint a moment | Helps the viewer imagine using the app | `Check your coffee<br />without opening the app.` |
| State an outcome | Sells the end state | `A home for every<br />coffee you buy.` |
| Kill a pain | Names and destroys the problem | `Never waste<br />a great bag.` |

Rewrite weak copy before layout generation. Prefer the user's benefit, not the UI inventory.
Do not describe features first. Lead with the life change, then let the feature support it.
If a slide needs too much text to make sense, fix the visual concept before writing more copy.

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
6. Convert approved `<br />` planning copy into render-safe prompt copy with explicit line blocks.
7. Lock the approved headline set before building final layouts.

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
- the slide-archetype plan for the whole set
- phone placement variety
- layout variation strategy
- contrast-slide plan
- background treatment
- differentiator treatment
- export target

Do not skip this step. The plan is what prevents style drift.

Before generation, also lock a visual-rhythm plan:
- which slides are typography-led versus screenshot-led
- which slide gets the boldest headline treatment
- which slide uses the richest supporting imagery
- which slide is the cleanest proof slide
- where the set intentionally changes from light to dark, flat to dimensional, or calm to energetic

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
- if the campaign would open stronger with a typography-led or hybrid-ad slide, let the anchor establish that bolder direction instead of defaulting to a centered phone
- treat slide 1 as a deliberate systems test, not just a pretty first draft
- treat the anchor as the formal definition of:
  - typography
  - background language
  - panel treatment
  - device treatment
  - accent behavior
  - overall visual family

Use slide 1 to test the failure-prone details early:
- crop safety after normalization
- headline font family, weight, and line breaks
- support-line size and density
- chip or badge scale
- CTA cues, arrows, toggles, or buttons if used
- phone scale and dominance
- how much supporting imagery is too much
- whether the slide still reads instantly at thumbnail size

Do not aim only for “good enough.”
Aim to perfect the anchor until it gives you a trustworthy system for the rest of the campaign.

If there is no stronger app-specific direction, use the proven portrait recipe from [references/visual-recipe.md](references/visual-recipe.md) as the default composition system.

Do not continue to slides 2 to N until the anchor is either:
- explicitly approved by the user, or
- clearly strong enough on internal review to serve as the campaign family reference

Then use the approved slide 1 as the primary style reference for the rest of the campaign.

This is the key consistency trick:
- scaffold with the image model
- then use that scaffolded slide as the family reference for the remaining slides
- use the normalized export of slide 1 as the follow-up style reference, not an arbitrary raw output

After revising slide 1, explicitly record what you learned from fixing it:
- what crop-safe spacing actually worked
- which font treatment survived normalization best
- which chip, CTA, or panel sizes stayed readable
- which visual motifs were too busy and were removed
- which text density was acceptable
- which composition rules should now be enforced for every later slide

Write those anchor findings into the layout plan or prompt log.
Use them as rules for slides 2 to N so later slides inherit a validated system instead of re-learning the same lesson.

State `Nano Banana` explicitly in the layout plan and prompt log.
If available, also record whether the credential came from `GEMINI_API_KEY` or `GOOGLE_API_KEY`.

### 6. Generate the rest of the campaign

Use the style anchor plus each target screenshot to generate slides 2 to N.

Follow these rules:
- preserve the real app UI
- do not redesign the product
- use enlarged UI fragments only from the same screenshot
- keep the campaign in the same family
- alternate between cleaner proof slides and richer ad slides when the story benefits from it
- vary phone placement across adjacent slides
- vary the overall composition rhythm across the set
- vary the amount of screenshot dominance across the set
- keep typography large and strong
- keep claims short and specific
- keep each slide focused on a single approved idea
- let the visual carry the explanation and let the text sharpen the claim
- make each background or decorative motif support the slide’s message
- keep the screenshot or core product visual as the main focus
- add supporting imagery only when it strengthens the message and the app category
- avoid dead empty backgrounds and avoid text-only billboard compositions
- explicitly lock the headline font family or type style to the anchor on follow-up slides
- do not let follow-up slides drift into serif headlines or a different typography voice unless the anchor already uses that
- avoid oversized white text cards or giant copy panels unless they are already part of the anchor’s design language

Use tasteful variation signals pulled from strong App Store campaigns:
- bold color-field slides with oversized headline type
- a few sticker, badge, path, orbit, ribbon, or glow motifs when they reinforce the claim
- clean footer bands or compact value bars when they add structure
- occasional cutout photography, mascots, objects, or scene fragments that make the app feel lived-in
- one restrained proof slide after a louder ad slide so the set can breathe

Do not confuse consistency with sameness. The set should feel art-directed, not templated.

For every follow-up prompt, explicitly restate the style DNA from the anchor:
- typography scale
- background language
- panel treatment
- device treatment
- accent behavior
- the crop-safe findings learned from anchor revisions
- the font, CTA, chip, and spacing decisions that proved reliable after normalization

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

Use the actual normalization math, not intuition:
- final iPhone portrait target ratio is `1320 / 2868 = 0.4603`
- the normalizer center-crops first, then resizes
- if the generated source is wider than `0.4603`, the surviving width is `src_h * 0.4603`
- horizontal trim on each side is `(src_w - src_h * 0.4603) / 2`
- if the generated source is narrower than `0.4603`, the surviving height is `src_w / 0.4603`
- vertical trim on top and bottom is `(src_h - src_w / 0.4603) / 2`

Turn that into a first-pass safe box before you prompt:
- for wide portrait sources, the safe left edge is `horizontal_trim + 0.08 * surviving_width`
- for wide portrait sources, the safe right edge is `src_w - safe_left_edge`
- for wide portrait sources, the safe top edge is `0.06 * src_h`
- for wide portrait sources, the safe bottom edge is `0.92 * src_h`
- for narrow portrait sources, mirror the same logic vertically with the top and bottom trim

Common first-pass examples:
- for a `1024x1536` source, only about `707px` of width survives; about `158px` is cut off on each side; safer content zone is roughly `x=216..808`, `y=92..1413`
- for a `1242x2208` source, only about `1017px` of width survives; about `113px` is cut off on each side; safer content zone is roughly `x=194..1048`, `y=132..2031`

When the exact first-pass source size is still unknown:
- assume a common portrait source wider than the final ratio
- act as if roughly `10 to 16 percent` of the source width may disappear from each side
- keep all must-read copy, phones, faces, chips, arrows, and proof panels inside the central `58 to 70 percent` of the source width on first pass
- this conservative first-pass rule is better than asking the model to “just leave some margin”

For text-heavy or proof-heavy slides, use stronger defaults:
- keep headline and support copy inside roughly the middle 70 percent of the canvas
- do not anchor important copy flush to the far left or far right edges
- keep chips and side claims fully inside the same safe zone
- shorten the copy before pushing type closer to the crop boundary

When writing prompts, explicitly tell Nano Banana:
- compose for a later center-crop to the final App Store size
- keep all critical text and key visuals well within safe margins
- leave sacrificial background space near the edges for normalization
- assume the first-pass portrait source may lose around 10 to 16 percent of width on each side during center-crop
- keep the entire must-read composition inside the central safe box rather than the full source canvas
- do not place headlines, chips, CTA cues, or the phone silhouette near the original left or right edges

If a slide looks good only before cropping, it is not done.

### 6.6. Run a crop-verification pass before final signoff

After generating the anchor and after generating the full set:
- normalize the current outputs
- inspect the normalized exports visually, not just the native renders
- actually look at the images one by one
- check that no headline, support line, screenshot edge, chip, or visual panel has been cropped awkwardly
- check that the phone still feels intentional after cropping
- check that no breathing room has collapsed around the headline or focal object
- use the contact sheet as a quick overview, then still inspect the individual normalized slides at full size

If the normalized export reveals any crop problem:
- revise the source prompt
- create more edge breathing room
- regenerate that slide
- normalize it again
- inspect the new normalized image again
- repeat until the crop is clearly working

Do not mark a slide as done just because the raw render looked good.
Treat this as a required visual verification loop, not an optional polish step.

### 7. Handle brand-value slides separately

If the set needs a slide for pricing, offline use, privacy, on-device AI, or ownership:
- do not fake an app screen
- do not use random abstract imagery with no message
- build a typography-led value slide
- use 2 to 3 meaningful premium panels or motifs that communicate the claims
- consider using the app icon, mascot, category objects, certificates, rewards, routes, coins, or other concrete symbols instead of another phone
- let one of these slides function as a true brand ad with large type and minimal UI if that improves the campaign rhythm

Good examples:
- ownership card or purchase metaphor for one-time payment
- signal-off or local-mode motif for offline use
- private-device / local model motif for on-device AI
- clear visual CTA cues such as a meaningful button, badge, chip, arrow, toggle, or panel that helps the slide read faster without turning into a text block

Avoid:
- robots
- glowing brains
- cloud clichés
- dense spec-sheet copy
- using extra explanatory text when a clearer visual would do the job

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
- review the normalized images themselves before batch signoff
- if the crop harms readability or layout, revise the source generation prompt and regenerate
- after every regeneration, normalize again and inspect the new normalized image
- keep iterating until the normalized export is working, not just the source render
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
- any slide whose normalized export still looks even slightly crop-broken after the first pass

## Prompting Guidelines

Use imperative prompt language with hard rules.

For this skill:
- say `Nano Banana` explicitly in the plan or prompt log
- describe slide 1 as the Nano Banana style anchor
- describe later slides as consistent variants derived from that anchor
- check `GEMINI_API_KEY` first, then `GOOGLE_API_KEY`, before generation
- if neither key exists, ask the user for the Gemini API key and pause generation until it is available
- do not switch to another image model because of missing credentials

Always include:
- preserve the screenshot faithfully
- do not redesign the app UI
- keep typography readable at thumbnail size
- keep headline line breaks intentional with `<br />` when needed
- keep the slide advertisement-first
- keep each slide focused on one idea only
- make the visual do the explaining first and let the copy make it faster to understand
- keep the slide in the same family as the style anchor
- make the visual language reinforce the slide’s message
- when using planned `<br />` copy, convert it into explicit prompt lines rather than pasting the token literally
- explicitly say `do not render literal <br /> characters`
- explicitly say `use the same headline font family / type style as the anchor`

When generating a value slide with no screenshot, say so explicitly.

## Failure Modes

Actively avoid these common bad outcomes:
- leaving the image-generation tool ambiguous when the user asked for Nano Banana
- skipping the Gemini credential check before attempting Nano Banana generation
- continuing without `GEMINI_API_KEY` or `GOOGLE_API_KEY` and pretending generation is unblocked
- switching to another image model because the Gemini key is missing
- skipping the copy-first phase or generating layouts before headlines are locked
- writing screenshot text like feature documentation instead of an ad argument
- pasting `<br />` directly into an image-generation prompt and getting the token rendered in the output
- saving only one set of outputs and skipping the native/export split
- using a raw or differently sized anchor image as the follow-up family reference
- trusting the model’s returned size instead of normalizing
- placing text or focal visuals too close to the edges so normalization crops them out
- checking the raw render but not the normalized image
- running one crop pass, noticing a problem, and not looping until it is fixed
- treating the slide like a text billboard instead of a rich product advertisement
- explaining the feature mostly with text when the visual could have shown it more clearly
- adding random imagery that is not clearly connected to the app category or message
- using the same vague background treatment on multiple slides
- using the same screenshot-plus-headline layout on nearly every slide
- making every slide equally screenshot-heavy so the campaign has no rhythm
- refusing to use bold type-led or value-led ad slides even when they would sell the message better
- generating all slides before the style anchor is locked
- treating the layout plan as optional
- reusing the same slide template structure across the set
- repeating the same phone placement on adjacent slides
- stuffing the slide with feature copy instead of one message
- writing headlines that join two ideas with “and”
- using feature lists as headlines
- using vague or buzzword-heavy headlines that do not sell a concrete user benefit
- building a set whose screenshots can be shuffled into any order without changing meaning
- letting text-heavy slides sit too close to the crop boundary because the raw render looked safe
- allowing follow-up slides to drift into a different font family or giant text-card treatment than the anchor
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
- [references/gemini-image-api.md](references/gemini-image-api.md): Nano Banana credential notes for Gemini-backed environments

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
- the set mixes clean proof slides with at least one more expressive ad-led slide when appropriate
- the set includes visual rhythm instead of one repeated template
- claims are grounded in the app
- the set feels visually consistent
- exports are normalized to one App Store size
