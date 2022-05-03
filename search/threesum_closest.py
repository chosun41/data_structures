def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    closest_sum = 2**31-1
    for i in range(len(nums)):
        j,k = i+1, len(nums)-1
        while j<k:
            curr_sum = nums[i] + nums[j] + nums[k]
            if curr_sum == target:
                return curr_sum
            if abs(curr_sum-target) < abs(closest_sum-target):
                closest_sum = curr_sum
            if curr_sum < target: #most important
                j = j+1
            else:
                k = k-1
    return closest_sum

if __name__=='__main__':

    # time: O(n^2)

    # Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

    # Return the sum of the three integers.

    # You may assume that each input would have exactly one solution.

    print(threeSumClosest(nums = [-1,2,1,-4], target = 1))