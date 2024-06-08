def Fibo2(n):
    # append
    fibTable = [0, 1]
    for i in range(2, n + 1):
        fibTable.append(fibTable[i - 1] + fibTable[i - 2])
    return fibTable[n]

fibTable = {1:1, 2:1}

def Fibo4(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

if __name__=='__main__':

    # Fibo2 - time:O(n), space:O(n)
    # Fibo4 - time: O(n), space:O(1)
    print(Fibo2(10))
    # i, fibTable = 0, [0, 1]
    # i, fibTable = 1, [0, 1, 1]
    # i, fibTable = 2, [0, 1, 1, 2]
    # i, fibTable = 3, [0, 1, 1, 2, 3]
    # i, fibTable = 4, [0, 1, 1, 2, 3, 5]
    # i, fibTable = 5, [0, 1, 1, 2, 3, 5, 8]
    # i, fibTable = 6, [0, 1, 1, 2, 3, 5, 8, 13]
    # i, fibTable = 7, [0, 1, 1, 2, 3, 5, 8, 13, 21]
    # i, fibTable = 8, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    # i, fibTable = 9, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    print(Fibo4(10))
    # i,a,b = 0,0,1
    # i,a,b = 1,1,1
    # i,a,b = 2,1,2
    # i,a,b = 3,2,3
    # i,a,b = 4,3,5
    # i,a,b = 5,5,8
    # i,a,b = 6,8,13
    # i,a,b = 7,13,21
    # i,a,b = 8,21,34
    # i,a,b = 9,34,55