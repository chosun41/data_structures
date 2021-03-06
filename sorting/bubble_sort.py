from copy import deepcopy

def BubbleSort1(A):
    for i in range(len(A)):
        for k in range(len(A) - 1, i, -1):
                if (A[k] < A[k - 1]):
                    A[k],A[k - 1]=A[k - 1],A[k]
    return A

def BubbleSort2(A):
    
    swapped = True 
    
    for i in range(len(A)):
        
        swapped=False

        for k in range(len(A) - 1, i, -1):
            if (A[k] < A[k - 1]):
                A[k],A[k - 1]=A[k - 1],A[k]
                swapped = True 
        
        # if there were no swaps return A
        if swapped==False:
            return A
                
                
if __name__ == '__main__':
    
    # time: 0(n^2) 
    # start at the front and back and swap if A[k-1]<A[k] down to i
    # second sort basically has a swapped parameter to check if one iteration has no swaps, return the list
    
    A = [54,26,93,17,77,31,44,55,20]
    
    print(BubbleSort1(deepcopy(A))) 
    # i=0, k=8, [54,26,93,17,77,31,44,20,55]
    # i=0, k=7, [54,26,93,17,77,31,20,44,55]
    # i=0, k=6, [54,26,93,17,77,20,31,44,55]
    # i=0, k=5, [54,26,93,17,20,77,31,44,55]
    # i=0, k=4, [54,26,93,17,20,77,31,44,55]
    # i=0, k=3, [54,26,17,93,20,77,31,44,55]
    # i=0, k=2, [54,17,26,93,20,77,31,44,55]
    # i=0, k=1, [17,54,26,93,20,77,31,44,55]
    # i=1, k=8, [17,54,26,93,20,77,31,44,55]
    # i=1, k=7, [17,54,26,93,20,77,31,44,55]
    # i=1, k=6, [17,54,26,93,20,31,77,44,55]
    # i=1, k=5, [17,54,26,93,20,31,77,44,55]
    # i=1, k=4, [17,54,26,20,93,31,77,44,55]
    # i=1, k=3, [17,54,20,26,93,31,77,44,55]
    # i=1, k=2, [17,20,54,26,93,31,77,44,55]
    # i=2, k=8, [17,20,54,26,93,31,77,44,55]
    # i=2, k=7, [17,20,54,26,93,31,44,77,55]
    # i=2, k=6, [17,20,54,26,93,31,44,77,55]
    # i=2, k=5, [17,20,54,26,31,93,44,77,55]
    # i=2, k=4, [17,20,54,26,31,93,44,77,55]
    # i=2, k=3, [17,20,26,54,31,93,44,77,55]
    # i=3, k=8, [17,20,26,54,31,93,44,55,77]
    # i=3, k=7, [17,20,26,54,31,93,44,55,77]
    # i=3, k=6, [17,20,26,54,31,44,93,55,77]
    # i=3, k=5, [17,20,26,54,31,44,93,55,77]
    # i=3, k=4, [17,20,26,31,54,44,93,55,77]
    # i=4, k=8, [17,20,26,31,54,44,93,55,77]
    # i=4, k=7, [17,20,26,31,54,44,55,93,77]
    # i=4, k=6, [17,20,26,31,54,44,55,93,77]
    # i=4, k=5, [17,20,26,31,44,54,55,93,77]
    # i=5, k=8, [17,20,26,31,44,54,55,77,93]
    # i=5, k=7, [17,20,26,31,44,54,55,77,93]
    # i=5, k=6, [17,20,26,31,44,54,55,77,93]
    # i=6, k=8, [17,20,26,31,44,54,55,77,93]
    # i=6, k=7, [17,20,26,31,44,54,55,77,93]
    # i=7, k=8, [17,20,26,31,44,54,55,77,93]
    
    print(BubbleSort2(deepcopy(A))) 
    # i=0, k=8, [54,26,93,17,77,31,44,20,55], swapped=True
    # i=0, k=7, [54,26,93,17,77,31,20,44,55], swapped=True
    # i=0, k=6, [54,26,93,17,77,20,31,44,55], swapped=True
    # i=0, k=5, [54,26,93,17,20,77,31,44,55], swapped=True
    # i=0, k=4, [54,26,93,17,20,77,31,44,55], swapped=True
    # i=0, k=3, [54,26,17,93,20,77,31,44,55], swapped=True
    # i=0, k=2, [54,17,26,93,20,77,31,44,55], swapped=True
    # i=0, k=1, [17,54,26,93,20,77,31,44,55], swapped=True
    # i=1, k=8, [17,54,26,93,20,77,31,44,55], swapped=False
    # i=1, k=7, [17,54,26,93,20,77,31,44,55], swapped=False
    # i=1, k=6, [17,54,26,93,20,31,77,44,55], swapped=True
    # i=1, k=5, [17,54,26,93,20,31,77,44,55], swapped=True
    # i=1, k=4, [17,54,26,20,93,31,77,44,55], swapped=True
    # i=1, k=3, [17,54,20,26,93,31,77,44,55], swapped=True
    # i=1, k=2, [17,20,54,26,93,31,77,44,55], swapped=True
    # i=2, k=8, [17,20,54,26,93,31,77,44,55], swapped=False
    # i=2, k=7, [17,20,54,26,93,31,44,77,55], swapped=True
    # i=2, k=6, [17,20,54,26,93,31,44,77,55], swapped=True
    # i=2, k=5, [17,20,54,26,31,93,44,77,55], swapped=True
    # i=2, k=4, [17,20,54,26,31,93,44,77,55], swapped=True
    # i=2, k=3, [17,20,26,54,31,93,44,77,55], swapped=True
    # i=3, k=8, [17,20,26,54,31,93,44,55,77], swapped=True
    # i=3, k=7, [17,20,26,54,31,93,44,55,77], swapped=True
    # i=3, k=6, [17,20,26,54,31,44,93,55,77], swapped=True
    # i=3, k=5, [17,20,26,54,31,44,93,55,77], swapped=True
    # i=3, k=4, [17,20,26,31,54,44,93,55,77], swapped=True
    # i=4, k=8, [17,20,26,31,54,44,93,55,77], swapped=False
    # i=4, k=7, [17,20,26,31,54,44,55,93,77], swapped=True
    # i=4, k=6, [17,20,26,31,54,44,55,93,77], swapped=True
    # i=4, k=5, [17,20,26,31,44,54,55,93,77], swapped=True
    # i=5, k=8, [17,20,26,31,44,54,55,77,93], swapped=True
    # i=5, k=7, [17,20,26,31,44,54,55,77,93], swapped=True
    # i=5, k=6, [17,20,26,31,44,54,55,77,93], swapped=True
    # i=6, k=8, [17,20,26,31,44,54,55,77,93], swapped=False
    # i=6, k=7, [17,20,26,31,44,54,55,77,93], swapped=False
