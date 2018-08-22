def quick_sort(arr, lo, hi):
    pivot = arr[hi]
    p = lo

    if lo < hi:
        for i in range(lo, hi):
            if arr[i] < pivot:
                arr[p], arr[i] = arr[i], arr[p]
                p += 1

        arr[p], arr[hi] = arr[hi], arr[p]
        quick_sort(arr, lo, p - 1)
        quick_sort(arr, p + 1, hi)

    return arr
