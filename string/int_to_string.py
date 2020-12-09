import functools
import string

def int_to_string(x):

    is_negative = False
    if x < 0:
        x, is_negative = -x, True

    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break

    # Adds the negative sign back if is_negative
    return ('-' if is_negative else '') + ''.join(reversed(s))


def string_to_int(s):
    
    # s[0] in '-+' -> s[0] or s[1] depending on boolean

    return (-1 if s[0] == '-' else 1) * functools.reduce(lambda running_sum, c: running_sum * 10 + string.digits.index(c),s[s[0] in '-+':],0)

if __name__=='__main__':
    
    x=int_to_string(321)
    print(x)
    print(type(x))
    y=string_to_int('-321')
    print(y)
    print(type(y))
    