def isToeplitzMatrix(matrix):
    return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
                for r, row in enumerate(matrix)
                for c, val in enumerate(row))

    # comparing to before
if __name__=='__main__':

    # A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

    # time: O(m*n)
    # space: O(1)

    print(isToeplitzMatrix(matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
    print(isToeplitzMatrix([[1,2],[2,2]]))