def maximumSwap(num):
    A = list(map(int, str(num)))
    last = {x: i for i, x in enumerate(A)}
    print(A)
    print(last)
    for i, x in enumerate(A):
        for d in range(9, x, -1):
            if d in last and last[d] > i: # bc you havent swapped before up to this point
                A[i], A[last[d]] = A[last[d]], A[i]
                return int("".join(map(str, A)))
    return num
    
if __name__ == '__main__':
    # time and space: O(n)
    # biggest number you can create by 1 swap
    print(maximumSwap(2736))