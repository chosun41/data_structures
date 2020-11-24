from lll import LinkedList,Node

# insert into ordered linked list by data value
def orderedInsert(L1, item):
    
    current = L1.head
    previous = None
    stop = False
    
    # traverse until you reach where data > item
    # at this point stop is True and youll have the current and previous pointers
    while current != None and not stop:
        if current.get_data() > item:
            stop = True
        else:
            previous = current
            current = current.get_next()

    temp = Node(item)
    
    # if empty linked list
    if previous == None:
        temp.set_next(self.head)
        L1.head = temp
    # if not empty linked list 
    # set temp next to current
    # and previous next should be temp
    else:
        temp.set_next(current)
        previous.set_next(temp)
    
    return L1

if __name__ == "__main__":

    # two pointers previous and current with a special condition for empty linkedlist
    # time: O(n)
    # space: O(1)
    
    l1 = LinkedList()
    
    node1 = Node(1)
    node2 = Node(2)
    node4 = Node(4)
    node5 = Node(5)
    
    l1.addNode(node1)
    l1.addNode(node2)
    l1.addNode(node4)
    l1.addNode(node5)

    print("\n")
    x=orderedInsert(l1,3)
    x.print_list()

