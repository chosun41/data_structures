def exist(board, word):
    def backtrack(word, i, j, m, n):
        nonlocal l,is_found
        if board[i][j] != word[l]:
            return
        visited.add((i, j))
        l += 1
        if l == len(word):
            is_found = True
            return 
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            i1, j1 = i + di, j + dj
            if 0 <= i1 < m and 0 <= j1 < n and (i1, j1) not in visited:
                backtrack(word, i1, j1, m, n)
                if is_found:
                    return 
        visited.remove((i, j))
        l -= 1

    if not board or not board[0]:
        return False
    if word == '':
        return True
    m, n = len(board), len(board[0])
    is_found = False
    l = 0
    visited = set()
    for i in range(m):
        for j in range(n):
            backtrack(word, i, j, m, n)
            if is_found:
                return True
    return False

if __name__=='__main__':
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