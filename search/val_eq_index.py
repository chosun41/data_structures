def search_entry_equal_to_its_index(A):

    left, right = 0, len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        difference = A[mid] - mid
        # A[mid] == mid if and only if difference == 0.
        if difference == 0:
            return mid
        elif difference > 0: # bc left has less than value
            right = mid - 1
        else:  # difference < 0. # bc right has more than value
            left = mid + 1
    return -1
    
if __name__=='__main__':
    
    # this works only if sorted, take advantage of position
    # left and right index at either ends,if the diff of A[(left+right)//2]-mid =0 then you found
    # your index, if its more look left (mid-1), if its less, then look right (mid+1)
    # time: O(log n)
    
    print(search_entry_equal_to_its_index([-2,0,2,3,6,7,9]))