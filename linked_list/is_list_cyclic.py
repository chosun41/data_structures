from cll import LinkedList,Node

def has_cycle(L1: LinkedList):

    # start at same place
    fast = slow = L1.head
    
    while fast and fast.next:
        
        # increment by 1 and 2
        slow, fast = slow.next, fast.next.next
        print(f"current slow is {slow.data}")
        print(f"current fast is {fast.data}")
        
        if slow is fast:
            
            return slow.data
            break
            
    return None

if __name__ == "__main__":
    
    # naive: hash table to see which one revisted
    # case analysis
    
    ll = LinkedList()

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
    
    print(has_cycle(ll))