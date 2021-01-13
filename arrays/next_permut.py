def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    for i in reversed(range(n)):
        if nums[i] > nums[i-1]:
            j = i
            while j < n and nums[j] > nums[i-1]:
                idx = j
                j += 1
            nums[idx], nums[i-1] = nums[i-1], nums[idx]
            for k in range((n-i)//2):
                nums[i+k], nums[n-1-k] = nums[n-1-k], nums[i+k]
            break
    else:
        nums.reverse()
    return nums
        
if __name__ == '__main__':
    # time: O(n)
    # space: O(1)
    print(nextPermutation([1,1,5])) # 151 while
    print(nextPermutation([1,2,3])) # 132 while 
    print(nextPermutation([1,3,2])) # i=1,idx=1,j=2,idx=2,j=3,231,k=0, nums[1+0],nums[3-1-0]=nums[3-1-0],nums[1+0],213
    print(nextPermutation([3,2,1])) # 123 (else)