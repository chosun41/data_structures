def intervalIntersection(A, B):
    ans = []
    i = j = 0

    while i < len(A) and j < len(B):
        # Let's check if A[i] intersects B[j].
        # lo - the startpoint of the intersection
        # hi - the endpoint of the intersection
        lo = max(A[i][0], B[j][0])
        hi = min(A[i][1], B[j][1])
        if lo <= hi: # important
            ans.append([lo, hi])

        # Remove the interval with the smallest endpoint
        if A[i][1] < B[j][1]: # end of interval not start of interval
            i += 1
        else:
            j += 1

    return ans

if __name__=='__main__':
    # time: O(m+n)
    # space: O(m+n)
    # start from beginning index, compare and add if to ans if it makes sense, increment
    print(intervalIntersection(A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]))