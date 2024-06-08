import collections
import heapq

def rearrangeString(s,k):
    if k < 2: 
        return s
    ans = []
    heap = [(-cnt, ltr) for ltr, cnt in collections.Counter(s).items()] # max heap
    # heapq.heapify(heap)
    print(heap)
    cooldown = {} # dictionary of index: (cnt,ltr)
    for i in range(len(s)):
        print(i)
        if i in cooldown and cooldown[i][0]: # first thing, is to check if something is up to be added to heap, anything else than 0 even negative works 
            heapq.heappush(heap, cooldown[i])
        if not heap:
            return '' # remember this
        cnt,ltr = heapq.heappop(heap)
        print(heap)
        ans.append(ltr)
        print(ans)
        cooldown[i + k] = (cnt + 1, ltr) # i+k to be used later)
        print(cooldown)
    return ''.join(ans)

if __name__=='__main__':
    # time: slogn s length of string and n number of distinct characters
    # space: s
    print(rearrangeString(s = "aabbcc", k = 3))
    print(rearrangeString(s = "aaadbbcc", k = 2))