# def nextPermutation(nums):
#     i = j = len(nums)-1
#     while i > 0 and nums[i-1] >= nums[i]: # decrement until you find index where not less than next index
#         i -= 1
#     if i == 0:   # nums are in descending order
#         nums.reverse()
#         return nums
#     k = i - 1    # find the last "ascending" position
#     while nums[j] <= nums[k]: #<= since right side is already in descending order
#         j -= 1
#     nums[k], nums[j] = nums[j], nums[k]  
#     l, r = k+1, len(nums)-1  # reverse the second part (k+1 here)
#     while l < r:
#         nums[l], nums[r] = nums[r], nums[l]
#         l +=1
#         r -= 1

#     return nums

def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    # To find next permutations, we'll start from the end
    i = j = len(nums)-1
    # First we'll find the first non-increasing element starting from the end
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1
    # After completion of the first loop, there will be two cases
    # 1. Our i becomes zero (This will happen if the given array is sorted decreasingly). In this case, we'll simply reverse the sequence and will return 
    if i == 0:
        nums.reverse()
        return nums
    # 2. If it's not zero then we'll find the first number greater then nums[i-1] starting from end
    while nums[j] <= nums[i-1]:
        j -= 1
    # Now out pointer is pointing at two different positions
    # i. first non-assending number from end
    # j. first number greater than nums[i-1]
    
    # We'll swap these two numbers
    nums[i-1], nums[j] = nums[j], nums[i-1]
    
    # We'll reverse a sequence strating from i to end
    nums[i:]= nums[len(nums)-1:i-1:-1]
    # We don't need to return anything as we've modified nums in-place

    return nums
    
if __name__ == '__main__':
    # time: O(n)
    # space: O(1)
    print(nextPermutation([1,1,5])) # 151 i=2,j=2,151
    print(nextPermutation([1,2,3])) # 132 i=2,j=2,132
    print(nextPermutation([1,3,2])) # 213 i=1,j=2,231,213
    print(nextPermutation([3,2,1])) # 123 i=0,j=2,1231
    print(nextPermutation([3,4,2,1])) # 4123 i=1,j=1,4321,4123

    # 1. find index of first decreasing element
    # 2. find index of element that is closest to the number from #1
    # 3. swap these elements
    # 4. reverse the 2nd part