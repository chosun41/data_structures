def has_two_sum(A, t): 

    i, j = 0, len(A) - 1

    while i <= j: # works only if sorted
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j] < t:
            i += 1
        else:  # A[i] + A[j] > t.
            j -= 1
    return False

def twoSum(nums, target):

    nums_hash = {}
    for i, num in enumerate(nums):
        potentialMatch = target - num
        if potentialMatch in nums_hash:
            return [nums_hash[potentialMatch], i]
        nums_hash[num] = i

def has_three_sum(A, t):

    A.sort()
    # Finds if the sum of two numbers in A equals to t - a.
    return any(has_two_sum(A, t - a) for a in A) # two sum plus a equal to t

def threeSum(nums):
    res = []
    nums.sort()
    if len(nums) < 3:
        return res

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]: 
            continue
        l, r = i, len(nums) - 1 ## l=i not 0
        while l < r :
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.append([nums[i] ,nums[l] ,nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]: 
                    l += 1
                while l < r and nums[r] == nums[r + 1]: 
                    r -= 1
            elif s < 0 :
                l += 1
            else:
                r -= 1
    return res

if __name__ == '__main__':
    
    # two sum O(n), three sum O(n^2), space O(1), not necessarily distinct, space O(n)
    # is it sorted
    # can you reuse an index
    # are all elements distinct
    
    print(has_two_sum([-2,1,2,4,7,11],6))
    print(has_two_sum([-2,1,2,4,7,11],10))
    print(has_three_sum([-2,1,2,4,7,11],17))
    print(has_three_sum([-2,1,2,4,7,11],21)) #7,7,7
    print(twoSum(nums = [2,7,11,15], target = 9))
    print(twoSum(nums = [3,2,4], target = 6))
    print(threeSum([-1,0,1,2,-1,-4])) # three sum equal to 0