def searchRange(nums, target):
    ans = [-1, -1]
    startindex = search(nums, target, True)
    endindex = search(nums, target, False)
    ans[0] = startindex
    ans[1] = endindex
    return ans
def search(nums, target, first_index):
    ans = -1
    start = 0
    end = len(nums)-1
    while start <= end:
        middle = end-start//2
        if target < nums[middle]:
            end = middle - 1
        elif target > nums[middle]:
            start = middle + 1
        else:
            ans = middle
            if first_index:
                end = middle - 1
            else:
                start = middle + 1
    return ans


nums = [5, 7, 7, 8, 8, 8, 8, 9, 10]
print(searchRange(nums, 7))


