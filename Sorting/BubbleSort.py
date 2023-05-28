# l1= [3, 1, 5, 4, 2, 7, 9, 6, 8]
l1=[1,2,3,4,5]
rangee = len(l1)-1

for _ in range(len(l1)-1):
    swap = 0
    for i in range(rangee):
        if l1[i] > l1[i+1]:
            l1[i], l1[i+1] = l1[i+1], l1[i]
            swap+=1
        else:
            continue
    if swap==0:
        print('Already sorted')
        break
    rangee -= 1

print(l1)








