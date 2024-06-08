def maxSubArrayLen(nums, k):
    res = 0
    preSums = {0: -1}
    s = 0
    for i,x in enumerate(nums):
        s += x # running total
        if s - k in preSums:
            res = max(res, i - preSums[s-k])
        if s not in preSums: # not an else 
            preSums[s] = i
        print(preSums,s,res)
    return res
    
if __name__=='__main__':
    # time and space: O(n)
    # max subarray whose sum equals k
    # presums is dict of running total start at what index
    print(maxSubArrayLen(nums = [1, -1, 5, -2, 3], k = 3))
