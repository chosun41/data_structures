
def subarraySum(nums, k):
    sub_num = {0:1}
    total = count = 0

    for n in nums:
        total += n
        
        if total - k in sub_num:
            count += sub_num[total-k]
        
        sub_num[total] = 1 + sub_num.get(total, 0)
    
    return count

if __name__ == '__main__':

    print(subarraySum(nums = [1,2,3], k = 3))
    
    # Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

    # A subarray is a contiguous non-empty sequence of elements within an array.

    

    # Example 1:

    # Input: nums = [1,1,1], k = 2
    # Output: 2
    # Example 2:

    # Input: nums = [1,2,3], k = 3
    # Output: 2
    

    # Constraints:

    # 1 <= nums.length <= 2 * 104
    # -1000 <= nums[i] <= 1000
    # -107 <= k <= 107