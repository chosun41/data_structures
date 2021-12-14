from collections import deque

# also contains appendleft in addition to popleft for deque
# produce minimum value for every sliding window of size k
 
def MinSlidingWindow(A, k):
    
    D = deque()
    res = []
    
    # tuples in deque
    
    for i in range(len(A)):
        
        # while last value in dequeue is greater or equal than current value, pop
        # makes sure min is left
        while D and D[-1][0] >= A[i]:
            D.pop()
            
        # (current value, i+k-1 (index k forward))
        D.append((A[i], i + k - 1))
        
        # this is to start appending from k-1 onwards
        if i >= k - 1: 
            res.append(D[0][0])
           
        # if i=D[0][1] that means it matches i+k-1 and has been the min for k times
        if i == D[0][1]: 
            D.popleft()
            
    return res

if __name__ == "__main__":

    # time and space: O(n)
 
    print(MinSlidingWindow([4, 3, 2, 1, 5, 7, 6, 8, 9], 3))
    
    # 0. D = [(4,2)]
    #    i = 0
    #    res = []
    # 1. D = [(3,3)] - 4>3 
    #    i = 1
    #    res = []
    # 2. D = [(2,4)] - 3>2 
    #    i = 2 >= 2
    #    res = [2]
    # 3. D = [(1,5)] - 2>1 
    #    i = 3 >= 2
    #    res = [2,1]
    # 4. D = [(1,5),(5,6)] - 1<5
    #    i = 4 >= 2
    #    res = [2,1,1]
    # 5. D = [(5,6),(7,7)] - 5<7
    #    i = 5 >= 2
    #    res = [2,1,1,1]
    #    popleft
    # 6. D = [(6,8)] - 7>6 
    #    i = 6 >= 2
    #    res = [2,1,1,1,5]
    # pop left
    # 7. D = [(6,8),(8,9)] - 6<8 
    #    i = 7 >= 2
    #    res = [2,1,1,1,5,6]
    # 8. D = [(6,8),(8,9),(9,10)] - 8<9
    #    i = 8 >= 2
    #    res = [2,1,1,1,5,6,6]
    