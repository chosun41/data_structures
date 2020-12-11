def merge_two_sorted_arrays(A, m, B,n):

    a, b, write_idx = m - 1, n - 1, m + n - 1
    while a >= 0 and b >= 0:
        if A[a] > B[b]:
            A[write_idx] = A[a]
            a -= 1
        else:
            A[write_idx] = B[b]
            b -= 1
        write_idx -= 1
    while b >= 0:
        A[write_idx] = B[b]
        write_idx, b = write_idx - 1, b - 1
    return A
        
if __name__ == '__main__':
    
    # O(m+n)
    # A contains enough to fit in b, m and n are numbers of initial entires in A and B respectively
    print(merge_two_sorted_arrays([3,13,17,None,None,None,None,None],3,[3,7,11,19],4))