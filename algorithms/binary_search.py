def binary_search(target, arr):
    high = len(arr) - 1
    low = 0
    while low <= high:
        median = (low + high) // 2
        if arr[median] == target:
            return median
        elif target > arr[median]:
            low = median + 1
        elif target < arr[median]:
            high = median - 1
    return False


l = [1, 7, 12, 13, 30, 42, 54, 71, 99]
# l.reverse()
print(l)
# n = 13
print(binary_search(30, l))
