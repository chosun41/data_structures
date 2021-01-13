def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums
            
if __name__ == '__main__':
    # time: O(n)
    # space: O(1)
    # move all zeros to the end and keep order of non zeros
    print(moveZeroes([0,1,0,3,12]))