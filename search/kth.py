# take advantage of pivot

def kth(arr, l, r, k): 
  
    # If k is smaller than number of  
    # elements in array 
    if (k > 0 and k <= r - l + 1): 
      
        pos = partition(arr, l, r) 
  
        if (pos - l == k - 1): 
            return arr[pos] 
        elif (pos - l > k - 1): 
            return kth(arr, l, pos - 1, k) 
        else:
            return kth(arr, pos + 1, r, k - pos + l - 1) 
  
    return float('inf')
  
# Standard partition process of QuickSort().  
def partition(arr, l, r): 
  
    x = arr[r] 
    i = l 
    for j in range(l, r): 
        if (arr[j] > x): # switch to < for smallest
            arr[i], arr[j] = arr[j], arr[i] 
            i += 1
    arr[i], arr[r] = arr[r], arr[i] 
    return i 
    
if __name__=='__main__':
    
    # time: O(n^2), but on average more like O(n) b/c of randomization
    
    a=[3,2,1,5,4]
    n=len(a)
    k=4
    
    print(kth(a, 0, n - 1, k))
