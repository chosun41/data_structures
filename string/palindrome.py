def is_palindrome1(s):
    return all(s[i]==s[~i] for i in range(len(s)//2))

def is_palindrome2(s):

    # i moves forward, and j moves backward.
    i, j = 0, len(s) - 1
    while i < j:
        # i and j both skip non-alphanumeric characters.
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i, j = i + 1, j - 1
    return True

if __name__=='__main__':
    
    # time: O(n)
    
    print(is_palindrome1('hahah'))
    print(is_palindrome1('haha'))
    
    print(is_palindrome2('hahah'))
    print(is_palindrome2('haha'))
