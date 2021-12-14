def matrix_in_spiral_order(matrix):
    if not matrix or not matrix[0]:
        return []
    ans = []
    m, n = len(matrix), len(matrix[0])
    u, d, l, r = 0, m - 1, 0, n - 1
    while l < r and u < d:
        ans.extend([matrix[u][j] for j in range(l, r)])
        ans.extend([matrix[i][r] for i in range(u, d)])
        ans.extend([matrix[d][j] for j in range(r, l, -1)])
        ans.extend([matrix[i][l] for i in range(d, u, -1)])
        u, d, l, r = u + 1, d - 1, l + 1, r - 1
    if l == r:
        ans.extend([matrix[i][r] for i in range(u, d + 1)])
    elif u == d:
        ans.extend([matrix[u][j] for j in range(l, r + 1)])
    return ans

if __name__ == '__main__':

    # time: O(n^2) space: O(1)
    print(matrix_in_spiral_order([[1,2,3],
                                  [4,5,6],
                                  [7,8,9]]))
    print(matrix_in_spiral_order([[1,2,3,4],
                                  [5,6,7,8],
                                  [9,10,11,12],
                                  [13,14,15,16]]))