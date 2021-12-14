def ReversingString(str):
    s = list(str)
    end = len(str) - 1
    start = 0

    while (start < end):
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

    return "".join(s)

if __name__=='__main__':
    
    # time: O(n) space: O(n)
    str = "CareerMonk Publications."
    print(ReversingString(str))
    print(str[::-1])