from PIL import Image, ImageChops, ImageFilter
from matplotlib import pyplot as plt

path = 'camera.jpg'

x = Image.open('camera.jpg')

plt.imshow(x)
plt.axis('off')
plt.show()




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