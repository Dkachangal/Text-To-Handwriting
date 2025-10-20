from PIL import Image, ImageChops, ImageFilter
from matplotlib import pyplot as plt
from pathlib import Path


charDir = Path('Characters')
new = charDir / 'f1.png'
img_i = Image.open(new)

# load images; convert page to RGBA so we can paste with alpha masks safely
page = Image.open('page.jpg')
a = Image.open('a1.png')
b = Image.open('h1.png')
c = Image.open('i1.png')
p = Image.open('p3.jpg')
space = Image.open('space.png')

print(a.width)
print(b.height)

char = {
    "a": a,
    "b": b,
    "c": c,
    # use the image object loaded earlier (renamed to img_i to avoid shadowing)
    "i": img_i,
    "space": space
}

# plt.imshow(p)
str = "cabi"


x = 100
# ensure background is RGBA so alpha masks work
p = p.convert("RGBA")

# don't shadow built-ins like `str` or variable names like `i`.
text = "cabi"

for ch in text:
    y = 200
    img = char[ch]
    # make sure pasted image has an alpha channel; if not, convert and create an alpha mask
    if img.mode != 'RGBA':
        img_rgba = img.convert('RGBA')
    else:
        img_rgba = img

    hei = y - img_rgba.height
    # when base (p) is RGBA, we can safely paste using the image itself as mask
    p.paste(img_rgba, (x, hei), img_rgba)
    x += 40

    # if i != " ":
    #     p.paste(char["space"], (x, hei))
# convert to RGB for display with matplotlib (it doesn't always handle RGBA the same way)
plt.imshow(p.convert('RGB'))
plt.axis('off')
plt.show()
# plt.show()




# page.paste(char["c"], (120, 463), c)
# page.paste(char["a"], (596, 1337), char["a"])
# page.paste(char["b"], (170, 463), char["b"])
# plt.imshow(p)
# plt.show()
# page.paste(char["a"], (149, 463), char["a"])

# plt.imshow(page)
# plt.show()

# plt.show()
# plt.show()
# page.show()




# page.show()

# plt.show()
# page.show()
# plt.show()
# plt.show()
# plt.imshow(land)
# banana.paste(land, (500, 500))
# plt.imshow(page)
# plt.imshow(banana)
# plt.imshow(banana)
# plt.imshow(a)
# plt.imshow(x)
# plt.show()

# banana = Image.open('banana.png')
# land = Image.open('land.jpeg')
# page = Image.open('Page.jpg')
# a = Image.open('a.jpg')

# page.paste(a, (300,400))
# plt.imshow(page)
# plt.show()

# plt.show()
# merg = ImageChops.multiply(banana, land)
# plt.show()
# plt.show()
# plt.show()
# plt.imshow(merg)
# plt.show()
# path = 'camera.jpg'

# x = Image.open("camera.jpg")
# a =  Image.open('frog.jpg')

# plt.imshow(x)
# plt.show()

# merged = ImageChops.multiply(x, a)
# plt.imshow(merged)
# plt.show()

# x.show()
# x.thumbnail((500, 500))
# plt.show()

# x.show()
# plt.imshow(x)
# plt.show()

# plt.imshow(a)
# plt.show()

# fig, axes = plt.subplots(1, 2, figsize=(10, 5))  # 1 row, 2 columns
# axes[0].imshow(x)
# axes[0].set_title('Camera')
# axes[0].axis('off')

# axes[1].imshow(a)
# axes[1].set_title('Frog')
# axes[1].axis('off')

# plt.tight_layout()
# plt.show()



"""
from PIL import Image, ImageChops, ImageFilter
from matplotlib import pyplot as plt
import os
import sys

img_path = 'camera.jpg'
# if not os.path.exists(img_path):
# 	print(f"Image not found: {img_path} (cwd: {os.getcwd()})")
# 	sys.exit(1)

x = Image.open(img_path)
sizeCam = x.size
print(sizeCam)
plt.imshow(x)
plt.axis('off')
# plt.tight_layout()
plt.show()
# plt.subplot(121),plt.imshow(x),plt.axis('off')
"""