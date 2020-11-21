from stack import Stack

def findingSpans(A):
    
    D = Stack()
    S = [None] * len(A)
    
    # to find the number of consecutive days that price has been <= current
    
    for i in range(len(A)):
        
        # keep popping as long as D is not empty and A i > A peek of D (compare prices to past)
        # P will become the index of the day where the earlier daily value is equal or greater
        # S will calculate the number of days between the current and last greater value
        while not D.isEmpty() and A[i] > A[D.peek()]:
            D.pop()
            
        if D.isEmpty():
            P = -1
        else:
            P = D.peek()
            
        S[i] = i - P
        
        # push current index to D
        D.push(i)
        
    print(S)


if __name__ == "__main__":
    
    findingSpans([6, 3, 4, 5, 2])
    
    # 1. D = [0]
    #    S = [1,None,None,None,None]
    #    P = -1
    # 2. D = [0,1]
    #    S = [1,1,None,None,None] - 3<6
    #    P = 0
    # 3. D = [0,2]
    #    S = [1,1,2,None,None] - 4>3 4<6
    #    P = 0
    # 4. D = [0,3]
    #    S = [1,1,2,3,None] - 5>4 5<6 
    #    P = 0
    # 5. D = [0,3]
    #    S = [1,1,2,3,1] - 2<5
    #    P = 3