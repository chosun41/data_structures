def matrix_in_spiral_order(square_matrix):
    def matrix_layer_in_clockwise(offset):
        if offset == len(square_matrix) - offset - 1:
            # square_matrix has odd dimension, and we are at the center of the
            # matrix square_matrix.
            spiral_ordering.append(square_matrix[offset][offset]) # center
            return

        # add first n-1 elements of first row
        spiral_ordering.extend(square_matrix[offset][offset:-1 - offset])
        
        # add first n-1 elements of last column (zipping transforms rows into columns)
        spiral_ordering.extend(list(zip(*square_matrix))[-1 - offset][offset:-1 - offset])
        
        # add last n-1 of last row in reverse order
        spiral_ordering.extend(square_matrix[-1 - offset][-1 -offset:offset:-1])
        
        # add last n-1 elements of first column in reverse order ((zipping transforms rows into columns))
        spiral_ordering.extend(list(zip(*square_matrix))[offset][-1 - offset:offset:-1])

    spiral_ordering = []
    for offset in range((len(square_matrix) + 1) // 2):
        matrix_layer_in_clockwise(offset)
    return spiral_ordering

if __name__ == '__main__':

    # time: O(n^2)
    print(matrix_in_spiral_order([[1,2,3],[4,5,6],[7,8,9]]))
    print(matrix_in_spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))