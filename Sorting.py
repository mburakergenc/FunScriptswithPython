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


def insertionSort(aList):
    for i in range(1,len(aList)):
        currValue = aList[i]
        pos = i
        while pos > 0 and aList[pos-1] > currValue:
            aList[pos] = aList[pos-1]
            pos -= 1
        aList[pos] = currValue

aList = [54,26,93,17,77,31,44,55,20]
insertionSort(aList)
print(aList)


def shellSort(aList):
    sublist_count = len(aList) // 2
    while sublist_count > 0:
        for startPosition in range(sublist_count):
            gapInsertionSort(aList, startPosition, sublist_count)

        print("After increments of size", sublist_count, "The list is", aList)

        sublist_count = sublist_count // 2


def gapInsertionSort(aList, start, gap):
    for i in range(start + gap, len(aList), gap):
        currentValue = aList[i]
        position = i

        while position >= gap and aList[position-gap] > currentValue:
            aList[position] = aList[position-gap]
            position = position - gap

        aList[position] = currentValue

aList = [54,26,93,17,77,31,44,55,20]
shellSort(aList)
print(aList)


def mergeSort(aList):
    print ("Splitting ", aList)
    if len(aList) > 1:
        mid = len(aList) // 2
        left_half = aList[:mid]
        right_half = aList[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                aList[k] = left_half[i]
                i += 1
            else:
                aList[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            aList[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            aList[k] = right_half[j]
            j += 1
            k += 1

    print("Merging ", aList)

aList = [54,26,93,17,77,31,44,55,20, 12]
mergeSort(aList)
print(aList)
