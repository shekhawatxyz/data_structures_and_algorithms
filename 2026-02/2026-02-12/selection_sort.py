def selection_sort(nums):
    for i in range(len(nums)):
        smallest_idx = i
        for j in range(i + 1, len(nums)):
            print(j, nums[j])
            print(smallest_idx, nums)
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
    return nums


nums = [3, 1, 5, 2, 9, 7]
print(selection_sort(nums))
