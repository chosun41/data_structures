# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    
    s=list(s)
    print(s)
    def reverse_range(s, start, finish):
        while start < finish:
            s[start], s[finish] = s[finish], s[start]
            start, finish = start + 1, finish - 1

    # First, reverse the whole string.
    reverse_range(s, 0, len(s) - 1)

    start = 0
    while True:
        finish = start
        while finish < len(s) and s[finish] != ' ':
            finish += 1
        if finish == len(s):
            break
        # Reverses each word in the string.
        reverse_range(s, start, finish - 1)
        start = finish + 1
    # Reverses the last word.
    reverse_range(s, start, len(s) - 1)
    return s

if __name__=='__main__':
    
    #time: O(n) space: O(1)
    
    # ram is costly -> yltsoc si mar (reverse) -> reverse individual words
    print(reverse_words('ram is costly'))
    