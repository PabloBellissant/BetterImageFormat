from PIL.Image import *
from A_jpgToTxt import unBuild
from A_jpgToTxt import build
from B_TxtToColorPixel import simplify
from B_TxtToColorPixel import complexify
from C_ColorPixelToColorGroup import colorization
from C_ColorPixelToColorGroup import deColorization
from D_smoothPixel import smooth
from D_smoothPixel import unSmooth
from F_toCompactestList import toList
from F_toCompactestList import reverseList


image = open("imagebis.jpg")
image = unBuild(image)
#print("1", image)
image = simplify(image)
#print("2", image)
image = colorization(image)
#print("3", image)
image = smooth(image)
#print("4", image)
image = toList(image)
print("5", image)
image = reverseList(image)

image = unSmooth(image)

image = deColorization(image)

image = complexify(image)

image = build(image)



#image = unSmooth(image)
#print("5", image)


#image = deColorization(image)

#image = complexify(image)

#image = build(image)
