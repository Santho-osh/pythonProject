class Node:

    def __init__(self, data = None, nextvalue = None):
        self.data = data
        self.nextvalue = nextvalue

    def __repr__(self):
        return self.data


class LinkedList:

    def __init__(self):
        self.head = None

    def __repr__(self):

        nodes = []
        current = self.head

        while current:
            nodes.append(repr(current))
            current = current.nextvalue

        return '[' + '->'.join(nodes) + ']'

    def prepend(self, data):
        self.head = Node(data= data, nextvalue= self.head)

    def append(self, data):
        if not self.head:
            self.head = Node(data= data)
            return

        current = self.head
        while current.nextvalue:
            current = current.nextvalue

        current.nextvalue = Node(data= data)

    def insert(self, data, middle = None):

        if middle is None:
            print('Data to insert after not specified')
            return

        current = self.head
        while current and current.data != middle:
            if current.nextvalue is None:
                newNode = Node(data= data)
                current.nextvalue = newNode
                return
            current = current.nextvalue

        newNode = Node(data= data)

        newNode.nextvalue = current.nextvalue
        current.nextvalue = newNode

    def find(self, data):
        current = self.head
        while current and current.data != data:
            current = current.nextvalue
        return current

    def remove(self, data):
        previous = None
        current = self.head

        while current and current.data != data:
            previous = current
            current = current.nextvalue

        if previous is None:
            self.head = current.nextvalue
        elif current:
            previous.nextvalue = current.nextvalue
            current.nextvalue = None

    def reverse(self):
        current = self.head
        previous = None
        next = None
        while current:
            next = current.nextvalue
            current.nextvalue = previous

            previous = current
            current = next

        self.head = previous



numbers = LinkedList()
numbers.append('2')
numbers.append('3')
numbers.prepend('1')
numbers.append('4')
numbers.append('5')
numbers.append('7')
numbers.insert('6', '5')
numbers.insert('8', '9')
print(numbers)
numbers.reverse()
print(numbers)












