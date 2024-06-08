def largestIsland(grid):
    N = len(grid)

    def move(x, y):
        for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if 0 <= x + i < N and 0 <= y + j < N:
                yield x + i, y + j

    def dfs(x, y, index):
        res = 0
        grid[x][y] = index # dfs marks the color
        for i, j in move(x, y):
            if grid[i][j] == 1:
                res += dfs(i, j, index) #!!! dont need visited because marking islands with number
        return res + 1 # also returns the area

    # dfs to get the area of the island
    index = 2 # color of island
    areas = {0: 0} # dictionary to contain the area of an island
    for x in range(N):
        for y in range(N):
            if grid[x][y] == 1:
                areas[index] = dfs(x, y, index)
                index += 1
    print(areas)
    print(grid)

    # look at 0 and see what is the max area based on immediate area and dictionary of areas
    res = max(areas.values())
    for x in range(N):
        for y in range(N):
            if grid[x][y] == 0:
                possible = set(grid[i][j] for i, j in move(x, y))
                print(possible)
                res = max(res, sum(areas[index] for index in possible) + 1)
    return res

if __name__=='__main__':
    # time and space: O(n^2)
    # can change at most one 0 to 1, what is the area of the largest island afterwards?
    print(largestIsland( [[1, 0], [0, 1]]))
    print("\n")
    print(largestIsland( [[1,0,0], [1,0,0],[0,1,0]]))