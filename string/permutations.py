def permut(array):
    if len(array) == 1:
        return [array]
    res = []
    for permutation in permut(array[1:]):
        for i in range(len(array)):
            res.append(permutation[:i] + array[0:1] + permutation[i:])
    print(res)
    return res
        
if __name__=='__main__':
    elems = [1, 2, 3]
    print(permut(elems))
    
    # array=[1,2,3]
    # for permutation in permut([2,3])
    # for permutation in [[2,3],[3,2]]
        # for i in range(3):
    # res=[[1,2,3],[2,1,3],[2,3,1],[1,3,2],[3,1,2],[3,2,1]]
    
        # array=[2,3]
        # for permutation in permut([3])
        # for permutation in [[3]]:
            # for i in range(2):
        # res=[[2,3],[3,2]]
        
        
    
            # array=[3]
            # return [[3]]
            
        
        