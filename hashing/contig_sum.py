def checkSubarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    dic = {0:-1}
    summ = 0
    for i, n in enumerate(nums):
        if k != 0:
            summ = (summ + n) % k
        else:
            summ += n
        if summ not in dic:
            dic[summ] = i
        else:
            if i - dic[summ] >= 2:
                return True
    return False

if __name__=='__main__':

    # Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

    # An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
    # time and space: O(n)
    print(checkSubarraySum(nums = [23,2,4,6,7], k = 6))
    # nums = [23,2,4,6,7], k = 6,dic = {0:-1}, summ=0
    # i=0,n=23,summ=5,dic={0:-1,5:0}
    # i=1,n=2,summ=1,dic={0:-1,5:0,1:1}
    # i=2,n=4,summ=5,2-0>=2 return True