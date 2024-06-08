import collections

def findTargetSumWays(A, S):
    count = collections.Counter({0: 1})
    for x in A:
        step = collections.Counter()
        for y in count:
            step[y + x] += count[y]
            step[y - x] += count[y]
        count = step
        print(step)
    return count[S]

if __name__=='__main__':
    print(findTargetSumWays(A=[1, 2, 0, 0, 0], S=3))
    # You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
    # + 1 + 2 + 0 + 0 + 0
    # + 1 + 2 + 0 + 0 - 0
    # + 1 + 2 + 0 - 0 + 0
    # + 1 + 2 - 0 + 0 + 0
    # + 1 + 2 - 0 + 0 - 0
    # + 1 + 2 + 0 + 0 - 0
    # + 1 + 2 - 0 + 0 + 0
    # + 1 + 2 - 0 - 0 - 0