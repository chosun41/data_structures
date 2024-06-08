from collections import Counter

def findPairs(nums, k):
    result = 0

    counter = Counter(nums)

    print(counter)

    for x in counter: # for x in counter not nums
        if k > 0 and x + k in counter:
            result += 1
        elif k == 0 and counter[x] > 1:
            result += 1
    return result

if __name__=='__main__':

    # find num of unique pairs whos difference is k
    print(findPairs(nums = [3,1,4,1,5], k = 2))
    print(findPairs(nums = [3,3,1,1,4,4,1,5], k = 2))
    print(findPairs(nums = [1,2,4,4,3,3,0,9,2,3], k = 3))
    print(findPairs(nums = [3,3,3], k = 0))