def nextPermutation(nums):
    i = j = len(nums)-1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1
    if i == 0:   # nums are in descending order
        nums.reverse()
        return nums
    k = i - 1    # find the last "ascending" position
    while nums[j] <= nums[k]: #<= since right side is already in descending order
        j -= 1
    nums[k], nums[j] = nums[j], nums[k]  
    l, r = k+1, len(nums)-1  # reverse the second part (k+1 here)
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l +=1
        r -= 1

    return nums
    
if __name__ == '__main__':
    # time: O(n)
    # space: O(1)
    print(nextPermutation([1,1,5])) # 151 i=2,j=2,151,j=2
    print(nextPermutation([1,2,3])) # 132 i=2,j=2,132,j=2
    print(nextPermutation([1,3,2])) # 213 i=1,j=2,231,j=2,213,i=2,j=1
    print(nextPermutation([3,2,1])) # 123 i=0,j=2,123,i=1,j=1
    print(nextPermutation([3,4,2,1])) # 4123 i=1,j=1,4321,j=3,4123,j=2,i=2

    # 1. find index of first decreasing element
    # 2. find index of element that is closest to the number from #1
    # 3. swap these elements
    # 4. reverse the 2nd part