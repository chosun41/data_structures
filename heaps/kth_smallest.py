from heap import MinHeap

# keep deleteing min until you reach k 
            
def FindKthSmallestEle(orig, k):
    
    count=0
    
    if k>orig.size:
        return -1
    else:
        while orig.size>0:
            x=orig.deleteMin()
            count+=1
            if count == k:
                return x
    

if __name__=='__main__':
    
    # time: O(k logn) - k for k times, logn for each deletion
    
    orig = MinHeap()
    orig.insert(1)
    orig.insert(20)
    orig.insert(5)
    orig.insert(100)
    orig.insert(1000)
    orig.insert(12)
    orig.insert(18)
    orig.insert(16)

    print(orig.heapList)
    print(FindKthSmallestEle(orig, 6))