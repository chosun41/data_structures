
def numSubseq(nums, target):
    nums.sort()
    n = len(nums)
    res = 0
    #one length subsequence
    i,j = 0,n-1


    for i in range(n):
        while i<=j and nums[i]+nums[j] > target:
            j-=1

        if i<=j and nums[i] + nums[j] <= target:
            res += pow(2,(j-i))

    return res
    
if __name__=='__main__':
    # time: O(nlogn) if needs sorting
    # space: O(1)
    # number of subseq sum of min and max <= target
    print(numSubseq(nums = [3,5,6,7], target = 9))
    print(numSubseq(nums = [3,3,6,8], target = 10))
 