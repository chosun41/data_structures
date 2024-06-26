def MaxContiguousSum3(A):
    maxSum = 0
    n = len(A)
    M = [0] * (n + 1)
    if(A[0] > 0): 
         M[0] = A[0]
    else: 
        M[0] = 0
    for i in range(1, n): 
        if(M[i - 1] + A[i] > 0):
            M[i] = M[i - 1] + A[i]
        else: 
            M[i] = 0

    for i in range(0, n): 
        if(M[i] > maxSum):
            maxSum = M[i]

    print(M)
    return maxSum

def MaxContiguousSum4(A):
    sumSoFar = sumEndingHere = 0
    n = len(A)
    for i in range(0, n) :
        sumEndingHere = sumEndingHere + A[i]
        if(sumEndingHere < 0):
            sumEndingHere = 0 # just reset when it becomes below 0
            continue
        if(sumSoFar < sumEndingHere):
            sumSoFar = sumEndingHere

    return sumSoFar

if __name__=='__main__':
    
    # MaxContiguousSum3 - time:O(n),space:O(n)
    # MaxContiguousSum4 - time:O(n),space:O(1)
    
    A = [-2,11,-4,13,-5,2]
    print(MaxContiguousSum3(A))
    print(MaxContiguousSum4(A))
    # sumsofar=0,sumendinghere=0,n=6
    # i=0,sumendinghere=-2,sumendinghere=0
    # i=1,sumendinghere=11,sumsofar=11
    # i=2,sumendinghere=7
    # i=3,sumendinghere=20,sumsofar=20
    # i=4,sumendinghere=15,sumsofar=20
    # i=5,sumendinghere=17,sumsofar=20
    
    B=[1,-3,4,-2,-1,6]
    print(MaxContiguousSum3(B))
    print(MaxContiguousSum4(B))
    # sumsofar=0,sumendinghere=0,n=6
    # i=0,sumendinghere=1,sumsofar=1
    # i=1,sumendinghere=-2,sumendinghere=0
    # i=2,sumendinghere=4,sumsofar=4
    # i=3,sumendinghere=2,sumsofar=4
    # i=4,sumendinghere=1,sumsofar=4
    # i=5,sumendinghere=7,sumsofar=7