a = [15, 32, 26, 11, 36, 19, 42, 44, 14]

def selectionSort(alist):

    n = 0
    for j in range(len(alist)):
        min = n
        for i in range(n, len(alist)):
            if alist[i] <= alist[min]:
                min = i
        if n < len(alist):
            n += 1

        alist[j], alist[min] = alist[min], alist[j]
    return alist



print(selectionSort(a))
