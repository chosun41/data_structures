from graph_list import Graph,DiGraph
import heapdict 

# dijkstra shortest path algorithm along with heap
# time: O(E log V) b/c E edges and log V  for heap updates. if not with heap then O(E + V^2)
# requires 3 vertex attributes - distance, visited, and previous as well as comparison methods lt gt 
# (self,other) to allow heapify from heapq library
# can't handle negative edges, greedy algorithm that exhaustively searches all nodes and nearest neighbor of each vertex

# just extracts previous to a list
def shortest(v, path):
    if v.previous:
        path.insert(0,v.previous.getVertexID())
        shortest(v.previous, path)
    return

def dijkstra(G, source):
    
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
    
if __name__ == '__main__':

    # graph 1
    G = DiGraph()
    G.addEdge('a', 'b', 4)  
    G.addEdge('a', 'c', 1)
    G.addEdge('c', 'b', 2)
    G.addEdge('b', 'e', 4)
    G.addEdge('c', 'd', 4)
    G.addEdge('d', 'e', 4)

    print('Graph data:')
    for v in G:
        for w in v.getConnections():
            vid = v.getVertexID()
            wid = w.getVertexID()
            print('( %s , %s, %3d)' % (vid, wid, v.getWeight(w)))

    source = G.getVertex('a')
    destination = G.getVertex('e')    
    dijkstra(G, source) 

    for v in G.vertDictionary.values():
        print(source.getVertexID(), " to ", v.getVertexID(), "-->", v.getDistance())

    path = [destination.getVertexID()]
    shortest(destination, path)
    print('The shortest path from a to e is: %s' % (path)) # show in reverse
    
    # graph 2
    G = DiGraph()
    G.addEdge('a', 'b', 2)  
    G.addEdge('a', 'c', 5)  
    G.addEdge('a', 'f', 20)
    G.addEdge('b', 'e', 22)
    G.addEdge('b', 'd', 8)
    G.addEdge('c', 'g', 4)
    G.addEdge('d', 'e', 3)
    G.addEdge('d', 'c', 6)
    G.addEdge('e', 'h', 4)
    G.addEdge('f', 'c', 9)
    G.addEdge('f', 'h', 1)
    G.addEdge('g', 'f', 4)
    G.addEdge('g', 'h', 12)
    G.addEdge('h', 'd', 11)
    G.addEdge('h', 'e', 5)

    print('Graph data:')
    for v in G:
        for w in v.getConnections():
            vid = v.getVertexID()
            wid = w.getVertexID()
            print('( %s , %s, %3d)' % (vid, wid, v.getWeight(w)))

    source = G.getVertex('a')
    destination = G.getVertex('h')    
    dijkstra(G, source) 

    for v in G.vertDictionary.values():
        print(source.getVertexID(), " to ", v.getVertexID(), "-->", v.getDistance())

    path = [destination.getVertexID()]
    shortest(destination, path)
    print('The shortest path from a to h is: %s' % (path)) # show in reverse
    
    # graph 3
    G = DiGraph()
    G.addEdge('s', 2, 9)  
    G.addEdge('s', 6, 14) 
    G.addEdge('s', 7, 15) 
    G.addEdge(2,3,24)
    G.addEdge(3,5,2)
    G.addEdge(3,'t',19)
    G.addEdge(4,3,6)
    G.addEdge(4,'t',6)
    G.addEdge(5,4,11)
    G.addEdge(5,'t',16)
    G.addEdge(6,3,18)
    G.addEdge(6,5,30)
    G.addEdge(6,7,5)
    G.addEdge(7,5,20)
    G.addEdge(7,'t',44)

    print('Graph data:')
    for v in G:
        for w in v.getConnections():
            vid = v.getVertexID()
            wid = w.getVertexID()
            print('( %s , %s, %3d)' % (vid, wid, v.getWeight(w)))

    source = G.getVertex('s')
    destination = G.getVertex('t')    
    dijkstra(G, source) 

    for v in G.vertDictionary.values():
        print(source.getVertexID(), " to ", v.getVertexID(), "-->", v.getDistance())

    path = [destination.getVertexID()]
    shortest(destination, path)
    print('The shortest path from s to t is: %s' % (path)) # show in reverse
    
    
