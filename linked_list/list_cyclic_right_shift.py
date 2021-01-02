from cll import LinkedList,Node

# right shift linked list by k nodes with new head and tail
def cyclically_right_shift_list(L, k):

    n=L.length()

    k %= n
    if k == 0:
        return L

    curr = L.tail
    
    steps_to_new_head = k
    
    while steps_to_new_head:
        steps_to_new_head -= 1
        curr = curr.next

    L.tail = curr
    L.head = L.tail.next

    return L
    
if __name__ == "__main__":

    # naive: hash table to see which one revisted
    # time: O(n)
    # space: O(1)
    
    ll = LinkedList()

    ll.print_list()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node0 = Node(0)
    
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
    x=cyclically_right_shift_list(ll,2)
    x.print_list()
    
    print("\n")
    print(x.head.data)
    print(x.tail.data)
    print(x.tail.next.data)