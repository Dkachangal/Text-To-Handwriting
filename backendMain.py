from PIL import Image
from pathlib import Path
import numpy as np
from skimage.filters import threshold_otsu

# FUNCTION 1 to input and save jpg image in folder name characters
# connects to the frontend
# to make once front end input image box in done

JpgimgPath = Path('characters')
chars = {}
# FUNCTION 2 Defines image in python + convert each image into image1.png + inserts it in dictionary chars
def jpg2png():
    str = "abcdefghijklmnopqrstuvexyz"
    for i in str:
        new = JpgimgPath/f'{i}.jpg'
        img = Image.open(f"{i}.jpg").convert("L")
        gray = np.array(img)
        thresh = threshold_otsu(gray)
        mask = gray < thresh
        rgba = np.zeros((gray.shape[0], gray.shape[1], 4), dtype=np.uint8)
        rgba[..., 0] = gray        # Red
        rgba[..., 1] = gray        # Green 
        rgba[..., 2] = gray        # Blue 
        rgba[..., 3] = mask * 255  #transparent

        Image.fromarray(rgba).save(f"{i}1.png")
        chars[f"{i}"] = img
