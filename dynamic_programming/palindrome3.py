def isValidPalindrome(s,k):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)] 
    for i in range(n+1, 0, -1): 
        for j in range(i, n+1): 
            if s[i-1] == s[j-1]:
                dp[i][j] = 0 if j-i<2 else dp[i+1][j-1]
            else:
                dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
    print(dp)
    return dp[1][n]<=k

if __name__=='__main__':

    # string is k palindrome if it is palindrome after removing k characters
    # time and space: O(n^2) - bottom up
    print(isValidPalindrome(s = "abcdeca", k = 2))
    # [[0, 0, 0, 0, 0, 0, 0, 0], 
    # [0, 0, 1, 2, 3, 4, 3, 2], 
    # [0, 0, 0, 1, 2, 3, 2, 3], 
    # [0, 0, 0, 0, 1, 2, 1, 2], 
    # [0, 0, 0, 0, 0, 1, 2, 3], 
    # [0, 0, 0, 0, 0, 0, 1, 2], 
    # [0, 0, 0, 0, 0, 0, 0, 1], 
    # [0, 0, 0, 0, 0, 0, 0, 0]]