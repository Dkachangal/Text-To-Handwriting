from PIL import Image
import os

from mainFront import page, characters

for i in page:
    print(f"page: {page[i]}")

for i in characters:
    print(f"char: {characters[i]}")

ch = 'a'
if ch=='a':
    print(characters['a'])