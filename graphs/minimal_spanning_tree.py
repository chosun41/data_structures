from graph_list import Graph,DiGraph
import heapdict 

# minimal spanning tree is a subgraph that contains all the vertices, but the total cost of edges is the minimum

# just extracts previous to a list
def shortest(v, path):
    if v.previous:
        path.insert(0,v.previous.getVertexID())
        shortest(v.previous, path)
    return

# pretty similar to dijkstra 
# time: O(V^2) without heaps and O(ElogV) using heaps
def Prims(G, source):
    
    # Set the distance for the source node to zero (from infinity)
    source.setDistance(0)
        
    # Put list pair into the priority queue (distance, vertex)
    # heapdict allows you to mimic a priority queue and easily update priorities w/o heapifying each time
    unvisitedQueue = heapdict.heapdict() 
    for v in G:
        unvisitedQueue[v.id]=v.getDistance()

    while unvisitedQueue:
        # Pops a vertex with the smallest distance 
        uv = unvisitedQueue.popitem()
        current=G.getVertex(uv[0])
        current.setVisited() # mark current as visited=True

        # for next in v.adjacent: every one of its neighbors
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            newDist = current.getDistance() + current.getWeight(next)

            # update adjacent distance if it is lower than the current vertex distance and also the previous vertex
            # that can be used later for the shortest path
            if newDist < next.getDistance():
                next.setDistance(newDist)
                next.setPrevious(current)
                unvisitedQueue[next.id] = newDist
                
                print('Updated : current = %s next = %s newDist = %s' \
                        % (current.getVertexID(), next.getVertexID(), next.getDistance()))
            else:
                print('Not updated : current = %s next = %s newDist = %s' \
                        % (current.getVertexID(), next.getVertexID(), next.getDistance()))

# using union and find operations
# time: O(ElogE)

# 1. create a sorted edge list by weight
# 2. create V trees
# 3. union trees if it doesn't create a cycle (doesn't have the same root)

parent = dict()
rank = dict()

def make_set(vertice):
    # set parent to itself and rank 0 to initialize
    # separate trees
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        # the tree with the higher rank becomes the parent
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: 
                rank[root2] += 1

def kruskal(G):
    
    # create an edge list of (weight, vertice1, vertice2) and sort
    edges = []
    for v in G:
        make_set(v.getVertexID())
        for w in v.getConnections():
            vid = v.getVertexID()
            wid = w.getVertexID()
            edges.append((v.getWeight(w), vid, wid))
    edges.sort()
    
    # recursively search for parent
    # if the parent of the two vertexes are not the same, union them and add to the spanningtree
    minimumSpanningTree = set()	
    
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimumSpanningTree.add(edge)
    return minimumSpanningTree
    
if __name__ == '__main__':

    # Prim
    G = Graph()
    G.addEdge("A", "B", 7)
    G.addEdge("A", "D", 5)
    G.addEdge("B", "C", 8)
    G.addEdge("B", "D", 9)
    G.addEdge("B", "E", 7)
    G.addEdge("C", "E", 5)
    G.addEdge("D", "E", 15)
    G.addEdge("D", "F", 6)
    G.addEdge("E", "F", 8)
    G.addEdge("E", "G", 9)
    G.addEdge("F", "G", 11)
    
    print('Graph data:')
    for v in G:
        for w in v.getConnections():
            vid = v.getVertexID()
            wid = w.getVertexID()
            print('( %s , %s, %3d)' % (vid, wid, v.getWeight(w)))

    source = G.getVertex('A')
    Prims(G, source) 
 
    for v in G.vertDictionary.values():
        print(source.getVertexID(), " to ", v.getVertexID(), "-->", v.getDistance())
        
    print("\n")
        
    for v in G.vertDictionary.values():
        if v.previous:
            print(v.previous.getVertexID(), " to ", v.getVertexID(), "-->", v.getDistance())

    # Kruskal
    G = Graph()
    G.addEdge('A', 'C', 7)
    G.addEdge('A', 'D', 5)
    G.addEdge('D', 'C', 9)
    G.addEdge('D', 'E', 15)
    G.addEdge('C', 'E', 7)
    G.addEdge('C', 'B', 8)
    G.addEdge('B', 'E', 5)
    G.addEdge('E', 'F', 8)
    G.addEdge('D', 'F', 6)
    G.addEdge('F', 'G', 11)
    G.addEdge('E', 'G', 9)
    
    print('Graph data:')
    for v in G:
        for w in v.getConnections():
            vid = v.getVertexID()
            wid = w.getVertexID()
            print('( %s , %s, %3d)' % (vid, wid, v.getWeight(w)))

    print(kruskal(G))