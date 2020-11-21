from lll import LinkedList,Node

def reverseList(L1):
    
    last = None
    current = L1.head

    # traverse list
    # set previous node (last) to current next
    # new last is current
    # current is next node
    while current:
        nextNode = current.get_next()
        current.set_next(last) 
        last = current
        current = nextNode

    # set the head to the very last node
    L1.head = last
    
    return L1
    
if __name__ == "__main__":
    
    # uses three pointers one for current, last, and nextnode
    # time: O(n)
    # space: O(1)
    
    linkedlst = LinkedList()
    linkedlst.addNode(Node(1))
    linkedlst.addNode(Node(2))
    linkedlst.addNode(Node(3))
    linkedlst.addNode(Node(4))
    
    x = reverseList(linkedlst)
     
    x.print_list()
