def findDiagonalOrder(matrix):
    if not matrix: 
        return []
    n,m = len(matrix),len(matrix[0])
    ans = [0]*(n*m)
    r,c = 0,0
    for i in range(len(ans)):
        ans[i] = matrix[r][c]
        # Up Direction
        if (r+c)%2 == 0: # most important
            if c == m-1:
                r += 1
            elif r == 0:
                c += 1
            else:
                r -= 1
                c += 1
        # Down direction
        else:
            if r == n-1:
                c += 1
            elif c == 0:
                r += 1
            else:
                r += 1
                c -= 1
    return ans

if __name__=='__main__':
    # time and space: O(n*m)
    print(findDiagonalOrder([[1,2,3],
                            [4,5,6],
                            [7,8,9]]))