import sys

class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        self.vertices[key] = Vertex(key)

    def get_vertex(self, key):
        if key in self.vertices:
            return self.vertices[key]

        else:
            return None

    def __contains__(self, key):
        return key in self.vertices

    def get_vertices(self):
        return self.vertices.keys()

    def add_edge(self, from_v, to_v, weight = 0):
        if from_v not in self.vertices:
            self.add_vertex(from_v)
        if to_v not in self.vertices:
            self.add_vertex(to_v)
        self.vertices[from_v].add_neighbour(self.vertices[to_v], weight)

    def __iter__(self):
        return iter(self.vertices.values())

class Vertex:
    def __init__(self, key):
        self.key = key
        self.connected_to = {}

    def add_neighbour(self, to_v, weight=0):
        self.connected_to[to_v] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def get_key(self):
        return self.key

    def get_weight(self, neighbour_v):
        return self.connected_to[neighbour_v]

    def __str__(self):
        return "Vertex {} is connected to ".format(self.key) +str([k.key for k in self.connected_to])

class VertexSearch(Vertex):
    def __init__(self, key):
        super().__init__(key)
        self._distance = sys.maxsize
        self._predecessor = 0
        self._color = 'white'

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, d):
        if d >= 0:
            self._distance = d

    @property
    def predecessor(self):
        return self._predecessor

    @predecessor.setter
    def predecessor(self, p):
        if isinstance(p, VertexSearch) or p == None:
            self._predecessor = p

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, c):
        if c in ('white', 'grey', 'black'):
            self._color = c

    def __lt__(self, other):
        return self.key < other.key

class GraphSearch(Graph):
    def add_vertex(self, key):
        self.num_vertices += 1
        self.vertices[key] = VertexSearch(key)

class GraphSearchUndirected(GraphSearch):
    def add_edge(self, v1, v2, weight = 0):
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)
        self.vertices[v1].add_neighbour(self.vertices[v2], weight)
        self.vertices[v2].add_neighbour(self.vertices[v1], weight)

from queue import Queue

graph = GraphSearchUndirected()
graph.add_edge('u', 'v')
graph.add_edge('u', 'x')
graph.add_edge('v', 'x')
graph.add_edge('v', 'w')
graph.add_edge('x', 'w')
graph.add_edge('x', 'y')
graph.add_edge('w', 'y')
graph.add_edge('w', 'z')
graph.add_edge('y', 'z')
print(graph.get_vertices())
for v in graph:
	print(v.key, 'connected to', [v.key for v in v.get_connections()])


def bfs(graph,start_n):
    start_n.distance = 0
    to_process_list = Queue()
    to_process_list.put(start_n)
    # print(start_n.distance)
    # print (to_process_list.queue[0].key)
    while not to_process_list.empty():
        cur_node = to_process_list.get()
        # print(cur_node.key)
        neighbours = cur_node.get_connections()
        for neighbour in neighbours:
            # print (neighbour.key)
            if neighbour.color == 'white':
                neighbour.color = 'grey'
                # print(cur_node.distance)
                neighbour.distance = cur_node.distance + 1
                neighbour.predecessor = cur_node
                to_process_list.put(neighbour)
            cur_node.color = 'black' 


bfs(graph, graph.get_vertex('u'))

assert graph.get_vertex('w').distance == 2
assert graph.get_vertex('z').distance == 3

# print (find_path(graph.get_vertex('z')))

    # def find_path(end_n):
    #     path = [end_n.key]
    #     node = end_n
    #     while node.predecessor:
    #         path.insert(0, node.key)
    #         node = node.predecessor
    #     path.insert(0, node.key)
    #     return path

def findPath(end_n):
    path = [end_n.key]
    node = end_n
    while node.predecessor:
        node = node.predecessor
        path.insert(0, node.key)
    return path

bfs(graph, graph.get_vertex('u'))
assert graph.get_vertex('w').distance == 2

print (findPath(graph.get_vertex('z')))