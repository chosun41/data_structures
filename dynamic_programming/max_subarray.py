def maxSubArray(nums):
    n = len(nums)
    max_sum = nums[0]
    for i in range(1, n):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1] 
        max_sum = max(nums[i], max_sum)
        
    print(nums)

    return max_sum

if __name__=='__main__':
    # time: O(n)
    # space: O(1)
    # find max sum of contiguous subarray with at least one element
    # rewrite in place if previous element is >0
    print(maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4])) # 4,-1,2,1 ->6