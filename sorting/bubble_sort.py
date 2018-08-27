def bubble_sort(arr, swaps=0):
    for i, x in enumerate(arr):
        if i < len(arr) - 1:
            if arr[i + 1] < x:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1

    return arr if swaps == 0 else bubble_sort(arr) 
