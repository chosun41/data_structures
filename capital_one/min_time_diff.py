def findMinDifference(timePoints):
        # create buckets array for the times converted to minutes
    minutes = [False] * (24 * 60)
    for time in timePoints:
        h, m = map(int, time.split(":"))
        min_time = h * 60 + m
        if minutes[min_time]:
            return 0
        minutes[min_time] = True
    prevIndex = float("inf")
    firstIndex = float("inf")
    lastIndex = float("inf")
    ans = float("inf")

    # find differences between adjacent elements in sorted array
    for i in range(24 * 60):
        if minutes[i]:
            if prevIndex != float("inf"):
                ans = min(ans, i - prevIndex)
            prevIndex = i
            if firstIndex == float("inf"):
                firstIndex = i
            lastIndex = i

    return min(ans, 24 * 60 - lastIndex + firstIndex)

if __name__ == '__main__':
    print(findMinDifference( timePoints = ["23:59","00:00"]))

   # Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
    

    # Example 1:

    # Input: timePoints = ["23:59","00:00"]
    # Output: 1
    # Example 2:

    # Input: timePoints = ["00:00","23:59","00:00"]
    # Output: 0
    