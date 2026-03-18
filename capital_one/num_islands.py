def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    def dfs_visit(grid, u):
        i,j=u[0],u[1]
        for x,y in ((0,1),(1,0),(-1,0),(0,-1)):
            if 0<=i+x<m and 0<=j+y<n and grid[i+x][j+y]=='1' and (i+x,j+y) not in visited:
                visited.add((i+x,j+y))
                dfs_visit(grid,(i+x,j+y))     
        
    count=0
    visited=set()
    m=len(grid)
    n=len(grid[0])
    
    for i in range(m):
        for j in range(n):
            if grid[i][j]=='1' and (i,j) not in visited:
                dfs_visit(grid,(i,j))
                count+=1
    return count

if __name__ == '__main__':
    # time and space: O(mn)
    # island is connected 1s surrounded by 0s in vertical and horizontal direction, not diagonally
    # what is the number of islands
    grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
    print(numIslands(grid))