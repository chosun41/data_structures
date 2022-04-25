import heapq

# heapq operations:
# 1. heapq.heapify(L) - heapify list L
# 2. heapq.nlargest(k,L),heapq.nsmallest(k,L) - return the klargest/smallest elements in L in a new list
# 3. heapq.heappush(L,a) - pushes element a on the heap list
# 4. heapq.heappop(L) - pops the smallest element from the list and returns it
# 4. heapq.heappushpop(L,a) - pushes a on the heap and then pops and returns the smallest element (combines a push and pop
# 5. e=h[0] - returns the smallest element on the heap without poping it

# min heap functionality in this library
# for max heap use -

# brute force would be to look at all the elements O(log n)
# this doesn't take advantage of pervious computations
# the median divides the collections into two equal parts
# when a new element is added, the parts can change by at most one element and the 
# the element to switch between two halves is either the largest of the smaller half or the smaller of the larger half

# with a min and max heap, we can keep track of all this

def online_median(sequence):
    
    min_heap=[]
    max_heap=[]
    result=[]
    
    for x in sequence:
         
        # push onto the max heap
        # the negative of popped item x after adding x
        heapq.heappush(max_heap,-heapq.heappushpop(min_heap,x)) #heappushpop most important part
        
        # if max_heap > min_heap length
        # push onto the min heap
        # the negative of the popped item from the max heap
        if len(max_heap)>len(min_heap):
            heapq.heappush(min_heap,-heapq.heappop(max_heap))
           
        # if the min and max heap length are same (even number of items) append 0.5 of
        # else append the smallest of the min heap
        if len(min_heap)==len(max_heap):
            result.append(0.5*(min_heap[0] + -max_heap[0]))
        else:
            result.append(min_heap[0])
           
    return result

if __name__=='__main__':
    
    # time: O(log n) space: O(n)
    
    print(online_median([1,0,3,5,2,0,1]))
    
    # L - min heap, H - max heap
    
    # Read in 1: L=[1], H=[]
    #            L=[], H=[-1]
    #            L=[1], H=[]
    #            result = [1]
    # Read in 0: L=[0,1], H=[]
    #            L=[1], H=[0]
    #            result = [1,0.5]
    # Read in 3: L=[1,3], H=[0]
    #            L=[3], H=[-1,0]
    #            L=[1,3], H=[0] 
    #            result = [1,0.5,1]
    # Read in 5: L=[1,3,5],H=[0]
    #            L=[3,5],H=[-1,0]
    #            result = [1,0.5,1,2]
    # Read in 2: L=[2,3,5],H=[-1,0]
    #            L=[3,5],H=[-2,-1,0]
    #            L=[2,3,5],H=[-1,0]
    #            result = [1,0.5,1,2,2]
    # Read in 0: L=[0,2,3,5],H=[-1,0]
    #            L=[2,3,5],H=[-1,0,0]
    #            result = [1,0.5,1,2,2,1.5]
    # Read in 1: L=[1,2,3,5],H=[-1,0,0]
    #            L=[2,3,5],H=[-1,-1,0,0]
    #            L=[1,2,3,5],H=[-1,0,0]
    #            result = [1,0.5,1,2,2,1.5,1]    
        