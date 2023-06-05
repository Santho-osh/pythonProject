# arr = [1, 3, 5, 6, 7, 9]
arr = [3, 4, 7, 1, 2, 9, 5]

# def search(arr, target):
#     start = 0
#     end = len(arr)-1
#     while start <= end:
#         middle = start + (end-start)//2
#         if target == arr[middle]:
#             return middle
#         elif target < arr[middle]:
#             end = middle -1
#         else:
#             start = middle +1
#     else:
#         return -1
#
# print(search(arr, 1))

def bubbleSortPractice(arr):
    for i in range(len(arr)-1):
        for j in range(1, len(arr)-i):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                continue

bubbleSortPractice(arr)
print(arr)


