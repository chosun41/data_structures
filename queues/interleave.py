import sys
sys.path.append('../stacks')
from stack import Stack
from queues import Queue

def interLeavingQueue(que):
    
     # get size of queue and cut half
     stk = Stack()
     halfSize = que.size() // 2
    
     # push first half onto stack 
     # stack - 11,12,13,14,15,16
     # queue - 17,18,19,20,21,22
     for i in range(0, halfSize):
          stk.push(que.dequeue())

     # empty out stack at end of queue
     # stack - 
     # queue - 17,18,19,20,21,22,16,15,14,13,12,11
     while not stk.isEmpty():
          que.enqueue(stk.pop())
        
     # first half to end
     # stack - 
     # queue - 16,15,14,13,12,11,17,18,19,20,21,22
     for i in range(0, halfSize):
          que.enqueue(que.dequeue())

     # first half to end
     # stack - 16,15,14,13,12,11
     # queue - 17,18,19,20,21,22
     for i in range(0, halfSize):
          stk.push(que.dequeue())
        
     # interleave
     # stack - 
     # queue - 11,17,12,18,13,19,14,20,15,21,16,22
     while not stk.isEmpty():
          que.enqueue(stk.pop())
          que.enqueue(que.dequeue())
  
if __name__ == "__main__":
    
    # basically get the stack to a place where you can pop for first part of interleave
    # and remainder of queue you can dequeue to the end for second part of interleave
    
    # time: O(n)
    # space: O(n)
    
    que = Queue(20)
    que.enqueue(11)
    que.enqueue(12)
    que.enqueue(13)
    que.enqueue(14)
    que.enqueue(15)
    que.enqueue(16)
    que.enqueue(17)
    que.enqueue(18)
    que.enqueue(19)
    que.enqueue(20)
    que.enqueue(21)
    que.enqueue(22)

    interLeavingQueue(que)  

    while not que.isEmpty():
        print(que.dequeue())   
