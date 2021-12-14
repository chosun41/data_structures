class ListNode:
    def __init__(self,val=None):
        self.val=val
        self.next=None
        
# even list followed by odd list from original input
def even_odd_merge(L):
    
    curr = L
    
    # if empty linked list return None
    if not curr:
        
        return None
    
    else:
        
        # if not empty linked list
        even_head = even_tail = ListNode()
        odd_head = odd_tail = ListNode()
        
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
        even_tail.next = odd_head.next
        return even_head.next

if __name__ == "__main__":
    
    # even list before odd list
    # first is index 0
    # time: O(n)
    # space: O(1)
   
    l1 = ListNode(0)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    l1.next.next.next = ListNode(3)
    l1.next.next.next.next = ListNode(4)
    l1.next.next.next.next.next = ListNode(5)
    l1.next.next.next.next.next.next = ListNode(6)
    l1.next.next.next.next.next.next.next = ListNode(7)
    
    x = even_odd_merge(l1)
    print(x.val)
    print(x.next.val)
    print(x.next.next.val)
    print(x.next.next.next.val)
    print(x.next.next.next.next.val)
    print(x.next.next.next.next.next.val)
    print(x.next.next.next.next.next.next.val)
    print(x.next.next.next.next.next.next.next.val)
    
