class Node:
    
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

# pivot a linked lsit around a number x
def list_pivoting(l,x):

    # 3 nodes with head and iteration pointers(tail)
    # 1 for less, equal, and greater
    less_head = less_iter = Node()
    equal_head = equal_iter = Node()
    greater_head = greater_iter = Node()
    
    # pointer to input list head
    curr = l
    
    # Populates the three lists
    # based on comparisons to input list
    # add node to node lists and traverse iteration pointers to corresponding next
    while curr:
        if curr.val < x:
            less_iter.next = curr
            less_iter = less_iter.next
        elif curr.val == x:
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
    return less_head.next

if __name__ == "__main__":

    # naive: maintain 3 lists and create new nodes for each. 
    # instead attach existing nodes to chain
    # time: O(n)
    # space: O(1)
    
    ll = Node(3)
    ll.next = Node(2)
    ll.next.next = Node(2)
    ll.next.next.next = Node(11)
    ll.next.next.next.next = Node(7)
    ll.next.next.next.next.next = Node(5)
    ll.next.next.next.next.next.next = Node(11)

    x=list_pivoting(ll,7)
    print(x.val)
    print(x.next.val)
    print(x.next.next.val)
    print(x.next.next.next.val)
    print(x.next.next.next.next.val)
    print(x.next.next.next.next.next.val)
    print(x.next.next.next.next.next.next.val)
