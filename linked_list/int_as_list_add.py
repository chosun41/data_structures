from lll import LinkedList,Node

# add two numbers that are represented as linked lists
def add_two_numbers(L1, L2):
    
    final_ll = LinkedList()
    
    L1_curr = L1.head
    L2_curr = L2.head
    
    carry = 0
    
    while L1_curr or L2_curr or carry:
        val = carry + (L1_curr.data if L1_curr else 0) + (L2_curr.data if L2_curr else 0)
        L1_curr = L1_curr.next if L1_curr else None
        L2_curr = L2_curr.next if L2_curr else None
        
        final_ll.addNode(Node(val % 10))

        carry = val // 10
        
    return final_ll

if __name__ == "__main__":

    # naive: 
    # grade school algorithm
    # time: O(max(n,m)) - n,m length of two lists
    # space: O(1)
    
    l1 = LinkedList()
    l2 = LinkedList()
    
    node1 = Node(3)
    node2 = Node(1)
    node3 = Node(4)
    node4 = Node(7)
    node5 = Node(0)
    node6 = Node(9)
    
    l1.addNode(node1)
    l1.addNode(node2)
    l1.addNode(node3)
    l2.addNode(node4)
    l2.addNode(node5)
    l2.addNode(node6)

    print("\n")
    l1.print_list()
    
    print("\n")
    l2.print_list()
    
    print("\n")
    x=add_two_numbers(l1,l2)
    x.print_list()
