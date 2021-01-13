def removeAdjacentDuplicates2(S):
    output = []
    for ch in S:
        if output and ch == output[-1]: 
            output.pop()
        else: 
            output.append(ch)
    return ''.join(output)

if __name__=='__main__':
    
    # time: O(n)
    # space: O(n-d) d # of duplicates 
    # stack
    print(removeAdjacentDuplicates2(['6', '2', '4', '1', '2', '1', '2', '2', '1']))