def selection_sort(arr):
    indices = range(len(arr))

    for i in indices:
        minIdx = i

        for ii in indices[i + 1:]:
            if arr[ii] < arr[minIdx]:
                minIdx = ii

        if minIdx != i:
            arr[i], arr[minIdx] = arr[minIdx], arr[i]

    return arr
