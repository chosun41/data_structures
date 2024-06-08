def LongestPalindromeSubsequence(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    # Base case: a single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1
        
    # Iterate over substrings of length 2 to n
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            if s[i] == s[j]:
                # If the two characters match, we can add two to the
                # length of the longest palindrome in the substring
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                # If the two characters don't match, we take the max
                # of the longest palindromes in the two substrings
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
    return dp[0][n-1]

if __name__ == '__main__':
    
    # time: O(n^2)
    print(LongestPalindromeSubsequence("AGTCMCTGA"))
    print(LongestPalindromeSubsequence("ABCBAMCTGA"))
    
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