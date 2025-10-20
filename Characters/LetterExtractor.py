from PIL import Image
import numpy as np
from skimage.filters import threshold_otsu   # For automatic threshold finding

# 1. Load the image
# f = Image.open("f.jpg").convert("L")

chars = {}

for i in "fghijklmnopqrstuvwxyz":
    i = Image.open(f"{i}.jpg")

for i in "fghijklmnopqrstuvwxyz":
    chars[f"{i}"] = i

img = Image.open("a.jpg").convert("L")  # 'L' means grayscale
gray = np.array(img)

# 2. Automatically find a good threshold
thresh = threshold_otsu(gray)

# 3. Create a mask
# Pixels darker than threshold → keep (ink)
# Pixels brighter → remove (background)
mask = gray < thresh

# 4. Create RGBA output (so we can make background transparent)
rgba = np.zeros((gray.shape[0], gray.shape[1], 4), dtype=np.uint8)
rgba[..., 0] = gray        # Red channel
rgba[..., 1] = gray        # Green channel
rgba[..., 2] = gray        # Blue channel
rgba[..., 3] = mask * 255  # Alpha channel: 255 = opaque, 0 = transparent

# 5. Optional smoothing (light blur edges)
# from scipy.ndimage import gaussian_filter
# rgba[..., 3] = gaussian_filter(rgba[..., 3], sigma=0.7)

# 6. Save the cleaned image
# Image.fromarray(rgba).save("Dollar1.png")
