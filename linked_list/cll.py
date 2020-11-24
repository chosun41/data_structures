# circular linked list

class Node:
    # constructor
    def __init__(self, data):
        self.data = data
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

# class for defining a linked list -
# doing for single linked list
class LinkedList:
     
    # initializing a list
    def __init__(self):
        self.head = None
        self.tail= None

    def is_empty(self):
        return self.head==None
    
    def length(self):
        current=self.head
        current=current.next
        count = 1
        while current!=self.head:
            count+=1
            current=current.next
        return count

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
            #If list is empty, both head and tail would point to new node
            # set newnode next to the head
            self.head = newNode    
            self.tail = newNode    
            newNode.next = self.head    
        else:    
            # set next of newnode to head, make it the new head, move tail next to new head
            newNode.next = self.head
            self.head = newNode
            self.tail.next= self.head   

    # method to add a node at the end of a list 
    def addLast(self, node):
        
        newNode = node
        
        if self.is_empty():    
            # if list is empty, both head and tail would point to new node
            # set newnode next to the head
            self.head = newNode    
            self.tail = newNode    
            newNode.next = self.head  
        else:
            # traverse until you reach tail
            # make newnode next the head
            # current next is new Node and repoint tail to the newnode
                
            newNode.next = self.head
            self.tail.next = newNode
            self.tail=newNode        
     
    # method to delete the first node of the linked list 
    def deleteBeg(self):
        
        if self.is_empty():
            raise Exception("can't delete from an empty list")
        else:
            # point tail to head next
            # point head to head next
            self.tail.next = self.head.next
            self.head = self.head.next
     
    # method to delete the last node of the linked list - 
    # keep tracker for current and node just before current
    # traverse to the end and detach the current by setting previous.next to None
    def deleteLast(self):
         
        if self.is_empty():
            raise Exception("can't delete from an empty list")
        else:
            current = self.head
            previous = self.head
             
            # only need to traverse because you need to access previous to last
            while current.next != self.head:
                previous = current
                current = current.next
                 
            previous.next = self.head
            self.tail = previous
                     
    # method to print the whole list
    def print_list(self):
        current = self.head
        if self.is_empty():
            print("empty linked list")
        else:
            print(current.data)
            current = current.next
            
            # need to print current and increment one to use the while statement below
            while current!=self.head:
                print(current.data)
                current = current.next 

if __name__ == "__main__":
    
    ll = LinkedList()
    print(ll.is_empty())
    
#     ll.deleteBeg()

    ll.print_list()
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
    ll.print_list()
    
    print("\n")
    print(ll.head.data)
    print(ll.tail.data)
    print(ll.tail.next.data)
    
    print("\n")
    ll.addLast(node6)
    ll.print_list()
    
    print("\n")
    print(ll.head.data)
    print(ll.tail.data)
    print(ll.tail.next.data)
    
    print("\n")
    ll.deleteBeg()
    ll.print_list()
    
    print("\n")
    print(ll.head.data)
    print(ll.tail.data)
    print(ll.tail.next.data)
    
    print("\n")
    ll.deleteLast()
    ll.print_list()
    
    print("\n")
    print(ll.head.data)
    print(ll.tail.data)
    print(ll.tail.next.data)
    