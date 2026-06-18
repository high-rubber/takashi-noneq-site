"""
This code colorizes a grayscale image by mapping the pixel intensity to a color
gradient defined by two RGB colors.
The user can specify min/max gray points used for interpolation:
- gray <= min uses COLOR_BLACK
- gray >= max uses COLOR_WHITE
- min < gray < max is linearly interpolated between the two colors
The output is saved as a new image file.
"""

import cv2
import numpy as np

INPUT_IMAGE = "bg_0.png"
OUTPUT_IMAGE = "output_colored.png"

# min -> COLOR_BLACK
# max -> COLOR_WHITE
GRAY_MIN = 64
GRAY_MAX = 255
COLOR_BLACK = "#000000"
COLOR_WHITE = "#00ffff"


def hex_to_rgb(hex_color: str) -> np.ndarray:
    """Convert #RRGGBB to RGB array([R, G, B], dtype=float32)."""
    code = hex_color.strip().lstrip("#")
    if len(code) != 6:
        raise ValueError(f"Invalid color code: {hex_color}")
    return np.array(
        [int(code[0:2], 16), int(code[2:4], 16), int(code[4:6], 16)], dtype=np.float32
    )


def colorize_grayscale(
    gray: np.ndarray,
    color_black: np.ndarray,
    color_white: np.ndarray,
    gray_min: int,
    gray_max: int,
) -> np.ndarray:
    """Map gray values to colors using clamped min/max interpolation."""
    if not (0 <= gray_min < gray_max <= 255):
        raise ValueError(
            f"Invalid gray range: min={gray_min}, max={gray_max}. Expected 0 <= min < max <= 255."
        )

    gray_f = gray.astype(np.float32)
    gray_clamped = np.clip(gray_f, gray_min, gray_max)
    t = (gray_clamped - gray_min) / float(gray_max - gray_min)
    colored_rgb = color_black + (color_white - color_black) * t[..., None]
    colored_rgb = np.clip(colored_rgb, 0, 255).astype(np.uint8)

    # OpenCV uses BGR channel order for writing image files.
    return cv2.cvtColor(colored_rgb, cv2.COLOR_RGB2BGR)


def main() -> None:
    gray = cv2.imread(INPUT_IMAGE, cv2.IMREAD_GRAYSCALE)
    # gray = cv2.equalizeHist(gray)  # Optional: enhance contrast for better colorization
    if gray is None:
        raise FileNotFoundError(f"Input image not found: {INPUT_IMAGE}")

    c0 = hex_to_rgb(COLOR_BLACK)
    c1 = hex_to_rgb(COLOR_WHITE)

    result = colorize_grayscale(gray, c0, c1, GRAY_MIN, GRAY_MAX)
    cv2.imwrite(OUTPUT_IMAGE, result)
    print(f"Saved: {OUTPUT_IMAGE}")


if __name__ == "__main__":
    main()
