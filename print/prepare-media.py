#!/usr/bin/env python3
"""
Upscale + sharpen the source product photos before embedding them in the PDF.

Why: several source images from the LT Showertec catalog are smaller than the
areas they fill in the layout (full-bleed dividers/cover in particular are
793x1122 px at 96dpi). Displaying them as-is means the browser stretches them,
which looks pixelated/blurry in the exported PDF. This script upscales every
photo to a generous ceiling using high-quality Lanczos resampling, then
applies a light unsharp mask to counter the inherent softness of upscaling.
It does not crop, recolor, or otherwise change what the images show.

Usage: run from print/media/ after adding or replacing a .png source photo:
    python3 ../prepare-media.py
Outputs matching .jpg files (quality 92) alongside the .png originals.
Logos (logo-adomsenior*.svg) are untouched.
"""
from PIL import Image, ImageFilter
import glob
import os

TARGET_LONG = 2000  # px ceiling — comfortably covers a full-bleed A4 page

for f in sorted(glob.glob("*.png")):
    im = Image.open(f).convert("RGB")
    w, h = im.size
    scale = TARGET_LONG / max(w, h)
    if scale <= 1.02:
        out = im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=60, threshold=2))
    else:
        nw, nh = round(w * scale), round(h * scale)
        up = im.resize((nw, nh), Image.LANCZOS)
        out = up.filter(ImageFilter.UnsharpMask(radius=1.6, percent=110, threshold=2))
    out_path = f.replace(".png", ".jpg")
    out.save(out_path, "JPEG", quality=92, optimize=True)
    print(f"{f} {w}x{h} -> {out_path} {out.size[0]}x{out.size[1]} ({os.path.getsize(out_path)//1024} KB)")
