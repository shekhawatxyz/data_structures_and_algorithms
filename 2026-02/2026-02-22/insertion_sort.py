def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1
    return nums


n = [5, 2, 4, 6, 1, 3]
print(insertion_sort(n))
