import functools
import string

# A for 10, B for 11, .. F for 15

def convert_base(num_as_string, b1, b2):
    def construct_from_base(num_as_int, base):
        return ('' if num_as_int == 0 else construct_from_base(num_as_int // base, base) + string.hexdigits[num_as_int % base].upper())

    is_negative = num_as_string[0] == '-'
    num_as_int = functools.reduce(lambda x, c: x * b1 + string.hexdigits.index(c.lower()),num_as_string[is_negative:], 0)
    return ('-' if is_negative else '') + ('0' if num_as_int == 0 else construct_from_base(num_as_int, b2))

if __name__=='__main__':
    
    # time: O(n(1+log b2 b1)) n - length of s, 
    
    print(convert_base("615",7,13))
    
    # 615 base 7 = 6*7^2 + 1*7 + 5 = 49*6+7+5 = 294 + 12 = 306 base 10
    # to convert to base 13
    # 306 mod 13 = 7
    # 306//13 = 23
    # 23 mod 13 = 10
    # 23//13 = 1
    # 1 mod 13 = 1
    # 1//13 0
    # in reverse 1A7