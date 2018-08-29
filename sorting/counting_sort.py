def counting_sort(arr):
    hi = max(arr)
    lo = min(arr)
    size = hi - lo + 1
    count = [0] * size

    for x in arr:
        count[x - lo] += 1

    return [i + lo for i in range(size) 
                   for _ in range(count[i])]
