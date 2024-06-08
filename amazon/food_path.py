def getFood(grid):
    start = None
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "*":
                start = (row, col)
                break

    q = [start]
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    curr = 1 # important
    while len(q) > 0:
        for i in range(len(q)): # important
            loc = q.pop(0)
            for d in directions:
                row = d[0] + loc[0]
                col = d[1] + loc[1]
                if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]):
                    if grid[row][col] == "#":
                        return curr
                    if grid[row][col] == "O":
                        grid[row][col] = curr
                        q.append((row, col))
        curr += 1
    return -1

if __name__ == '__main__':
    
    # You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.

    # You are given an m x n character matrix, grid, of these different types of cells:

    # '*' is your location. There is exactly one '*' cell.
    # '#' is a food cell. There may be multiple food cells.
    # 'O' is free space, and you can travel through these cells.
    # 'X' is an obstacle, and you cannot travel through these cells.
    # You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

    # Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.

    

    # Example 1:


    # Input: grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
    # Output: 3
    # Explanation: It takes 3 steps to reach the food.
    # Example 2:


    # Input: grid = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]
    # Output: -1
    # Explanation: It is not possible to reach the food.
    # Example 3:


    # Input: grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]
    # Output: 6
    # Explanation: There can be multiple food cells. It only takes 6 steps to reach the bottom food.

    print(getFood([["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]))