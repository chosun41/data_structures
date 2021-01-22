def longestValidParentheses(s):
    stack = [] # record only the index of not valid parentheses, matched parens index will be popped
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif stack and s[stack[-1]] == '(':
            stack.pop()
        else:
            stack.append(i)
    stack = [-1] + stack + [len(s)] # -1 and length used to pick outer ranges
    ans = 0
    for i in range(len(stack)-1):
        ans = max(ans, stack[i+1]-stack[i]-1) # find difference between ranges 
    print(stack)
    return ans

if __name__ == '__main__':
    # time and space: O(n)
    # find length of longest well formed parentheses
    print(longestValidParentheses(s = ")()())"))