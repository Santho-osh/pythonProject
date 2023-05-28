alist =[3, 4, 5, 2, 3, 4, 2, 1]
def findDuplicates(alist):
    i = 0
    ans =[]
    while i < len(alist):
        correct = alist[i]-1
        if alist[i] != i+1:
            if alist[correct] != alist[i]:
                alist[correct], alist[i] = alist[i], alist[correct]
            else:
                ans.append(alist[i])
        i += 1
    return ans


print(findDuplicates(alist))

