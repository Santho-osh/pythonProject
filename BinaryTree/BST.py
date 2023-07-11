from collections import deque

class Node:


    def __init__(self, data, leftchild = None, rightchild = None):
        self.data = data
        self.leftchild = leftchild
        self.rightchild = rightchild

    def __str__(self):
        return f'{self.leftchild} - {self.data} - {self.rightchild}'


def insert(head, node):

    if head ==  None:
        return node
    if node.data <= head.data:
        head.leftchild = insert(head.leftchild, node)
    else:
        head.rightchild = insert(head.rightchild, node)

    return head

def print_tree(head):
    if head.leftchild:
        print_tree(head.leftchild)

    print(head.data)

    if head.rightchild:
        print_tree(head.rightchild)





# alist = [8, 5, 10, 3, 6, 9, 12]
# head = None
# for i in alist:
#         x = Node(i)
#         if head == None:
#             head = insert(None, x)
#         else:
#             insert(head, x)





root = Node(8)
A = Node(5)
B = Node(3)
C = Node(10)
D = Node(12)
E = Node(9)
F = Node(6)

head = insert(None, root)
insert(head, A)
insert(head, C)
insert(head, B)
insert(head, F)
insert(head, E)
insert(head, D)

q = []
q.append(head)
q.append(None)
while(len(q)>1):
    temp = q.pop(0)
    if temp == None:
        print()
        q.append(None)
        continue
    print(temp.data, end=' ')
    if(temp.leftchild!=None):
        q.append(temp.leftchild)
    if(temp.rightchild!=None):
        q.append(temp.rightchild)


# print(print_tree(head))
# # print(head)
# print(head.leftchild)
# print(head)
# print(head.rightchild)
#
# print(head.leftchild.leftchild)
# print(head.leftchild)
# print(head.leftchild.rightchild)
#
# print(head.rightchild.leftchild)
# print(head.rightchild)
# print(head.rightchild.rightchild)
