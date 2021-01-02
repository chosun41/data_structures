from lll import LinkedList,Node

# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L1, k):

    # start with two pointers at head
    first=L1.head
    second=L1.head

    # increment first pointer k times
    for _ in range(k):
        first = first.next

    # the second should be incremented up to the length left in list, which would be k away from the end
    while first.next!=None:
        first, second = first.next, second.next
        
    # second points to the (k + 1)-th last node, deletes its successor.
    second.next = second.next.next
    return L1
    
if __name__ == "__main__":
    
    # naive: traverse two times, first to record length of list and to subtract k from it to see which element to stop at
    # the first is k up ahead, by the time it stops the second will be at kth last
    # time: O(n)
    # space: O(1)
   
    l1 = LinkedList()

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    
    l1.addNode(node1)
    l1.addNode(node2)
    l1.addNode(node3)
    l1.addNode(node4)
    l1.addNode(node5)
    l1.addNode(node6)
    l1.addNode(node7)
    
    x=remove_kth_last(l1,2)
    print("\n")
    x.print_list()