a = [15, 32, 26, 11, 36, 19, 42, 44, 14]

def bubble(alist):

    for i in range(len(alist)):
        for j in range(1, len(alist)-i):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]

    return alist

print(bubble(a))