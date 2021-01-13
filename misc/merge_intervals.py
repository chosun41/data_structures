def merge(intervals):

    merged = []
    for interval in intervals:
        # last end is less than current beginning
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
        # otherwise, there is overlap, so we merge the current and previous intervals
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged
        
if __name__ == '__main__':
    # time: O(n log n) -> mostly because of initial sort by key 0 of each sublist
    # space: O(n)
    print(merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))