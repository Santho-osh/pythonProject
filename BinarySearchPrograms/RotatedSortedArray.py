
def search(nums, target):
    pivot = findPivot(nums, target)
    tillpivot = binarySearch(nums, target, 0, pivot)
    frompivot = binarySearch(nums, target, pivot+1, len(nums)-1)
    if tillpivot != -1:
        return tillpivot
    else:
        return frompivot


def findPivot(nums, target):
    start = 0
    end = len(nums)-1
    while start < end:
        middle = (start+end)>>1
        if nums[middle]>nums[middle+1]:
            return middle
        if nums[middle]<nums[middle-1]:
            return middle-1
        if nums[middle] > nums[start]:
            start = middle+1
        else:
            end = middle-1
    return -1

def binarySearch(nums, target, start, end):

    while start <= end:
        middle = (start + end) >> 1
        if target > nums[middle]:
            start = middle+1
        elif target < nums[middle]:
            end = middle-1
        else:
            return middle

    return -1


nums= [4,5,6,7,0,1,2]
print(search(nums, 0))