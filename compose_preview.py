# -*- coding: utf-8 -*-
"""X (Twitter) Profile Preview Card Composer.

Combines 1500x500 banner, square avatar, display name, handle, bio, and X UI
into a realistic 749x465 Twitter dark-mode profile preview card.
"""

from __future__ import annotations

import argparse
import math
import os
import sys
from pathlib import Path
from typing import Optional, Tuple, List

from PIL import Image, ImageDraw, ImageFont


def _find_font(font_names: List[str]) -> Optional[str]:
    """Search system font directories for available fonts."""
    search_dirs = []
    if sys.platform == "win32":
        search_dirs.append(Path(os.environ.get("WINDIR", "C:\\Windows")) / "Fonts")
    elif sys.platform == "darwin":
        search_dirs.extend([
            Path("/System/Library/Fonts"),
            Path("/Library/Fonts"),
            Path.home() / "Library/Fonts",
        ])
    else:
        search_dirs.extend([
            Path("/usr/share/fonts"),
            Path("/usr/local/share/fonts"),
            Path.home() / ".fonts",
            Path.home() / ".local/share/fonts",
        ])

    for font_name in font_names:
        for sdir in search_dirs:
            p = sdir / font_name
            if p.exists():
                return str(p)
            # Recursive check for Linux subdirs
            matched = list(sdir.glob(f"**/{font_name}"))
            if matched:
                return str(matched[0])
    return None


def get_font(kind: str = "sans", size: int = 15, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    """Load the best available font with cross-platform fallbacks."""
    bold_candidates = [
        "msyhbd.ttc", "segoeuib.ttf", "NotoSansSC-Bold.otf", "NotoSansSC-VF.ttf",
        "PingFang Bold.ttf", "Arial Bold.ttf", "arialbd.ttf", "DejaVuSans-Bold.ttf",
        "wqy-microhei.ttc"
    ]
    regular_candidates = [
        "msyh.ttc", "segoeui.ttf", "NotoSansSC-Regular.otf", "NotoSansSC-VF.ttf",
        "PingFang.ttc", "Arial.ttf", "arial.ttf", "DejaVuSans.ttf",
        "wqy-microhei.ttc"
    ]
    candidates = bold_candidates if bold else regular_candidates

    font_path = _find_font(candidates)
    if font_path:
        try:
            f = ImageFont.truetype(font_path, size)
            if "VF" in font_path:
                weight = 700 if bold else 400
                try:
                    f.set_variation_by_axes([weight])
                except Exception:
                    pass
            return f
        except Exception:
            pass

    try:
        return ImageFont.load_default()
    except Exception:
        return ImageFont.load_default()


def draw_verified_badge(size: int = 20) -> Image.Image:
    """Generate Twitter blue verified badge (scalloped circle + white checkmark)."""
    S = size * 4
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)

    cx, cy = S / 2.0, S / 2.0
    r_base = S * 0.40
    r_bump = S * 0.12
    n_points = 12
    for i in range(n_points):
        angle = i * (2.0 * math.pi / n_points)
        bx = cx + r_base * math.cos(angle)
        by = cy + r_base * math.sin(angle)
        d.ellipse([bx - r_bump, by - r_bump, bx + r_bump, by + r_bump], fill="#1D9BF0")
    d.ellipse([cx - r_base, cy - r_base, cx + r_base, cy + r_base], fill="#1D9BF0")

    stroke = max(2, int(S * 0.08))
    p1 = (int(S * 0.28), int(S * 0.50))
    p2 = (int(S * 0.43), int(S * 0.66))
    p3 = (int(S * 0.73), int(S * 0.35))
    d.line([p1, p2, p3], fill="#FFFFFF", width=stroke, joint="curve")

    r_cap = stroke // 2
    for p in [p1, p3]:
        d.ellipse([p[0] - r_cap, p[1] - r_cap, p[0] + r_cap, p[1] + r_cap], fill="#FFFFFF")

    return im.resize((size, size), Image.Resampling.LANCZOS)


