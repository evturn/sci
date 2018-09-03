from random import randint

def partition(arr, left, right, pivotIdx):
    pivotVal = arr[pivotIdx]
    arr[pivotIdx], arr[right] = arr[right], arr[pivotIdx]
    currIdx = left

    for i in range(left, right):
        x = arr[i]
        if x < pivotVal:
            arr[currIdx], arr[i] = arr[i], arr[currIdx]
            currIdx += 1

    arr[right], arr[currIdx] = arr[currIdx], arr[right]
    return currIdx

def quickselect(arr, left, right, k):
    if left == right:
        return arr[left]

    idx = randint(left, right)
    pivotIdx = partition(arr, left, right, idx)

    if k == pivotIdx:
        return arr[k]
    elif k < pivotIdx:
        return quickselect(arr, left, pivotIdx - 1, k)
    else:
        return quickselect(arr, pivotIdx + 1, right, k)
