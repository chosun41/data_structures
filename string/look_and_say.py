def look_and_say(n):
    def next_number(s):
        result, i = [], 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]: # check if reached end
                i += 1
                count += 1
            result.append(str(count) + s[i]) # + s[i]
            i += 1
        return ''.join(result)

    s = '1'
    for _ in range(1, n):
        s = next_number(s)
    return s

if __name__=='__main__':
    
    # n is which number of sequence, m is count of numbers in any one row
    # 1,11,21,1211,111221 -> how many of previous there are
    # time: O(n*m)
    
    print(look_and_say(3))