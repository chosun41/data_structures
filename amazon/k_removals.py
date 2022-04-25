from collections import Counter
from heapq import *

def findLeastNumOfUniqueInts(arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        count_arr = Counter(arr)
        print(count_arr)
        heap = []
        for val,count in count_arr.items():
            heappush(heap,(count,val)) # need to heappush or else this doesn't work

        print(heap)
        while heap and k>0:
            count,val = heappop(heap)
            if count>1: # so 0 doesn't appear in count in heap
                heappush(heap,(count-1,val))

            k-=1
        print(heap)

        return len(heap)

if __name__ == '__main__':
    
    # Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

    

    # Example 1:

    # Input: arr = [5,5,4], k = 1
    # Output: 1
    # Explanation: Remove the single 4, only 5 is left.
    # Example 2:
    # Input: arr = [4,3,1,1,3,3,2], k = 3
    # Output: 2
    # Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
    

    # Constraints:

    # 1 <= arr.length <= 10^5
    # 1 <= arr[i] <= 10^9
    # 0 <= k <= arr.length

    print(findLeastNumOfUniqueInts( arr = [5,5,4], k = 1))
    print(findLeastNumOfUniqueInts( arr = [4,3,1,1,3,3,2], k = 3))