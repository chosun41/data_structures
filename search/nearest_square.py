def square_root(k):

    left, right = 0, k
    # Candidate interval [left, right] where everything before left has square
    # <= k, everything after right has square > k.
    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid
        if mid_squared <= k:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1

    
if __name__=='__main__':
    
    # take nonnegative integer and returns the largest intger whose square is <= k
    # time: O(log k)
    
    print(square_root(300)) #17^2=289, 18^2=324
    
    # 0. left=0, right=300
    #    mid = 150
    #    150^2>300 -> right=149
    # 1. left=0, right=149
    #    mid = 74
    #    74^2>300 -> right=73
    # 2. left=0, right=73
    #    mid = 36
    #    36^2>300 -> right=35
    # 3. left=0,right=35
    #    mid=17
    #    17^2<=300 -> left=18
    # 4. left=18,right=35
    #    mid = 26
    #    26^2>300 -> right=25
    # 5. left=18,right=25
    #    mid = 22
    #    22^2>300 -> right=21
    # 6. left=18,right=21
    #    mid = 19
    #    19^2>300 -> right=18
    # 7. left=18,right=18
    #    mid=18
    #    18^2>300 -> right=17
    #    return 17
    print(square_root(16)) #4^2=16