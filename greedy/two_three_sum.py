def has_two_sum(A, t):

    i, j = 0, len(A) - 1

    while i <= j:
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j] < t:
            i += 1
        else:  # A[i] + A[j] > t.
            j -= 1
    return False

def has_three_sum(A, t):

    A.sort()
    # Finds if the sum of two numbers in A equals to t - a.
    return any(has_two_sum(A, t - a) for a in A)

if __name__ == '__main__':
    
    # two sum O(n), three sum O(n^2), space O(1), not necessarily distinct
    
    print(has_two_sum([-2,1,2,4,7,11],6))
    print(has_two_sum([-2,1,2,4,7,11],10))
    print(has_three_sum([-2,1,2,4,7,11],17))
    print(has_three_sum([-2,1,2,4,7,11],21)) #7,7,7