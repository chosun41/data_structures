import collections

def orangesRotting(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    num_fresh_oranges = 0 

    q = collections.deque()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                num_fresh_oranges +=1
            elif grid[i][j]==2:
                q.append((i,j,0))

    while q:
        i,j,d = q.popleft()
        for x,y in ((0,1),(1,0),(-1,0),(0,-1)):
            if 0<=i+x<len(grid) and 0<=j+y<len(grid[0]) and grid[i+x][j+y]==1:
                num_fresh_oranges -=1
                if num_fresh_oranges ==0:
                    return d+1
                grid[i+x][j+y] += 1
                q.append((i+x,j+y,d+1))

    return -1

if __name__ == '__main__':
    
    # You are given an m x n grid where each cell can have one of three values:

    # 0 representing an empty cell,
    # 1 representing a fresh orange, or
    # 2 representing a rotten orange.
    # Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

    # Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

    

    # Example 1:


    # Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
    # Output: 4
    # Example 2:

    # Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
    # Output: -1
    # Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
    # Example 3:

    # Input: grid = [[0,2]]
    # Output: 0
    # Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
    

    # Constraints:

    # m == grid.length
    # n == grid[i].length
    # 1 <= m, n <= 10
    # grid[i][j] is 0, 1, or 2.

    print(orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]]))
    print(orangesRotting(grid = [[2,1,1],[0,1,1],[1,0,1]]))