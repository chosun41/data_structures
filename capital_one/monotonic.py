def isMonotonic(A):
    increasing = decreasing = True

    for i in range(len(A) - 1):
        if A[i] > A[i+1]:
            increasing = False
        if A[i] < A[i+1]:
            decreasing = False

    return increasing or decreasing
    
if __name__ =='__main__':
    # time: O(n)
    # space: O(1)
    print(isMonotonic([1,2,2,3]))
    print(isMonotonic([1,3,2]))
        