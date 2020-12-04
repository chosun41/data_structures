from graph_list import Graph,DiGraph

# topological sort is an ordering of verticies in a DAG (directed acyclic graph)
# in which each node comes before all nodes to which it has outgoing edges
# there might be multiple topological sorts unless theres a hamilitonian path, in which case there will be a unique
# topological sort ordering
# usually requires vertex in degree and dfs
# can be used to detect cycles

def mark_as_visited(G, node, visited, topological_ordering): 
    visited.append(node)
    v = G.getVertex(node)
    for k in v.getConnections():
        if k.id not in visited:
            mark_as_visited(G,k.id, visited, topological_ordering) 

    # basically ensures that by insert at start, that nodes with less indegree
    # will appear at start of the topolical ordering list
    topological_ordering.insert(0, node) 
    
def topological_sort(G): 
    
    visited=[]

    topological_ordering = [] 

    # visited basically becomes sort of dfs
    for v in G:
        if v.id not in visited:
            mark_as_visited(G,v.id, visited, topological_ordering) 

    return topological_ordering

if __name__ == '__main__':
    
    # time: 0(|E| + |V|)

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
    
    print(topological_sort(G))
    
    # visited=[7, 11, 2, 9, 10, 8]
    # topological_ordering=[7, 8, 11, 10, 9, 2]

    # visited=[7, 11, 2, 9, 10, 8, 5]
    # topological_ordering=[5, 7, 8, 11, 10, 9, 2]

    # visited=[7, 11, 2, 9, 10, 8, 5, 3]
    # topological_ordering=[3, 5, 7, 8, 11, 10, 9, 2]
   