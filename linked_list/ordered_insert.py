class ListNode:
    def __init__(self,val=None):
        self.val=val
        self.next=None

# insert into ordered linked list by data value
def orderedInsert(L1, item):

    sentinel = ListNode()
    sentinel.next=L1
    
    current = L1
    previous = sentinel
    stop = False
    
    # traverse until you reach where data > item
    # at this point stop is True and youll have the current and previous pointers
    while current and not stop:
        if current.val > item:
            stop = True
        else:
            previous = current
            current = current.next

    temp = ListNode(item)

    temp.next = current
    previous.next = temp
    
    return sentinel.next

if __name__ == "__main__":

    # two pointers previous and current with a special condition for empty linkedlist
    # time: O(n)
    # space: O(1)
    
    l1 = ListNode(1)
    l1.next=ListNode(2)
    l1.next.next=ListNode(4)
    l1.next.next.next=ListNode(5)

    x=orderedInsert(l1,0)
    print(x.val)
    print(x.next.val)
    print(x.next.next.val)
    print(x.next.next.next.val)


