def isValidPalindrome(s,k):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)] 
    for i in range(n + 1): 
        for j in range(n + 1): 
            if not i or not j: 
                dp[i][j] = i or j 
            elif s[i - 1] == s[n - j]: 
                dp[i][j] = dp[i - 1][j - 1] 
            else: 
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
    print(dp)
    return dp[n][n] <= k * 2


if __name__=='__main__':

    # string is k palindrome if it is palindrome after removing k characters
    # time and space: O(n^2)
    print(isValidPalindrome(s = "abcdeca", k = 2))
    # [[0, 1, 2, 3, 4, 5, 6, 7], 
    # [1, 0, 1, 2, 3, 4, 5, 6], 
    # [2, 1, 2, 3, 4, 5, 4, 5], 
    # [3, 2, 1, 2, 3, 4, 5, 6], 
    # [4, 3, 2, 3, 2, 3, 4, 5], 
    # [5, 4, 3, 2, 3, 4, 5, 6], 
    # [6, 5, 4, 3, 4, 3, 4, 5], 
    # [7, 6, 5, 4, 5, 4, 5, 4]]