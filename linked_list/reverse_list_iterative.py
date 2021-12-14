class ListNode:
    def __init__(self,val=None):
        self.val=val
        self.next=None

def reverseList(L1):
    
    prev = None
    current = L1

    # traverse list
    # set previous node (last) to current next
    # new last is current
    # current is next node
    while current:
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode

    # set the head to the very last node
    L1 = prev
    
    return L1
    
if __name__ == "__main__":
    
    # uses three pointers one for current, last, and nextnode
    # time: O(n)
    # space: O(1)
    
    linkedlst = ListNode(1)
    linkedlst.next = ListNode(2)
    linkedlst.next.next = ListNode(3)
    linkedlst.next.next.next = ListNode(4)
    
    x = reverseList(linkedlst)
    print(x.val)
    print(x.next.val)
    print(x.next.next.val)
    print(x.next.next.next.val)
    
    # last=None,curr=1->2->3->4
    # next=2->3->4, curr=1,last=1,curr=2->3->4
    # next=3->4,curr=2->1,last=2->1,curr=3->4
    # next=4,curr=3->2->1,last=3->2->1,curr=4
    # next=None,curr=4->3->2->1,last=4->3->2-1,curr=None