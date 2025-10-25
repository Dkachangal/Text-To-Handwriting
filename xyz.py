# from mainFront import characters
from PIL import Image
import os
# path= "C:\Users\Divyansh Kachangal\OneDrive\Documents\GitHub\Text-To-Handwriting\u1.png"
path= "C:\Users\Divyansh Kachangal\OneDrive\Documents\GitHub\Text-To-Handwriting\u1.png"
path = path.replace("\\", "/")
# newPath = rf"{path}"
y = Image.open(path)
y.show()
# if os.path.isfile(path):
#     x = Image.open(path)
#     x.show()
# x = Image.open(r'C:\Users\Divyansh Kachangal\OneDrive\Documents\GitHub\Text-To-Handwriting')
dict = {
    # "a": x,
}

# for i in dict:
#     print(dict[i])