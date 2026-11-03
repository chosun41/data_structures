class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        row_zero = False # Tracker for the first row specifically
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0 # Mark the column
                    if r > 0:
                        matrix[r][0] = 0 # Mark the row
                    else:
                        row_zero = True
                        
        # Fill based on markers (skipping first row/col for now)
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
                    
        # Handle the first column
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
                
        # Handle the first row
        if row_zero:
            for c in range(cols):
                matrix[0][c] = 0

# --- Test Example ---
if __name__ == "__main__":

    # special case for row_Zero so that it doesnt wipe both first column and first row

    # Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

    # You must do it in place.
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Solution().setZeroes(matrix)
    print(matrix) 
    # Expected: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]