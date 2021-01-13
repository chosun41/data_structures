def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    dic = {}
    for n in nums:
        if n not in dic:
            dic[n] = 1
        else:
            dic[n] += 1

    maxFreq = 0
    freq2num = {}
    for key,val in dic.items():
        if val in freq2num:
            freq2num[val].append(key)
        else:
            freq2num[val] = [key]
        maxFreq = max(maxFreq,val)

    res = []
    for f in range(maxFreq,-1,-1):
        if f in freq2num:
            res += freq2num[f]
        if len(res) >= k:
            return res
        
if __name__=='__main__':
    # time and space: O(n) bucket sort
    print(topKFrequent(nums = [1,1,1,2,2,3], k = 2))