def searchRange(A, target):

    lmost = leftsearch(A,target)
    rmost = rightsearch(A,target)
    return [lmost,rmost]

def leftsearch(A,tar):
    l = 0
    r = len(A)-1
    tarI = -1#target index
    while l <= r: # close in on mid
        mid = (l+r)//2
        if A[mid] > tar:
            r = mid - 1
        elif A[mid] < tar:
            l = mid + 1
        else:
            tarI = mid
            r = mid - 1 # most important because of the l<=r condition or else while condition continues
    return tarI

def rightsearch(A,tar):
    l = 0
    r = len(A)-1
    tarI = -1
    while l <= r: # close in on mid
        mid = (l+r)//2
        if A[mid] > tar:
            r = mid -1
        elif A[mid] <tar:
            l = mid + 1
        else:
            tarI = mid
            l = mid+1 # most important
    return tarI

if __name__=='__main__':
    # time: O(logn)
    # space: O(1)
    # return back start and ending index of target
    print(searchRange([5,7,7,8,8,10], target = 8))
    print(searchRange([5,7,7,8,8,10], target = 6))