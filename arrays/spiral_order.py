def matrix_in_spiral_order(matrix):
    result = []
    if not matrix or not matrix[0]:
        return result
    m, n = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, m - 1, 0, n - 1
    while top <= bottom and left <= right:
        # Traverse right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        # Traverse down
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        # Traverse left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        # Traverse up
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

if __name__ == '__main__':

    # time: O(n^2) space: O(1)
    print(matrix_in_spiral_order([[1,2,3],
                                  [4,5,6],
                                  [7,8,9]]))
    print(matrix_in_spiral_order([[1,2,3,4],
                                  [5,6,7,8],
                                  [9,10,11,12],
                                  [13,14,15,16]]))