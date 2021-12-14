
def maxLength(ribbons,k):
    total = sum(ribbons)
    if k > total:
        return 0
    
    lo, hi = 1, min(total // k, max(ribbons)) # minimum max of ribbon lengths or sum ribbons//k pieces, lo hi stand for max ribbon length
    
    while lo < hi: # binary search
        mid = (lo + hi+1) // 2
        if sum(x // mid for x in ribbons) >= k: #>=
            lo = mid
        else:
            hi = mid - 1
    
    return lo

if __name__ == '__main__':

    # time: O(logn)
    # space: O(1)

    # You are given an integer array ribbons, where ribbons[i] represents the length of the ith ribbon, and an integer k. You may cut any of the ribbons into any number of segments of positive integer lengths, or perform no cuts at all.

    # For example, if you have a ribbon of length 4, you can:
    # Keep the ribbon of length 4,
    # Cut it into one ribbon of length 3 and one ribbon of length 1,
    # Cut it into two ribbons of length 2,
    # Cut it into one ribbon of length 2 and two ribbons of length 1, or
    # Cut it into four ribbons of length 1.
    # Your goal is to obtain k ribbons of all the same positive integer length. You are allowed to throw away any excess ribbon as a result of cutting.

    # Return the maximum possible positive integer length that you can obtain k ribbons of, or 0 if you cannot obtain k ribbons of the same length.

    print(maxLength(ribbons = [9,7,5], k = 3))

    print(maxLength(ribbons = [7,5,9], k = 4))