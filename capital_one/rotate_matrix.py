def rotate_matrix(matrix):

    # reverse
    l = 0
    r = len(matrix) -1
    while l < r:
        matrix[l], matrix[r] = matrix[r], matrix[l]
        l += 1
        r -= 1
    # transpose 
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix
            
if __name__ == '__main__':
     
    # time: O(n^2) space: O(1)
    
    A=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print(rotate_matrix(A))

    # We can do this in two steps.
    # Reversing the matrix does this:
    # [1,2,3],
    # [4,5,6],
    # [7,8,9]]
    # ->
    # [7, 8, 9],
    # [4, 5, 6],
    # [1, 2, 3]

    # Transposing means: rows become columns, columns become rows.

    # [7, 8, 9],
    # [4, 5, 6],
    # [1, 2, 3]
    # ->
    # [7,4,1],
    # [8,5,2],
    # [9,6,3]