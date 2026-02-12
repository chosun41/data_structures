def phone_mnemonic(digits):
    mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return list(mapping[digits[0]])
    prev = phone_mnemonic(digits[:-1])
    additional = mapping[digits[-1]]
    return [s + c for s in prev for c in additional]

if __name__ == '__main__':
    
    # time and space: 0(4^n) 
    # N is the length of digits. Note that 44 in this expression is referring to the maximum value length in the hash map, and not to the length of the input.
    # The worst-case is where the input consists of only 7s and 9s. In that case, we have to explore 4 additional paths for every extra digit. Then, for each combination, it costs up to NN to build the combination. 
    # For the problem constraints, we're given, M = 4M=4, because of digits 7 and 9 having 4 letters each.
    print(phone_mnemonic('2276696'))

    # prev, additional = '227669','6' ...
    # prev, additional = '22766','9' ...
    # prev, additional = '2276','6' ...
    # prev, additional = '227','6' ...
    # prev, additional = '22','7' ['aa','ab','ac,'ba','bb','bc','ca','cb','cc'] + ['pqrs'] ^
    # prev, additional = '2','2' ['aa','ab','ac,'ba','bb','bc','ca','cb','cc'] ^ 