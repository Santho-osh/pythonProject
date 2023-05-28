exampleList = [2, 6, 8, 12, 13, 15, 15, 15, 15, 15, 15, 17, 18, 22, 45, 68]

def binarySearchAlgorithm(alist: list, target: int):
    start= 0
    end = len(alist)-1
    return helperFunction(alist, target, start, end)
def helperFunction(alist, target, start, end):
    middle = (start + end)//2
    if start>end:
        return alist[start]
    if alist[middle] == target:
        return middle
    elif alist[middle] > target:
        return helperFunction(alist, target, start, end= middle-1)
    else:
        start = middle+1
        return helperFunction(alist, target, start, end)



print(binarySearchAlgorithm(exampleList, 14))