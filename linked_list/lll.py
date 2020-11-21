# Node of a Singly Linked List
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

# class for defining a linked list   
class LinkedList:
     
    # initializing a list
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head==None
    
    def length(self):
        current=self.head
        count = 0
        while current:
            count+=1
            current=current.next
        return count

    # method to add a node in the linked list -
    def addNode(self, node):
        if self.is_empty():
            self.addBeg(node)
        else:
            self.addLast(node)           
         
    # method to add a node at the beginning of the list with a data - 
    # connect a newnode before the current head and make it the current head
    def addBeg(self, node):
        newNode = node
        newNode.next = self.head
        self.head = newNode
         
    # method to add a node after the node having the data=data. The data of the new node is value2 -
    # traverse until data matches - node.next to current.next and current.next to the new node
    # if you reach end, raise exception
    def addAfterValue(self, data, node):
        newNode = node
        current = self.head
         
        while current.next != None or current.data != data:
            if current.data == data:
                newNode.next = current.next
                current.next = newNode
                return
            else:
                current = current.next
             
        raise Exception("The data provided is not present")
                 
    # method to add a node at a particular position
    def addAtPos(self, pos, node):
        count = 0
        current = self.head
        previous = self.head
         
        if pos > self.length() or pos < 0:
            print("The position does not exist. Please enter a valid position")
        else:
            while current.next != None or count < pos:
                count = count + 1
                if count == pos:
                    previous.next = node
                    node.next = current
                    return
                     
                else:
                    previous = current
                    current = current.next       
                 
    # method to add a node at the end of a list -
    # start with the head and traverse to end of ll and set last node's next to parameter node object
    def addLast(self, node):
        current = self.head
         
        while current.next != None:
            current = current.next
 
        newNode = node
        newNode.next = None
        current.next = newNode 
     
    # method to delete the first node of the linked list -
    # detach head by setting the head to head.next
    def deleteBeg(self):
        if self.is_empty():
            raise Exception("can't delete from an empty list")
        else:
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
             
            while current.next != None:
                previous = current
                current = current.next
                 
            previous.next = None           
         
    # method to delete a node after the node having the given data
    def deleteValue(self, data):
        current = self.head
        previous = self.head
         
        while current.next != None or current.data != data:
            if current.data == data:
                previous.next = current.next
                return
                    
            else:
                previous = current
                current = current.next
                 
        print("The data provided is not present")                 
         
    # method to delete a node at a particular position
    def deleteAtPos(self, pos):
        count = 0
        current = self.head
        previous = self.head
 
        if pos > self.length or pos < 0:
            print("The position does not exist. Please enter a valid position")
        # to deletle the first position of the linkedlist
        elif pos == 1:
            self.delete_beg()
        else:        
            while current.next != None or count < pos:
                count = count + 1
                if count == pos:
                    previous.next = current.next
                    return
                else:
                    previous = current
                    current = current.next
    # get class functions
     
    # returns the first element of the list
    def getFirst(self):
        if self.is_empty():
            raise Exception("The list is empty")
        else:
            return self.head.data
     
    # returns the last element of the list
    def getLast(self):
         
        if self.is_empty():
            raise Exception("The list is empty")
        else:
            current = self.head
             
            while current.next != None:
                current = current.next
                 
            return current.data
     
    # returns node at any position -
    # check if valid position
    # keep traversing until you match position and raise counter count
    def getAtPos(self, pos):
        count = 0
        current = self.head
         
        if pos > self.length() or pos < 0:
            raise Exception("The position does not exist. Please enter a valid position")
        else:
            while current.next != None or count < pos:
                count += 1
                if count == pos:
                    return current.data
                else:
                    current = current.next
 
                     
    # method to print the whole list
    def print_list(self):
        current = self.head
        if not current:
            print("empty linked list")
        while current:
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
    node7 = Node(7)
    
    ll.addNode(node1)
    ll.addNode(node2)
    ll.addNode(node3)
    ll.addNode(node4)
    ll.addNode(node5)
    ll.deleteLast()
    ll.print_list()
    
    print("\n")
    ll.addBeg(node0)
    ll.print_list()
    
    print("\n")
    print(ll.getFirst())
    print(ll.getLast())
    print(ll.getAtPos(2))
    
    print("\n")
    ll.addAtPos(2,node6)
    ll.addAfterValue(6,node7)
    ll.print_list()
    
    print("\n")
    print(ll.length())