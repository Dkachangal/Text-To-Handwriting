from PIL import Image, ImageChops, ImageFilter
from matplotlib import pyplot as plt

path = 'camera.jpg'

x = Image.open("camera.jpg")
a =  Image.open('frog.jpg')

# x.thumbnail((500, 500))
x.show()



plt.imshow(x)
plt.show()

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