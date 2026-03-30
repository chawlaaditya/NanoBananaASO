#!/usr/bin/env python3
import base64
import io
import json
import math
import os
import random
import ssl
import sys
import urllib.request
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

try:
    import certifi
except ImportError:
    certifi = None


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "output" / "social"
BG_PATH = OUT_DIR / "nano-banana-pro-bg.png"
FINAL_PATH = OUT_DIR / "x-article-header-5x2.png"

W = 2000
H = 800

HEADLINE = "APP STORE ADS.\nON AUTOPILOT."
SUBHEAD = (
    "A Nano Banana Pro skill that reads your app, plans the story, "
    "generates the campaign, and exports the set."
)
INSTALL = "npx skills add chawlaaditya/NanoBananaASO"

PROMPT = """
Create a premium ultra-wide social header background for a developer tool that automates
App Store screenshot campaigns.

No words, no letters, no numbers, no logos, no UI text, no watermarks.

Composition:
- left 45 percent should be mostly clean dark negative space for later headline overlay
- right 55 percent should feel energetic and premium
- show a stylish collage of tall mobile campaign cards, polished phone silhouettes, layered
  screenshot frames, motion arcs, glass highlights, and launch-poster atmosphere

Art direction:
- deep graphite and near-black base
- electric green, cyan, coral, warm cream, and subtle violet accents
- cinematic lighting
- editorial tech poster feel
- crisp, premium, not generic AI art
- strong depth, tasteful grain, strong contrast
- designed to crop cleanly into a 5:2 banner

Keep the image visually compelling but uncluttered.
""".strip()


def require_api_key() -> str:
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise SystemExit("Missing GEMINI_API_KEY or GOOGLE_API_KEY")
    return api_key


def fetch_background(api_key: str) -> Image.Image:
    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        "gemini-3-pro-image-preview:generateContent"
    )
    payload = {
        "contents": [{"parts": [{"text": PROMPT}]}],
        "generationConfig": {
            "imageConfig": {
                "aspectRatio": "16:9",
                "imageSize": "4K",
            }
        },
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": api_key,
        },
        method="POST",
    )
    ssl_context = None
    if certifi is not None:
        ssl_context = ssl.create_default_context(cafile=certifi.where())

    with urllib.request.urlopen(req, timeout=180, context=ssl_context) as response:
        data = json.loads(response.read().decode("utf-8"))

    candidates = data.get("candidates", [])
    for candidate in candidates:
        parts = candidate.get("content", {}).get("parts", [])
        for part in parts:
            inline = part.get("inlineData")
            if inline and inline.get("data"):
                image_bytes = base64.b64decode(inline["data"])
                return Image.open(io.BytesIO(image_bytes)).convert("RGBA")

    raise RuntimeError(f"No image returned: {json.dumps(data)[:600]}")


def cover(image: Image.Image, target_w: int, target_h: int) -> Image.Image:
    src_ratio = image.width / image.height
    dst_ratio = target_w / target_h
    if src_ratio > dst_ratio:
        new_h = target_h
        new_w = int(new_h * src_ratio)
    else:
        new_w = target_w
        new_h = int(new_w / src_ratio)
    resized = image.resize((new_w, new_h), Image.Resampling.LANCZOS)
    left = (new_w - target_w) // 2
    top = (new_h - target_h) // 2
    return resized.crop((left, top, left + target_w, top + target_h))


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size=size)


def wrap_text(draw: ImageDraw.ImageDraw, text: str, max_width: int, text_font) -> str:
    words = text.split()
    lines = []
    current = []
    for word in words:
        trial = " ".join(current + [word])
        if draw.textbbox((0, 0), trial, font=text_font)[2] <= max_width or not current:
            current.append(word)
        else:
            lines.append(" ".join(current))
            current = [word]
    if current:
        lines.append(" ".join(current))
    return "\n".join(lines)


def draw_gradient(canvas: Image.Image, left_color, right_color):
    grad = Image.new("RGBA", (canvas.width, canvas.height))
    px = grad.load()
    for x in range(canvas.width):
        t = x / max(canvas.width - 1, 1)
        r = int(left_color[0] * (1 - t) + right_color[0] * t)
        g = int(left_color[1] * (1 - t) + right_color[1] * t)
        b = int(left_color[2] * (1 - t) + right_color[2] * t)
        a = int(left_color[3] * (1 - t) + right_color[3] * t)
        for y in range(canvas.height):
            px[x, y] = (r, g, b, a)
    canvas.alpha_composite(grad)


def rounded_panel(size, fill, radius=34, stroke=None, stroke_width=0):
    panel = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(panel)
    box = (0, 0, size[0] - 1, size[1] - 1)
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=stroke, width=stroke_width)
    return panel


