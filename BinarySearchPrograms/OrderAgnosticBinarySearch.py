def orderAgnosticBinarySearch(alist, target):
    start = 0
    end = len(alist)-1
    isAsc = alist[start] < alist[end]

    while start <= end:
        middle = start + (end-start)//2
        if isAsc:
            if target < alist[middle]:
                end = middle-1
            elif target > alist[middle]:
                start = middle+1
            else:
                return middle
        else:
            if target > alist[middle]:
                end = middle-1
            elif target < alist[middle]:
                start = middle+1
            else:
                return middle
    return -1


print(orderAgnosticBinarySearch([5, 4, 3, 2, 1], 5))

