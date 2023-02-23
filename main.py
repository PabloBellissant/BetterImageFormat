from PIL.Image import *
from A_jpgToTxt import unBuild
from A_jpgToTxt import build
from B_TxtToColorPixel import simplify
from B_TxtToColorPixel import complexify


image = open("image.jpg")
image = unBuild(image)
print(image)
image = simplify(image)
print(image)
image = complexify(image)
print(image)
image = build(image)