def add_card(base: Image.Image, x: int, y: int, w: int, h: int, angle: float, colors, footer_text):
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(card)

    panel = rounded_panel((w, h), fill=colors[0], radius=42)
    card.alpha_composite(panel)

    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    o = ImageDraw.Draw(overlay)
    o.rounded_rectangle((0, 0, w - 1, h - 1), radius=42, fill=(0, 0, 0, 0))
    for i in range(h):
        alpha = int(90 * (1 - i / h))
        o.line((0, i, w, i), fill=(*colors[1][:3], alpha), width=1)
    card.alpha_composite(overlay)

    footer_h = 82
    footer = rounded_panel((w, footer_h), fill=(252, 252, 252, 255), radius=30)
    card.alpha_composite(footer, (0, h - footer_h))

    draw.rounded_rectangle((28, 28, 96, 54), radius=14, fill=(255, 255, 255, 85))
    draw.rounded_rectangle((w - 92, 28, w - 28, 54), radius=14, fill=(255, 255, 255, 45))

    device_x = 34
    device_y = 100
    device_w = w - 68
    device_h = h - 210
    draw.rounded_rectangle(
        (device_x, device_y, device_x + device_w, device_y + device_h),
        radius=48,
        fill=(12, 14, 18, 255),
        outline=(24, 28, 34, 255),
        width=6,
    )
    draw.rounded_rectangle(
        (device_x + 70, device_y + 18, device_x + device_w - 70, device_y + 42),
        radius=12,
        fill=(18, 18, 20, 255),
    )

    screen = Image.new("RGBA", (device_w - 18, device_h - 18), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(screen)
    for yy in range(screen.height):
        t = yy / max(screen.height - 1, 1)
        mix = tuple(
            int(colors[2][i] * (1 - t) + colors[3][i] * t) for i in range(3)
        )
        sdraw.line((0, yy, screen.width, yy), fill=(*mix, 255), width=1)
    sdraw.rounded_rectangle(
        (18, 24, screen.width - 18, 74),
        radius=18,
        fill=(255, 255, 255, 28),
    )
    sdraw.rounded_rectangle(
        (18, 100, screen.width - 18, screen.height - 132),
        radius=24,
        fill=(255, 255, 255, 12),
    )
    for idx in range(4):
        left = 24 + idx * ((screen.width - 64) // 4)
        sdraw.rounded_rectangle(
            (left, screen.height - 98 - idx * 12, left + 32, screen.height - 34),
            radius=16,
            fill=(255, 255, 255, 160 if idx == 2 else 80),
        )
    card.alpha_composite(screen, (device_x + 9, device_y + 9))

    card_draw = ImageDraw.Draw(card)
    footer_font = font("/Library/Fonts/SF-Pro-Text-Medium.otf", 28)
    card_draw.text((26, h - footer_h + 22), footer_text, font=footer_font, fill=(18, 20, 24, 255))

    shadow = Image.new("RGBA", (w + 80, h + 80), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shadow)
    sdraw.rounded_rectangle((40, 24, 40 + w - 1, 24 + h - 1), radius=48, fill=(0, 0, 0, 130))
    shadow = shadow.filter(ImageFilter.GaussianBlur(18))

    rotated_shadow = shadow.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True)
    rotated_card = card.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True)

    base.alpha_composite(rotated_shadow, (x - 40, y - 24))
    base.alpha_composite(rotated_card, (x, y))


