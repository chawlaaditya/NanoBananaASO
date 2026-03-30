#!/usr/bin/env python3
import base64
import io
import json
import mimetypes
import os
import ssl
import sys
import urllib.request
from pathlib import Path

from PIL import Image

try:
    import certifi
except ImportError:
    certifi = None


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "output" / "social" / "nb-pure"
OUT_DIR.mkdir(parents=True, exist_ok=True)

API_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "gemini-3-pro-image-preview:generateContent"
)


PROMPTS = [
    """
Create a premium social header for an X article about a tool that automates App Store screenshots.

Aspect ratio: ultra-wide 5:2 banner.

Design direction:
- extremely clean
- minimal
- premium
- readable at a glance
- bold but not cluttered
- designed like a polished tech launch poster

Required headline text exactly:
FULLY AUTOMATED
APP STORE
SCREENSHOTS

Optional small supporting line:
Nano Banana Pro skill

Layout:
- large headline on the left half
- 2 or 3 elegant iPhone screenshot campaign cards on the right half
- dark charcoal background with subtle depth
- white typography
- one bright accent color only, vivid green
- plenty of negative space
- strong hierarchy
- no extra text
- no tiny labels
- no logos
- no watermarks
- no fake UI paragraphs
- keep all text safely inside the center 80 percent of the canvas for crop safety

The final image should feel clean, sophisticated, and instantly understandable.
""".strip(),
    """
Design a striking but simple ultra-wide 5:2 editorial banner for an X article.

This image is promoting a Nano Banana Pro workflow that automatically turns app screenshots into App Store marketing creative.

Required headline text exactly:
RAW SHOTS IN.
ADS OUT.

Optional small subline:
App Store creative, automated

Visual composition:
- huge readable white display typography
- one clean dark background with subtle lighting
- right side shows premium stacked app screenshot cards, slightly angled
- minimal green accents
- no clutter
- no decorative nonsense
- no gradients that overpower the text
- no long body copy
- no logos or watermark
- everything should read in under one second
- keep the image crop-safe for a final 5:2 banner

Style:
- premium product launch poster
- modern Apple-adjacent cleanliness
- crisp
- balanced
- elegant
""".strip(),
    """
Create a clean premium 5:2 banner image for an X article cover.

The subject is a Nano Banana Pro skill that automates App Store screenshot creation end to end.

Required headline text exactly:
APP STORE ADS.
ON AUTOPILOT.

Optional subline:
Built with Nano Banana Pro

Composition:
- left side dominated by oversized headline in white
- right side shows 3 polished mobile app campaign slides
- background should be matte black or deep graphite
- a single sharp neon-green highlight line or glow
- simple, expensive, readable
- not busy
- not futuristic slop
- no extra paragraphs
- no made-up badges
- no fake metrics
- keep the design centered and crop-safe
- no logos or watermark
""".strip(),
    """
Create an ultra-clean premium 5:2 X article cover image.

This is for a tool that automates App Store screenshot campaigns.

Required headline text exactly:
FULLY AUTOMATED
APP STORE ADS

Important text rule:
- the headline is the only readable text in the entire image
- do not put any readable text inside phones, cards, buttons, labels, or UI
- use abstract app screens and shapes only

Composition:
- oversized white condensed sans-serif headline on the left
- 3 elegant mobile campaign cards on the right
- deep matte black background
- one thin neon-green accent line or glow
- simple, expensive, minimal
- lots of negative space
- no clutter
- no logos
- no watermark
- no extra captions
- crop-safe for 5:2
""".strip(),
    """
Design a minimalist cinematic social banner in a 5:2 ratio.

Subject:
Nano Banana Pro automates App Store screenshots.

Required headline text exactly:
RAW SHOTS IN.
APP STORE ADS OUT.

Important:
- this headline is the only readable text allowed
- no readable text anywhere else

Visual style:
- black background
- white type
- subtle green accent
- right side shows clean premium stacked phone cards with abstract screenshot layouts
- no extra badges
- no random UI labels
- no noisy details
- should feel like a polished launch poster
- should be instantly legible
- keep everything safely centered for cropping
""".strip(),
    """
Use the attached reference image for typography, spacing, color palette, UI style, and overall product-marketing feel.

Create a light-themed 5:2 X article header in that same design family.

Match these reference traits:
- DM Sans style typography
- huge bold headline
- soft off-white background
- restrained warm orange accent
- rounded neutral product card
- calm, modern SaaS landing page aesthetic
- clean spacing
- not noisy

Required headline text exactly:
App Store ads
on autopilot

Optional short support line:
Automated screenshot campaigns with Nano Banana Pro

Layout:
- headline and support line on the left
- one polished rounded product-demo panel on the right
- inside the panel, show elegant app screenshot campaign slides in a clean UI style inspired by the reference
- keep everything very readable and minimal
- no extra paragraphs
- no logos
- no watermarks
- no nonsense labels
- crop-safe for a final 5:2 banner

The image should feel like it belongs to the same world as the reference website hero.
""".strip(),
    """
Use the attached reference image for typography, spacing, color palette, and overall design language.

Create a light-themed 5:2 X article header for a Codex / Claude Code skill, not a SaaS product.

Match these reference traits:
- DM Sans style typography
- giant bold headline
- soft off-white background
- subtle warm orange accent
- rounded product panel
- calm, premium landing-page feel
- very clean spacing
- minimal noise

Required headline text exactly:
App Store ads
for your skill

Optional short support line:
A Codex skill that turns raw screenshots into polished App Store creative

Critical framing:
- this is a developer skill / agent skill
- do not make it look like a SaaS dashboard
- do not show charts, analytics, pricing, or app settings panels
- instead show a clean tooling-style composition:
  - a rounded workspace panel
  - tasteful app screenshot campaign previews
  - subtle prompt / terminal / generation cues
  - a design or creative-workflow feeling

Layout:
- headline and support line on the left
- one rounded hero panel on the right
- inside the panel, show a premium skill workflow for generating App Store screenshot campaigns
- keep it visually simple and readable
- no extra paragraphs
- no logos
- no watermarks
- no cluttered code blocks
- crop-safe for a final 5:2 banner

The image should feel like a premium developer tool landing page hero in the style family of the reference.
""".strip(),
    """
Use the attached reference image for typography, spacing, color palette, and overall design language.

Create a light-themed 5:2 X article header for a Codex / Claude Code skill that automates App Store screenshot creation.

The article's core idea is:
- App Store screenshots matter a lot
- most teams underinvest in them
- making them well is too much manual work
- this skill automates the entire workflow end to end

Match these reference traits:
- DM Sans style typography
- huge bold headline
- soft off-white background
- subtle warm orange accent
- rounded clean product panel
- calm, premium SaaS-landing-page polish
- minimal and highly readable

Required headline text exactly:
App Store screenshots,
fully automated

Optional short support line:
A Codex skill for end-to-end screenshot campaigns

Critical framing:
- this is a developer skill / coding-agent skill
- do not make it look like a SaaS dashboard
- do not show analytics, pricing, or settings
- show a clean creative-workflow surface instead:
  - a raw app screenshot or capture on the left of the panel
  - polished App Store campaign slides on the right of the panel
  - a subtle generation or workflow cue between them

Layout:
- headline and support line on the left
- one rounded hero panel on the right
- very clean composition
- no extra paragraphs
- no cluttered code blocks
- no logos
- no watermarks
- very little small text
- crop-safe for a final 5:2 banner

The final image should make the promise obvious in one second: this skill turns manual screenshot work into a polished automated workflow.
""".strip(),
]


