def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
    n = len(intervals)

    prev = 0
    count = 1

    for i in range(1, n):
        if intervals[i][0] >= intervals[prev][1]:
            prev = i
            count += 1

    return n - count

if __name__ == '__main__':
    print(eraseOverlapIntervals(intervals = [[1,2],[1,2],[1,2]]))

    # Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

    # Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

    

    # Example 1:

    # Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
    # Output: 1
    # Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
    # Example 2:

    # Input: intervals = [[1,2],[1,2],[1,2]]
    # Output: 2
    # Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
    # Example 3:

    # Input: intervals = [[1,2],[2,3]]
    # Output: 0
    # Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
    

    # Constraints: