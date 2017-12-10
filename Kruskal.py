class UnionFind:

    def __init__(self, nums):
        self.our_list = [0] * nums
        for i in range(nums):
            self.our_list[i] = i

    def root(self, v):
        while v != self.our_list[v]:
            self.our_list[v] = self.our_list[self.our_list[v]]
            v = self.our_list[v]

        return v

    def are_connected(self, vertex, node):
        return self.root(vertex) == self.root(node)

    def union(self, v, n):
        i = self.root(v)
        j = self.root(n)
        self.our_list[i] = j


class Graph:

    def __init__(self):
        # self.vertices_adj = dict()
        self.vertex_id    = []
        self.vertex_names = dict()
        self.size         = 0
        self.edges        = []
        self.edges_and_ref = dict()

        # adding a vertex
    def add_vertex(self, name):
        self.vertex_names[name] = self.size
        self.vertex_id.append(name)
        self.size += 1

    def get_vertex_id(self, name):
        return self.vertex_names[name]

    def get_vertex_name(self, idd):
        return self.vertex_id[idd]

    def get_connected_nodes(self, weight):
        return self.edges_and_ref[weight]

        # adding an edge to the dictionary.
    def add_edge(self, frm, to, weight):
        # adding a the edge to the list for Kruskal Algorithm
        self.edges.append(weight)

        self.edges_and_ref[weight] = [frm, to]


    def kruskal(self):
        UF = UnionFind(self.size)
        self.edges.sort()
        minimum_spanning_tree = []
        counter = 1
        for edge in self.edges:
            f , to = self.get_connected_nodes(edge)
            f_id  = self.get_vertex_id(f)
            to_id = self.get_vertex_id(to)

            if not UF.are_connected(f_id, to_id):
                UF.union(f_id, to_id)
                print('%d- Adding edge between %s -> %s : Weight = %d' %(counter, to, f, edge))
                counter += 1
                minimum_spanning_tree.append((f, to, edge))
            if counter == self.size:
                break

        return minimum_spanning_tree

g = Graph()
# adding vertecies
g.add_vertex('BOS')
g.add_vertex('PVD')
g.add_vertex('JFK')
g.add_vertex('BWI')
g.add_vertex('ORD')
g.add_vertex('MIA')
g.add_vertex('DFW')
g.add_vertex('SFO')
g.add_vertex('LAX')

# adding edges for Vertex BOS
g.add_edge('BOS', 'SFO', 2704)
g.add_edge('BOS', 'JFK', 187 )
g.add_edge('BOS', 'ORD', 867 )
g.add_edge('BOS', 'MIA', 1258)

# adding edges for Vertex PVD
g.add_edge('PVD', 'JFK', 144)
g.add_edge('PVD', 'ORD', 849)

# adding edges for Vertex DFW
g.add_edge('DFW', 'LAX', 1235)
g.add_edge('DFW', 'SFO', 1465)
g.add_edge('DFW', 'ORD', 802 )
g.add_edge('DFW', 'JFK', 1391)
g.add_edge('DFW', 'MIA', 1121)

# adding edges for Vertex BWI
g.add_edge('BWI', 'JFK', 184)
g.add_edge('BWI', 'ORD', 621)
g.add_edge('BWI', 'MIA', 946)

# adding edges for Vertex JFK
g.add_edge('JFK', 'ORD', 740)

# adding edges for Vertex ORD
g.add_edge('ORD', 'SFO', 1846)

# adding edges for Vertex MIA
g.add_edge('MIA', 'LAX', 2342)
g.add_edge('SFO', 'LAX', 337)

g.kruskal()
