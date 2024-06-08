def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    n = len(s)
    m = len(p)
    dp = [[False]*(n+1) for _ in range(m+1)]
    dp[0][0] = True
    for i in range(m):
        for j in range(-1, n):
            if j == -1:
                if p[i] == "*":
                    dp[i+1][j+1] = dp[i-1][j+1] # i -1?
                continue
            if p[i].isalpha():
                if p[i] == s[j]:
                    dp[i+1][j+1] = dp[i][j]
            elif p[i] == ".":
                dp[i+1][j+1] = dp[i][j]
            else:
                dp[i+1][j+1] = dp[i-1][j+1] or (dp[i+1][j] and (p[i-1] == s[j] or p[i-1] == "."))
    print(dp)
    return dp[-1][-1]

if __name__ == '__main__':
    s = "aa"
    p = "a*"
    print(isMatch(s, p))
    s = "aa"
    p = "a"
    print(isMatch(s, p))