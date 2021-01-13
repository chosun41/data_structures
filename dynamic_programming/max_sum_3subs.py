def maxSumOfThreeSubarrays(nums, k):
    subsum = sum(nums[:k])
    take1 = [(0, ()) for _ in range(len(nums))]
    take2 = [(0, ()) for _ in range(len(nums))]
    take3 = [(0, ()) for _ in range(len(nums))]

    for i in range(k - 1, len(nums)):
        subsum = subsum - nums[i - k] + nums[i]

        # update take 1
        if subsum > take1[i - 1][0]:
            take1[i] = (subsum, (i - k + 1,))
        else:
            take1[i] = take1[i - 1]

        # update take 2
        if subsum + take1[i - k][0] > take2[i - 1][0]:
            newval = subsum + take1[i - k][0]
            newidx = take1[i - k][1] + (i - k + 1,)
            take2[i] = (newval, newidx)
        else:
            take2[i] = take2[i - 1]

        # update take 3
        if subsum + take2[i - k][0] > take3[i - 1][0]:
            newval = subsum + take2[i - k][0]
            newidx = take2[i - k][1] + (i - k + 1,)
            take3[i] = (newval, newidx)
        else:
            take3[i] = take3[i - 1]

    return take3[-1][1]
    
if __name__ == '__main__':
    # find sum of three non overlapping subarrays of size k
    # use lexicographically smallest solution
    # with indices of starting indices
    print(maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2))