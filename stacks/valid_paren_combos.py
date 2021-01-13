def removeInvalidParentheses(s):
    # define when a combination of parenthesis is still valid
    def valid(candidate):
        counter = 0
        for char in candidate:
            if char == "(": 
                counter += 1
            elif char == ")": 
                counter -= 1
            if counter < 0: 
                return False
        # balanced?
        return counter == 0

    res, frontier = set() , set([s])
    while not res:
        _next = set()
        for candidate in frontier:
            if valid(candidate): 
                res.add(candidate) 
                continue
            # generate more candidates based on this candidate
            for i, letter in enumerate(candidate):
                # skip trash
                if letter not in "()": 
                    continue
                _next.add(candidate[:i] + candidate[i+1:])
        frontier = _next
    return res
    
if __name__ == '__main__':
    # time: O(2^n)
    # space: O(n)
    print(removeInvalidParentheses("(a)())()"))
    # (a)())()
    
    # a)())()
    # (a())()
    # (a)))()
    # (a)()()
    # (a)()))
    # (a)())(
