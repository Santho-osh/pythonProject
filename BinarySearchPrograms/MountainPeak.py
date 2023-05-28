array = [1, 2, 5, 7, 10, 4, 3,]
def binSearch(arr):
    start = 0

    end = len(arr)-1
while start <= end:
        middle = start + (end-start)//2
        if start == end:
            return arr[start]
        elif arr[middle] < arr[middle+1]:
            start = middle+1
        elif arr[middle] > arr[middle+1]:
            end = middle
        else:
            return -1



print(binSearch(array))




