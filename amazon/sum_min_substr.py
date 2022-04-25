def sumSubarrayMins(A):
    res = 0
    s = []
    A = [0] + A + [0]
    for i, x in enumerate(A):
        print(i,x,s)
        while s and A[s[-1]] > x:
            j = s.pop()
            k = s[-1]
            res += A[j] * (i - j) * (j - k)
        print(res)
        s.append(i)
        print(s)
        print()
    return res % (10**9 + 7)


if __name__ == '__main__':
    
    # Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

    

    # Example 1:

    # Input: arr = [3,1,2,4]
    # Output: 17
    # Explanation: 
    # Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
    # Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
    # Sum is 17.
    # Example 2:

    # Input: arr = [11,81,94,43,3]
    # Output: 444

    print(sumSubarrayMins(A=[3,1,2,4]))
    print(sumSubarrayMins(A=[11,81,94,43,3]))