nums = [1, 2, 4, 3, 5, 6, 7, 10, 9, 8]
for i in range(1, len(nums)):
    j = i
    while j > 0 and nums[j - 1] > nums[j]:
        nums[j - 1], nums[j] = nums[j], nums[j - 1]
        j -= 1
print(nums)
