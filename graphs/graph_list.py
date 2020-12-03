class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = float('infinity')
        # Mark all nodes unvisited        
        self.visited = False  
        # Predecessor
        self.previous = None

    def __lt__(self, other):
        return self.distance < other.distance
    
    def __gt__(self, other):
        return self.distance > other.distance

    def addNeighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def getConnections(self):
        return self.adjacent.keys()  

    def getVertexID(self):
        return self.id

    def getWeight(self, neighbor):
        return self.adjacent[neighbor]

    def setDistance(self, dist):
        self.distance = dist

    def getDistance(self):
        return self.distance

    def setPrevious(self, prev):
        self.previous = prev

    def setVisited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])
    
# undirected graph
class Graph:
    def __init__(self):
        self.vertDictionary = {}
        self.numVertices = 0

    # allows you to iterate through the graph vertices
    def __iter__(self):
        return iter(self.vertDictionary.values())

    def addVertex(self, node):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(node)
        self.vertDictionary[node] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertDictionary:
            return self.vertDictionary[n]
        else:
            return None

    def addEdge(self, frm, to, cost=0):
        if frm not in self.vertDictionary:
            self.addVertex(frm)
        if to not in self.vertDictionary:
            self.addVertex(to)

        self.vertDictionary[frm].addNeighbor(self.vertDictionary[to], cost)
        # For directed graph do not add this
        self.vertDictionary[to].addNeighbor(self.vertDictionary[frm], cost)

    def getVertices(self):
        return self.vertDictionary.keys()

#     def setPrevious(self, current):
#         self.previous = current

#     def getPrevious(self, current):
#         return self.previous

    def getEdges(self):
        edges = []
        for v in self:
            for w in v.getConnections():
                vid = v.getVertexID()
                wid = w.getVertexID()
                edges.append((vid, wid, v.getWeight(w)))
        return edges
    
# directed graph
class DiGraph:
    def __init__(self):
        
        # dictionary of vertex objects
        self.vertDictionary = {}
        self.numVertices = 0

    # allows you to iterate through the graph vertices
    def __iter__(self):
        return iter(self.vertDictionary.values())

    def addVertex(self, node):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(node)
        self.vertDictionary[node] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertDictionary:
            return self.vertDictionary[n]
        else:
            return None

    def addEdge(self, frm, to, cost=0):
        if frm not in self.vertDictionary:
            self.addVertex(frm)
        if to not in self.vertDictionary:
            self.addVertex(to)

        self.vertDictionary[frm].addNeighbor(self.vertDictionary[to], cost)

    def getVertices(self):
        return self.vertDictionary.keys()

#     def setPrevious(self, current):
#         self.previous = current

#     def getPrevious(self, current):
#         return self.previous

    def getEdges(self):
        edges = []
        for v in self:
            for w in v.getConnections():
                vid = v.getVertexID()
                wid = w.getVertexID()
                edges.append((vid, wid, v.getWeight(w)))
        return edges
    
if __name__ == '__main__':

    G = Graph()
    G.addEdge('a', 'b', 4)  
    G.addEdge('a', 'c', 1)
    G.addEdge('c', 'b', 2)
    G.addEdge('b', 'e', 4)
    G.addEdge('c', 'd', 4)
    G.addEdge('d', 'e', 4)

    print('Graph data:')
    print(G.getEdges())

# class AdjNode:
#     def __init__(self, value):
#         self.vertex = value
#         self.next = None

# class Graph:
#     def __init__(self, num):
#         self.V = num
#         self.graph = [None] * self.V

#     # Add edges
#     def add_edge(self, s, d):
#         node = AdjNode(d)
#         node.next = self.graph[s]
#         self.graph[s] = node

#         node = AdjNode(s)
#         node.next = self.graph[d]
#         self.graph[d] = node

#     # Print the graph
#     def print_agraph(self):
#         for i in range(self.V):
#             print("Vertex " + str(i) + ":", end="")
#             temp = self.graph[i]
#             while temp:
#                 print(" -> {}".format(temp.vertex), end="")
#                 temp = temp.next
#             print(" \n")


# if __name__ == "__main__":
    
#     V = 5

#     # Create graph and edges
#     graph = Graph(V)
#     graph.add_edge(0, 1)
#     graph.add_edge(0, 2)
#     graph.add_edge(0, 3)
#     graph.add_edge(1, 2)

#     graph.print_agraph()
            
            