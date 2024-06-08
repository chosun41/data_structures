def longestValidParentheses(s):
    max_length = 0
    stk=[-1]
    for i in range(len(s)):
        if s[i] == '(':
            stk.append(i)
        else:
            if stk:
                stk.pop()
                
            if stk:
                max_length = max(max_length, i-stk[-1])
            else:
                stk.append(i)
            
    print(stk)

    return max_length

if __name__ == '__main__':
    # time and space: O(n)
    # find length of longest well formed parentheses
    print(longestValidParentheses(s = ")()())"))