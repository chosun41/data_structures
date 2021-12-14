def wallsAndGates(rooms):
    """
    :type rooms: List[List[int]]
    :rtype: void Do not return anything, modify rooms in-place instead.
    """
    if not rooms:
        return

    h = len(rooms)
    w = len(rooms[0])

    q = []
    for i in range(h):
        for j in range(w):
            if rooms[i][j] == 0:
                q.append((i,j))
    print(q)

    for row, col in q: # bfs not dfs, you iterate through neighbors in que not for dfs for one gate after another
        dist = rooms[row][col] + 1
        for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
            r = row + dy
            c = col + dx
            if 0 <= r < h and 0 <= c < w and rooms[r][c] == 2147483647: # if within bounds and is infinite
                rooms[r][c] = dist
                q.append((r,c))
    return rooms
                
if __name__=='__main__':
    # time and space: O(mn)
    # matrix of -1,0,inf
    # 0 is gate, -1 obstacle, inf is empty space
    # for each matrix index, find min steps to a gate
    # append 0s(gates) with coordinates to a queue
    # start from gates and bfs from there adding stuff to the queue
    rooms = [[2147483647,-1,0,2147483647],
             [2147483647,2147483647,2147483647,-1],
             [2147483647,-1,2147483647,-1],
             [0,-1,2147483647,2147483647]]
    print(wallsAndGates(rooms))
    
    # q=[(0,2),(3,0)],  rooms = [[2147483647,-1,0,1],
    #                            [2147483647,2147483647,1,-1],
    #                            [1,-1,2147483647,-1],
    #                            [0,-1,2147483647,2147483647]]
    # q=[(1,2),(2,0),(0,3)]   rooms = [[2147483647,-1,0,1],
    #                            [2,2,1,-1],
    #                            [1,-1,2,-1],
    #                            [0,-1,2147483647,2147483647]]
    # q=[(1,0),(3,2)]   rooms = [[3,-1,0,1],
    #                            [2,2,1,-1],
    #                            [1,-1,2,-1],
    #                            [0,-1,3,2147483647]]
    # q=[(3,2)]         rooms = [[3,-1,0,1],
    #                            [2,2,1,-1],
    #                            [1,-1,2,-1],
    #                            [0,-1,3,4]]
    