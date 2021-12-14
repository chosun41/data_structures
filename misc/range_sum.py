class NumMatrix(object):
    
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if matrix and matrix[0]:
            self.summ = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
            for i in range(1, len(matrix)+1):
                for j in range(1, len(matrix[0])+1):
                    self.summ[i][j] = self.summ[i-1][j]+self.summ[i][j-1]-self.summ[i-1][j-1]+matrix[i-1][j-1]
                

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.summ[row2+1][col2+1] - self.summ[row2+1][col1] - self.summ[row1][col2+1] + self.summ[row1][col1]


if __name__ == '__main__':

    # Given a 2D matrix matrix, handle multiple queries of the following type:

    # Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
    # Implement the NumMatrix class:

    # NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
    # int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

    # time and space: O(nm)

    # Calculate a 2D sum matrix, so that the matrix can be divided into

    # A B

    # C D

    # The return value is D-B-C+A
    numMatrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
    print(numMatrix.sumRegion(2, 1, 4, 3)); # return 8 (i.e sum of the red rectangle)
    print(numMatrix.sumRegion(1, 1, 2, 2)); # return 11 (i.e sum of the green rectangle)
    print(numMatrix.sumRegion(1, 2, 2, 4)); # return 12 (i.e sum of the blue rectangle)