def draw_tip_button(size: int = 44) -> Image.Image:
    """Generate tip button with circular border and $ icon."""
    S = size * 4
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)

    stroke = 4
    d.ellipse([stroke // 2, stroke // 2, S - 1 - stroke // 2, S - 1 - stroke // 2], outline="#536471", width=stroke)

    font = get_font(size=int(S * 0.46), bold=True)
    bbox = d.textbbox((0, 0), "$", font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    tx = (S - tw) // 2 - bbox[0]
    ty = (S - th) // 2 - bbox[1]
    d.text((tx, ty), "$", font=font, fill="#EFF3F4")

    return im.resize((size, size), Image.Resampling.LANCZOS)


def wrap_text(text: str, font: ImageFont.ImageFont, max_width: int, draw: ImageDraw.ImageDraw) -> List[str]:
    """Wrap text to fit within max_width pixels."""
    lines: List[str] = []
    for raw_line in text.splitlines():
        if not raw_line:
            lines.append("")
            continue
        cur = ""
        for ch in raw_line:
            test_line = cur + ch
            bb = draw.textbbox((0, 0), test_line, font=font)
            if bb[2] - bb[0] <= max_width:
                cur = test_line
            else:
                if cur:
                    lines.append(cur)
                cur = ch
        if cur:
            lines.append(cur)
    return lines


def compose_profile_preview(
    banner_path_or_img: str | Path | Image.Image,
    avatar_path_or_img: str | Path | Image.Image,
    name: str = "HUZI",
    handle: str = "@lihu9048",
    bio: str = "学习AI，分享AI",
    verified: bool = True,
    button_text: str = "编辑个人资料",
    width: int = 749,
    height: int = 465,
    banner_height: int = 250,
) -> Image.Image:
    """Compose banner, avatar, and X profile metadata into a profile preview image."""
    if isinstance(banner_path_or_img, (str, Path)):
        banner_img = Image.open(banner_path_or_img)
    else:
        banner_img = banner_path_or_img

    if isinstance(avatar_path_or_img, (str, Path)):
        avatar_img = Image.open(avatar_path_or_img)
    else:
        avatar_img = avatar_path_or_img

    canvas = Image.new("RGBA", (width, height), (0, 0, 0, 255))

    # 1. Fit and scale banner to (width, banner_height)
    bw, bh = banner_img.size
    target_ratio = width / banner_height
    curr_ratio = bw / bh
    if curr_ratio > target_ratio:
        crop_w = int(bh * target_ratio)
        x0 = (bw - crop_w) // 2
        b_cropped = banner_img.crop((x0, 0, x0 + crop_w, bh))
    else:
        crop_h = int(bw / target_ratio)
        y0 = (bh - crop_h) // 2
        b_cropped = banner_img.crop((0, y0, bw, y0 + crop_h))

    banner_scaled = b_cropped.resize((width, banner_height), Image.Resampling.LANCZOS).convert("RGBA")
    canvas.paste(banner_scaled, (0, 0))

    # 2. Avatar cutout and composition
    # Proportions relative to 749x465 template:
    scale = width / 749.0
    cx = int(107 * scale)
    cy = int(banner_height - 4 * scale)
    r_inner = int(84 * scale)
    r_outer = int(88 * scale)

    draw = ImageDraw.Draw(canvas)
    draw.ellipse([cx - r_outer, cy - r_outer, cx + r_outer, cy + r_outer], fill=(0, 0, 0, 255))

    av_d = r_inner * 2
    av_resized = avatar_img.resize((av_d, av_d), Image.Resampling.LANCZOS).convert("RGBA")

    # High-quality circular mask
    mask_big = Image.new("L", (av_d * 4, av_d * 4), 0)
    ImageDraw.Draw(mask_big).ellipse([0, 0, av_d * 4 - 1, av_d * 4 - 1], fill=255)
    mask = mask_big.resize((av_d, av_d), Image.Resampling.LANCZOS)

    av_masked = Image.new("RGBA", (av_d, av_d), (0, 0, 0, 0))
    av_masked.paste(av_resized, (0, 0), mask)
    canvas.paste(av_masked, (cx - r_inner, cy - r_inner), av_masked)

    # 3. Top-right action buttons
    tip_size = int(44 * scale)
    tip_x = int(516 * scale)
    tip_y = int(266 * scale)
    tip_btn = draw_tip_button(tip_size)
    canvas.paste(tip_btn, (tip_x, tip_y), tip_btn)

    btn_w = int(166 * scale)
    btn_h = int(44 * scale)
    btn_x = int(560 * scale)
    btn_y = int(266 * scale)
    btn_img = Image.new("RGBA", (btn_w, btn_h), (0, 0, 0, 0))
    bd = ImageDraw.Draw(btn_img)
    bd.rounded_rectangle([0, 0, btn_w - 1, btn_h - 1], radius=int(btn_h // 2), outline="#536471", width=1)

    btn_font = get_font(size=int(15 * scale), bold=True)
    bb = bd.textbbox((0, 0), button_text, font=btn_font)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    bd.text(((btn_w - tw) // 2, (btn_h - th) // 2 - 2), button_text, font=btn_font, fill="#EFF3F4")
    canvas.paste(btn_img, (btn_x, btn_y), btn_img)

    # 4. User identity metadata
    name_x = int(18 * scale)
    name_y = int(362 * scale)
    name_font = get_font(size=int(21 * scale), bold=True)
    draw.text((name_x, name_y), name, font=name_font, fill="#EFF3F4")

    nbb = draw.textbbox((name_x, name_y), name, font=name_font)
    if verified:
        badge_size = int(20 * scale)
        badge = draw_verified_badge(badge_size)
        badge_x = nbb[2] + int(6 * scale)
        badge_y = name_y + (nbb[3] - nbb[1] - badge_size) // 2 + 1
        canvas.paste(badge, (badge_x, badge_y), badge)

    handle_y = int(394 * scale)
    handle_font = get_font(size=int(15 * scale), bold=False)
    draw.text((name_x, handle_y), handle, font=handle_font, fill="#71767B")

    bio_y = int(430 * scale)
    bio_font = get_font(size=int(15 * scale), bold=False)
    max_bio_w = int(width - name_x - 30 * scale)
    bio_lines = wrap_text(bio, bio_font, max_bio_w, draw)

    line_spacing = int(20 * scale)
    for i, line in enumerate(bio_lines):
        draw.text((name_x, bio_y + i * line_spacing), line, font=bio_font, fill="#EFF3F4")

    return canvas.convert("RGB")


def main() -> None:
    parser = argparse.ArgumentParser(description="Compose X (Twitter) profile preview card.")
    parser.add_argument("--banner", required=True, help="Path to banner image (1500x500 or any 3:1 ratio)")
    parser.add_argument("--avatar", required=True, help="Path to avatar image (1:1 square)")
    parser.add_argument("--name", default="HUZI", help="Display name (default: HUZI)")
    parser.add_argument("--handle", default="@lihu9048", help="X handle (default: @lihu9048)")
    parser.add_argument("--bio", default="学习AI，分享AI", help="User bio (default: 学习AI，分享AI)")
    parser.add_argument("--no-verified", action="store_true", help="Omit blue verified badge")
    parser.add_argument("--button-text", default="编辑个人资料", help="Right action button text")
    parser.add_argument("--width", type=int, default=749, help="Output width (default: 749)")
    parser.add_argument("--height", type=int, default=465, help="Output height (default: 465)")
    parser.add_argument("--out", default="profile-preview.png", help="Output path (default: profile-preview.png)")

    args = parser.parse_args()

    res = compose_profile_preview(
        banner_path_or_img=args.banner,
        avatar_path_or_img=args.avatar,
        name=args.name,
        handle=args.handle,
        bio=args.bio,
        verified=not args.no_verified,
        button_text=args.button_text,
        width=args.width,
        height=args.height,
    )

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    res.save(out_path, "PNG", optimize=True)
    print(f"[OK] Profile preview card saved: {out_path} ({res.width}x{res.height})")


if __name__ == "__main__":
    main()
