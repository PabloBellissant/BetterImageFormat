
# From [[(100,100,100),(90,89,194)],[(45,59,0),(49,114,86)]] to [(100,100,100),(90,89,194),(45,59,0),(49,114,86)]



def simplify(pixelList):
    fullList = [len(pixelList[0]), len(pixelList)]
    for i in range(len(pixelList)):
        for p in range(len(pixelList[i])):
            fullList.append(pixelList[i][p])
    return fullList


def complexify(pixelSimpleList):

    fullList = []
    actual = 1
    for i in range(pixelSimpleList[0]):
        complexList = []

        for p in range(pixelSimpleList[1]):
            actual +=1
            complexList.append(pixelSimpleList[actual])
        fullList.append(complexList)
    return fullList
