from graph_list import Graph,DiGraph

# breadth first search - crawl to neighbors and expand (uses queues)
# better for shortest path
def bfs(graph, node, visited):
    queue=[]
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0) 
        v = graph.getVertex(s)
        for k in v.getConnections():
            if k.id not in visited:
                visited.append(k.id)
                queue.append(k.id)
    return visited

# depth first search - go deep and go back when you hit a dead end (uses stack)
# lower memory requirement than bfs
# better for paths, cycles, spanning forest, connected components
def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        v = graph.getVertex(node)
        for k in v.getConnections():
            dfs(graph,k.id, visited)
    return visited

if __name__ == '__main__':

    G = DiGraph()
    G.addEdge('a', 'b', 1)  
    G.addEdge('a', 'c', 1)
    G.addEdge('b', 'd', 1)
    G.addEdge('b', 'e', 1)
    G.addEdge('c', 'd', 1)
    G.addEdge('c', 'e', 1)
    G.addEdge('d', 'e', 1)
    G.addEdge('e', 'a', 1)
    print('Graph data:')
    print(G.getEdges())
 
    y=bfs(G,'a',[])
    print(y)
    
    print("\n")

    G = DiGraph()
    G.addEdge('a', 'b', 1)  
    G.addEdge('a', 'c', 1)
    G.addEdge('b', 'd', 1)
    G.addEdge('b', 'e', 1)
    G.addEdge('c', 'd', 1)
    G.addEdge('c', 'e', 1)
    G.addEdge('d', 'e', 1)
    G.addEdge('e', 'a', 1)
    print('Graph data:')
    print(G.getEdges())
 
    x=dfs(G,'a',[])
    print(x)
    
    G = DiGraph()
    G.addEdge(11, 2, 1)
    G.addEdge(11, 9, 1)
    G.addEdge(11, 10, 1)
    G.addEdge(8, 9, 1)
    G.addEdge(3, 10, 1)
    G.addEdge(7, 11, 1)  
    G.addEdge(7, 8, 1)
    G.addEdge(5, 11, 1)
    G.addEdge(3, 8, 1)
    print('Graph data:')
    print(G.getEdges())
    
    z=dfs(G,7,[])
    print(z)
