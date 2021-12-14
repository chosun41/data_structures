def validPalindrome1(s):
    for i in range(len(s)):
        t = s[:i] + s[i+1:]
        if t == t[::-1]: 
            return True

    return s == s[::-1]

def validPalindrome2(s):
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
    while i < j: # not i<=j
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            if check_palindrome(i+1, j) or check_palindrome(i, j-1):
                return True
            else:
                return False
    return True

if __name__ == '__main__':
    # if you remove one letter, is it a valid palindrome
    # time: O(n^2) space: O(n)
    print(validPalindrome1("abca"))
    # time: O(n) space: O(n)
    print(validPalindrome2("abca"))