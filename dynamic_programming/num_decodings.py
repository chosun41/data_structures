def numDecodings(s):
    if not s or s[0] == '0':
        return 0
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n+1): # starting character and character before it is not 0
        if 1 <= int(s[i-1]) <= 9:
            dp[i] += dp[i-1]
        if 10 <= int(s[i-2:i]) <= 26:
            dp[i] += dp[i-2]
    print(dp)
    return dp[n]
    
if __name__=='__main__':
    # time and space: O(n) 
    # number of different encodings from integer
    # a-1 to z-26
    # "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6)
    print(numDecodings(s = "226"))
    