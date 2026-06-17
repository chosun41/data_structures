class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        col = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)
        
        res = []
        board = [["."] * n for _ in range(n)]
        
        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue # continue not return
                
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                
                backtrack(r + 1)
                
                # Clean up (backtrack)
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
                
        backtrack(0)
        return res

# --- Test Example ---
if __name__ == "__main__":

    # The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

    # Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

    # Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

    

    # Example 1:


    # Input: n = 4
    # Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    # Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
    # Example 2:

    # Input: n = 1
    # Output: [["Q"]]
    sol = Solution()
    print(len(sol.solveNQueens(4))) # Expected: 2 solutions