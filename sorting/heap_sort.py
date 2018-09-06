def heapify(arr, i, count):
    hi = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < count and arr[i] < arr[l]:
        hi = l

    if r < count and arr[hi] < arr[r]:
        hi = r

    if hi != i:
        arr[i], arr[hi] = arr[hi], arr[i]
        heapify(arr, hi, count)

def heap_sort(arr):
    count = len(arr)

    for i in range(count, -1, -1):
        heapify(arr, i, count)

    for i in range(count - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)

    return arr
