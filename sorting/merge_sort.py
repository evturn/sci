def merge_sort(arr):
    l = len(arr)

    if l <= 1:
        return arr

    mid = l // 2
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right, res=[]):
    while len(left) > 0 and len(right) > 0:
        l = left[0] 
        r = right[0]
        if l <= r:
            res.append(l)
            left = left[1:]
        else:
            res.append(r)
            right = right[1:]

    return res + left + right
