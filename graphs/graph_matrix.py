class Vertex:
    def __init__(self, node):
        self.id = node
        # Mark all nodes unvisited        
        self.visited = False  

    def addNeighbor(self, neighbor, G):
        G.addEdge(self.id, neighbor)

    def getConnections(self, G):
        return G.adjMatrix[self.id]

    def getVertexID(self):
        return self.id

    def setVertexID(self, id):
        self.id = id

#     def setVisited(self):
#         self.visited = True

#     def __str__(self):
#         return str(self.id)
    
# undirected graph
class Graph:
    
    def __init__(self, numVertices, cost=0):
        # 2d matrix V*V
        self.adjMatrix = [[-1] * numVertices for _ in range(numVertices)]
        self.numVertices = numVertices
        self.vertices = []
        for i in range(0, numVertices):
            newVertex = Vertex(i)
            self.vertices.append(newVertex)

    def setVertex(self, vtx, id):
        if 0 <= vtx < self.numVertices:
            self.vertices[vtx].setVertexID(id)

    def getVertex(self, n):
        for vertxin in range(0, self.numVertices):
            if self.vertices[vertxin].getVertexID() == n:
                return vertxin       
        return -1

    def addEdge(self, frm, to, cost=0): 
        if self.getVertex(frm) != -1 and self.getVertex(to) != -1:
            self.adjMatrix[self.getVertex(frm)][self.getVertex(to)] = cost
            # For directed graph do not add this
            self.adjMatrix[self.getVertex(to)][self.getVertex(frm)] = cost  

    def getVertices(self):
        vertices = []
        for vertxin in range(0, self.numVertices):
            vertices.append(self.vertices[vertxin].getVertexID())
        return vertices

    def printMatrix(self):
        for u in range(0, self.numVertices):
            row = []
            for v in range(0, self.numVertices):
                row.append(self.adjMatrix[u][v])
            print(row)

    def getEdges(self):
        edges = []
        for u in range(0, self.numVertices):
            for v in range(0, self.numVertices):
                if self.adjMatrix[u][v] != -1:
                    vid = self.vertices[u].getVertexID()
                    wid = self.vertices[v].getVertexID()
                    edges.append((vid, wid, self.adjMatrix[u][v]))
        return edges

# directed graph
class DiGraph:
    
    def __init__(self, numVertices, cost=0):
        # 2d matrix V*V
        self.adjMatrix = [[-1] * numVertices for _ in range(numVertices)]
        self.numVertices = numVertices
        self.vertices = []
        for i in range(0, numVertices):
            newVertex = Vertex(i)
            self.vertices.append(newVertex)

    def setVertex(self, vtx, id):
        if 0 <= vtx < self.numVertices:
            self.vertices[vtx].setVertexID(id)

    def getVertex(self, n):
        for vertxin in range(0, self.numVertices):
            if self.vertices[vertxin].getVertexID() == n:
                return vertxin       
        return -1

    def addEdge(self, frm, to, cost=0): 
        if self.getVertex(frm) != -1 and self.getVertex(to) != -1:
            self.adjMatrix[self.getVertex(frm)][self.getVertex(to)] = cost 

    def getVertices(self):
        vertices = []
        for vertxin in range(0, self.numVertices):
            vertices.append(self.vertices[vertxin].getVertexID())
        return vertices

    def printMatrix(self):
        for u in range(0, self.numVertices):
            row = []
            for v in range(0, self.numVertices):
                row.append(self.adjMatrix[u][v])
            print(row)

    def getEdges(self):
        edges = []
        for u in range(0, self.numVertices):
            for v in range(0, self.numVertices):
                if self.adjMatrix[u][v] != -1:
                    vid = self.vertices[u].getVertexID()
                    wid = self.vertices[v].getVertexID()
                    edges.append((vid, wid, self.adjMatrix[u][v]))
        return edges
    
if __name__ == '__main__':
    G = Graph(5)
    G.setVertex(0, 'a')
    G.setVertex(1, 'b')
    G.setVertex(2, 'c')
    G.setVertex(3, 'd')
    G.setVertex(4, 'e')
    print('Graph data:')  
    G.addEdge('a', 'e', 10)  
    G.addEdge('a', 'c', 20)
    G.addEdge('c', 'b', 30)
    G.addEdge('b', 'e', 40)
    G.addEdge('e', 'd', 50)
    G.addEdge('f', 'e', 60)
    G.printMatrix()      
    print(G.getEdges())

# # adjacency matrix is sparse so it takes up more memory than needed

# # undirected graph
# class Graph:

#     # Initialize the matrix
#     def __init__(self, size):
#         self.adjMatrix = []
#         for i in range(size):
#             self.adjMatrix.append([0 for i in range(size)])
#         self.size = size

#     # Add edges
#     def add_edge(self, v1, v2):
#         if v1 == v2:
#             print("Same vertex %d and %d" % (v1, v2))
#         self.adjMatrix[v1][v2] = 1
#         self.adjMatrix[v2][v1] = 1

#     # Remove edges
#     def remove_edge(self, v1, v2):
#         if self.adjMatrix[v1][v2] == 0:
#             print("No edge between %d and %d" % (v1, v2))
#             return
#         self.adjMatrix[v1][v2] = 0
#         self.adjMatrix[v2][v1] = 0

#     def __len__(self):
#         return self.size

#     # Print the matrix
#     def print_matrix(self):
#         for row in self.adjMatrix:
#             print(row)
            
# # directed graph           
# class DiGraph:

#     # Initialize the matrix
#     def __init__(self, size):
#         self.adjMatrix = []
#         for i in range(size):
#             self.adjMatrix.append([0 for i in range(size)])
#         self.size = size

#     # Add edges
#     def add_edge(self, v1, v2):
#         if v1 == v2:
#             print("Same vertex %d and %d" % (v1, v2))
#         self.adjMatrix[v1][v2] = 1

#     # Remove edges
#     def remove_edge(self, v1, v2):
#         if self.adjMatrix[v1][v2] == 0:
#             print("No edge between %d and %d" % (v1, v2))
#             return
#         self.adjMatrix[v1][v2] = 0

#     def __len__(self):
#         return self.size

#     # Print the matrix
#     def print_matrix(self):
#         for row in self.adjMatrix:
#             print(row)

# if __name__ == '__main__':
#     g = Graph(5)
#     g.add_edge(0, 1)
#     g.add_edge(0, 2)
#     g.add_edge(1, 2)
#     g.add_edge(2, 0)
#     g.add_edge(2, 3)

#     g.print_matrix()