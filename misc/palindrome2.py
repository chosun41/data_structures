def validPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    def check_palindrome(i, j):
        if i >= j:
            return True
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
    
    i = 0
    j = len(s)-1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            if check_palindrome(i+1, j) or check_palindrome(i, j-1):
                return True
            else:
                return False
    return True

if __name__=='__main__':
    # time: O(n)
    # space: O(1)
    print(validPalindrome(s = "abca"))
    print(validPalindrome(s = "abc"))
