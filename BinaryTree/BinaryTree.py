class Node:
    def __init__(self, data):
        self.data = data

        self.left = None
        self.right = None

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()

        print(self.data)

        if self.right:
            self.right.print_tree()

def insert(head, node):
    if head == None:
        return node
    if node.get_data() <= head.get_data():
        head.set_left(insert(head.get_left(), node))
    else:
        head.set_right(insert(head.get_right(), node))
    return head

A=Node(45)
B=Node(2)
C=Node(33)
D=Node(54)
E=Node(25)
F=Node(68)
G=Node(72)
H=Node(81)
I=Node(23)

head = insert(None, E)

print(head)

insert(head, B)
head.print_tree()






















