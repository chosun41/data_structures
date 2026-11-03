def combinations(n,k):
    def backtrack(first = 1, curr = []):
        # if the combination is done
        if len(curr) == k:  
            output.append(curr[:])
            return
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
    
    # time and space: O(C (n k)) time because of append and pop
    print(combinations(5, 3))
    # avoid repeats because i keeps going up

    # i,curr,output = 1,[],[]
    # i,curr,output = 1,[1],[] -> backtrack(2,[1])
    # i,curr,output = 2,[1,2],[] -> backtrack(3,[1,2])
        # i,curr,output = 3,[1,3],[[1,2,3],[1,2,4],[1,2,5]] -> backtrack(4, [1,3])
            # i,curr,output = 4,[1,3,4],[[1,2,3],[1,2,4],[1,2,5]] -> backtrack(5,[1,3,4])
                 # i,curr,output = 4,[1,3,4],[[1,2,3],[1,2,4],[1,2,5],[1,3,4]] ^
                 # i,curr,output = 4,[1,3],[[1,2,3],[1,2,4],[1,2,5],[1,3,4]]
                 # i,curr,output = 5,[1,3,5],[[1,2,3],[1,2,4],[1,2,5],[1,3,4]] -> backtrack(6,[1,3,5])
                     # i,curr,output = 6,[1,3,5],[[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5]] ^
                     # i,curr,output = 6,[1,3],[[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5]]
    # i,curr,output = 3,[1,2,3],[] -> backtrack(4,[1,2,3])
        # i,curr,output = 3,[1,2,3],[[1,2,3]] ^
        # i,curr,output = 3,[1,2],[[1,2,3]]
        # i,curr,output = 4,[1,2,4],[[1,2,3]] -> backtrack(5,[1,2,4])
            # i,curr,output = 4,[1,2,4],[[1,2,3],[1,2,4]] ^
            # i,curr,output = 4,[1,2],[[1,2,3],[1,2,4]] 
            # i,curr,output = 5,[1,2,5],[[1,2,3],[1,2,4]] -> backtrack(6,[1,2,5])
                # i,curr,output = 6,[1,2,5],[[1,2,3],[1,2,4],[1,2,5]] 
                # i,curr,output = 6,[1,2],[[1,2,3],[1,2,4],[1,2,5]] ^