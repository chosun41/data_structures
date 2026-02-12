def Knapsack(cap, val, wt):
    n = len(val)
    dp = [[0 for j in range(cap+1)] for i in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1, cap+1):
            if wt[i-1]<=j:
                dp[i][j] = max(dp[i-1][j], val[i-1] + dp[i-1][j-wt[i-1]])
            else:
                dp[i][j] = dp[i-1][j]

    print(dp)
    return dp[n][cap]


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
    # 4  [0, 0, 30, 50, 70, 80]] 2 50 + 30 from 3,3 vs 3,5
