def permutations(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def backtrack(first = 0):
        # if all integers are used up
        if first == n:  
            output.append(nums[:])
        for i in range(first, n):
            # place i-th integer first 
            # in the current permutation
            nums[first], nums[i] = nums[i], nums[first]
            # use next integers to complete the permutations
            backtrack(first + 1)
            # backtrack
            nums[first], nums[i] = nums[i], nums[first]
    
    n = len(nums)
    output = []
    backtrack()
    return output

if __name__ == '__main__':
    
    # time: O(n x n!) space: O(n!)
    print(permutations([2,3,5,7]))

    