def draw_noise(canvas: Image.Image, opacity: int = 18):
    rnd = random.Random(4)
    noise = Image.new("L", (canvas.width, canvas.height))
    noise.putdata([rnd.randint(96, 160) for _ in range(canvas.width * canvas.height)])
    noise = noise.filter(ImageFilter.GaussianBlur(0.35))
    noise_rgba = Image.merge("RGBA", (noise, noise, noise, Image.new("L", noise.size, opacity)))
    canvas.alpha_composite(noise_rgba)


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    api_key = require_api_key()

    bg = fetch_background(api_key)
    bg.save(BG_PATH)

    canvas = Image.new("RGBA", (W, H), (10, 12, 17, 255))
    bg_cover = cover(bg, W, H)
    bg_cover = bg_cover.filter(ImageFilter.GaussianBlur(1.2))
    canvas.alpha_composite(bg_cover)

    left_fade = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw_gradient(left_fade, (7, 9, 14, 250), (7, 9, 14, 60))
    canvas.alpha_composite(left_fade)

    vignette = Image.new("L", (W, H), 0)
    vdraw = ImageDraw.Draw(vignette)
    vdraw.ellipse((-240, -180, W + 260, H + 220), fill=190)
    vignette = ImageChops.invert(vignette).filter(ImageFilter.GaussianBlur(120))
    canvas.putalpha(255)
    dark = Image.new("RGBA", (W, H), (5, 6, 10, 118))
    dark.putalpha(vignette)
    canvas.alpha_composite(dark)

    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    gdraw.ellipse((1170, -60, 1900, 690), fill=(95, 255, 170, 42))
    gdraw.ellipse((1440, 80, 2140, 740), fill=(52, 170, 255, 34))
    gdraw.ellipse((1280, 180, 1820, 780), fill=(255, 129, 92, 24))
    glow = glow.filter(ImageFilter.GaussianBlur(80))
    canvas.alpha_composite(glow)

    add_card(canvas, 1120, 142, 228, 528, -7, (
        (28, 223, 108, 255),
        (120, 255, 196, 255),
        (18, 30, 28),
        (10, 80, 58),
    ), "Analyze the app")
    add_card(canvas, 1315, 86, 236, 560, 2, (
        (33, 182, 255, 255),
        (147, 238, 255, 255),
        (6, 32, 48),
        (22, 112, 175),
    ), "Plan the story")
    add_card(canvas, 1516, 118, 228, 528, 7, (
        (255, 166, 0, 255),
        (255, 220, 118, 255),
        (42, 24, 0),
        (112, 62, 4),
    ), "Generate the set")
    add_card(canvas, 1682, 152, 214, 496, 0, (
        (246, 244, 255, 255),
        (255, 255, 255, 255),
        (48, 14, 120),
        (136, 92, 255),
    ), "Export ready")

    draw = ImageDraw.Draw(canvas)
    eyebrow_font = font("/Library/Fonts/SF-Pro-Text-Bold.otf", 30)
    headline_font = font("/Library/Fonts/SF-Compact-Display-Heavy.otf", 124)
    sub_font = font("/Library/Fonts/SF-Pro-Text-Medium.otf", 33)
    chip_font = font("/Library/Fonts/SF-Pro-Text-Bold.otf", 24)
    install_font = font("/Library/Fonts/SFNSMono.ttf", 24)

    left_x = 92
    draw.rounded_rectangle((left_x, 66, left_x + 250, 112), radius=22, fill=(255, 255, 255, 18), outline=(255, 255, 255, 42), width=1)
    draw.text((left_x + 20, 78), "NANO BANANA PRO", font=eyebrow_font, fill=(210, 255, 228, 255))

    draw.multiline_text(
        (left_x, 140),
        HEADLINE,
        font=headline_font,
        fill=(248, 250, 252, 255),
        spacing=-6,
    )

    accent_y = 430
    draw.rounded_rectangle((left_x, accent_y, left_x + 380, accent_y + 14), radius=8, fill=(31, 255, 140, 255))
    draw.rounded_rectangle((left_x + 392, accent_y, left_x + 560, accent_y + 14), radius=8, fill=(72, 188, 255, 255))

    wrapped = wrap_text(draw, SUBHEAD, 720, sub_font)
    draw.multiline_text(
        (left_x, 470),
        wrapped,
        font=sub_font,
        fill=(194, 203, 218, 255),
        spacing=9,
    )

    chips = ["READS THE APP", "PLANS THE STORY", "EXPORTS THE SET"]
    cx = left_x
    cy = 640
    for chip in chips:
        bbox = draw.textbbox((0, 0), chip, font=chip_font)
        pad_x = 22
        chip_w = bbox[2] - bbox[0] + pad_x * 2
        draw.rounded_rectangle(
            (cx, cy, cx + chip_w, cy + 46),
            radius=20,
            fill=(255, 255, 255, 14),
            outline=(255, 255, 255, 34),
            width=1,
        )
        draw.text((cx + pad_x, cy + 11), chip, font=chip_font, fill=(237, 242, 247, 255))
        cx += chip_w + 12

    install_w = draw.textbbox((0, 0), INSTALL, font=install_font)[2] + 36
    install_y = 716
    draw.rounded_rectangle(
        (left_x, install_y, left_x + install_w, install_y + 44),
        radius=18,
        fill=(9, 13, 19, 220),
        outline=(79, 255, 163, 110),
        width=1,
    )
    draw.text((left_x + 18, install_y + 10), INSTALL, font=install_font, fill=(176, 255, 209, 255))

    draw_noise(canvas)
    canvas = canvas.convert("RGB")
    canvas.save(FINAL_PATH, quality=95)
    print(FINAL_PATH)


if __name__ == "__main__":
    main()
