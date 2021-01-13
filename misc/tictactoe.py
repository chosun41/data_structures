class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0] * n for i in range(n)]
        self.size = n

    def move(self, row: int, col: int, player: int) -> int:
        if self.board[row][col] == 0: 
            self.board[row][col] = player
        
        for i in range(self.size):
            if self.board[row][i] != player: # check same row
                break
            if i == self.size-1:
                return player
        
        for i in range(self.size):
            if self.board[i][col] != player: # check same column
                break
            if i == self.size-1:
                return player
            
        for i in range(self.size):
            if self.board[i][i] != player: # check right diagonals
                break
            if i == self.size-1:
                return player
        
        for i in range(self.size):
            if self.board[i][self.size-i-1] != player: # check left diagonal
                break
            if i == self.size-1:
                return player
        return 0  
        
if __name__ == '__main__':
    # time: O(n)
    # space: O(n^2)
    x=TicTacToe(3)
    print(x.move(0, 0, 1))
    print(x.move(0, 2, 2))
    print(x.move(2, 2, 1))
    print(x.move(1, 1, 2))
    print(x.move(2, 0, 1))
    print(x.move(1, 0, 2))
    print(x.move(2, 1, 1))
    
    # 1   2 
    # 2 2 
    # 1 1 1