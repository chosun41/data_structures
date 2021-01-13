
def longestOnes(A,K):
    left = 0
    for right in range(len(A)):
        # only subtract 1 if it is a zero
        K -= 1 - A[right]
        # if negative consumed all bits
        if K < 0:
            # if left is zero,have to increase K since we used all zeros already
            K += 1 - A[left]
            left += 1 # increment left to keep window size
    return right - left + 1
    
if __name__=='__main__':
    # time: O(n)
    # space: O(1)
    # can change K values from 0 to 1, what is the longest continuous sequence of 1s?
    
    print(longestOnes(A = [1,1,1,0,0,0,1,1,1,1,0], K = 2))
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
    print(longestOnes(A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3))