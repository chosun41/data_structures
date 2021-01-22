def isOneEditDistance(s, t):
    if s == t:
        return False
    l1, l2 = len(s), len(t)
    if l1 > l2: # force s no longer than t
        return isOneEditDistance(t, s)
    if l2 - l1 > 1:
        return False
    for i in range(len(s)):
        if s[i] != t[i]:
            if l1 == l2:
                s = s[:i]+t[i]+s[i+1:]  # replacement
            else:
                s = s[:i]+t[i]+s[i:]  # insertion
            break
    return s == t 

if __name__=='__main__':
    # time: O(s+t)
    # space: O(1)
    print(isOneEditDistance(s = "ab", t = "acb"))
    