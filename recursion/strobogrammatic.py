def isStrobogrammatic(num):

    rotated_digits = ['0', '1', '', '', '', '', '9', '', '8', '6']

    rotated_string_builder = []

    for c in reversed(num):
        rotated_string_builder.append(rotated_digits[int(c)])

    rotated_string = "".join(rotated_string_builder)
    return rotated_string == num

if __name__=='__main__':
    
    # time: O(n)
    # space: O(1)
    print(isStrobogrammatic("69"))
    print(isStrobogrammatic("962"))
