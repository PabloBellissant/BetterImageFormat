# From 10,19,21,25,36 ↦ 10,9,1,5,36


def deductableValue(firstValue, value): # "1458", "1465" ↦ 5

    while(len(firstValue) < len(value)): firstValue = "0"+firstValue     # Both input has same lengh at this point

    for i in range(len(value)):
        if(firstValue[i] != value[i]):
            valInside = i
            if(valInside+1 < len(value) and valInside+1 < len(firstValue)):
                if(int(firstValue[valInside]) + 1 == int(value[valInside]) and int(firstValue[valInside+1]) >= int(value[valInside+1])) :
                    valInside += 1
            value = value[valInside:]
            break
    return value


def getDeductValue(firstValue, value):


    print(firstValue[:len(value)])

getDeductValue(27,)



