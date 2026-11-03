# def maxSumOfThreeSubarrays(nums, k):
#     subsum = sum(nums[:k])
#     take1 = [(0, ()) for _ in range(len(nums))]
#     take2 = [(0, ()) for _ in range(len(nums))]
#     take3 = [(0, ()) for _ in range(len(nums))]

#     for i in range(k - 1, len(nums)):
#         subsum = subsum - nums[i - k] + nums[i]

#         # update take 1
#         if subsum > take1[i - 1][0]:
#             take1[i] = (subsum, (i - k + 1,))
#         else:
#             take1[i] = take1[i - 1]

#         # update take 2
#         if subsum + take1[i - k][0] > take2[i - 1][0]:
#             newval = subsum + take1[i - k][0]
#             newidx = take1[i - k][1] + (i - k + 1,)
#             take2[i] = (newval, newidx)
#         else:
#             take2[i] = take2[i - 1]

#         # update take 3
#         if subsum + take2[i - k][0] > take3[i - 1][0]:
#             newval = subsum + take2[i - k][0]
#             newidx = take2[i - k][1] + (i - k + 1,)
#             take3[i] = (newval, newidx)
#         else:
#             take3[i] = take3[i - 1]

#     print(take3)
#     return take3[-1][1]

def maxSumOfThreeSubarrays(nums, k):
    n = len(nums)
    
    # Create an array to store the sums of all possible subarrays of length k in nums.
    sums = [sum(nums[i:i+k]) for i in range(n-k+1)]
    
    # Create two arrays to store the starting index of the maximum sum subarray of length k to the left and to the right of each index in nums.
    left = [0] * (n-k+1)
    right = [n-k] * (n-k+1)
    for i in range(1, n-k+1):
        if sums[i] > sums[left[i-1]]:
            left[i] = i
        else:
            left[i] = left[i-1]
        if sums[n-k-i] >= sums[right[n-k-i+1]]:
            right[n-k-i] = n-k-i
        else:
            right[n-k-i] = right[n-k-i+1]
    
    # Initialize the maximum sum and the starting indices of the three subarrays.
    max_sum = float('-inf')
    res = [0, k, 2*k]
    
    # Iterate through the sums array from index k to n-2k and calculate the sum of three subarrays starting at i-k, i and i+k using the sums array and the left and right arrays.
    for i in range(k, n-2*k+1):
        left_sum = sums[left[i-k]]
        right_sum = sums[right[i+k]]
        mid_sum = sums[i]
        total_sum = left_sum + mid_sum + right_sum
        
        # If the sum of three subarrays is greater than the current maximum sum, update the maximum sum and the starting indices of the three subarrays.
        if total_sum > max_sum:
            max_sum = total_sum
            res = [left[i-k], i, right[i+k]]
    
    return res

if __name__ == '__main__':
    # find sum of three non overlapping subarrays of size k
    # use lexicographically smallest solution
    # with indices of starting indices
    print(maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2))