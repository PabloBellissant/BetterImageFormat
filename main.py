from PIL.Image import *
from A_jpgToTxt import unBuild
from A_jpgToTxt import build
from B_TxtToColorPixel import simplify
from B_TxtToColorPixel import complexify
from C_ColorPixelToColorGroup import colorization
from C_ColorPixelToColorGroup import deColorization


image = open("image.jpg")
image = unBuild(image)
#print("1", image)
image = simplify(image)
#print("2", image)
image = colorization(image)
#print("3", image)

image = deColorization(image)
print("4", image)
image = complexify(image)
#print("5", image)
image = build(image)
