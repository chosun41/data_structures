def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    i = 0
    for j in range(len(nums)): 
        if nums[j] != 0: # j not i, i is for zeros that are to be swapped
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums
            
if __name__ == '__main__':
    # time: O(n)
    # space: O(1)
    # move all zeros to the end and keep order of non zeros
    print(moveZeroes([0,1,0,3,12]))
    # i=0,j=0,[0,1,0,3,12]
    # i=0,j=1,[1,0,0,3,12]
    # i=1,j=2,[1,0,0,3,12]
    # i=1,j=3,[1,3,0,0,12]
    # i=2,j=4,[1,3,12,0,0]