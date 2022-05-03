def shipWithinDays(weights, D):
    left, right = max(weights), sum(weights)
    while left < right:
        mid, need, cur = (left + right) // 2, 1, 0 # need is days needed, cur is current cargo of ship
        for w in weights:
            if cur + w > mid:
                need += 1
                cur = 0
            cur += w
        if need > D: # most important
            left = mid + 1
        else: 
            right = mid
    return left

if __name__=='__main__':
    print(shipWithinDays(weights = [3,2,2,4,1,4], D = 3))
    print(shipWithinDays(weights = [1,2,3,1,1], D = 4))

# what is minimum capacity of ship of that needs to carry weights in order in D days?
# Time complexity: O(n * logSIZE), where SIZE is the size of the search space (sum of weights - max weight).
# Space complexity: O(1).

# JohnyRufus's avatar
# JohnyRufus
# 2556
# March 17, 2019 12:09 AM

# a) Without considering the limiting limiting days D, if we are to solve, the answer is simply max(a)
# b) If max(a) is the answer, we can still spend O(n) time and greedily find out how many partitions it will result in.

# [1,2,3,4,5,6,7,8,9,10], D = 5

# For this example, assuming the answer is max(a) = 10, disregarding D,
# we can get the following number of days:
# [1,2,3,4] [5] [6] [7] [8] [9] [10]

# So by minimizing the cacpacity shipped on a day, we end up with 7 days, by greedily chosing the packages for a day limited by 10.

# To get to exactly D days and minimize the max sum of any partition, we do binary search in the sum space which is bounded by [max(a), sum(a)]

# Binary Search Update:
# One thing to note in Binary Search for this problem, is even if we end up finding a weight, that gets us to D partitions, we still want to continue the space on the minimum side, because, there could be a better minimum sum that still passes <= D paritions.

# In the code, this is achieved by: