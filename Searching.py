def sequentialSearch(aList, item):
    pos = 0
    found = False

    while pos < len(aList) and not found:
        if aList[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found

l = [1,2,5,134,23412312,3213,4523,12,3213,123123123123123123,123123123,123123123]
print(sequentialSearch(l, 123123123))

def orderedSequentialSearch(aList, item):
    pos = 0
    found = False
    stop = False
    while pos < len(aList) and not found and not stop:
        if aList[pos] == item:
            found = True
        else:
            if aList[pos] > item:
                stop = True
            else:
                pos += 1
    return found


def binarySearch(aList, item):
    first = 0
    last = len(aList) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if aList[mid] == item:
            found = True
        else:
            if item < aList[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

l = [1,3,7,12,22,99,233,9239,213213123,123123584359123]
print(binarySearch(l, 213213123))


# Binary Search with Recursion

def RecursiveBinarySearch(aList, item):
    first = 0
    last = len(aList) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if aList[mid] == item:
            return True
        else:
            if item < aList[mid]:
                return RecursiveBinarySearch(aList[:mid], item)
            else:
                return RecursiveBinarySearch(aList[mid + 1:], item)

l = [1,3,6,22,221,553,1233,123123,123543212,1231243512,3123123123123123123,45435345435345435345345345]
print(binarySearch(l, 3123123123123123123))