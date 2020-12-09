def prefixTable(pattern):
    m = len(pattern)
    F = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = F[k - 1]
        if pattern[k] == pattern[q]:
            k = k + 1
        F[q] = k
    return F

def KMP(text, pattern):
    n = len(text)
    m = len(pattern)
    F = prefixTable(pattern)
    q = 0
    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = F[q - 1]
        if pattern[q] == text[i]:
            q = q + 1
        if q == m:
            return i - m + 1
    return -1

if __name__=='__main__':
    
    # time: O(m+n)
                
    print(KMP("bacbabababacaca", "ababaca")) 
   
    # prefix table - m=7, ababaca - 0000000,k=0
    # q=1,k=0,ababaca - 0000000
    # q=2,k=1,ababaca - 0010000
    # q=3,k=2,ababaca - 0012000
    # q=4,k=3,ababaca - 0012300
    # q=5,k=1,ababaca - 0012310
    # q=6,k=1,ababaca - 0012311
    
    # kmp - n=15,m=7,q=0
    # i=0. q=0
    # i=1. q=0
    # i=2. q=1
    # i=3. q=0
    # i=4. q=0
    # i=5. q=1
    # i=6. q=2
    # i=7. q=3
    # i=8. q=4
    # i=9. q=5
    # i=10. q=4
    # i=11. q=5
    # i=12. q=6