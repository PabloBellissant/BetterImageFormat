
# From image to [[(100,100,100),(90,89,194)],[(45,59,0),(49,114,86)]]



from PIL import Image
import numpy as np

def unBuild(image = open("image.jpg")):

    width, height = image.size
    openedImage = []
    for i in range(height):
        actualLine = []
        for p in range(width):
            actualLine.append(image.getpixel((p, i)))
        openedImage.append(actualLine)
    return openedImage

def build(str):
    array = np.array(str, dtype=np.uint8)
    new_image = Image.fromarray(array)
    new_image.save('new.png')
    print("Image build")