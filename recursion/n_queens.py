def n_queens(n):
    def solve_n_queens(row):
        if row == n:
            # All queens are legally placed.
            result.append(col_placement[:])
            return
        for col in range(n): # abs(row-r)!=abs(col-c)
            if all(r!=row and c!=col and abs(row-r)!=abs(col-c) for r, c in enumerate(col_placement[:row])):
                col_placement[row] = col
                solve_n_queens(row + 1)

    result = []
    col_placement = [0] * n
    solve_n_queens(0)
    return result

if __name__=='__main__':
    # time: O(n!) number of possibilities dwindle
    # space: O(n)
    print(n_queens(4))
    
    # [[1, 3, 0, 2], [2, 0, 3, 1]] locations in each row
    
    #   0 1 2 3
    # 0 o x o o
    # 1 o o o x
    # 2 x o o o
    # 3 o o x o
    
    # [0,1] none in row 0, none in col 1, not in [1,0],[1,2],[2,3] 
    # [1,3] none in row 1, none in col 3, not in [0,2],[2,2],[3,1] 
    # [2,0] none in row 2, none in col 0, not in [0,2],[1,1],[3,1] 
    # [3,2] none in row 3, none in col 2, not in [1,0],[2,1],[2,3] 
    
    #   0 1 2 3
    # 0 o o x o
    # 1 x o o o
    # 2 o o o x
    # 3 o x o o
    
    