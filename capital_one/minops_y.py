from collections import Counter
from itertools import chain
def minimumOperationsToWriteY(grid):
    
    n  = len(grid)   
    n2 = n//2

    y = ((grid[i][i], grid[n-i-1][n2],          #  <-- 1)
            grid[i][n-i-1]) for i in range(n2)) # 

    ctr1 = Counter(chain(*y))                   #  <-- 2)
    ctr1[grid[n2][n2]]+= 1                      #

    ctr2 = Counter(chain(*grid)) - ctr1         #  <-- 3)

    return n*n - max(                           #  <-- 4)
            ctr1[0]+ctr2[1], ctr1[1]+ctr2[0],
            ctr1[0]+ctr2[2], ctr1[2]+ctr2[0], 
            ctr1[1]+ctr2[2], ctr1[2]+ctr2[1])

if __name__ == '__main__':

    print(minimumOperationsToWriteY([[1,2,2],[1,1,0],[0,1,0]]))

   # You are given a 0-indexed n x n grid where n is odd, and grid[r][c] is 0, 1, or 2.

    # We say that a cell belongs to the Letter Y if it belongs to one of the following:

    # The diagonal starting at the top-left cell and ending at the center cell of the grid.
    # The diagonal starting at the top-right cell and ending at the center cell of the grid.
    # The vertical line starting at the center cell and ending at the bottom border of the grid.
    # The Letter Y is written on the grid if and only if:

    # All values at cells belonging to the Y are equal.
    # All values at cells not belonging to the Y are equal.
    # The values at cells belonging to the Y are different from the values at cells not belonging to the Y.
    # Return the minimum number of operations needed to write the letter Y on the grid given that in one operation you can change the value at any cell to 0, 1, or 2.

    

    # Example 1:


    # Input: grid = [[1,2,2],[1,1,0],[0,1,0]]
    # Output: 3
    # Explanation: We can write Y on the grid by applying the changes highlighted in blue in the image above. After the operations, all cells that belong to Y, denoted in bold, have the same value of 1 while those that do not belong to Y are equal to 0.
    # It can be shown that 3 is the minimum number of operations needed to write Y on the grid.
    # Example 2:

