from deque import Deque
    
def palindromeCheckerWithDeque(str1):
    d1 = Deque()

    for ch in str1:
        d1.addRear(ch)
    
    while d1.size() > 1 and eq1:
        first=d1.removeFront()
        last=d1.removeRear()
        if first!=last:
            return False

    return True

if __name__ == "__main__":
    
    # basically since you have a front (end) and rear (start) to access, you can pop from both sides as a pair
    # and then compare until you reach the middle
    # when it doesn't match, set to False and break immediately
    print(palindromeCheckerWithDeque("lsdkjfskf"))
    print(palindromeCheckerWithDeque("madam"))