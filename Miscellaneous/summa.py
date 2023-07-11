alist = [2, 5, 6, 7, 9, 10, 13, 15, 18]


def binarySearchTest(alist, num):
    start = 0
    end = len(alist) - 1
    while(start < end):
        mid = start + (end-start)//2
        if alist[mid] == num:
            return True
        if num < alist[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False

print(binarySearchTest(alist, 20))

