# def countSubstrings(s):

#     if not s:
#         return 0
#     dp = [[False]*len(s) for _ in range(len(s))]
#     res = 0
#     for l in range(1, len(s)+1):
#         for i in range(len(s)-l+1):
#             j = i+l-1
#             if i == j:
#                 dp[i][j] = True
#                 res += 1
#             elif i+1 == j:
#                 if s[i] == s[j]:
#                     dp[i][j] = True
#                     res += 1
#             else:
#                 if s[i] == s[j] and dp[i+1][j-1]:
#                     dp[i][j] = True
#                     res += 1
#     print(dp)
#     return res

def countSubstrings( s):
    """
    :type s: str
    :rtype: int
    """
    count = 0

    # Initialize a lookup table of dimensions len(s) * len(s)
    dp = [[False for i in range(len(s))] for i in range(len(s))]
    
    # Base case: A string with one letter is always a palindrome
    for i in range(len(s)):
        dp[i][i] = True
        count += 1

    # Base case: Substrings of two letters
    for i in range(len(s)-1):
        dp[i][i + 1] = (s[i] == s[i + 1])
        # A boolean value is added to the count where True means 1 and False means 0
        count += dp[i][i + 1]

    # Substrings of lengths greater than 2
    for length in range(3, len(s)+1):
        i = 0
        # Checking every possible substring of any specific length
        for j in range(length - 1, len(s)):
            dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
            count += dp[i][j]
            i += 1

    print(dp)
    
    return count
    
if __name__=='__main__':
    # time and space: O(n^2)
    # count num of palindromic substrings
    print(countSubstrings("aaa"))