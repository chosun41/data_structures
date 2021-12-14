from collections import deque
    
def palindromeCheckerWithDeque(str1):
    d1 = deque(str1)
   
    while len(d1)>1:
        first=d1.popleft()
        last=d1.pop()
        if first!=last:
            return False

    return True

if __name__ == "__main__":
    
    # basically since you have a front (end) and rear (start) to access, you can pop from both sides as a pair
    # and then compare until you reach the middle
    # when it doesn't match, set to False and break immediately
    print(palindromeCheckerWithDeque("lsdkjfskf"))
    print(palindromeCheckerWithDeque("madam"))