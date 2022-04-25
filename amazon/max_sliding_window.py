import collections

def maxSlidingWindow(nums, k):
    opt = []
    q = collections.deque()
    for i in range(len(nums)):
        n = nums[i]
        
        #move the window
        if q and q[0]<=i-k: 
            q.popleft()

        #pop the right if the element in queue is not greater than the in-coming one
        #by doing this, we can always keep the max in the current window at left most
        while q and nums[q[-1]]<=n: 
            q.pop()

        q.append(i)

        #add the max to the output array after the first kth element
        if i+1>=k: 
            opt.append(nums[q[0]])
    return opt

if __name__ == '__main__':
    
    # You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

    # Return the max sliding window.

    

    # Example 1:

    # Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    # Output: [3,3,5,5,6,7]
    # Explanation: 
    # Window position                Max
    # ---------------               -----
    # [1  3  -1] -3  5  3  6  7       3
    #  1 [3  -1  -3] 5  3  6  7       3
    #  1  3 [-1  -3  5] 3  6  7       5
    #  1  3  -1 [-3  5  3] 6  7       5
    #  1  3  -1  -3 [5  3  6] 7       6
    #  1  3  -1  -3  5 [3  6  7]      7
    # Example 2:

    # Input: nums = [1], k = 1
    # Output: [1]
    

    # Constraints:

    # 1 <= nums.length <= 105
    # -104 <= nums[i] <= 104
    # 1 <= k <= nums.length

    print(maxSlidingWindow( nums = [1,3,-1,-3,5,3,6,7], k = 3))