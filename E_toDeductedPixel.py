# From 10,19,21,25,36 ↦ 10,9,1,5,36

import random

def deductableValue(firstValue, value): # "1458", "1465" ↦ 5 PRIVATE

    memFirstVal = "" # Memory ( -x)
    memVal = ""
    if(firstValue.__contains__("-")) :
        memFirstVal = firstValue[firstValue.index("-"):]
        firstValue = firstValue[:firstValue.index("-")]
    if (value.__contains__("-")):
        memVal = value[value.index("-"):]
        value = value[:value.index("-")]


    while(len(firstValue) < len(value)): firstValue = "0" + firstValue     # Both input has same length at this point



    for i in range(len(value)):
        if(firstValue[i] != value[i]):
            valueIns = value[i:]
            lenChange = len(valueIns)-1
            if(int(firstValue) + 10**lenChange >= int(value)): return valueIns[1:]
            else: return value[i:]
            break



    firstValue = firstValue + memFirstVal
    value = value + memVal
    if(value.isdigit()) : value = int(value)

    return value

print(deductableValue("1136", "1147"))


def getDeductValue(firstValue, value): # PRIVATE

    memFirstVal = ""  # Memory ( -x)
    memVal = ""
    if (firstValue.__contains__("-")):
        memFirstVal = firstValue[firstValue.index("-"):]
        firstValue = firstValue[:firstValue.index("-")]
    if (value.__contains__("-")):
        memVal = value[value.index("-"):]
        value = value[:value.index("-")]




    finalValue = int(firstValue[:-len(value)]+value)

    if (firstValue[len(firstValue) - len(value)] == value[0]):
        firstValue = str(int(firstValue) + 10 ** len(value))
        print("a")


    while(finalValue < int(firstValue)):
        print("dbd")
        finalValue += int(10**len(value))


    while(len(str(finalValue)) < len(value) and int(firstValue)+10 >= int(value)):
        print("cac")
        finalValue = "1"+str(finalValue)



    firstValue = firstValue + memFirstVal
    value = value + memVal
    finalValue = str(finalValue) + memVal

    if (finalValue.isdigit()): finalValue = int(finalValue)

    return finalValue




def compile(txt):
    inputDic = txt[2]
    extDico = {}
    for color in range(3):
        dico = inputDic[color]
        for i in range(len(dico)):
            key = list(dico.keys())[i]
            values = list(dico.values())[i]

            for p in range(len(values)-1):
                oposite = len(values)-1-p
                values[oposite] = deductableValue(str(values[oposite-1]), str(values[oposite]))

            dico[key] = values
        extDico[color] = dico
    outputList = [txt[0],txt[1],extDico]

    return outputList


def unCompile(txt):
    inputDic = txt[2]
    extDico = {}
    for color in range(3):
        dico = inputDic[color]
        for i in range(len(dico)):
            key = list(dico.keys())[i]
            values = list(dico.values())[i]

            for p in range(len(values)-1):
                values[p+1] = getDeductValue(str(values[p]), str(values[p+1]))

            dico[key] = values
        extDico[color] = dico
    outputList = [txt[0], txt[1], extDico]

    return outputList