def api_key() -> str:
    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key:
        raise SystemExit("Missing GEMINI_API_KEY or GOOGLE_API_KEY")
    return key


def request_image(prompt: str, reference_image: Path | None = None):
    parts = [{"text": prompt}]
    if reference_image is not None:
        mime_type = mimetypes.guess_type(reference_image.name)[0] or "image/png"
        parts.append(
            {
                "inlineData": {
                    "mimeType": mime_type,
                    "data": base64.b64encode(reference_image.read_bytes()).decode(),
                }
            }
        )

    payload = {
        "contents": [{"parts": parts}],
        "generationConfig": {
            "imageConfig": {
                "aspectRatio": "16:9",
                "imageSize": "2K",
            }
        },
    }
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode(),
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": api_key(),
        },
        method="POST",
    )
    ssl_context = None
    if certifi is not None:
        ssl_context = ssl.create_default_context(cafile=certifi.where())
    with urllib.request.urlopen(req, timeout=180, context=ssl_context) as response:
        data = json.loads(response.read().decode())
    for candidate in data.get("candidates", []):
        for part in candidate.get("content", {}).get("parts", []):
            inline = part.get("inlineData")
            if inline and inline.get("data"):
                return Image.open(io.BytesIO(base64.b64decode(inline["data"]))).convert("RGB")
    raise RuntimeError(json.dumps(data)[:1200])


def crop_to_5_2(img: Image.Image, width: int = 2000, height: int = 800) -> Image.Image:
    target_ratio = width / height
    src_ratio = img.width / img.height
    if src_ratio > target_ratio:
        new_h = img.height
        new_w = int(new_h * target_ratio)
        left = (img.width - new_w) // 2
        top = 0
        cropped = img.crop((left, top, left + new_w, top + new_h))
    else:
        new_w = img.width
        new_h = int(new_w / target_ratio)
        left = 0
        top = (img.height - new_h) // 2
        cropped = img.crop((left, top, left + new_w, top + new_h))
    return cropped.resize((width, height), Image.Resampling.LANCZOS)


def main():
    chosen = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    if not 1 <= chosen <= len(PROMPTS):
        raise SystemExit("Prompt index out of range")
    prompt = PROMPTS[chosen - 1]
    reference_image = ROOT / "output" / "playwright" / "datafast-ref.png"
    if chosen == 6 and not reference_image.exists():
        raise SystemExit(f"Missing reference image: {reference_image}")
    img = request_image(prompt, reference_image if chosen == 6 else None)
    raw_path = OUT_DIR / f"header-variant-{chosen}-raw.png"
    final_path = OUT_DIR / f"header-variant-{chosen}-5x2.png"
    raw_path.write_bytes(b"")
    img.save(raw_path)
    crop_to_5_2(img).save(final_path)
    print(final_path)


if __name__ == "__main__":
    main()
