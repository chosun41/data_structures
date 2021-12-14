def combinations(n,k):
    def backtrack(first = 1, curr = []):
        # if the combination is done
        if len(curr) == k:  
            output.append(curr[:])
        for i in range(first, n + 1): # first
            # add i into the current combination
            curr.append(i)
            # use next integers to complete the combination
            backtrack(i + 1, curr) #i+1 not first+1
            # backtrack
            curr.pop()
    
    output = []
    backtrack()
    return output

if __name__ == '__main__':
    
    # time: O(k C (k n)) space: O(C (k n)) time because of append and pop
    print(combinations(5, 3))