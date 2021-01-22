def Fibo1(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return Fibo1(n-1)+Fibo1(n-2)
    
def Fibo2(n):
    # append
    fibTable = [0, 1]
    for i in range(2, n + 1):
        fibTable.append(fibTable[i - 1] + fibTable[i - 2])
    return fibTable[n]

fibTable = {1:1, 2:1}
def Fibo3(n):
    # return recursive
    if n <= 2:
        return 1
    if n in fibTable:
        return fibTable[n]
    else:
        fibTable[n] = Fibo3(n - 1) + Fibo3(n - 2)
    return fibTable[n]

def Fibo4(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

if __name__=='__main__':
    
    # Fibo1 - time:O(2^n)
    # Fibo2,3 - time:O(n), space:O(n)
    # Fibo4 - time: O(n), space:O(1)
    print(Fibo1(10))
    print(Fibo2(10))
    print(Fibo3(10))
    print(Fibo4(10))