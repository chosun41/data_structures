from copy import deepcopy

def quickSort(A,low,high):
    if low >= high:
        return
    pivot = A[low]
    i = low+1
    j = high
    while i <= j:
        while i <= j and A[i] <= pivot:
            i = i + 1
        while A[j] >= pivot and j >= i:
            j = j -1
        if j < i:
            break
        A[i], A[j] = A[j], A[i]

    A[low], A[j] = A[j], A[low]
    partitionPoint = j

    quickSort(A,low,partitionPoint-1)
    quickSort(A,partitionPoint+1,high)
    
    return A

import random
def quickSortRandom(A, low, high):
    if low < high:
        pivot = Partition(A, low, high)
        quickSortRandom(A, low, pivot - 1)
        quickSortRandom(A, pivot + 1, high)
    return A
 
def Partition(A, low, high) :
    pivot = random.randrange(low,high)
    A[pivot],A[high]=A[high],A[pivot]
    for i in range(low, high):
        if A[i] <= A[high]: #bc pivot is high now
            A[low],A[i]=A[i],A[low]
            low += 1
 
    A[low],A[high]=A[high],A[low] # place pivot back in middle
    return low
    
if __name__ == '__main__':
    
    # time: 0(nlogn) 
    # makes use of pivot to recursively organize elements <,=,> between sublists, 
    # randomized quick sort has better average time case
    
    A = [54,26,93,17,77,31,44,55,20]
    print(quickSort(deepcopy(A),0,len(A)-1))
    print(quickSortRandom(deepcopy(A),0,len(A)-1))
    
    # low=0,high=8
    # pivot=54
    # i=1,j=8
    # 26<=54,i=2
    # 93>54,i=2
    # 20<54,j=8
    # [54,26,20,17,77,31,44,55,93]
    # 20<=54,i=3
    # 17<=54,i=4
    # 77>54,i=4
    # 93>=54,j=7
    # 55>=54,j=6
    # 44<54,j=6
    # [54,26,20,17,44,31,77,55,93]
    # 44<=54,i=5
    # 31<=54,i=6
    # 77>54,i=6
    # 77>=54,j=5
    # [31,26,20,17,44,54,77,55,93]
    # partitionpoint=5
    
        # low=0,high=4
        # pivot=31
        # i=1,j=4
        # 26<=31,i=2
        # 20<=31,i=3
        # 17<=31,i=4
        # 44>31,i=4
        # 44>=31,j=3
        # 17<31,j=3
        # [17,26,20,31,44,54,77,55,93]
        # partitionpoint=3
        
            # low=0,high=2
            # pivot=17
            # i=1,j=2
            # 26>17,i=1
            # 20>=17,j=1
            # 26>=17,j=0
            # [17,26,20,31,44,54,77,55,93]
            # partitionpoint=0
                
                # low=0,high=-1 return
                
                # low=1,high=2
                # pivot=26
                # i=2,j=2
                # 20<=26,i=3
                # [17,20,26,31,44,54,77,55,93]
            
            # low=4,high=4 return
    
        # low=6,high=8
        # pivot=77
        # i=7,j=8
        # 55<77,i=7
        # 93>77,j=7
        # 55<77,j=7
        # [17,20,26,31,44,54,77,55,93]
        # partitionpoint=7

            # low=6,high=6 return
            # low=8,high=8 return
