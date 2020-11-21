import sys
sys.path.append('../stacks')
from stack import Stack
from queues import Queue

def reverseQueueFirstKElements(que, k):
    
     stk = Stack()
     
     # disqualifying factors
     if que == None or k > que.size():
         return
        
     # push for up to k, push k deq's to stack
     for i in range(k):
          stk.push(que.dequeue())
     
     # pass stuff from stack at end of queue
     while not stk.isEmpty():
          que.enqueue(stk.pop())
     
     # pass everything from start to end of queue for non k items
     for i in range(0, que.size() - k):
          que.enqueue(que.dequeue())

if __name__ == "__main__":
    
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

    reverseQueueFirstKElements(que, 4) 

    while not que.isEmpty():
        print(que.dequeue())