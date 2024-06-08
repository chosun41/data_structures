def removeInvalidParentheses(s):
    def dfs(s):
        mi = valid(s)
        if mi == 0:
            ans.append(s) # dont care about if it was in visited
            return
        
        for i in range(len(s)):
            if s[i] in ('(', ')'): # check only parenthetical characters
                ns = s[:i] + s[i+1:]
                if ns not in visited and valid(ns) < mi: 
                    # number of paren to remove in candidate has to be less than current num of parens to remove
                    visited.add(ns)
                    dfs(ns)
                
    def valid(s):
        ans,bal = 0,0
        for c in s:
            ans += {'(': 1, ')': -1}.get(c,0)
            bal += ans < 0
            ans = max(ans, 0)
        return ans + bal
    
    visited = set([s])
    ans = []
    dfs(s)
    return ans
    
if __name__ == '__main__':
    # time: O(2^n) # decide whether to keep or lose the parentheses
    # space: O(n)
    print(removeInvalidParentheses("(a)())()"))
    # (a)())()
    
    # a)())()
    # (a())()
    # (a)))()
    # (a)()()
    # (a)()))
    # (a)())(
