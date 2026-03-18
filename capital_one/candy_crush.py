def candyCrush(board):
    # Edge case
    if board is None:
        return board
    
    ROWS, COLS = len(board), len(board[0])
    is_all_crushed = True
    
    # Step 1: Tag rows that need to be crushed
    # We are going to achieve this by searching each row with a sliding window of 3 
    # and if we find numbers that match, we will keep track of it. We will mark it 
    # negative so we know which values to crush and because there's a chance of a
    # vertical crush that depends on our horizontal crush
    for row in range(ROWS):
        for col in range(COLS - 2):
            num1 = abs(board[row][col])
            num2 = abs(board[row][col + 1])
            num3 = abs(board[row][col + 2])
            
            # Checking if it can be crushed horizontally
            if num1 == num2 and num2 == num3 and num1 != 0:
                board[row][col] = -num1
                board[row][col + 1] = -num2
                board[row][col + 2] = -num3
                is_all_crushed = False
        
    
    # Step 2: Tag columns that need to be crushed
    # We are going to achieve this by searching each column with a sliding window
    # of 3 and if we find numbers that match, we will keep track of it. We will 
    # mark it negative so we know which values to crush
    for col in range(COLS):
        for row in range(ROWS - 2):
            num1 = abs(board[row][col])
            num2 = abs(board[row + 1][col])
            num3 = abs(board[row + 2][col])
        
            # Checking if it can be crushed vertically
            if num1 == num2 and num2 == num3 and num1 != 0:
                board[row][col] = -num1
                board[row + 1][col] = -num2
                board[row + 2][col] = -num3
                is_all_crushed = False
    
    # Step 3: Crush the candies
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] < 0:
                board[row][col] = 0
    
    # Step 4: Gravity
    # For every column, we want to put every positive number at the bottom.
    # For every positive number, we want to swap it so that positive
    # number are at the bottom and zeroes are at the top. It is 
    # similar to https://leetcode.com/problems/move-zeroes/
    for col in range(COLS):
        idx = ROWS - 1
        for row in range(ROWS - 1, -1, -1):
            if board[row][col] > 0:
                board[idx][col], board[row][col] = board[row][col], board[idx][col]
                idx -= 1
    
    return board if is_all_crushed else candyCrush(board)


if __name__ == '__main__':

    print(candyCrush(board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]))
    print(candyCrush( board = [[1,3,5,5,2],[3,4,3,3,1],[3,2,4,5,2],[2,4,4,5,5],[1,4,4,1,1]]))

    # This question is about implementing a basic elimination algorithm for Candy Crush.

    # Given an m x n integer array board representing the grid of candy where board[i][j] represents the type of candy. A value of board[i][j] == 0 represents that the cell is empty.

    # The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:

    # If three or more candies of the same type are adjacent vertically or horizontally, crush them all at the same time - these positions become empty.
    # After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. No new candies will drop outside the top boundary.
    # After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
    # If there does not exist more candies that can be crushed (i.e., the board is stable), then return the current board.
    # You need to perform the above rules until the board becomes stable, then return the stable board.

    

    # Example 1:


    # Input: board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
    # Output: [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]
    # Example 2:

    # Input: board = [[1,3,5,5,2],[3,4,3,3,1],[3,2,4,5,2],[2,4,4,5,5],[1,4,4,1,1]]
    # Output: [[1,3,0,0,0],[3,4,0,5,2],[3,2,0,3,1],[2,4,0,5,2],[1,4,3,1,1]]