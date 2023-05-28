# def message():
#     print('Hello world')
#     message1()
#
# def message1():
#     print('Hello world')
#     message2()
#
# def message2():
#     print('Hello world')
#     message3()
#
# def message3():
#     print('Hello world')
#
# message()

# def fib(n):
#     alist = [0, 1]
#     def fibseries(fib(), prev=0, curr=1):
#         while n != len(alist):
#             nth = alist[curr] + alist[prev]
#             alist.append(nth)
#             prev += 1
#             curr += 1
#             fibseries(prev, curr)
#         return alist
#     return fibseries()
#
# print(fib(10))

# def nth_fib_number(n:int):
#     if n < 2:
#         return n
#     return nth_fib_number(n-1)+nth_fib_number(n-2)
#
# print(nth_fib_number(8))


# def binarysearch(alist, target):
#     start = 0
#     end = len(alist) - 1
#     while True:
#         middle = start + (end - start) // 2
#         if alist[middle] == target:
#             return middle
#         elif target < alist[middle]:
#             end = middle - 1
#         else:
#             start = middle + 1
#
#
# alist = [1,2,3,4,5,6,7,8,9]
# print(binarysearch(alist, 9))

# def print1ton(n):
#     if n == 0:
#         return
#     print1ton(n-1)
#     print(n)
#
#
# print1ton(6)

# def fact(n):
#     if n == 1:
#         return n
#     facto = n * fact(n-1)
#     return facto
#
# print(fact(5))


# revSum = 0
# def revNum(n):
#     global revSum
#     if n == 0:
#         return
#     revSum = (revSum * 10)+(n % 10)
#     revNum(n // 10)
#
# revNum(3579)
# print(revSum)
import math
# def rev2(n, base=None):
#     if n%10 == n:
#         return n
#     rem = n % 10
#     # q = n // 10
#     base = int(math.log(n, 10))
#     return rem * (10 ** base) + rev2(n // 10, base)
#
# print(rev2(3579))

# print(int(math.log(3579, 10))+1)

# def numberOfSteps(num):
#     return help(num, 0)
#
# def help(num, steps):
#     if(num==0):
#         return steps
#     if(num%2==0):
#         return help(num//2, steps+1)
#     return help(num-1, steps+1)
#
# print(numberOfSteps(14))

# def ifSorted(alist):
#     return help(alist, 0)
# def help(alist, index):
#     if index == len(alist)-1:
#         return True
#     if alist[index] < alist[index+1]:
#         return help(alist, index+1)
#     else:
#         return False
#
# print(ifSorted([1,2,3,5,4]))


alist = [1,3,4,4,5,6,4,7]
# def linearSearch(alist, target):
#     """Linear Search using Recursion"""
#     return help(alist, target, 0, [])
#
# def help(alist, target, index, anotherList):
#     if index == len(alist):
#         return anotherList
#     if alist[index] == target:
#         anotherList.append(index)
#     return help(alist, target, index+1, anotherList)
#
# print(linearSearch(alist, 4))

def findAllIndex(alist, target, index):
    ansList = []
    if index == len(alist):
        return ansList;
    if alist[index] == target:
        ansList.append(index)
    ansFromBelowCalls = findAllIndex(alist, target, index+1)
    ansList.extend(ansFromBelowCalls)
    return ansList

print(findAllIndex(alist, 4, 0))

# num = 12
# print(len(list(str(num))))
#
# print(math.log(9999, 10))








