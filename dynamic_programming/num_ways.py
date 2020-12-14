def number_of_ways(n, m):
    def compute_number_of_ways_to_xy(x, y):
        if x == y == 0:
            return 1

        ways_top = 0 if x == 0 else compute_number_of_ways_to_xy(x - 1, y)
        ways_left = 0 if y == 0 else compute_number_of_ways_to_xy(x, y - 1)
        return ways_top + ways_left

    return compute_number_of_ways_to_xy(n - 1, m - 1)

if __name__ == '__main__':
    
    # time: O(mn), space: O(mn)
    # total number of ways to get from top left to bottom right
    
    print(number_of_ways(5,5))
    
    # 1 1 1  1  1
    # 1 2 3  4  5
    # 1 3 6  10 15
    # 1 4 10 20 35
    # 1 5 15 35 70