def myPow(x, n):
    if not n:
        return 1
    if n < 0:
        return 1 / myPow(x, -n)
    if n % 2==1:
        return x * myPow(x, n-1)
    return myPow(x*x, n//2)

if __name__=='__main__':
    # time and space: O(logn)
    print(myPow(x = 2.00000, n = 3))