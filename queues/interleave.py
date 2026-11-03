from collections import deque

def interLeavingQueue(que):

    stk=[]
    deq = deque(que)
    halfsize=len(deq)//2

    for i in range(halfsize):
        stk.append(deq.popleft())

    print(stk)

    for i in range(halfsize):
        deq.append(stk.pop())

    print(stk,deq)

    for i in range(halfsize):
        deq.append(deq.popleft())

    print(stk,deq)

    for i in range(halfsize):
        stk.append(deq.popleft())

    print(stk,deq)

    for i in range(halfsize):
        deq.append(stk.pop())
        deq.append(deq.popleft())

    print(stk,deq)

    return deq
  
if __name__ == "__main__":
    
    # basically get the stack to a place where you can pop for first part of interleave
    # and remainder of queue you can dequeue to the end for second part of interleave

    # time: O(n)
    # space: O(n)

    que = [11,12,13,14,15,16,17,18,19,20,21,22]

    print(interLeavingQueue(que))
