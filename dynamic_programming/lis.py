def lis(arr): 
    n = len(arr) 
  
    # Declare the list (array) for LIS and initialize LIS 
    # values for all indexes 
    lis = [1]*n 
  
    # Compute optimized LIS values in bottom up manner 
    for i in range (1, n): 
        for j in range(0, i): 
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 : # need second condition to make sure its an increasing subsequence
                lis[i] = lis[j]+1
  
    print(lis)
  
    return max(lis)
# end of lis function 

if __name__=='__main__':

    # time: O(n^2)
    # longest increasing subseqeunce not necessarily contiguous, but left to right, up to current index
    arr = [10, 22, 9, 33, 21, 50, 41, 60] # 10,22,33,41,60 or 10,22,33,50,60
    print(lis(arr))
