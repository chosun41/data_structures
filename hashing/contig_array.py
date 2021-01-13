def findMaxLength(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dic = {0:-1}
    count = 0
    maxlen = 0
    for i in range(len(nums)):
        count += (1 if nums[i] == 1 else -1)
        if count not in dic:
            dic[count] = i
        else:
            maxlen = max(maxlen, i - dic[count])
    return maxlen 

if __name__=='__main__':
    # time and space: O(n)
    # find max length of contiguous array that have equal number of 0 and 1s
    print(findMaxLength([0,1,0]))