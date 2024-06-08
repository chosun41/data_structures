def findPeakElement(nums):
    low, high = 0, len(nums)-1
    while low < high: #important because if last element is the peak, so mid doesn't cause out of bounds index exception
        mid = (high+low)//2
        if nums[mid] < nums[mid+1]: # continue looking right if mid is less than
            low = mid+1
        else: # if they are same or next element is less than current
            high = mid
    return low

if __name__=='__main__':
    # time: O(logn)
    # space: O(1)
    # peak is index of elements where it is strictly greater than neighbors
    # Assume there is a peak, then peak's left will be monotonic increasing while its right will be monotonic decreasing.

    # So during binary search, if nums[mid] > nums[mid+1], we know mid is on the right side of peak, and we should left shift our hi, otherwise we should right shift our lo.
    # When lo == hi, we find our peak index.

    # Since we are comparing nums[mid] and nums[mid+1], we should not consider other indices as a candidate peak during that iteration. So, we should update as lo = mid + 1 and hi = mid. Because if nums[mid+1] is the peak, we right shift lo to mid+1; Otherwise nums[mid] is the peak, we left shift hi to mid.

    # We can safely use mid+1 as long as we initialized hi as len(nums)-1. As the maximum value of mid is hi-1, otherwise lo <= hi and loop breaks, mid+1
    # will not exceed len(nums)-1.
    print(findPeakElement( nums = [1,2,1,3,5,6,4])) # there is a peak at 1,2,1 but this is not strictly greater
    # low=0,high=6
    # mid=3 3<5 low=4
    # mid=5 6>4 high=5
    # mid=4 5<6 low=5
    # return 5
    