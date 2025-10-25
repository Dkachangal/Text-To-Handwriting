from PIL import Image
import os

path = "C:\Users\Divyansh Kachangal\OneDrive\Documents\GitHub\Text-To-Handwriting\u1.png"
safe_path = os.path.normpath(path)
x = Image.open(safe_path)
x.show()