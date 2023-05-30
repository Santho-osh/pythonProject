def setMismatch(nums):
    i = 0
    while i < len(nums):
        correct = nums[i]-1
        if nums[correct] != nums[i]:
            nums[correct], nums[i] = nums[i], nums[correct]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i+1:
            return [nums[i], i+1]

nums = [1, 2, 2, 4]

print(setMismatch(nums))
print(nums)














