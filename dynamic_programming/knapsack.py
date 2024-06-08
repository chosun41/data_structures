def Knapsack(cap, val, wt):
    n=len(val)
    M = [[0 for x in range(cap + 1)] for x in range(n+1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n+1): 
        for j in range(cap + 1): 
            if i == 0 or j == 0: # 0s for first col and first row
                M[i][j] = 0
            elif wt[i-1] <= j: # if you can fit item i-1 size, take max of prev row and item value + value from prev row and j-item weight
                M[i][j] = max(val[i-1] + M[i-1][j-wt[i-1]], M[i-1][j]) 
            else: 
                M[i][j] = M[i-1][j] # else copy value from prev row
  
    print(M)
    return M[n][cap] 


if __name__=='__main__':
    
    # knapsack of itemvalue and itemweight, maximum value and satisfies weight constraint
    
    print(Knapsack(5,[60,50,70,30],[5,3,4,2]))
    
    # time: O(nw)
    
    #              M
    #     0  1  2   3   4   5
    # 0 [[0, 0, 0,  0,  0,  0], 
    # 1  [0, 0, 0,  0,  0,  60], 5
    # 2  [0, 0, 0,  50, 50, 60], 3
    # 3  [0, 0, 0,  50, 70, 70], 4
    # 4  [0, 0, 30, 50, 70, 80]] 2
