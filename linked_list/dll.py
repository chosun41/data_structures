# doubly linked list

class Node:
    # Constructor to initialize data
    # If data is not given by user,its taken as None 
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
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
    # method for setting the next field of the node
    def setPrev(self, prev):
        self.prev = prev
       # method for getting the next field of the node    
    def getPrev(self):
        return self.prev
    # returns true if the node points to another node
    def hasPrev(self):
            return self.prev != None	    
    # __str__ returns string equivalent of Object
    def __str__(self):
        return "Node[Data = %s]" % (self.data,)

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def is_empty(self):
        return self.head==None

    # method to add a node in the linked list -
    def addNode(self, node):
        if self.is_empty():
            self.addBeg(node)
        else:
            self.addLast(node)           
         
    # method to add a node at the beginning of the list with a data  
    def addBeg(self, node):
        
        newNode = node
        
        if self.is_empty():
            # set node next to head and prev to None
            # set head and tail to node
            newNode.next = self.head
            newNode.prev = None
            self.head = self.tail = newNode
        else:
            # set node next to head and prev to None
            # set head prev to node and make the node the new head
            newNode.next = self.head
            newNode.prev = None
            self.head.prev=newNode
            self.head = newNode            
                 
    # method to add a node at the end of a list 
    def addLast(self, node):

        if self.is_empty():
            # set node next to head and prev to None
            # set head and tail to node
            newNode.next = self.head
            newNode.prev = None
            self.head = newNode
            self.tail = newNode
        else:
            # no need to traverse since you have a tail
            # set node next to None and node prev to current
            # attach current next to node and node is new tail
            newNode = node
            newNode.next = None
            newNode.prev = self.tail
            self.tail.next = newNode 
            self.tail = newNode            
     
    # method to delete the first node of the linked list 
    def deleteBeg(self):
        
        if self.is_empty():
            raise Exception("can't delete from an empty list")
        else:
            # set head to head next and new head prev to None
            self.head = self.head.next
            self.head.prev = None
     
    # method to delete the last node of the linked list 
    def deleteLast(self):
         
        if self.is_empty():
            raise Exception("can't delete from an empty list")
        else:    
            self.tail = self.tail.prev
            self.tail.next=None    

    def fwd_print(self):
        
        current = self.head
        if not current:
            print("empty linked list")
        else:
            while (current != None):
                print (current.data) 
                current = current.next

    def rev_print(self):
        
        current = self.tail
        if not current:
            print("empty linked list")
        else:
            while (current != None):
                print (current.data)
                current = current.prev

if __name__ == '__main__':
    
    ll = LinkedList()
    print(ll.is_empty())
    
#     ll.deleteBeg()

    print("\n")
    ll.fwd_print()
    print("\n")
    ll.rev_print()
    
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node0 = Node(0)
    node6 = Node(6)
    
    ll.addNode(node1)
    ll.addNode(node2)
    ll.addNode(node3)
    ll.addNode(node4)
    ll.addNode(node5)
    ll.addBeg(node0)
    print("\n")
    ll.fwd_print()
    print("\n")
    ll.rev_print()
    
    print("\n")
    print(ll.head.data)
    print(ll.tail.data)
    
    print("\n")
    ll.addLast(node6)
    print("\n")
    ll.fwd_print()
    print("\n")
    ll.rev_print()
    
    print("\n")
    print(ll.head.data)
    print(ll.tail.data)
    
    print("\n")
    ll.deleteBeg()
    print("\n")
    ll.fwd_print()
    print("\n")
    ll.rev_print()
    
    print("\n")
    print(ll.head.data)
    print(ll.tail.data)
    
    print("\n")
    ll.deleteLast()
    print("\n")
    ll.fwd_print()
    print("\n")
    ll.rev_print()
    
    print("\n")
    print(ll.head.data)
    print(ll.tail.data)
