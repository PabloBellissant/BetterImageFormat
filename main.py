from PIL.Image import *
from A_jpgToTxt import unBuild
from A_jpgToTxt import build
from B_TxtToColorPixel import simplify
from B_TxtToColorPixel import complexify
from C_ColorPixelToColorGroup import colorization
from C_ColorPixelToColorGroup import deColorization
from D_smoothPixel import smooth
from D_smoothPixel import unSmooth
from E_toDeductedPixel import compile
from E_toDeductedPixel import unCompile
from F_toCompactestList import toList
from F_toCompactestList import reverseList


image = open("imageg.jpg")
image = unBuild(image)
#print("1", image)
image = simplify(image)
#print("2", image)
image = colorization(image)
#print("3", image)
image = smooth(image)
print("__4", image)
image = compile(image)
print("5", image)
image = toList(image)
print("6", image)
image = reverseList(image)
print("7", image)
image = unCompile(image)
print("__8", image)
image = unSmooth(image)

image = deColorization(image)

image = complexify(image)

image = build(image)



#image = unSmooth(image)
#print("5", image)


#image = deColorization(image)

#image = complexify(image)

#image = build(image)
