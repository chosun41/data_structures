from heapq import *

def maxEvents(events):
    events.sort(key = lambda e: e[0])
    pq = [] # store end time of open events
    count = 0
    i, n = 0, len(events)
    d = 0  # current day
    
    while i < n or pq:
        if not pq:
            d = events[i][0]
        while i < n and d >= events[i][0]: # push all events we can possibly attend
            heappush(pq, events[i][1])
            i += 1
        heappop(pq)  # attend this one event
        count += 1
        d += 1
        while pq and pq[0] < d: # remove all impossible-to-attend events
            heappop(pq)
        
    return count

if __name__ == '__main__':
    
    # You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

    # You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

    # Return the maximum number of events you can attend.

    

    # Example 1:


    # Input: events = [[1,2],[2,3],[3,4]]
    # Output: 3
    # Explanation: You can attend all the three events.
    # One way to attend them all is as shown.
    # Attend the first event on day 1.
    # Attend the second event on day 2.
    # Attend the third event on day 3.
    # Example 2:

    # Input: events= [[1,2],[2,3],[3,4],[1,2]]
    # Output: 4

    print(maxEvents( events= [[1,2],[2,3],[3,4]]))
    print(maxEvents( events= [[1,2],[2,3],[3,4],[1,2]]))