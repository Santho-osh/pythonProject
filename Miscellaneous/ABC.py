import abc

class A(abc.ABC):

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def something(self):
        pass

class B(A):

    def __init__(self, name):
        super().__init__(name)


obj = B('Santhosh')



