def subarraysWithKDistinct(nums, k):
    cnt, res, l, m = [0] * (len(nums) + 1), 0, 0, 0
    for n in nums:
        cnt[n] += 1
        if cnt[n] == 1:
            k -= 1
            if (k < 0):
                cnt[nums[m]] = 0
                m += 1
                l = m
        if k <= 0:
            while(cnt[nums[m]] > 1):
                cnt[nums[m]] -= 1
                m += 1
            res += m - l + 1
    return res

if __name__ == '__main__':
    print(subarraysWithKDistinct(nums = [1,2,1,2,3], k = 2))

   # Given an integer array nums and an integer k, return the number of good subarrays of nums.

    # A good array is an array where the number of different integers in that array is exactly k.

    # For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
    # A subarray is a contiguous part of an array.

    

    # Example 1:

    # Input: nums = [1,2,1,2,3], k = 2
    # Output: 7
    # Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
    # Example 2:

    # Input: nums = [1,2,1,3,4], k = 3
    # Output: 3
    # Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
    