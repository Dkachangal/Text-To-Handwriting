# Takes input from front end
# here taking a random FrontEnd(main) file 
from PIL import Image
import numpy as np
from skimage.filters import threshold_otsu
from pathlib import Path
import datetime

JpgimgPath = Path('Characters')
 
chars = {}

str = "fghijklmnopqrstuvwxyz"

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

    Image.fromarray(rgba).save(f"{i}1.png")
    chars[f"{i}"] = img

