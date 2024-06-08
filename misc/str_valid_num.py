def isNumber(s):
    """
    :type s: str
    :rtype: bool
    """
    s = s.strip()
    met_dot = met_e = met_digit = False
    for i, char in enumerate(s):
        if char in '+-':
            if i > 0 and s[i-1] != 'e': # !!!only time you have it after 1st index is right after an e
                return False
        elif char == '.':
            if met_dot or met_e: # dot must be before e and only one dot
                return False
            met_dot = True
        elif char == 'e':
            if met_e or not met_digit: # must be after a digit and only one e
                return False
            met_e, met_digit = True, False # reset met digit, since there should be one after an e
        elif char.isdigit():
            met_digit = True
        else:
            return False # any other character
    return met_digit

if __name__=='__main__':
    # time: O(n)
    # space: O(1)
    print(isNumber("2e10"))
    print(isNumber("1e.1"))