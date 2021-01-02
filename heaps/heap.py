# array implementation of min and max heap
# start at index 1 instead of 0 because of children indexing
# min/max element at index 1 (start of the heap)
# compared to bst and binary tree, heap every parent is >= (max) or <= (min) compared to children
# also is a complete (not perfect) binary tree where add at end from left to right
# can also use heapq library

# heapsort is also here - heapify an unsorted array, pop and reheapify as you add to output list

class MaxHeap:
    
    def __init__(self):
        self.heapList=[0]
        self.size=0
        
    def parent(self,index):
        return index//2
    
    def leftChildIndex(self,index):
        if 2*index<=self.size:
            return 2*index
        return -1
    
    def rightChildIndex(self,index):
        if 2*index+1<=self.size:
            return 2*index+1
        return -1        

    def leftChild(self,index):
        if 2*index<=self.size:
            return self.heapList[2*index]
        return -1
    
    def rightChild(self,index):
        if 2*index+1<=self.size:
            return self.heapList[2*index+1]
        return -1
    
    def searchElement(self,itm):
        i=1
        while(i<=self.size):
            if itm==self.heapList[i]:
                return i
            i+=1
        return -1
    
    def getMaximum(self):
        
        if self.size==0:
            return -1
        return self.heapList[1]
    
    # reach down to the leaves
    # find the minimum child and swap if parent greater than the child
    def percolateDown(self,i):
        
        while(i*2)<=self.size:
        
            maximumChild=self.maximumChild(i)
            
            if self.heapList[i]<self.heapList[maximumChild]:
                self.heapList[i],self.heapList[maximumChild]=self.heapList[maximumChild],self.heapList[i]
            i=maximumChild

    # find child that is smaller, if only left child use that
    def maximumChild(self,i):
        
        if i*2+1>self.size:
            return i*2
        else:
            if self.heapList[i*2]>self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1
            
    # reach down to the root
    # if the child (i) less than its parent (i//2), switch the elements
    # do this up to the root        
    def percolateUp(self,i):
        
        while i//2>0:   
            if self.heapList[i]>self.heapList[i//2]:
                self.heapList[i//2],self.heapList[i]=self.heapList[i],self.heapList[i//2] 
            i//=2
         
    # replace start of heap with the end, pop the end
    # and percolate down the start of the heap until its in its proper place
    def deleteMax(self):
        
        retval=self.heapList[1]
        self.heapList[1]=self.heapList[self.size]
        self.size-=1
        self.heapList.pop()
        self.percolateDown(1)
        return retval
    
    # append to end of heap
    # percolate up the element until its in its proper place
    def insert(self,k):
        self.heapList.append(k)
        self.size+=1
        self.percolateUp(self.size)
        
    def heapify(self,A):
        i=len(A)//2
        self.size=len(A)
        self.heapList=[0]+A[:]
        while(i>0):
            self.percolateDown(i)
            i-=1
            
    def heapSort(self,A):
        
        self.heapify(A)
        
        arr = []
        
        while self.size>0:
            arr.insert(0,self.deleteMax())
            
        return arr
    
    # just start searching from the middle
    def findMininMaxHeap(self):
        min=float('infinity')
        for i in range((self.size+1)//2,self.size):
            if(self.heapList[i]<min):
                min=self.heapList[i]
        return min
    
    # delete at position
    def delete(self,i):
        if(self.size<i):
            return
        key=self.heapList[i]
        self.heapList[i]=self.heapList[self.size]
        self.heapList.pop()
        self.size-=1
        self.percolateDown(i)
        return key
        
class MinHeap:
    
    def __init__(self):
        self.heapList=[0]
        self.size=0
        
    def parent(self,index):
        return index//2
    
    def leftChildIndex(self,index):
        if 2*index<=self.size:
            return 2*index
        return -1
    
    def rightChildIndex(self,index):
        if 2*index+1<=self.size:
            return 2*index+1
        return -1     
    
    def leftChild(self,index):
        if 2*index<=self.size:
            return self.heapList[2*index]
        return -1
    
    def rightChild(self,index):
        if 2*index+1<=self.size:
            return self.heapList[2*index+1]
        return -1
    
    def searchElement(self,itm):
        i=1
        while(i<=self.size):
            if itm==self.heapList[i]:
                return i
            i+=1
        return -1
    
    def getMinimum(self):
        
        if self.size==0:
            return -1
        return self.heapList[1]
    
    # reach down to the leaves
    # find the minimum child and swap if parent greater than the child
    def percolateDown(self,i):
        
        while(i*2)<=self.size:
        
            minimumChild=self.minimumChild(i)
            
            if self.heapList[i]>self.heapList[minimumChild]:
                self.heapList[i],self.heapList[minimumChild]=self.heapList[minimumChild],self.heapList[i]
            i=minimumChild

    # find child that is smaller, if only left child use that
    def minimumChild(self,i):
        
        if i*2+1>self.size:
            return i*2
        else:
            if self.heapList[i*2]<self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1
            
    # reach down to the root
    # if the child (i) less than its parent (i//2), switch the elements
    # do this up to the root        
    def percolateUp(self,i):
        
        while i//2>0:   
            if self.heapList[i]<self.heapList[i//2]:
                self.heapList[i//2],self.heapList[i]=self.heapList[i],self.heapList[i//2]
            i//=2
         
    # replace start of heap with the end, pop the end
    # and percolate down the start of the heap until its in its proper place
    def deleteMin(self):
        
        retval=self.heapList[1]
        self.heapList[1]=self.heapList[self.size]
        self.size-=1
        self.heapList.pop()
        self.percolateDown(1)
        return retval
    
    # append to end of heap
    # percolate up the element until its in its proper place
    def insert(self,k):
        self.heapList.append(k)
        self.size+=1
        self.percolateUp(self.size)
        
    def heapify(self,A):
        i=len(A)//2
        self.size=len(A)
        self.heapList=[0]+A[:]
        while(i>0):
            self.percolateDown(i)
            i-=1
            
    def heapSort(self,A):
        
        self.heapify(A)
        
        arr = []
        
        while self.size>0:
            arr.append(self.deleteMin())
            
        return arr
    
    # just start searching from the middle
    def findMaxinMinHeap(self):
        max=-float('infinity')
        for i in range((self.size+1)//2,self.size):
            if(self.heapList[i]>max):
                max=self.heapList[i]
        return max
    
    # delete at position
    def delete(self,i):
        if(self.size<i):
            return
        key=self.heapList[i]
        self.heapList[i]=self.heapList[self.size]
        self.heapList.pop()
        self.size-=1
        self.percolateDown(i)
        return key
    
if __name__=='__main__':
    
        h1=MinHeap()
        h1.insert(17)
        h1.insert(15)
        h1.insert(6)
        h1.insert(4)
        h1.insert(4)
        h1.insert(3)
        h1.insert(1)
        print(h1.heapList[1:])
        h1.deleteMin()
        print(h1.heapList[1:])
        print(h1.findMaxinMinHeap())
        h1.delete(3)
        print(h1.heapList[1:])
        print("\n")
        
        h2=MaxHeap()
        h2.insert(1)
        h2.insert(4)
        h2.insert(4)
        h2.insert(3)
        h2.insert(15)
        h2.insert(6)
        h2.insert(17)
        print(h2.heapList[1:])
        h2.deleteMax()
        print(h2.heapList[1:])
        print(h2.findMininMaxHeap())
        h2.delete(3)
        print(h2.heapList[1:])
        print("\n")
        
        h3=MinHeap()
        h3.heapify([17,6,1,4,4,3,15])
        print(h3.heapList[:])
        
        h4=MaxHeap()
        x=h4.heapSort([534, 246, 933, 127, 277, 321, 454, 565, 220])
        print(x)
        
        h5=MinHeap()
        y=h5.heapSort([534, 246, 933, 127, 277, 321, 454, 565, 220])
        print(y)
       
    
            