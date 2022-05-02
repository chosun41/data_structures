import collections

def minKnightMoves(x,y):
    q = collections.deque([(0, 0, 0)])
    x, y, visited = abs(x), abs(y), set([(0,0)])
    while q:
        a, b, step = q.popleft()
        if (a, b) == (x,y): 
            return step
        for dx, dy in [(1,2),(2,1),(1,-2),(2,-1),(-1,2),(-2,1)]:  # no need to have (-1, -2) and (-2, -1) since it only goes 1 direction
            if (a+dx, b+dy) not in visited and -1 <= a+dx <= x+2 and -1 <= b+dy <= y+2:
                visited.add((a+dx, b+dy))
                q.append((a+dx, b+dy, step+1))
    return -1

if __name__=='__main__':

    # In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

    # A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

    # Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

    # time and space: O(|x|*|y|)

    print(minKnightMoves( x = 5, y = 5)) # Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
    print(minKnightMoves(x = 2, y = 1)) # [0, 0] → [2, 1]
    print(minKnightMoves(x = -5, y = -5)) # [0, 0] → [2, 1] # prune negative space by taking absolute values