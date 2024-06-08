def kthSmallest(matrix, k):
    n = len(matrix)
    # Set the range of the search to be between the smallest element
    # and the largest element in the matrix
    left, right = matrix[0][0], matrix[n-1][n-1]
    
    # Binary search for the kth smallest element
    while left < right: # l<r not l<=r
        mid = (left + right) // 2
        count = 0
        j = n - 1
        # Count the number of elements in the matrix that are less than or equal to mid
        for i in range(n):
            while j >= 0 and matrix[i][j] > mid:
                j -= 1
            count += j + 1
        # Update the range of the search
        if count < k:
            left = mid + 1
        else:
            right = mid
    
    return left

if __name__=='__main__':
    # time: O(n x log(max-min))
    # space: O(1)
    matrix = [
       [ 1,  5,  9],
       [10, 11, 13],
       [12, 13, 15]
    ]
    k = 8
    print(kthSmallest(matrix, k))
    # O(logn) O(1)