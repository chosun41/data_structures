def countSubstrings(s):
    count = 0
    
    def expand(left, right):
        res = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            res += 1
            left -= 1
            right += 1
        return res
        
    for i in range(len(s)):
        count += expand(i, i)     # Odd
        count += expand(i, i + 1) # Even
        
    return count

if __name__ == '__main__':
    print(countSubstrings("aaa"))
     # Given a string s, return the number of palindromic substrings in it.

    # A string is a palindrome when it reads the same backward as forward.

    # A substring is a contiguous sequence of characters within the string.

    

    # Example 1:

    # Input: s = "abc"
    # Output: 3
    # Explanation: Three palindromic strings: "a", "b", "c".
    # Example 2:

    # Input: s = "aaa"
    # Output: 6
    # Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
    