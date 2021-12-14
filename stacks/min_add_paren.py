def minAddToMakeValid(s):
    ans,bal = 0,0
    for c in s:
        ans += {'(': 1, ')': -1}.get(c,0)
        bal += ans < 0
        ans = max(ans, 0)
    return ans + bal

if __name__=='__main__':
    print(minAddToMakeValid(s = "((("))
    print(minAddToMakeValid(s = "()))(("))