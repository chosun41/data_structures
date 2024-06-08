def lis(arr): 
    n = len(arr)
    res = [1] * n 
    for i in range(1,n):
        for j in range(i):
            if arr[j]<arr[i] and res[j]+1>res[i]:
                res[i]+=1
    print(res)
    return res[-1]

# end of lis function 

if __name__=='__main__':

    # time: O(n^2)
    # longest increasing subseqeunce not necessarily contiguous, but left to right, up to current index
    arr = [10, 22, 9, 33, 21, 50, 41, 60] # 10,22,33,41,60 or 10,22,33,50,60
    print(lis(arr))

    # i,j,lis = 1,0,[1,2,1,1,1,1,1,1]

    # i,j,lis = 2,0,[1,2,1,1,1,1,1,1]
    # i,j,lis = 2,1,[1,2,1,1,1,1,1,1]

    # i,j,lis = 3,0,[1,2,1,2,1,1,1,1]
    # i,j,lis = 3,1,[1,2,1,3,1,1,1,1]
    # i,j,lis = 3,2,[1,2,1,3,1,1,1,1]

    # i,j,lis = 4,0,[1,2,1,3,2,1,1,1]
    # i,j,lis = 4,1,[1,2,1,3,2,1,1,1]
    # i,j,lis = 4,2,[1,2,1,3,2,1,1,1] lis[4]<lis[2]+1 -> 2=2 (i=2 not part of an increasing subseq)
    # i,j,lis = 4,3,[1,2,1,3,2,1,1,1]
    
    # i,j,lis = 5,0,[1,2,1,3,2,2,1,1]
    # i,j,lis = 5,1,[1,2,1,3,2,3,1,1]
    # i,j,lis = 5,2,[1,2,1,3,2,4,1,1]
    # i,j,lis = 5,3,[1,2,1,3,2,4,1,1]
    # i,j,lis = 5,4,[1,2,1,3,2,4,1,1]

    # i,j,lis = 6,0,[1,2,1,3,2,4,2,1]
    # i,j,lis = 6,1,[1,2,1,3,2,4,3,1]
    # i,j,lis = 6,2,[1,2,1,3,2,4,3,1]
    # i,j,lis = 6,3,[1,2,1,3,2,4,4,1]
    # i,j,lis = 6,4,[1,2,1,3,2,4,4,1]
    # i,j,lis = 6,5,[1,2,1,3,2,4,4,1]

    # i,j,lis = 7,0,[1,2,1,3,2,4,4,2]
    # i,j,lis = 7,1,[1,2,1,3,2,4,4,3]
    # i,j,lis = 7,2,[1,2,1,3,2,4,4,3]
    # i,j,lis = 7,3,[1,2,1,3,2,4,4,4]
    # i,j,lis = 7,4,[1,2,1,3,2,4,4,4]
    # i,j,lis = 7,5,[1,2,1,3,2,4,4,5]
    # i,j,lis = 7,6,[1,2,1,3,2,4,4,5]




