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

def toConcractLst(string):
    newStr = string.split("_")
    for i in range(len(newStr)):
        if(str(newStr[i]).isdigit()) : newStr[i] = int(newStr[i])
    return newStr





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
    valueKeep = string[string.index("_")+1:]


    dic = {}

    for color in range(3):
        valueRest = valueKeep.split("/-")[color]
        insideDic = {}
        insideList = valueRest.split("/")

        for i in range(len(insideList)): # Dictionary Builder
            keyList = int(insideList[i][:insideList[i].index("_")])
            insideDic[keyList] = toConcractLst(insideList[i][insideList[i].index("_")+1:])

        dic[color] = insideDic


    returnString = [int(string[:string.index("_")]), "TO REPLACE", dic]
    returnString[1] = int(getNumberOfPixel(returnString)/returnString[0])
    print(returnString)











    return


listt = [17, 26, {0: {0: ['70-59', 138, 155], 136: ['142-', '153-', '156-41'], 153: ['25-', 45, 64], 237: ['132-3', '139-0', '144-6'], 255: ['0-22', '27-15', '46-15', '65-2', '200-239']}, 1: {0: ['70-59', 138, '142-', '153-44'], 28: ['132-3', '139-0', '144-6'], 217: ['25-', 45, 64], 255: ['0-22', '27-15', '46-15', '65-2', '200-239']}, 2: {0: ['70-59', 138, 155], 21: ['142-', '153-', '156-41'], 36: ['132-3', '139-0', '144-6'], 234: ['25-', 45, 64], 255: ['0-22', '27-15', '46-15', '65-2', '200-239']}}]
print(listt)
whatList = toList(listt)
print(whatList)
reverseList(whatList)

# {0: {0: ['70-59', 138, 155], 136: ['142-', '153-', '156-41'], 153: ['25-', 45, 64], 237: ['132-3', '139-0', '144-6'], 255: ['0-22', '27-15', '46-15', '65-2', '200-239']}, 1: {0: ['70-59', 138, '142-', '153-44'], 28: ['132-3', '139-0', '144-6'], 217: ['25-', 45, 64], 255: ['0-22', '27-15', '46-15', '65-2', '200-239']}, 2: {0: ['70-59', 138, 155], 21: ['142-', '153-', '156-41'], 36: ['132-3', '139-0', '144-6'], 234: ['25-', 45, 64], 255: ['0-22', '27-15', '46-15', '65-2', '200-239']}}
# {0: {0: ['70-59', 138, 155], 136: ['142-', '153-', '156-41'], 153: ['25-', 45, 64], 237: ['132-3', '139-0', '144-6'], 255: ['0-22', '27-15', '46-15', '65-2', '200-239']}, 1: {0: ['70-59', 138, '142-', '153-44'], 28: ['132-3', '139-0', '144-6'], 217: ['25-', 45, 64], 255: ['0-22', '27-15', '46-15', '65-2', '200-239']}, 2: {0: ['70-59', 138, 155], 21: ['142-', '153-', '156-41'], 36: ['132-3', '139-0', '144-6'], 234: ['25-', 45, 64], 255: ['0-22', '27-15', '46-15', '65-2', '200-239']}}