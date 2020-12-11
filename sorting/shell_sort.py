def ShellSort(arr): 
  
    # Start with a big gap, then reduce the gap 
    n = len(arr) 
    gap = n//2
  
    # Do a gapped insertion sort for this gap size. 
    # The first gap elements a[0..gap-1] are already in gapped  
    # order keep adding one more element until the entire array 
    # is gap sorted 
    while gap > 0: 
  
        for i in range(gap,n): 
  
            # add a[i] to the elements that have been gap sorted 
            # save a[i] in temp and make a hole at position i 
            temp = arr[i] 
  
            # shift earlier gap-sorted elements up until the correct 
            # location for a[i] is found 
            j = i 
            while  j >= gap and arr[j-gap] >temp: 
                arr[j] = arr[j-gap] 
                j -= gap 
  
            # put temp (the original a[i]) in its correct location 
            arr[j] = temp 
        
        gap //= 2
    
    return arr

if __name__ == '__main__':
    
    # time: 0(n^2) 
    # makes use of gaps
    
    A = [54,26,93,17,77,31,44,55,20]
    print(ShellSort(A))
    
    # n=9
    # gap=4
    # i=4,temp=77,j=4,54<77,[54,26,93,17,77,31,44,55,20]
    # i=5,temp=31,j=5,26<31,[54,26,93,17,77,31,44,55,20]
    # i=6,temp=44,j=6,93>44,j=2[54,26,44,17,77,31,93,55,20]
    # i=7,temp=55,j=7,17<55,[54,26,44,17,77,31,93,55,20]
    # i=8,temp=22,j=8,77>20,54>20,j=0,[20,26,44,17,54,31,93,55,77]
    # gap=2
    # i=2,temp=44,j=2,20<44,[20,26,44,17,54,31,93,55,77]
    # i=3,temp=17,j=3,26>17,j=1,[20,17,44,26,54,31,93,55,77]
    # i=4,temp=54,j=4,44<54,[20,17,44,26,54,31,93,55,77]
    # i=5,temp=31,j=5,26<31,[20,17,44,26,54,31,93,55,77]
    # i=6,temp=93,j=6,54<93,[20,17,44,26,54,31,93,55,77]
    # i=7,temp=55,j=7,31<55,[20,17,44,26,54,31,93,55,77]
    # i=8,temp=77,j=8,93>77,j=6,[20,17,44,26,54,31,77,55,93]
    # gap=1
    # i=1,temp=17,j=1,20>17,j=0,[17,20,44,26,54,31,77,55,93]
    # i=2,temp=44,j=2,20<44,[17,20,44,26,54,31,77,55,93]
    # i=3,temp=26,j=3,44>26,j=2,[17,20,26,44,54,31,77,55,93]
    # i=4,temp=54,j=4,44<54,[17,20,26,44,54,31,77,55,93]
    # i=5,temp=31,j=5,54>31,j=4,j=3,[17,20,26,31,44,54,77,55,93]
    # i=6,temp=77,j=6,54>77,[17,20,26,31,44,54,77,55,93]
    # i=7,temp=55,j=7,77>55,[17,20,26,31,44,54,55,77,93]
    # i=8,temp=93,j=8,77<93,[17,20,26,31,44,54,55,77,93]
    # gap=0