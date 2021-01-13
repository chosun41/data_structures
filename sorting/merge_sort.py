def MergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        lefthalf = A[:mid]
        righthalf = A[mid:]
        MergeSort(lefthalf)
        MergeSort(righthalf)
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                A[k] = lefthalf[i]
                i += 1
            else:
                A[k] = righthalf[j]
                j += 1
            k += 1

        # anything thats left
        while i < len(lefthalf):
            A[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            A[k] = righthalf[j]
            j += 1
            k += 1
            
    return A
            
if __name__ == '__main__':
    
    # time: 0(nlogn) 
    # divide all into individual lists and comparison between recursive pairs
    
    A = [54,26,93,17,77,31,44,55,20]
    print(MergeSort(A))
    # [54,26,93,17] [77,31,44,55,20]
    # [54,26] [93,17] [77,31] [44,55,20]
    # [54] [26] [93] [17] [77] [31] [44] [55,20]
    # [26,54]  [17,93]   [31,77]  [44] [55] [20]
    #  [17,26,54,93]     [31,77]   [44]  [20,55]
    #  [17,26,54,93]     [31,77]  [20,44,55]
    #   [17,26,54,93]    [20,31,44,55,77]
    #            [17,20,26,31,44,54,55,77,93]