def bubble_sort(arr):
    rn = len(arr)
    swapping = True
    while swapping:
        swapping = False
        for i in range(1, rn):
            if arr[i - 1] > arr[i]:
                swapping = True
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        rn -= 1
    return arr
