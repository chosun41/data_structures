from collections import deque

def longestSubarray(nums, limit):
    maxq = deque()
    minq = deque()
    n = len(nums)
    j = 0
    ans = 0
    for i in range(n):
        while maxq and nums[i] > maxq[-1]:
            maxq.pop()
        maxq.append(nums[i])
        while minq and nums[i] < minq[-1]:
            minq.pop()
        minq.append(nums[i])

        print(i, maxq, minq)

        if maxq[0] - minq[0] > limit:
            if nums[j] == maxq[0]:
                maxq.popleft()
            if nums[j] == minq[0]:
                minq.popleft()
            j += 1

        print(j, maxq, minq)
        ans = max(ans, i - j + 1)
    return ans

if __name__ == '__main__':

    print(longestSubarray(nums = [8,2,4,7], limit = 4))
    print(longestSubarray(nums = [10,1,2,4,7,2], limit = 5))
    print(longestSubarray(nums = [4,2,2,2,4,4,2,2], limit = 0))

# Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

 

# Example 1:

# Input: nums = [8,2,4,7], limit = 4
# Output: 2 
# Explanation: All subarrays are: 
# [8] with maximum absolute diff |8-8| = 0 <= 4.
# [8,2] with maximum absolute diff |8-2| = 6 > 4. 
# [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
# [2] with maximum absolute diff |2-2| = 0 <= 4.
# [2,4] with maximum absolute diff |2-4| = 2 <= 4.
# [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
# [4] with maximum absolute diff |4-4| = 0 <= 4.
# [4,7] with maximum absolute diff |4-7| = 3 <= 4.
# [7] with maximum absolute diff |7-7| = 0 <= 4. 
# Therefore, the size of the longest subarray is 2.
# Example 2:

# Input: nums = [10,1,2,4,7,2], limit = 5
# Output: 4 
# Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
# Example 3:

# Input: nums = [4,2,2,2,4,4,2,2], limit = 0
# Output: 3

# Let n be the length of the array nums.

# Approach 3: Two Deques
# Intuition
# While heaps are commonly used to track max and min values, their frequent insertion and removal operations are inefficient (O(logn) time). Deques, or double-ended queues, offer efficient O(1) time complexity for adding and removing elements from both ends and are more suitable for this problem.

# We use two deques for this problem. One deque maintains numbers in decreasing order, ensuring the largest number in the window is always at the front. If a new number exceeds those at the deque's end, we remove those elements since they can no longer be the maximum in the current window.

# Similarly, the other deque will maintain the numbers in increasing order, ensuring the smallest number in the window is always at the front. If a new number is smaller than those at the deque's end, it replaces them, ensuring accuracy for the current window's minimum.

# These deques hold all the potential minimum and maximum values for the current and future windows.

# When expanding the window to include a new element, we add it to both deques while preserving their order. If the absolute difference between the maximum and minimum values at the front of the deques exceeds the limit, we shrink the window by moving the left pointer. Removing elements from the front of either deque maintains the correct min and max values in constant time, enabling efficient checks to ensure the window stays within the limit.

# Algorithm
# Initialization:
# Initialize two deques, maxDeque and minDeque.
# Initialize left to 0 to represent the start of the sliding window.
# Initialize maxLength to 0 to store the length of the longest valid subarray.
# Iterate through the array nums from left to right using a variable right:
# For each element nums[right]:
# Maintain the maxDeque in decreasing order:
# While maxDeque is not empty and the last element in maxDeque is less than nums[right]:
# Remove the last element from maxDeque.
# Add nums[right] to the back of maxDeque.
# Maintain the minDeque in increasing order:
# While minDeque is not empty and the last element in minDeque is greater than nums[right]:
# Remove the last element from minDeque.
# Add nums[right] to the back of minDeque.
# Check if the current window exceeds the limit:
# While the absolute difference between the first elements of maxDeque and minDeque is greater than limit:
# If the first element of maxDeque is equal to nums[left]:
# Remove the first element from maxDeque.
# If the first element of minDeque is equal to nums[left]:
# Remove the first element from minDeque.
# Increment left by 1.
# Update maxLength:
# Set maxLength to the maximum of maxLength and (right - left + 1).
# Return maxLength which stores the length of the longest valid subarray.

# Time Complexity: O(n)

# Initializing the two deques, maxDeque and minDeque, takes O(1) time.

# Iterating through the array nums from left to right involves a single loop that runs n times.

# Maintaining maxDeque and minDeque involves adding and removing elements. Each element can be added and removed from the deques at most once, resulting in O(1) time per operation. Over the entire array, this results in O(n) time for both deques combined.

# Checking the condition and potentially shrinking the window involves deque operations, which each take O(1) time. Over the entire array, this takes O(n) time.

# Updating the maxLength variable involves a simple comparison and assignment, each taking O(1) time per iteration. Over the entire array, this takes O(n) time.

# Therefore, the total time complexity is O(n).

# Space Complexity: O(n)

# The two deques, maxDeque and minDeque, store elements of the array. In the worst case, each deque could store all n elements of the array.

# The additional variables left, right, and maxLength use constant space.

# Therefore, the space complexity is O(n) due to the deques storing up to n elements in the worst case.