def unordered_linear_search(L,value):
    for i in range(len(L)):
        if L[i]==value:
            return i
    return -1

def ordered_linear_search(L,value):
    for i in range(len(L)):
        if L[i]==value:
            return i
        elif L[i]>value:
            return -1
    return -1

def BinarySearchRecursive(arr, low, high, x): 
  
    # Check base case 
    if low<=high: 
  
        mid = (high + low) // 2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
  
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return BinarySearchRecursive(arr, low, mid - 1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return BinarySearchRecursive(arr, mid + 1, high, x) 
  
    else: 
        # Element is not present in the array 
        return -1
    
def BinarySearchIterative(numbersList, value):
    n=len(numbersList)
    
    lo, hi = 0, n-1
    while lo <= hi:
        mid = (lo + hi) // 2

        if numbersList[mid]>value:
            hi = mid-1
        elif numbersList[mid]<value:
            lo = mid+1
        else:
            return mid

if __name__=='__main__':
    
    # everything O(n) except for binary search which is O(log n)
    A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
    B = [34,46,93,127,277,321,454,565,1220]
    print(unordered_linear_search(A, 277)) 
    print(ordered_linear_search(B, 565)) 
    print(BinarySearchRecursive(A, 0,len(A)-1,277)) 
    print(BinarySearchIterative(A, 277)) 
