def countBattleships(board):
    total = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'X':
                flag = 1
                if j > 0 and board[i][j-1] == 'X': # previous column
                    flag = 0
                if i > 0 and board[i-1][j] == 'X': # previous row
                    flag = 0
                total += flag
    return total
    
if __name__ =='__main__':
    # time: O(mn)
    # space: O(1)
    board=[['X','.','.','X'],
           ['.','.','.','X'],
           ['.','.','.','X']]
    print(countBattleships(board))