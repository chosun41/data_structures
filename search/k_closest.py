def findClosestElements1(arr, k, x):
    diffTuples = sorted((abs(x - num), num) for num in arr)
    return sorted(map(lambda x: x[1], diffTuples[:k])) 


def findClosestElements2(arr, k, x):

    def findIndex(arr, target):
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = l + (r-l)//2
            if arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l

    index = findIndex(arr, x)
    l, r = index, index # start from index out

    while r - l < k:
        if l == 0: 
            return arr[:k]
        if r == len(arr): 
            return arr[-k:]
        if x - arr[l] <= arr[r] - x: # diff on both sides determines the pointer increment/decrement, slide towards one with smaller diff
            l -= 1
        else: 
            r += 1
    return arr[l:r]

if __name__ == '__main__':
    # time: O(nlogn)
    # space: O(k)
    print(findClosestElements1(arr = [1,2,3,4,5], k = 4, x = 3))
    # time: O(logn + k)
    # space: O(k)
    print(findClosestElements2(arr = [1,2,3,4,5], k = 4, x = 3))