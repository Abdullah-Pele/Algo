import heapq
import sys

class MinHeap:

    def __init__(self, li=[]):
        self.list = li
        self.size = 0
        heapq.heapify(self.list)

    def __iter__(self):
        return iter(self.list)

    def add(self, num):
        heapq.heappush(self.list, num)
        self.size += 1

    def poll(self):
        self.size -= 1
        return heapq.heappop(self.list)

    def peek(self):
        return self.list[0]

    def __len__(self):
        return len(self.list)

    def is_empty(self):
        return self.__len__() == 0

    def __str__(self):
        return self.list


class Edge:

    def __init__(self, frm, to, weight = 0):
        self.frm    = frm
        self.to     = to
        self.weight = weight

    def fromEdge(self):
        return self.frm

    def to(self):
        return self.to

    def weight(self):
        return self.weight

    def __str__(self):
        return str(self.frm) + " -> " + str(self.to) + " : " + str(self.weight)


class Vertex:

    def __init__(self,  name, prev=None, dist=None):
        self.name = name
        self.prev = prev
        self.dist = dist
        self.visit = False

    def set_distance(self, dist):
        self.dist = dist

    def set_prev(self, prev):
        self.prev = prev

    def get_distance(self):
        return self.dist

    def visited(self):
        self.visit = True

    def is_visited(self):
        return self.visit

    def get_prev(self):
        return self.prev


class Graph:

    def __init__(self):
        self.vertices_adj = dict()
        self.vertex_id    = []
        self.vertex_names = dict()
        self.size         = 0
        self.edges        = []

        # adding a vertex
    def add_vertex(self, name):
        self.vertices_adj[name] = dict()
        self.vertex_names[name] = self.size
        self.vertex_id.append(name)
        self.size += 1

    def get_vertex_id(self,name):
        return self.vertex_names[name]

    def get_vertex_name(self, idd):
        return self.vertex_id[idd]

        # adding an edge to the dictionary.
    def add_edge(self, frm, to, weight):
        # because it's an undirected graph we two edges.
        self.vertices_adj[frm][to] = weight
        self.vertices_adj[to][frm] = weight

        # adding a the edge to the list for Kruskal Algorithm
        self.edges.append(weight)


        # getting a vertex neighbors.
    def adj(self, v):
        return self.vertices_adj[v]

    def get_edge(self, frm, to):
        return self.vertices_adj[frm][to]

    def get_prev_value(self, prevList, disList, value):
        x = self.get_vertex_id[value]
        prev = prevList[x]
        return disList[prev]

    def dijkstra(self, start, target):
        prev    = []
        visited = [False] * self.size
        pq = MinHeap()
        fromTo = dict()
        distanceTo = dict()

        for name in self.vertex_id:
            fromTo[name] = sys.maxsize

        for i in range(self.size):
            prev.append(i)

        fromTo[start] = 0
        distanceTo[0] = start
        pq.add(0)
        vert = start
        print("from \t to \t weight")

        while not pq.is_empty() :
            minmum   = pq.poll()
            vert     = distanceTo[minmum]
            if target == vert:
                break
            print(start+" \t "+ vert + "\t = " +str(minmum))

            adjacent = self.adj(vert)
            index = self.get_vertex_id(vert)

            if visited[index]:
                continue

            for neighbor in adjacent:
                edge   = self.get_edge(vert, neighbor)
                wieght_of_path = fromTo[vert]

                if fromTo[neighbor] > edge+wieght_of_path:
                    formerValue = fromTo[neighbor]
                    fromTo[neighbor] = edge+wieght_of_path
                    nIndex = self.get_vertex_id(neighbor)
                    prev[nIndex] = index
                    if formerValue in distanceTo:
                        del distanceTo[formerValue]
                        distanceTo[edge+wieght_of_path] = neighbor
                        pq.add(edge+wieght_of_path)
                    else:
                        distanceTo[edge+wieght_of_path] = neighbor
                        pq.add(edge+wieght_of_path)

            visited[index] = True
        print(prev)
        print(fromTo)
        print(distanceTo)


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

g.dijkstra("BWI", "DFW")
