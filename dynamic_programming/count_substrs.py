def countSubstrings(s):

    if not s:
        return 0
    dp = [[False]*len(s) for _ in range(len(s))]
    res = 0
    for l in range(1, len(s)+1):
        for i in range(len(s)-l+1):
            j = i+l-1
            if i == j:
                dp[i][j] = True
                res += 1
            elif i+1 == j:
                if s[i] == s[j]:
                    dp[i][j] = True
                    res += 1
            else:
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    res += 1
    print(dp)
    return res
    
if __name__=='__main__':
    # time and space: O(n^2)
    # count num of palindromic substrings
    print(countSubstrings("aaa"))