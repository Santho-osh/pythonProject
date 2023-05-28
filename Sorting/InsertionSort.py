alist = [5, 3, 4, 1, 2]

def insertionSort(alist):
    for i in range(0, len(alist)-1): #or (1, len(alist))
        for j in range(i+1, 0, -1): #or (i, 0, -1)
            if(alist[j] < alist[j-1]):
                alist[j], alist[j-1] = alist[j-1], alist[j]
            else:
                break

insertionSort(alist)
print(alist)

