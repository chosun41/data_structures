def findClosestElements(arr, k, x):

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
    print(l,r)

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
    # time: O(logn)
    # space: O(k)
    print(findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3))