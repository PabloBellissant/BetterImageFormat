import random


# From 10,11,12,14,15,16,18 ↦ 10-2,14-2,18


def simplify(list): # Private !
    list.append(99999)
    betterList = []
    i = 0
    while i < len(list)-1:
        betterList.append(list[i])
        changeValue = 0
        go = True
        while list[i]+1 == list[i+1] and go == True:
            changeValue += 1
            i += 1
            if(i > len(list)-1): go = False
        if changeValue != 0:
            if(changeValue == 1): betterList[len(betterList)-1] = str(list[i-changeValue])+"-"
            else : betterList[len(betterList)-1] = str(list[i-changeValue])+"-"+str(changeValue-2)
        i+=1
    list.pop(len(list)-1)
    return betterList


def developpe(list): # Private !
    newList = []
    for i in range(len(list)):
        if(str(list[i]).__contains__("-")):
            value = list[i][:list[i].index("-")]

            if(list[i].index("-") == len(list[i])-1):
                valueAfter = 2
            else:
                valueAfter = int(list[i][list[i].index("-")+1:])+3

            for p in range(int(valueAfter)):
                newList.append(int(value)+p)

        else : newList.append(list[i])
    return newList




def smooth(txt):
    txtColor = txt[2]
    for color in range(len(txtColor)):
        for intensity in range(len(txtColor[color])):
            actualIntensity = list(txtColor[color].keys())[intensity]
            attributePixels = txtColor[color][actualIntensity]
            smoothPixel = simplify(attributePixels)
            txtColor[color].update({actualIntensity:smoothPixel})

    finalList = [txt[0],txt[1],txtColor]
    return finalList



def unSmooth(txt):
    txtColor = txt[2]
    for color in range(len(txtColor)):
        for intensity in range(len(txtColor[color])):
            actualIntensity = list(txtColor[color].keys())[intensity]
            attributePixels = txtColor[color][actualIntensity]
            DeveloppePixel = developpe(attributePixels)
            txtColor[color].update({actualIntensity:DeveloppePixel})
    finalList = [txt[0], txt[1], txtColor]
    return finalList