

def minPushBox(grid):
    dire = [(1,0),(0,1),(-1,0),(0,-1)]
    
    def can_get(cur_b,cur_p,tar):
        seen,cur = set([cur_p]),set([cur_p])
        while cur:
            tmp = []
            for loc in cur:
                for x,y in dire:
                    if 0<= loc[0]+x < len(grid) and 0 <= loc[1] + y < len(grid[0]) and (loc[0]+x,loc[1] +y) != cur_b and grid[loc[0] +x][loc[1] +y] != '#' and (loc[0]+x,loc[1] +y) not in seen:
                        tmp += [(loc[0]+x,loc[1] +y)]
            cur = set(tmp)
            seen |= cur
            if tar in seen:
                return True
        return False
        
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'B': box = (i,j)
            if grid[i][j] == 'S': player = (i,j)
            if grid[i][j] == 'T': target = (i,j)
            
    seen,cur,res = set([(box,player)]), set([(box,player)]), 0
    while cur:
        tmp = []
        res += 1
        for b,p in cur:
            for x,y in dire:
                if 0<= b[0]+x < len(grid) and 0 <= b[1] + y < len(grid[0]) and grid[b[0]+x][b[1]+y] != '#' and can_get(b,p,(b[0]-x,b[1]-y)) and ((b[0]+x,b[1]+y),b) not in seen:
                    tmp += [((b[0]+x,b[1]+y),b)]
        cur = set(tmp)
        seen |= cur
        for x,y in dire:
            if (target,(target[0]+x,target[1]+y)) in seen:
                return res
    return -1

if __name__ == '__main__':

    # A storekeeper is a game in which the player pushes boxes around in a warehouse trying to get them to target locations.

    # The game is represented by an m x n grid of characters grid where each element is a wall, floor, or box.

    # Your task is to move the box 'B' to the target position 'T' under the following rules:

    # The character 'S' represents the player. The player can move up, down, left, right in grid if it is a floor (empty cell).
    # The character '.' represents the floor which means a free cell to walk.
    # The character '#' represents the wall which means an obstacle (impossible to walk there).
    # There is only one box 'B' and one target cell 'T' in the grid.
    # The box can be moved to an adjacent free cell by standing next to the box and then moving in the direction of the box. This is a push.
    # The player cannot walk through the box.
    # Return the minimum number of pushes to move the box to the target. If there is no way to reach the target, return

    grid = [["#","#","#","#","#","#"],
            ["#","T",".",".","#","#"],
            ["#",".","#","B",".","#"],
            ["#",".",".",".",".","#"],
            ["#",".",".",".","S","#"],
            ["#","#","#","#","#","#"]]
    print(minPushBox(grid))