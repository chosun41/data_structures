import sys
sys.path.append('../stacks')
from stack import Stack

class Queue:
    
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
        
    def enqueue(self,element):
        self.s1.push(element)
        
    def dequeue(self):
        if self.s2.isEmpty():
            #transfers elements in _enq to _deq
            while not self.s1.isEmpty():
                self.s2.push(self.s1.pop())
        return self.s2.pop()
    
if __name__ == "__main__":
    
    # only when s2 is empty pop and push everything from s1
    # else just pop s2
    # anything pushed is not needed until s2 is empty
    
    q=Queue()
    q.enqueue(0)
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())

    