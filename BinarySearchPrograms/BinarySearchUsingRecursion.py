array = [12, 15, 22, 45, 56, 67, 78, 99, 130, 156]
#  index  0   1   2   3   4   5   6   7   8    9
def binarySearchUsingRecusion(array, target):
    start = 0
    end = len(array)-1
    return index(array, target, start, end)
def index(array, target, start, end):
    middle = end-start//2
    if start > end:
        return -1
    if target < array[middle]:
        return index(array, target, start, middle-1)
    elif target > array[middle]:
        return index(array, target, middle+1, end)
    else:
        return middle


print(binarySearchUsingRecusion(array, 200))























































