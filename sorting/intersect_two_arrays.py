def intersect_two_sorted_arrays(A, B):
    
    i,j,intersection_A_B=0,0,[]
    
    while i<len(A) and j<len(B):
        if A[i]==B[j]:
            if i==0 or A[i]!=A[i-1]: # to escape duplicates on just one side
                intersection_A_B.append(A[i])
            i,j=i+1,j+1
        elif A[i]<B[j]:
            i+=1
        else:
            j+=1
    return intersection_A_B


if __name__ == '__main__':

    # time and space: O(m + n)
    print(intersect_two_sorted_arrays([2,3,3,5,5,6,7,7,8,12],[5,5,6,8,8,9,10,10]))