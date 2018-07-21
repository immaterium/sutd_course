
# ver 2
class Graph:
    def __init__(self):
        self._vertices = {}
        self._num_vertices = 0

    @property
    def num_vertices(self):
        return self._num_vertices

    def increase_num_vertices(self, val):
        self._num_vertices += val

    @property
    def vertices(self):
        return self._vertices
    
    def add_vertex(self, key):
        self.vertices[key] = Vertex(key)
        self.increase_num_vertices(1)

    def add_edge(self, start, end, weight=None):
        start.add_neighbour(end, weight)

    def get_vertex(self, key):
        return self.vertices.get(key, None)

    def get_vertices(self):
        return self.vertices

class Vertex:
    def __init__(self, key):
        self._key = key
        self._connected_to = {}

    @property
    def key(self):
        return self._key

    @property
    def connected_to(self):
        return self._connected_to

    def add_neighbour(self, vertex, weight=0):
        self.connected_to[vertex] = weight

    def get_connections(self):
        return list(self.connected_to.keys())

    def get_key(self):
        return self._key

    def get_weight(self, neighbour):
        return self.connected_to.get(neighbour, 'No such neighbour')

    def __str__(self):
        connections = self.get_connections()
        remainder = ""
        for v in connections:
            remainder += '{},'.format(v.key)
        return "Vertex {} is connected to {}.".format(self._key, remainder[:-1])

class VertexSearch(Vertex):
    def __init__(self, key, distance=0, predecessor=None, color='white'):
        super().__init__(key)
        self._distance = distance
        self._predecessor = predecessor
        self._color = color

    @property
    def distance(self):
        return self._distance
    
    @distance.setter
    def distance(self, val):
        self.distance = val

    @property
    def predecessor(self):
        return self._predecessor

    @predecessor.setter
    def predecessor(self, val):
        self.predecessor = val

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, val):
        self.color = val
    
    def __lt__(self, other):
        return self.key < other.key 

class GraphSearch(Graph):
    def __init__(self):
        super().__init__()

    def add_vertex(self, key):
        self.vertices[key] = VertexSearch(key)
        self.increase_num_vertices(1)

class GraphSearchUndirected(GraphSearch):
    def __init__(self):
        super().__init__()

    def add_edge(self, v1, v2, weight=0):
        v1.add_neighbour(v2, weight)
        v2.add_neighbour(v1, weight)


def test_graph():
    g = Graph()
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)
    g.add_vertex(0)

    g.add_edge(g.get_vertex(0), g.get_vertex(1), 5)
    g.add_edge(g.get_vertex(1), g.get_vertex(2), 4)
    g.add_edge(g.get_vertex(5), g.get_vertex(2), 1)
    g.add_edge(g.get_vertex(2), g.get_vertex(3), 9)
    g.add_edge(g.get_vertex(3), g.get_vertex(4), 7)
    g.add_edge(g.get_vertex(5), g.get_vertex(4), 8)
    g.add_edge(g.get_vertex(5), g.get_vertex(0), 1)
    g.add_edge(g.get_vertex(3), g.get_vertex(5), 3)
    
    print(g.get_vertices())
    print(g.get_vertex(0))
    print(g.get_vertex(1))
    print(g.get_vertex(2))
    print(g.get_vertex(3))
    print(g.get_vertex(4))
    print(g.get_vertex(5))

def test_GS():
    g = GraphSearch()
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)
    g.add_vertex(0)

    g.add_edge(g.get_vertex(0), g.get_vertex(1), 5)
    g.add_edge(g.get_vertex(1), g.get_vertex(2), 4)
    g.add_edge(g.get_vertex(5), g.get_vertex(2), 1)
    g.add_edge(g.get_vertex(2), g.get_vertex(3), 9)
    g.add_edge(g.get_vertex(3), g.get_vertex(4), 7)
    g.add_edge(g.get_vertex(5), g.get_vertex(4), 8)
    g.add_edge(g.get_vertex(5), g.get_vertex(0), 1)
    g.add_edge(g.get_vertex(3), g.get_vertex(5), 3)

    print(g.get_vertices())
    print(g.get_vertex(0))
    print(g.get_vertex(1))
    print(g.get_vertex(2))
    print(g.get_vertex(3))
    print(g.get_vertex(4))
    print(g.get_vertex(5))

def test_UGS():
    g = GraphSearchUndirected()
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)
    g.add_vertex(0)

    g.add_edge(g.get_vertex(0), g.get_vertex(1), 5)
    g.add_edge(g.get_vertex(1), g.get_vertex(2), 4)
    g.add_edge(g.get_vertex(5), g.get_vertex(2), 1)
    g.add_edge(g.get_vertex(2), g.get_vertex(3), 9)
    g.add_edge(g.get_vertex(3), g.get_vertex(4), 7)
    g.add_edge(g.get_vertex(5), g.get_vertex(4), 8)
    g.add_edge(g.get_vertex(5), g.get_vertex(0), 1)
    g.add_edge(g.get_vertex(3), g.get_vertex(5), 3)

    print(g.get_vertices())
    print(g.get_vertex(0))
    print(g.get_vertex(1))
    print(g.get_vertex(2))
    print(g.get_vertex(3))
    print(g.get_vertex(4))
    print(g.get_vertex(5))

# ver 1
# class Graph:

#     def __init__(self, vertices, num_vertices):
#         self.vertices = {}
#         self.num_vertices = 0

#     def add_vertex(self, vertex):
#         self.num_vertices += 1
#         self.vertices[key] = Vertex(key)

#     def add_edge(self, from_v, to_v):
#         if from_v not in self.vertices


#     def add_edge(self, from_v, to_v, weight):
#         if from_v not in self.vertices:
#             self.add_vertex

#     def get_vertex(self, key):
#         if key in self.vertices:
#             return self.vertices[key]
#         else:
#             return None

#     def get_vertices(self):
        

#     def __contains__(key):
#         return key in self.vertices

#     def __iter__():
#         return iter(self.vertices.values())

# class Vertex:

#     def __init__(self, key, connected_to):
#         self.key = key
#         self.connected_to = {}

#     def add_neighbour(self, to_v, weight=0):
#         self.connected_to[to_v] = weight

#     def get_connections(self):
#         return self.connected_to.keys()

#     def get_key(self):
#         return self.get_key

#     def get_weight(self, neighbour_v):
#         return self.connected_to[neighbour_v]

#     def __str__():
#         return "Vertex {} is connected to ".format(self.key) + str([k.key for k in self.connected_to])







