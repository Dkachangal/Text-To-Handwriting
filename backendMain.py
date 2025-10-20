from PIL import Image, ImageFilter
from matplotlib import pyplot as plt
from pathlib import Path
import numpy as np
from skimage.filters import threshold_otsu
import datetime

# FUNCTION 1 to input and save jpg image in folder name characters
# connects to the frontend
# to make once front end input image box in done

JpgimgPath = Path('characters')
chars = {}
str = "abcdefghijklmnopqrstuvwxyz"

# FUNCTION 2 Defines image in python + convert each image into image1.png + inserts it in dictionary chars
# def jpg2png():
#     global chars
#     str = "abcdefghijklmnopqrstuvwxyz"
#     for i in str:
#         new = JpgimgPath/f'{i}.jpg'
#         img = Image.open(new).convert("L")

#         gray = np.array(img)
#         thresh = threshold_otsu(gray)
#         mask = gray < thresh

#         rgba = np.zeros((gray.shape[0], gray.shape[1], 4), dtype=np.uint8)
#         rgba[..., 0] = gray        # Red
#         rgba[..., 1] = gray        # Green 
#         rgba[..., 2] = gray        # Blue 
#         rgba[..., 3] = mask * 255  #transparent

        # save image:
        # TO DO: 
        # update the code so as it creates a new folder and saves the image there rather than this location
        # Image.fromarray(rgba).save(f"{i}1.png")
        # chars[i] = img
# jpg2png()
def createDict():
    for i in str:
        new = JpgimgPath/f'{i}1.png'
        img = Image.open(new).convert("L")
        chars[i] = img

createDict()

space = Image.open('space.png')
chars[" "] = space # defining space

# LET THE STRING FROM USER BE :
user_data = "this is the user defined string it is the first sentence"
# Let the Page selected by the user be page:
page = Image.open('p3.jpg')

# FUNCTION 3 to iterate the user defined string and paste each element on the page
def iterateUserStr():

    global page
    page = page.convert("RGBA")
    x = 100
    # global x
    y = 200
    for i in user_data:
        ch = chars[i]
        if ch.mode != 'RGBA':
            img_rgba = ch.convert('RGBA')
        else:
            img_rgba = ch

        datas = img_rgba.getdata()
        new_data = []
        for item in datas:
            # item = (R, G, B, A)
            # if the pixel is near-white, make it fully transparent
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)
        img_rgba.putdata(new_data)

        hei = y - img_rgba.height
        page.paste(img_rgba, (x, hei), img_rgba)
        x += 40
        
    plt.imshow(page.convert('RGB'))
    plt.axis('off')

def it2():
    global page
    str = "cabi"
    x = 100
    page = page.convert("RGBA")
    text = "cabi"
    for ch in text:
        y = 200
        img = chars[ch]
        if img.mode != 'RGBA':
            img_rgba = img.convert('RGBA')
        else:
            img_rgba = img

        hei = y - img_rgba.height
        page.paste(img_rgba, (x, hei), img_rgba)
        x += 40
it2()
# iterateUserStr()
page.show()