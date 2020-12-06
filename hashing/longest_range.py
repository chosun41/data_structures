def longest_contained_range(A):

    # unprocessed_entries records the existence of each entry in A.
    unprocessed_entries = set(A)

    max_interval_size = 0
    while unprocessed_entries:
        a = unprocessed_entries.pop()

        # Finds the lower bound of the largest range containing a.
        lower_bound = a - 1
        while lower_bound in unprocessed_entries:
            unprocessed_entries.remove(lower_bound)
            lower_bound -= 1

        # Finds the upper bound of the largest range containing a.
        upper_bound = a + 1
        while upper_bound in unprocessed_entries:
            unprocessed_entries.remove(upper_bound)
            upper_bound += 1

        max_interval_size = max(max_interval_size,
                                upper_bound - lower_bound - 1)
    return max_interval_size


if __name__=='__main__':
    
    # make sure that b/t two integers, all the numbers exist and give the size of that biggest subset
    # basically you just check lower and upper bound -1/+1 repeatedly and update lower and upper bounds
    # update the max_interval_size and do this until unprocessed is empty
    # here is [-2,-1,0,1,2,3] -> 6
    # time: O(n)

    A=[3,-2,7,9,8,1,2,0,-1,5,8]

    print(longest_contained_range(A))
    
    # 0. unprocessed_entries=[3,-2,7,9,8,1,2,0,-1,5]
    #    a=3
    #    l=-3,u=4
    #    max_interval_size=6
    # 1. unprocessed_entries=[7,9,8,5]
    #    a=7
    #    l=6,u=10
    #    max_interval_size=max(3,6)
    # 2. unprocessed_entries=[5]
    #    a=5
    #    l=4,u=6
    #    max_interval_size=max(1,6)
         
    
    