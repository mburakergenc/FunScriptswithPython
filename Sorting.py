def bubbleSort(aList):
    for passNum in range(len(aList) - 1, 0, -1):
        for i in range(passNum):
            if aList[i] > aList[i+1]:
                temp = aList[i]
                aList[i] = aList[i+1]
                aList[i + 1] = temp

aList = [54,26,93,17,77,31,44,55,20]
bubbleSort(aList)
print(aList)


def shortBubbleSort(aList):
    exchanges = True
    pass_num = len(aList) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if aList[i] > aList[i+1]:
                exchanges = True
                temp = aList[i]
                aList[i] = aList[i+1]
                aList[i+1] = temp
        pass_num -= 1

aList = [54,26,93,17,77,31,44,55,20]
shortBubbleSort(aList)
print(aList)


def selectionSort(aList):
    for fillSlot in range(len(aList)-1, 0, -1):
        posOfMax = 0
        for location in range(1, fillSlot+1):
            if aList[location] > aList[posOfMax]:
                posOfMax = location
        temp = aList[fillSlot]
        aList[fillSlot] = aList[posOfMax]
        aList[posOfMax] = temp

aList = [54,26,93,17,77,31,44,55,20]
selectionSort(aList)
print(aList)

