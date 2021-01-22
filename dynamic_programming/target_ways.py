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
    # a list of non negative integers, list all the ways it equals target S
    print(findTargetSumWays(A=[1, 1, 1, 1, 1], S=3))