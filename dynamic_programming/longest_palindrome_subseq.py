def LongestPalindromeSubsequence(A):
    n = len(A)
    L = [[0 for x in range(n)] for x in range(n)]
    # palindromes with length 1 (diagonals)
    for i in range(0, n):
        L[i][i] = 1

    # palindromes with length up to j+1 (basically proceeding to close in on upper right diagonal
    for k in range(2, n + 1):
        for i in range(0, n - k + 1):
            j = i + k - 1
            if A[i] == A[j] and k == 2:
                L[i][j] = 2
            if A[i] == A[j]:
                L[i][j] = 2 + L[i + 1][j - 1] # 2 + entry in next row, prev col
            else:
                L[i][j] = max(L[i + 1][j] , L[i][j - 1]) # max of prev entry in row, or next row same entry

    print(L)
    return L[0][n - 1]

if __name__ == '__main__':
    
    # time: O(n^2)
    print(LongestPalindromeSubsequence("AGTCMCTGA"))
    
    # L
    #       0  1  2  3  4  5  6  7  8
    #       A  G  T  C  M  C  T  G  A       
    # 0 A [[1, 1, 1, 1, 1, 3, 5, 7, 9], 
    # 1 G  [0, 1, 1, 1, 1, 3, 5, 7, 7], 
    # 2 T  [0, 0, 1, 1, 1, 3, 5, 5, 5], 
    # 3 C  [0, 0, 0, 1, 1, 3, 3, 3, 3], 
    # 4 M  [0, 0, 0, 0, 1, 1, 1, 1, 1], 
    # 5 C  [0, 0, 0, 0, 0, 1, 1, 1, 1], 
    # 6 T  [0, 0, 0, 0, 0, 0, 1, 1, 1], 
    # 7 G  [0, 0, 0, 0, 0, 0, 0, 1, 1], 
    # 8 A  [0, 0, 0, 0, 0, 0, 0, 0, 1]]