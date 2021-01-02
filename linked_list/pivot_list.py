from lll import LinkedList,Node

# pivot a linked lsit around a number x
def list_pivoting(l,x):

    # 3 nodes with head and iteration pointers(tail)
    # 1 for less, equal, and greater
    less_head = less_iter = Node(None)
    equal_head = equal_iter = Node(None)
    greater_head = greater_iter = Node(None)
    
    # empty linkedlist
    new_ll=LinkedList()
    
    # pointer to input list head
    curr = l.head
    
    # Populates the three lists
    # based on comparisons to input list
    # add node to node lists and traverse iteration pointers to corresponding next
    while curr:
        if curr.data < x:
            less_iter.next = curr
            less_iter = less_iter.next
        elif curr.data == x:
            equal_iter.next = curr
            equal_iter = equal_iter.next
        else:  # curr.data > x.
            greater_iter.next = curr
            greater_iter = greater_iter.next
        curr = curr.next
        
    # Combines the three lists.
    # attach greater to equal and attach equal to less, return 
    greater_iter.next = None
    equal_iter.next = greater_head.next
    less_iter.next = equal_head.next
    
    new_ll.head = less_head.next
    return new_ll

if __name__ == "__main__":

    # naive: maintain 3 lists and create new nodes for each. 
    # instead attach existing nodes to chain
    # time: O(n)
    # space: O(1)
    
    ll = LinkedList()

    ll.print_list()
    node1 = Node(3)
    node2 = Node(2)
    node3 = Node(2)
    node4 = Node(11)
    node5 = Node(7)
    node6 = Node(5)
    node7 = Node(11)
    
    ll.addNode(node1)
    ll.addNode(node2)
    ll.addNode(node3)
    ll.addNode(node4)
    ll.addNode(node5)
    ll.addNode(node6)
    ll.addNode(node7)
    ll.print_list()
    
    print("\n")
    x=list_pivoting(ll,7)
    x.print_list()
