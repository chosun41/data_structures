def checkValidString(s):
    lo = hi = 0
    for c in s:
        lo += 1 if c == '(' else -1
        hi += 1 if c != ')' else -1
        print(lo,hi)
        if hi < 0: 
            break
        lo = max(lo, 0)

    return lo == 0

if __name__=='__main__':
    # time: O(n)
    # space: O(1)
    # return true if valid string based on parentheses, * can be a parentheses or empty string
    print(checkValidString("(*))"))
    
    # '(' lo=1,hi=1
    # '*' lo=0,hi=2
    # ')' lo=-1,hi=1
    # ')' lo=-1,hi=0
    