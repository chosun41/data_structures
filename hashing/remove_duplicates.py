from copy import deepcopy

# time: average n^2
def removeDuplicates1(A):
    
    def elem(A,n,e):
        for i in range(n):
            if A[i]==e:
                return 1
        return 0
    
    m=0
    for i in range(len(A)):
        if not elem(A,m,A[i]):
            A[m]=A[i]
            m+=1     
    return A[:m]

# sort so duplicates clustered together
# time: average n log n
def removeDuplicates2(A):
    A.sort()
    j=0
    for i in range(1,len(A)):
        if A[j]!=A[i]:
            j+=1
            A[j]=A[i]
    return A[:j+1]

# basically just list and set
# time: average n
def removeDuplicates3(A):
    unique = []
    helperSet = set()
    for x in A:
        if x not in helperSet:
            unique.append(x)
            helperSet.add(x)
    return unique

if __name__ == '__main__':
    A = [54,31,93,54,77,31,44,55,93]
    print(A)
    print(removeDuplicates1(deepcopy(A)))
    # m=0,[54,31,93,54,77,31,44,55,93]
    # i=0,m=0,[54,31,93,54,77,31,44,55,93],m=1
    # i=1,m=1,[54,31,93,54,77,31,44,55,93],m=2
    # i=2,m=2,[54,31,93,54,77,31,44,55,93],m=3
    # i=3,m=3,[54,31,93,54,77,31,44,55,93],m=3
    # i=4,m=3,[54,31,93,77,77,31,44,55,93],m=4
    # i=5,m=4,[54,31,93,77,77,31,44,55,93],m=4
    # i=6,m=4,[54,31,93,77,44,31,44,55,93],m=5
    # i=7,m=5,[54,31,93,77,44,55,44,55,93],m=6
    # i=8,m=6,[54,31,93,77,44,55,44,55,93],m=6
    #         [54,31,93,77,44,55]
    
    print(removeDuplicates2(deepcopy(A)))
    # j=0, [54,31,93,54,77,31,44,55,93] -> [31,31,44,54,54,55,77,93,93]
    # i=1,j=0,    [31,31,44,54,54,55,77,93,93]
    # i=2,j=0,j=1,[31,44,44,54,54,55,77,93,93]
    # i=3,j=1,j=2,[31,44,54,54,54,55,77,93,93]
    # i=4,j=2,    [31,44,54,54,54,55,77,93,93]  
    # i=5,j=2,j=3,[31,44,54,55,54,55,77,93,93]  
    # i=6,j=3,j=4,[31,44,54,55,77,55,77,93,93]  
    # i=7,j=4,j=5,[31,44,54,55,77,93,77,93,93]   
    # i=8,j=5     [31,44,54,55,77,93,77,93,93]   
    #             [31,44,54,55,77,93] 
    print(removeDuplicates3(deepcopy(A)))
    