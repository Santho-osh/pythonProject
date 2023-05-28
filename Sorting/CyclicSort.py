# alist = [5, 4, 3, 2, 1]
#
# def cyclicSort(alist):
#     i = 0
#     while i < len(alist):
#         correctIndex = alist[i]-1
#         if alist[i] != alist[correctIndex]:
#             alist[i], alist[correctIndex] = alist[correctIndex], alist[i]
#         else:
#             i += 1
#
# cyclicSort(alist)
# print(alist)

#https://leetcode.com/problems/missing-number/
nums = [9,6,4,2,3,5,7,0,1]
def missingNumber(nums):
    i = 0
    while i < len(nums):
        correct = nums[i]
        if correct < len(nums) and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i:
            return i
        else:
            continue
    return len(nums)


print(missingNumber(nums))








