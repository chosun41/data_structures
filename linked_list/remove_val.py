class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

def removeElements(head, val):
    sentinel = ListNode(0)
    sentinel.next = head

    prev, curr = sentinel, head
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next

    return sentinel.next

if __name__ == '__main__':
    
    # time: O(n)
    # space: O(1)

    x=ListNode(1)
    x.next=ListNode(2)
    x.next.next=ListNode(6)
    x.next.next.next=ListNode(3)
    x.next.next.next.next=ListNode(4)
    x.next.next.next.next.next=ListNode(5)
    x.next.next.next.next.next.next=ListNode(6)
    y=removeElements(x,1)
    print(y.val)
    print(y.next.val)
    print(y.next.next.val)
    print(y.next.next.next.val)
    print(y.next.next.next.next.val)
    print(y.next.next.next.next.next.val)
