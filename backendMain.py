from PIL import Image
from pathlib import Path
import numpy as np
from skimage.filters import threshold_otsu
import datetime

# FUNCTION 1 to input and save jpg image in folder name characters
# connects to the frontend
# to make once front end input image box in done

JpgimgPath = Path('characters')
chars = {}

# FUNCTION 2 Defines image in python + convert each image into image1.png + inserts it in dictionary chars
def jpg2png():

    str = "abcdefghijklmnopqrstuvwxyz"

    for i in str:
        new = JpgimgPath/f'{i}.jpg'
        img = Image.open(new).convert("L")

        gray = np.array(img)
        thresh = threshold_otsu(gray)
        mask = gray < thresh

        rgba = np.zeros((gray.shape[0], gray.shape[1], 4), dtype=np.uint8)
        rgba[..., 0] = gray        # Red
        rgba[..., 1] = gray        # Green 
        rgba[..., 2] = gray        # Blue 
        rgba[..., 3] = mask * 255  #transparent

        # save image:
        # TO DO: 
        # update the code so as it creates a new folder and saves the image there rather than this location
        Image.fromarray(rgba).save(f"PNG_{i}.png")
        chars[f"{i}"] = img

# FUNCTION 3 to iterate the user defined string and paste each element on the page

