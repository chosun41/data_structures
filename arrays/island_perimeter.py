def islandPerimeter(grid):
    islands, neighbours = 0, 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                islands += 1
                #Checking down neighbours
                if i < len(grid)-1 and grid[i+1][j]:
                    neighbours += 1
                #Checking right neighbours
                if j < len(grid[i])-1 and grid[i][j+1]:
                    neighbours += 1
    return 4*islands - 2*neighbours

if __name__ == '__main__':
    # time: O(mn)
    # space: O(1)
    print(islandPerimeter(grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))