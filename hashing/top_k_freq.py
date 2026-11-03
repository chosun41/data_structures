import heapq
from collections import Counter,defaultdict

def topKFrequent1(nums,k): 
    # O(1) time 
    if k == len(nums):
        return nums
    
    # 1. build hash map : character and how often it appears
    # O(N) time
    count = Counter(nums)   

    # 2-3. build heap of top k frequent elements and
    # convert it into an output array
    # O(N log k) time
    return heapq.nlargest(k, count.keys(), key=count.get) 

def topKFrequent2(nums, k):
    bucket = [[] for _ in range(len(nums) + 1)]
    Count = Counter(nums).items()  
    for num, freq in Count: 
        bucket[freq].append(num) 

    print(bucket)

    # bucket is freq:num
    flat_list = [item for sublist in bucket for item in sublist]
    print(bucket,flat_list)
    return flat_list[::-1][:k]
        
if __name__=='__main__':
    # time and space: O(n) bucket sort
    print(topKFrequent1(nums = [1,2,2,2,3,3,3], k = 2))
    print(topKFrequent2(nums = [1,2,2,2,3,3,3], k = 2))