import heapq
def minMeetingRooms(intervals):
    intervals.sort(key = lambda x: x[0])
    res = 0
    heap, l_heap = [], 0
    for interval in intervals:
        while heap and heap[0] <= interval[0]:
            heapq.heappop(heap)
            l_heap -= 1
        heapq.heappush(heap, interval[1])
        l_heap += 1
        res = max(res, l_heap)
    return res

if __name__=='__main__':
    # time: O(nlogn)
    # space: O(n)
    # meeting start and end, how many minimum meeting rooms required to accomodate meetings
    print(minMeetingRooms(intervals = [[0,30],[5,10],[15,20]]))