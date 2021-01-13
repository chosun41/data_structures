def findStrobogrammatic(n):
    result = []
    hash = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    helper(result, [None]*n, 0, n-1, hash)
    
    return result
    
def helper(result, item, start, end, hash):
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
    print(findStrobogrammatic(5))