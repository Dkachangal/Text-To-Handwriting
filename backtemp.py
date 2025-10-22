from PIL import Image, ImageFilter
from matplotlib import pyplot as plt
from pathlib import Path
import numpy as np
from skimage.filters import threshold_otsu
import datetime
import cv2

# FUNCTION 1 to input and save jpg image in folder name characters
# connects to the frontend
# to make once front end input image box in done

JpgimgPath = Path('characters')
chars = {}
str = "abcdefghijklmnopqrstuvwxyz"

# FUNCTION 2 Defines image in python + convert each image into image1.png
def jpg2png():
    global chars
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
        # Image.fromarray(rgba).save(f"{i}1.png")
        # chars[i] = img

def createDict():
    for i in str:
        new = JpgimgPath/f'{i}1.png'
        img = Image.open(new)
        chars[i] = img

createDict()

space = Image.open('space.png')
chars[" "] = space # defining space

# LET THE STRING FROM USER BE :
user_data = "this is the user defined string it is the first sentence"

# Let the Page selected by the user be page:
page = Image.open('p3.jpg')

# FUNCTION 3 to iterate the user defined string and paste each element on the page
# WRITING

# user_data = 'hello world'

def iterateUserStr():
    global page
    global user_data
    page = page.convert("RGBA")

    # Convert page to grayscale and threshold once
    page_gray = np.array(page.convert("L"))
    _, thresh = cv2.threshold(page_gray, 150, 255, cv2.THRESH_BINARY_INV)
    height, width = thresh.shape

    x = 100  # starting x
    line_spacing = 50  # how much to move down for next line if needed

    for ch in user_data:
        if x >= width:
            # move to next line if reaching edge
            x = 100
            # find y at new line
            # here you can just increment by line spacing
            # or find top of next line from threshold
            # For simplicity, we just move down
            # y will be computed dynamically per character below

        if ch == ' ':
            x += 20  # spacing for space
            continue

        img = chars[ch]
        if img.mode != 'RGBA':
            img_rgba = img.convert('RGBA')
        else:
            img_rgba = img

        # Compute y dynamically for this x (top of ink in column)
        x_use = min(x, width-1)  # clamp x to image width
        column = thresh[:, x_use]  # all pixels in this column
        y_candidates = np.where(column > 0)[0]  # indexes of black pixels

        if len(y_candidates) > 0:
            y_line = y_candidates[0]  # top of line at this x
        else:
            y_line = 200  # fallback if no ink found

        # Paste letter
        hei = y_line - img_rgba.height
        page.paste(img_rgba, (x, hei), img_rgba)

        # Increment x for next letter
        x += img_rgba.width + 5  # add small gap

    plt.imshow(page)
    plt.axis('off')
    plt.show()


iterateUserStr()