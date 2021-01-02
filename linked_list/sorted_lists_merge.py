from lll import LinkedList,Node

def merge_two_sorted_lists(L1,L2):

    # head of both lists
    curr_1 = L1.head
    curr_2 = L2.head
    
    # empty linked list
    new_ll = LinkedList()

    # traverse while still nodes and compare which the least to new_ll
    while curr_1 and curr_2:
        if curr_1.data <= curr_2.data:
            new_ll.addNode(Node(curr_1.data))    
            curr_1 = curr_1.next
        else:
            new_ll.addNode(Node(curr_2.data))  
            curr_2=curr_2.next

    # appends remaining nodes of L1 or L2
    if not curr_1:
        while curr_2:
            new_ll.addNode(Node(curr_2.data)) 
            curr_2=curr_2.next
    elif not curr_2:
        while curr_1:
            new_ll.addNode(Node(curr_1.data)) 
            curr_1 = curr_1.next

    # return the new list
    return new_ll

if __name__ == "__main__":
    
    # naive: append everything and sort in place
    # time: O(n+m)
    # space: O(1)
   
    l1 = LinkedList()
    l2 = LinkedList()

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    
    l1.addNode(node1)
    l2.addNode(node2)
    l1.addNode(node3)
    l2.addNode(node4)
    l1.addNode(node5)
    l2.addNode(node6)
    l1.addNode(node7)
    
    print("\n")
    l1.print_list()
    
    print("\n")
    l2.print_list()
    
    print("\n")
    x = merge_two_sorted_lists(l1,l2)
    x.print_list()