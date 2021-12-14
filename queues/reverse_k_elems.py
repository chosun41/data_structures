from collections import deque

def reverseQueueFirstKElements(que, k):

    stk = []
    deq = deque(que)
    
    for i in range(k):
        stk.append(deq.popleft())

    print(stk)
    
    for i in range(k):
        deq.append(stk.pop())

    for i in range(len(deq)-k):
        deq.append(deq.popleft())

    return deq

if __name__ == "__main__":
    
    # time: O(n)
    # space: O(n)
    que = [20,11,12,13,14,15,16,17,18]

    print(reverseQueueFirstKElements(que, 4))