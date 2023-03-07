from D_smoothPixel import developpe



def getNumberOfPixel(listt): # Private !
    toList = list(listt[2][0].values())
    BetterList = []
    for p in range(len(toList)):
        for i in range(len(toList[p])):
            BetterList.append(toList[p][i])
    return len(developpe(BetterList))


def toContinusStr(list, char = "_"): # Private !
    return char.join([str(x) for x in list])




def toList(lst):
    betterInput = []
    valuesColorSliced = []
    for color in range(3):
        for p in range(len(lst[2][color])):
            keys = list(lst[2][color].keys())[p]
            lst[2][color][keys] = str(keys) + "_" + toContinusStr(lst[2][color][keys])


        valuesColorSliced.append(toContinusStr(list(lst[2][color].values()), "/"))
    values = toContinusStr(valuesColorSliced,"/-")


    newLst = str(lst[0]) +"_"+ values


    return newLst

def reverseList(string):
    first = string[:string.index("_")]
    valueRest = "/"+string[string.index("_")+1:]
    print(valueRest)

    dic = {}
    colorList = [valueRest[:valueRest.index("/-")], valueRest[valueRest.index("/-")+2:]]
    print("wow", colorList)
    for i in range(valueRest.count("/")):
        valueRest = valueRest[1:]
        if(valueRest.__contains__("/")):
            insideValue = valueRest[:valueRest.index("/")]
            valueRest = valueRest[valueRest.index("/"):]

        else:
            insideValue = valueRest
            print("here", insideValue)

        preciseKey = insideValue[:insideValue.index("_")]
        dic[preciseKey] = insideValue[insideValue.index("_")+1:]
    print(dic)






    return


listt = [17, 26, {0: {0: ['70-59', 138, 155], 136: ['142-', '153-', '156-41'], 153: ['25-', 45, 64], 237: ['132-3', '139-0', '144-6'], 255: ['0-22', '27-15', '46-15', '65-2', '200-239']}, 1: {0: ['70-59', 138, '142-', '153-44'], 28: ['132-3', '139-0', '144-6'], 217: ['25-', 45, 64], 255: ['0-22', '27-15', '46-15', '65-2', '200-239']}, 2: {0: ['70-59', 138, 155], 21: ['142-', '153-', '156-41'], 36: ['132-3', '139-0', '144-6'], 234: ['25-', 45, 64], 255: ['0-22', '27-15', '46-15', '65-2', '200-239']}}]
print(listt)
whatList = toList(listt)
print(whatList)
reverseList(whatList)