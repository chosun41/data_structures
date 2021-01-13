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
    
if __name__=='__main__':
    # time and space: O(mn)
    matrix= [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]]
    x=NumMatrix(matrix)
    print(x.sumRegion(2,1,4,3))