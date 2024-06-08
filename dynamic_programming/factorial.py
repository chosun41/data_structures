def factorial1(n):
    if n == 0: 
        return 1
    return n * factorial1(n - 1)

factTable = {}

def factorial2(n): 
       
    res = 1
      
    for i in range(2, n+1): 
        res *= i 
    return res 

if __name__=='__main__':
    
    # factorial1 - time and space: O(n)
    # factorial2 - time: O(n) space: 0(1)
    print(factorial1(6))
    print(factorial2(6))