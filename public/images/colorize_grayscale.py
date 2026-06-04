"""
This code colorizes a grayscale image by mapping the pixel intensity (0-255)
to a color gradient defined by two RGB colors.
The user can specify the colors for black and white,
and the code will interpolate between them to create a colored version of the grayscale image.
The output is saved as a new image file.
"""

import cv2
import numpy as np

INPUT_IMAGE = "tks2026_tus_bpf1-10_binauto.jpg"
OUTPUT_IMAGE = "output_colored.png"

# Example: black -> #000000, white -> #ff0000
COLOR_BLACK = "#000088"
COLOR_WHITE = "#ffffff"


def hex_to_rgb(hex_color: str) -> np.ndarray:
    """Convert #RRGGBB to RGB array([R, G, B], dtype=float32)."""
    code = hex_color.strip().lstrip("#")
    if len(code) != 6:
        raise ValueError(f"Invalid color code: {hex_color}")
    return np.array(
        [int(code[0:2], 16), int(code[2:4], 16), int(code[4:6], 16)], dtype=np.float32
    )


def colorize_grayscale(
    gray: np.ndarray, color_black: np.ndarray, color_white: np.ndarray
) -> np.ndarray:
    """Map gray(0-255) to colors by linear interpolation between two RGB colors."""
    t = gray.astype(np.float32) / 255.0
    colored_rgb = color_black + (color_white - color_black) * t[..., None]
    colored_rgb = np.clip(colored_rgb, 0, 255).astype(np.uint8)

    # OpenCV uses BGR channel order for writing image files.
    return cv2.cvtColor(colored_rgb, cv2.COLOR_RGB2BGR)


def main() -> None:
    gray = cv2.imread(INPUT_IMAGE, cv2.IMREAD_GRAYSCALE)
    if gray is None:
        raise FileNotFoundError(f"Input image not found: {INPUT_IMAGE}")

    c0 = hex_to_rgb(COLOR_BLACK)
    c1 = hex_to_rgb(COLOR_WHITE)

    result = colorize_grayscale(gray, c0, c1)
    cv2.imwrite(OUTPUT_IMAGE, result)
    print(f"Saved: {OUTPUT_IMAGE}")


if __name__ == "__main__":
    main()
