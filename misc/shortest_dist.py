import collections

def shortestDistance(grid):
    ## RC ##
    ## APPROACH : BFS ##

    if not grid : 
        return 0
    n = len(grid)
    m = len(grid[0])
    builds = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                builds.append((i, j, 0))
    print(builds)
    distances = collections.defaultdict(list)
    for build in builds:
        queue=[build]
        visited = set()
        while queue:
            i, j, d = queue.pop(0)
            for x, y in [(0,1),(0,-1),(-1,0),(1,0)]:
                if 0 <= i + x < n and 0 <= j + y < m and grid[ i+x ][ j+y ]==0 and (i+x, j+y) not in visited:
                    visited.add((i+x, j+y))
                    distances[(i+x,j+y)].append(d+1)
                    queue.append((i+x, j+y, d+1))
    print(distances)
    ans = float('inf')
    for d in distances.values():
        if len(d) == len(builds):
            ans = min(ans,sum(d) )
    return -1 if(ans == float('inf')) else ans

if __name__=='__main__':
    # time and space: O(mn)
    # 0 empty land,1 marks building, 2 obstacle
    # what is the shortest dist of new building to rest of buildings
    # bfs from buildings
    grid=[[1,0,2,0,1],
          [0,0,0,0,0],
          [0,0,1,0,0]]
    print(shortestDistance(grid))
    