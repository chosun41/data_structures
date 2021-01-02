def validPalindrome1(s):
    for i in range(len(s)):
        t = s[:i] + s[i+1:]
        if t == t[::-1]: 
            return True

    return s == s[::-1]

def validPalindrome2(s):
    def is_pali_range(i, j):
        return all(s[k] == s[j-k+i] for k in range(i, j))

    for i in range(len(s) // 2):
        if s[i] != s[~i]:
            j = len(s) - 1 - i
            return is_pali_range(i+1, j) or is_pali_range(i, j-1)
    return True

if __name__ == '__main__':
    # time: O(n^2) space: O(n)
    print(validPalindrome1("abca"))
    # time: O(n) space: O(n)
    print(validPalindrome2("abca"))