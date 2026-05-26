"""
This script generates a set of favicons from a regular image.
Outputs:
- favicon.ico
- favicon-16x16.png
- favicon-32x32.png
- apple-touch-icon.png (180x180)
"""

from pathlib import Path
from PIL import Image, ImageOps

# ===== Setting =====
INPUT_IMAGE = "takashigoto_mayfes_m_sb50pix-binthresh215.jpg"   # Input image path
OUTPUT_DIR = ""  # Output directory
BG_COLOR = (255, 255, 255, 0)  # Background color (RGBA). Keep as is for transparency
# ==============


def make_square_canvas(img: Image.Image, size: int, bg_color=(255, 255, 255, 0)) -> Image.Image:
    """
    Resize the image to fit within a square canvas while maintaining aspect ratio and center it.
    """
    # Correctly apply EXIF rotation
    img = ImageOps.exif_transpose(img)

    # Convert to RGBA (for transparency) if not already in that mode
    if img.mode != "RGBA":
        img = img.convert("RGBA")

    # Resize to fit within size x size while maintaining aspect ratio
    fitted = ImageOps.contain(img, (size, size), Image.Resampling.LANCZOS)

    # Create background canvas and paste the image at the center
    canvas = Image.new("RGBA", (size, size), bg_color)
    x = (size - fitted.width) // 2
    y = (size - fitted.height) // 2
    canvas.paste(fitted, (x, y), fitted)
    return canvas


def save_png(img: Image.Image, path: Path, size: int, bg_color=(255, 255, 255, 0)) -> None:
    square = make_square_canvas(img, size, bg_color=bg_color)
    square.save(path, format="PNG", optimize=True)


def save_ico(img: Image.Image, path: Path, bg_color=(255, 255, 255, 0)) -> None:
    """
    Save favicon.ico containing multiple sizes.
    """
    # Representative sizes to include in ICO
    sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64)]
    base = make_square_canvas(img, 256, bg_color=bg_color)
    base.save(path, format="ICO", sizes=sizes)


def main() -> None:
    in_path = Path(INPUT_IMAGE)
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)

    if not in_path.exists():
        raise FileNotFoundError(f"Input image not found: {in_path}")

    with Image.open(in_path) as img:
        # 1) favicon.ico
        save_ico(img, out_dir / "favicon.ico", BG_COLOR)

        # 2) favicon-16x16.png
        save_png(img, out_dir / "favicon-16x16.png", 16, BG_COLOR)

        # 3) favicon-32x32.png
        save_png(img, out_dir / "favicon-32x32.png", 32, BG_COLOR)

        # 4) apple-touch-icon.png
        save_png(img, out_dir / "apple-touch-icon.png", 180, BG_COLOR)

    print("Generation complete:")
    print(out_dir / "favicon.ico")
    print(out_dir / "favicon-16x16.png")
    print(out_dir / "favicon-32x32.png")
    print(out_dir / "apple-touch-icon.png")


if __name__ == "__main__":
    main()