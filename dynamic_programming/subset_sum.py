def SubsetSum1(A, X):
    # preliminary
    if X < 0 or X > sum(A):  # T = sum(A)
        return False

    # algorithm
    subSum = [False] * (X+1)
    subSum[0] = True
    p = 0
    while not subSum[X] and p < len(A): # p and q close in at each other, see if q-a fits
        a = A[p]
        q = X
        while not subSum[X] and q >= a:
            if not subSum[q] and subSum[q - a]:
                subSum[q] = True
            q -= 1
        p += 1
    print(subSum)
    return subSum[X]

if __name__ == '__main__':
    
    # time: O(nX), space: O(X)
    
    A = [3, 2, 4, 19, 3, 7, 13, 10, 6, 11]
    print(SubsetSum1(A,17))

    # p=0,subSum=[True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    # a=3,q=17,subSum[14]=False,q=16
    # ...
    # a=3,q=3,subSum[0]=True,subsum=[True,False,False,True,...],q=2,p=1
    # a=2,q=17,subSum[15]=False
    # ...
    # a=2,q=5,subsum[3]=True,subsum=[True,False,False,True,False,True...],q=4
    # ...
    # a=2,q=2,subsum[0]=True,subsum=[True,False,True,True,False,True],q=1,p=2
    # a=4,q=17,subsum[13]=False,q=16
    # ...
    # a=4,q=9,subsum[5]=True,subsum=[True,False,True,True,False,True,False,False,False,True,...]
    # ..
    # a=4,q=7,subsum[3]=True,subsum=[True,False,True,True,False,True,False,True,False,True,...]
    # a=4,q=6,subsum[2]=True,subsum=[True,False,True,True,False,True,True,True,False,True,...]
    # ..
    # a=4,q=4,subsum[0]=True,subsum=[True,False,True,True,True,True,True,True,False,True,...],p=3
    # a=19,q=17,p=4
    # a=3,q=17,subsum[14]=False
    # ..
    # a=3,q=12,subsum[9]=True,subsum=[True,False,True,True,True,True,True,True,False,True,False,False,True,..]
    # ..
    # a=3,q=10,subsum[7]=True,subsum=[True,False,True,True,True,True,True,True,False,True,True,False,True,..]
    # ..
    # a=3,q=8,subsum[5]=True,subsum=[True,False,True,True,True,True,True,True,True,True,True,False,True,..]
    # ..
    # a=3,q=3,subsum[0]=True,subsum=[True,False,True,True,True,True,True,True,True,True,True,False,True,..],p=5
    # ..
    # a=7,q=17,subsum[10]=True,subsum=[True,False,True,True,True,True,True,True,True,True,True,False,True,False,False,False,False,True]