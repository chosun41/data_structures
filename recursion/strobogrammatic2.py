def findStrobogrammatic(n):
    result = []
    hash = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    def helper(result, item, start, end): # need to separate functions because of result capture not sub function
        if start > end:
            result.append(''.join(item))
            return
        
        for key in hash: 
            if start == end and key in ('6','9'): # middle position conditions
                continue
            
            if start != end and start == 0 and key == '0': # start position conditions
                continue
            
            item[start], item[end] = key, hash[key]

            helper(result, item, start+1, end-1)

    helper(result, [None]*n, 0, n-1)
    
    return result
        
if __name__=='__main__':
    # strobogrammatic is it looks same upside down
    # find strings of length n that are strobogrammatic
    # time: O(5^n) 5 options in each slot
    # space: O(5^n)
    print(len(findStrobogrammatic(5)))