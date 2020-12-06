import collections

def can_form_palindrome(s):

    # A string can be permuted to form a palindrome if and only if the number
    # of chars whose frequencies is odd is at most 1.
    return sum(v % 2 for v in collections.Counter(s).values()) <= 1

if __name__=='__main__':
    
    # this is you permutate a string
    
    print(can_form_palindrome("hahah"))
    print(can_form_palindrome("halas"))