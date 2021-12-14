import random

class Solution:

    def __init__(self,w):
        """
        :type w: List[int]
        """
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self):
        """
        :rtype: int
        """
        target = self.total_sum * random.random()
        # run a linear search to find the target zone
        for i, prefix_sum in enumerate(self.prefix_sums):
            if target < prefix_sum: # target<prefix_sum
                return i
                
if __name__=='__main__':
    x=Solution([1,3])
    # prefix sums =[1,4]
    # enumerate random to find target if less than return i
    print(x.pickIndex())
    print(x.pickIndex())
    print(x.pickIndex())
    print(x.pickIndex())