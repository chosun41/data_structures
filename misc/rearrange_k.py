import collections
import heapq
def rearrangeString(s,k):
    if k < 2: 
        return s
    ans = []
    heap = [(-cnt, ltr) for ltr, cnt in collections.Counter(s).items()]
    heapq.heapify(heap)
    cooldown = {} # dictionary of index: (cnt,ltr)
    for i in range(len(s)):
        if i in cooldown and cooldown[i][0]: # if i in cooldown and !=0
            heapq.heappush(heap, cooldown[i])
        if not heap:
            return ''
        cnt, ltr = heapq.heappop(heap)
        ans.append(ltr)
        cooldown[i + k] = (cnt + 1, ltr) # i+k to be used later)
    return ''.join(ans)

if __name__=='__main__':
    # time and space: O(n), heapify actually becomes O(n)
    # rearrange string so that each letter that repeats is at least k distance from each other
    # max heap
    print(rearrangeString(s = "aabbcc", k = 3))
    print(rearrangeString(s = "aaadbbcc", k = 2))