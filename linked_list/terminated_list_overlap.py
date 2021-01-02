from lll import LinkedList,Node

def overlapping_no_cycle_lists(L1,L2):

    # makes sure that L1 is supposed to refer to the shorter length list
    if L1.length() > L2.length():
        L1, L2 = L2, L1  
        
    # Advances the longer list to get equal length lists.
    l2_curr = L2.head
    l1_curr = L1.head
    
    for _ in range(abs(L1.length() - L2.length())):
        l2_curr = l2_curr.next

    while l1_curr and l2_curr and l1_curr is not l2_curr:
        l1_curr, l2_curr = l1_curr.next, l2_curr.next
    return l1_curr.data  # None implies there is no overlap between l0 and l1.
    
if __name__ == "__main__":
    
    # naive: hash table to see which one revisted or compare every node pointer 0(mn)
    # need to advance longer list (L2) by diff in lists
    # time: O(n)
    # space: O(1)
    
    l1 = LinkedList()
    l2 = LinkedList()

    node0 = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    
    l1.addNode(node0)
    l1.addNode(node1)
    l1.addNode(node2)
    l1.addNode(node3)
    l1.addNode(node4)
    l1.addNode(node5)
    
    print("\n")
    l1.print_list()
    print(l1.length())
    
    l2.addNode(node6)
    l2.addNode(node7)
    l2.addNode(node3)
    l2.addNode(node4)
    l2.addNode(node5)
    
    print("\n")
    l2.print_list()
    print(l2.length())
    
    print("\n")
    print(overlapping_no_cycle_lists(l1,l2))