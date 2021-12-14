class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L1, k):

    # start with two pointers at head
    first=L1
    second=L1

    # increment first pointer k times
    for _ in range(k):
        first = first.next

    # the second should be incremented up to the length left in list, which would be k away from the end
    while first.next:
        first, second = first.next, second.next
        
    # second points to the (k + 1)-th last node, deletes its successor.
    second.next = second.next.next
    return L1
    
if __name__ == "__main__":
    
    # naive: traverse two times, first to record length of list and to subtract k from it to see which element to stop at
    # the first is k up ahead, by the time it stops the second will be at kth last
    # time: O(n)
    # space: O(1)
   
    l1 = ListNode(1)
    l1.next=ListNode(2)
    l1.next.next=ListNode(3)
    l1.next.next.next=ListNode(4)
    l1.next.next.next.next=ListNode(5)
    l1.next.next.next.next.next=ListNode(6)
    l1.next.next.next.next.next.next=ListNode(7)
    
    x=remove_kth_last(l1,2)
    print(x.val)
    print(x.next.val)
    print(x.next.next.val)
    print(x.next.next.next.val)
    print(x.next.next.next.next.val)
    print(x.next.next.next.next.next.val)
