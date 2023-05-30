alist = [5,4,6,7,9,3,10,9,5,6]
def findDuplicates(nums):
    i = 0
    ans =[]
    while i < len(nums):

        if nums[i] != i+1:
            correct = nums[i] - 1
            if nums[correct] != nums[i]:
                nums[correct], nums[i] = nums[i], nums[correct]
            else:

                i += 1
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i+1:
            ans.append(nums[i])

    return ans








print(findDuplicates(alist))
print(alist)

