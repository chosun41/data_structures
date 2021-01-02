# rotate once clockwise
# bit complement of x is -x-1
def rotate_matrix(square_matrix):

    matrix_size = len(square_matrix) - 1
    
    # start from corners and move right
    for i in range(len(square_matrix) // 2):
        for j in range(i, matrix_size - i):
            # Perform a 4-way exchange. Note that A[~i] for i in [0, len(A) - 1]
            # is A[-(i + 1)].
            
            #  0,0 -1,0  -1,-1 0,-1
            # -1,0 -1,-1  0,-1 0,0
            
            #  0,1  -2,0  -1,-2 1,-1
            # -2,0 -1,-2  1,-1  0,1
            
            # ...
            
            (square_matrix[i][j], square_matrix[~j][i], square_matrix[~i][~j],square_matrix[j][~i]) = \
            (square_matrix[~j][i],square_matrix[~i][~j],square_matrix[j][~i],square_matrix[i][j])
    return square_matrix
            
if __name__ == '__main__':
     
    # time: O(n^2) space: O(1)
    
    A=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print(rotate_matrix(A))
    
    #   0  1  2  3
    # 0 1  2  3  4
    # 1 5  6  7  8
    # 2 9  10 11 12
    # 3 13 14 15 16
    
    #   0  1  2  3
    # 0 13 9  5  1
    # 1 14 10 6  2
    # 2 15 11 7  3
    # 3 16 12 8  4
    
    # 1 - 0,0 -> 0,3
    # 13 - 3,0 -> 0,0