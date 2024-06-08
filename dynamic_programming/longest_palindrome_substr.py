def longestPalSubstr(s):
    p = ''
    for i in range(len(s)):
        # these palindrome functions starting from the center and expanding out
        p1 = get_palindrome(s, i, i+1)
        p2 = get_palindrome(s, i, i)
        p = max([p, p1, p2], key=len)
    return p

def get_palindrome(s,l,r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]

if __name__ == '__main__':
    
    # time: O(n^2)
    
    print(longestPalSubstr('cabcbaabac'))