import cv2
import numpy as np
import os
from skimage.filters import threshold_otsu

def extract_characters_auto(image_path, save_dir="chrs"):
    os.makedirs(save_dir, exist_ok=True)

    # known order of your characters
    sequence = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.?*;:“”/\\%[]()÷×+-=,#")

    # Load in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply Gaussian blur and threshold
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    thresh_val = threshold_otsu(blur)
    binary = (blur < thresh_val).astype(np.uint8) * 255

    # Remove small noise using morphological open
    kernel = np.ones((3, 3), np.uint8)
    clean = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

    # Invert: white text on black bg for contour detection
    inverted = 255 - clean

    # Find contours
    contours, _ = cv2.findContours(inverted, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Get bounding boxes, filter by size
    boxes = [cv2.boundingRect(c) for c in contours]
    boxes = [b for b in boxes if b[2] > 10 and b[3] > 25]  # ignore small dots

    # Sort contours row-wise and left-to-right
    def sort_contours(bboxes, row_tolerance=50):
        bboxes = sorted(bboxes, key=lambda b: (b[1] // row_tolerance, b[0]))
        return bboxes

    boxes = sort_contours(boxes, row_tolerance=60)

    print(f"Detected {len(boxes)} letters")

    # Crop and save
    for i, (x, y, w, h) in enumerate(boxes):
        if i >= len(sequence):
            break
        char_crop = img[y:y+h, x:x+w]
        char_crop = 255 - char_crop  # black text on white
        char_crop = cv2.copyMakeBorder(char_crop, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=255)
        cv2.imwrite(os.path.join(save_dir, f"{sequence[i]}.jpg"), char_crop)

    print("✅ All characters saved successfully in:", save_dir)
extract_characters_auto("abc/TanyaChar.jpg")