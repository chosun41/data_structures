def factorial1(n):
    if n == 0: 
        return 1
    return n * factorial1(n - 1)

factTable = {}

def factorial2(n):
    try:
        return factTable[n]
    except KeyError:
        if n == 0:
            factTable[0] = 1
            return 1
        else:
            factTable[n] = n * factorial2(n - 1)
            return factTable[n]

if __name__=='__main__':
    
    # factorial1 - time: O(n+m), space: O(max(m,n))
    # factorial2 - time: O(max(m,n)), space:O(max(m,n))
    print(factorial1(6))
    print(factorial2(6))