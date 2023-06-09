class CustomQueue:

    def __init__(self):
        self.queue = []
        self.size = 0


    def put(self, value):
        self.queue.append(value)
        self.size += 1

    def get(self):
        self.size -= 1
        return self.queue.pop(0)

    def getSize(self):
        return self.size

qu = CustomQueue()
qu.put(5)
qu.put(6)
qu.put(7)
print(qu.get())
print(qu.getSize())
