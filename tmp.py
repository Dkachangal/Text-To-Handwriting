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

user_data = input("Enter some data")
user_data_list = list(user_data)
# Let the Page selected by the user be page:
page = Image.open('p3.jpg')
# print(type(page.width))
x_max = 100


# word finder function
def wordLenFinderpx(i, user_data_list):
    word_len = 0
    while i < len(user_data_list) and user_data_list[i] != " ":
        word_len += chars[user_data_list[i]].width
        i += 1
    return word_len

# FUNCTION 3 to iterate the user defined string and paste each element on the page
# WRITING
def iterateUserStr():
    global page
    global user_data
    global x_max
    global user_data_list
    x = 100

    x_max= page.width
    y = 200
    page = page.convert("RGBA")
    
    for i in range(len(user_data_list)):
        word_len = 0
        # printing
        print(user_data_list[i])
        char = user_data_list[i]
        img = chars[char]
        if x == 100:
            if user_data_list[i] == " ":
                continue
        if img.mode != 'RGBA':
            img_rgba = img.convert('RGBA')
        else:
            img_rgba = img

        hei = y - img_rgba.height
        page.paste(img_rgba, (x, hei), img_rgba)
        # printing ends
        # print(img_rgba.width)
        # the new line conditioin

        word_len = wordLenFinderpx(i, user_data_list)
        
        if (x + word_len> x_max):
            x = 100
            y+=54
            x-=30
        if (x+30 < x_max+41):
            x +=30
        

    plt.imshow(page)
    plt.show()

iterateUserStr()