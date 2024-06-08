
def longestOnes(nums, k):
    left = 0
    answer = 0
    counts = {0: 0, 1: 0}
    
    for right, num in enumerate(nums): # not while
        counts[num] += 1
        
        while counts[0] > k:
            counts[nums[left]] -= 1
            left += 1

        answer = max(answer, right - left + 1)
        
    return answer
    
if __name__=='__main__':
    # time: O(n)
    # space: O(1)
    # can change K values from 0 to 1, what is the longest continuous sequence of 1s?
    
    print(longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))
    # right=0,K=2
    # right=1,K=2
    # right=2,K=2
    # right=3,K=1
    # right=4,K=0
    # right=5,K=-1,K=-1,left=1
    # right=6,K=-1,K=-1,left=2
    # right=7,K=-1,K=-1,left=3
    # right=8,K=-1,K=0,left=4
    # right=9,K=0
    # right=10,K=-1,K=0,left=5
    # 10-5+1=6
    print(longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))