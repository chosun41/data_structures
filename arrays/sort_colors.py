def sortColors(nums):
    """
    Dutch National Flag problem solution.
    """
    # for all idx < left : nums[idx < left] = 0
    # curr is an index of element under consideration
    left = curr = 0
    # for all idx > right : nums[idx > right] = 2
    right = len(nums) - 1

    while curr <= right:
        if nums[curr] == 0: # send toward the start
            nums[left], nums[curr] = nums[curr], nums[left]
            left += 1
            curr += 1
        elif nums[curr] == 2: # send toward the end
            nums[curr], nums[right] = nums[right], nums[curr]
            right -= 1
        else:
            curr += 1
            
    return nums
            
if __name__=='__main__':
    
    # variant of dutch flag problems
    # time: O(n)
    # space: O(1)
    nums = [2,0,2,1,1,0]
    print(sortColors(nums))