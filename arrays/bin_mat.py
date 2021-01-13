def leftMostColumnWithOne(binaryMatrix) -> int:
        
    rows = len(binaryMatrix) 
    cols = len(binaryMatrix[0]) 

    # Set pointers to the top-right corner.
    current_row = 0
    current_col = cols - 1

    # Repeat the search until it goes off the grid.
    while current_row < rows and current_col >= 0:
        if binaryMatrix[current_row][current_col] == 0:
            current_row += 1
        else:
            current_col -= 1

    # If we never left the last column, it must have been all 0's.
    return current_col + 1 if current_col != cols - 1 else -1
        

if __name__=='__main__':
    
    # each row is nondecreasing and each row after is a seq>=prev row
    # find leftmost col with a 1
    # time: O(m+n)
    # space: O(1)

    print(leftMostColumnWithOne([[0,0],[0,0]]))
    print(leftMostColumnWithOne([[0,0],[0,1]]))
    print(leftMostColumnWithOne([[0,0],[1,1]]))
    print(leftMostColumnWithOne([[0,0,0,1],[0,0,1,1],[0,1,1,1]]))