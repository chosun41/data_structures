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

def BinarySearchRecursive(numbersList, value, low=0, high=-1):
    if not numbersList: 
        return -1
    if(high == -1): 
        high = len(numbersList) - 1
    if low == high:
        if numbersList[low] == value: 
            return low
        else: 
            return -1
        
    mid = low + (high - low) // 2 
   
    if numbersList[mid] > value: 
        return BinarySearchRecursive(numbersList, value, low, mid - 1) # if mid>value then look left in range low,mid-1
    elif numbersList[mid] < value: 
        return BinarySearchRecursive(numbersList, value, mid + 1, high) # if mid<value then look right in range mid+1, high
    else: 
        return mid

if __name__=='__main__':
    
    # everything O(n) except for binary search which is O(log n)
    A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
    B = [34,46,93,127,277,321,454,565,1220]
    print(unordered_linear_search(A, 277)) 
    print(ordered_linear_search(B, 565)) 
    print(BinarySearchRecursive(A, 277))  
