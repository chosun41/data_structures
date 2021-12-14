class ListNode:
    def __init__(self,val=None):
        self.val=val
        self.next=None

# add two numbers that are represented as linked lists
def add_two_numbers(L1, L2):
    
    final_ll = ListNode()
    head = final_ll
    
    L1_curr = L1
    L2_curr = L2
    
    carry = 0
    
    while L1_curr or L2_curr or carry:
        val = carry + (L1_curr.val if L1_curr else 0) + (L2_curr.val if L2_curr else 0)
        L1_curr = L1_curr.next if L1_curr else None
        L2_curr = L2_curr.next if L2_curr else None
        
        head.next = ListNode(val%10)
        head = head.next

        carry = val // 10
        
    return final_ll.next

if __name__ == "__main__":

    # naive: 
    # grade school algorithm
    # time: O(max(n,m)) - n,m length of two lists
    # space: O(n)
    
    l1 = ListNode(3)
    l1.next = ListNode(1)
    l1.next.next=ListNode(4)
    l2 = ListNode(7)
    l2.next=ListNode(0)
    l2.next.next=ListNode(9)
    
    x=add_two_numbers(l1,l2)
    print(x.val)
    print(x.next.val)
    print(x.next.next.val)
    print(x.next.next.next.val)
