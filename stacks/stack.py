# stack implented by an array
# can also do linkedlist

class Stack:
    def __init__(self, limit=10):
        self.limit= limit
        self.array = []
    def size(self):
        return len(self.array)
    def isEmpty(self):
        return len(self.array) == 0
    def isFull(self):
        return len(self.array) == self.limit
    def peek(self):
        if self.isEmpty():
            return None
        return self.array[-1]
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack Underflow")
        data = self.array.pop()
        return data
    def push(self, data):
        if self.isFull():
            self.resize()
#             raise Exception("Stack Overflow")
        self.array.append(data)
    # dynamically resize
    def resize(self):
        self.limit = 2*self.limit
        
if __name__ == "__main__":
    
    our_stack=Stack(5)
    our_stack.push(1)
    our_stack.push(21)
    our_stack.push(14)
    our_stack.push(31)
    our_stack.push(19)
    our_stack.push(3)
    our_stack.push(99)
    our_stack.push(9)
    print(our_stack.peek())
    print(our_stack.pop())
    print(our_stack.peek())
    print(our_stack.pop())
    print(our_stack.size())