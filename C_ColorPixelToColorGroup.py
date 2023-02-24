
# From [(80,90,100)] to {0:{80:[0]},1:{90:[0]},2:{100:[0]}}


def colorization(txt):
    newList = {0:{},1:{},2:{}}
    txt = list(txt)
    for color in range(3):
        actualColorDict = {}
        for p in range(256): #power of color
            for n in range(len(txt)-2): #number of pixels.
                if(txt[n+2][color] == p): # If actual pixel = color
                    if(p in newList[color]):
                        newList[color][p].append(n+2)

                    else:
                        newList[color][p] = [n]
    newList = [txt[0],txt[1],newList]
    return newList






def deColorization(txt):
    totalPixel = txt[0] * txt[1]
    withoutSize = txt[2]
    print(withoutSize[1])
    print(withoutSize[1][0])
    for color in range(3):
        for actualPixel in range(totalPixel-1):
            print(color, )

