# for max heap

def heapify(arr, n, i): 
    
    largest = i  # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # swap 
  
        # Heapify the root.  (recursive, but with new largest index)
        heapify(arr, n, largest) 

# The main function to sort an array of given size  
def heapSort(arr): 
    n = len(arr) 
  
    # Build a MAXHEAP
    # Since last parent will be at ((n//2)-1) we can start at that location. 
    # just goes in reverse
    for i in range(n // 2 - 1, -1, -1): 
        heapify(arr, n, i) 
        
    print(arr)
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # swap 
        heapify(arr, i, 0) 

if __name__=='__main__':

    # time: O(log n)
    
    arr = [534, 246, 933, 127, 277, 321, 454, 565, 220]
    heapSort(arr) 
    print(arr)

