from lll import LinkedList,Node

# even list followed by odd list from original input
def even_odd_merge(L: LinkedList):
    
    curr = L.head
    final_ll = LinkedList()
    
    # if empty linked list return None
    if not curr:
        
        return None
    
    else:
        
        # if not empty linked list
        even_head = even_tail = Node(None)
        odd_head = odd_tail = Node(None)
        
        count = 0

        while curr:

            if count == 0:
                even_tail.next = curr
                even_tail = even_tail.next
            elif count == 1:
                odd_tail.next = curr
                odd_tail = odd_tail.next

            curr = curr.next

            # alternate between 0 and 1 (bitwise operation)
            count ^= 1

        # make sure odd_tail which is at end of final_ll is None
        # attach odd to even by connecting odd head to even tail
        # set final linkedlist to even head
        odd_tail.next = None
        even_tail.next = odd_head.next
        final_ll.head = even_head.next
        return final_ll

if __name__ == "__main__":
    
    # even list before odd list
    # first is index 0
    # time: O(n)
    # space: O(1)
   
    l1 = LinkedList()

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
    l1.addNode(node6)
    l1.addNode(node7)
    
    print("\n")
    x=even_odd_merge(l1)
    x.print_list()
