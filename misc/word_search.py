def exist(board, word):
    
    visited = set()

    for i in range(len(board)):
        for j in range(len(board[0])):
            if getWords(board, word, i,j, visited):
                return True
    return False

def getWords(board, word, i, j, visited, pos = 0):
    if pos == len(word):
        return True

    if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or (i,j) in visited or word[pos] != board[i][j]:
        return False   

    visited.add((i,j))
    res = (getWords(board, word, i-1,j, visited, pos+1) or
            getWords(board, word, i,j-1, visited, pos+1) or
            getWords(board, word, i+1,j, visited, pos+1) or
            getWords(board, word, i,j+1, visited, pos+1))
    visited.remove((i,j))
    return res

if __name__=='__main__':
    # time: O(n4^L) space: O(L) - n number of letters on board, l is length of word, 3 is directions
    board = [["A","B","C","E"],
             ["S","F","C","S"],
             ["A","D","E","E"]]
    word = "ABCCED"
    print(exist(board,word))
    board = [["A","B","C","E"],
             ["S","F","C","S"],
             ["A","D","E","E"]], 
    word = "ABCB"
    print(exist(board,word))