# pivot everything less than pivot to start, equal to pivot to middle, and larger than middle to the end
# time: O(n) space:O(1)

def dutch_flag_partition(pivot_index, A):

    pivot = A[pivot_index]
    # Keep the following invariants during partitioning:
    # bottom group: A[:smaller].
    # middle group: A[smaller:equal].
    # unclassified group: A[equal:larger].
    # top group: A[larger:].
    smaller, equal, larger = 0, 0, len(A)
    # Keep iterating as long as there is an unclassified element.
    while equal < larger:
        # A[equal] is the incoming unclassified element.
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else:  # A[equal] > pivot.
            larger -= 1 # why decrement before swap?
            A[equal], A[larger] = A[larger], A[equal]
    return A

    
if __name__ == '__main__':
    A=[0,1,2,0,2,1,1]
    print(dutch_flag_partition(3, A))
    print(dutch_flag_partition(2, A))