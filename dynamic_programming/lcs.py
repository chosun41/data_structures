def LCS(X, Y):
    if not X or not Y:
        return ""
    x, m, y, n = X[0], X[1:], Y[0], Y[1:]
    if x == y:
        return x+LCS(m, n)
    else:
        # Use key=len to select the maximum string in a list efficiently
        return max(LCS(X, n), LCS(m, Y), key=len)

def LCS2(X, Y):
    Table = [[0 for j in range(len(Y) + 1)] for i in range(len(X) + 1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(X):
        for j, y in enumerate(Y):
            if x == y:
                Table[i + 1][j + 1] = Table[i][j] + 1 # se entry is current + 1
            else:
                Table[i + 1][j + 1] = max(Table[i + 1][j], Table[i][j + 1]) # se entry max of below or to the right
    # read the substring out from the matrix
    result = ""
    x, y = len(X), len(Y)
    print(Table)
    while x != 0 and y != 0:
        if Table[x][y] == Table[x - 1][y]:
            x -= 1
        elif Table[x][y] == Table[x][y - 1]:
            y -= 1
        else:
            assert X[x - 1] == Y[y - 1]
            result = X[x - 1] + result
            x -= 1
            y -= 1
    return result

if __name__=='__main__':
    
    # least common subsequence, left to right not necessarily contiguous sequence
    # lcslength1 - time: O(2^n)
    # lcslength2 - time: O(mn), space: O(mn) (b/c of table)
    print("Longest common subsequence: ", LCS('ABCBDAB', 'BDCABA'))
    print("Longest common subsequence: ", LCS2('ABCBDAB', 'BDCABA'))
    
    #        0  1  2  3  4  5  6
    #        B  D  C  A  B  A
    #  0 A [[0, 0, 0, 0, 0, 0, 0], 
    #  1 B  [0, 0, 0, 0, 1, 1, 1], 
    #  2 C  [0, 1, 1, 1, 1, 2, 2], 
    #  3 B  [0, 1, 1, 2, 2, 2, 2], 
    #  4 D  [0, 1, 1, 2, 2, 3, 3], 
    #  5 A  [0, 1, 2, 2, 2, 3, 3], 
    #  6 B  [0, 1, 2, 2, 3, 3, 4], 
    #  7    [0, 1, 2, 2, 3, 4, 4]]
    # x=7,y=6, T[7][6]=T[6][6], x=6,y=6
    # x=6,y=6  T[6][6]!=T[5][6],T[6][6]!=T[6][5],result='A'
    # x=5,y=5  T[5][5]=T[4][5],x=4,y=5
    # x=4,y=5  T[4][5]!=T[3][5],T[4][5]!=T[4][4],result='BA'
    # x=3,y=4  T[3][4]!=T[2][4],T[3][4]=T[3][3],x=3,y=3
    # x=3,y=3  T[3][3]!=T[2][3],T[3][3]!=T[3][2],result='CBA'
    # x=2,y=2  T[2][2]!=T[1][2],T[2][2]=T[2][1],x=2,y=1
    # x=2,y=1  T[2][1]!=T[1][1],T[2][1],T[2][0],result='BCBA'
    # x=1,y=0 stop