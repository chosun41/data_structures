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

    def setPrevious(self, current):
        self.previous = current

    def getPrevious(self, current):
        return self.previous

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

    def setPrevious(self, current):
        self.previous = current

    def getPrevious(self, current):
        return self.previous

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
            