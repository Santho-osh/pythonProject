import abc
import numpy as np

class Graph(abc.ABC):

    def __init__(self, totalVertices, directed = False):
        self.totalVertices = totalVertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass

    @abc.abstractmethod
    def get_indegree(self, v):
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass

    @abc.abstractmethod
    def display(self):
        pass

class AdjacencyMatrixGraph(Graph):
    def __init__(self, totalVertices, directed = False):
        super().__init__(totalVertices, directed)
        self.matrix = np.zeros((totalVertices, totalVertices))

    def add_edge(self, v1, v2, weight = 1):
        if v1 >= self.totalVertices or v2 >= self.totalVertices or v1 < 0 or v2 < 0:
            raise ValueError(f'Vertices {v1} and {v2} are out of bounds')

        if weight < 0:
            raise ValueError('An edge cannot have weight < 1')

        self.matrix[v1][v2] = weight

        if self.directed == False:
            self.matrix[v2][v1] = weight

    def get_adjacent_vertices(self, v):
        if v >= self.totalVertices or v < 0:
            raise ValueError(f'Cannot access Vertex {v}')

        adjacent_vertices = []
        for i in range(self.totalVertices):
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)
        return adjacent_vertices

    def get_indegree(self, v):
        if v >= self.totalVertices or v < 0:
            raise ValueError(f'Cannot access Vertex {v}')

        indegree = 0
        for i in range(self.totalVertices):
            if self.matrix[i][v] > 0:
                indegree = indegree+1

        return indegree

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.totalVertices):
            for v in self.get_adjacent_vertices(i):
                print(i, '-->', v)


g = AdjacencyMatrixGraph(4)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)

for i in range(4):
    print(f'Adjacent vertices of {i} are {g.get_adjacent_vertices(i)}')

for i in range(4):
    print(f'{i} has an indegree of {g.get_indegree(i)}')

for i in range(4):
    for j in g.get_adjacent_vertices(i):
        print(f'Weight between {i}, {j} is {g.get_edge_weight(i, j)}')

g.display()




