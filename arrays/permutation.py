def apply_permutation(perm, A):
    
    for i in range(len(A)):
        while perm[i] != i:
            A[perm[i]], A[i] = A[i], A[perm[i]] #perm[i] has to be first
            perm[perm[i]], perm[i] = perm[i], perm[perm[i]] #perm[perm[i]] has to be first
            print(A)
            print(perm)
    return A
            
if __name__ == '__main__':
    
    # time: O(n log n) space: O(n)
    print(apply_permutation([2,0,1,3], ['a','b','c','d']))
    
    # 0.i=0
    #   perm[0] = 2, A=['c', 'b', 'a', 'd'],perm=[1, 0, 2, 3]
    #   perm[0] = 1, A=['b', 'c', 'a', 'd'],perm=[0, 1, 2, 3]
    #  
    # 1. i=1 perm[1] = 1
    # 2. i=2 perm[2]=2
    # 3. i=3 perm[3]=3