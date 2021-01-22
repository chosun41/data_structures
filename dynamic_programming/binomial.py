def compute_binomial_coefficient(n, k):

    if k in (0, n):
        return 1

    without_k = compute_binomial_coefficient(n - 1, k)
    with_k = compute_binomial_coefficient(n - 1, k - 1)
    return without_k + with_k

if __name__ == '__main__':
    
    # O(nk)
    # (n k) = (n-1 k) + (n-1 k-1)
    
    print(compute_binomial_coefficient(5,2))