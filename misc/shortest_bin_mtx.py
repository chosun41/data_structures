import collections

def shortestPathBinaryMatrix(grid):
        r = len(grid)
        c = len(grid[0])
        if grid[0][0] or grid[r-1][c-1]:
          return -1
        dirs = [[1,0], [-1,0], [0,1], [0,-1], [-1,-1], [1,1], [1,-1], [-1,1]]
        seen = set()
        queue = collections.deque([(0,0,1)]) # indice, dist
        seen.add((0,0))
        while queue:
          i,j,dist = queue.popleft()
          if i == r -1 and j == c - 1:
            return dist
          for d1, d2 in dirs: 
            x, y = i + d1, j + d2
            if 0 <= x < r and 0 <= y < c:
              if (x,y) not in seen and grid[x][y] == 0:
                seen.add((x, y))
                queue.append((x, y, dist + 1))
        return -1

if __name__=='__main__':
    # shortest path length in a binary matrix
    # time and space: O(mn)
    print(shortestPathBinaryMatrix(grid = [[0,0,0],[1,1,0],[1,1,0]]))
    print(shortestPathBinaryMatrix(grid = [[1,0,0],[1,1,0],[1,1,0]]))
    print(shortestPathBinaryMatrix(grid = [[0,0,0,1,0,0,0],
                                           [0,1,1,1,0,0,0],
                                           [0,1,0,0,0,1,1],
                                           [0,0,1,1,1,0,1],
                                           [0,1,1,1,0,0,0]]))