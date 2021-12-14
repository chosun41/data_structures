def kthSmallest(matrix, k):
    n = len(matrix)

    def count_lt(x):
        """The number of elements less than x."""
        
        # Start in the bottom-left corner.
        
        # Go up until <x; add i+1 to total; go right.
        # Stop when you reach the top or right edge.
        i, j = n-1, 0
        total = 0
        while 0 <= i and j < n:
            if matrix[i][j] < x:
                total += i+1 #?
                j += 1
            else:
                i -= 1
        return total

    lo = matrix[0][0]
    hi = matrix[-1][-1]

    while True:
        mid = (lo + hi) // 2
        if mid == lo:
            return lo
        elif count_lt(mid) < k:
            lo, hi = mid, hi
        else:
            lo, hi = lo, mid
        print(lo,mid,hi)

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
    # lo=1,hi=15
    # mid=8,total=2,lo=8,hi=15
    # mid=11,total=4,lo=11,hi=15
    # mid=13,total=6,lo=13,hi=15
    # mid=14,total=8,lo=13,hi=14