def generate_primes(n):

    primes=[]
    is_prime=[False,False]+[True]*(n-1)
    for p in range(2,n+1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p*2,n+1,p):
                is_prime[i] = False
    return primes
    
if __name__ == '__main__':
    
    # time: O(n log log n) space: O(n)
    print(generate_primes(18))