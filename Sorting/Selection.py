def maxindex(alist, start, end):
    max = start
    for i in range(start, end+1):
        if(alist[max] < alist[i]):
            max=i
    return max

def selectionSort(alist):
    for i in range(len(alist)):
        lastindex = len(alist)-i-1
        maxIndex = maxindex(alist, 0, lastindex)
        alist[maxIndex], alist[lastindex] = alist[lastindex], alist[maxIndex]


alist = [9, 8, 7, 6, 5, 4, 3, 2, 1]
selectionSort(alist)
print(alist)










