# time: O(n) space:O(1)

def delete_duplicates(A):

    if not A:
        return []

    write_index = 1
    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return A[:write_index]

    
if __name__ == '__main__':
    A=[2,3,5,5,7,11,11,11,13]
    print(delete_duplicates(A))