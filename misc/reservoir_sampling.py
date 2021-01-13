import random

def pick(nums, target):
    """
    :type target: int
    :rtype: int
    """
    res = None
    count = 0
    for i, n in enumerate(nums):
        if n == target:
            num = random.randint(0, count) # first is 100% target
            if num == 0:
                res = i
            count += 1 # ensures uniform prob of picking the target
    return res

if __name__=='__main__':
    # time: O(n)
    # space: O(1)
    # return index
    print(pick([1,2,3,3,3],3))