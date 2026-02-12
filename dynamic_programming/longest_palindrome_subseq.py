# def LongestPalindromeSubsequence(s):
#     n = len(s)
#     dp = [[0] * n for _ in range(n)]
    
#     # Base case: a single character is a palindrome of length 1
#     for i in range(n):
#         dp[i][i] = 1
        
#     # Iterate over substrings of length 2 to n
#     for l in range(2, n+1):
#         for i in range(n-l+1):
#             j = i + l - 1
#             if s[i] == s[j]:
#                 # If the two characters match, we can add two to the
#                 # length of the longest palindrome in the substring
#                 dp[i][j] = dp[i+1][j-1] + 2
#             else:
#                 # If the two characters don't match, we take the max
#                 # of the longest palindromes in the two substrings
#                 dp[i][j] = max(dp[i+1][j], dp[i][j-1])

#     print(dp)
    
#     return dp[0][n-1]

def LongestPalindromeSubsequence(text):
    text1, text2 = text, text[::-1]
    # Get the lengths of both input strings
    len_text1, len_text2 = len(text1), len(text2)
    
    # Initialize a 2D array (list of lists) with zeros for dynamic programming
    # The array has (len_text1 + 1) rows and (len_text2 + 1) columns
    dp_matrix = [[0] * (len_text2 + 1) for _ in range(len_text1 + 1)]
    
    # Loop through each character index of text1 and text2
    for i in range(1, len_text1 + 1):
        for j in range(1, len_text2 + 1):
            # If the characters match, take the diagonal value and add 1
            if text1[i - 1] == text2[j - 1]:
                dp_matrix[i][j] = dp_matrix[i - 1][j - 1] + 1
            else:
                # If the characters do not match, take the maximum of the value from the left and above
                dp_matrix[i][j] = max(dp_matrix[i - 1][j], dp_matrix[i][j - 1])
    
    # The bottom-right value in the matrix contains the length of the longest common subsequence
    return dp_matrix[len_text1][len_text2]

if __name__ == '__main__':
    
    # time: O(n^2) - lps is just lcs of text and reverse of text (reuse lcs solution)
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

    #  A   B  C  B  A  M  C  T  G  A
    # [[1, 1, 1, 3, 5, 5, 5, 5, 5, 5],
    # [0, 1, 1, 3, 3, 3, 3, 3, 3, 3], 
    # [0, 0, 1, 1, 1, 1, 3, 3, 3, 3],
    # [0, 0, 0, 1, 1, 1, 1, 1, 1, 3], 
    # [0, 0, 0, 0, 1, 1, 1, 1, 1, 3], 
    # [0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 
    # [0, 0, 0, 0, 0, 0, 1, 1, 1, 1], 
    # [0, 0, 0, 0, 0, 0, 0, 1, 1, 1], 
    # [0, 0, 0, 0, 0, 0, 0, 0, 1, 1], 
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]