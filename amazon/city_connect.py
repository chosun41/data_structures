import heapq
import collections

def minimumCost(n, connections):
    # Create our adjacency list/graph
    adj = collections.defaultdict(list)
    for c1, c2, cost in connections:
        adj[c1].append([c2, cost])
        adj[c2].append([c1, cost])
        
    # Creat our heap and add our starting cost and location (0 cost to start).
    heap = [(0, 1)]
    heapq.heapify(heap)
    seen = set()
    total_cost = 0
    while heap:
        cost, city = heapq.heappop(heap)
        # If we haven't visited the city yet.
        if city not in seen:
            # Add it to seen (we got here via the lowest cost path) and add the cost to our total.
            seen.add(city)
            total_cost += cost
            # For the current nodes neighboring cities
            for nei, cst in adj[city]:
                # Push the neis on the heap so we select the lowest cost nei next.
                heapq.heappush(heap, [cst, nei])
    # Return our cost if we have visited all N nodes.
    return total_cost if len(seen) == n else -1


if __name__ == '__main__':
    
    # There are n cities labeled from 1 to n. You are given the integer n and an array connections where connections[i] = [xi, yi, costi] indicates that the cost of connecting city xi and city yi (bidirectional connection) is costi.

    # Return the minimum cost to connect all the n cities such that there is at least one path between each pair of cities. If it is impossible to connect all the n cities, return -1,

    # The cost is the sum of the connections' costs used.

    

    # Example 1:


    # Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
    # Output: 6
    # Explanation: Choosing any 2 edges will connect all cities so we choose the minimum 2.
    # Example 2:


    # Input: n = 4, connections = [[1,2,3],[3,4,4]]
    # Output: -1
    # Explanation: There is no way to connect all cities even if all edges are used.
    

    # Constraints:

    # 1 <= n <= 104
    # 1 <= connections.length <= 104
    # connections[i].length == 3
    # 1 <= xi, yi <= n
    # xi != yi
    # 0 <= costi <= 105

    print(minimumCost(n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]))
    print(minimumCost(n = 4, connections = [[1,2,3],[3,4,4]]))