a = [15, 32, 26, 11, 36, 19, 42, 44, 14]
b = ['san','bhar','tar','keer','kar']
# def selectionsort(alist):
#
#     for i in range(len(alist)):
#         min_index = i
#
#         for j in range(i+1, len(alist)):
#             if alist[min_index] > alist[j]:
#                 min_index = j
#
#         alist[min_index], alist[i] = alist[i], alist[min_index]
#
#     return alist
#
# print(selectionsort(b))

def bubble(alist):
    for i in range(len(alist)):
        for j in range(1, len(alist)):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]

    return alist

print(bubble(a))

def bubble_efficient(alist):

    for i in range(len(alist)-1, 0, -1):
        for j in range(1, i):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]

    return alist

print(bubble_efficient(a))

def insertion(alist):
    for i in range(len(alist)-1):

        for j in range(i+1, 0, -1):

            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]


    return alist

print(insertion(a))




