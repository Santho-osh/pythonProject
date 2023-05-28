array = [12, 15, 22, 45, 56, 67, 78, 99, 130, 156]

def binSearch(array, target):
    start = 0
    end = len(array)-1
    while start <= end:
        middle = end-start//2
        if target < array[middle]:
            end = middle-1
        elif target > array[middle]:
            start = middle+1
        else:
            return middle

    return -1

print(binSearch(array, 200))








