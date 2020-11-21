class Node:
    # constructor
    def __init__(self):
        self.data = None
        self.next = None
        # method for setting the data field of the node    
    def set_data(self, data):
        self.data = data
    # method for getting the data field of the node   
    def get_data(self):
        return self.data
      # method for setting the next field of the node
    def set_next(self, next):
        self.next = next
       # method for getting the next field of the node    
    def get_next(self):
        return self.next
    # returns true if the node points to another node
    def has_next(self):
        return self.next != None

class Stack(object):
    
    def __init__(self, data=None):
        self.head = None
        if data:
            for data in data:
                self.push(data)

    def push(self, data):
        temp = Node()
        temp.set_data(data)
        temp.set_next(self.head)
        self.head = temp

    def pop(self):
        if self.head is None:
            raise IndexError
        temp = self.head.get_data()
        self.head = self.head.get_next()
        return temp
    
    def peek(self):
        if self.head is None:
            raise IndexError
        return self.head.get_data()

if __name__ == "__main__":
    
    # head is actually the top of the stack (LIFO)
    our_list = ["first", "second", "third", "fourth"]
    our_stack = Stack(our_list)
    print(our_stack.pop())
    print(our_stack.peek())
    print(our_stack.pop())
    print(our_stack.peek())
    print(our_stack.pop())
