def countAlternatingSubarrays(nums):
    n = len(nums)
    dp = [1] * n
    
    for i in range(1, n):
        if nums[i-1] != nums[i]:
            dp[i] = dp[i - 1] + 1
    
    return sum(dp)


if __name__ == '__main__':

    print(countAlternatingSubarrays(nums = [0,1,1,1]))
    print(countAlternatingSubarrays(nums = [1,0,1,0]))

    #     You are given a 
    # binary array
    #  nums.

    # We call a 
    # subarray
    #  alternating if no two adjacent elements in the subarray have the same value.

    # Return the number of alternating subarrays in nums.

    

    # Example 1:

    # Input: nums = [0,1,1,1]

    # Output: 5

    # Explanation:

    # The following subarrays are alternating: [0], [1], [1], [1], and [0,1].

    # Example 2:

    # Input: nums = [1,0,1,0]

    # Output: 10

    # Explanation:

    # Every subarray of the array is alternating. There are 10 possible subarrays that we can choose.

    

    # Constraints:

    # 1 <= nums.length <= 105
    # nums[i] is either 0 or 1.