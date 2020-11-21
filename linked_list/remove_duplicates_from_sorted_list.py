from lll import LinkedList,Node

def remove_duplicates(L):

    it = L.head
    
    while it:
        
        # Uses next_distinct to find the next distinct value.
        next_distinct = it.next
        
        # just keep reattaching next_distinct while data value repeats
        while next_distinct and next_distinct.data == it.data:
            next_distinct = next_distinct.next
            
        it.next = next_distinct
        
        it = next_distinct
     
    # return list amended
    return L

if __name__ == "__main__":
    
    # naive: hash table while traversing
    # time: O(n)
    # space: O(1)
   
    l1 = LinkedList()

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(2)
    node4 = Node(3)
    node5 = Node(4)
    node6 = Node(4)
    node7 = Node(4)
    node8 = Node(5)
    
    l1.addNode(node1)
    l1.addNode(node2)
    l1.addNode(node3)
    l1.addNode(node4)
    l1.addNode(node5)
    l1.addNode(node6)
    l1.addNode(node7)
    l1.addNode(node8)
    
    print("\n")
    l1.print_list()
    
    x=remove_duplicates(l1)
    print("\n")
    x.print_list()