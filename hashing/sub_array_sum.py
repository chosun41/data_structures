from collections import defaultdict

def subarraySum1(nums, k):
    count=0

    for i in range(len(nums)):
        for j in range(1,len(nums)-i+1):
            if sum(nums[i:i+j])==k:
                count+=1
    return count

def subarraySum2(nums,k):
        ddict = defaultdict(int)
        tot = 0
        cnt = 0
        ddict[0] = 1
        for i in range(len(nums)):
            tot += nums[i]
            cnt += ddict[tot-k]
            ddict[tot] += 1
        return cnt

if __name__ == '__main__':
    
    # time: O(n^2)
    # space: O(1)
    print(subarraySum1([1,2,3],3))
    # time: O(n)
    # space: O(n)  
    # hashmap of cumulative sum
    print(subarraySum2([1,2,3],3))