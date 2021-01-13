def maxSubArrayLen(nums, k):
    res = 0
    preSums = {0: -1}
    s = 0
    for i,x in enumerate(nums):
        s += x
        if s - k in preSums:
            res = max(res, i - preSums[s-k])
        if s not in preSums:
            preSums[s] = i
    return res
    
if __name__=='__main__':
    # time and space: O(n)
    print(maxSubArrayLen(nums = [1, -1, 5, -2, 3], k = 3))
