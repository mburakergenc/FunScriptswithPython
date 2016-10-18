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

def recursiveBinarySearch(aList, item):
    first = 0
    last = len(aList) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if aList[mid] == item:
            return True
        else:
            if item < aList[mid]:
                return recursiveBinarySearch(aList[:mid], item)
            else:
                return recursiveBinarySearch(aList[mid + 1:], item)

l = [1,3,6,22,221,553,1233,123123,123543212,1231243512,3123123123123123123,45435345435345435345345345]
print(recursiveBinarySearch(l, 3123123123123123123))


def interpolationSearch(aList, item):
    min = 0
    max = len(aList) - 1
    while min <= max:
        scale = (item - aList[min]) // (aList[max] - aList[min])
        mid = min + (max-min) * scale
        if aList[mid] == item:
            return mid
        elif aList[mid] < item:
            min = mid + 1
        else:
            max = mid - 1
    return -1

l = [1,3,6,22,221,553,1233,123123,123543212,1231243512,3123123123123123123,45435345435345435345345345]
print(interpolationSearch(l, 45435345435345435345345345))