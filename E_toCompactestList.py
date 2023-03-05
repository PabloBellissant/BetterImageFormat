


def toList(list):
    print(list)
    newList = str(list[0])+"/"+str(list[1])+str(list[2])



    return newList

def reverseList(str):
    newStr = "["+str[:str.index("/")]+", "+str[str.index("/")+1:]+"]"
    newStr = newStr[:newStr.index("{")]+", "+newStr[newStr.index("{"):]
    newStr = eval(newStr)





    return newStr

list = [4, 2, {0: {0: ['1-2'], 63: [0], 237: ['6-']}, 1: {0: ['1-2'], 28: ['6-'], 72: [0]}, 2: {0: ['1-2'], 36: ['6-'], 204: [0]}}]
whatList = toList(list)
print(whatList)
print(list)
print(reverseList(whatList),"   ---REVERSE---   ")
