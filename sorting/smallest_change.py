def smallest_nonconstructible_value(A):

    max_constructible_value = 0
    for a in sorted(A):
        if a > max_constructible_value + 1:
            break
        max_constructible_value += a
    return max_constructible_value + 1 #important max constructible value + 1

if __name__ == '__main__':
    
    # smallest change that can't be made by adding several values
    # time: O(n log n) space: O(1)
    
    print(smallest_nonconstructible_value([1,3]))
    print(smallest_nonconstructible_value([1,2]))
    print(smallest_nonconstructible_value([1,2,5]))
    print(smallest_nonconstructible_value([12,2,1,15,2,4]))
    
    # 1,2,2,4,12,15
    # 1=1,max=1
    # 2=2,max=3
    # 2<4,max=5
    # 4<6,max=9
    # 12>10, return 10