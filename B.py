# backendMain.py
from PIL import Image
from matplotlib import pyplot as plt
from pathlib import Path
import numpy as np
from skimage.filters import threshold_otsu
import os


# ---------- FUNCTION 1: Convert all JPG character images to transparent PNGs ----------
def jpg2png(characters_dict, output_folder="DKChars"):
    """
    Converts each .jpg character image to a transparent .png and saves in DKChars folder.
    """
    output_path = Path(output_folder)
    output_path.mkdir(exist_ok=True)

    for ch, img_path in characters_dict.items():
        if not os.path.exists(img_path):
            print(f"⚠️ File not found for '{ch}' at {img_path}")
            continue

        try:
            img = Image.open(img_path).convert("L")
            gray = np.array(img)
            thresh = threshold_otsu(gray)
            mask = gray < thresh

            rgba = np.zeros((gray.shape[0], gray.shape[1], 4), dtype=np.uint8)
            rgba[..., 0] = gray
            rgba[..., 1] = gray
            rgba[..., 2] = gray
            rgba[..., 3] = mask * 255

            Image.fromarray(rgba).save(output_path / f"{ch}1.png")
            print(f"✅ Converted: {ch}.jpg → {ch}1.png")

        except Exception as e:
            print(f"❌ Error converting '{ch}': {e}")

    print(f"✅ Conversion done. Saved to folder: {output_folder}")


# ---------- FUNCTION 2: Load all PNG characters ----------
def createDict(folder_path="DKChars"):
    """
    Loads all converted PNG character images into a dictionary.
    """
    chars = {}
    folder = Path(folder_path)

    for file in folder.glob("*1.png"):
        ch = file.stem[0]
        try:
            chars[ch] = Image.open(file)
        except Exception as e:
            print(f"⚠️ Error loading '{file}': {e}")

    if Path("space.png").exists():
        chars[" "] = Image.open("space.png")

    print(f"✅ Loaded {len(chars)} characters from {folder_path}")
    return chars


# ---------- FUNCTION 3: Iterate through text and draw it ----------
def iterateUserStr(user_data, chars, page_path):
    """
    Iterates user text and pastes each character image on the selected page.
    """
    if not os.path.exists(page_path):
        print(f"❌ Page not found: {page_path}")
        return

    page = Image.open(page_path).convert("RGBA")
    x, y = 100, 200
    x_max = page.width

    for ch in user_data:
        if ch not in chars:
            continue

        img = chars[ch].convert("RGBA")
        hei = y - img.height
        page.paste(img, (x, hei), img)

        if (x + 41 > x_max - img.width):
            x = 100
            y += 54
            x -= 30
        else:
            x += 30

    plt.imshow(page)
    plt.axis("off")
    plt.show()
    print("✅ Final handwritten page generated.")
