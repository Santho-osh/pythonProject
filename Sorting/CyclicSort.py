alist = [3, 5, 2, 1, 4]

def cyclicSort(alist):
    while (alist[0] != 1):
        value = alist[0]
        if(value-1 == 0):
            continue
        else:
            alist[0], alist[value-1] = alist[value-1], alist[0]



cyclicSort(alist)
print(alist)







