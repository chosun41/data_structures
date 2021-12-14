def findStrobogrammatic(n):
    result = []
    hash = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    helper(result, [None]*n, 0, n-1, hash)
    
    return result
    
def helper(result, item, start, end, hash): # need to separate functions because of result capture not sub function
    if start > end:
        result.append(''.join(item))
        return
    
    for key in hash: 
        if start == end and key in ('6','9'): # 6,9 cant be in odd middle position
            continue
        
        if start != end and start == 0 and key == '0': 
            continue
        
        item[start], item[end] = key, hash[key]
        helper(result, item, start+1, end-1, hash)
        
if __name__=='__main__':
    # strobogrammatic is it looks same upside down
    # find strings of length n that are strobogrammatic
    # time: O(5 ^(n/2))
    # space: O(n)
    #     Time complexity : O(5^(N/2)), at ecah step we have 5 options except '4' options at first location ("0" cant be placed at first location). Fanout is 5 and depth of the tree is N/2, since at each level, we fill start and end positions simultaneously. 

    # Space Complexity: At a time only one brach is explore and remains in the stack, O(N/2)~O(N)
    print(findStrobogrammatic(5))