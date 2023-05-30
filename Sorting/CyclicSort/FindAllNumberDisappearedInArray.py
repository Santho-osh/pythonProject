def allmissingNumber(nums):
    i = 0
    ans = []
    while i < len(nums):
        correct = nums[i] -1
        if correct < len(nums) and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i+1:
            ans.append(i+1)
        else:
            continue
    return ans

nums = [4,3,2,7,8,2,3,1]
print(allmissingNumber(nums))

