def permutations(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def backtrack(first = 0):
        if first == n:  
            output.append(nums[:])
        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1) # !!! first not i
            nums[first], nums[i] = nums[i], nums[first]
    
    n = len(nums)
    output = []
    backtrack()
    return output

if __name__ == '__main__':
    
    # time and space: O(n!)
    print(permutations([2,3,5,7]))
    