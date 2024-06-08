def binomialCoeff(n, k):
     
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
 
    # Recursive Call
    return binomialCoeff(n-1, k-1) + binomialCoeff(n-1, k)

if __name__ == '__main__':

    # Time : O(n*max(k,n-k)) 
    # Space: O(n*max(k,n-k))
    
    # C(n, k) = C(n-1, k-1) + C(n-1, k) C(5,2) = C(4,3) + C(4,2)  10 = 4+6
    # C(n, 0) = C(n, n) = 1
    
    print(binomialCoeff(5,2))