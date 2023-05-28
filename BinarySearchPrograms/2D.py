array2d = [[18, 9, 12],
           [36, -4, 91],
           [44, 33, 16]]

def search2darray(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == target:
                return i, j
    else:
        return -1

print(search2darray(array2d, 16))










