from graph_list import Graph,DiGraph

# modification of topical sort
def isCyclicUtil(G, node, visited, recStack): 

    # Mark current node as visited and  
    # adds to recursion stack 
    v = G.getVertex(node)
    visited.append(v.id)
    recStack.append(v.id)

    # Recur for all neighbours 
    # if any neighbour is visited and in  
    # recStack then graph is cyclic 
    for k in v.getConnections():
        if k.id not in visited:
            if isCyclicUtil(G,k.id, visited, recStack) == True: 
                return True
        elif k.id in recStack: 
            return True

    # The node needs to be poped from  
    # recursion stack before function ends 
    recStack.remove(v.id)
    return False

# Returns true if graph is cyclic else false 
def isCyclic(G): 
    visited = []
    recStack = []
    for v in G: 
        if v.id not in visited:
            if isCyclicUtil(G,v.id,visited,recStack) == True: 
                return True
    return False

if __name__ == '__main__':
    
    # time: O(V + E)

    G = DiGraph()
    G.addEdge('a', 'b', 1)  
    G.addEdge('b', 'a', 1)
    print(isCyclic(G))
    
    G = DiGraph()
    G.addEdge('a', 'b', 1)  
    G.addEdge('b', 'c', 1)
    G.addEdge('c', 'd', 1)
    print(isCyclic(G))  
    
    G = DiGraph()
    G.addEdge('a', 'b', 1)  
    G.addEdge('b', 'c', 1)
    G.addEdge('c', 'd', 1)
    G.addEdge('d', 'a', 1)
    print(isCyclic(G)) 