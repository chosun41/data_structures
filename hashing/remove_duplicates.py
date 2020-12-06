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
    print(removeDuplicates1(A))
    print(removeDuplicates2(A))
    print(removeDuplicates3(A))
    