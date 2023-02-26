
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
    fullList = [[],[],[]]
    fullDictList = [{},{},{}]
    for y in range(3): # from [{80:[0,2],90:[1]}] ↦ [{0:80,2:80,1:90}]
        i = 0
        while len(fullList[y]) < totalPixel:
            for p in range(len(withoutSize[y][list(withoutSize[y])[i]])):
                fullList[y].append(withoutSize[y][list(withoutSize[y])[i]][p])
                fullDictList[y][withoutSize[y][list(withoutSize[y])[i]][p]] = list(withoutSize[y].keys())[list(withoutSize[y].values()).index(withoutSize[y][list(withoutSize[y])[i]])]
            i+=1

    print(",",fullDictList)
    buildList = []
    for color in range(3):
        for allPixel in range(totalPixel):
            if(color == 0): buildList.append([fullDictList[color].get(allPixel)])
            else: buildList[allPixel].append(fullDictList[color].get(allPixel))


    for i in range(len(buildList)): #Convert all list to tuple
        buildList[i] = tuple(buildList[i])

    buildList.insert(0, txt[1]) # add size of image
    buildList.insert(0, txt[0])
    return buildList


