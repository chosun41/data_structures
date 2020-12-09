# rotate once clockwise
# bit complement of x is -x-1
def rotate_matrix(square_matrix):

    matrix_size = len(square_matrix) - 1
    
    # start from corners and move right
    for i in range(len(square_matrix) // 2):
        for j in range(i, matrix_size - i):
            # Perform a 4-way exchange. Note that A[~i] for i in [0, len(A) - 1]
            # is A[-(i + 1)].
            (square_matrix[i][j], square_matrix[~j][i], square_matrix[~i][~j],square_matrix[j][~i]) = \
            (square_matrix[~j][i],square_matrix[~i][~j],square_matrix[j][~i],square_matrix[i][j])
    return square_matrix
            
if __name__ == '__main__':
     
    # time: O(n^2) space: O(1)
    
    A=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print(rotate_matrix(A))
    print(~0)