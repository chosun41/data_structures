import itertools

def decoding(s):

    count, result = 0, []
    for c in s:
        if c.isdigit():
            count = count * 10 + int(c) #in case more than 2 digits
        else:  # c is a letter of alphabet.
            result.append(c * count)  # Appends count copies of c to result.
            count = 0
    return ''.join(result)


def encoding(s):

    result, count = [], 1
    for i in range(1, len(s) + 1): # +1 important as well as i==len(s), need last part because we always append i-1
        if i == len(s) or s[i] != s[i - 1]:
            # Found new character so write the count of previous character.
            result.append(str(count) + s[i - 1])
            count = 1
        else:  # s[i] == s[i - 1].
            count += 1
    return ''.join(result)
    
    
if __name__=='__main__':
    
    # time: O(n) 
    
    x=encoding('aaaabccccaa')
    print(x) # 4a1b4c2a
    print(decoding(x))