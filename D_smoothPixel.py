
# From 10,11,12,14,15,16,18 ↦ 10-2,14-2,18

def smooth(txt):
    finalValue = []
    for color in range(3):
        for i in range(len(txt[2][color])):
            getIn = list(txt[2][0].values())[i]
            getIn.append(9999999)
            value = 0
            littleOutput = []
            for fullIn in range(len(getIn)-1):
                if(getIn[fullIn]+1 == getIn[fullIn+1]):
                    value +=1
                else:
                    if(value == 0): littleOutput.append(getIn[fullIn])
                    else:
                        littleOutput.append(str(getIn[fullIn-value])+"-"+str(value))
                        value = 0
            finalValue.append(littleOutput)
    return finalValue



def unSmooth(txt):
    print()


