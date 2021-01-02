from graph_list import Graph,DiGraph

# used when there are negative weights and easier for distributed machines, no need for priority queue
# time: O(ExV) - longer than dijkstra

# just extracts previous to a list
def shortest(v, path):
    if v.previous:
        path.insert(0,v.previous.getVertexID())
        shortest(v.previous, path)
    return

def BellmanFord(G, source):
    
    # Set the distance for the source node to zero (from infinity)
    source.setDistance(0)
        
    for current in G:
        for next in current.adjacent:

            newDist = current.getDistance() + current.getWeight(next)

            # update adjacent distance if it is lower than the current vertex distance and also the previous vertex
            # that can be used later for the shortest path
            if newDist < next.getDistance():
                next.setDistance(newDist)
                next.setPrevious(current)

                print('Updated : current = %s next = %s newDist = %s' \
                        % (current.getVertexID(), next.getVertexID(), next.getDistance()))
            else:
                print('Not updated : current = %s next = %s newDist = %s' \
                        % (current.getVertexID(), next.getVertexID(), next.getDistance()))
                
    # check for negative-weight cycles
    for current in G:
        for next in current.adjacent:
            assert next.getDistance() <= current.getDistance() + current.getWeight(next)
    
if __name__ == '__main__':

    # directed graph with no negative cycle
    G = DiGraph()
    G.addEdge('a', 'b', -1)  
    G.addEdge('a', 'c', 4) 
    G.addEdge('b', 'c', 3) 
    G.addEdge('b', 'd', 2) 
    G.addEdge('b', 'e', 2)
    G.addEdge('d', 'b', 1)
    G.addEdge('d', 'c', 5)
    G.addEdge('e', 'd', -3)

    print('Graph data:')
    for v in G:
        for w in v.getConnections():
            vid = v.getVertexID()
            wid = w.getVertexID()
            print('( %s , %s, %3d)' % (vid, wid, v.getWeight(w)))

    source = G.getVertex('a')
    destination = G.getVertex('e')    
    BellmanFord(G, source) 

    for v in G.vertDictionary.values():
        print(source.getVertexID(), " to ", v.getVertexID(), "-->", v.getDistance())

    path = [destination.getVertexID()]
    shortest(destination, path)
    print('The shortest path from a to e is: %s' % (path)) # show in reverse
    
    # directed graph with negative cycle
    G = DiGraph()
    G.addEdge(0, 1,1)  
    G.addEdge(1,2,-1)
    G.addEdge(2,3, -1) 
    G.addEdge(3,0, -1) 

    print('Graph data:')
    for v in G:
        for w in v.getConnections():
            vid = v.getVertexID()
            wid = w.getVertexID()
            print('( %s , %s, %3d)' % (vid, wid, v.getWeight(w)))

    source = G.getVertex(0)
    destination = G.getVertex(4)    
    BellmanFord(G, source) 

    for v in G.vertDictionary.values():
        print(source.getVertexID(), " to ", v.getVertexID(), "-->", v.getDistance())

    path = [destination.getVertexID()]
    shortest(destination, path)
    print('The shortest path from 0 to 4 is: %s' % (path)) # show in reverse
