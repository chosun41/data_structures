def generate_pascal_triangle(n):

    result = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            # Sets this entry to the sum of the two above adjacent entries.
            result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
    return result

            
if __name__ == '__main__':
     
    # time and space: O(n^2)
    
    print(generate_pascal_triangle(5))
    
    # 1
    # 11
    # 121
    # 1331
    # 14641