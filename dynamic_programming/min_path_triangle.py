def minimum_path_weight(triangle):

    min_weight_to_curr_row = [0]
    for row in triangle:
        min_weight_to_curr_row = [
            row[j] + 
            min(min_weight_to_curr_row[max(j - 1, 0)],
                min_weight_to_curr_row[min(j,len(min_weight_to_curr_row) - 1)])
            for j in range(len(row))]
        
        # for each entry in the row (j), add from the minimum of the previous entry or the previous row, next col if it exists
        
    return min(min_weight_to_curr_row)

if __name__ == '__main__':
    
    # time:O(n^2),space:O(n)
    
    triangle = [[2],[4,4],[8,5,6],[4,2,6,2],[1,5,2,3,4]]
    
    print(minimum_path_weight(triangle))
    
    # min path to each
    # [2]
    # [6, 6]
    # [14, 11, 12]
    # [18, 13, 17, 14]
    # [19, 18, 15, 17, 18]
    # 2+4+5+2+2=15

    