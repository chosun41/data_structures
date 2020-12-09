import itertools

def look_and_say(n):
    def next_number(s):
        result, i = [], 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1
            result.append(str(count) + s[i])
            i += 1
        return ''.join(result)

    s = '1'
    for _ in range(1, n):
        s = next_number(s)
    return s


# Pythonic solution uses the power of itertools.groupby().
def look_and_say_pythonic(n):
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(list(group))) + key for key, group in itertools.groupby(s))
    return s

if __name__=='__main__':
    
    # n is which number of sequence
    # 1,11,21,1211,111221 -> how many of previous there are
    # time: O(n*2^n)
    
    print(look_and_say(3))
    print(look_and_say_pythonic(3))