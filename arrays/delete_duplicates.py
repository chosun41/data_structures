# time: O(n) space:O(1)

def delete_duplicates(A):

    if not A:
        return []

    write_index = 1
    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]: #write index at 1 all here
            A[write_index] = A[i]
            write_index += 1
    return A[:write_index]

    
if __name__ == '__main__':
    A=[2,3,5,5,7,11,11,11,13]
    print(delete_duplicates(A))
    # [2,3,5,5,7,11,11,11,13]
    # write_index=1,i=1,2!=3,[2,3,5,5,7,11,11,11,13],write_index=2
    # write_index=2,i=2,3!=5,[2,3,5,5,7,11,11,11,13],write_index=3
    # write_index=3,i=3,5=5,[2,3,5,5,7,11,11,11,13],write_index=3
    # write_index=3,i=4,5!=7,[2,3,5,7,7,11,11,11,13],write_index=4
    # write_index=4,i=5,7!=11,[2,3,5,7,11,11,11,11,13],write_index=5
    # write_index=5,i=6,11=11,[2,3,5,7,11,11,11,11,13],write_index=5
    # write_index=5,i=7,11=11,[2,3,5,7,11,11,11,11,13],write_index=5
    # write_index=5,i=8,11!=13,[2,3,5,7,11,13,11,11,13],write_index=6
    # [2,3,5,7,11,13]
    