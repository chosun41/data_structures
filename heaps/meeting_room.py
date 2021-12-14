import heapq
def minMeetingRooms(intervals):
    intervals.sort(key = lambda x: x[0])
    res = 0
    heap = []
    for interval in intervals:
        while heap and heap[0] <= interval[0]: # keep popping room until theres a meeting room that can't be occupied
            heapq.heappop(heap)
        heapq.heappush(heap, interval[1])
        res = max(res, len(heap))
    return res

if __name__=='__main__':
    # time: O(nlogn)
    # space: O(n)
    # meeting start and end, how many minimum meeting rooms required to accomodate meetings
    print(minMeetingRooms(intervals = [[0,30],[5,10],[15,20]]))
    # res=0,heap=[],l_heap=0
    # heap = [30], l_heap=1, res= 1
    # heap = [10,30], l_heap=2, res=2, 
    # heap = [30], l_heap=1, heap = [20,30], l_heap=2, res=2